# 山竹科研机制图 Skill

`research-mechanism-figure` · v0.1 · Agent Skills 格式

这套 Skill 帮研究者把论文、笔记、已确认的机制关系或自绘草图整理成有依据的机制图，并在可用工具支持下重绘为 **文字、节点、箭头可分别编辑** 的 PPT 对象。

它提供工作流程、Prompt、关系表与编辑性检查。**当前版本没有通用的一键“图片转可编辑 PPT”转换器**。如果使用图像转换工具或原生形状重绘，需要检查实际 PPT 对象；把 PNG 放进一页 PPT 不算完成转换。

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
|`VALIDATION.md`|已完成检查和当前限制|

PD-1/PD-L1 示例是一张概念插图，非实验数据；使用于科研发表前仍需领域专家核对。[Hamanishi 等（2016）](https://pubmed.ncbi.nlm.nih.gov/26899259/)、[Zou 等（2016）](https://pubmed.ncbi.nlm.nih.gov/26936508/)及 [Wei 等（2018）](https://pubmed.ncbi.nlm.nih.gov/30115704/)是示例的公开来源。

## 当前验证状态

技能包结构已通过校验，示例中的提取、关系确认与生图流程经过手工演练。**自动发现和完整的 PPT 桌面逐对象操作验收尚未完成**；目前没有经过该验收的可编辑 PPTX 示例。详细结果见 [VALIDATION.md](VALIDATION.md)。

此 Skill 不连接微信，也不自动上传公众号或发送研究资料到第三方服务。使用外部生图/转换工具前，请核对材料使用权限和工具的数据处理方式。

## 许可

原始 Skill 文本、Prompt、参考文档和脚本采用 [MIT License](LICENSE)。示例 PNG 仅供查看工作流结果，授权范围见 [ASSET_LICENSE.md](ASSET_LICENSE.md)。
