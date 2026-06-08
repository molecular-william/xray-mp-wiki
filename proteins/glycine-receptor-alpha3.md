---
title: Human Glycine Receptor Alpha-3 Homopentamer (GlyRα3)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature14972]
verified: false
---

# Human Glycine Receptor Alpha-3 Homopentamer (GlyRα3)

## Overview

The human glycine receptor alpha-3 subunit (GlyRα3) is a pentameric ligand-gated ion channel (pLGIC) belonging to the Cys-loop receptor family. Glycine receptors mediate fast inhibitory synaptic transmission in the spinal cord and brainstem and play key roles in motor coordination and inflammatory pain processing. Disruption of GlyR function causes hyperekplexia, a neurological disorder with exaggerated startle response. In vivo, GlyRs exist as homopentamers of α-subunits or heteropentamers of α- and β-subunits. The GlyRα3 homopentamer structure presented here represents the first crystallographic analysis of a pLGIC in the antagonist-induced inactive state.


## Structure Determination

No structure determined.

## Expression and Purification

- **Expression system**: Baculovirus expression in Sf9 insect cells
- **Construct**: GlyRα3 crystallization construct (human GlyRα3 residues 1-460, Δ343-418::AGT, C-terminus truncated by 4 residues, Strep II tag added to C-terminus)
- **Notes**: The 76-residue intracellular loop between M3 and M4 helices was replaced with an Ala-Gly-Thr tripeptide. Four residues were deleted from the C-terminus based on sequence alignments with mammalian GlyRα3 sequences. Bac-to-Bac system was used for baculovirus generation. Cells grown in sfx medium at 27°C for 72 h.

### Purification Workflow

- **Expression system**: Sf9 insect cells (baculovirus)
- **Expression construct**: GlyRα3 crystallization construct with Strep II tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and harvest | Baculovirus expression | — | sfx medium | Sf9 cells grown at 27°C for 72 h, harvested by centrifugation at 2000g |
| Membrane preparation | Cell lysis and membrane isolation | — | 50 mM Tris pH 8.0, 150 mM NaCl, 1% protease inhibitors cocktail | Cells disrupted in Microfluidizer, homogenate clarified at 10000g, crude membranes collected at 125000g |
| Solubilization | Detergent solubilization | -- | 20 mM Tris pH 8.0, 150 mM NaCl + 0.2 g DDM per gram of membranes | Membranes mechanically homogenized in DDM |
| Affinity chromatography | Strep-tag affinity chromatography | Strep affinity resin (IBA) | 20 mM Tris pH 8.0, 150 mM NaCl, 1 mM DDM | Bound to Strep resin, washed with buffer containing 1 mM DDM |
| Elution | Affinity chromatography | Strep affinity resin (IBA) | 20 mM Tris pH 8.0, 150 mM NaCl, 1 mM DDM, 5 mM desthiobiotin | Eluted with 5 mM desthiobiotin |
| Size-exclusion chromatography | Size-exclusion chromatography | -- | 20 mM Tris pH 8.0, 150 mM NaCl, 1 mM DDM | Further purified by gel filtration, all steps at 4°C |


## Crystallization

### doi/10.1038##nature14972

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | ~3 mg/ml GlyRα3-strychnine complex (0.2 mM strychnine incubated at 4°C for 30 min) |
| Reservoir | 25 mM sodium citrate pH 4.0, 100 mM KCl, 200 mM MgCl2, 30-33% PEG400 |
| Mixing ratio | 0.5 μl protein : 0.5 μl reservoir |
| Temperature | 4 |
| Growth time | ~1 month |
| Cryoprotection | Direct freezing in liquid nitrogen from crystallization drops |
| Notes | Diffraction data collected at beamline 22-ID, Advanced Photon Source, Argonne. Final 3.0 Å data set assembled from 15 crystals (10-30° per crystal). Structure determined by molecular replacement using apo-GluCl (4TNV) as search model. |


## Biological / Functional Insights

### Closed ion channel pore in antagonist-bound state

The ion channel pore of GlyRα3 is lined by the transmembrane helix M2. The narrowest constriction is 1.4 Å caused by the side chain of Leu261 (Leu 9') at the mid-point of the channel. Since the radius of a dehydrated chloride ion is 1.8 Å, this is consistent with a closed, non-conducting state. Leu261 forms the shut gate. In the antagonized state, all five M2 helices are straight and oriented parallel to the pore axis. The M2 helices are 11.0 Å apart at the apex (Ala272), 11.7 Å at the base, and 13.0 Å at the most constricted point (Leu261), averaging the distance between Cα carbons of i and i+2 protein subunits. This corresponds to an ~4° tilt of the M2 helix towards the pore axis compared to the apo-GluCl structure.

### Antagonist-induced conformational changes

Strychnine binds in a larger orthosteric pocket in the extracellular domain, and loop C of GlyRα3 adopts an open conformation. The M2-M3 loop is displaced inwards towards the pore, the pore-lining M2 helix tilts in a direction opposite to that observed in active conformations of related pLGICs, and the pore is shut. This represents the first crystallographic analysis of a pLGIC in the inactive state induced by a competitive antagonist.

### ECD-TMD interface and signal transduction

The ECD-TMD interface contains hydrophobic contacts between the N-terminal portion of the M2-M3 loop, the β1-β2 loop, and the β6-β7 (Cys) loop, as well as polar contacts between the C-terminal portion of the M2-M3 loop and the β6-β7 loop. Pro275 from the M2-M3 loop interacts with Leu142 and Phe145 from the β6-β7 loop. Tyr279 side-chain hydroxyl oxygen is hydrogen-bonded to the main-chain amino nitrogen of Leu142. Pro275 of the M2-M3 loop is 7.1 Å from Thr54 of the β1-β2 loop in the strychnine-bound state.

### Hyperekplexia mutations

Highly conserved residue Pro250 (Pro-2') of M2 is critical for ion selectivity; mutation Pro250Thr in GlyRα1 is linked to hyperekplexia. Leu261 (Leu9') is highly conserved and mutation of the equivalent Leu285 in GlyRβ to Arg has been linked to hyperekplexia. Other hyperekplexia mutations in GlyRα1 (V260M, T265I, Q266H, S267N) with spontaneous channel activity cluster on the pore-lining M2 helix. Hyper-ekplexia mutations in GlyRα1 (R271Q/L/P, K276E/Q, Y279C/S) are clustered around the M2-M3 loop and lead to reductions in glycine sensitivity and maximum probability of channel opening.


## Cross-References

- [Cys-Loop Receptor Family](/xray-mp-wiki/concepts/cys-loop-receptor-family/) — GlyRα3 belongs to the Cys-loop receptor (pLGIC) family
- [GluCl (GABA-Gated Chloride Channel from C. elegans)](/xray-mp-wiki/proteins/glucl/) — Used as molecular replacement search model; key comparative structure for pLGIC gating
- [ELIC (Erwinia chrysanthemi Ligand-gated Ion Channel)](/xray-mp-wiki/proteins/elic/) — Prokaryotic pLGIC homologue used for structural comparisons
- [GLIC (Gloeobacter violaceus Ion Channel)](/xray-mp-wiki/proteins/glic/) — Prokaryotic pLGIC homologue for structural comparisons
- [Human GABA_A Receptor Beta-3 Subunit](/xray-mp-wiki/proteins/gabar-b3/) — Related eukaryotic Cys-loop receptor structure for comparison
- [Mouse 5-HT3A Receptor](/xray-mp-wiki/proteins/mouse-5ht3a-receptor/) — Related eukaryotic Cys-loop receptor structure
- [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) — Native neurotransmitter ligand of glycine receptors
- [Isothermal Titration Calorimetry (ITC)](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) — Used to measure strychnine binding thermodynamics to GlyRα3
