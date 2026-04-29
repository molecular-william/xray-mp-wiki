---

title: Endothelin ETB Receptor
created: 2026-04-27
updated: 2026-04-27
type: protein
tags: [gpcr, receptor, membrane-protein]
sources: [doi/10.1016##j.bbrc.2019.12.091]

---


# Endothelin ETB Receptor

## Overview

The endothelin ETB receptor is a class A G-protein-coupled receptor (GPCR) that binds endothelin-1 (ET-1), ET-2, ET-3, and sarafotoxins. ETB receptors are expressed in vascular endothelium and vascular smooth muscle. Stimulation of endothelial ETB induces nitric oxide-mediated vasorelaxation and hypotension, while smooth muscle ETB activation causes vasoconstriction. ETB receptors are therapeutic targets for circulatory diseases including pulmonary arterial hypertension (PAH).

## Structure

- **PDB ID**: 6LRY (ETB-S6b complex)
- **Resolution**: 3.0 Å
- **Space group**: P2₁2₁2₁
- **Construct**: ETB-Y5-T4L — thermostabilized with 5 mutations (R124Y¹·⁵⁵, D154A²·⁵⁷, K270A⁵·³⁵, DS342A⁶·⁵⁴, I381A⁷·⁴⁸) + T4 lysozyme (T4L) inserted into intracellular loop 3 (between L303⁵·⁶⁸ and L311⁶·²³)
- **Phasing**: Molecular replacement using ET-3-bound receptor (PDB 6IGK)
- **Data collection**: 32 datasets merged (KAMO system)

The receptor consists of canonical 7 transmembrane helices (TM), amphipathic helix 8 (H8) at the C-terminus, and two antiparallel β-strands in extracellular loop 2 (ECL2).

## Activation Mechanism

### Inactive State (Antagonist-bound)
- **W336⁶·⁴⁸–D147²·⁵⁰ salt bridge**: Stabilizes the inactive conformation by connecting TMs 2, 3, 6, and 7 at the receptor core
- This salt bridge network is a hallmark of class A GPCR inactive states

### Active State (Agonist-bound, S6b)
- **W336⁶·⁴⁸ rotation**: W336 rotates inwardly and forms a hydrogen bond with N378⁷·⁴⁵
- **D147²·⁵⁰ rearrangement**: Forms hydrogen bonds with N119¹·⁵⁰ and T188³·³⁹, disrupting the inactive salt bridge
- **TM5 displacement**: The intracellular end of TM5 opens outward by 4 Å relative to inactive/endothelin-bound states — a conformational change analogous to what is seen in neurotensin receptor (NTSR1) upon agonist binding, and preceding the larger TM6 outward movement (10–14 Å) seen in full G-protein-coupled states
- This suggests the S6b-bound receptor adopts a more active conformation for G-protein coupling

## Ligand Binding

### [[sarafotoxin-s6b]]
- 21-amino-acid peptide with bicyclic architecture (disulfide bonds C1–C15 and C3–C11)
- N-terminal region (residues 1–7), α-helical region (residues 8–17), C-terminal region (residues 18–21)
- 4 cysteines conserved with ET-1/ET-3; 8 residues differ
- K9 forms a salt bridge with D246ᴱᴰᴸ² in ECL2, anchoring the α-helical region

### Endothelin-1 and Endothelin-3
- Similar bicyclic architecture; S6b superimposes well (RMSD for Cα = 0.39 and 0.40 Å)
- ET-1 structure at 2.0 Å resolution elucidated detailed activation process

## Solubilization and Purification

- **Expression**: [[sf9-cells]] (baculovirus [[baculovirus-expression]])
- **Construct**: N-terminal HA signal peptide + Flag epitope tag (DYKDDDDK) + 9-aa linker; C-terminus truncated after S407; 3 cysteines mutated to alanine (C396A, C400A, C405A) to avoid palmitoylation
- **Solubilization**: 1% [[ddm]], 0.2% [[cholesterol-hydrogen-succinate]], 20 mM [[tris-buffer]]-HCl pH 7.5, 200 mM [[sodium-chloride]], 2 mg/mL iodoacetamide, 1 hr at 4°C
- **Affinity**: [[talon-resin]] (GFP-His₁₀ tag), washed with 0.1% [[lmng]] + 0.01% [[cholesterol-hydrogen-succinate]] + 15 mM [[imidazole]]; eluted with 0.01% [[lmng]] + 0.001% [[cholesterol-hydrogen-succinate]] + 200 mM [[imidazole]]
- **Tag removal**: [[tev-protease]] cleavage; GFP-His₁₀ and TEV removed by [[talon-resin]]
- **SEC**: [[superdex-columns]] 10/300 Increase, 20 mM [[tris-buffer]]-HCl pH 7.5, 150 mM [[sodium-chloride]], 0.01% [[lmng]], 0.001% [[cholesterol-hydrogen-succinate]]
- **Concentration**: 40 mg/mL (Millipore 50 kDa MWCO [[amicon-filters]])
- **Crystallization**: S6b added during concentration; crystals soaked with S6b prior to data collection

## Related Endothelin Receptors

- **ETA receptor**: Expressed in vascular smooth muscle; stimulation causes vasoconstriction
- **ET-1**: Most potent vasoconstrictor known (LD₅₀ for mice ~0.015 mg/kg)
- **Endothelin receptor antagonists**: Bosentan (antagonist), K-8794 (inverse agonist), IRL2500 (peptide inverse agonist), IRL1620 (partial agonist) — all previously structurally characterized

## Related GPCRs

- [[a2a-adenosine-receptor]] — GPCR with [[bril]] fusion and thermostabilization
- [[angiotensin-ii-type-1-receptor]] — GPCR with SFX/XFEL and LCP crystallization
- [[5ht2b-receptor]] — Serotonin GPCR with BRIL fusion and LCP
- [[kappa-opioid-receptor]] — Opioid GPCR with [[nanobody]] stabilization
- [[p2y12-receptor]] — GPCR with BRIL fusion and LCP crystallization

## References

- Izume et al. (2020) Biochem. Biophys. Res. Commun. — ETB-S6b structure (this paper)
- Shihoya et al. (2018) Nat. Commun. 9:4711 — ETB-ET-3 structure
- Shihoya et al. (2017) Nat. Struct. Mol. Biol. 24:758–764 — ETB-bosentan structure
- Nagiri et al. (2019) Commun. Biol. 2:236 — ETB-IRL2500 structure
- Okuta et al. (2016) J. Mol. Biol. 428:2265–2274 — ETB thermostabilization

## Cross-References

- [[sarafotoxin-s6b]] — Sarafotoxin S6b peptide ligand
- [[sf9-cells]] — Baculovirus expression system
- [[t4-lysozyme]] — T4 lysozyme fusion partner (T4L)
- [[baculovirus-expression]] — Baculovirus expression system