---
title: "AdiC Arginine/Agmatine Antiporter"
created: 2026-06-02
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1186##s12915-021-01102-4, doi/10.1038##nature08201, doi/10.1038##nature08741, doi/10.1038##nature10917, doi/10.1126##science.1173654, doi/10.1073##pnas.1605442113, doi/10.1073##pnas.1018081108]
verified: false
---

# AdiC Arginine/Agmatine Antiporter

## Overview

AdiC is an arginine/agmatine antiporter from the APC (amino acid-polyamine-organocation) superfamily of membrane proteins. It functions as a virtual proton pump in the extreme acid resistance system of Escherichia coli, importing [L-Arginine](/xray-mp-wiki/reagents/substrates/l-arginine) from the extracellular environment and exporting its decarboxylation product agmatine. AdiC forms a homodimer with each subunit containing 10 transmembrane helices arranged in two inverted repeat domains. The crystal structure, solved at 3.2 A resolution in complex with a Fab fragment, reveals an outward-open, substrate-free conformation with a prominent extracellular-facing central cavity. The substrate binding site is located at the cavity floor and involves conserved aromatic residues that stabilize substrates through cation-pi interactions.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature08201 | 3NCY | 3.2 A | P1 | Salmonella enterica serovar Typhimurium AdiC in complex with [Fab21 Antibody Fragment](/xray-mp-wiki/reagents/antibodies/fab21) fragment | none (substrate-free, outward-open state) |
| doi/10.1038##nature08741 | 3H5M | 3.0 A | I2_12_12_1 | Escherichia coli AdiC (Arg-bound) | [L-Arginine](/xray-mp-wiki/reagents/substrates/l-arginine) |
| doi/10.1038##nature08741 | 3H5M | 3.62 A | P2_12_12_1 | Escherichia coli AdiC (rebuilt model, corrected register shift in TM6-8) | [L-Arginine](/xray-mp-wiki/reagents/substrates/l-arginine) |
| doi/10.1038##nature08741 | 3HQK | 3.2 A | P1 | Salmonella enterica serovar Typhimurium AdiC | none (substrate-free) |
| doi/10.1038##nature08741 | 3HQK | 3.2 A | P1 | Salmonella enterica serovar Typhimurium AdiC (rebuilt model, corrected TM1b, TM5, TM6) | none (substrate-free) |
| doi/10.1126##science.1173654 | 3LRB | 3.6 | P2_12_12_1 (also solved in P1) | Escherichia coli O157:H7 AdiC (arginine/agmatine antiporter) | none (outward-facing, open conformation) |
| doi/10.1073##pnas.1605442113 | 5J4N | 2.6 |  | Wild-type E. coli AdiC with bound agmatine (Agm) | Agmatine |
| doi/10.1073##pnas.1605442113 | 5J4N | 2.2 |  | Wild-type E. coli AdiC (substrate-free) | none |
| doi/10.1073##pnas.1018081108 | 3OB6 | 3.0 |  | E. coli AdiC N101A mutant co-crystallized with 1 mM L-arginine | [L-Arginine](/xray-mp-wiki/reagents/substrates/l-arginine) |
| doi/10.1186##s12915-021-01102-4 | 7O82 | 1.7 | P 1 21 1 | Wild-type E. coli AdiC (outward-open, substrate-free) | none |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: not specified

### Purification Workflow

#### Source: doi/10.1038##nature08201


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200) | 100 mM NaCl, 5 mM [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/decylmaltoside), 20 mM Tris-HCl pH 8 + 5 mM [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/decylmaltoside) | Purified from Salmonella enterica serovar Typhimurium AdiC-[Fab21 Antibody Fragment](/xray-mp-wiki/reagents/antibodies/fab21) complex |

**Final sample**: 8 mg/ml


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Reconstitution | Liposome reconstitution | not applicable | not specified + not specified | AdiC reconstituted in liposomes for transport assays |

#### Source: doi/10.1073##pnas.1605442113

- **Expression system**: Escherichia coli
- **Expression construct**: Wild-type AdiC and mutants

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cloning, overexpression and purification | As described previously |  |  | AdiC was cloned, overexpressed and purified as described previously (ref 22) |


## Crystallization

### doi/10.1038##nature08201

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | AdiC-Fab21 complex, 8 mg/ml in 100 mM NaCl, 5 mM [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/decylmaltoside), 20 mM Tris-HCl pH 8 |
| Reservoir | 30-35% PEG 400, 100-200 mM CaCl2, 100 mM [Glycine](/xray-mp-wiki/reagents/buffers/glycine) pH 9-9.5 |
| Mixing ratio | 1:1 (protein to reservoir) |
| Temperature | 20 C |
| Growth time | 2-4 weeks |
| Cryoprotection | crystals frozen after 2-4 weeks |
| Notes | Crystals diffracted to 3.2 A. SeMet derivatives used for phasing. Data collected on NSLS, APS, and ALS. |

### doi/10.1073##pnas.1605442113

| Parameter | Value |
|---|---|
| Protein sample | Purified wild-type AdiC |
| Notes | Crystallization details in SI Methods. Crystals grown at Swiss Light Source, beamline X06SA. |


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

AdiC mirrors the common fold observed in four phylogenetically unrelated families of Na+-coupled solute transporters. Structural alignment with LeuT (Ca r.m.s.d. 3.1 A), [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/betp) (3.6 A), Mhp1 (3.4 A), and SGLT1 (4.0 A) confirms a prediction based on hydropathy analysis of APC superfamily proteins. Beyond the transmembrane helix match, substrate bound in LeuT coincides with the region of AdiC where functionally critical residues Y93 and W293 reside. This highlights emerging questions of convergent evolution versus deep links among ostensibly unrelated membrane proteins.

### Three-gate transport mechanism with substrate-dependent binding sites

The Arg-bound AdiC structure reveals a three-gate mechanism controlling substrate exchange. Two substrate binding sites are proposed: one located between the proximal gate Trp202 and the middle gate Trp293, which favors Arg binding, and another between Trp293 and the distal gate (Tyr93, Glu208, and Tyr365), which prefers [Agmatine](/xray-mp-wiki/reagents/ligands/agmatine). In the Arg-bound structure, Trp202 rotates by 90 degrees and translocates by approximately 10 A compared to the substrate-free state, occluding Arg from the periplasmic side. Major conformational changes occur in TM2, TM6, and TM10, with TM6 exhibiting the most pronounced changes. The rebuilt model places Glu208 in the transport path, where it hydrogen bonds to Tyr93 and Tyr365, creating a more acidic substrate-binding cleft.

### ITC binding affinity measurements

Isothermal titration calorimetry (ITC) measurements show that wild-type E. coli AdiC binds [L-Arginine](/xray-mp-wiki/reagents/substrates/l-arginine) with a binding affinity of approximately 162 +/- 5 uM. The N22A missense mutant shows enhanced arginine binding with a Kd of 27.5 +/- 1.4 uM, representing a 6-fold stronger binding compared to wild-type AdiC. The difference in binding affinity between WT and N22A mutant suggests that Asn22 plays a role in modulating substrate release kinetics.

### Register shift corrections in deposited AdiC models

Examination of the deposited AdiC models revealed significant register shifts in transmembrane helices. The E. coli AdiC (PDB 3H5M) exhibits a register shift of 3-4 amino acids (one helical turn) in TM6, TM7, and TM8 compared to the rebuilt model, affecting functionally important residues including Trp202 and Glu208 in TM6, and Trp293 in TM8. The Salmonella AdiC (PDB 3HQK) model shows register shifts in TM1b, the C-terminal half of TM5, and TM6b, with shifts of approximately one amino acid (one quarter of a helical turn). The rebuilt models fit SeMet anomalous density data significantly better than the original deposited models.

### Outward-facing open conformation of E. coli O157:H7 AdiC

The crystal structure of AdiC from E. coli O157:H7 was determined at 3.6 Å resolution by osmium-based SAD phasing. The structure exists in an outward-facing, open conformation. AdiC has 12 TMs arranged in a two-layer architecture: inner layer (TM1, TM3, TM6, TM8, TM10) surrounded by outer layer (TM2, TM4, TM5, TM7, TM9, TM11, TM12). TM1-TM5 display inverted pseudo-two-fold symmetry with TM6-TM10 (RMSD 3.7 Å over 116 Cα atoms). TM1 and TM6 contain short nonhelical Gly-containing loops: the GSG motif (Gly25-Ser26-Gly27) in TM1 and the GVESA motif (Gly206-Val-Glu-Ser-Ala210) in TM6, which are signature sequences of the APA family. The homodimeric interface involves TM11 and TM12 from each subunit. A central cavity opens to the periplasm, lined by invariant residues including the GSG motif, Tyr87, Tyr101, Val217, Asn219, and the GVESA motif from TM6, and Cys286, Ser289, Leu290, Trp293 from TM8, and Val358 from TM10. Glu208 is proposed as a pH sensor that remains protonated at periplasmic pH and undergoes deprotonation at cytoplasmic pH, driving the antiport cycle.

### Four-step antiport mechanism of AdiC

Based on structural and biochemical analysis, a four-step antiport mechanism is proposed: Step 1 — substrate (Arg) binding results in occlusion from the periplasm; Step 2 — the antiporter switches to an inward-facing conformation where Arg is competitively displaced by Agm; Step 3 — the antiporter closes and occludes the substrate from the cytoplasm; Step 4 — the antiporter opens to the periplasm, releasing Agm. The default state is the outward-facing, open conformation captured in the crystal structure. Y93K mutation cripples binding to both Arg and Agm; Y87A reduces Agm binding; Y365A reduces Arg binding. ITC measurements show AdiC binds Agm with ~8x higher affinity than Arg.

### High-resolution wild-type AdiC structures reveal water molecules in substrate binding

The crystal structures of wild-type AdiC with bound agmatine at 2.6 Å and substrate-free at 2.2 Å resolution were solved. The high-resolution structures enabled identification of crucial water molecules in the substrate-binding sites. In the substrate-free structure, four water molecules (H2O1-H2O4) occupy the binding pocket, with H2O2 and H2O4 mimicking the hydrophilic portions of agmatine. In the agmatine-bound structure, a water molecule (H2O1) bridges the interaction between Ser357 (TM10) and the agmatine guanidinium group. These structures provide the most accurate view of the wild-type AdiC substrate binding mechanism to date.

### Agmatine release mechanism via conformational changes

A potential mechanism for agmatine release was proposed based on morphing between the outward-facing occluded Arg-bound structure and the outward-open Agm-bound and substrate-free structures. The mechanism involves: protonation of Glu208 under extreme acidic conditions abolishing electrostatic interaction with agmatine, rearrangement of hydrogen bonds at the intracellular gate, rotation of the Met104 methylmercapto group by ~180 degrees, and replacement of agmatine by water molecules from bulk solution.

### Ligand binding affinity measurements by scintillation proximity assay

Scintillation proximity assay (SPA) binding measurements showed wild-type AdiC has an approximately threefold higher affinity for agmatine (Ki = 56 µM) compared to arginine (Ki = 148 µM). The N22A mutant shows inverted specificity with higher affinity for arginine than agmatine. Mutants N101A and W293A show strongly impaired binding. The M104A mutation reduces agmatine affinity by ~50%, indicating a significant interaction between the Met104 sulfur atom and the guanidinium group of agmatine.

### 1.7 A resolution structure of AdiC reveals extensive water networks

The structure of AdiC was determined at an unprecedented resolution of 1.7 A by X-ray crystallography. This high resolution allowed identification of 21 and 15 water molecules in the substrate-binding sites of monomers A and B, respectively, compared to only 7 water molecules at 2.2 A resolution. Seven water molecules were identified as placeholders for substrate (L-arginine/agmatine) atoms, preserving binding site geometry in the substrate-free state. MD simulations confirmed the presence of six of these seven placeholder waters with occupancies ranging from 17% to 74%. The work demonstrates that water molecules play a critical role in stabilizing the protein and substrate-binding site, and act as structural placeholders for substrate atoms.

### Gate flexibility: W202 mobile, W293 restrained

MD simulations of the 1.7 A structure revealed differential flexibility of AdiC gating residues. The outward-facing thin gate W202 (proximal gate) is mobile and samples a large range of conformations, while the middle gate W293 is restrained by a water-mediated hydrogen bond network involving H2O9 and residues N22, S289, and S298. Based on this, a refined transport cycle is proposed where W202 screens for substrate in the outward-open state, while W293 is mobile in the inward-open state looking for agmatine.

### Water-filled cavity at the dimer interface stabilizes the AdiC homodimer

A water-filled cavity was identified at the dimer interface of AdiC, with bridging interactions through water-mediated hydrogen bonds between monomers. MD simulations confirmed the cavity is occupied by approximately 2 water molecules on average, preferentially at positions a-d. Point mutations disrupting the interfacial water network (Q88E, Y367F, T421V) validated the importance of water molecules for dimer stabilization. The Y367F mutant showed the most dramatic thermostability reduction of almost 10 C.

### N101A mutant reveals substrate-induced transition fit mechanism

The crystal structure of AdiC N101A mutant bound to Arg+ at 3.0 A resolution captures an open-to-out Arg+-bound intermediate state, completing the picture of major conformational states during the transport cycle of 5+5 inverted repeat fold transporters. In the N101A mutant, the Arg+ guanidinium group is mislocalized and travels freely between Trp293 (TM8) and Trp202 (TM6a), in contrast to wild-type where it is restricted near Trp293. The N101A mutant shows V_MAX ~1% of wild-type while K_M (~100 uM) is only slightly altered compared to wild-type (~40 uM), demonstrating that proper coordination of the guanidinium group with Asn101 and Trp293 is essential for the transition to the occluded state rather than for initial substrate recognition. The N101D mutation rescues activity by restoring hydrogen bonding capacity at position 101. This provides the first clues on the molecular mechanism of substrate-induced transition fit in 5+5 inverted repeat fold transporters.

### Pseudosymmetry of repeats dictates conformational changes

Analysis of the AdiC structure reveals that the 5+5 inverted repeat topology allows generation of symmetry-related states along the transport cycle. The superposition of repeat 2 (TMs 6-10) over repeat 1 (TMs 1-5) is an almost pure twofold rotation (175.2 degrees, translation 0.02 A). This pseudosymmetry was exploited to model an open-to-in conformation, revealing that the transition from outward- to inward-facing states results in pivoting of both bundle (TM1, TM2, TM6, TM7) and hash (TM3, TM4, TM8, TM9) domains, while TMs 5 and 10 show minor changes. The same operation applied to Mhp1 reproduces the crystal structure of its open-to-in conformation, validating the approach. The subunit axis in AdiC protomers deviates only 6 degrees from the membrane plane and is perpendicular to the dimer axis, ensuring independent function of each protomer with minimal alteration of the dimer interface.


## Cross-References

- [GadC Glutamate/GABA Antiporter](/xray-mp-wiki/proteins/slc-transporters/gadc/) — Homologous APC superfamily member; structural comparison for transport mechanism
- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/) — Structural template with similar fold; substrate bound in LeuT coincides with AdiC substrate binding site
- [APC Superfamily (Amino Acid-Polyamine-Organocation Transporter Family)](/xray-mp-wiki/concepts/transport-mechanisms/apc-superfamily/) — AdiC belongs to the APC superfamily of membrane proteins
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — AdiC operates via alternating access between outward-open and inward-open conformations
- [Major Facilitator Superfamily](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — MFS transporters share structural similarities with APC superfamily transporters
- [Virtual Proton Pump](/xray-mp-wiki/concepts/transport-mechanisms/virtual-proton-pump/) — AdiC is the prototypical virtual proton pump in E. coli acid resistance
- [Substrate-Induced Transition Fit in 5+5 Inverted Repeat Transporters](/xray-mp-wiki/concepts/transport-mechanisms/substrate-induced-transition-fit/) — AdiC N101A structure provides the first molecular clues on substrate-induced transition fit mechanism in 5+5 inverted repeat fold transporters
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Detergent used for AdiC purification and solubilization
- [Fab21 Antibody Fragment](/xray-mp-wiki/reagents/antibodies/fab21/) — Fab fragment used to form complex for crystallographic phasing
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — SeMet derivatives used for anomalous dispersion phasing
- [Agmatine](/xray-mp-wiki/reagents/ligands/agmatine/) — Agmatine is the decarboxylation product of arginine and the exchanged substrate in AdiC-mediated Arg/Agm antiport
