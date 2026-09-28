# Mechanism extraction prompt

Use this before image generation. Include only sources and notes supplied or explicitly approved by the user.

> From the provided papers, cited notes, verified relationships, and/or original sketch, extract the smallest mechanism needed for the requested figure. Do not generate an image yet.
>
> Return: (1) figure purpose and biological scope; (2) core cells, compartments, molecules, states, interventions, and outcomes; (3) a table with columns `element | acts on / relates to | relationship type | direction | evidence/source | certainty | needs review`; (4) uncertain, context-dependent, or conflicting relations; (5) important omissions and why they are outside scope; and (6) a plain-language layout proposal.
>
> Preserve the distinction between correlation, association, proposed mechanism, and demonstrated causality. Give each relation a source locator (section, figure, page, DOI/PMID, or user note). If evidence is missing, label the relation `UNCERTAIN` rather than filling the gap from memory. Do not add familiar but unrequested pathways. End with a concise human-review checkpoint listing the exact claims that need confirmation.
