---
title: KcsA Potassium Channel
created: 2026-05-27
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2020.06.012, doi/10.1016##j.str.2012.03.027, doi/10.1038##nature01580, doi/10.1038##nature04508, doi/10.1038##nature09136, doi/10.1038##nsmb.1531]
verified: false
---

# KcsA Potassium Channel

## Overview

KcsA is a prokaryotic voltage-gated potassium channel from Streptomyces lividans that serves as a model system for understanding potassium channel structure, gating, and selectivity. The channel forms a homotetramer with a central pore lined by the highly conserved TVGYG selectivity filter motif. Wild-type KcsA can adopt both open-gate and closed-gate conformations under the same crystallization conditions, providing structural insight into the allosteric coupling between the activation gate and the selectivity filter. This wiki entry covers structures from multiple studies including the first open-gate structure of wild-type KcsA with barium binding, Cd2+-bound cysteine mutant structures revealing outer vestibule dynamics during C-type inactivation gating, and fully open KcsA structures with rubidium ions revealing conformational coupling between the activation gate and selectivity filter.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2020.06.012 | 6W0A | 3.2 A | I4 | Wild-type KcsA from Streptomyces lividans | Ba2+ (1 mM BaCl2, 5 mM KCl, open-gate, constricted filter) |
| doi/10.1016##j.jmb.2020.06.012 | 6W0B | 3.6 A | I4 | Wild-type KcsA from Streptomyces lividans | Ba2+ (2 mM BaCl2, 5 mM KCl, open-gate, constricted filter) |
| doi/10.1016##j.jmb.2020.06.012 | 6W0C | 3.5 A | I4 | Wild-type KcsA from Streptomyces lividans | Ba2+ (4 mM BaCl2, 5 mM KCl, open-gate, constricted filter) |
| doi/10.1016##j.jmb.2020.06.012 | 6W0D | 3.6 A | I4 | Wild-type KcsA from Streptomyces lividans | Ba2+ (5 mM BaCl2, 5 mM KCl, open-gate, constricted filter) |
| doi/10.1016##j.jmb.2020.06.012 | 6W0E | 3.5 A | I4 | Wild-type KcsA from Streptomyces lividans | Ba2+ (10 mM BaCl2, 5 mM KCl, open-gate, constricted filter) |
| doi/10.1016##j.str.2012.03.027 | Cd2+-bound Y82C-KcsA | 2.4 A | I4 | Y82C mutant of KcsA from Streptomyces lividans, crystallized with Fab fragments | Cd2+ (100 uM, individually bound to cysteine residues; no inter-subunit metal bridge in closed state) |
| doi/10.1016##j.str.2012.03.027 | Spin label-bound Y82C-KcsA | 2.5 A | I4 | Y82C mutant of KcsA from Streptomyces lividans with nitroxide spin label, crystallized with Fab fragments | Nitroxide spin label at Y82C position |
| doi/10.1038##nature09136 | OM-Rb (Fully open KcsA with Rb+) | 3.3 A | I4 | Wild-type KcsA from Streptomyces lividans | Rb+ ions in selectivity filter (fully open state, 50-3.3 A resolution) |
| doi/10.1038##nature09136 | E71H-F103A (Closed state) | 3.2 A | I4 | E71H-F103A double mutant of KcsA from Streptomyces lividans | Rb+ ions (closed state, 40-3.2 A resolution) |

## Expression and Purification

- **Expression system**: E. coli XL-1 Blue
- **Construct**: Wild-type KcsA and Y82C/E71A-Y82C mutants from Streptomyces lividans, expressed from pQE32 vector. Cells grown at 37 C with OD600 of 0.8-1.0, induced with 0.5 mM IPTG for 3 h. Lysis buffer: 20 mM Tris (pH 8.0), 0.2 M NaCl, 1 mM PMSF, 20 ug/ml DNase I. Cell membranes collected by centrifugation at 100,000g at 4 C for 1 h. Tandem dimer (TD) and tandem tetramer (TT) constructs of Y82C-KcsA were made by cloning Y82C-containing KcsA into the appropriate protomer positions of the genetically linked tandem constructs.


### Purification Workflow

*Source: doi/10.1016##j.jmb.2020.06.012*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | High-pressure homogenization | -- | 20 mM Tris (pH 8.0), 0.2 M NaCl, 1 mM PMSF, 20 ug/ml DNase I + -- | Cells lysed using Avestin Emulsiflex C5 homogenizer |
| Membrane collection | Centrifugation | -- | -- + -- | Membrane pellet collected at 100,000g at 4 C for 1 h |
| Solubilization | Detergent solubilization | -- | 20 mM Tris (pH 7.5), 0.15 M KCl + 40 mM n-decyl-beta-D-maltoside (DM) | Overnight incubation at 4 C |
| Purification | -- | -- | 20 mM Tris (pH 7.5), 0.15 M KCl + 40 mM DM | Purification details not fully specified; protein crystallized after solubilization |

### Purification Workflow

*Source: doi/10.1016##j.str.2012.03.027*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression | E. coli expression | -- | 20 mM Tris (pH 8.0), 0.2 M NaCl, 1 mM PMSF + -- | Y82C and E71A/Y82C mutants expressed from pQE32 vector in E. coli XL-1 Blue |
| Membrane collection | Centrifugation | -- | -- + -- | Cell membranes collected by centrifugation at 100,000g at 4 C for 1 h |
| Solubilization | Detergent solubilization | -- | Not specified + Not specified | Membranes solubilized for crystallization and functional studies |


## Crystallization

### doi/10.1016##j.jmb.2020.06.012

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (soak) |
| Protein sample | Solubilized wt KcsA in DM |
| Reservoir | Not fully specified in paper |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Crystals soaked in solutions containing 0-10 mM BaCl2 with varying KCl concentrations (0-10 mM) |
| Notes | Wild-type KcsA crystallized in two distinct conformations (open-gate and closed-gate) under identical conditions. Open-gate structures obtained by soaking pre-grown crystals in BaCl2 solutions. Closed-gate structures obtained with 0-10 mM KCl and 5 mM BaCl2. All open-gate structures have constricted selectivity filters. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (soak) |
| Protein sample | Solubilized wt KcsA in DM |
| Reservoir | Not fully specified in paper |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Crystals soaked in BaCl2 solutions with 5 mM KCl at varying BaCl2 concentrations (1-10 mM) |
| Notes | Open-gate structures captured at BaCl2 concentrations of 1, 2, 4, 5, and 10 mM. All show constricted selectivity filter with Ba2+ bound at site S4. Space group I4 for all open-gate structures. |

### doi/10.1016##j.str.2012.03.027

| Parameter | Value |
|---|---|
| Method | Co-crystallization / Cd2+ soaking with Fab fragments |
| Protein sample | Y82C-KcsA mutant in detergent |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Crystals of Cd2+-bound Y82C-KcsA obtained by cocrystallization or Cd2+ (100 uM) soaking after crystal formation. Fab fragments present during crystallization. |
| Notes | Cd2+-bound Y82C-KcsA crystallized in the closed state at 2.4 A resolution. No explicit inter-subunit Cd2+ metal bridges observed; Cd2+ bound individually to cysteine residues. S-gamma to S-gamma distances: 16.5 A (diagonal), 11.7 A (adjacent). Spin label-bound Y82C-KcsA crystallized at 2.5 A resolution with Fab. Distance between N-O groups of spin labels in diagonal subunits: 12.7 A. Attempts to crystallize Cd2+-bound form in inactivated state using low K+ or M96V background were unsuccessful. |

### doi/10.1038##nature09136

| Parameter | Value |
|---|---|
| Method | Crystallization not specified in supplementary data |
| Protein sample | Wild-type KcsA (OM-Rb) and E71H-F103A mutant |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | OM-Rb structure: Fully open KcsA with Rb+ ions in selectivity filter, space group I4, cell dimensions a=b=157.79 A, c=73.88 A, resolution 50-3.3 A, Rmerge 41.1%, completeness 97.2%, Rwork/Rfree 24.04/25.6, 3923 protein atoms, 4 ligand/ion atoms. E71H-F103A closed state: Space group I4, cell dimensions a=b=156.14 A, c=76.29 A, resolution 40-3.2 A, Rmerge 46.6%, completeness 81.6%, Rwork/Rfree 21.95/26.95, 3986 protein atoms, 6 ligand/ion atoms. |


## Biological / Functional Insights

### Open-gate conformation of wild-type KcsA

Wild-type KcsA crystallized in two distinct conformations: open-gate and closed-gate, captured under identical crystallization conditions. The open-gate conformation has a C-alpha-C-alpha distance at Thr112 of approximately 23 A, roughly double the closed-gate distance of 12 A. The major structural difference is a ~30 degree swinging motion of the C-terminal end of TM2, hinged at Ser102. The open-gate structure is structurally similar to the engineered open-mutant KcsA (PDB 3F7V) with an RMSD of 0.56 A for backbone atoms. This represents the first time an open-gate form of wild-type KcsA has been crystallized.

### Barium binding to the selectivity filter

Anomalous diffraction experiments show that Ba2+ primarily binds to the innermost site S4 of the selectivity filter in the open-gate conformation. Ba2+ was also detected at site S2 in the closed-conductive structure with Ba2+/Na+ incubation. No Ba2+ binding was detected in any closed-gate soak structures, indicating that Ba2+ cannot access the filter from the extracellular side in the closed-conductive conformation due to a high free-energy barrier of about 30 kcal/mol. The selectivity filter adopts a constricted conformation in all Ba2+-bound structures, suggesting that Ba2+ binding drives the inactive filter state.

### Allosteric coupling between gate and selectivity filter

The constricted selectivity filter in open-gate structures demonstrates the allosteric crosstalk between the selectivity filter and the activation gate. The Ba2+-induced constricted filter state promotes the open conformation of the activation gate, a well-documented bi-directional allosteric phenomenon in KcsA. Functional experiments showed that Ba2+ destabilizes the closed state of the blocked channel by 1.5 kcal/mol, consistent with allosteric coupling between selectivity filter conformation and the activation gate.

### Barium block mechanism and lock-in effect

Ba2+ acts as an open-state blocker of K+ channels, blocking the conduction pathway from the intracellular side. PMF calculations show no significant free energy barrier for Ba2+ entry from the intracellular side in the open-gate channel, with the most stable position near site S4 (7 kcal/mol lower than bulk). In contrast, accessing the filter from the extracellular side in the closed-conductive channel requires overcoming a high free-energy barrier of about 30 kcal/mol. The external lock-in effect, whereby K+ binding to external sites S0-S2 impedes Ba2+ forward translocation, is enhanced by the presence of Ba2+ in the filter, increasing K+/Na+ selectivity at external sites by about 3.2 kcal/mol.

### Cd2+-induced C-type inactivation and metal bridge formation

External Cd2+ enhances the rate of C-type inactivation in the Y82C mutant of KcsA via metal-bridge formation. Cd2+ does not affect wild-type KcsA inactivation rate, indicating specific interaction with the engineered cysteine. A 10-fold increase in inactivation rate is observed with Cd2+ (from 1,200 ms to ~120 ms midpoint at ~40 uM Cd2+). The non-inactivating E71A/Y82C mutant does not show Cd2+-induced inactivation, suggesting that metal bridge formation requires the ability to undergo C-type inactivation. Tandem dimer (diagonal cysteines) and tandem tetramer (adjacent cysteines) constructs demonstrate that Cd2+ metal bridges form only between adjacent subunits, not diagonal ones.

### Outer vestibule dynamics during C-type inactivation

CW-EPR distance measurements using spin-labeled TD-Y82C constructs show that the mean distance between spin labels in diagonal subunits is 12 A in the closed state and 8 A upon opening the activation gate, representing a 2 A inward movement per subunit. The crystal structure of spin label-bound Y82C-KcsA confirms this distance (12.7 A between N-O groups of spin labels). In the Cd2+-bound closed state, the S-gamma to S-gamma distances between cysteines are 16.5 A (diagonal) and 11.7 A (adjacent), far from the ~5 A needed for Cd2+ metal bridge formation. This indicates that subunits must dynamically come closer during the transition to the inactivated state to enable metal bridge formation between adjacent subunits. Molecular dynamics simulations show that Cd2+ coordinated between adjacent subunits is stable, while diagonal coordination is energetically unfavorable (~50 kcal/mol penalty).

### Conformational coupling between activation gate and selectivity filter

The gating cycle of K+ channels is defined by four kinetic states, where the activation and selectivity filter gates exist in either conductive or non-conductive conformations. The two gates are coupled so that opening of the activation gates stabilizes the non-conductive conformation of the filter while inactivating the filter stabilizes the activation gate in its closed conformation. This bidirectional allosteric coupling was demonstrated through comparison of fully open KcsA structures with Rb+ in the selectivity filter and closed-state structures. The selectivity filter adopts a partially inactivated conformation in the fully open KcsA with Rb+, demonstrating that gate opening drives filter inactivation. The C-terminal domain plays a critical role in this coupling, as C-terminal truncation leads to wider opening of the inner bundle gate and reduced coupling efficiency between the gates.

### F103 side chain reorientation as a gate state reporter

When the intracellular gate opens, the rotameric conformation of the Phe103 side chain seen in the open inactivated crystal structure becomes highly favored compared to the preferred closed state conformation. Adiabatic energy maps of the side chain dihedral angles show that this energetic balance suggests that the conformation of Phe103 is a faithful reporter of the intracellular gate conformation and provides a possible mechanism for how information about the lower gate might be relayed to the selectivity filter. The approximately 2 kcal/mol van der Waals interaction energy between F103 and T74/T75 residues in the pore helix contributes to this coupling mechanism.

### C-terminal domain role in gate coupling efficiency

Fluorescence energy transfer experiments using Alexa Fluor 350 and 488 dyes revealed that the energy transfer efficiency at the inner gate (G116C) decreases significantly after chymotrypsin treatment. This implies that C-terminal truncation leads to a wider opening of the inner bundle gate than that of its full-length counterpart. At least in KcsA, the coupling efficiency between gates appears to be proportional to the degree of opening in the inner helix bundle, revealing the underlying principle of conformational coupling from the gate to the filter.

### Structural conservation with NaK closed conformation

The closed NaK structure (PDB 2AHY) superimposes well with closed KcsA (PDB 1K4C) with an r.m.s.d. of 0.73 A for inner and pore helices. Outer helices are slightly shifted translationally. This structural correlation confirms that the closed conformation of the nonselective NaK channel is structurally equivalent to the closed conformation of the selective K+ channel KcsA. The NaK structure provides an important comparison point, demonstrating that the conserved gating mechanics extend beyond K+-selective channels to nonselective cation channels.


## Cross-References

- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/decylmaltoside/) — Primary solubilization detergent (40 mM) for KcsA extraction
- [Barium Chloride](/xray-mp-wiki/reagents/additives/barium-chloride/) — Ba2+ blocker used in soak experiments (0-10 mM) to study selectivity filter binding
- [Cadmium Chloride](/xray-mp-wiki/reagents/additives/cadmium-chloride/) — Cd2+ ions form metal bridges between adjacent subunits in Y82C-KcsA outer vestibule during C-type inactivation
- [POPC](/xray-mp-wiki/reagents/lipids/popc/) — Component of 3POPC:1POPG lipid bilayer in MD simulations
- [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/) — MD simulations of open-gate KcsA and Cd2+ coordination dynamics
- [KirBac Potassium Channels](/xray-mp-wiki/proteins/kirbac-potassium-channels/) — Homologous prokaryotic potassium channel; Ba2+ binding studied in KirBac structures
- [C-type Inactivation](/xray-mp-wiki/concepts/c-type-inactivation/) — Cd2+-induced C-type inactivation mechanism studied in Y82C-KcsA mutant
- [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/kvap/) — Selectivity filter structure in KvAP is essentially identical to KcsA; glycine-gating hinge mechanism first identified in KcsA-MthK comparison
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/allosteric-regulation/) — Conformational coupling between activation gate and selectivity filter in KcsA is a key example of allosteric regulation
- [NaK Channel from Bacillus cereus](/xray-mp-wiki/proteins/nak-channel/) — NaK shares high sequence homology and overall architecture with KcsA but has a non-selective filter resembling cyclic nucleotide-gated channels; closed NaK structure superimposes with KcsA (r.m.s.d. 0.73 A)
- [MthK (Methanobacterium thermoautotrophicum K+ Channel)](/xray-mp-wiki/proteins/mthk/) — Open NaK structure superimposes with open MthK (PDB 1LNQ, r.m.s.d. 0.74 A); MthK is the model for open tetrameric cation channel pore
