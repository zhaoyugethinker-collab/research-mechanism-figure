# Editable PPT redraw from a mechanism image

Use this route when the user supplies a mechanism image and asks for a PowerPoint that can be edited object by object. The image is a layout reference; the confirmed relationship table is the authority for labels and arrows. A bitmap inside a slide is a reference layer, not an editable result.

## 1. Establish the redraw inventory

Record each visible item before drawing:

|Item|PPT object|Text or label|Relationship / endpoint|Evidence or uncertainty|
|---|---|---|---|---|
|Cell or compartment|Native shape or freeform|Separate text box|Contains or borders specified molecules|Confirm location|
|Molecule / receptor|Native shape|Separate text box|Attached to cell or membrane|Confirm identity|
|Arrow / inhibition|Connector, line, or native arrow|Optional separate label|Named start and end objects|Confirm direction and meaning|
|Outcome|Native shape|Separate text box|Follows supported relation|Avoid universal claims|

If a label, edge, or endpoint is unreadable, mark it as unresolved. Ask for a higher resolution source or a human decision instead of guessing. Do not copy a published illustration without permission.

## 2. Build native objects

- Choose slide size, object order, positions, colors, and readable text sizes from the reference image.
- Use actual PowerPoint/Impress shapes and text boxes for cells, compartments, labels, and result boxes. Use editable connectors or lines for relationships. Do not flatten the group into a PNG or a single SVG image.
- Keep ligand–receptor binding separate from downstream activating or inhibitory relations. Attach every line to the intended objects and make arrowheads or T-bars unambiguous.
- The original image may be placed temporarily as a reference layer during reconstruction, then removed from the deliverable slide. If it remains, disclose it and do not count it as editable content.
- A model or conversion tool may propose object positions, but confirmed science controls labels and relationships.

## 3. Export and check

Deliver the PPTX plus a rendered preview. Include an object inventory with counts of text boxes, native shapes, lines/connectors, and embedded images. Inspect the file structure; zero embedded images is a useful target for a fully native redraw, but structure counts alone do not prove usable editing.

In PowerPoint or Impress, perform three separate actions on the final file: change a label, move a node, and select or adjust an arrow. Save, close, reopen, and check that the edits persist. Record which actions passed. If desktop interaction cannot be performed, mark the result `PARTIAL — object structure checked, GUI editability pending`.

When no suitable PPT authoring tool is available, provide the relationship table, object inventory, and redraw instructions. State plainly that no editable PPTX was produced.
