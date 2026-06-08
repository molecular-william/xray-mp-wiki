---
title: AdiC Arginine/Agmatine Antiporter
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature08201, doi/10.1038##nature08741, doi/10.1038##nature10917]
verified: false
---

# AdiC Arginine/Agmatine Antiporter

## Overview

AdiC is an arginine/agmatine antiporter from the APC (amino acid-polyamine-organocation) superfamily of membrane proteins. It functions as a virtual proton pump in the extreme acid resistance system of Escherichia coli, importing L-arginine from the extracellular environment and exporting its decarboxylation product agmatine. AdiC forms a homodimer with each subunit containing 10 transmembrane helices arranged in two inverted repeat domains. The crystal structure, solved at 3.2 A resolution in complex with a Fab fragment, reveals an outward-open, substrate-free conformation with a prominent extracellular-facing central cavity. The substrate binding site is located at the cavity floor and involves conserved aromatic residues that stabilize substrates through cation-pi interactions.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature08201 | not specified | 3.2 A | P1 | Salmonella enterica serovar Typhimurium AdiC in complex with Fab21 fragment | none (substrate-free, outward-open state) |
| doi/10.1038##nature08741 | 3H5M | 3.0 A | I2_12_12_1 | Escherichia coli AdiC (Arg-bound) | L-arginine |
| doi/10.1038##nature08741 | 3H5M (rebuilt) | 3.62 A | P2_12_12_1 | Escherichia coli AdiC (rebuilt model, corrected register shift in TM6-8) | L-arginine |
| doi/10.1038##nature08741 | 3HQK | 3.2 A | P1 | Salmonella enterica serovar Typhimurium AdiC | none (substrate-free) |
| doi/10.1038##nature08741 | 3HQK (rebuilt) | 3.2 A | P1 | Salmonella enterica serovar Typhimurium AdiC (rebuilt model, corrected TM1b, TM5, TM6) | none (substrate-free) |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: not specified

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Size-exclusion chromatography | SEC | Superdex 200 | 100 mM NaCl, 5 mM decylmaltoside, 20 mM Tris-HCl pH 8 + 5 mM decylmaltoside | Purified from Salmonella enterica serovar Typhimurium AdiC-Fab21 complex |

**Final sample**: 8 mg/ml


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Reconstitution | Liposome reconstitution | not applicable | not specified + not specified | AdiC reconstituted in liposomes for transport assays |


## Crystallization

### doi/10.1038##nature08201

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | AdiC-Fab21 complex, 8 mg/ml in 100 mM NaCl, 5 mM decylmaltoside, 20 mM Tris-HCl pH 8 |
| Reservoir | 30-35% PEG 400, 100-200 mM CaCl2, 100 mM glycine pH 9-9.5 |
| Mixing ratio | 1:1 (protein to reservoir) |
| Temperature | 20 C |
| Growth time | 2-4 weeks |
| Cryoprotection | crystals frozen after 2-4 weeks |
| Notes | Crystals diffracted to 3.2 A. SeMet derivatives used for phasing. Data collected on NSLS, APS, and ALS. |


## Biological / Functional Insights

### Homodimer architecture with independent subunits

AdiC is a homodimer in detergent micelles and phospholipid membranes. Each subunit functions as an independent transporter, as demonstrated by transport assays with tandem constructs containing one wild-type and one W293L mutant subunit. The WT-Mut tandem showed roughly half the arginine uptake rate of WT-WT, eliminating cooperative transport models requiring substrate binding to both subunits during a single transport cycle. The homodimeric interface is provided by helices TM11 and TM12, which are non-participants in the inverted repeat symmetry.

### Inverted pseudo-two-fold symmetry and TM architecture

TM1-TM5 of AdiC align with TM6-TM10 turned upside down around a pseudo-two-fold axis nearly parallel to the membrane plane (Ca r.m.s.d. ~3.4 A). TM1 pairs with TM6, TM2 with TM7, and so on. This inverted repeat is not apparent in the primary sequence but is a hallmark of the APC superfamily architecture. The five transmembrane helices lining the central cavity are TM1, TM2, TM3, TM8, and TM9.

### Aromatic box substrate binding site

The central cavity floor is formed by a pair of aromatic side chains, Y93 and W293, projecting inward from TM3 and TM8. An additional aromatic residue, W202, hangs 10-15 A away on the cavity wall. These conserved residues are proposed to stabilize substrates through cation-pi interactions, solving the electrostatic problem of substrate binding in a hydrated region exposed to pH 2, where Glu/Asp side chains would be protonated and incapable of forming coulombic contacts. The cavity wall is completely devoid of charged side chains. Mutation of these aromatic residues inhibits transport activity.

### Outward-facing conformation and transport mechanism

The crystal structure captures AdiC in an outward-open, substrate-free conformation. The central cavity is an extracellular-facing aqueous cavern, approximately 25 A wide at the rim, tapering to a floor situated about halfway through the membrane. The cavity is cut off from the cytoplasmic solution by tightly packed protein approximately 15 A thick. This structure identifies a probable location for substrate binding at the cavity's floor, consistent with the alternating access mechanism. A dual-open mechanism with two different outward-open conformations of high and low substrate affinity is proposed.

### Structural similarity to Na+-coupled symporters

AdiC mirrors the common fold observed in four phylogenetically unrelated families of Na+-coupled solute transporters. Structural alignment with LeuT (Ca r.m.s.d. 3.1 A), BetP (3.6 A), Mhp1 (3.4 A), and SGLT1 (4.0 A) confirms a prediction based on hydropathy analysis of APC superfamily proteins. Beyond the transmembrane helix match, substrate bound in LeuT coincides with the region of AdiC where functionally critical residues Y93 and W293 reside. This highlights emerging questions of convergent evolution versus deep links among ostensibly unrelated membrane proteins.

### Three-gate transport mechanism with substrate-dependent binding sites

The Arg-bound AdiC structure reveals a three-gate mechanism controlling substrate exchange. Two substrate binding sites are proposed: one located between the proximal gate Trp202 and the middle gate Trp293, which favors Arg binding, and another between Trp293 and the distal gate (Tyr93, Glu208, and Tyr365), which prefers agmatine. In the Arg-bound structure, Trp202 rotates by 90 degrees and translocates by approximately 10 A compared to the substrate-free state, occluding Arg from the periplasmic side. Major conformational changes occur in TM2, TM6, and TM10, with TM6 exhibiting the most pronounced changes. The rebuilt model places Glu208 in the transport path, where it hydrogen bonds to Tyr93 and Tyr365, creating a more acidic substrate-binding cleft.

### ITC binding affinity measurements

Isothermal titration calorimetry (ITC) measurements show that wild-type E. coli AdiC binds L-arginine with a binding affinity of approximately 162 +/- 5 uM. The N22A missense mutant shows enhanced arginine binding with a Kd of 27.5 +/- 1.4 uM, representing a 6-fold stronger binding compared to wild-type AdiC. The difference in binding affinity between WT and N22A mutant suggests that Asn22 plays a role in modulating substrate release kinetics.

### Register shift corrections in deposited AdiC models

Examination of the deposited AdiC models revealed significant register shifts in transmembrane helices. The E. coli AdiC (PDB 3H5M) exhibits a register shift of 3-4 amino acids (one helical turn) in TM6, TM7, and TM8 compared to the rebuilt model, affecting functionally important residues including Trp202 and Glu208 in TM6, and Trp293 in TM8. The Salmonella AdiC (PDB 3HQK) model shows register shifts in TM1b, the C-terminal half of TM5, and TM6b, with shifts of approximately one amino acid (one quarter of a helical turn). The rebuilt models fit SeMet anomalous density data significantly better than the original deposited models.


## Cross-References

- [GadC Glutamate/GABA Antiporter](/xray-mp-wiki/proteins/gadc/) — Homologous APC superfamily member; structural comparison for transport mechanism
- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/leut/) — Structural template with similar fold; substrate bound in LeuT coincides with AdiC substrate binding site
- [APC Superfamily (Amino Acid-Polyamine-Organocation Transporter Family)](/xray-mp-wiki/concepts/apc-superfamily/) — AdiC belongs to the APC superfamily of membrane proteins
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — AdiC operates via alternating access between outward-open and inward-open conformations
- [Major Facilitator Superfamily](/xray-mp-wiki/concepts/mfs-transporter/) — MFS transporters share structural similarities with APC superfamily transporters
- [Virtual Proton Pump](/xray-mp-wiki/concepts/virtual-proton-pump/) — AdiC is the prototypical virtual proton pump in E. coli acid resistance
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/decylmaltoside/) — Detergent used for AdiC purification and solubilization
- [Fab21 Antibody Fragment](/xray-mp-wiki/reagents/antibodies/fab21/) — Fab fragment used to form complex for crystallographic phasing
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — SeMet derivatives used for anomalous dispersion phasing
- [Agmatine](/xray-mp-wiki/reagents/ligands/agmatine/) — Agmatine is the decarboxylation product of arginine and the exchanged substrate in AdiC-mediated Arg/Agm antiport
