# 山竹科研机制图 Skill

`research-mechanism-figure` · v0.2 · Agent Skills 格式

这套 Skill 帮研究者把论文、笔记、已确认的机制关系或自绘草图整理成有依据的机制图，并在可用工具支持下重绘为 **文字、节点、箭头可分别编辑** 的 PPT 对象。

它提供工作流程、Prompt、关系表与编辑性检查。**当前版本没有通用的一键“图片转可编辑 PPT”转换器**。如果使用图像转换工具或原生形状重绘，需要检查实际 PPT 对象；把 PNG 放进一页 PPT 不算完成转换。

## 第二期：亚细胞级机制图

对应文章：**如何使用GPT和Codex画亚细胞级机制图？**

从膜、胞质到细胞核，用关系表、原创结构图和风格卡约束生成，再做定向修正与复检。需要PPT时，进一步重绘为原生文字、细胞结构和箭头。

- [第二期完整案例与复跑入口](examples/ifng-stat1-pdl1/README.md)
- [实际使用的A/B/C提示词](examples/ifng-stat1-pdl1/prompts/)
- [原创结构草图](examples/ifng-stat1-pdl1/structure-guide.png)与[风格卡](examples/ifng-stat1-pdl1/style-guide.png)
- [换题输入模板](prompts/subcellular-input-template.md)、[定向修正模板](prompts/targeted-edit.md)
- [原生可编辑PPT重绘指令](prompts/native-ppt-redraw.md)
- [三版封面提示词](prompts/covers/README.md)

本轮A/B/C各3次，C为B的配对编辑：两次改善、一次退化。原生PPT另做C1重绘，775个原生叶对象、0图片对象，已在PowerPoint副本完成改字、移动分子与细胞核、调整箭头并保存重开。样本小、单一非盲评审，不承诺修正必然成功或普遍可靠。

本仓库公开Skill、Prompt与原创输入参考；最终精细插画、PPT成品和编辑截图未作为二进制资源上传。第一期PD-1/PD-L1案例继续保留。

## 能做什么

1. 提取细胞、分子、方向关系、证据来源和待核实项。
2. 先让人确认关系表，再写生图 Prompt 或生成概念图。
3. 根据确认的关系和图片参考，指导工具用原生文本框、形状和连接线重绘 PPT。
4. 检查文字能否改、节点能否移动、箭头能否单独选中，并如实标明未验证的步骤。

## 安装与使用

将整个仓库目录放到 Codex 的 `skills/research-mechanism-figure` 路径下；目录根部必须保留 `SKILL.md`。也可以在支持 Agent Skills 的宿主中按其文档安装。打开新任务后，用 `$research-mechanism-figure` 调用。

Windows PowerShell 示例：

```powershell
git clone https://github.com/zhaoyugethinker-collab/research-mechanism-figure.git "$env:USERPROFILE\.codex\skills\research-mechanism-figure"
```

macOS / Linux 示例：

```bash
git clone https://github.com/zhaoyugethinker-collab/research-mechanism-figure.git ~/.codex/skills/research-mechanism-figure
```

使用时给出论文或笔记、原图或草图、希望保留的机制关系，以及输出要求（PNG、PPTX 等）。机制关系有歧义时，Skill 会先列出待确认项。若目标是可编辑 PPT，请明确要求“文字、节点、箭头分别可编辑”。

## 仓库内容

|路径|用途|
|---|---|
|`SKILL.md`|主要工作流程与边界|
|`prompts/`|机制提取、生图和 Codex 工作流 Prompt|
|`references/`|科学边界与机制图检查表|
|`examples/pd1-pdl1/`|公开文献支持的概念案例与示例图|
|`examples/ifng-stat1-pdl1/`|第二期：亚细胞机制输入、来源和实际提示词|
|`scripts/inspect_native_pptx.py`|标准库PPT对象结构检查；不代替GUI测试|
|`VALIDATION.md`|已完成检查和当前限制|

PD-1/PD-L1 示例是一张概念插图，非实验数据；使用于科研发表前仍需领域专家核对。[Hamanishi 等（2016）](https://pubmed.ncbi.nlm.nih.gov/26899259/)、[Zou 等（2016）](https://pubmed.ncbi.nlm.nih.gov/26936508/)及 [Wei 等（2018）](https://pubmed.ncbi.nlm.nih.gov/30115704/)是示例的公开来源。

## 当前验证状态

技能包结构、资源链接及PPT检查脚本已作本地验证。第二期C1原生PPT已完成本机PowerPoint逐对象编辑、保存和重开检查；此公开输入包不附成品PPT。**技能自动发现、跨产品效果与独立领域专家审稿仍未验证。** 第一期历史记录保持原有状态，不能被第二期检查追溯替代。见 [VALIDATION.md](VALIDATION.md)。

此 Skill 不连接微信，也不自动上传公众号或发送研究资料到第三方服务。使用外部生图/转换工具前，请核对材料使用权限和工具的数据处理方式。

## 许可

原始 Skill 文本、Prompt、参考文档和脚本采用 [MIT License](LICENSE)。示例 PNG 仅供查看工作流结果，授权范围见 [ASSET_LICENSE.md](ASSET_LICENSE.md)。
