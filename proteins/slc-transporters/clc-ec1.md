---
title: CLC-ec1 Cl-/H+ Antiporter
created: 2020-04-20
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [transporter, ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1901822116, doi/10.7554##eLife.53479, doi/10.1371##journal.pbio.1001441, doi/10.1038##sj.emboj.7600909, doi/10.1073##pnas.1205764109, doi/10.1038##nature09556, doi/10.1038##nsmb.2814, doi/10.1126##science.1082708]
verified: false
---

# CLC-ec1 Cl-/H+ Antiporter

## Overview

CLC-ec1 is a prokaryotic CLC Cl-/H+ antiporter from Escherichia coli that has served as the paradigm for the CLC transporter family. Like all CLC proteins, CLC-ec1 is a homodimer in which each subunit independently catalyzes the coupled exchange of chloride ions (Cl-) for protons (H+). The transport cycle involves two key glutamate residues: Gluex (E148) positioned at the extracellular entryway to the Cl- permeation pathway, acting as both a gate for Cl- transport and a participant in H+ transport, and Gluin (E203) located toward the intracellular side, acting as an H+ transfer site. Structural and functional studies have identified E202 as a critical water-organizer that creates a proton conduit connecting intracellular solvent with Gluin (E203). Large nonpolar substitutions at E202 (e.g., E202Y) dramatically slow H+ access by blocking the interfacial pathway between the two CLC subunits, providing the first direct visualization of the intracellular H+ access route. A key breakthrough was the engineering of a monomeric ClC-ec1 mutant (WW, I201W/I422W), which demonstrated that the ClC subunit alone is the basic functional unit for transport and that cross-subunit interactions are not required for Cl-/H+ antiport (Robertson et al., 2010, Nature).

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.7554##eLife.53479 | 6V2J | 2.6 | I222 | CLC-ec1 QQQ triple mutant (E148Q/E203Q/E113Q) from E. coli, expressed in E. coli, crystallized in lipidic cubic phase without Fab fragment | Cl- ions at Scen and Sint binding sites |
| doi/10.1371##journal.pbio.1001441 | 1OTS | 2.5 | Not specified | CLC-ec1 wild-type from E. coli, original Dutzler et al. structure; also DeltaNC construct (residues 2-16 and 461-464 deleted) diffracting to 2.2-2.7 A | Cl- ions at Scen and Sint binding sites |
| doi/10.1073##pnas.1901822116 | 6AD7 |  |  | CLC-ec1 E148D mutant with Br- at 200 mM; expressed in E. coli | Br- at Sint and Sxet sites; no Br- at Scen |
| doi/10.1073##pnas.1901822116 |  |  |  | CLC-ec1 E148N mutant; expressed in E. coli | Br- |
| doi/10.1073##pnas.1205764109 | 4FTH |  |  | EcCLC E148A mutant with Fab fragment; expressed in E. coli | Glutamate from solution at the central Cl- binding site |
| doi/10.1073##pnas.1901822116 |  |  |  | CLC-ec1 E148A mutant with 50 mM [Bromoacetate](/xray-mp-wiki/reagents/ligands/bromoacetate/); expressed in E. coli | [Bromoacetate](/xray-mp-wiki/reagents/ligands/bromoacetate/) |
| doi/10.1038##nature09556 |  | 3.1 |  | CLC-ec1 WW double mutant (I201W/I422W) monomer from E. coli, expressed in E. coli, crystallized by sitting-drop vapor diffusion | Cl- at central binding site; crystallized in presence of NO3- |
| doi/10.1038##nsmb.2814 | 4MQX | 3.50 | C2 | CLC-ec1 cysteineless A399C A432C double mutant, Hg2+-cross-linked, expressed in E. coli | Cl- at central binding site; disulfide bond (Hg2+-catalyzed) between Cys399 and Cys432 |
| doi/10.1126##science.1082708 |  | 2.5 |  | Wild-type EcClC-Fab complex from E. coli; expressed in E. coli, purified in decylmaltoside (DM) | Cl- ions at Scen and Sint binding sites; Glu148 carboxyl at Sext site (closed conformation) |
| doi/10.1126##science.1082708 |  | 3.0 |  | EcClC E148A mutant-Fab complex from E. coli | Br- at Scen, Sint, and Sext sites (anion queue representing open conformation) |
| doi/10.1126##science.1082708 |  | 3.3 |  | EcClC E148Q mutant-Fab complex from E. coli | Br- at Scen, Sint, and Sext sites; glutamine side chain directed toward extracellular solution |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: E. coli CLC-ec1 wild-type and mutants (E202A, E202Q, E202Y, E202F, E202W, E148A, etc.), expressed in E. coli; DeltaNC construct (Delta15N/Delta4C) for crystallography

### Purification Workflow

*Source: doi/10.7554##eLife.53479*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Standard protein preparation | -- | -- + -- | Protein purification carried out as described (Walden et al., 2007) |
| Detergent extraction | Detergent solubilization | -- | -- + Decyl maltoside ([DM](/xray-mp-wiki/reagents/detergents/dm/)) | CLC-ec1 QQQ extracted with [DM](/xray-mp-wiki/reagents/detergents/dm/) (Anatrace) |
| Cobalt-affinity chromatography | Affinity chromatography | Cobalt affinity resin | -- + [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) (gradual exchange from [DM](/xray-mp-wiki/reagents/detergents/dm/)) | Detergent gradually exchanged for lauryl [Maltose](/xray-mp-wiki/reagents/substrates/maltose/) neopentyl glycol ([LMNG](/xray-mp-wiki/reagents/detergents/lmng/)) during the affinity step |
| Size-exclusion chromatography | SEC | -- | Buffer containing [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) + [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) | Final SEC step performed in LMNG-containing buffer |

### Purification Workflow

*Source: doi/10.1371##journal.pbio.1001441*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Standard protein preparation | -- | -- + -- | Protein purification in [DM](/xray-mp-wiki/reagents/decylmaltoside/) ([DM](/xray-mp-wiki/reagents/detergents/dm/)) as described (Walden et al., 2007) |
| Detergent extraction and purification | Affinity chromatography | Cobalt column | 100 mM Na/K tartrate, 20 mM tris-SO4, 20 mM imidazole-H2SO4, pH 7.5 + 5 mM [DM](/xray-mp-wiki/reagents/detergents/dm/) | Cl- contamination minimized by washing with Cl--free buffer; eluted with 400 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |
| Size-exclusion chromatography | SEC | -- | 100 mM Na/K tartrate, 10 mM tris-SO4, pH 7.5 + 5 mM [DM](/xray-mp-wiki/reagents/detergents/dm/) | Final purification step for crystallography and ITC |

### Purification Workflow

*Source: doi/10.1073##pnas.1205764109*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | E. coli expression | -- | -- + -- | EcCLC WT and mutant proteins expressed in E. coli and purified according to a published protocol (Dutzler et al., 2002, Nature) |
| Fab complex formation | Complex formation | -- | -- + -- | EcCLC E148A mutant protein mixed with Fab fragment in an OD280 ratio of 1:1.5 |
| Size-exclusion chromatography | SEC | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) (GE Health Life Sciences) | 10 mM [Hepes](/xray-mp-wiki/reagents/buffers/hepes/) pH 7.4, 150 mM potassium glutamate + 4 mM [DM](/xray-mp-wiki/reagents/detergents/dm/) | Complex protein further purified on [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) sizing column equilibrated in Cl--free buffer containing 150 mM potassium glutamate |

### Purification Workflow

*Source: doi/10.1038##nature09556*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | E. coli fermentation | — | Terrific broth | Induced with IPTG for expression of ClC-ec1 wild-type and WW (I201W/I422W) mutant |
| Membrane isolation and solubilization | Cell lysis and membrane fractionation | — | Decylmaltoside (DM) | Membranes solubilized in DM-containing buffer; protein purified as described previously for ClC-ec1 |
| Size-exclusion chromatography | SEC in decylmaltoside micelles | — | 100 mM NaCl, 10 mM Tris-HCl pH 7.5 + ~40 mM decylmaltoside | Monomeric state of WW mutant assessed on SEC column calibrated with membrane transport protein standards. Wild-type homodimer (100 kDa) elutes at 12.8 ml; WW mutant shifts to monomer position (~1 ml later). |

### Purification Workflow

*Source: doi/10.1038##nsmb.2814*

- **Expression system**: E. coli
- **Expression construct**: CLC-ec1 cysteineless variant with A399C A432C double mutation

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression and purification | Published protocol (Nguitragool & Miller, 2007) | — | 100 mM NaCl, 20 mM HEPES, 5 mM DM or 50 uM DMNG, pH 7.5 + 5 mM DM or 1 mM DMNG | Expression and purification according to published protocols. Some preparations exchanged from DM to DMNG for stability. Final SEC on Superdex 200. |
| Mercury-induced cross-link | HgCl2 treatment | — |  | Purified protein reacted with 4-fold molar ratio excess of HgCl2 for 1 h at room temperature. Excess Hg2+ removed by 1 mM EDTA and/or gel filtration. |
| Gel shift assay | mPEG5K PEGylation assay | — |  | Maleimide-PEG 5000 used to assess free cysteines. Single cysteine mutants shift to one higher MW band; double mutants shift to second higher MW band. Complete protection by Hg2+ confirms cross-link formation. |

**Final sample**: Cross-linked CLC-ec1 A399C A432C mutant in DM or DMNG


## Crystallization

### doi/10.7554##eLife.53479

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified QQQ protein in [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), concentrated to at least 30 mg/mL |
| Temperature | 16 |
| Growth time | 3-4 weeks |
| Cryoprotection | Flash-frozen in liquid nitrogen without further additives |
| Notes | Protein mixed with 1.5 parts (w/w) of monolein containing 10% (w/w) [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) using syringe reconstitution method. 25 nL LCP droplets overlaid with 600 nL precipitant in 96-well glass sandwich plates. Crystals harvested after 3-4 weeks incubation at 16 C. Structure solved by molecular replacement. No antibody Fab fragment used. |

### doi/10.1371##journal.pbio.1001441

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Protein sample | Purified CLC-ec1 DeltaNC construct in [DM](/xray-mp-wiki/reagents/detergents/dm/) |
| Reservoir | Not specified in paper |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals of DeltaNC construct diffracted to 2.2-2.7 A Bragg spacing. E202Y mutant crystals obtained at 3.2 A resolution. 52 crystallographic water molecules modeled in the DeltaNC dataset. Data collection details not fully specified. |

### doi/10.1073##pnas.1205764109

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | EcCLC E148A mutant with Fab, at 15 mg/mL |
| Reservoir | 50 mM [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) pH 9.0, 34% (w:v) [Peg](/xray-mp-wiki/reagents/additives/peg/) 300 |
| Temperature | 20 |
| Growth time | Not specified |
| Cryoprotection | Flash-frozen in liquid nitrogen without further additives |
| Notes | Crystals grown by mixing equal volumes of protein (15 mg/mL) with crystallization solution containing 50 mM [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) (pH 9.0) and 34% [Peg](/xray-mp-wiki/reagents/additives/peg/) 300. Crystals were directly harvested from the drop and flash-frozen. Data collected at the Advanced Photon Source. Structure determined in the absence of Cl- with 150 mM potassium glutamate in the protein buffer. |

### doi/10.1038##nature09556

| Parameter | Value |
|---|---|
| Method | Sitting-drop vapor diffusion |
| Protein sample | CLC-ec1 WW mutant (9-15 mg/ml) in 100 mM NaCl, ~40 mM decylmaltoside, 10 mM Tris-HCl pH 7.5 |
| Reservoir | 100 mM LiNO3, 41-45% (w/v) PEG400, 100 mM glycine-NaOH pH 9.5 |
| Temperature | 20 |
| Growth time | 2-4 weeks |
| Cryoprotection | Flash-frozen in liquid nitrogen |
| Notes | 1 ul protein mixed with equal volume reservoir, plus ~10 mM 4-cyclohexyl-1-butyl-beta-D-maltoside added to the 2 ul drop. Crystals grown by vapor diffusion in sitting drop trays. Data collected remotely at beamline 8.2.1 of the Advanced Light Source Eastern Annex. Data processed in HKL2000. Structure solved by molecular replacement in PHASER using residues 30-450 of a single subunit of ClC-ec1 as search model; refinement in REFMAC5. |


## Biological / Functional Insights

### QQQ mutant reveals outward-facing open state of CLC transporter

The triple mutant QQQ (E148Q/E203Q/E113Q) mimics the fully H+-loaded state of CLC-ec1 and reveals a global conformational change that generates an outward-facing open state. The structure shows widening of the extracellular vestibule, improved accessibility for Cl- from the extracellular side, and new conformations for both glutamate residues, providing the first high-resolution view of a CLC transporter intermediate that has been missing from structural models.

### Gluex adopts an "out" conformation in the outward-facing state

In the QQQ structure, Gluex (Q148) adopts a novel 'out' conformation, moving away from the permeation pathway into the hydrophobic core of the protein. This conformation, previously only observed in CLC-1 channels, is stabilized by small adjustments in residues 186, 190, 199, and 357. This suggests that the 'out' position represents a key transport intermediate accessible to both CLC transporters and channels.

### Extracellular vestibule opening widens Cl- entry pathway

Analysis using HOLE reveals that the extracellular bottleneck to Cl- permeation is relieved in QQQ compared to WT and E148Q structures. Helices N, O, and P move to widen the extracellular entryway, consistent with the QQQ structure representing the outward-facing open state. Cl- transport rates for QQQ are ~2-fold faster than E148Q, supporting the functional significance of this conformational change.

### Unified transport model for CLC proteins

Based on the QQQ structure, MD simulations, DEER spectroscopy, and functional studies, a unified framework for the CLC transport cycle is proposed. The model integrates the conformational changes in Gluex, Gluin, and E113, explaining how Cl- and H+ exchange is coupled through alternating access mechanisms. The model reconciles structural and functional data across all CLC-type proteins, including both transporters and channels.

### E202 as water-organizer for intracellular H+ access to Gluin

E202, a conserved glutamate at the intracellular surface of CLC-ec1, acts as a water-organizer that creates a proton conduit connecting intracellular solvent with Gluin (E203). E202 is located at the apex of a narrow aqueous invagination ('interfacial pathway' or 'fjord') between the two CLC subunits. Mutation of E202 to large nonpolar side chains (E202Y, E202F, E202W) dramatically slows H+ transport (up to 200-fold) without directly impairing the Cl- pathway, as demonstrated by ITC binding studies and uncoupled Cl- transport assays on E148A background.

### Interfacial pathway vs polar pathway for H+ access

Two potential H+ access routes were examined: a 'polar pathway' containing five crystallographically visible waters embedded in salt bridges, and an 'interfacial pathway' at the subunit interface. Mutations disrupting the polar pathway had minimal effect on antiport rates. In contrast, mutations at E202, which sits at the protein-water boundary of the interfacial pathway, severely impair H+ transport. This identifies the interfacial pathway as the primary route for intracellular H+ access to Gluin.

### E202Y crystal structure reveals blocked water conduit

The 3.2 A crystal structure of the E202Y mutant shows the substituted tyrosine side chain blocking the polar portal at the top of the interfacial fjord. An unexpected cross-subunit rearrangement occurs: I201 from the neighboring subunit moves to pack closely against the Y202 aromatic ring, adding nonpolar mass that sequesters Gluin away from aqueous protons. This structural rationalization is confirmed by monomeric CLC-ec1 experiments, where the E202Y mutation causes only a 4-fold reduction in H+ transport (vs 200-fold in the dimer), since the cross-subunit interaction cannot form.

### E202 is not a compulsory protonation point

E202 is not itself a required protonation site in the H+ transport pathway. E202Q (isosteric and polar) and E202A (small and nonpolar) mutants both support H+ uptake at about 20% of wild-type rates. This demonstrates that E202's role is structural (organizing water molecules) rather than as a proton carrier. E202 is strictly conserved across all CLC proteins, including CLC channels that require H+ movement for gating, suggesting a universal water-organizing function.

### Cl-/H+ stoichiometry and Cl- slippage in slow mutants

E202 mutants with large side chains show higher Cl-/H+ stoichiometry than wild-type, likely reflecting Cl- slippage through the inner gate in stalled transporters waiting for H+. The preservation of normal stoichiometry in monomeric E202Y supports this interpretation. Cl- binding affinity measured by ITC (KD = 0.74 mM for WT, 1.6 mM for E202Y) is only weakly affected, confirming that E202 mutations act on the H+ pathway rather than the Cl- pathway.

### Three distinct anion-binding sites in the CIC selectivity filter

The CIC selectivity filter in its open conformation (E148Q mutant) contains three anion-binding sites designated Sint, Scen, and Sext that bridge the intracellular and extracellular solutions. The adjacent peaks are separated by 7 A (Sint to Scen) and 5 A (Scen to Sext). The larger separation between Sint and Scen is partially due to Ser107 coordinating the ion in Scen. Scen and Sext are nearly in van der Waals contact. In the closed conformation (wild-type), only Sint and Scen are occupied, as the negatively charged side chain of the conserved Glu148 binds to Sext akin to a tethered anion. Despite the close proximity and resulting electrostatic repulsion, the three sites can be occupied simultaneously.

### Quantitative ion-binding affinities of the CIC selectivity filter

Using Br- anomalous scattering at the Br K-edge (0.92 A) at the Swiss Light Source, the binding affinities of the CIC selectivity filter were determined. In the open conformation, the dissociation constants (KD) for Br- are: Sext ~4 mM, Scen ~13 mM, and Sint ~23 mM. In the closed conformation, Scen affinity increases to KD ~5 mM, while Sint remains similar to the open conformation. This change in affinity (~0.6 kcal/mol) is attributed to small conformational differences and the stronger electrostatic repulsion between two Br- ions compared to Br- and the negatively charged glutamate side chain. Br-/Cl- competition experiments show little selectivity between Cl- and Br- in Sext, slightly higher affinity for Br- in Sint, and higher affinity for Cl- in Scen, making Scen and Sext bind Cl- equally well.

### Multi-ion single-file conduction in CIC channels parallels K+ channel mechanism

The CIC selectivity filter accommodates three ions simultaneously, enabling a multi-ion single-file conduction mechanism that parallels the well-established mechanism of K+ channels. In both channel families, ions permeate in single file with mutual electrostatic repulsion fostering rapid conduction. However, key differences exist: (1) in CIC channels, the binding sites are fully occupied, whereas in K+ channels, ions alternate with water molecules; (2) the CIC selectivity filter does not undergo a conformational change in the absence of bound ions (unlike K+ channels, which collapse into a non-conducting conformation at low K+ concentrations), which may contribute to the generally lower conduction rates of CIC channels compared to K+ channels. The energetic balance between the binding sites (particularly Sext and Scen) mirrors the tight energetic balance important for ion conduction in K+ channels and likely contributes to efficient Cl- conduction.

### E148D mutation reveals Midlow conformation of Gluex

The E148D mutation in CLC-ec1 (where Gluex is shortened by one methylene group) reveals a previously unobserved "Midlow" conformation of the Gluex equivalent (Asp148). In this conformation, Asp148 sits between the external (Sext) and central (Scen) Cl- binding sites, and the central site is emptied of Cl-. This provides structural evidence that the Gluex can adopt at least 3 distinct conformational states (Up, Middle, and Down) during the transport cycle of a single CLC antiporter.

### Extra external anion binding site Sxet in CLC-ec1

A novel extra external anion binding site (Sxet) was discovered above Sext in the E148D mutant at high anion concentration. The Sxet is located 6 A above Sext along the anion transport pathway and is coordinated by the backbone amide and side-chain guanidinium group of Arg147, the side chain of Phe317 via anion-quadruple interaction, and the N-terminal helical dipoles of helices F, L, and N. This site becomes visible only at 50 mM NaBr and prominent at 200 mM NaBr. Mutations R147A/F317A showed significantly different Cl- turnover rates at low Cl- concentration compared to wild-type.

### Bromoacetate as a mobile carboxylate mimic in CLC-ec1

[Bromoacetate](/xray-mp-wiki/reagents/ligands/bromoacetate/) (BAA), a short carboxylic acid with anomalously detectable bromine, was used to probe anion binding in the ungated E148A mutant. [Bromoacetate](/xray-mp-wiki/reagents/ligands/bromoacetate/) can occupy either the external (Sext) or central (Scen) Cl- binding site, demonstrating that a mobile carboxylate group from solution can substitute for the missing Gluex side chain. This supports the model where the Gluex carboxylate shuttles between external and central binding sites during the transport cycle.

### Limited solvent accessibility of Asp148 explains slowed transport in E148D

Comparison of E148Q (protonated mimic of wild-type) and E148N (protonated mimic of E148D) reveals that Asn148 is buried inside the protein while Gln148 is solvent-accessible. This limited extracellular solvent accessibility of the protonated Asp148 likely retards H+ transport, followed by Cl- slippage, resulting in increased Cl-/H+ stoichiometry in the E148D mutant. The E148D mutant showed approximately one order of magnitude slower Cl- transport than wild-type.

### E148A mutant structure with solution glutamate bound at central Cl- binding site

A crystal structure of the EcCLC E148A mutant (Egate removed) in the absence of Cl- and presence of 150 mM sodium glutamate reveals electron density compatible with a solution glutamate molecule extending its side chain into the anion transport pathway to reach the central Cl- binding site. This provides direct structural evidence that a mobile carboxylate group from solution can substitute for the missing Egate side chain, supporting the shuttle mechanism in which the Egate carboxylate carries a proton between the external solution and the central Cl- site.

### Solution carboxylates mediate H+ transport in E148A mutant

When Egate is mutated to alanine (E148A), H+ transport ceases unless carboxylate-containing molecules (glutamate, gluconate) are supplied in solution. This H+ influx depends on the carboxylate group, as evidenced by the failure of homocysteic acid (which has a sulfate instead of a carboxylate) to support the influx. The glutamate/gluconate-mediated H+ influx depends on the normal H+ pathway, as mutation of the Ein glutamate (E203V) prevents it. These data support a mechanism in which the glutamate carboxylate functions as a surrogate Cl- ion that can accept a proton and transfer it between the external solution and the central Cl- binding site.

### Cl- requirement for H+ transport and inhibition of solution-mediated transport

Cl- ions are required for H+ transport in wild-type CLC transporters but inhibit solution-mediated H+ transport in the Egate mutant (E148A). One millimolar Cl- inhibits solution-mediated H+ transport nearly completely (apparent Ki < 0.1 mM). This opposing effect is explained by competition between Cl- and the carboxylate group in the anion transport pathway: Cl- is needed to destabilize the permanently-bound Egate carboxylate in wild-type, but outcompetes the more weakly-binding solution carboxylate in the Egate mutant.

### Aspartate insufficient to replace glutamate at the Egate position

Aspartate at the Egate position (E148D) cannot fully replace glutamate. The shorter aspartate side chain can adopt the external and outer Cl- site conformations but cannot easily reach the central Cl- binding site. With aspartate at the Egate position, H+ transport is measurable compared to alanine but extremely slow compared to glutamate in both EcCLC and [Cmclc](/xray-mp-wiki/proteins/slc-transporters/cmclc/). This demonstrates that the glutamate side chain length is critical for the shuttle mechanism, as Egate must reach the central Cl- site to release or capture H+.

### H+ shuttle mechanism on the Egate carboxylate

The data support a mechanism in which H+ are transported on a carboxylate group that enters the anion pathway. The carboxylate of the Egate glutamate transfers a proton between the extracellular solution and the central Cl- binding site. Cl- and the Egate carboxylate compete with and destabilize each other in the anion transport pathway. The presence of Cl- perturbs the pKa of the Egate carboxylate, rendering it susceptible to H+ exchange. H+ transport is coupled to Cl- movement because the Egate carboxylate in its deprotonated form mimics Cl-.

### Warts-and-hooks strategy for engineering a monomeric ClC transporter

A "warts-and-hooks" strategy was used to engineer a monomeric ClC-ec1 by introducing tryptophan substitutions on the subunit interface. The double mutant I201W/I422W (WW) places four "warts" within the subunit contact region to disrupt shape complementarity while offering two tryptophan "hooks" to the bilayer at each membrane interface. The WW mutant elutes as a monomer on SEC calibrated with membrane transport standards, and glutaraldehyde crosslinking in both detergent micelles and liposomes confirms its monomeric state (Robertson et al., 2010, Nature).

### Monomeric ClC subunit is transport-competent with preserved Cl-/H+ antiport activity

The WW monomer retains defining features of ClC-ec1 transport: (1) Unitary Cl- efflux rate of ~160 s-1 (roughly half of wild-type ~300 s-1); (2) Anion specificity is maintained, with Cl- efflux fully dependent on K+ ionophore; (3) Cl-/H+ exchange stoichiometry of 2.3 +/- 0.3 (vs 2.0 for wild-type), demonstrating that H+-coupled Cl- antiport is preserved in the monomer. This directly establishes that the ClC subunit alone contains all essential components of the transport mechanism (Robertson et al., 2010, Nature).

### Crystal structure of monomeric ClC-ec1 reveals preserved subunit architecture

The 3.1 A crystal structure of the WW monomer shows that the 18 membrane-embedded helices align precisely with those of the wild-type subunit (Calpha RMSD 0.6 A), despite the absence of native cross-subunit dimerization contacts. Most side chains projecting from the exposed subunit interface are well ordered and unperturbed from their buried positions in the wild-type dimer. The mechanistically crucial central Cl- ion is present at the same position as in wild-type, coordinated by Ser107, Glu148, and Tyr445. Cl- density is lower in WW than wild-type, possibly due to competition with NO3- present during crystallization (Robertson et al., 2010, Nature).

### Parallel-pathways model validated: ClC homodimer consists of two independent transporters

The demonstration that a monomeric ClC subunit is fully transport-competent validates the parallel-pathways model in which the ClC homodimer consists of two single-subunit transporters operating independently. This explains the puzzling observation that cross-subunit interactions at the dimer interface are not required for function. The results align ClC transporters with other membrane protein families where each subunit independently functions (e.g., aquaporin tetramers, FNT pentamers, UT urea transporters), raising the question: why are all ClC proteins homodimers if the subunit alone suffices? (Robertson et al., 2010, Nature).

### Helix O movement is required for Cl-/H+ exchange in CLC-ec1

Basilio et al. (2014) demonstrated that transport in CLC-ec1 is inhibited by cross-links constraining movement of helix O far from the transport pathway. Cross-linking the intracellular portion of helix O to helices Q or J via cysteine pairs (A399C A432C, L252C P424C, A399C T428C, G259C A399C) reduced Cl- transport by 30-100 fold. The cross-linked protein adopts a wild-type-like structure (PDB 4MQX, 3.5 A, RMSD 0.48 A vs WT), confirming stabilization of a native conformation rather than distortion. The A396C A399C intra-helix cross-link showed only ~3-fold reduction, suggesting helix O moves as a rigid body.

### Glutamate gate mechanism of CLC channel gating

The 2003 Dutzler et al. Science study on wild-type and mutant EcClC-Fab complexes established the glutamate gate mechanism of CLC chloride channel gating. In the closed state, the Glu148 carboxyl group occupies the extracellular Cl- binding site (Sext) in the selectivity filter, mimicking a Cl- ion and blocking the pore. In the open state (E148A, E148Q), the glutamate side chain is removed or displaced, and a Cl- ion occupies the Sext site, creating an uninterrupted anion queue (Sint-Scen-Sext) through the pore. Electrophysiological studies on ClC-0 from Torpedo ray confirmed that mutation of the corresponding residue (E166) abolishes fast gating. This mechanism explains the coupling between Cl- conduction and gating: Cl- ions and the glutamate carboxyl compete for the same binding site, and pH modulates gating through protonation of the glutamate. The glutamate gate represents a simple form of gating by local side chain occlusion, fundamentally different from the large-scale conformational changes of K+ channel activation gating.

### Tyr445 forms the inner gate of CLC-ec1

Ile402 at the C-terminal end of helix O directly contacts Tyr445, a conserved residue that constricts the intracellular end of the Cl- transport pathway. Introducing the A399C A432C cross-link on the background of the Y445A mutant reduced transport only ~3-fold (vs ~100-fold with Tyr at 445), demonstrating that movement of helix O is transduced to the ion pathway via this contact. The Y445A mutant alone removes the inhibitory effect of the cross-link, proving Tyr445 is a key element of the internal gate. When both Glu148 (external gate) and Tyr445 (inner gate) are removed (E148A Y445A double mutant), the cross-link has no effect, confirming the two-gate model.

### CLC transporters have two gates: Glu148 (external) and Tyr445 (internal)

The cross-link inhibits transport by ~100-fold in WT background but only ~2-3-fold in either E148A or Y445A single mutants, and has no effect in the E148A Y445A double mutant. This demonstrates that neither Glu148 alone nor Tyr445 alone can account for the inhibitory effect - both gates must be present. If Glu148 were the only gate, the Y445A mutant would still be inhibited; if helix O only controlled H+ pathway, the E148A mutant would still be inhibited. The results establish that CLC transporters use an alternating-access mechanism with two gates, contrary to the earlier single-gate model.

### Helix O movement is coupled to Cl- pathway but not H+ pathway

Cross-link formation does not alter the 2 Cl-/1 H+ stoichiometry of transport in WT or A399C A432C backgrounds. The I402S and Y445A mutations on the A399C A432C background also preserve normal stoichiometry before cross-linking. After cross-linking, the residual transport in I402S and Y445A mutants maintains the correct stoichiometry, demonstrating that helix O movement controls Cl- access through the two gates rather than the H+ pathway. This establishes that the H+ pathway is independent of the conformational changes required for Cl- transport.

### Transport model for CLC exchangers with two coupled gates

A new transport model for CLC exchangers was proposed based on the finding of two gates. The cycle involves six states: (1) apo state with inner (Tyr445) and outer (Glu148) gates closed; (2) inner gate opens, allowing Cl- binding; (3) Cl- binding causes Glu148 displacement and protonation from outside, triggering inner gate closure; (4) fully loaded outward-facing state; (5) Cl- exit and Glu148 reenters pathway; (6) proton transferred to Glu203 and released intracellularly. Helix O is part of the coupling machinery between the two gates, allowing simultaneous substrate binding while preventing ion slippage. This model explains how Cl-/H+ exchange can sustain tight coupling even at acidic pHs.


## Cross-References

- [STCLC](/xray-mp-wiki/proteins/slc-transporters/stclc/) — Salmonella typhimurium CLC homolog for structural comparison
- [CLC-sy1](/xray-mp-wiki/proteins/slc-transporters/clc-sy1/) — Synechocystis CLC homolog for structural comparison
- [Decyl Maltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Detergent used for protein extraction and purification
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used for final purification and crystallization in QQQ mutant study
- [Lipidic Cubic Phase (LCP) Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Crystallization method used for the QQQ mutant
- [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — The QQQ structure represents the outward-facing open intermediate in the transport cycle
- [CLC Cl-/H+ Exchange Transport Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/clc-proton-transport-mechanism/) — Key evidence for the Egate carboxylate shuttle mechanism and H+ transfer pathway
- [CmCLC Cl-/H+ Antiporter](/xray-mp-wiki/proteins/slc-transporters/cmclc/) — Eukaryotic CLC transporter from C. merolae used for comparative mechanistic studies
- [Bromoacetate](/xray-mp-wiki/reagents/ligands/bromoacetate/) — Referenced in the context of Bromoacetate
- [DM](/xray-mp-wiki/reagents/detergents/dm/) — Referenced in the context of DM
- [CLC Two-Gate Transport Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/clc-two-gate-mechanism/) — Helix O movement and Tyr445 inner gate discovery establishes the two-gate alternating-access model for CLC transporters
