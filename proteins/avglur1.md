---
title: AvGluR1 Ligand-Binding Domain (LBD)
created: 2026-05-28
updated: 2026-05-28
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2013.01.006]
verified: false
---

# AvGluR1 Ligand-Binding Domain (LBD)

## Overview

The ligand-binding domain (LBD) of AvGluR1, an ionotropic glutamate receptor from the freshwater bdelloid rotifer Adineta vaga. AvGluR1 is proposed as an evolutionary link between prokaryotic and eukaryotic iGluRs, possessing both an amino-terminal domain and three membrane-spanning segments with the SYTAN motif characteristic of AMPA, kainate, and NMDA receptors. The LBD exhibits unusual ligand binding properties, accommodating chemically diverse amino acids including alanine, cysteine, methionine, and phenylalanine alongside glutamate, aspartate, and serine. A key discovery is that chloride ions act as surrogate ligand atoms, replacing the gamma-carboxyl group for neutral amino acids.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.str.2013.01.006 | 4IO2 | 1.37 | P21 | S1 A433-K543 + GT linker + S2 L656-P788 | L-glutamate |
| doi/10.1016##j.str.2013.01.006 | 4IO3 | 1.66 | P21 | S1 A433-K543 + GT linker + S2 L656-P788 | L-aspartate |
| doi/10.1016##j.str.2013.01.006 | 4IO4 | 1.94 | P21 | S1 A433-K543 + GT linker + S2 L656-P788 | L-serine |
| doi/10.1016##j.str.2013.01.006 | 4IO5 | 1.72 | P21 | S1 A433-K543 + GT linker + S2 L656-P788 | L-alanine |
| doi/10.1016##j.str.2013.01.006 | 4IO6 | 1.60 | P21 | S1 A433-K543 + GT linker + S2 L656-P788 | L-methionine |
| doi/10.1016##j.str.2013.01.006 | 4IO7 | 1.92 | P21 | S1 A433-K543 + GT linker + S2 L656-P788 | L-phenylalanine |

 - Data collection: SER-CAT 22-ID beamline, APS, Advanced Photon Source
 - Data collection: SER-CAT 22-ID beamline, APS, Advanced Photon Source
 - Data collection: SER-CAT 22-ID beamline, APS, Advanced Photon Source
 - Data collection: SER-CAT 22-ID beamline, APS, Advanced Photon Source
 - Data collection: SER-CAT 22-ID beamline, APS, Advanced Photon Source
 - Data collection: SER-CAT 22-ID beamline, APS, Advanced Photon Source

## Expression and Purification

- **Expression system**: Escherichia coli Origami B(DE3)
- **Construct**: S1 residues A433-K543 connected via a GT dipeptide linker to S2 residues L656-P788, with N-terminal MH8SSGLVPRGS affinity tag and thrombin cleavage site
- **Induction**: 30 uM IPTG for 15 hr at 18 C
- **Media**: pET22b vector

### Purification Workflow

- **Expression system**: E. coli Origami B(DE3)
- **Expression construct**: S1 A433-K543 + GT linker + S2 L656-P788, N-terminal MH8SSGLVPRGS affinity tag
- **Tag info**: MH8SSGLVPRGS His-tag with thrombin cleavage site

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and solubilization | Bacterial cell lysis, soluble fraction isolated | N/A | N/A | Soluble fraction from bacterial cell lysates |
| Affinity chromatography | Ni-NTA chromatography | Ni-NTA | N/A | N-terminal His-tag purification |
| Tag cleavage | Thrombin cleavage | N/A | N/A | Extended native N-terminal sequence by four residues (ARLK) to enable thrombin cleavage |
| Ion exchange chromatography | SP sepharose ion exchange | SP sepharose | N/A | Final purification step |
**Yield**: 8-10 mg from 12 L cultures


## Crystallization

### doi/10.1016##j.str.2013.01.006

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | AvGluR1 LBD with L-glutamate |
| Reservoir | N/A |
| Temperature | N/A |
| Growth time | N/A |
| Notes | Crystallized as back-to-back dimers, canonical arrangement found in full-length GluA2. P21 space group |


## Biological / Functional Insights

### Unusual ligand binding profile

AvGluR1 LBD binds glutamate with Kd 203 +/- 18 nM, comparable to GluR0 from Synechocystis (193 nM) but distinct from GluA2 AMPA receptor (821 nM). It shows preference for kainate-receptor-like binding, with higher affinity for the kainate receptor-preferring agonist SYM2081 (Kd 49.5 uM) and the GluK1-preferring antagonist UBP-310 (Kd 160 uM). It binds AMPA (Kd 130 uM) and quisqualate (Kd 39 uM) but has very low affinity for kainate (Kd 2.7 mM) and NMDA (Kd 9.9 mM). Uniquely, AvGluR1 is activated by neutral amino acids alanine, cysteine, methionine, and phenylalanine in addition to acidic amino acids glutamate and aspartate.

### Chloride ions act as surrogate ligand atoms

Crystal structures of alanine, serine, and methionine complexes reveal that chloride ions occupy positions equivalent to the gamma-carboxyl group oxygen atoms in the glutamate complex. In the alanine complex, a Cl- ion is coordinated by Arg676 side chain, the main chain amide of Asp720, and water molecules W3 and W7. In the serine complex, the Cl- ion is displaced by 2.3 A and coordinated by both Arg702 and Arg676 side chains and the main-chain amide of Asp720. Removal of Cl- lowers affinity for alanine (53-fold) and serine (19-fold) but not for glutamate or aspartate. The methionine affinity decreases only 18-fold in HEPES buffer despite strong Cl- electron density, suggesting methionine can adopt an alternative rotamer.

### Prokaryotic iGluR-like features

The AvGluR1 LBD has a two-domain closed-cleft clamshell structure typical of iGluRs. It shares deletions with bacterial iGluRs, lacking loop 2 and alpha helix G that are present in AMPA and kainate receptor LBDs. A structure-based phylogenetic analysis reveals clustering of AvGluR1 with bacterial iGluRs rather than vertebrate iGluRs. However, AvGluR1 has a large amino-terminal domain like eukaryotic iGluRs and shows weak LBD self-association in solution (similar to eukaryotic iGluRs), despite phylogenetic clustering with bacterial receptors.

### Dimer assembly and desensitization

AvGluR1 LBD amino acid complexes crystallized as back-to-back dimers with a buried surface of 1,305 A2 per subunit. The dimer interface is formed primarily by polar interactions between alpha helices C and H, with salt bridges between Arg523-Asp762, Glu524-Lys759, and Asp743-Arg769. The dimer has an upright orientation (45 degrees between alpha helix H vectors) compared to the GluA2 dimer (61 degrees), similar to the bacterial GluR0 dimer. Introduction of Cys mutations at Ser520 and Leu766 (S520C/L766C) to form disulfide crosslinks abolishes desensitization completely, consistent with the model that LBD dimer rupture drives desensitization.

### Desensitization attenuated by concanavalin A

Treatment with concanavalin A (0.5 mg/ml for 4 min) strongly attenuates desensitization of AvGluR1, similar to the effect on kainate receptors in mammalian iGluRs. This is consistent with the greater sequence similarity of AvGluR1 to kainate versus AMPA receptors and the larger number of predicted N-linked glycosylation sites in AvGluR1 compared to GluA2.


## Cross-References

- [L-Glutamate](/xray-mp-wiki/reagents/substrates/l-glutamate/) — Primary orthosteric ligand of AvGluR1 with Kd 203 nM
- [L-Aspartate](/xray-mp-wiki/reagents/substrates/l-aspartate/) — Acidic amino acid ligand binding to AvGluR1 LBD
- [L-Alanine](/xray-mp-wiki/reagents/substrates/l-alanine/) — Neutral amino acid ligand using chloride ion as surrogate
- [L-Serine](/xray-mp-wiki/reagents/substrates/l-serine/) — Neutral amino acid ligand using chloride ion as surrogate
- [L-Methionine](/xray-mp-wiki/reagents/l-methionine/) — Neutral amino acid ligand with reduced chloride dependence
- [L-Phenylalanine](/xray-mp-wiki/reagents/l-phenylalanine/) — Hydrophobic amino acid ligand that occludes anion binding site
- [GluA2 LBD](/xray-mp-wiki/proteins/glua2-lbd/) — AMPA receptor LBD used for structural comparison of dimer assembly
- [Allosteric Regulation](/xray-mp-wiki/concepts/allosteric-regulation/) — ATD-LBD linker conformation and allosteric regulation of activation
