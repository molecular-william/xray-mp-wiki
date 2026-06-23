---
title: Rat Neurotensin Receptor 1 (NTSR1)
created: 2026-06-02
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11558, doi/10.1038##ncomms8895, doi/10.1073##PNAS.1317903111, doi/10.1126##sciadv.abe5504]
verified: false
---

# Rat Neurotensin Receptor 1 (NTSR1)

## Overview

The rat [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) receptor 1 (NTSR1) is a class A G protein-coupled receptor (GPCR) belonging to the ghrelin receptor family that binds the tridecapeptide [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) (NTS). NTSR1 is involved in various physiological processes including neurotransmission, pain modulation, and regulation of body temperature. The thermostabilized NTSR1-GW5 construct with T4 lysozyme fusion enabled the first crystal structure of a [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) receptor in complex with NTS(8-13). Subsequently, directed evolution in E. coli yielded signaling-competent NTR1 variants crystallized without fusion proteins. A new crystallization design using a [DARPIN](/xray-mp-wiki/reagents/protein-tags/darpin/) D12 fusion chaperone enabled determination of five new structures: apo-state NTSR1 as well as complexes with nonpeptide inverse agonists [SR48692](/xray-mp-wiki/reagents/ligands/sr48692/) and SR142948A, partial agonist [RTI-3a (Partial NTSR1 Agonist)](/xray-mp-wiki/reagents/ligands/rti-3a/), and the novel full agonist [SRI-9829 (Full NTSR1 Agonist)](/xray-mp-wiki/reagents/ligands/sri-9829/), providing structural rationales for how ligands modulate NTSR1 activation and inactivation.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature11558 | Not specified | 2.80 | — | NTSR1-GW5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) (GW5 thermostabilizing mutations, [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) replacing ICL3) | NTS(8-13) |
| doi/10.1073##PNAS.1317903111 | Not specified | 3.26 | — | NTR1-TM86V-deltaIC3A (TM86V mutations, deltaIC3A deletion) | [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) |
| doi/10.1073##PNAS.1317903111 | Not specified | 2.75 | — | NTR1-TM86V-deltaIC3B | [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) |
| doi/10.1126##sciadv.abe5504 | Not specified | 2.5-3.2 | — | NTSR1-H4x (stabilized NTSR1-H4 mutant fused to [DARPIN](/xray-mp-wiki/reagents/protein-tags/darpin/) D12 via shared helix) | Multiple (NTS8-13, [SRI-9829 (Full NTSR1 Agonist)](/xray-mp-wiki/reagents/ligands/sri-9829/), [RTI-3a (Partial NTSR1 Agonist)](/xray-mp-wiki/reagents/ligands/rti-3a/), [SR48692](/xray-mp-wiki/reagents/ligands/sr48692/), SR142948A, apo) |

## Expression and Purification

- **Expression system**: E. coli (for NTR1 variants) and Sf9 insect cells (for NTSR1-GW5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)); NTSR1-H4x expressed in E. coli

- **Construct**: NTSR1-GW5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) for initial structure; TM86V-deltaIC3A/B for evolved structures; NTSR1-H4x (NTSR1-H4 mutant fused to [DARPIN](/xray-mp-wiki/reagents/protein-tags/darpin/) D12 crystallization chaperone via shared helix) for small-molecule ligand complexes

- **Notes**: NTSR1-H4 is a previously developed highly stable rNTSR1 mutant used for pharmacological studies


### Purification Workflow

- **Expression system**: E. coli
- **Expression construct**: NTSR1-H4x (NTSR1-H4 fused to [DARPIN](/xray-mp-wiki/reagents/protein-tags/darpin/) D12)
- **Tag info**: MBP-TrxA-His8 tag cleaved by [HRV 3C Protease](/xray-mp-wiki/reagents/additives/hrv-3c-protease/); octahistidine tag on [DARPIN](/xray-mp-wiki/reagents/protein-tags/darpin/)

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and harvest | Fermentation | — | 100 mM HEPES pH 8.0, 30% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 400 mM NaCl | Cells harvested at 5000g for 20 min at 4C, ~7g pellet per L culture |
| Cell lysis | Lysozyme treatment and sonication | — | Resuspension Buffer (100 mM HEPES pH 8.0, 30% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 400 mM NaCl) with 2 mg/ml lysozyme, 5 mM MgCl2, 0.05 mg/ml DNase I | Incubated 1 hour while stirring |
| Solubilization | Detergent solubilization | — | 2% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (n-dodecyl-beta-D-maltopyranoside) + 0.2% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Incubated 1 hour while stirring, followed by 30 min sonication |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Immobilized metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) (IMAC) | [TALON](/xray-mp-wiki/reagents/additives/talon/) Superflow (GE Healthcare) | Wash Buffer I: 25 mM HEPES pH 8.0, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 600 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 5 mM MgCl2, 2 mM 2-ME, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/); Wash Buffer II: 25 mM HEPES pH 8.0, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 150 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 2 mM 2-ME, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) + 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Batch incubation overnight; elution with 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) in Elution Buffer (25 mM HEPES pH 7.0, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 150 mM NaCl, 0.1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 2 mM 2-ME) |
| Desalting and tag cleavage | Size exclusion desalting + protease cleavage | PD MiniTrap G-25 columns (GE Healthcare) | G-25 Buffer (10 mM HEPES pH 7.0, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 2 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/)) | Protein incubated 3 hours with [HRV 3C Protease](/xray-mp-wiki/reagents/additives/hrv-3c-protease/) to cleave MBP and TrxA tags |
| Cation exchange chromatography | [Ion-Exchange Chromatography](/xray-mp-wiki/methods/purification/ion-exchange-chromatography/) | SP Sepharose (GE Healthcare) | G-25 Buffer |  |
| [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) | [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) (SEC) | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) 10/300 GL (GE Healthcare) | SEC Buffer (10 mM HEPES pH 7.0, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), 2 mM [DTT](/xray-mp-wiki/reagents/additives/dtt/)) |  |


## Crystallization

### doi/10.1038##nature11558

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Notes | NTSR1-GW5-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) crystallized in LCP. Space group P21 with cell dimensions a=46.96, b=69.62, c=97.53, alpha=90, beta=101.7, gamma=90 deg. Data collected at Diamond Light Source beamline I24. |

### doi/10.1126##sciadv.abe5504

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) and vapor diffusion |
| Notes | NTSR1-H4x crystallized in complex with NTS8-13, [SRI-9829 (Full NTSR1 Agonist)](/xray-mp-wiki/reagents/ligands/sri-9829/), [RTI-3a (Partial NTSR1 Agonist)](/xray-mp-wiki/reagents/ligands/rti-3a/), [SR48692](/xray-mp-wiki/reagents/ligands/sr48692/), SR142948A, and in apo state. LCP crystallization for most complexes; vapor diffusion used for NTSR1-H4x:NTS8-13. For LCP: [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/), 10 mg/ml protein, 50-250 mM NaCl, 100 mM HEPES pH 7.5, 0.1 M MgCl2, 28-30% [PEG400](/xray-mp-wiki/reagents/additives/peg-400/), 2% [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/), 0.04-0.5% NG ([NG](/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/)). For NTSR1-H4bmx: 100 mM [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) pH 9.4, 1 M NaCl, 0.3% NG, 15% [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/), 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/). Vapor diffusion: 100 mM HEPES pH 7.0, 27% [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/), 0.069-0.15% NG, 3% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/). Crystals grown at 20C. Cryoprotected with 50 mM [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) pH 9.4, 1 M NaCl, 0.3% NG, 15% [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/), 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/). Data collected at Swiss Light Source beamline X06SA, wavelength 1 A, 100K. |


## Biological / Functional Insights

### Agonist-induced and inverse agonist-induced conformational changes in NTSR1

Five new NTSR1 structures with small-molecule ligands revealed distinct conformational states. Full agonists NTS8-13 and [SRI-9829 (Full NTSR1 Agonist)](/xray-mp-wiki/reagents/ligands/sri-9829/) induce contraction of the extracellular binding pocket, while inverse agonists [SR48692](/xray-mp-wiki/reagents/ligands/sr48692/) and SR142948A favor expansion of the extracellular opening of helices VI and VII, causing constriction at the intracellular portion. The partial agonist [RTI-3a (Partial NTSR1 Agonist)](/xray-mp-wiki/reagents/ligands/rti-3a/) induces an intermediate contraction. This demonstrates that ligand efficacy correlates with the ability to mimic the binding mode of the endogenous agonist [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/).

### Role of L-Leu and adamantyl moieties in agonism vs inverse agonism

The bulky adamantyl moiety of inverse agonists [SR48692](/xray-mp-wiki/reagents/ligands/sr48692/) and SR142948A exerts a steric effect that widens the hydrophobic subpocket at F331(6.58), hindering contraction of the extracellular receptor portion. In contrast, the isobutyl side chain of L-Leu (present in agonists) is optimally shaped to induce and stabilize a contracted arrangement of TM6 at its extracellular tip. Replacing the adamantyl moiety of [SR48692](/xray-mp-wiki/reagents/ligands/sr48692/) with an L-Leu side chain converts this inverse agonist into the partial agonist [RTI-3a (Partial NTSR1 Agonist)](/xray-mp-wiki/reagents/ligands/rti-3a/).

### ECL3 and TM7 interactions crucial for NTSR1 activation

All agonists form contacts with ECL3, TM6, and TM7 on one wall of the binding site, and with the ECL2 beta-hairpin and TM2 on the opposite wall. This anchoring pattern is important for inducing contraction of the extracellular receptor portion. NTS8-13 interacts with W339(ECL3), F344(7.28), Y347(7.31), and H348(7.32) in TM7. Mutagenesis of these residues causes moderate drops in agonist affinity but substantially stronger reductions in Gq potency (100-1000 fold), suggesting they stabilize contracted binding site conformation.

### Polar network and hydrophobic core in activation transmission

A network of polar interactions beneath the agonist binding site links the extracellular conformational changes to the intracellular G protein interface. Key residues include D150(3.33), R328(6.55), N355(7.39), and Y351(7.35) in the polar network, and F358(7.42), Y324(6.51), W321(6.48), and F317(6.44) in the hydrophobic cascade. D150(3.33)A, R328(6.55)M, and N355(7.39)A mutations markedly reduce agonist potency without strongly affecting affinity, confirming their role in activation signal transmission.


## Cross-References

- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — T4L fusion replacing ICL3 in NTSR1-GW5-T4L construct
- [Designed Ankyrin Repeat Protein (DARPin)](/xray-mp-wiki/reagents/protein-tags/darpin/) — DARPin D12 fusion chaperone used for NTSR1-H4x crystallization
- [NTSR1 TM86V-deltaIC3A Mutant](/xray-mp-wiki/proteins/gpcr/tm86v-delta-ic3a/) — Evolved NTR1 variant crystallized without fusion proteins
- [Decyl Maltoside (DM)](/xray-mp-wiki/reagents/detergents/decyl-maltoside/) — Detergent used for NTSR1 solubilization and thermostability measurement
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Detergent used for NTSR1 solubilization
- [SR48692](/xray-mp-wiki/reagents/ligands/sr48692/) — Non-peptide inverse agonist co-crystallized with NTSR1-H4x
- [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) — Endogenous peptide agonist used for comparison with small-molecule ligands
- [Glycine (Buffer)](/xray-mp-wiki/reagents/buffers/glycine/) — Used in cryoprotection solution for NTSR1-H4bmx crystals
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Ion-Exchange Chromatography](/xray-mp-wiki/methods/purification/ion-exchange-chromatography/) — Method used in structure determination or purification
