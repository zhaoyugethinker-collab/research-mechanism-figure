# PD-1 / PD-L1 example

This example uses the same public-source, minimal mechanism prepared for the project benchmark. It demonstrates input packaging, relation extraction, and prompt preparation. The example does not establish a GPT-vs-Codex image-quality winner.

## Validation state

The frozen benchmark and resulting relation table were manually reviewed in the project workflow. The prior user-authorized scope explicitly covered image generation for this same frozen case, so that existing confirmation was used as the human-confirmation basis; no relationships were changed. A new image was generated and saved as `skill-generated.png`. This is still a conceptual illustration awaiting domain review. The Skill package was not dynamically registered in the active Codex runtime during validation, so automatic skill recognition is **not verified**; the workflow was applied manually. Overall status is `PARTIAL` in [VALIDATION.md](../../VALIDATION.md).

The project contains a separate native-shape PPT redraw and a PDF preview. It is not copied here as `example-editable.pptx` because PowerPoint/Impress GUI interaction checks (text edit, node movement, arrow selection) were not completed. Do not treat the existing PPTX as an example that passed the Skill's full editability review.

## Files

- `benchmark-input.md`: frozen task, cited sources, scope, and parent prompt.
- `mechanism-table.md`: extracted relationships and evidence/uncertainty status.
- `example-prompts.md`: prompts to reproduce extraction and image planning after human confirmation.
- `skill-generated.png`: image generated during the manual Skill validation run; not experimental data and not a scientifically approved final figure.
