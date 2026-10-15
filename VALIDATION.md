# v0.2 validation record

Date: 2026-10-15. Scope: public skill package and one subcellular case. Overall scientific/runtime status remains PARTIAL; checks below do not establish general reliability.

| Check | Result | Scope |
|---|---|---|
| Package syntax/frontmatter and resource links | PASS | Local quick validator and referenced-file check |
| Public text privacy review | PASS | No private machine paths, credentials, authentication caches or private reports included |
| A/B/C actual inputs | Included | Exact prompts, original sketch/style guides and frozen review rubric; three calls each, C paired with B |
| Iterative correction | Mixed | C1/C2 improved, C3 regressed; no population-level stability claim |
| Native C1 redraw | Checked | 775 native leaf shapes, 19 groups, 30 textboxes, 264 custom freeforms, zero picture/media objects |
| PowerPoint edit/save/reopen | PASS for this case | On a copy: STAT1 label changed, IRF1 moved, nuclear structure moved, phosphorylation arrow adjusted; saved, closed and reopened; XML changes checked |
| Editor screenshot | User supplied | Actual multi-object selection screenshot archived locally; selection alone is not proof of save persistence |
| PPT inspector behavior | PASS | Actual native C1 accepted with zero-image requirement; raster-only fixture rejected |
| Skill automatic discovery / cross-host reproduction | NOT_VERIFIED | This session followed the package workflow explicitly |
| Independent domain review | NOT_PERFORMED | Educational simplified mechanism; case assessed by the same Codex session |

The public package contains original prompts and input references, not the final C1 image, PPT binary or user editor screenshot. Host-specific authoring scripts and raw local receipts are not distributed. No dedicated image-to-editable-ppt converter or complete PaperBanana multi-agent pipeline was run.

## Historical v0.1 record (unchanged)

# Skill validation report

**Status: PARTIAL**  
Skill: `research-mechanism-figure` v0.1  
Case: PD-1/PD-L1-mediated tumor immune evasion  
Date: 2026-09-27

## What was validated

| Check | Result | Evidence / limits |
|---|---|---|
| Skill correctly recognized by Codex runtime | **Not verified** | The package was created in the project asset directory and was not installed to the active Codex user skill directory. This session cannot refresh skill discovery dynamically. The workflow below was followed manually from `SKILL.md`. |
| Followed “mechanism before image” | **Yes, manual workflow** | Read the frozen benchmark, extracted the minimal elements and relations, and prepared the table before calling image generation. |
| Public-source metadata | **Yes** | The three cited PMID/title/DOI combinations were checked against their PubMed records on 2026-09-28; this is not a full scientific claim audit. |
| Generated a relationship table | **Yes** | `examples/pd1-pdl1/mechanism-table.md` records source, direction, certainty, and review needs. |
| Uncertain/context-dependent claims marked | **Yes** | Immune evasion is described as a contributing mechanism, not a sole cause or guaranteed outcome; expression and response are not universal. |
| Human confirmation gate | **Passed by prior scope confirmation** | This is the same frozen benchmark and relationship chain from the earlier user-authorized PD-1/PD-L1 figure task. No new biological relationships were added. This basis is recorded because no separate new confirmation was requested. |
| Generated an image after the gate | **Yes** | A new image-generation call used the confirmed minimal chain. Output: `examples/pd1-pdl1/skill-generated.png`. |
| Unapproved mechanism expansion | **None observed** | The generated image contains the tumor cell, CD8+ T cell, PD-L1, PD-1, reduced T-cell effector activity, and tumor immune evasion. No IFN-γ, TCR/MHC-I, SHP2, TAM/MDSC, treatment, or quantitative data appeared. |
| Image quality/science check | **Partial** | Labels and requested chain are visible, including “Conceptual illustration; not experimental data”. The graphic still requires domain review before scientific use; image generation alone does not validate biology. |
| Continued through editable-PPT conversion | **Partial / unavailable converter** | No dedicated `image-to-editable-ppt` tool was available. A separate native-shape redraw exists elsewhere in the asset pack, but GUI interaction checks (text edit, node movement, arrow selection) remain incomplete; therefore it is not bundled as a verified example PPT. |
| Final scientific verification | **Pending human domain review** | The output is a concept illustration. A qualified reviewer should compare it with the cited literature and intended context before release. |
| Skill package structure | **PASS** | The local `skill-creator` quick validator returned “Skill is valid!” when run in UTF-8 mode. This checks package syntax/scaffold quality, not runtime discovery or scientific correctness. |

## Validation output

The manual run produced an extraction table, a prompt, and a new PNG. The flow respected the key ordering—table before image generation—and showed no unauthorized pathway additions. Because automatic skill recognition was not tested and the editable-PPT route was not fully verified, the overall result is **PARTIAL**, not PASS.

## Next validation step

Install the folder in the Codex skills directory, start a fresh task, confirm the skill is discoverable, and repeat the case. For a complete workflow pass, obtain human domain review and test text editing, node movement, and arrow selection in PowerPoint or Impress.
