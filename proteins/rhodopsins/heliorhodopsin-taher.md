---
title: Heliorhodopsin (TaHeR) from Thermoplasmatales archaeon SG8-52-1
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-019-1604-6, doi/10.1038##s41598-022-17716-9]
verified: false
---

# Heliorhodopsin (TaHeR) from Thermoplasmatales archaeon SG8-52-1

## Overview

Heliorhodopsin (HeR) from an uncultured Thermoplasmatales archaeon SG8-52-1 (TaHeR) is a member of the heliorhodopsin family, a distinct class of microbial rhodopsins discovered through functional metagenomics. HeRs have seven predicted transmembrane helices and bind an all-trans retinal chromophore as in type-1 microbial rhodopsins, but exhibit less than 15% sequence identity with type-1 and type-2 rhodopsins and display the reverse orientation in the membrane. TaHeR does not function as a proton pump or ion channel; instead it exhibits a long-lived photoactivated state and is thought to function as a signalling photoreceptor. The 2.4 A crystal structure reveals an overall fold similar to bacteriorhodopsin, with a linear hydrophobic pocket for retinal binding, a unique polar-interaction network around the Schiff base, and an unexpected lateral fenestration above the beta-ionone ring that facilitates retinal uptake from the environment. A 1.97 A structure at pH 4.5 revealed a chloride anion in the Schiff base cavity (SBC) that substitutes for the neutralized Glu-108 counterion, and identified an intramolecular signaling pathway connecting the SBC to the extracellular A-B loop via conserved residues including His-23, Gln-26, and Trp-243.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##s41586-019-1604-6 | 6IS6 | 2.4 A | P212121 | Full-length TaHeR with N-terminal 6x His tag, expressed in E. coli C41(Rosetta) | all-trans retinal (covalently bound via Schiff base to Lys238) |
| doi/10.1038##s41598-022-17716-9 | 7U55 | 1.97 A | P21212 | Full-length TaHeR with N-terminal 6x His tag | all-trans retinal, chloride ion |

## Expression and Purification

- **Expression system**: E. coli C41(Rosetta)
- **Construct**: Full-length TaHeR with N-terminal 6x His tag, codon-optimized for E. coli
- **Induction**: 1 mM IPTG for 20 h at 25 C
- **Media**: 10 uM all-trans retinal supplemented in culture

### Purification Workflow

*Source: doi/10.1038##s41586-019-1604-6*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | Sonication | — | 20 mM Tris-HCl pH 7.5, 20% glycerol | Cells were disrupted by sonication |
| Membrane isolation | Ultracentrifugation | — | 20 mM Tris-HCl pH 7.5, 20% glycerol | Crude membrane fraction collected at 180,000g for 1 h |
| Membrane solubilization | Detergent solubilization | — | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 1% DDM | Membrane fraction solubilized in DDM-containing buffer |
| Affinity chromatography | Ni-NTA | Ni-NTA agarose | 0.03% DDM | His-tagged TaHeR purified by Ni-NTA affinity chromatography |

### Purification Workflow

*Source: doi/10.1038##s41598-022-17716-9*

- **Expression system**: E. coli C41(Rosetta)
- **Expression construct**: TaHeR-I51C mutant for EPR studies
- **Tag info**: N-terminal 6x His tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent solubilization | — | 50 mM MES pH 6.5, 300 mM NaCl, 1% OG + 1% OG (octylglucoside) | Purification carried out in OG detergent |
| Affinity chromatography | Ni-NTA | HisTrap 1 mL Ni-NTA column (GE Healthcare) | 50 mM MES pH 6.5, 300 mM NaCl, 1% OG, 20 mM imidazole + 1% OG | Elution with 20-500 mM imidazole gradient over 30 CV |
| Size exclusion chromatography | SEC | Superdex 200 10/300 GL (Cytiva) | 20 mM MES pH 6.5, 300 mM NaCl, 1% OG + 1% OG | Fractions with A550/A280 > 0.7 combined for crystallization |


## Crystallization

### doi/10.1038##s41586-019-1604-6

| Parameter | Value |
|---|---|
| Method | [Lipidic cubic phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) crystallization (in meso) |
| Protein sample | Purified TaHeR in DDM solution, reconstituted into [monoolein](/xray-mp-wiki/reagents/lipids/monoolein/)-based lipidic cubic phase |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) |
| Protein-to-lipid ratio | Not specified |
| Temperature | 293 K |
| Growth time | Not specified |
| Cryoprotection | Crystals harvested directly and flash frozen in liquid nitrogen |
| Notes | Crystals obtained by in meso crystallization. Data collected to 2.4 A resolution. Space group P212121. Structure solved by molecular replacement using [bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (PDB 1M0L) as search model after trimming side chains to alanine. |

### doi/10.1038##s41598-022-17716-9

| Parameter | Value |
|---|---|
| Method | [Bicelle crystallization](/xray-mp-wiki/methods/crystallization/bicelle-crystallization/) |
| Protein sample | Purified TaHeR at 7.5 mg/ml in OG, combined with bicelles (2:1 ratio, final 5 mg/ml protein, 8% bicelle) |
| Reservoir | 26% PEG 3350, 0.1 M sodium phosphate monobasic pH 4.5, 0.28 M ammonium sulfate, 0.18 M 1,6-hexanediol |
| Mixing ratio | 4 ul protein-bicelle + 1.5 ul reservoir |
| Temperature | 307 K (34 C) |
| Growth time | Several months |
| Cryoprotection | None - crystals flash frozen directly in liquid nitrogen |
| Notes | First HeR crystallized via bicelles. Large 50-100 um diamond-shaped crystals. Hanging drop vapor diffusion. Data collected at APS beamline 23-ID-B. Structure solved by molecular replacement using basic TaHeR (PDB 6IS6) at 1.97 A. Space group P21212. |


## Biological / Functional Insights

### Overall fold similarity to bacteriorhodopsin

The overall fold of TaHeR is similar to [bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) (BR), with seven transmembrane helices. However, there are notable differences: TM3 is kinked by a hydrogen bond between Ser114 and the carbonyl oxygen of Ser111 (instead of the Pro91 kink in BR), and TM7 is not kinked at Lys238 (contrast with the conserved kink in type-1 rhodopsins). Sequence identity between HeR and BR is less than 15%.

### Dimer interface

TaHeR forms a dimer in the crystal structure with an extensive interface of approximately 1800 A^2 per protomer. The dimer is stabilized by hydrogen bonds involving Glu186-Tyr48, Thr125-Asn44, and Thr131-Thr131' and Thr155-Thr155' interactions. HS-AFM analysis confirmed that HeR typically functions as a dimer in the lipid membrane.

### Lateral fenestration for retinal capture

An unexpected lateral fenestration between TM5 and TM6, located above the beta-ionone ring of the retinal chromophore, provides a direct pathway for retinal from the lipid environment to the binding pocket. This fenestration is critical for capturing exogenous retinal, since HeR-expressing organisms lack retinal biosynthetic pathways. The G171W mutant, which blocks the fenestration, showed no retinal regeneration, confirming the functional role of this feature.

### Unique retinal binding pocket

The retinal-binding pocket is a linear hydrophobic cavity lined by residues including Tyr109, Asn143, Phe203, Phe206, Ala113, and Met116. Despite the low sequence identity with type-1 rhodopsins, the residues accommodating the C11-C12 bond (Tyr109, Phe203, Phe206) similarly contribute to 13-cis isomerization. A conserved glycine (Gly146) near the beta-ionone ring increases planarity for red-shifted absorption, as in type-1 rhodopsins.

### Schiff base environment and polar-interaction network

The Schiff base (Lys238) forms a hydrogen bond with the counterion Glu108, which is surrounded by polar residues Ser112 and Ser234. A unique polar network includes His23, His82, Glu108, and Ser234 with a four-coordinated water molecule, providing a hydrophilic environment around the Schiff base. This is distinct from BR, where the equivalent region has hydrophobic/aromatic residues. The proton-accepting group (PAG) for M intermediate formation appears to be formed by the hydrogen-bonding network including water molecules, rather than a specific carboxylate or histidine residue.

### Functional characterization as signalling photoreceptor

TaHeR exhibits a photocycle with K, M, and O intermediates and a long-lived photoactivated state (tau approximately 1 s). No proton release from the protein is observed, and the protein does not function as a proton pump or ion channel. The long O intermediate lifetime is conserved across HeRs from bacteria, archaea, eukaryotes, and giant viruses, suggesting a conserved signalling photoreceptor function.

### Chloride binding at low pH in Schiff base cavity

The 1.97 A TaHeR structure at pH 4.5 revealed a chloride anion in the Schiff base cavity (SBC) that serves as a surrogate counterion to stabilize the protonated retinal Schiff base (RSBH+) when the primary counterion Glu-108 is neutralized by protonation at low pH. This is analogous to HeR 48C12, which accommodates acetate at pH 4.3. The chloride ion is hydrogen bonded to the RSBH+ through a water-mediated network. Under basic conditions (pH 8.0), the SBC contains only water molecules and the Glu-108 counterion. Most HeRs are predicted to accommodate exogenous anions as surrogate counterions under acidic conditions or when the counterion is mutated.

### Intramolecular signal transduction pathway

Comparison of TaHeR structures at pH 8.0 and pH 4.5 reveals a conserved intramolecular signaling pathway: (1) chloride/acetate binding in the SBC at low pH, (2) reorientation of His-23, (3) displacement of a water molecule adjacent to Ser-78, (4) disordering of Gln-26 and Trp-243 into two conformations. This pathway connects the SBC to the extracellular A-B loop, which shows a ~6 A shift at residue Ile-51 between the two structures. Similar changes are observed in HeR 48C12 between its pH 8.8 and pH 4.3 structures, suggesting a conserved signaling mechanism among HeRs.

### DEER spectroscopy reveals dimer-of-dimer assemblies

DEER (double electron-electron resonance) spectroscopy on spin-labelled TaHeR (I51C mutant with MTSL or IAP labels) revealed distance distributions indicating transient dimer-of-dimer assemblies. Two distance populations were observed at ~4.7 nm (dimer) and ~6.6 nm (dimer-of-dimers). Light irradiation and acidification increase the population of the 6.6 nm long-distance peak, suggesting pH- and light-dependent oligomerization. These dimer-of-dimer assemblies may be relevant for transducer protein binding in a sensory function, consistent with HS-AFM observations.


## Cross-References

- [Bacteriorhodopsin](/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/) — Structural homolog with similar overall fold despite less than 15% sequence identity
- [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) — All-trans retinal chromophore covalently bound via Schiff base to Lys238
- [Retinal Chromophore Conformation](/xray-mp-wiki/concepts/retinal-chromophore-conformation/) — Retinal configuration and isomerization in HeR compared to type-1 rhodopsins
- [Lipidic Cubic Phase Crystallization](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — Structure solved by in meso crystallization in monoolein
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used in the lipidic cubic phase crystallization matrix
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization and purification
- [Bicelle Crystallization](/xray-mp-wiki/methods/crystallization/bicelle-crystallization/) — Low pH structure (1.97 A) solved using bicelle crystallization method
- [DEER Spectroscopy](/xray-mp-wiki/methods/structure-determination/deer-spectroscopy/) — DEER revealed pH- and light-dependent dimer-of-dimer assemblies of TaHeR
- [Rhodopsin Photocycle](/xray-mp-wiki/concepts/rhodopsin-photocycle/) — TaHeR photocycle with K, M, and O intermediates characteristic of microbial rhodopsins
- [MES](/xray-mp-wiki/reagents/buffers/mes/) — MES buffer used in purification and crystallization at pH 6.5
