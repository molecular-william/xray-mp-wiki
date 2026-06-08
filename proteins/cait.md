---
title: CaiT Carnitine Antiporter from Escherichia coli
created: 2026-06-05
updated: 2026-06-05
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.1788]
verified: false
---

# CaiT Carnitine Antiporter from Escherichia coli

## Overview

CaiT is an L-carnitine/gamma-butyrobetaine antiporter from Escherichia coli that belongs to the betaine/choline/carnitine transporter (BCCT) family. Unlike other BCCT family members which are Na+/H+-dependent symporters, CaiT functions as a precursor/product antiporter independently of the ion gradient. The crystal structure at 3.15 A resolution reveals a homotrimeric complex with each protomer containing 12 transmembrane helices and 4 L-carnitine molecules outlining the transport pathway across the membrane. Mutagenesis studies identified a primary binding site at the center of the protein and a secondary substrate-binding site at the bottom of the intracellular vestibule, providing mechanistic insights into the antiport process.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.1788 | 3HFX | 3.15 A | P6(3) | CaiT from E. coli, residues 12-504, C-terminal GFP-His10 tag with TEV cleavage site, Met353 mutated to Leu; homotrimer | L-carnitine (4 molecules per protomer) |

## Expression and Purification

- **Expression system**: Escherichia coli C41
- **Construct**: CaiT from E. coli cloned into pET28-derivative vector with C-terminal GFP-His10 tag and TEV protease cleavage site; Met353 mutated to Leu by sequencing; cultured in Terrific broth, induced with 0.3 mM IPTG at 18 C for 20 h

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell membrane isolation | Cell lysis and membrane fractionation | not applicable | not specified + DDM | Cells cultured in Terrific broth, induced with 0.3 mM IPTG at 18 C for 20 h; membranes isolated from disrupted C41 cells |
| Membrane solubilization | Detergent solubilization | not applicable | not specified + DDM (1% w/v) | Membranes solubilized with 1% (w/v) n-dodecyl beta-D-maltoside (DDM) |
| Metal affinity chromatography (first pass) | Ni-NTA metal ion affinity chromatography | Ni-NTA | 20 mM Tris-HCl pH 8.0, 300 mM NaCl, 200 mM imidazole, 0.05% DDM + DDM | GFP-CaiT eluted from Ni-NTA column; contains C-terminal GFP-His10 tag |
| TEV protease cleavage | Protease digestion | not applicable | not specified + not specified | TEV protease cleavage site between GFP-His10 and CaiT; removes GFP-His10 tag |
| Metal affinity chromatography (second pass) | Ni-NTA metal ion affinity chromatography | Ni-NTA | not specified + not specified | Second Ni-column separates CaiT from TEV-His and GFP-His; CaiT flows through |
| Size exclusion chromatography | Size exclusion chromatography | Superdex 200 10/300 GL column (GE Healthcare) | 50 mM HEPES-NaOH pH 7.5, 150 mM NaCl, 0.03% DDM + DDM | Final SEC purification; concentrated to 10 mg/ml using 100-kDa Amicon Ultra-4 tube at 4 C |


## Crystallization

### doi/10.1038##nsmb.1788

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | CaiT at 10 mg/ml in 0.03% DDM |
| Reservoir | 0.1 M HEPES-NaOH pH 7.5, 20-26% (v/v) PEG-400, 0.1 M NaCl, 18 mM N-octyl-beta-D-glucopyranoside, 5 mM L-carnitine |
| Temperature | 20 C |
| Growth time | not specified |
| Notes | Crystals grown by hanging-drop vapor diffusion at 20 C. Heavy atom derivatives obtained by soaking crystals in mother liquor containing 5 mM ethylmercurithiosalicylic acid and sodium salt. Cryoprotected with reservoir solution containing 30% PEG-400, 0.020% DDM, and 10 mM N-octyl-beta-D-glucopyranoside. Space group P6(3), cell dimensions a=b=134.2 A, c=85.1 A, alpha=beta=90 deg, gamma=120 deg. Phased by SIRAS using mercury peak-wavelength (1.0039 A) dataset. Model contains residues 12-504, nine mercury atoms, and four L-carnitine molecules. Rwork/Rfree = 0.262/0.281. |


## Biological / Functional Insights

### BCCT family antiporter with unique Na+-independent mechanism

CaiT belongs to the betaine/choline/carnitine transporter (BCCT) family but functions as a precursor/product antiporter independently of the ion gradient, unlike all other BCCT members which are Na+ or H+ dependent symporters. The conserved Na+-binding motif (Gly-X-Gly in TM3) is altered to Cys-Thr-Ser in CaiT, and key Na+-coordinating residues from BetP are mutated (Ser468 to Leu422 in TM10, Met310 to Ser263 in TM7), disrupting the Na+-binding site.

### Four L-carnitine binding sites outline transport pathway

The crystal structure reveals four L-carnitine molecules per protomer: LC-I (primary binding site, center of protein), LC-II (secondary cytoplasmic site at bottom of intracellular vestibule), LC-III (extracellular surface cavity), and LC-IV (entrance of intracellular vestibule). LC-I forms hydrogen bonds with Gly253, Gly254, Gly257, Ser310, Ser313, and Trp316, and cation-pi interactions with Trp316 and Tyr319. LC-II interacts with Tyr327 and Gln330. LC-III interacts with Gly310, Trp316, and Tyr114. LC-IV contacts Glu85 and Arg337.

### Mutagenesis reveals functional binding sites

Mutagenesis of LC-II-interacting residues Y327L and Q330L markedly reduced carnitine uptake, supporting the existence of a cytoplasmic secondary substrate-binding site (Sin1). W316L (Trp316L) reduced transport rate by approximately 70%, while Y114L had minor effect, indicating the importance of aromatic residues at the periplasmic barrier top in transport activity.

### Cytoplasmic gate conformational rearrangement

Structural comparison with BetP (occluded state) reveals that Tyr327 and Gln330 in CaiT (corresponding to Trp377 and Phe380 in BetP) coordinate with LC-II and deviate to allow inward or outward permeation, suggesting LC-II binding is associated with conformational rearrangements favoring opening of the cytoplasmic gate. Intracellular portions of TM3, TM4, TM8, and TM10 in CaiT deviate by approximately 2 Angstroms from corresponding BetP portions.

### Homotrimeric architecture with 12 TM helices

CaiT crystallizes as a homotrimer with a threefold axis perpendicular to the membrane plane. Each protomer contains 12 transmembrane helices (TM1-TM12) with both N and C termini exposed to the cytoplasm. The monomer resembles a cylinder with maximum height of 52 Angstroms and maximum diameter of 45 Angstroms. TM3-TM12 form a structural core similar to the Na+-coupled symporter BetP and cores of unrelated transporters LeuT, vSGLT, and Mhp1.


## Cross-References

- [Betaine/Choline/Carnitine Transporter (BCCT) Family](/xray-mp-wiki/concepts/bcct-family/) — CaiT belongs to the BCCT family; unique Na+-independent antiport mechanism distinguishes it from other BCCT members
- [BetP Betaine Transporter from Bacillus subtilis](/xray-mp-wiki/proteins/betp/) — Structural comparison with BetP (occluded state) provides insights into cytoplasmic gate mechanism
- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/leut/) — Core architecture comparison; LC-II reciprocal position of LeuT second binding site; outward-facing conformational state speculation
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — CaiT operates via alternating-access mechanism between inward-facing and outward-facing conformations
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for CaiT solubilization, purification, and cryoprotection
- [n-Octyl-beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-glucopyranoside/) — Detergent used in crystallization and cryoprotection
- [HEPES (4-(2-hydroxyethyl)-1-piperazineethanesulfonic acid)](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in SEC and crystallization (HEPES-NaOH pH 7.5)
- [TEV Protease (Tobacco Etch Virus Protease)](/xray-mp-wiki/reagents/protein-tags/tevp-protease/) — TEV protease used for cleavage of C-terminal GFP-His10 tag during purification
- [Mercury (HgCl2)](/xray-mp-wiki/reagents/additives/mercury/) — Mercury compound (ethylmercurithiosalicylate) used for SIRAS phasing in crystal structure determination
- [L-Carnitine](/xray-mp-wiki/reagents/ligands/l-carnitine/) — Endogenous substrate and ligand of CaiT; four molecules observed per protomer in crystal structure
- [Gamma-Butyrobetaine](/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/) — Endogenous substrate of CaiT antiport exchange with L-carnitine
