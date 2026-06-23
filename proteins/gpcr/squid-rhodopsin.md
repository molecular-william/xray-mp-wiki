---
title: "Squid Rhodopsin (Class A GPCR, Gq-coupled)"
created: 2026-05-26
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1074##jbc.C800040200, doi/10.1016##j.jmb.2011.08.044, doi/10.1038##nature06925]
verified: false
---

# Squid Rhodopsin (Class A GPCR, Gq-coupled)

## Overview

Squid rhodopsin from Todarodes pacificus is an invertebrate visual pigment that interacts with Gq-type G-protein to activate the inositol 1,4,5-triphosphate signaling pathway. The first crystal structure of squid rhodopsin was determined at 3.7 A resolution (PDB 2ZIY), revealing seven transmembrane helices and an amphipathic helix H8 similar to bovine rhodopsin and the human beta2-adrenergic receptor. Notably, squid rhodopsin contains a well-structured cytoplasmic region involved in G-protein interaction, which is flexible or disordered in bovine rhodopsin and beta2-AR. The transmembrane helices 5 and 6 are longer and extrude into the cytoplasm. The distal C-terminal tail contains a short hydrophilic alpha-helix CH after palmitoylated cysteine residues. The cytoplasmic region folds compactly, consisting of CL2, the extended TH5/TH6 region, H8, and the distal C-terminal tail including the CH helix. The Schiff base counterion is Tyr-111 (Asn-87 and Asn-185 are within hydrogen-bonding distance of the Schiff base nitrogen). The crystal structures of the primary photoreaction intermediates bathorhodopsin (Batho) and isorhodopsin (Iso, 9-cis) revealed that light energy absorbed by the protein is converted into distortion energy of the retinal polyene chain: upon photoisomerization, the central moiety moves toward the cytoplasmic side while the ionone ring and Schiff base remain relatively fixed, creating a right-handed screwed configuration.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1074##jbc.C800040200 | 2ZIY | 3.7 A | Not reported | Squid rhodopsin from Todarodes pacificus, C-terminally truncated by V8 protease cleavage (residues 1-373); dark state with 11-cis-retinal. Structure determined by molecular replacement using bovine rhodopsin (PDB 1GZM). Features extended TH5/TH6, structured CL3, and C-terminal helix CH. | 11-cis-retinal |
| doi/10.1016##j.jmb.2011.08.044 | 3P1L | 2.8 A | P62 | C-terminally truncated [squid rhodopsin](/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/) (residues 1-372, cleaved at Glu373 by V8 protease); bathorhodopsin state (all-trans retinal) | all-trans retinal |
| doi/10.1016##j.jmb.2011.08.044 | 3P1K | 2.7 A | P62 | C-terminally truncated [squid rhodopsin](/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/) (residues 1-357, cleaved at Glu358 by V8 protease); isorhodopsin state (9-cis retinal) | 9-cis retinal |
| doi/10.1016##j.jmb.2011.08.044 | 2BRS | 2.7 A | P62 | C-terminally truncated [squid rhodopsin](/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/) (dark state, 11-cis) | 11-cis retinal |
| doi/10.1038##nature06925 | 2BRS | 2.5 A | P62 | C-terminally truncated [squid rhodopsin](/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/) (residues Glu9-Glu358, cleaved at Glu373 by V8 protease; dark state, 11-cis retinal) | 11-cis retinal |

## Expression and Purification

- **Expression system**: Loligo (Todarodes) pacificus (native retina)
- **Construct**: Native [squid rhodopsin](/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/) from microvillar membranes; C-terminus truncated by V8 protease cleavage at Glu373 or Glu358

### Purification Workflow

#### Source: doi/10.1074##jbc.C800040200


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane isolation | Sucrose flotation of rhabdomeric membranes | -- | HEPES buffer (5 mM HEPES, pH 7.0, 1 mM EDTA, 1 mM DTT) + -- | Squid retina from Todarodes pacificus caught in the Japan Sea |
| V8 protease treatment | Proteolytic cleavage | -- | HEPES buffer (5 mM HEPES, pH 7.0, 1 mM EDTA, 1 mM DTT) + -- | 50:1 w/w rhodopsin:V8 protease, room temperature, 1 h. Removes unique C-terminal proline-rich extension. |
| Solubilization | Detergent extraction | -- | 50 mM HEPES pH 7.0, 0.05% DDM + 2% dodecyl maltoside (DDM) | Solubilization at 4 C for 1 h |
| Anion exchange | DEAE-cellulose column (flow-through) | DEAE-cellulose | 50 mM HEPES pH 7.0, 0.05% DDM + 0.05% DDM | Unbound fraction collected |
| Lectin affinity | Concanavalin A-Sepharose 4B | Concanavalin A-Sepharose 4B | 50 mM HEPES pH 7.0, 0.05% DDM + 0.05% DDM | Eluted with 0.2 M alpha-methyl mannoside. Fractions pooled, dialyzed against buffer A, concentrated by ultrafiltration (Amicon Ultra, Millipore). |

#### Source: doi/10.1016##j.jmb.2011.08.044


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane extraction | Selective extraction from squid microvillar membranes | -- | Tris buffer with zinc [acetate](/xray-mp-wiki/reagents/buffers/acetate/) + n-octyl beta-D-glucopyranoside ([OG](/xray-mp-wiki/reagents/detergents/og/)) | Rhodopsin extracted selectively from microvillar membranes; all manipulations performed in dim red light (>640 nm) |


## Crystallization

### doi/10.1074##jbc.C800040200

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 10 mg/ml purified squid rhodopsin in 10 mM HEPES pH 7.0, 200 mM NaCl, 2 mM dodecyldimethylamine oxide (LDAO), 0.03% DDM |
| Reservoir | 0.1 M HEPES pH 7.0, 8% ethylene glycol, 28% PEG 400 |
| Temperature | 20 C |
| Growth time | 5 days to appear, 2 weeks to stop growing |
| Cryoprotection | Data collected at 100 K on beam line BL45XU at SPring-8 |
| Notes | Structure determined by molecular replacement using bovine rhodopsin (PDB 1GZM) as search model. Refinement performed with CNS, REFMAC5, and O. B-factor sharpening used with Bsharp values -50 to -150 A2. Coordinates deposited as PDB 2ZIY. V8 protease treatment removes C-terminal proline-rich extension. |

### doi/10.1038##nature06925

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | C-terminally truncated squid rhodopsin solubilized in n-octyl beta-D-glucopyranoside (OG) |
| Reservoir | 3.2 M ammonium sulfate, 32 mM MES pH 6.4, 38 mM EDTA, 10 mM beta-mercaptoethanol |
| Temperature | 277 K |
| Growth time | >6 months |
| Cryoprotection | 20% sucrose, flash-frozen in liquid propane at 100 K |
| Notes | Hexagonal P62 crystals. Extracted from microvillar membranes with octylglucoside in presence of zinc acetate. V8-protease cleavage at Glu373. |

### doi/10.1016##j.jmb.2011.08.044

| Parameter | Value |
|---|---|
| Method | In meso crystallization (hexagonal P62 crystals) |
| Protein sample | Truncated [squid rhodopsin](/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/) solubilized in n-octyl beta-D-glucopyranoside ([OG](/xray-mp-wiki/reagents/detergents/og/)) |
| Reservoir | not specified |
| Temperature | 100 K (cryogenic) |
| Growth time | not specified |
| Cryoprotection | Cryocooled to 100 K; crystals handled in dim red light (>640 nm) |
| Notes | Hexagonal P62 crystals. Data collected at SPring-8 BL41XU using a 10-micrometer microbeam. Photoreaction states trapped by illumination at specific wavelengths: blue light (473 nm) for bathorhodopsin, yellow light (560 nm) for isorhodopsin, red light (635 nm) for dark-state rhodopsin. |


## Biological / Functional Insights

### Extended TH5 and TH6 form a structured cytoplasmic domain for G-protein coupling

The 3.7 A crystal structure of squid rhodopsin (PDB 2ZIY) revealed that transmembrane helices 5 and 6 are longer than in bovine rhodopsin and the human beta2-adrenergic receptor, extruding into the cytoplasm. This extension is accompanied by a 12-amino-acid insertion in the CL3 region. TH5 elongates to Lys-239 with a bend at His-230, while TH6 extends from Glu-245 with a bend at Ser-275 before Pro-276 and Tyr-277. Together with CL2, H8, and the distal C-terminal tail, these elements form a compact, well-ordered cytoplasmic domain that is thought to mediate selective recognition and activation of the Gq protein. In bovine rhodopsin and beta2-AR, the corresponding CL3 region is either flexible, disordered, or substituted.

### Short hydrophilic C-terminal helix CH

The distal C-terminal tail of squid rhodopsin contains a short hydrophilic alpha-helix (CH) formed by residues Asp-341 to Asp-347, located after the palmitoylated cysteine residues that anchor H8 to the membrane. The residues in the distal C-terminal tail interact with neighboring residues in CL2, the extruded TH5/TH6, and the short helix H8. After helix CH, the C-terminal tail from Lys-348 to Glu-373 interacts closely with the extended TH5/TH6 region and returns to the putative membrane surface in an extended structure via polar interactions with CL2.

### Schiff base environment and counterion

The Schiff base connecting 11-cis-retinal to Lys-305 has Tyr-111 as its counterion, in contrast to bovine rhodopsin where Glu-113 serves this role. Asn-87 and Asn-185 residues are located within hydrogen-bonding distances from the nitrogen atom of the Schiff base. This arrangement is consistent with a slower photoisomerization rate in squid rhodopsin compared to bovine rhodopsin.

### Distinct electrostatic profile for Gq coupling specificity

The electrostatic potentials of the cytoplasmic surfaces of squid rhodopsin have a profile characteristic of intracellular GPCR domains. The distinct electrostatic profiles between squid rhodopsin (Gq-coupled) and bovine rhodopsin (Gt-coupled) are located around the TH5 intracellular surface region. The corresponding TH5 region was important for Gi coupling but less so for Gq in BLT1 (leukotriene B4 receptor). The compact hydrophilic intracellular domain of squid rhodopsin, anchored by cysteine palmitoylations at H8, is proposed to participate in recognizing and activating the Gq protein on the lateral membrane surface.

### Retinal distortion stores light energy in bathorhodopsin

The bathorhodopsin structure reveals that upon photoisomerization (11-cis to all-trans), the retinal central moiety moves largely toward the cytoplasmic side while the ionone ring and Schiff base undergo limited movement. The polyene chain takes on a right-handed screwed configuration with twisted C7=C8, C9=C10, and C11=C12 bonds. The C13 methyl pushes Ser187 into the E-II loop, and the C9 methyl pushes Phe188. This distortion stores approximately 35 kcal/mol of energy, conserved between vertebrate and invertebrate rhodopsins.

### Structural differences from [bovine rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/)

[Squid rhodopsin](/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/) differs from [bovine rhodopsin](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) in the retinal-binding pocket: the beta-ionone ring is surrounded by aromatic residues (vs glutamate in bovine), and the retinal polyene chain associates with helix III backbone over three helical turns (vs polar residue Thr118 in bovine). The Schiff base H-bond partner is Asn87 or Tyr111 (vs Gly89 and Glu113 in bovine). These differences slow cis-trans isomerization in [squid rhodopsin](/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/) compared to bovine while maintaining similar bathorhodopsin energy levels.

### X-ray radiation damage in rhodopsin

Significant X-ray radiation damage was characterized: (1) retinal isomerization to an orange species (precursor of retro form) at approximately 4 x 10^14 photons/mm^2, (2) breakage of disulfide bond between Cys108 and Cys186, (3) loss of electron density at Asp80 (decarboxylation/radiolysis). These changes produce photochemically inactive products that can be distinguished from functional photointermediates. Data collection must account for approximately 50% protein damage at doses of 3 x 10^15 photons/mm^2.


## Cross-References

- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Primary detergent for squid rhodopsin extraction and crystallization
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization in 2% DDM for the 3.7 A structure determination
- [Ammonium Sulfate](/xray-mp-wiki/reagents/additives/ammonium-sulfate/) — Crystallization precipitant at 3.2 M in sitting-drop vapor diffusion
- [MES (2-(N-Morpholino)ethanesulfonic Acid)](/xray-mp-wiki/reagents/buffers/mes/) — Crystallization buffer at 32 mM, pH 6.4
- [11-cis-Retinal](/xray-mp-wiki/reagents/ligands/11-cis-retinal/) — Chromophore covalently bound to Lys305 via protonated Schiff base in the dark state
- [Acetate Buffer (sodium acetate)](/xray-mp-wiki/reagents/buffers/acetate/) — Zinc acetate used in squid rhodopsin extraction buffer
- [Tris (Tris-HCl buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Used in extraction buffer for squid rhodopsin purification
- [Bovine Rhodopsin (Dark State)](/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/) — Comparative vertebrate rhodopsin; key reference for retinal-binding pocket and cytoplasmic region differences
- [Human Beta2-Adrenergic Receptor (beta2 AR)](/xray-mp-wiki/proteins/gpcr/beta2-adrenergic-receptor/) — Comparative GPCR structure; squid rhodopsin has structured CL3 vs disordered in beta2 AR
- [GPCR G-Protein Coupling](/xray-mp-wiki/concepts/signaling-receptors/gpcr-g-protein-coupling/) — Squid rhodopsin is model for Gq-coupled GPCR with structured cytoplasmic domain
- [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) — Cryoprotectant at 20% used for flash-freezing squid rhodopsin crystals
