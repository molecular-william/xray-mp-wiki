---
title: CaVAb Bacterial Voltage-Gated Calcium Channel
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12775, doi/10.1038##nature19102]
verified: false
---

# CaVAb Bacterial Voltage-Gated Calcium Channel

## Overview

CaVAb is a bacterial voltage-gated calcium channel that serves as an evolutionary link between prokaryotic sodium channels and eukaryotic voltage-gated calcium channels. CaVAb shares structural homology with [NavAb](/xray-mp-wiki/proteins/navab) but has evolved distinct selectivity filter chemistry that confers calcium permeability. The selectivity filter sequence FQVMTLDDWSDG differs from NavAb's TLESW motif through key substitutions that create a high-affinity calcium binding site. This paper reports the first structural analysis of a bacterial calcium channel, revealing how selectivity filter architecture determines ion selectivity between sodium and calcium. Subsequent studies have determined high-resolution structures of CaVAb in complex with multiple classes of Ca2+ antagonist drugs, revealing distinct binding sites and mechanisms for dihydropyridines and phenylalkylamines.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature12775 | N/A | 3.3 A | C 1 21 | CaVAb 175TLDDWSD181 variant; homotetramer; selectivity filter sequence FQVMTLDDWSDG with key substitutions E177 (vs T in [NavAb](/xray-mp-wiki/proteins/navab)), D178 (vs L), D181 (vs W); crystallized with 100 mM Cd2+ and 100 mM Mn2+ soaking | Cd2+ (100 mM soaking), Mn2+ (100 mM soaking) |
| doi/10.1038##nature12775 | N/A | 3.3 A | C 1 21 | CaVAb 175TLDDWSD181 variant; homotetramer; crystallized with 15 mM Ca2+ soaking | Ca2+ (15 mM soaking) |
| doi/10.1038##nature19102 | N/A | 2.7 A | P212121 | CaVAb with 5 mM Ca2+; wild-type channel without drug | Ca2+ (5 mM) |
| doi/10.1038##nature19102 | N/A | 3.2 A | P212121 | CaVAb (W195Y) with [Amlodipine](/xray-mp-wiki/reagents/ligands/amlodipine) and 5 mM Ca2+; W195Y mutation substituted the Y residue from mammalian CaV1.1 for W195 in CaVAb for better drug resolution | [Amlodipine](/xray-mp-wiki/reagents/ligands/amlodipine) |
| doi/10.1038##nature19102 | N/A | 3.2 A | P212121 | CaVAb (W195Y) with [Nimodipine](/xray-mp-wiki/reagents/ligands/nimodipine) and 5 mM Ca2+ | [Nimodipine](/xray-mp-wiki/reagents/ligands/nimodipine) |
| doi/10.1038##nature19102 | N/A | 3.3 A | P212121 | CaVAb (W195Y) with [UK-59811](/xray-mp-wiki/reagents/ligands/uk-59811) and 5 mM Ca2+ | [UK-59811](/xray-mp-wiki/reagents/ligands/uk-59811) |
| doi/10.1038##nature19102 | N/A | 3.3 A | P212121 | CaVAb with [Br-Verapamil](/xray-mp-wiki/reagents/ligands/br-verapamil) and 5 mM Ca2+ | [Br-Verapamil](/xray-mp-wiki/reagents/ligands/br-verapamil) |

## Expression and Purification

- **Expression system**: [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression) expression in Trichoplusia ni (High5) insect cells
- **Construct**: pFastBac-[FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag)-CaVAb; multiple variants including I199S, W195Y, T206S, E177D S178D M181N, E177D S178D M181N W195Y; all on N49K mutation background

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell harvest | [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression) infection of T. ni insect cells; harvested 72 h post-infection | — |  |  |
| Solubilization | Cell lysis in buffer A (50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl), pH 7.4) | — |  |  |
| Purification | Not specified in detail | — |  |  |
| Crystallization | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) | — |  |  |


## Crystallization

### doi/10.1038##nature12775

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | Not specified in supplementary information |
| Reservoir | Not specified in supplementary information |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Crystals in space group C 1 21. Ca2+ binding sites identified at the selectivity filter through anomalous difference Fourier maps. Multiple soaking conditions tested: 0.5, 2.5, 5, 10, and 15 mM Ca2+. Cd2+ and Mn2+ soaking at 100 mM also performed. |

### doi/10.1038##nature19102

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | CaVAb with 5 mM Ca2+ |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Wild-type CaVAb crystals without drug in P212121 space group at 2.7 A resolution; serves as baseline for drug-bound structures |

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | CaVAb (W195Y) with [Amlodipine](/xray-mp-wiki/reagents/ligands/amlodipine) |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | [Amlodipine](/xray-mp-wiki/reagents/ligands/amlodipine)-bound structure in P212121 at 3.2 A resolution; W195Y mutation enables better resolution of drug binding site |

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | CaVAb (W195Y) with [Nimodipine](/xray-mp-wiki/reagents/ligands/nimodipine) |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | [Nimodipine](/xray-mp-wiki/reagents/ligands/nimodipine)-bound structure in P212121 at 3.2 A resolution |

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | CaVAb (W195Y) with [UK-59811](/xray-mp-wiki/reagents/ligands/uk-59811) |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | [UK-59811](/xray-mp-wiki/reagents/ligands/uk-59811)-bound structure in P212121 at 3.3 A resolution; anomalous scattering of Br confirms binding location |

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | CaVAb with [Br-Verapamil](/xray-mp-wiki/reagents/ligands/br-verapamil) |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | [Br-Verapamil](/xray-mp-wiki/reagents/ligands/br-verapamil)-bound structure in P212121 at 3.3 A resolution; anomalous scattering of Br defines exact binding location in central cavity |


## Biological / Functional Insights

### Calcium selectivity filter architecture

The CaVAb selectivity filter has the sequence FQVMTLDDWSDG, which differs from [NavAb](/xray-mp-wiki/proteins/navab) (FQVMTLESWSMG) at positions 177 (E vs L), 178 (D vs E), 180 (D vs S), and 181 (D vs G). The introduction of two adjacent negatively charged residues (E177 and D178) at the high-field-strength site creates a calcium-coordinating environment. This is consistent with the EEEE motif found in eukaryotic voltage-gated calcium channels, where four glutamate residues from each domain coordinate Ca2+ ions.

### Ca2+ binding sites at the selectivity filter

Anomalous difference Fourier maps reveal three Ca2+ binding sites (Site 1, 2, and 3) at the selectivity filter. Site 1 and Site 2 show clear anomalous density for Ca2+ when crystals are soaked with calcium solutions. The Ca2+ ions are coordinated by oxygen atoms from selectivity filter residues and water molecules. Evidence for hydration shells around bound Ca2+ ions is observed through omit maps, with Ca2+-8H2O complexes modeled at the binding sites.

### Mutagenesis of selectivity filter residues

Systematic mutagenesis of the selectivity filter residues reveals how each position contributes to ion selectivity. The 175TLDDWSN181 mutant (D181N) shows altered permeability with E_rev of +35 mV for Ca2+ and +7.5 mV for Ba2+. The 175TLEDWSD181 mutant (E177D) has E_rev of +30 mV for Ca2+ and +14.5 mV for Ba2+. The 175TLEDWSM181 mutant (E177D, D181M) shows E_rev of +20 mV for Ca2+ and -6.38 mV for Ba2+. The 175TLDDWSM181 mutant (D181M) fails to produce ionic current in Ca2+/Ba2+ solutions but shows large Na+ currents when [EGTA (Ethylene Glycol Tetraacetic Acid)](/xray-mp-wiki/reagents/additives/egta) is added. The 175TLDSWSM181 mutant (D178S, D181M) also shows altered permeation properties.

### Structural comparison with NavAb

The CaVAb selectivity filter structure can be compared to [NavAb](/xray-mp-wiki/proteins/navab) to understand the molecular basis of calcium versus sodium selectivity. The key differences are at positions 177, 178, and 181 where CaVAb has negatively charged residues (E, D, D) compared to NavAb (L, E, G). These substitutions create a calcium-binding pocket while maintaining the overall selectivity filter fold. The distance between the carboxyl oxygen of E177 and the main chain nitrogen of S180/D181 is approximately 2.9 A and 3.3 A respectively.

### Allosteric mechanism of dihydropyridine binding

Dihydropyridines ([Amlodipine](/xray-mp-wiki/reagents/ligands/amlodipine), nimodipine, UK-59811) bind at the external, lipid-facing surface of the pore module at the interface between two subunits. Their binding site is exposed to the extracellular side of the membrane but not to the intracellular side. Binding displaces an endogenous lipid molecule from the common binding site and allosterically induces an asymmetric conformation of the selectivity filter. In the asymmetric state, partially dehydrated Ca2+ binds to Site 1 off-axis, closer to one or two D178 carboxylate groups at a distance of 2.8-3.3 A, suggesting direct interaction of bound Ca2+ with the carboxylate side chain and blocking the pore. Drug-free Ca2+ binds near the central axis in a fully hydrated state, coordinated symmetrically by four D178 carboxylate side chains.

### Pore-blocking mechanism of phenylalkylamine binding

Phenylalkylamines (verapamil, [Br-Verapamil](/xray-mp-wiki/reagents/ligands/br-verapamil)) bind in the central cavity of the pore on the intracellular side of the ion selectivity filter, physically blocking the ion-conducting pathway. Br-verapamil is stretched between two subunits, consistent with drug binding at the interface of domains III and IV in mammalian CaV1.2 channels. Binding is state-dependent: the IC50 for resting state block is 24 uM, 30-fold higher than after depolarizing stimuli (810 nM), revealing that access is greatly enhanced by opening the intracellular activation gate. Drug binding disrupts the fourfold symmetry of the pore, similar to dihydropyridine binding.


## Cross-References

- [NavAb Bacterial Voltage-Gated Sodium Channel](/xray-mp-wiki/proteins/voltage-gated-channels/navab/) — Related bacterial voltage-gated channel with similar fold and selectivity filter architecture
- [Ion Channel Selectivity Filter](/xray-mp-wiki/concepts/selectivity-filter/) — Paper provides detailed structural analysis of CaVAb selectivity filter
- [Intramembrane Ion Coordination](/xray-mp-wiki/concepts/intramembrane-ion-coordination/) — Paper reveals Ca2+ coordination geometry at selectivity filter sites
- [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) — Crystallization method used for structure determination
- [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression) — Expression system used for protein production
- [Amlodipine](/xray-mp-wiki/reagents/ligands/amlodipine) — Ligand or small molecule used in this study
- [Egta](/xray-mp-wiki/reagents/additives/egta) — Additive used in purification or crystallization buffers
- [Br Verapamil](/xray-mp-wiki/reagents/ligands/br-verapamil) — Ligand or small molecule used in this study
- [Uk 59811](/xray-mp-wiki/reagents/ligands/uk-59811) — Ligand or small molecule used in this study
- [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris-hcl) — Buffer component in purification and crystallization
