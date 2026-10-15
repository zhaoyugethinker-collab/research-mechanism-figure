#!/usr/bin/env python3
"""Read-only native-object inventory. This does not prove GUI editability or science."""
from pathlib import Path
import argparse
import json
import sys
import zipfile
import xml.etree.ElementTree as ET

NS={'p':'http://schemas.openxmlformats.org/presentationml/2006/main',
    'a':'http://schemas.openxmlformats.org/drawingml/2006/main'}

def inspect(path):
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise ValueError('ZIP CRC check failed')
        names=archive.namelist()
        slides=sorted(n for n in names if n.startswith('ppt/slides/slide') and n.endswith('.xml') and '/_rels/' not in n)
        if not slides:
            raise ValueError('No slide XML parts found')
        rows=[]
        for part in slides:
            root=ET.fromstring(archive.read(part))
            shapes=root.findall('.//p:sp',NS)
            textboxes=[s for s in shapes if (prop:=s.find('p:nvSpPr/p:cNvSpPr',NS)) is not None and prop.get('txBox')=='1']
            row={'slide':part,'native_shapes':len(shapes),'groups':len(root.findall('.//p:grpSp',NS)),
                 'textboxes':len(textboxes),'freeforms':len(root.findall('.//a:custGeom',NS)),
                 'connectors':len(root.findall('.//p:cxnSp',NS)),'pictures':len(root.findall('.//p:pic',NS)),
                 'image_references':len(root.findall('.//a:blip',NS))}
            rows.append(row)
        media=len([n for n in names if n.startswith('ppt/media/') and not n.endswith('/')])
        zero=media==0 and all(r['pictures']==0 and r['image_references']==0 for r in rows)
        return {'slides':rows,'embedded_media_files':media,'zero_images':zero,
                'scope':'OOXML inventory only; counts overlap. GUI edit/save/reopen and scientific review are separate checks.'}

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pptx',type=Path)
    parser.add_argument('--require-zero-images',action='store_true')
    args=parser.parse_args(argv)
    try:
        result=inspect(args.pptx)
    except (OSError,ValueError,zipfile.BadZipFile,ET.ParseError) as exc:
        print(json.dumps({'status':'ERROR','error':str(exc)},ensure_ascii=False))
        return 1
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 2 if args.require_zero_images and not result['zero_images'] else 0

if __name__=='__main__':
    sys.exit(main())
