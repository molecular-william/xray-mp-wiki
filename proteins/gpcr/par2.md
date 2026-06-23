---
title: Human Protease-Activated Receptor 2 (PAR2) - Stabilized T4L Fusion
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature22309]
verified: false
---

# Human Protease-Activated Receptor 2 (PAR2) - Stabilized T4L Fusion

## Overview

Human Protease-Activated Receptor 2 (PAR2) is a class A G protein-coupled receptor that is irreversibly activated by proteolytic cleavage of its N terminus, which unmasks a tethered peptide ligand that binds and activates the transmembrane receptor domain. PAR2 is implicated in a wide range of diseases including cancer and inflammation. The crystal structures of PAR2 in complex with two distinct small-molecule antagonists ([AZ8838 (PAR2 Antagonist)](/xray-mp-wiki/reagents/ligands/az8838/) and [AZ3451 (PAR2 Antagonist)](/xray-mp-wiki/reagents/ligands/az3451/)) and a blocking antibody ([MAB3949 Monoclonal Antibody (PAR2-specific)](/xray-mp-wiki/reagents/antibodies/mab3949/) Fab) were solved, revealing multiple allosteric sites on the receptor that can be targeted for structure-based drug design. The PAR2 structure shares 36% sequence identity with [PAR1](/xray-mp-wiki/proteins/gpcr/par1/) but exhibits key structural differences in ECL2, ECL3, and TM5-7 that prevent [Vorapaxar](/xray-mp-wiki/reagents/ligands/vorapaxar/) binding.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature22309 | 5IRV | 2.80 | P1 | Human PAR2-StaR (nine thermostabilizing mutations: G89A, H108A, G157A, M166L, Y174A, V176E, M268A, I289A, T293A) with N-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (residues 1-54 replaced by T4 lysozyme inserted before F58), ICL3 cytochrome b562RIL insertion (between L269 and E276), glycosylation mutation N222Q, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) after K377, C-terminal His6 tag. Bound to antagonist [AZ8838 (PAR2 Antagonist)](/xray-mp-wiki/reagents/ligands/az8838/).
 | [AZ8838 (PAR2 Antagonist)](/xray-mp-wiki/reagents/ligands/az8838/) |
| doi/10.1038##nature22309 | 5IRW | 3.59 | P1 | Same PAR2-StaR [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fusion construct as above. Bound to antagonist [AZ3451 (PAR2 Antagonist)](/xray-mp-wiki/reagents/ligands/az3451/).
 | [AZ3451 (PAR2 Antagonist)](/xray-mp-wiki/reagents/ligands/az3451/) |
| doi/10.1038##nature22309 | 5IRX | 4.00 | P212121 | Human PAR2-StaR (nine thermostabilizing mutations) with N-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (residues 1-54 removed, first residue V55), ICL3 cytochrome b562RIL insertion (between L269 and E276), glycosylation mutation N222Q, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) after K377, C-terminal His6 tag (PAR2-StaR NDelta54/CDelta20 N222Q b562RIL-C04). Bound to weak antagonist AZ7188 and Fab fragment of [MAB3949 Monoclonal Antibody (PAR2-specific)](/xray-mp-wiki/reagents/antibodies/mab3949/) blocking antibody.
 | AZ7188, [MAB3949 Monoclonal Antibody (PAR2-specific)](/xray-mp-wiki/reagents/antibodies/mab3949/) Fab |

## Expression and Purification

No purification described.

## Crystallization

### doi/10.1038##nature22309

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Notes | PAR2-StaR [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) fusion co-crystallized with [AZ8838 (PAR2 Antagonist)](/xray-mp-wiki/reagents/ligands/az8838/) at 2.80 A (P1, 3 crystals merged, cell 37.11, 62.26, 87.34 A; alpha 104.90, beta 90.88, gamma 96.89). Co-crystallized with [AZ3451 (PAR2 Antagonist)](/xray-mp-wiki/reagents/ligands/az3451/) at 3.59 A (P1, 9 crystals merged, cell 37.10, 62.60, 86.47 A; alpha 104.38, beta 91.66, gamma 96.40). PAR2-StaR b562RIL C04 with Fab3949 at 4.00 A (P212121, 1 crystal, cell 38.52, 159.7, 164.1 A; alpha 90, beta 90, gamma 90).
 |


## Biological / Functional Insights

### Allosteric antagonist binding sites

Two distinct allosteric sites were identified on PAR2. [AZ8838 (PAR2 Antagonist)](/xray-mp-wiki/reagents/ligands/az8838/) binds in a fully occluded pocket near the extracellular surface, lined by residues from TM1-3, TM7 and ECL2. [AZ3451 (PAR2 Antagonist)](/xray-mp-wiki/reagents/ligands/az3451/) binds to a remote allosteric site outside the helical bundle. Both antagonists prevent structural rearrangements required for receptor activation and signalling. The slow binding kinetics of [AZ8838 (PAR2 Antagonist)](/xray-mp-wiki/reagents/ligands/az8838/) (low on-rate 1,021 M-1 s-1, residence time 1.4 h) is an attractive feature for competing against the tethered ligand.

### PAR2 vs PAR1 structural differences

PAR2 and [PAR1](/xray-mp-wiki/proteins/gpcr/par1/) share 36% sequence identity and overall structures are highly similar (r.m.s.d. 1.70 A between 252 aligned C-alpha atoms). Key differences: in PAR2, the top four helical turns of TM5 bend 5.9 A towards the TMD core; ECL2 is tethered to TM3 via a hydrogen bond between H227ECL2 and Y156 3.33; TM6 moves 4.7 A towards the core and TM7 moves 1.8 A outward on the extracellular side. These movements eliminate the [Vorapaxar](/xray-mp-wiki/reagents/ligands/vorapaxar/) binding pocket in PAR2. His135 2.64 in PAR2 (replaced by Tyr162 in [PAR1](/xray-mp-wiki/proteins/gpcr/par1/)) explains [AZ8838 (PAR2 Antagonist)](/xray-mp-wiki/reagents/ligands/az8838/) selectivity for PAR2 over [PAR1](/xray-mp-wiki/proteins/gpcr/par1/).

### Antibody-mediated blocking of PAR2

[MAB3949 Monoclonal Antibody (PAR2-specific)](/xray-mp-wiki/reagents/antibodies/mab3949/) Fab binds to the extracellular surface of PAR2 with high affinity (Kd 7.6 nM). The binding epitope comprises residues 59-63 from the amino terminus, residues 220 and 232-234 from ECL2, and residues 315-319 from TM6 and ECL3. The paratope includes all CDR loops, with most extensive contacts from CDR heavy loop 3. [MAB3949 Monoclonal Antibody (PAR2-specific)](/xray-mp-wiki/reagents/antibodies/mab3949/) blocks PAR2 activation by both [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) (IC50 286 nM) and activating peptide SLIGRL (IC50 253 nM), likely through direct competition with the tethered or activating peptide.

### Tethered ligand activation mechanism

PAR2 is activated by proteolytic cleavage of the N terminus, which unmasks a tethered peptide ligand (SLIGRL) that binds and activates the transmembrane domain. Asp228ECL2 is a central residue involved in receptor activation; mutation to Ala or Asn resulted in 123- and 165-fold loss of potency for the activating peptide. The ECL2 beta-hairpin (Thr215-Cys226) followed by a loop (His227-Leu235) occupies the top half of the orthosteric binding pocket.


## Cross-References

- [Human Protease-Activated Receptor 1 (PAR1)](/xray-mp-wiki/proteins/gpcr/par1/) — PAR2 shares 36% sequence identity with PAR1; structures compared in this paper
- [Vorapaxar](/xray-mp-wiki/reagents/ligands/vorapaxar/) — PAR1 antagonist; binding pocket eliminated in PAR2 due to structural differences
- [T4 Lysozyme (T4L)](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) — T4L fusion inserted into N terminus for PAR2 crystallization
- [Allosteric Regulation](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) — Paper demonstrates multiple allosteric sites on PAR2 for antagonist binding
- [Thermostabilization](/xray-mp-wiki/concepts/construct-design/thermostabilization/) — PAR2-StaR constructed with nine thermostabilizing mutations for crystallization
- [GPCR Active Conformation](/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-conformation/) — Antagonist binding prevents structural rearrangements required for GPCR activation
- [His6 Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) — Decahistidine tag added to C terminus for Ni-NTA affinity purification
- [Lauryl Maltose Neopentyl Glycol (LMNG)](/xray-mp-wiki/reagents/detergents/lmng/) — Primary detergent used for solubilization and purification of PAR2-StaR
- [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) — Related biological concept
- [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) — Additive used in purification or crystallization buffers
