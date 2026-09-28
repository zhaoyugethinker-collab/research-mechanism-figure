# Image-generation prompt template

Use only after a user or named human reviewer confirms the mechanism table. Replace bracketed fields with confirmed content. Do not paste unsupported mechanism claims into the prompt.

> Create an original scientific mechanism illustration for **[audience and purpose]**.
>
> **Canvas and layout:** [aspect ratio, cell/compartment placement, visual hierarchy].  
> **Required elements:** [confirmed cells, molecules, states, outcomes and locations].  
> **Required relations:** [confirmed binding, activation, inhibition, movement, or context relationship; specify arrow start and end].  
> **Labels:** Render these labels verbatim: [exact labels].  
> **Visual style:** [plain background, palette, line weight, typography, whitespace].  
> **Exclusions:** Do not add [unconfirmed cells, pathways, causal claims, treatment, data, or labels]. Do not copy or trace a published figure.  
> **Scientific status:** Label as “Conceptual illustration; not experimental data” unless the user requests other accurate wording. Do not depict quantitative findings without supplied data.

Return one initial image. Preserve it before iteration. If a label, arrow, or relationship is visually ambiguous, report the ambiguity and request targeted correction rather than silently asserting correctness.
