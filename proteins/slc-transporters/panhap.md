---
title: PaNhaP Sodium/Proton Antiporter from Pyrococcus abyssi
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.7554##ELIFE.03579]
verified: false
---

# PaNhaP Sodium/Proton Antiporter from Pyrococcus abyssi

## Overview

PaNhaP is an electroneutral Na+/H+ antiporter from the hyperthermophilic archaeon *Pyrococcus abyssi*, belonging to the CPA1 (cation-proton antiporter 1) family. It exchanges one Na+ for one H+ with 1:1 stoichiometry, playing roles in intracellular pH and sodium homeostasis. PaNhaP is a functional homologue of the medically important human Na+/H+ exchanger NHE1 and serves as a structural model for understanding CPA1 transport mechanisms. It functions as a homodimer, with each protomer containing 13 transmembrane helices (H1-H13) arranged in an inverted 6-helix repeat. The structure was determined in two conformations (pH 8 and pH 4) by X-ray crystallography, with the substrate ion (Tl+ as Na+ surrogate) bound at pH 8. The ion-binding site at the deepest point of a negatively charged cytoplasmic funnel is coordinated by three acidic sidechains (Glu73, Asp130, Asp159), a water molecule, Ser155, and the main-chain carbonyl of Thr129. Transport activity is pH-dependent and cooperative at pH 6, mediated by allosteric coupling through His292 at the dimer interface.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##ELIFE.03579 | 4CZ8 | 3.15 | P21 | SeMet-labeled PaNhaP, CPD fusion cleaved | Na+ (substrate ion) |
| doi/10.7554##ELIFE.03579 | 4CZ9 | 3.5 | P64 | Native PaNhaP, CPD fusion cleaved | none (no bound Na+) |
| doi/10.7554##ELIFE.03579 | 4CZA | 3.2 | P21 | Native PaNhaP, thallium-soaked at pH 8 | Tl+ (Na+ surrogate) |

## Expression and Purification

- **Expression system**: Escherichia coli C41-(DE3)
- **Construct**: Codon-optimized PaNhaP (WP_010868413.1) with C-terminal CPD (cysteine protease domain) fusion
- **Notes**: CPD fusion allows tag-free elution by inositol-hexaphosphate cleavage. SeMet-labeled protein expressed in PASM-5052 medium with 5 mM beta-mercaptoethanol.
- **Induction**: ZYM-5052 autoinduction medium, 10 hr at 37°C

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane isolation | Ultracentrifugation | — | 20 mM Tris pH 7.4, 250 mM sucrose, 140 mM choline chloride | Membranes resuspended at 15 mg/ml protein |
| Solubilization | Detergent extraction | — | 20 mM Tris pH 7.4, 150 mM NaCl, 30% glycerol, 1.5% Cymal-5 | Overnight solubilization at 4°C, clarified at 100,000xg for 1 hr |
| Affinity chromatography | Talon resin (Co2+ affinity) | — | Wash buffer - 20 mM Tris pH 7.4, 300 mM NaCl, 10 mM imidazole, 0.15% Cymal-5 | Supernatant with 5 mM imidazole incubated 2 hr with Talon resin at 4°C. Elution with 20 uM inositol-hexaphosphate cleaves CPD tag |
| Size exclusion chromatography | SEC | Superdex 200 | 10 mM Na-Citrate pH 4.0, 300 mM NaCl, 0.15% Cymal-5 | Concentrated to 5 mg/ml. Pooled fractions diluted 1:4 with buffer containing 100 mM NaCl and re-concentrated |


## Crystallization

### doi/10.7554##ELIFE.03579

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | PaNhaP at 5 mg/ml in SEC buffer |
| Reservoir | 100 mM Tris/HCl pH 8.0, 100 mM CaCl2/MgCl2, 35-40% PEG 400 |
| Temperature | 20 |
| Growth time | 3 months |
| Cryoprotection | Direct vitrification in liquid nitrogen |
| Notes | Long needle-like crystals at pH 8. Used for SeMet SAD phasing and thallium soaks |

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | PaNhaP at 5 mg/ml in SEC buffer |
| Reservoir | 100 mM Na-Citrate pH 4.0, 100 mM CaCl2/MgCl2, 35-40% PEG 400 |
| Temperature | 20 |
| Growth time | 7 days |
| Cryoprotection | Direct vitrification in liquid nitrogen |
| Notes | Trapezoidal crystals at pH 4, up to 200 um. Different space group and cell dimensions from pH 8 crystals |


## Biological / Functional Insights

### Architecture of the ion-binding site

The Na+ binding site in PaNhaP is formed by three acidic sidechains (Glu73 from H3, Asp130 from H5 unwound stretch, Asp159 from H6), a water molecule held by Asp130, the hydroxyl group of Ser155, and the main-chain carbonyl of Thr129. The trigonal bipyramidal coordination geometry is similar to that in Na+-translocating F-ATPase c-rings. The ion retains partial hydration via the water molecule. All ion-binding residues are in the first half of the inverted repeat.

### pH-dependent conformational changes

At pH 4 (compared to pH 8), the dimer undergoes significant rearrangements: (1) all six inter-protomer ion pairs break due to protonation; (2) protomers tilt away from the dimer interface; (3) H1 extends by one helical turn; (4) Asp130 shifts 2.7 A into the ion-binding space; (5) Asn158 reorients to potentially regulate ion access. These changes disrupt the Na+ binding site and prevent ion binding at low pH.

### pH-dependent cooperativity and allosteric regulation

PaNhaP shows positive cooperative Na+ transport at pH 6 (Hill coefficient 1.9) but non-cooperative transport at pH 5 (Hill coefficient ~1.1). Cooperativity is mediated by His292 at the dimer interface through a pH-dependent allosteric coupling mechanism. At neutral/basic pH, cooperative increase in Na+ affinity inhibits substrate release, serving as a safety mechanism against excessive Na+ influx. This mirrors the pH-dependent cooperativity observed in human NHE1.

### Dual proton access pathways

Protons (likely as H3O+) can access the binding pocket via two routes: (1) the negatively charged cytoplasmic funnel extending between the 6-helix bundle and the dimer interface, which serves as the Na+ access/egress path; (2) a narrow polar channel defined by bundle helices H5c, H12c, H6, and H13. Using separate pathways for Na+ and H+ currents in opposite directions may be advantageous at high transport rates. The narrow polar channel likely involves the conserved Glu154/Arg337 salt bridge and Asn158.

### Structural model for human NHE1

PaNhaP shares key features with human NHE1, including dimeric architecture, 13 TMHs, CPA1 family conservation of unwound H5/H12 stretches, ion-binding residues (Ser155, Asp130, ND motif), functionally important Arg337/Arg362, and pH-dependent Na+ cooperativity (Hill coefficient ~1.8 at pH 6.8 for NHE1). PaNhaP serves as an excellent structural model for the membrane domain of NHE1, a major drug target for heart and kidney diseases.


## Cross-References

- [MjNhaP1 Sodium/Proton Antiporter](/xray-mp-wiki/proteins/slc-transporters/mjnhaP1/) — Closely related CPA1 antiporter from Methanocaldococcus jannaschii; same functional family with conserved rocking-bundle mechanism
- [Na+/H+ Antiporter NhaA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/nhaa/) — Related E. coli CPA2 antiporter; electrogenic (2H+:1Na+) versus electroneutral PaNhaP; different fold but similar transport principles
- [Rocking-Bundle Mechanism](/xray-mp-wiki/concepts/rocking-bundle-mechanism/) — PaNhaP uses a rocking-bundle alternating-access mechanism with 6-helix bundle tilting ~7 degrees during transport cycle
- [pH-Dependent Gating](/xray-mp-wiki/concepts/ph-dependent-gating/) — PaNhaP transport activity is strongly pH-dependent with a bell-shaped profile; pH regulates both ion binding affinity and dimer cooperativity
