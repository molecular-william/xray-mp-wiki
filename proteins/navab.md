---
title: NavAb Bacterial Voltage-Gated Sodium Channel
created: 2026-05-27
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2019.06.031, doi/10.1038##ncomms3465, doi/10.1038##nature10238, doi/10.1038##ncomms14205]
verified: false
---

# NavAb Bacterial Voltage-Gated Sodium Channel

## Overview

NavAb is a bacterial voltage-gated sodium channel from Alicyclobacillus sp. that serves as the evolutionary ancestor of eukaryotic voltage-gated sodium (NaV) and calcium (CaV) channels. NavAb is composed of a tetramer of identical subunits, each containing a voltage-sensing module (VS, S0-S4), an S4-S5 linker, and a pore module (PM, S5-P-S6). This paper reports the first high-resolution resting-state structure of a voltage-gated sodium channel, revealing the complete voltage-dependent gating mechanism including the sliding helix mechanism of voltage sensing, S4-S5 linker-mediated pore opening, and activation gate closure.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.cell.2019.06.031 | 6P6X | 4.0 A | N/A | NavAb G94C/Q150C disulfide-crosslinked resting state, C-terminal truncation (Delta28); homotetramer of VS-S4-S5 linker-PM subunits; disulfide bond between G94C on S4 of one subunit and Q150C on S5 of neighboring subunit | Disulfide crosslink (G94C-Q150C) stabilizing resting state conformation |
| doi/10.1016##j.cell.2019.06.031 | 6P6Y | 2.8 A | N/A | NavAb V100C/Q150C disulfide-crosslinked activated state, C-terminal truncation (Delta28); homotetramer; disulfide bond between V100C on S4 and Q150C on S5 of neighboring subunit | Disulfide crosslink (V100C-Q150C) stabilizing activated state conformation |
| doi/10.1016##j.cell.2019.06.031 | 6P6W | N/A | N/A | NavAb KAV/G94C/Q150C activated state (crystal structure, not cryo-EM); voltage-shifting mutations N49K/L109A/M116V (KAV) plus G94C/Q150C disulfide crosslink | Disulfide crosslink (G94C-Q150C) |
| doi/10.1038##ncomms3465 | 3RVY | N/A | N/A | NavAb closed pore conformation; used as structural comparison to NavMs open pore | None (comparison structure) |
| doi/10.1038##nature10238 | 3J5Q | 2.70 A | I222 | NavAb-Ile217Cys cysteine mutant; homotetramer; used for Hg-SAD phasing; Ile217 mutated to Cys for mercury binding site identification; two symmetry-related molecules in asymmetric unit forming dimer-of-dimers arrangement | None (native structure; separate Hg-derivative used for phasing) |
| doi/10.1038##nature10238 | 3J5Q | 2.80 A | I222 | NavAb-Ile217Cys cysteine mutant; homotetramer; second data set with slightly different cell dimensions; same dimer-of-dimers crystal packing | None |
| doi/10.1038##nature10238 | 3J5R | 2.95 A | I222 | NavAb-Met221Cys cysteine mutant; homotetramer; Met221 mutated to Cys; pore structure highly similar to Ile217Cys variant with tapering around Met221Cys side-chains | None |

## Expression and Purification

- **Expression system**: Escherichia coli
- **Construct**: Full-length NavAb from Alicyclobacillus sp.; wild-type and Ile217Cys/Met221Cys cysteine mutants

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Standard bacterial lysis | — |  |  |
| Membrane solubilization | Detergent solubilization | — |  |  |
| Purification | Affinity chromatography | — |  |  |
| Final polishing | Size-exclusion chromatography | — |  |  |


## Crystallization

### doi/10.1038##nature10238

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, hanging drop |
| Protein sample | NavAb-Ile217Cys or NavAb-Met221Cys at approximately 10 mg/mL |
| Reservoir | Not specified in supplementary information |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Crystals grew in space group I222 with two molecules in the asymmetric unit forming a dimer-of-dimers arrangement. Type I crystal lattice with stacked layers of NavAb channels in a membrane-like environment. Phospholipid molecules observed bound to the channel (six per subunit). |


## Biological / Functional Insights

### Resting-state voltage sensor conformation

In the resting state, the S4 segment of the voltage-sensing domain is drawn intracellularly, with three gating charges (R1-R3) passing through the transmembrane electric field. The S4 helix adopts a 3(10) helix conformation from G94C to R4. An extracellular aqueous cleft is formed between the S1-S2 and S3-S4 helical hairpins, wider and shallower than in the activated state. The S3 helix tilts slightly toward S4 and the S3-S4 loop is shorter.

### S4-S5 linker elbow mechanism

The inward movement of S4 in the resting state forms a sharply angled bend (elbow) at the junction of S4 with the S4-S5 linker. This elbow tightens the collar of S4-S5 linkers around the S5 and S6 segments of the pore module, preventing opening of the S6 activation gate. Hydrophobic residues (I119, L123, V126) on the S4-S5 linker interact with conserved residues (N211, I216) on S6, keeping the activation gate tightly closed at residue I217. Upon depolarization, S4 moves outward by ~11.5 A, loosening the collar and allowing the S6 activation gate to open to 10.5 A diameter.

### Sliding helix mechanism of voltage sensing

S4 moves almost vertically across the membrane (~11.5 A) while also rotating significantly. The gating charges exchange ion pair partners between the intracellular negative charge (INC) cluster (E59, E80) and the extracellular negative charge (ENC) cluster (E32, N49) as S4 translocates through the hydrophobic constriction site (HCS) on S2. This movement is consistent with the classical sliding helix mechanism of voltage-dependent gating, not the transporter or paddle mechanisms. In the activated state, S4 changes from a 3(10) helix to a loop plus alpha helix followed by a 3(10) helix.

### Phospholipid binding sites

Ordered 1,2-dimyristoyl-sn-glycero-3-phosphocholine (DMPC) phospholipid molecules were observed in the cryo-EM structure. Phosphate head groups interact with residues W76 on S2 and S121, P128 on the S4-S5 linker. Acyl chains interact with V120, I124, and I127 on the S4-S5 linker. These phospholipid binding sites may represent drug target sites in the channel.

### Implications for sodium channel pharmacology

The resting-state structure provides insights into state-dependent modulation by drugs and toxins. Local anesthetics and antiarrhythmics can access their blocking site through the pore via fenestrations in the resting state. The conformational change between resting and activated states at the receptor site for gating modifier toxins and drugs suggests that drug binding may stabilize specific conformational states.

### Pre-open state conformation of NavAb

The conformation of NavAb in crystals fits with expectations for a pre-open state: the voltage sensors are activated, the selectivity filter is rigid and open, but the pore is closed by the intracellular activation gate. The conformation does not fit the open state (activation gate is closed) nor the inactivated state (selectivity filter is rigidly held open, not collapsed). This is consistent with the slow-inactivation mechanism observed in NaChBac and related bacterial sodium channels, which involves relaxation or collapse of the selectivity filter and pore lining.

### Conserved selectivity filter architecture in NaV and CaV channels

The selectivity filter sequence in the NaChBac channel family is conserved as TLESW. In vertebrate NaV channels, the high field-strength site is formed by the DEKA selectivity motif, but this is EEEE or EEDD in CaV channels. These amino acid differences indicate that NavAb achieves selectivity for Na+ over Ca2+ through subtly different mechanisms. The architecture of the NaV and CaV channel pores is highly similar to the pore structure observed in NavAb.

### Ion coordination in the NavAb selectivity filter

The NavAb selectivity filter features potential ion interaction sites at Site_HFS (E177), Site_CEN (L176*), and Site_IN (T175*). A proposed Na+ ion coordination scheme involves four oxygen atoms coordinating a centrally located Na+ ion in a square pyramidal or square bipyramidal geometry. Putative water molecules are modeled 2.5 A off the backbone carbonyls of Leu176, superimposing onto site 3 carbonyls from K+ channel selectivity filters. The geometry at Site_IN approximates an ideal coordination scheme for hypothetical water molecules bound off Thr175 backbone carbonyls. This coordination scheme is chemically validated by superposition with a 0.95 A resolution guanine tetraplex structure showing ideal Na+-coordination geometry.

### Conserved interaction network in the NavAb pore module

An interconnected network of hydrogen bond interactions is centered around the selectivity filter-lining Glu177 residues, extending throughout the P- and P2-helices. A highly-conserved P-helix-S5 hydrogen bonding interaction is observed between Ser166 and Thr149. The Glu177 side-chain interacts with backbone amides of Ser180 and Met181 from the P2-helix of a neighboring subunit. This interaction network likely determines the structure and stability of the pore and selectivity filter.

### Pore domain rigid-body motion during gating

Superposition of NavAb closed pore domain and Kv1.2/2.1 open pore domain subunits demonstrates tight structural coupling between S5-S6 helices in voltage-gated ion channels. Two rigid-body motions occur during gating: one for the pore modules (S5-S6) and one for the S4-S5 linkers/VSDs. The spatial relationship among alpha-helices within each bundle remains relatively constant as the VSD rolls over the PM, pivoting at the base of the S5 segment. The S4-S5 linker pivots along the membrane interface with largest displacements occurring at the intracellular side of the VSD (e.g., the S1N helix).

### Crystal packing and membrane-like environment

The stacked layers of NavAb channels observed in the Type I crystal lattice resemble phospholipid bilayers. Six (of seven) phospholipids per subunit are bound to NavAb, representing the outer and inner leaflets of the membrane bilayer. The VSDs are particularly devoid of lattice distortions: extracellular loops are completely free from direct crystal contacts and only a minor contact is observed between the S1N helix and the intracellular S2-S3 loop.


## Cross-References

- [NavMs Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/navms/) — Related bacterial sodium channel with open pore conformation for comparison
- [Sodium Channel Gating and Selectivity](/xray-mp-wiki/concepts/sodium-channel-gating/) — Paper elucidates voltage-sensing and pore gating mechanisms
- [KcsA Potassium Channel](/xray-mp-wiki/proteins/kcsa/) — Structural comparison for selectivity filter architecture
- [Voltage Sensor Paddle](/xray-mp-wiki/concepts/voltage-sensor-paddle/) — Voltage-sensing domain architecture comparison with NavAb VSD
- [Channel Gating](/xray-mp-wiki/concepts/channel-gating/) — Paper provides structural basis for voltage-dependent gating
- [Intramembrane Ion Coordination](/xray-mp-wiki/concepts/intramembrane-ion-coordination/) — Paper models Na+ coordination scheme in selectivity filter
- [Single-Wavelength Anomalous Diffraction](/xray-mp-wiki/methods/single-wavelength-anomalous-diffraction/) — SAD phasing with mercury derivative used for NavAb-Ile217Cys structure
- [C-Type Inactivation](/xray-mp-wiki/concepts/c-type-inactivation/) — Paper discusses inactivation mechanism and selectivity filter collapse
