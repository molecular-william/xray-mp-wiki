---
title: "Particulate Methane Monooxygenase (pMMO) from Methylococcus capsulatus (Bath)"
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature03311, doi/10.1021##bi800598h]
verified: false
---

# Particulate Methane Monooxygenase (pMMO) from Methylococcus capsulatus (Bath)

## Overview

Particulate methane monooxygenase (pMMO) is an integral membrane metalloenzyme that catalyses the conversion of methane to [Methanol](/xray-mp-wiki/reagents/additives/methanol) in methanotrophic bacteria. It is the predominant form of methane monooxygenase, produced by all known methanotrophs and housed in intracytoplasmic membranes. The enzyme from Methylococcus capsulatus (Bath) is a trimer composed of three subunits (pmoB, pmoA, pmoC) with an α3β3γ3 polypeptide arrangement. pMMO contains three metal centres per protomer — a mononuclear copper site, a dinuclear copper site, and a zinc site — that are proposed to be involved in methane hydroxylation at ambient temperature. The structure of pMMO from M. capsulatus (Bath) (PDB 1Y54) and M. trichosporium OB3b (PDB 3CHX) provide insight into how biological systems activate the extremely strong C-H bond of methane (104 kcal mol-1) for conversion to [Methanol](/xray-mp-wiki/reagents/additives/methanol).

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature03311 | 1Y54 | 2.8 A | unknown | Native pMMO heterotrimeric complex from Methylococcus capsulatus (Bath). The trimer is composed of three subunits: pmoB (α, ~47 kDa, residues 33-414), pmoA (β, ~24 kDa, 7 TM helices), and pmoC (γ, ~22 kDa, 5 TM helices). The pmoA2, pmoB2, and pmoC2 gene copies were used. The final model consists of 2,424 amino acid residues, 9 copper ions, and 8 zinc ions. Six copper sites were located using SOLVE. The N-terminal 32 residues of pmoB are a leader sequence that is cleaved. Several regions are disordered: 6 N-terminal residues of pmoA, 44 N-terminal residues of pmoC, residues 193-244 of pmoA (disordered loop), and residues 204-230 and 260-289 of pmoC. | copper (mononuclear and dinuclear sites), zinc (membrane site) |
| doi/10.1021##bi800598h | 3CHX | 3.9 A | P2(1)2(1)2(1) | pMMO heterotrimeric complex from Methylosinus trichosporium OB3b. Anisotropic data to 2.9 A allowed additional model building. The overall architecture is the same as M. capsulatus (Bath) pMMO — an alpha3beta3gamma3 trimer. The mononuclear copper center present in M. capsulatus (Bath) pMMO is absent; instead, the mononuclear site is replaced by a different arrangement. The zinc site in M. capsulatus (Bath) is occupied by copper in M. trichosporium OB3b pMMO. | copper (dinuclear site, zinc site replaced by copper) |

## Expression and Purification

- **Expression system**: Methylococcus capsulatus (Bath)
- **Construct**: Native pMMO from the second gene copy (pmoA2, pmoB2, pmoC2) of Methylococcus capsulatus (Bath). The pmoB subunit includes residues 33-414 after cleavage of a 32-residue N-terminal leader sequence.

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane isolation | Cell fractionation | -- | -- + -- | Not detailed in paper; intracytoplasmic membranes from M. capsulatus (Bath) |
| pMMO purification | Detergent solubilization and chromatography | -- | -- + -- | Purified pMMO contains 2-15 copper ions and 0-2 [IRON](/xray-mp-wiki/reagents/additives/iron) ions per ~100 kDa. Metal content determined by ICP-AES. |


## Crystallization

### doi/10.1038##nature03311

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | Purified pMMO from Methylococcus capsulatus (Bath) |
| Reservoir | Zinc [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate) present in crystallization buffer (source of zinc site) |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Data collected at copper and zinc absorption edges. Three complete data sets merged for CuSAD phasing. Anomalous peaks at copper edge in both CuANOM and Highres maps. Zinc sites identified in Highres map (zinc absorption edge). The zinc site is occupied by zinc from zinc [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate) in the crystallization buffer; in vivo it may be occupied by copper or [IRON](/xray-mp-wiki/reagents/additives/iron). Ramachandran plot: 95.6% (pmoA), 97.2% (pmoB), 97.1% (pmoC) in most favoured and additional allowed regions. |


## Biological / Functional Insights

### Trimeric architecture with α3β3γ3 arrangement

The crystal structure reveals that pMMO forms a trimer with an α3β3γ3 polypeptide
arrangement. Each protomer contains single copies of the pmoB, pmoA, and pmoC subunits.
The soluble regions are derived primarily from pmoB and include two antiparallel β-barrel
structures — one at the N terminus (7 strands) and one at the C terminus (8 strands),
oriented approximately 90° from each other. The two β-barrels are separated by a β-hairpin
followed by two transmembrane helices. The pmoA subunit (7 TM helices) packs against the
two TM helices of pmoB, while pmoC (5 TM helices) is oriented approximately parallel to
the membrane normal. Residues from a 22-residue loop linking TM helices to the C-terminal
β-barrel participate in trimer interface interactions with β-barrels from adjacent protomers.
The trimer is consistent with electron micrographs showing hexagonal particles ~9 nm in
diameter with six maxima of protein density.

### Mononuclear copper site in pmoB

The first metal centre is a mononuclear copper site located in pmoB approximately 25 Å
above the membrane surface, near the N-terminal β-barrel. The copper ion is coordinated
by the δ nitrogen atoms of His 48 and His 72 with nearly linear geometry. Gln 404 is also
within 3 Å of the copper ion. His 72 is highly conserved, while His 48 is replaced by
asparagine in M. trichosporium OB3b. This site is assigned as mononuclear based on strong
anomalous Fourier peaks and the absence of additional consistent peaks. If this site
generates the type 2 Cu(II) EPR signal observed at g = 2.06, it may be catalytic.

### Dinuclear copper site in pmoB

The second metal centre is a dinuclear copper site also within the N-terminal β-barrel of
pmoB, approximately 21 Å from the mononuclear site. This site is modelled as dinuclear on
the basis of oblong electron density in the 3.0 Å copper anomalous Fourier map and two
distinct peaks in a 2.8 Å zinc anomalous Fourier map. The Cu···Cu distance refines to
approximately 2.6 Å, consistent with EXAFS measurements. In the dinuclear site, one copper
ion is coordinated by the N-terminal residue of pmoB (His 33) via both the N-terminal
amino nitrogen and the side chain δ nitrogen. The second copper is ligated by His 137 and
His 139. His 33 and His 139 are held in position by hydrogen bonds to Glu 35 and Gly 152
carbonyl oxygen, respectively. This dinuclear site is an attractive candidate for the
active site, as it is structurally unusual. An adjacent cavity lined by conserved
hydrophobic residues (Pro 94 from pmoB, Leu 78, Ile 163, Val 164 from pmoC) is proposed
for methane binding. The side chain of conserved residue Trp 156 shields the dinuclear
centre from solvent, analogous to cytochrome c oxidase.

### Zinc site in the membrane

The third metal centre is modelled as a single zinc ion located within the lipid bilayer,
approximately 19 Å from the dinuclear copper centre. This site represents the highest
peak in a zinc anomalous Fourier map but is not present in copper anomalous maps. The zinc
ion is coordinated in distorted tetrahedral geometry by conserved residues Asp 156, His
160, and His 173 from pmoC, and Glu 195 from pmoA (tentatively assigned due to a
disordered loop). ICP-AES indicates pMMO samples contain less than 0.2 moles of zinc per
100 kDa before crystallization, meaning the zinc in this site is derived from zinc [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate)
in the crystallization buffer. This site may be occupied by another metal ion in vivo
such as copper or [IRON](/xray-mp-wiki/reagents/additives/iron).

### Structural similarity to cytochrome c oxidase subunit II

The pmoB subunit structurally resembles subunit II of cytochrome c oxidase, which contains
the dinuclear CuA site. Both contain a soluble C-terminal β-barrel domain and two TM
helices. However, the pmoB and cytochrome c oxidase β-barrels are not superimposable. The
pmoB dinuclear copper site differs from CuA in that it lacks cysteine sulphur bridges,
complete electron delocalization, and high covalency of Cu-S bonds. The structural
similarity suggests the dinuclear site in pMMO may function in electron transfer rather
than catalysis. If so, the mononuclear copper site might be the catalytic centre.

### Metal stoichiometry and catalytic implications

The three metal centres give a stoichiometry of three copper ions and a fourth yet-to-be-
identified metal ion per 100 kDa αβγ protomer. This is consistent with values measured by
ICP-AES for M. capsulatus (Bath) pMMO but significantly different from the 12-15 copper
ions reported by Chan and co-workers based on a proposed trinuclear copper cluster. No
electron density was detected for [IRON](/xray-mp-wiki/reagents/additives/iron) at the [IRON](/xray-mp-wiki/reagents/additives/iron) absorption edge. The dinuclear centre
is the most attractive candidate for the active site because dicopper centres in
haemocyanin, tyrosinase, and catechol oxidase can bind and/or activate dioxygen. However,
the Cu-Cu separation in pMMO (2.6 Å) is significantly smaller than in those enzymes.
A second cavity involving the same residues extends almost to the zinc site, suggesting
possible substrate access pathways.


## Cross-References

- [Single-Wavelength Anomalous Diffraction (SAD)](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — Phasing method used to solve the pMMO structure via copper and zinc anomalous sites
- [Sitting-Drop Vapor Diffusion](/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/) — Crystallization method used for pMMO structure determination
- [Zinc Chloride (ZnCl2)](/xray-mp-wiki/reagents/additives/zinc-chloride/) — Zinc source in crystallization buffer; zinc occupies the membrane metal centre
- [Copper(I) (Cu+)](/xray-mp-wiki/reagents/ligands/cu(i)/) — Copper is the key metal cofactor in the mononuclear and dinuclear metal centres
- [IRON](/xray-mp-wiki/reagents/additives/iron) — Additive used in purification or crystallization buffers
- [Methanol](/xray-mp-wiki/reagents/additives/methanol) — Additive used in purification or crystallization buffers
- [Acetate Buffer (Sodium Acetate)](/xray-mp-wiki/reagents/buffers/acetate) — Buffer component in purification or crystallization
