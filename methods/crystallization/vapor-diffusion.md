---


title: Vapor Diffusion Crystallization
created: 2026-04-26
updated: 2026-04-27
type: method
tags: [crystallization-vapor-diffusion]
sources: [doi/10.1002##anie.201302374, doi/10.1016##j.bbabio.2023.148986, doi/10.1007##s10969-013-9154-x, doi/10.1016##j.cell.2010.05.003]


---
layout: default



# Vapor Diffusion Crystallization

## Description

Vapor diffusion is the most widely used method for protein crystallization. A droplet containing protein and precipitant solution is equilibrated against a larger reservoir of higher precipitant concentration. Water vapor diffuses from the droplet to the reservoir, slowly concentrating the protein and promoting crystallization.

## Variants

- **Sitting drop**: Droplet sits on a platform above reservoir
- **Hanging drop**: Droplet hangs from a coverslip sealed over reservoir

## Proteins Using Vapor Diffusion (from this wiki)

- [[opsin-gpcr]] — Ops* crystallized at pH 5.6 with OG detergent
- [[psi-lhci-supercomplex]] — Form-A crystals in 50 mM Tris-HCl pH 7.0, 50 mM Li₂SO₄, 4.5-7.0% PEG 6000
- [[a2a-adenosine-receptor]] — sitting-drop [[vapor-diffusion]] with A2A-PSB1-bRIL construct
- [[acrB]] — sitting-drop vapor diffusion: 0.1 M Na-phosphate pH 6.2, 0.1 M NaCl, 8% PEG 4000; crystals soaked with 6 mM Linezolid in cryosolvent (25% [[glycerol]])
- [[kirbac]] — vapor diffusion at 19°C (Bio21 C3 facility); KirBac3.1 structures crystallized in multiple space groups (P2₁2₁2, I222, C222₁, P1); soaked in 50 mM [[spermine]] for polyamine binding studies
- [[etb-receptor]] — vapor diffusion; ETB-S6b complex crystals; 32 datasets merged by KAMO; P2₁2₁2 space group; 3.0 Å resolution; [[molecular-replacement]] using ET-3-bound receptor (PDB 6IGK)

## Key Variables

- **Precipitant**: PEGs, salts (Li₂SO₄, ammonium sulfate), organic solvents
- **pH**: Critical for protein charge state and solubility
- **Temperature**: Typically 4°C, 18°C, or 20°C
- **Additives**: Ligands, detergents, ions, small molecules

|## Related Methods
|
|- [[lipidic-cubic-phase]] — LCP method for membrane proteins
|- [[microbatch]] — oil-overlay method
|- [[dialysis]] — equilibrium dialysis crystallization

## See Also

### Alternative Methods
- [[lipidic-cubic-phase]] — LCP method for membrane proteins
- [[microbatch]] — Oil-overlay method
- [[dialysis]] — Equilibrium dialysis crystallization

### Related Techniques
- [[crystallization]] — General crystallization overview
- [[purification]] — Purification methods

## Backlinks

Pages that link to this page:
{% assign backlinks = site.pages | where_exp: "page", "page.content contains page.url" | sort: 'title' %}
{% for page in backlinks %}
- [[{{ page.title }}]]
{% endfor %}
{% if backlinks.size == 0 %}
*No pages currently link to this page.*
{% endif %}
