---
title: Human Serotonin Transporter (SERT)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature17629, doi/10.1038##ncomms11673]
verified: false
---

# Human Serotonin Transporter (SERT)

## Overview

The human serotonin transporter (SERT, also known as SLC6A4) is a neurotransmitter/sodium symporter (NSS) family member that terminates serotonergic signalling through the Na+/Cl--coupled reuptake of serotonin (5-HT) from the synaptic cleft into presynaptic neurons. SERT is a primary target for antidepressant drugs including selective serotonin reuptake inhibitors (SSRIs) such as (S)-citalopram and paroxetine, as well as psychostimulants. X-ray crystal structures of human SERT bound to (S)-citalopram and paroxetine at ~3.1 A resolution revealed how antidepressants lock the transporter in an outward-open conformation by binding to the central site, and identified an allosteric site at the extracellular vestibule that sterically hinders ligand unbinding.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature17629 | not specified (paper pre-dates PDB deposition) | 3.14 A | C222₁ | SERT ts3 — human SERT with thermostabilizing mutations Y110A, I291A, T439S, surface cysteine mutations C554A, C580A, C622A, fused to C-terminal GFP, twin Strep tag, and His10 tag; thrombin cleavage sites at N-terminus (after Gln76) and C-terminus (after Thr618); complexed with paroxetine and 8B6 Fab | paroxetine, CHS, N-acetylglucosamine, Na+, Cl-, 8B6 Fab |
| doi/10.1038##nature17629 | not specified (paper pre-dates PDB deposition) | 3.15 A | C222₁ | SERT ts3 — human SERT with thermostabilizing mutations Y110A, I291A, T439S, surface cysteine mutations C554A, C580A, C622A, fused to C-terminal GFP, twin Strep tag, and His10 tag; thrombin cleavage sites at N-terminus (after Gln76) and C-terminus (after Thr618); complexed with (S)-citalopram and 8B6 Fab | (S)-citalopram (central site and allosteric site), CHS, N-acetylglucosamine, Na+, Cl-, 8B6 Fab |
| doi/10.1038##nature17629 | not specified (paper pre-dates PDB deposition) | 4.53 A | C222₁ | SERT ts2 — human SERT with thermostabilizing mutations I291A, T439S, surface cysteine mutations C554A, C580A, C622A (lacks Y110A); fused to C-terminal GFP, twin Strep tag, and His10 tag; complexed with paroxetine and 8B6 Fab | paroxetine, CHS, N-acetylglucosamine, Na+, Cl-, 8B6 Fab |
| doi/10.1038##nature17629 | not specified (paper pre-dates PDB deposition) | 3.24 A | C222₁ | SERT ts3 — human SERT with thermostabilizing mutations Y110A, I291A, T439S, surface cysteine mutations C554A, C580A, C622A; (S)-citalopram soaked into paroxetine-bound crystals | (S)-citalopram (partially occupied at allosteric site), CHS, Na+, Cl- |
| doi/10.1038##nature17629 | not specified (paper pre-dates PDB deposition) | 1.62 A | P4₃2₁2 | 8B6 Fab — monoclonal antibody fragment against SERT | none (solved independently) |

## Expression and Purification

### Purification Workflow

- **Expression system**: HEK293S GnT- cells
- **Expression construct**: BacMam vector, C-terminal GFP fusion with twin Strep and His10 tags, thrombin cleavage sites

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and infection | Baculovirus-mediated transduction | HEK293S GnT- cells | standard cell culture media | Mammalian cells infected with SERT baculovirus |
| Membrane solubilization | Detergent solubilization | -- | 50 mM Tris pH 8, 150 mM NaCl, 20 mM DDM, 2.5 mM CHS, 0.5 mM DTT, 1 µM inhibitor (paroxetine, (S)-citalopram, or Br-citalopram) + 20 mM DDM | Membranes harvested and solubilized |
| Affinity chromatography | Strep Tactin affinity chromatography | Strep Tactin resin | 20 mM Tris pH 8, 150 mM NaCl, 0.05% DDM + 0.05% DDM | Large-scale purification of SERT |
| Size exclusion chromatography | Size exclusion chromatography | Superdex 200 | 20 mM Tris pH 8, 150 mM NaCl, 0.02% DDM, 0.1 mM CHS + 0.02% DDM | Monodisperse fractions collected |


## Crystallization

### doi/10.1038##nature17629

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | SERT ts3 — paroxetine complex with 8B6 Fab |
| Reservoir | not specified |
| Notes | Outward-open conformation, C222₁ space group |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | SERT ts3 — (S)-citalopram complex with 8B6 Fab |
| Reservoir | not specified |
| Notes | (S)-citalopram bound to both central and allosteric sites, C222₁ space group |

| Parameter | Value |
|---|---|
| Method | Crystal soaking |
| Protein sample | SERT ts3 — paroxetine-bound crystals |
| Reservoir | not specified |
| Notes | Partial occupancy at allosteric site |


## Biological / Functional Insights

### Antidepressant binding to the central site

(S)-citalopram and paroxetine both bind to the central binding site (S1) located between transmembrane helices 1, 3, 6, 8 and 10. The amine groups of both drugs occupy subsite A and interact with the conserved Asp98 carboxylate at distances of 4.1 A ((S)-citalopram) and 3.1 A (paroxetine), explaining paroxetine's higher affinity. Tyr95 forms a cation-pi interaction beneath the amine groups. The drugs lock SERT in an outward-open conformation, wedging between scaffold helices 3, 8, 10 and core helices 1, 6, directly blocking serotonin binding.

### Allosteric site identification

A second (S)-citalopram molecule was found in an allosteric site at the periphery of the extracellular vestibule, approximately 13 A from the central site. The allosteric site is interposed between extracellular loops 4 and 6 and transmembrane helices 1, 6, 10 and 11. A maltose detergent head group was also observed in the allosteric site in the paroxetine complex. Occupancy of this allosteric site sterically hinders ligand unbinding from the central site, providing a structural explanation for (S)-citalopram's action as an allosteric ligand.

### Allosteric modulation of inhibitor dissociation

100 µM (S)-citalopram decreased the first-order rate of 3H-citalopram dissociation by nearly tenfold (0.0032 ± 0.0007 versus 0.025 ± 0.002 min⁻¹), with wild-type and ts2 transporters showing similar effects. This demonstrates that allosteric modulation of ligand unbinding is intact in the ts2 and ts3 constructs. The malleability of the allosteric site suggests a spectrum of small molecules could range from inhibiting to enhancing transport activity.

### Ion binding sites

Two sodium binding sites (Na1 and Na2) and one chloride binding site (Cl-) were identified. Na1 is coordinated by Ala96-CO, Asn101-Oδ1, Ser336-Oγ, Ser336-CO, and Asn368-Oδ1 with mean distance 2.4 A. Cl- is coordinated by Tyr121-OH, Gln332-Nε, Ser336-Oγ, and Ser372-Oγ with mean distance 3.1 A. Na2 is coordinated by Gly94-CO, Val97-CO, Leu434-CO, Asp437-Oδ1, and Ser438-Oγ with mean distance 2.4 A.

### Extracellular and intracellular gates

Ytr176 and Phe335 define the extracellular gate, separated by 10 A, providing open access to the extracellular vestibule. The intracellular gate is closed, similar to outward-facing conformations of dDAT and LeuT, precluding direct access from the central ligand binding site to the intracellular solution. Tyr176 and Asp98 are separated by 4.0 A, and TM10 is closer to TM1b, bringing Glu494 and Arg104 within 4.8 A.

### N-linked glycosylation

EL2 is predicted to contain two N-linked glycosylation sites, Asn208 and Asn217. Electron density for an N-acetylglucosamine moiety was found linked to Asn208, and weak density was also found near Asn217. A conserved disulfide bridge is formed between Cys200 and Cys209 in EL2.

### TM12 kink and cholesterol binding

TM12 has a pronounced kink halfway across the membrane, unlike LeuT but reminiscent of dDAT. A cholesterol hemisuccinate (CHS) molecule binds near TM12a, stacking against Trp573 in a groove formed by Leu577, Ile576, and Ala580. Crystal lattice packing occurs at the kink in TM12, generating an apparent SERT dimer, though SERT is a monomer in detergent.

### Leu99 critical for transport rate (inward-to-outward transition)

Mutational analysis of Leu99 in hSERT (equivalent to Leu25 in LeuT) was performed using a well-established serotonin uptake system based on expression of hSERT in HEK293MSR cells, which presents fully functional, uniformly oriented transporters. Leu99 was mutated to seven hydrophobic residues (Ala, Val, Ile, Met, Phe, Tyr, Trp). The Leu99Trp mutation was completely inactive in transport. Km values were similar to wild-type hSERT (0.8-1.5 times wild-type Km) for all active mutants, indicating substrate binding is largely unaffected. However, all active mutants exhibited significantly decreased Vmax (5-25% of wild-type), demonstrating that the rate-limiting inward-to-outward-facing transition is compromised by any Leu99 mutation. This shows a highly specific requirement for leucine at position 99 for proper transport dynamics.


## Cross-References

- [Drosophila Dopamine Transporter (dDAT)](/xray-mp-wiki/proteins/d-dopamine-transporter/) — NSS family homolog; structural comparison between SERT and dDAT reveals conserved architecture and distinct EL6/EL2 regions
- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/leut/) — NSS family prototype; SERT shares the LeuT-fold architecture with 12 transmembrane helices; Leu25 in LeuT corresponds to Leu99 in SERT
- [Neurotransmitter/Sodium Symporter (NSS) Family](/xray-mp-wiki/concepts/nss-family/) — SERT is a human member of the NSS family (SLC6A4)
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — SERT transport mechanism follows alternating access between outward-open and inward-facing states
- [Paroxetine](/xray-mp-wiki/reagents/ligands/paroxetine/) — SSRI antidepressant; cocrystal structure of SERT-ts3-paroxetine complex at 3.14 A
- [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) — NSS family substrate; dDAT substrate-bound structure for comparison
- [Cholesteryl Hemisuccinate (CHS)](/xray-mp-wiki/reagents/cholesteryl-hemisuccinate/) — Lipid additive; CHS molecule bound near TM12a in SERT crystals
- [Leu25 Gatekeeper Mechanism in NSS Transporters](/xray-mp-wiki/concepts/leu25-gatekeeper/) — Equivalent Leu99 in hSERT shown to be critical for transport rate; hSERT counter-transports K+
