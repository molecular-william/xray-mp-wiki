---
title: GLIC (Gloeobacter violaceus Ion Channel)
created: 2026-05-28
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2012.08.009, doi/10.1016##j.str.2016.02.014, doi/10.1038##nature07461, doi/10.1038##NSMB.1933, doi/10.1038##emboj.2013.17]
verified: false
---

# GLIC (Gloeobacter violaceus Ion Channel)

## Overview

GLIC is a prokaryotic pentameric ligand-gated ion channel (pLGIC) from the cyanobacterium Gloeobacter violaceus. It is a proton-gated ion channel that serves as a bacterial homolog of eukaryotic Cys-loop receptors including nicotinic acetylcholine receptors (nAChR), GABA_A receptors, and serotonin 5-HT3 receptors. GLIC can be activated by low pH and is inhibited by general anesthetics including ketamine, propofol, and volatile anesthetics. It has been widely used as a model system for understanding anesthetic action on pLGICs and for the structural and functional characterization of allosteric modulation in Cys-loop receptors.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature07461 | 3GHG | 3.1 A | C2 | Full-length GLIC from Gloeobacter violaceus, wild-type | None (apo-GLIC, open-state structure) |
| doi/10.1038##nature07461 | 3GHG | 3.5 A | C2 | Full-length GLIC E221A mutant from Gloeobacter violaceus | None (apo-E221A mutant, open-state structure) |
| doi/10.1016##j.str.2012.08.009 | 3EAM | 3.25 A | P21212 | Full-length GLIC from Gloeobacter violaceus, residues 1-355 | None (apo-GLIC, used as molecular replacement model) |
| doi/10.1016##j.str.2012.08.009 | Ketamine-bound GLIC | 2.99 A | Not specified in paper | Full-length GLIC from Gloeobacter violaceus co-crystallized with ketamine | Ketamine (1 mM, 5 binding sites per pentamer) |
| doi/10.1016##j.str.2016.02.014 | 5HCJ | 2.95 A | C2 | Full-length GLIC from Gloeobacter violaceus, MBP fusion tag cleaved | Bromoform (pore site in locally closed conformation) |
| doi/10.1016##j.str.2016.02.014 | 5HCM | 3.15 A | C2 | Full-length GLIC from Gloeobacter violaceus, MBP fusion tag cleaved | Bromoform (open conformation, intra-subunit sites) |
| doi/10.1038##NSMB.1933 | WT-Cd2+ GLIC | 3.4 A | C2 | Full-length GLIC from Gloeobacter violaceus | Cd2+ (50 mM CdCl2, two binding sites in intracellular pore entry) |
| doi/10.1038##NSMB.1933 | WT-TEAs GLIC | 3.5 A | C2 | Full-length GLIC from Gloeobacter violaceus | Tetraethylammonium (TEAs, 10 mM, binds in center of membrane) |
| doi/10.1038##NSMB.1933 | WT-Zn2+ GLIC | 3.6 A | C2 | Full-length GLIC from Gloeobacter violaceus | Zn2+ (100 mM ZnCl2, binds to intracellular pore entry) |
| doi/10.1038##NSMB.1933 | WT-TBSb GLIC | 3.7 A | C2 | Full-length GLIC from Gloeobacter violaceus | Tetrabutylammonium bromide (TBSb, 5 mM, binds in center of membrane) |
| doi/10.1038##NSMB.1933 | WT-TMAs GLIC | 3.4 A | C2 | Full-length GLIC from Gloeobacter violaceus | Tetramethylammonium (TMAs, 30 mM, binds near intracellular pore entry) |
| doi/10.1038##NSMB.1933 | WT-Br-lido GLIC | 3.5 A | C2 | Full-length GLIC from Gloeobacter violaceus | Bromo-lidocaine (15 mM, binds in hydrophobic region at extracellular half of pore) |
| doi/10.1038##NSMB.1933 | WT-Cs+ GLIC | 3.7 A | C2 | Full-length GLIC from Gloeobacter violaceus | Cs+ (anomalous signal used for structural studies) |
| doi/10.1038##NSMB.1933 | E221A-Zn2+ GLIC | 3.7 A | C2 | Full-length GLIC E221A mutant from Gloeobacter violaceus | Zn2+ (Zn2+ binding to intracellular pore entry abolished by E221A mutation) |
| doi/10.1038##emboj.2013.17 | GLIC_2.4 | 2.4 A | C2 | Full-length GLIC from Gloeobacter violaceus, residues 1-355 | Br- (anion 1 at vestibule edge), Cs+ (cations 1-4 in vestibule), acetate (acetate 1 and 2 at two binding sites), sulfate (at Lys38 and Arg109) |
| doi/10.1038##emboj.2013.17 | GLIC S6'G | 2.4 A | C2 | Full-length GLIC S230G mutant (Ser6' to Gly) from Gloeobacter violaceus | None (mutant structure for MD simulation comparison) |
| doi/10.1038##emboj.2013.17 | GLIC S6'V | 2.4 A | C2 | Full-length GLIC S230V mutant (Ser6' to Val) from Gloeobacter violaceus | None (mutant structure for MD simulation comparison) |
| doi/10.1038##emboj.2013.17 | GLIC S6'T | 2.4 A | C2 | Full-length GLIC S230T mutant (Ser6' to Thr) from Gloeobacter violaceus | None (mutant structure for MD simulation comparison) |
| doi/10.1038##emboj.2013.17 | GLIC S6'T/I9'L | 2.4 A | C2 | Full-length GLIC double mutant S230T/I9'L from Gloeobacter violaceus | None (double mutant with altered pH sensitivity) |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: Full-length GLIC from Gloeobacter violaceus expressed as a fusion with Maltose-binding protein (MBP) using a plasmid provided by Raimund Dutzler's group. The MBP tag was preceded by an E. coli pELB signal sequence and a decahistidine (His10) tag. After purification, MBP was cleaved with HRV 3C protease.


### Purification Workflow

*Source: doi/10.1016##j.str.2012.08.009*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | E. coli expression with MBP fusion | -- | -- + -- | Expressed as MBP fusion protein using plasmid from Dutzler group |
| Purification | MBP affinity chromatography | -- | -- + -- | Protocol modified from Bocquet et al. 2009 and Hilf and Dutzler 2009 |

**Final sample**: ~10 mg/ml in unspecified buffer

### Purification Workflow

*Source: doi/10.1016##j.str.2016.02.014*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | E. coli C43 expression with MBP fusion | -- | -- + -- | Each mutant of GLIC fused to maltose-binding protein expressed in E. coli C43 cells |
| Purification | MBP affinity chromatography | -- | -- + -- | Purified as described in Bocquet et al. 2007 |
| Tag cleavage | Protease cleavage | -- | -- + -- | MBP fusion protein cleaved and concentrated |

**Final sample**: 6-8 mg/ml in unspecified buffer

### Purification Workflow

*Source: doi/10.1038##NSMB.1933*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | E. coli expression with MBP-His10 fusion | -- | -- + -- | Expressed as MBP-His10 fusion with E. coli pELB signal sequence |
| Membrane extraction | Detergent solubilization | -- | -- + DDM (n-Dodecyl-beta-D-maltopyranoside) | Extracted from isolated membranes with DDM |
| Affinity purification | Ni-NTA affinity chromatography | Ni-NTA resin | -- + DDM | Purified on Ni-NTA resin |
| Tag cleavage | HRV 3C protease cleavage | -- | -- + DDM | MBP cleaved off with HRV 3C protease, removed by rebinding to Ni-NTA |
| Size-exclusion chromatography | SEC on Superdex 200 column | Superdex 200 | 10 mM Tris pH 7.5, 150 mM NaCl, 0.5 mM DDM + DDM | GLIC pentamer peak pooled and concentrated to 10 mg/ml |

**Final sample**: 10 mg/ml in 10 mM Tris pH 7.5, 150 mM NaCl, 0.5 mM DDM


## Crystallization

### doi/10.1016##j.str.2012.08.009

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | GLIC (~10 mg/ml) pre-equilibrated with 0.5 mg/ml E. coli polar lipids and 1 mM ketamine |
| Reservoir | 10%-12% PEG 4000, 225 mM ammonium sulfate, 50 mM sodium acetate buffer (pH 3.9-4.1) |
| Mixing ratio | 1:1 protein to reservoir |
| Temperature | 4 C |
| Growth time | Crystals usually appeared within 1 week |
| Cryoprotection | Soaking in reservoir solution supplemented with 20% glycerol and 10 mM ketamine for 30 min before flash freezing in liquid nitrogen |
| Notes | Ketamine co-crystallization: GLIC pre-equilibrated with 1 mM ketamine for at least 1 hr at 4 C before mixing with reservoir solution. Six detergent and ten lipid molecules built into electron density during refinement. |

### doi/10.1016##j.str.2016.02.014

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | GLIC (6-8 mg/ml) co-crystallized with bromoform |
| Reservoir | 0.1 M sodium acetate buffer (pH 4), 0.4 M NaSCN, 12%-16% PEG 4000, 17% glycerol, 2% w/v bromoform |
| Mixing ratio | 1:1 protein to reservoir |
| Temperature | 20 C |
| Growth time | Crystals induced by micro-seeding from crushed crystals 1 hr after setup |
| Cryoprotection | Glycerol (17%) present in crystallization solution |
| Notes | Two crystal forms: locally closed (PDB 5HCJ, 2.95 A) and open (PDB 5HCM, 3.15 A), both in space group C2. Bromoform co-crystallized at 2% w/v. Data collected at SOLEIL PX1 beamline. Five monomers in asymmetric unit. |

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | GLIC (6-8 mg/ml) in open conformation with bromoform |
| Reservoir | 0.1 M sodium acetate buffer (pH 4), 0.4 M NaSCN, 12%-16% PEG 4000, 17% glycerol, 2% w/v bromoform |
| Mixing ratio | 1:1 protein to reservoir |
| Temperature | 20 C |
| Growth time | Crystals induced by micro-seeding from crushed crystals 1 hr after setup |
| Cryoprotection | Glycerol (17%) present in crystallization solution |
| Notes | Open form co-crystal (PDB 5HCM, 3.15 A resolution). Bromoform bound to intra-subunit sites DP-exp and DP-deep. Anomalous signal from bromine used for site identification. |

### doi/10.1038##NSMB.1933

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | GLIC (~10 mg/ml) with 0.5 mg/ml E. coli polar lipids, soaked with inhibitors (5 mM TBSb, 10 mM TEAs, 30 mM TMAs, 15 mM bromo-lidocaine) or 100 mM ZnCl2 or 50 mM CdCl2 replacing NaCl |
| Reservoir | 200-500 mM (NH4)2SO4, 50 mM sodium acetate buffer (pH 4.0), 9-12% PEG 4000 |
| Mixing ratio | 1:1 protein to reservoir |
| Temperature | 4 C |
| Growth time | Crystals obtained by cocrystallization or soaking of native crystals |
| Cryoprotection | 30% (v/v) ethylene glycol, flash-frozen in liquid propane |
| Notes | All WT and mutant complexes crystallized in space group C2. Structure of GLIC at 3.1 A (PDB 3EHZ) served as starting model for molecular replacement in PHENIX. For cryoprotection, crystals transferred into mother liquor with 30% ethylene glycol. |


## Biological / Functional Insights

### pH-activation of GLIC and the role of Glu221 in gating

GLIC is activated by low pH (proton-gated channel). Two-electrode voltage clamp recordings of GLIC expressed in Xenopus oocytes showed current activation at low extracellular pH. The E221A mutation (Glu221 to Alanine) was used to study the gating mechanism. The E221A mutant showed altered pore properties compared to WT. The 2Fo-Fc electron density at 3.6 A resolution showed the pore helices of the E221A mutant. Comparison of the intracellular pore entry between the E221A mutant and WT GLIC (with altered Glu221 side-chain conformation) revealed differences in pore radius, suggesting that Glu221 plays a critical role in the gating mechanism. The E221A mutation affects the intracellular vestibule and alters the conductance properties of the channel. Reversal potential measurements at different salt concentrations (130 mM NaCl high salt vs 30 mM NaCl low salt) confirmed ion permeation through the mutant channel.

### Ketamine binding to an intersubunit cavity in the EC domain

Ketamine binds to a pre-existing cavity between adjacent subunits in the extracellular domain of GLIC. Five ketamine molecules bind per pentamer in equivalent pockets. The binding site is near the homologous orthosteric agonist-binding site in Cys-loop receptors, but 9-10 A closer to the transmembrane domain. The ketamine site partially overlaps with the binding interface of large antagonists in Cys-loop receptors. Ketamine is positively charged at low pH and is stabilized in an amphipathic pocket through electrostatic interactions with N152, D153, D154 of the beta8-beta9 loop (loop F), van der Waals contacts with F174 and L176 of loop C, interaction with K183 of beta10, and a potential hydrogen bond with Y23 of beta1. The pocket volume is 248 A3, compatible with ketamine's volume of 219 A3.

### Functional validation of the ketamine binding site

The N152C mutation in the ketamine-binding pocket shifted the EC50 for GLIC activation from pH 5.0 (WT) to pH 5.4, and increased the ketamine IC50 from 58 uM (WT) to 110 uM, indicating reduced ketamine inhibition. Covalent labeling of N152C with CBFS (8-(chloromercuri)-2-dibenzofuransulfonic acid) mimicked the ketamine inhibitory effect. The residual current from CBFS labeling could be completely inhibited by ketamine with a higher IC50 of 180 uM. Treatment with 10 mM DTT removed CBFS and restored normal channel function. These results demonstrate the functional significance of the ketamine-binding pocket revealed in the crystal structure.

### Multiple anesthetic binding sites in GLIC

The ketamine binding site in the EC domain is approximately 30 A away from the channel gate. A previously identified site for propofol or desflurane is in the upper part of the transmembrane domain within a subunit of GLIC (Nury et al., 2011), distinct from the ketamine binding site. Two factors contribute to different sites: (1) ketamine is more soluble in the aqueous phase than propofol/desflurane, making it more attractive to solvent-exposed pockets; (2) ketamine has a larger molecular size. Multiple anesthetic binding sites in GLIC have been suggested by tryptophan fluorescence quenching experiments showing halothane and thiopental binding in the EC domain, TM domain, and EC-TM interface.

### Bromoform binding sites in GLIC open and locally closed conformations

Bromoform inhibits GLIC at sub-millimolar concentrations. Crystal structures of GLIC in the open form (PDB 5HCM) identified three intra-subunit binding sites in the transmembrane domain: DP-exp (containing DP and DP' subsites), DP-deep, and the inter-subunit DP-tunnel site. The locally closed form structure (PDB 5HCJ) revealed an additional bromoform molecule in the channel pore (PS site) that is not present in the open form. This pore site is specifically occupied when the channel is closed, replacing ordered pentagon water molecules found in the open form. The intra-subunit binding sites are different between the LC and open forms; binding to the intra-subunit cavity is discouraged in the locally closed form due to remodeling of the cavity and steric occlusion by Y197 side chain.

### Anesthetic access pathways and conformation-dependent binding

Molecular dynamics simulations reveal that general anesthetics predominantly access GLIC from the lipid bilayer through the DP-exp site, which serves as the main entry point to all other transmembrane binding sites. An additional access pathway from the extracellular vestibule to the pore site was also observed. The pore site (PS) is accessible in all functional forms of GLIC but is only spontaneously occupied in the open form simulations. In the locally closed and resting forms, access to the pore is blocked by the closed gate. Free energy calculations show state-dependent binding affinities for all tested sites except the extracellular site ES. The pore site markedly stabilizes the inactive (resting and locally closed) states compared to the active (open) state, making it a strong candidate for the functional site of anesthetic inhibition.

### Role of Y197 in modulating anesthetic binding

Residue Y197 plays a critical role in modulating anesthetic binding to GLIC. The side chain of Y197 adopts two alternative conformations: an up conformation that does not interfere with DP binding sites, and a down conformation that partially overlaps the DP' subsite of DP-exp. Y197 is highly conserved among Cys-loop receptors including nicotinic acetylcholine, 5HT3, and glycine receptors. The Y197 orientation directly affects the rotamer distribution of F195, which interacts with the M2-M3 helix and may modulate GLIC gating. A F195A mutant shows a strong loss of function phenotype. Y197 orientation is a key determinant of anesthetic binding affinity and insertion depth in the intra-subunit cavity.

### Two-region model of open channel block in pLGICs

Large pore blockers such as quaternary ammonium compounds (TEA, TBA, TBSb, TMA) and lidocaine bind in the center of the membrane, about halfway across the transmembrane domain. The binding site is in a cavity at the boundary between the hydrophobic and hydrophilic parts of the channel. Larger molecules like TBA and TPA bind more strongly due to hydrophobic interactions with their longer alkyl chains. Smaller blockers (TEA, TMA) bind progressively closer to the intracellular side. The affinity is determined by long-range electrostatics and hydrophobic interactions. This mechanism is general across pLGICs and related cation-selective channels.

### Divalent ion block at the intracellular pore entry

Divalent transition metal ions (Cd2+, Zn2+) bind to the narrow intracellular pore entry of GLIC, at a site distinct from the quaternary ammonium binding site. Zn2+ binds to a single site at the intracellular pore entry involving Glu221, and is still permeant (current saturates at negative potentials). Cd2+ binds to two overlapping positions in the intracellular pore (one overlapping with Zn2+ site, one 5 A extracellular to it) and causes strong block. The E221A mutation essentially abolishes both Zn2+ and Cd2+ binding, demonstrating that Glu221 plays a dominant role in divalent ion interaction. The same mutants had a smaller influence on TBA block, confirming two distinct binding regions.

### High-resolution structure reveals ion binding sites in the extracellular vestibule

The 2.4 A resolution structure of GLIC reveals multiple ion binding sites in the extracellular domain vestibule. Br- binds at the vestibule edge (anion 1) contacting the main chain amino groups of Phe78 and Arg85 and the Ne guanidinium atom from Arg85. Four Cs+ binding sites were identified: cation 1 at the vestibule edge near the beta2-beta5 loop and WXP motif; cations 2 (two layers of 5 ions each) at the level of acidic residues Asp86 and Asp88, approximately 25 A apical to the outer membrane interface; cation 3 binding to the carboxylate of Asp153 and hydroxyl of Tyr23; and cation 4 binding to main chain carbonyls of Leu146 to Val149. Ten acetate molecules (two per monomer) occupy two distinct binding sites: acetate 1 at the vestibule next to ion binding sites, and acetate 2 at the subunit interface near the conserved agonist-binding pocket. Sulfate ions bind at the extracellular mouth of the pore at Lys38 and Arg109.

### Cis-proline in the Cys-loop of GLIC

The GLIC_2.4 structure confirms that the proline residue in the Phe/Tyr-Pro-Phe/Met motif at the apex of the Cys-loop adopts a cis conformation, as in the previous 3EAM structure. This conserved proline is in a trans conformation in both ELIC and GluCl structures, but residual electron density suggests the trans conformation should be inverted. The cis-proline forms a hydrogen bond with the main chain amino group of residue 20' in the M3 alpha-helical segment, virtually extending M3 through the Cys-loop and articulating the transmembrane domain with respect to the extracellular domain. This interaction, together with a similar hydrogen bond between Arg117 and Asn21' (Asn245), stabilizes the open conductive form of pLGICs.

### Ser6' side chain conformation affects pore water organization

Molecular dynamics simulations of GLIC reveal that the Ser6' side chain conformation (defined by chi1 and chi2 dihedral angles) significantly affects water organization in the pore. The global free energy minimum (conformation alpha, chi1=304 deg, chi2=88 deg) corresponds to Ogamma and Hgamma pointing toward the intracellular compartment. Two other conformations were significantly populated: beta (193 deg, 186 deg) and gamma (200 deg, 180 deg). The chi2 angle greatly affects water organization: alpha favors occupying the water pentagon positions observed in MD simulations, whereas beta favors the crystallographically observed self-stabilized pentagon location. During steered MD pulling of a Na+ ion through the pore, the Ser6' conformation becomes affected as soon as the ion enters the extracellular half of the pore, with approximately 10% in conformation gamma and 10% in conformation beta.

### Thr2' conformation responds to ion position in the pore

During 200 ns MD simulations, Thr2' was observed in two conformations alpha (~80%) and beta (~20%). When a Na+ ion approaches Thr2' (within 5 A), the residue increases its proportion of the alpha conformation to nearly 90% when the ion is at the same level. However, this behavior displayed high variability during four different pulling simulations, so it is not yet possible to assess if this represents a general feature in pLGICs.

### Membrane potential effects on ion permeation

Simulations with imposed electric potentials of -50 and +50 mV across the simulation cell showed that the pore structure was not affected during 50 ns simulations. The water hydration profile was similar in all three simulations (-50 mV, +50 mV, and unbiased 200 ns), with the only noticeable difference being sodium enrichment in the bottom part of the pore. Ion permeation was not observed in any of the simulations. The number of Na+ ions within 4 A of Glu-2' increased to 5.0 +/- 0.3 during the -50 mV simulation compared to 3.0 +/- 0.3 in the basic simulation, though not significantly in the +50 mV simulation (3.5 +/- 0.5).

### S6' mutants alter GLIC pH sensitivity and conductance

Electrophysiology in Xenopus oocytes and BHK cells was used to characterize GLIC Ser6' mutants (S6'G, S6'T, S6'V, and S6'T/I9'). The S6'T/I9'L double mutant shows altered pH sensitivity with EC50 values of 5.4 +/- 0.6 for WT and 4.7 +/- 0.5 for the double mutant. The S6'G mutant was studied in heteropentameric mixtures with WT GLIC, showing that mixed populations of S6'G/Wt heteropentamers are synthesized and expressed at the plasma membrane with slower ON kinetics as the S6'G fraction increases.

### AquaSol electrostatics calculations predict ion binding sites

AquaSol, a solver for the non-linear Poisson-Boltzmann-Langevin equation, was used to compute cation, anion, and water density maps around the 2.4 A structure of GLIC and the 3.3 A structure of GluCl. Protonation states of titrable residues were determined using PROPKA and Karlsberg pKa prediction servers. In GLIC at pH 4.6, Asp86 and Asp88 were not protonated due to the presence of cations next to them in the crystal structure, and His11' (His235) was deprotonated. The simulations predicted cation density at all experimentally observed binding sites (cation 1, cation 2a, cation 2b, cation 3, cation 4) and anion density at anion 1 and sulfate sites, consistent with MD simulation occupancy data.


## Cross-References

- [Tetraethylammonium (TEA)](/xray-mp-wiki/reagents/ligands/tetraethylammonium/) — Key pore blocker; IC50 measured by two-electrode voltage clamp
- [Tetrabutylammonium (TBA)](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/) — Key pore blocker; larger analog of TEA with stronger binding
- [Bromo-lidocaine](/xray-mp-wiki/reagents/ligands/bromo-lidocaine/) — Local anesthetic derivative; bound in hydrophobic region of pore
- [Zinc Chloride](/xray-mp-wiki/reagents/additives/zinc-chloride/) — Zn2+ used as structural probe and functional blocker of GLIC
- [Cadmium Chloride](/xray-mp-wiki/reagents/additives/cadmium-chloride/) — Cd2+ used as structural probe and functional blocker of GLIC
- [Cesium Chloride](/xray-mp-wiki/reagents/additives/cesium-chloride/) — Cs+ used for anomalous diffraction studies of GLIC pore
- [PEG 4000](/xray-mp-wiki/reagents/additives/peg-4000/) — Crystallization precipitant (9-12% in reservoir)
- [ELIC (Erwinia ligate Ligand-gated Ion Channel)](/xray-mp-wiki/proteins/elic/) — Bacterial pLGIC homolog; direct structural comparison between closed (ELIC) and open (GLIC) states
