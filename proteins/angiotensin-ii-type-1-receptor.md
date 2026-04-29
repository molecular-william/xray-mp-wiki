---

title: Angiotensin II Type 1 Receptor
created: 2026-04-27
updated: 2026-04-28
type: protein
tags: [gpcr, receptor]
sources: [doi/10.1016##j.cell.2018.12.006, doi/10.1016##j.cell.2015.04.011]

---
layout: default


# Angiotensin II Type 1 Receptor (AT1R)

## Overview

The angiotensin II type 1 receptor (AT1R) is a prototypical class A G-protein-coupled receptor (GPCR) that is central to cardiovascular and renal homeostasis. Activation by the octapeptide angiotensin II (AngII) triggers Gq-mediated calcium signaling, leading to vasoconstriction. AT1R is a major therapeutic target — angiotensin receptor blockers (ARBs) are used by over 5% of US adults. Beyond Gq, AT1R also couples to other G protein isoforms and engages β-arrestins and GRKs, making it a model system for studying biased agonism.

## Structural Biology

### Inactive-State Structure by SFX/XFEL (PDB: 4YAY)

The first AT1R structure was solved by **serial femtosecond crystallography (SFX)** at the LCLS X-ray free-electron laser (Zhang et al., 2015, Cell). This breakthrough method enabled structure determination from microcrystals too small for synchrotron diffraction.

- **Method**: LCP-SFX (lipidic cubic phase [serial-femtosecond-crystallography](/methods/structure-determination/serial-femtosecond-crystallography/)) at LCLS
- **Resolution**: 2.9 Å
- **Construct**: [bril](/reagents/protein-tags/bril/) fused to N-terminus; AT1R residues 1, 7–16, 320–359 truncated; fully glycosylated (no PNGase F treatment)
- **Key features**: ECL2 as β-hairpin; helix 8 in unusual bent conformation away from membrane; unique sodium-binding pocket with Asn295⁷·⁴⁶ (first GPCR structure with Ser at this position); Asn111³·³⁵–Asn295⁷·⁴⁶ hydrogen bond stabilizes inactive state
- **Critical binding residues**: Arg167ᴱᴰᴸ² (salt bridge with tetrazole), Tyr35¹·³⁹ (H-bond with naphthyridin), Trp84²·⁶⁰ (π–π stacking); all three mutations abolish binding
- **Docking**: Enabled structural basis for all clinically used ARBs (losartan, candesartan, valsartan, telmisartan, eprosartan, olmesartan, azilsartan). These featured a C-terminal truncation, N-terminal deletion (residues 7–16), and an N-terminal BRIL fusion. The antagonist-bound structures showed ECL2 as a β-hairpin and helix 8 in an unusual bent conformation away from the membrane plane.

### Active-State Structure (PDB: 6DO1)

The first active-state AT1R structure was determined at 2.9 Å resolution (Wingler et al., 2019, Cell), revealing the receptor bound to the partial agonist S1I8 and the conformation-stabilizing nanobody. Key features:

- **Construct design**: [bril](/reagents/protein-tags/bril/) inserted into ICL3 (residues 226–227) instead of N-terminus; I320 truncated to stop. This construct showed 2-fold higher AngII affinity than wild-type and retained strong nanobody binding.
- **Crystallization**: [lipidic-cubic-phase](/methods/crystallization/lipidic-cubic-phase/) (LCP) with [monoolein](/methods/crystallization/monoolein/) + [cholesterol-lipid](/reagents/lipids/cholesterol-lipid/), using [tris-buffer](/reagents/buffers/tris-buffer/)/MgCl₂/PEG 300 precipitant.
- **Conformational changes**: 11 Å outward displacement of TM6, inward rotation of TM7, rotation of TM5 away from transducer pocket, reorganization of ICL2 into a short α-helix, and helix 8 adopting a conventional membrane-parallel position.
- **Conserved motifs**: Y302⁷·⁵³ (NPxxY motif) rotated 10 Å inward; R126³·⁵⁰ participates in a hydrogen-bonding network with the nanobody CDR3.
- **Peptide binding mode**: S1I8 binds in extended conformation with N-terminus facing solvent and C-terminus buried in the receptor core. The binding pocket is remodeled into a half-β-barrel involving the receptor N-terminus, ECL2 β-hairpin, and the peptide's first three residues.
- **Unique activation mechanism**: AT1R uses a phenylalanine ratchet (F208⁵·⁵¹/F249⁶·⁴⁴/F250⁶·⁴⁵) and N111³·³⁵–N295⁷·⁴⁶ hydrogen bond instead of the canonical sodium-regulated ionic lock seen in other class A GPCRs.

## Expression and Purification

### Inactive-State Construct (4YAY — SFX)

- **Expression system**: [sf9-cells](/methods/expression-systems/sf9-cells/) (Bac-to-Bac [baculovirus-expression](/methods/expression-systems/baculovirus-expression/))
- **Solubilization**: 1% [ddm](/reagents/detergents/ddm/) + 0.2% [cholesterol-hydrogen-succinate](/reagents/lipids/cholesterol-hydrogen-succinate/)
- **Purification**: Affinity chromatography (His-tag on [bril](/reagents/protein-tags/bril/)), followed by [size-exclusion-chromatography](/methods/purification/size-exclusion-chromatography/)
- **SEC buffer**: Standard GPCR SEC buffer (20 mM [hepes-buffer](/reagents/buffers/hepes-buffer/) pH 7.5, 150 mM [sodium-chloride](/reagents/additives/sodium-chloride/), 0.05% [ddm](/reagents/detergents/ddm/))

### Active-State Construct (6DO1 — LCP)

- **Expression system**: [hek293-cells](/methods/expression-systems/hek293-cells/) (mammalian, transient transfection)
- **Detergent**: [ddm](/reagents/detergents/ddm/) for membrane solubilization
- **Purification**: Affinity chromatography (His-tag on [bril](/reagents/protein-tags/bril/)), followed by [size-exclusion-chromatography](/methods/purification/size-exclusion-chromatography/)
- **SEC buffer**: 20 mM [hepes-buffer](/reagents/buffers/hepes-buffer/) pH 7.5, 150 mM [sodium-chloride](/reagents/additives/sodium-chloride/), 0.05% [ddm](/reagents/detergents/ddm/), 1 μM [s1i8-angiotensin-ii](/reagents/ligands/s1i8-angiotensin-ii/)

## Crystallization

### Inactive-State (4YAY)

- **Method**: [lipidic-cubic-phase](/methods/crystallization/lipidic-cubic-phase/) (LCP) with [monoolein](/methods/crystallization/monoolein/)-based mesophase
- **Protein-to-lipid ratio**: Standard LCP ratio (~1:1 w/w)
- **Data collection**: LCLS X-ray free-electron laser (SFX)
- **Note**: Microcrystals too small for synchrotron diffraction; serial femtosecond crystallography enabled structure determination

### Active-State (6DO1)

- **Method**: [lipidic-cubic-phase](/methods/crystallization/lipidic-cubic-phase/) (LCP) — [monoolein](/methods/crystallization/monoolein/)-based mesophase
- **Lipid**: [monoolein](/methods/crystallization/monoolein/) supplemented with [cholesterol-lipid](/reagents/lipids/cholesterol-lipid/)
- **Precipitant**: [tris-buffer](/reagents/buffers/tris-buffer/)/MgCl₂/PEG 300
- **Ligand**: [s1i8-angiotensin-ii](/reagents/ligands/s1i8-angiotensin-ii/) (partial agonist) + conformation-stabilizing [nanobody](/reagents/antibodies/nanobody/)

## Biased Signaling

The AT1R is a model system for biased agonism. Simple mutations in AngII at position 8 (F→I→A or deletion) shift signaling from Gq-dominant to β-arrestin-dominant. Full agonists (F8) fit tightly into the active-state cavity, while smaller biased ligands (A8, deletion) cannot fully engage Y292⁷·⁴³, producing incomplete conformational changes.

## Therapeutic Relevance

- **ARBs** ([losartan](/reagents/ligands/losartan/), olmesartan, [valsartan](/reagents/ligands/valsartan/), etc.) — non-peptide antagonists that occupy a smaller volume at the bottom of the ligand-binding groove
- **Biased agonists** (e.g., TRV027, TRV028) — AngII analogs deficient in Gq coupling but retaining β-arrestin signaling; pursued for heart failure as alternatives to ARBs
- The active-state structure reveals steric incompatibilities between the peptide-bound pocket and ARB binding, explaining inverse agonism

## Related Entities

- [s1i8-angiotensin-ii](/reagents/ligands/s1i8-angiotensin-ii/) — partial agonist AngII analog (Sarcosine1, Isoleucine8)
- [nanobody](/reagents/antibodies/nanobody/) — conformation-stabilizing synthetic nanobody
- [monoolein](/methods/crystallization/monoolein/) — lipidic cubic phase matrix for LCP crystallization
- [mng-detergent](/reagents/detergents/mng-detergent/) — maltose neopentyl glycol used for solubilization
- [cholesterol-hydrogen-succinate](/reagents/lipids/cholesterol-hydrogen-succinate/) — CHS used to stabilize receptor in detergent
- [lipidic-cubic-phase](/methods/crystallization/lipidic-cubic-phase/) — LCP crystallization method
- [xray-crystallography](/methods/structure-determination/xray-crystallography/) — structure determination technique
- [zd7155](/reagents/ligands/zd7155/) — high-affinity antagonist (inactive-state structure, PDB: 4YAY)
- [losartan](/reagents/ligands/losartan/) — first clinically used ARB; surmountable antagonist
- [candesartan](/reagents/ligands/candesartan/) — insurmountable inverse agonist; triple salt bridge network with Arg167ᴱᴰᴸ²
- [valsartan](/reagents/ligands/valsartan/) — ARB with high affinity for AT1R
- [telmisartan](/reagents/ligands/telmisartan/) — long-acting ARB
- [bril](/reagents/protein-tags/bril/) — apocytochrome b562RIL fusion partner (N-terminal fusion in 4YAY construct)
- [serial-femtosecond-crystallography](/methods/structure-determination/serial-femtosecond-crystallography/) — SFX method used for 4YAY structure
- [sf9-cells](/methods/expression-systems/sf9-cells/) — Baculovirus expression system
- [ddm](/reagents/detergents/ddm/) — Solubilization detergent
- [cholesterol-hydrogen-succinate](/reagents/lipids/cholesterol-hydrogen-succinate/) — CHS for stabilization