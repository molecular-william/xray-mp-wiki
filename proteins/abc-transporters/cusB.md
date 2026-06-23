---
title: "CusB Membrane Fusion Protein"
created: 2026-05-27
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2009.08.029, doi/10.1038##nature09743]
verified: false
---

# CusB Membrane Fusion Protein

## Overview

CusB is a periplasmic membrane fusion protein (MFP) from Escherichia coli, functioning as a critical adaptor in the CusABC tripartite copper/silver efflux system. It bridges the inner-membrane efflux pump CusA and the outer-membrane channel CusC, mediating resistance to Cu+ and Ag+ ions. CusB is the first MFP structure solved from a heavy-metal efflux RND transporter. The protein adopts an elongated conformation with four distinct domains: three beta-strand domains and a unique three-helix bundle alpha-helical domain (Domain 4), contrasting with the two-helical hairpin motif found in other MFPs. Two distinct conformations (open and compact) were captured in a single crystal, demonstrating remarkable conformational flexibility. CusB contains multiple metal-binding sites for [Cu(i)](/xray-mp-wiki/reagents/ligands/cu(i)) and Ag(I), each coordinated by methionine residues, representing the first MFP-ligand complex structures.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2009.08.029 | 2L9P | 3.40 A | I222 | Full-length CusB with C-terminal 6xHis tag (residues 1-369) | Apo |
| doi/10.1016##j.jmb.2009.08.029 | 2L9Q | 3.78 A | I222 | Full-length CusB with C-terminal 6xHis tag | Copper(I) (Cu+) |
| doi/10.1016##j.jmb.2009.08.029 | 2L9R | 3.84 A | I222 | Full-length CusB with C-terminal 6xHis tag | Silver(I) (Ag+) |
| doi/10.1038##nature09743 | 3NE5 | 2.90 A | -- | CusB residues 79-400 (molecule 1) and 79-402 (molecule 2) in CusBA co-crystal; CusB forms hexameric channel with six protomers per [Cusa](/xray-mp-wiki/proteins/cusA) trimer | [Cymal 6](/xray-mp-wiki/reagents/detergents/cymal-6) |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3)
- **Construct**: Full-length CusB with C-terminal 6xHis tag, overproduced from pET15b cusB expression vector

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell growth and induction | Cells grown in 12 L LB medium with 100 ug/ml [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin) at 37 C, induced with 1 mM IPTG at OD600 ~0.5 | -- | LB medium with 100 ug/ml ampicillin + -- | Cells harvested within 4 h of induction |
| Cell lysis | Cells resuspended in 20 mM Na-[HEPES](/xray-mp-wiki/reagents/buffers/hepes) (pH 7.2), 100 mM NaCl and disrupted with French pressure cell; debris removed by centrifugation at 20,000 rpm for 45 min at 4 C | -- | 20 mM Na-Hepes (pH 7.2), 100 mM NaCl + -- | Crude lysate collected |
| Solubilization | Crude lysate supplemented with 0.5% n-dodecyl-beta-D-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm)) | -- | 20 mM Na-Hepes (pH 7.2), 100 mM NaCl + 0.5% DDM | Membrane fraction solubilized |
| Ni2+ affinity chromatography | Ni2+-affinity column chromatography | Ni2+-affinity resin | 20 mM Na-Hepes (pH 7.2), 100 mM NaCl + 0.5% DDM | His-tagged CusB captured on Ni2+ column |
| Size exclusion chromatography | G-200 sizing column chromatography | Superdex 200 | 20 mM Na-Hepes (pH 7.2), 100 mM NaCl + 0.5% DDM | Monodisperse fraction collected |
| Concentration and storage | Protein concentrated to 20 mg/ml | -- | 20 mM Na-Hepes (pH 7.5), 0.04% DDM + 0.04% DDM | Purity >95% by 10% SDS-PAGE stained with Coomassie Brilliant Blue |


## Crystallization

### doi/10.1016##j.jmb.2009.08.029

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 20 mg/ml CusB in 20 mM Na-Hepes (pH 7.5), 0.04% DDM |
| Reservoir | not specified in methods section |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Apo-CusB crystals grown at room temperature; Cu(I) and [Ag(i)](/xray-mp-wiki/reagents/ligands/ag(i)) complexes obtained by soaking metal ions into apo-crystals. Space group I222 for all forms. Two distinct conformations (molecules A and B) found in asymmetric unit. |

### doi/10.1038##nature09743

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | 0.1 mM CusA (native) and 0.1 mM CusB (SeMet-substituted) in 20 mM Na-HEPES pH 7.5, 0.05% CYMAL-6 |
| Reservoir | 10% PEG 6000, 0.1 M Na-HEPES pH 7.5, 0.1 M ammonium acetate, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol) |
| Temperature | Room temperature |
| Growth time | 2 months |
| Cryoprotection | Stepwise glycerol increase to 30% in 5% increments |
| Notes | CusA-CusB co-crystal. SAD phasing used with six selenium sites per CusB molecule. Model consists of 1,686 amino acid residues (CusA residues 4-1043, CusB mol 1 residues 79-400, CusB mol 2 residues 79-402). |


## Biological / Functional Insights

### Unique three-helix bundle Domain 4

Unlike other known MFP structures (AcrA, MexA, MacA) which possess a two-helical hairpin motif, CusB Domain 4 folds into a three-helix bundle. This helix-turn-helix-turn-helix secondary structure creates an approximately 27-A-long structure, making it at least 20 A shorter than the two-helical hairpin domains of MexA and AcrA. CusB is the only periplasmic MFP protein known to possess this three-helical domain instead of a two-helical hairpin motif. The three-helix bundle is presumably located near the outer membrane and may interact with the periplasmic domain of [Cusc](/xray-mp-wiki/proteins/cusC).

### Conformational flexibility and hinge motion

Two distinct conformations of CusB were captured in a single crystal, suggesting the MFP is highly flexible. Molecule A adopts a more open conformation while molecule B exhibits a compact form. Superimposition gives an overall RMSD of 2.6 A over C-alpha atoms. The hinge region, composed of two loops (residues 116-120 and 240-242) between Domains 2 and 3, permits rigid-body movement. When Domains 1+2 are superimposed, the alpha-helical domains differ by approximately 21 degrees. When Domains 3+4 are superimposed, the beta-barrels of Domain 1 shift by approximately 23 degrees. This flexibility may allow CusB to accommodate different states during the efflux cycle.

### Multiple metal-binding sites with methionine coordination

CusB contains multiple Cu(I) and Ag(I) binding sites, each coordinated by one methionine residue. In the CusB-Cu(I) complex, four Cu+ binding sites were identified in the asymmetric unit: sites C1 and C2 in molecule A, and C1' and C2' in molecule B. Site C1 is located in Domain 1 (N- and C-termini region) and is coordinated by M324, F358, and R368. Site C2 is in Domain 4 (three-helix bundle) and is coordinated by M190, W158, and Q162. For Ag(I), a single binding site A1 was identified next to M324 in molecule A, coordinated by the same residues M324, F358, and R368. This methionine-only coordination mode is distinct from other copper tolerance proteins (CusF, CucR, Atx1) which use two-methionine or two-cysteine binding pockets.

### CusA-CusB interaction interface

Cross-linking mass spectrometry revealed that the N-terminal region of CusB (residues 84-101, polypeptide beta: IDPTQTQNLGVKTATVTR) directly interacts with the periplasmic domain of CusA (residues 148-157, polypeptide alpha: SGKHDLADLR). Domain 1 of CusB, formed by the N- and C-terminal ends, interacts with the periplasmic domain of the CusA transporter. This interaction site corresponds to the PC1 region of [Acrb](/xray-mp-wiki/proteins/acrB), analogous to how AcrA interacts with AcrB. The structural model of CusA was generated based on the AcrB crystal structure and sequence alignment, indicating that the CusA periplasmic domain (residues 148-157) is located directly above the vestibule region, facing the periplasm.

### Hexameric CusB channel formation

The co-crystal structure revealed that six CusB protomers assemble into a continuous funnel-like channel with the central channel formed along the crystallographic three-fold symmetry axis. Domain 1 and the lower half of domain 2 create a cap-like structure, while the upper half of domain 2, together with domains 3 and 4, contribute to the central channel. The channel is approximately 62 A in length with an average internal diameter of approximately 37 A, giving a volume of approximately 65,000 A^3. The inner surface is predominantly negatively charged, suggesting capacity to bind positively charged metal ions. The narrowest section is at residue D232 of each CusB protomer, close to the hinge region between domains 3 and 4. The widest section forms at the top edge with an inner diameter of approximately 56 A. The alpha-helices of domain 4 create an inverted conical structure.

### CusA-CusB binding affinity by ITC

Isothermal titration calorimetry measurements determined the equilibrium dissociation constant for CusB binding to the CusA pump as 5.1 +/- 0.3 uM. This micromolar-range affinity is consistent with a functional adaptor interaction in the tripartite efflux complex.

### Metal ion relay via N-terminal methionine residues

The N-terminal residues M49, M64 and M66 of CusB are proposed to form a three-methionine metal-binding site. Although these residues are intrinsically disordered and not visible in electron density maps, the co-crystal structure shows that the N-terminal tails of CusB molecules are located outside the cleft between PC1 and PC2 subdomains of the CusA pump. This positioning suggests CusB may help transfer metal ions via the N-terminal three-methionine binding site into the periplasmic cleft of CusA. The proposed metal transport pathway is: (1) Cu(I)/Ag(I) ions delivered from CusF chaperone to the three-methionine binding site (M49, M64, M66) at the CusB N-terminal tail; (2) transfer from CusB to the three-methionine cluster (M573, M623, M672) inside the periplasmic cleft of CusA; (3) release to the nearest methionine pair (M271-M755) located above the three-methionine binding site of CusA; (4) extrusion through the CusC channel.

### CusC3-CusB6-CusA3 tripartite complex model

A structural model of the complete CusC3-CusB6-CusA3 tripartite efflux complex was constructed based on the CusBA crystal complex structure and the predicted CusC model. The final model represents a 750-kDa complex that spans both the inner and outer membranes of E. coli and extrudes Cu(I) and Ag(I) ions. This model integrates the trimeric CusA pump, hexameric CusB channel, and predicted trimeric CusC outer membrane channel into a functional efflux assemblage.


## Cross-References

- [AcrB Multidrug Efflux Pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) — AcrB is the prototypical RND efflux pump; CusA structural model based on AcrB structure
- [MexB Efflux Pump](/xray-mp-wiki/proteins/abc-transporters/mexB/) — MexB is a P. aeruginosa RND efflux pump homologous to CusA
- [AcrA Membrane Fusion Protein](/xray-mp-wiki/proteins/abc-transporters/acra/) — AcrA is the MFP partner of AcrB; CusB compared structurally to AcrA
- [MexA Membrane Fusion Protein](/xray-mp-wiki/proteins/mexA/) — MexA is the P. aeruginosa MFP homolog; CusB superimposed with MexA showing domain similarities
- [TolC Outer Membrane Channel](/xray-mp-wiki/proteins/abc-transporters/tolc/) — TolC is the outer-membrane channel of the AcrAB-TolC system; CusC is the functional homolog in CusABC
- [OprM Outer Membrane Channel](/xray-mp-wiki/proteins/oprM/) — OprM is the P. aeruginosa outer-membrane channel; similar elongated alpha-helical tunnel structure
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — DDM (0.5% solubilization, 0.04% crystallization) used throughout purification and crystallization
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — SeMet-CusB used for MAD phasing in structure determination
- [CUSC](/xray-mp-wiki/proteins/cusC) — Entity mentioned in text
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes) — Entity mentioned in text
