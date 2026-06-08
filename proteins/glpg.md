---
title: GlpG Rhomboid Intramembrane Protease
created: 2026-05-26
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2007.10.014, doi/10.1021##bi300368b, doi/10.1016##j.molcel.2015.12.022, doi/10.1038##emboj.2010.243, doi/10.1038##nsmb1179]
verified: false
---

# GlpG Rhomboid Intramembrane Protease

## Overview

GlpG is the archetypal rhomboid intramembrane protease from Escherichia coli, belonging to the Ser/His catalytic class of intramembrane proteases that cleave transmembrane substrates within the lipid bilayer. High-resolution crystal structures have been solved in both detergent and membrane-mimetic bicelle environments, revealing structural changes upon substrate binding and a two-stage catalytic mechanism involving interrogation and scission complexes. The active enzyme adopts an open conformation in the membrane environment, with lateral movement of TM5 away from TM2. The inhibitor-bound structure reveals the position of the oxyanion hole, the S1 and S2 binding subsites, and subtle conformational changes sufficient for catalysis.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.jmb.2007.10.014 | 3B45 | 1.9 A | P212121 | Wild-type E. coli GlpG (residues 1-245, full-length transmembrane construct) | DDM detergent molecules (169 detergent atoms observed in the structure) |
| doi/10.1016##j.jmb.2007.10.014 | 3B44 | 1.7 A | P212121 | GlpG W136A mutant (Trp136 replaced with alanine at the distal tip of the L1 loop) | DDM detergent molecules (175 detergent atoms observed in the structure) |
| doi/10.1016##j.molcel.2015.12.022 | 5F5B | 2.00 A | R32 | DeltaN-GlpG Y205F (residues 87-276, catalytically inactive Y205F mutant) | VRMA peptide aldehyde (Gurken tetrapeptide aldehyde, Ac-VRMA-CHO) |
| doi/10.1016##j.molcel.2015.12.022 | 5F5D | 2.20 A | C2221 | DeltaN-GlpG Y205F (residues 87-276, crystallized in DMPC/CHAPSO bicelles) | -- |
| doi/10.1016##j.molcel.2015.12.022 | 5F5G | 2.20 A | C2221 | DeltaN-GlpG Y205F (residues 87-276, soaked with tripeptide aldehyde) | RMA peptide aldehyde (Ac-RMA-CHO) |
| doi/10.1016##j.molcel.2015.12.022 | 5F5J | 2.30 A | C2221 | DeltaN-GlpG Y205F (residues 87-276, soaked with tetrapeptide aldehyde) | VRMA peptide aldehyde (Ac-VRMA-CHO) |
| doi/10.1016##j.molcel.2015.12.022 | 5F5K | 2.30 A | C2221 | DeltaN-GlpG Y205F (residues 87-276, soaked with hexapeptide aldehyde) | RKVRMA peptide aldehyde (Ac-RKVRMA-CHO) |
| doi/10.1038##emboj.2010.243 | 2XOW | 2.09 A | R32 | Wild-type E. coli GlpG (residues 92-270) covalently bound to amino-methoxy-isocoumarin inhibitor | Amino-methoxy-isocoumarin (7-amino-4-chloro-3-methoxy isocoumarin, JLK-6) |
| doi/10.1038##emboj.2010.243 | 2XOV | 1.65 A | R32 | Wild-type E. coli GlpG (residues 92-270), native enzyme without inhibitor | -- |
| doi/10.1038##nsmb1179 | 2NRF | 2.6 A | P212121 | Transmembrane core domain of E. coli GlpG (residues 91-272 for molecule A, residues 91-241 and 251-272 for molecule B), two molecules per asymmetric unit | None (no ligand bound; shows open and half-open conformations of helix alpha5) |

## Expression and Purification

- **Expression system**: E. coli
- **Construct**: DeltaN-GlpG (residues 87-276) with His6-Myc tag expressed under identical conditions across all structural studies

### Purification Workflow

*Source: doi/10.1016##j.molcel.2015.12.022*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Expression | -- | -- + -- | DeltaN-GlpG Y205F expressed in E. coli under identical conditions for all structural studies |
| Purification | Affinity chromatography | -- | -- + -- | Purified as previously described (Dickey et al. 2013 Cell 155:1270-1281) |

### Purification Workflow

*Source: doi/10.1038##emboj.2010.243*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Expression in E. coli | -- | -- + DDM | Full-length GlpG expressed in E. coli and solubilized in DDM detergent |
| Purification | Affinity chromatography | -- | -- + DDM | Purified as previously described (Lemberg et al. 2005, Stevenson et al. 2007) |


## Crystallization

### doi/10.1038##nsmb1179

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | Transmembrane core domain of E. coli GlpG (residues 87-276) |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Crystals diffracted to 2.6 A resolution, space group P212121. Two molecules per asymmetric unit with different alpha5 conformations (open and half-open). Molecular replacement used for structure determination. |

### doi/10.1016##j.jmb.2007.10.014

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop or sitting drop) |
| Protein sample | Wild-type GlpG and W136A mutant, purified in detergent |
| Reservoir | Crystallization conditions similar to those used for the original GlpG structure (Wang et al. 2006, Nature 444:179-183) |
| Temperature | Not explicitly stated in this paper |
| Growth time | Not explicitly stated |
| Cryoprotection | Not explicitly stated |
| Notes | Wild-type GlpG was crystallized from similar conditions as the W136A mutant for accurate structural comparison. Both structures solved by molecular replacement using the original 2006 structure (PDB 2R3R) as search model. Space group P212121. |

### doi/10.1016##j.molcel.2015.12.022

| Parameter | Value |
|---|---|
| Method | Bicelle crystallization |
| Protein sample | DeltaN-GlpG Y205F (residues 87-276) in DMPC/CHAPSO bicelles (2.8:1 ratio) |
| Reservoir | 0.1 M NaOAc (pH 5.5), 3 M NaCl, 5% ethylene glycol |
| Temperature | Room temperature |
| Notes | Active rhomboid protease crystallized in a membrane-mimetic bicelle environment. Crystals of gate-closed form obtained in 0.1 M Tris (pH 8.5), 3 M NaNO3, 15% glycerol. Peptide aldehydes soaked into crystals for 7-24 hr at room temperature. |

| Parameter | Value |
|---|---|
| Method | Bicelle crystallization with peptide aldehyde soaking |
| Protein sample | DeltaN-GlpG Y205F in DMPC/CHAPSO bicelles (2.8:1) |
| Reservoir | 0.1 M NaOAc (pH 5.5), 3 M NaCl, 5% ethylene glycol |
| Cryoprotection | Cryoprotected in reservoir buffer with peptide aldehyde |
| Notes | Crystals soaked with 2.5 mM peptide aldehydes (RMA-CHO, VRMA-CHO, RKVRMA-CHO) in reservoir buffer for 7-24 hr at room temperature, then flash-frozen in nitrogen stream. Space group C2221 for all substrate complex structures. |

### doi/10.1038##emboj.2010.243

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Protein sample | Truncated GlpG WT (residues 92-270) in DDM |
| Reservoir | 2.5-3 M ammonium chloride |
| Mixing ratio | 1:1 protein to reservoir |
| Temperature | 25 C |
| Growth time | Not explicitly stated |
| Cryoprotection | 25% glycerol added to mother liquor, flash-frozen in liquid nitrogen |
| Notes | Native enzyme crystals obtained by mixing 2.5-3 M ammonium chloride with protein at 1:1 ratio. Inhibitor-bound crystals obtained by soaking single crystals in 1 mM amino-methoxy-isocoumarin (JLK-6) and 7.5% DMSO in buffer (25 mM Bis-Tris pH 7.0, 2.5 M ammonium chloride) for 20 h at 25 C. Space group R32 for both native and acyl enzyme structures. |


## Biological / Functional Insights

### Alpha5 helix gating mechanism for substrate entry

The 2NRF structure reveals two conformations of GlpG in one asymmetric unit. Molecule A shows an open conformation where helix alpha5 is bent away from the rest of the molecule, producing a large cleft between helices alpha2 and alpha5 large enough to accommodate an extended polypeptide chain. Molecule B shows a half-open conformation similar to the previously published closed form, with the L5 loop flexible and disordered. The alpha5 helix is proposed to be the gating helix for substrate entry into the active site. Helix alpha5 is one of the least conserved helices in the rhomboid family, making it an ideal structural element for providing access to entering substrate without causing the entire molecule to rearrange. The catalytic residue Ser201 is placed at the bottom of a water-filled cavity approximately 10 A below the membrane surface.

### Open conformation in membrane environment

In the bicelle-membrane environment, the GlpG Y205F structure adopts an open conformation where TM5 has shifted up and away from TM2, compared to the gate-closed form observed in detergent-crystallized structures (e.g., PDB 2IC8). This open conformation represents the catalytically active state of rhomboid proteases, where the substrate entry portal is accessible from the lateral membrane surface.

### Non-competitive inhibition reveals two-stage catalysis

Peptide aldehyde inhibitors exhibit non-competitive inhibition of GlpG, meaning Km is unchanged but Vmax decreases dose-dependently. This reveals that substrate does not contact the catalytic center in the initial Michaelis complex, providing direct experimental evidence for a two-stage catalytic mechanism: an interrogation complex (substrate bound laterally without contacting catalytic serine) followed by a scission complex (substrate extended into catalytic site).

### Tetrahedral intermediate structure

Crystal structures with peptide aldehydes covalently attached to catalytic S201 captured the tetrahedral intermediate of rhomboid catalysis. The aldehyde carbon is tetrahedral, mimicking the transition state. The oxyanion is stabilized by a tripartite interaction network: H150 side chain (2.69 A), S201 backbone (2.91 A), and N154 side chain (3.04 A). This resolves prior discrepancies from non-peptidic inhibitor structures.

### Extended substrate-enzyme interactions

Beyond the catalytic center, the substrate makes a network of backbone-backbone interactions with the L3 and L5 loops of GlpG, explaining the broad sequence selectivity of rhomboid proteases. The P1 alanine side chain points into a water-retention cavity (3 bound water molecules). P4 valine forms hydrophobic interactions with F146 and M120 on the L1 loop. The P2 methionine and P3 arginine side chains point upward and out, making unexpected "extra" stabilizing contacts that increase inhibitor potency 10-fold.

### Water-retention site at P1

The P1 substrate residue sits in a surprisingly large cavity that was previously postulated as a water-retention site. Three water molecules are retained in this cavity upon substrate binding, unperturbed by the substrate. The requirement for small residues at P1 may not be purely steric but could result from disruptive effects larger side chains have on the water-retention site, which may aid proteolysis.

### P3 arginine extra interactions

The P3 arginine side chain makes a series of unexpected stabilizing contacts with the L5 loop, including hydrogen bonding directly with the backbone CO of M247 at 3.06 A distance, and potentially with hydroxyl side chains of S193, S248, and/or N251. Mutating P3 arginine to alanine (as in the natural TatA substrate) reduced cleavage ~2-fold and decreased inhibitor potency 10-fold, demonstrating the functional importance of these "extra" interactions.

### Peptide aldehydes inhibit rhomboid in living cells

Ac-VRMA-CHO completely blocked TatA-Flag processing by endogenous GlpG in living E. coli cells without requiring pre-incubation. The IC50 in cells (98 +/- 11 uM) was indistinguishable from the Ki measured in proteoliposomes (113 +/- 4 uM), validating proteoliposomes as an effective mimic of the natural E. coli membrane environment. The hexapeptide aldehyde Ac-RKVRMA-CHO displayed an IC50 of 2.9 +/- 0.3 uM in cells, demonstrating potent inhibition.

### Oxyanion hole structure revealed by isocoumarin inhibitor

The acyl enzyme structure of GlpG covalently bound to amino-methoxy-isocoumarin reveals the position and orientation of the oxyanion hole. The benzoyl carbonyl oxygen of the inhibitor makes a strong hydrogen bond (2.61 A) to the main chain amide of the catalytic S201. Weaker hydrogen bonds are formed by the main chain amide of L200, the side chain amide of N154, and the imidazole nitrogen of H150. This proves that rhomboids act by a mechanism that closely resembles classical serine proteases, despite being phylogenetically unrelated.

### Substrate binding subsites S1 and S2'

The inhibitor-bound structure identifies the S1 subsite as a cavity adjacent to the catalytic dyad, formed by residues from TM3, TM4, TM6, and loop-1 (notably A182, S185, Q189, F197, and A253). The S2' subsite is a hydrophobic cavity fully formed only upon inhibitor binding, located at a distance from the catalytic residues consistent with binding of a P2' residue. Mutations of A253 into larger residues (V, I, L, T) progressively restrict P1 specificity toward smaller residues like glycine.

### Loop-5 conformational change upon inhibitor binding

Comparison of native and acyl enzyme structures reveals that loop-5 (residues 243-250) moves from a capping position over the active site (resting state) to a lifted position upon inhibitor binding. This is accompanied by a displacement of TM5 and TM6 by approximately 1.25 A, with the greatest deviation at the C-terminus of TM5 and N-terminus of TM6 (residues 250-252). The movement of loop-5 is consistent with it functioning as a flexible gate that occludes the catalytic center in the resting state.

### Subtle structural change sufficient for catalysis

The inhibitor-bound structure suggests that subtle structural changes are sufficient for catalysis, as opposed to large conformational changes previously proposed from comparisons of unliganded GlpG structures. The average displacement of TM5 and TM6 is only 1.25 A, and the overall architecture of multiple reported GlpG structures is similar. This challenges the hypothesis that large TM5 movements (up to 35 degrees tilt) occur during catalysis, suggesting instead that extreme variations in published structures may be artifacts of the detergent environment and crystal contacts.

### Substrate binding model for TatA peptide

A tetrapeptide model of TatA (Thr-Ala-Ala-Phe) was docked into the GlpG active site. In the preferred model, the P1 alanine side chain points into the S1 cavity, while the P2' phenylalanine fits into the hydrophobic S2' cavity, forming contacts with W157, V204, Y205, and W236. The P2 threonine and P1' alanine side chains face the solvent, consistent with the observed lack of specificity at these positions. Loop-5 residues F245, M247, and M249 can form contacts with substrate residues at P2 and P1' positions, suggesting a role in stabilizing the substrate.


## Cross-References

- [Intramembrane Proteolysis](/xray-mp-wiki/concepts/intramembrane-proteolysis/) — GlpG is the archetypal rhomboid intramembrane protease that cleaves substrates within the lipid bilayer
- [Rhomboid Protease Family](/xray-mp-wiki/concepts/rhomboid-protease/) — GlpG belongs to the rhomboid family of Ser/His intramembrane proteases
- [DDM (N-Dodecyl-beta-D-maltopyranoside)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization and purification of GlpG
- [Cytoplasmic Domain of E. coli Rhomboid Protease GlpG (EcoGlpG-Cyto)](/xray-mp-wiki/proteins/ecglpg-cyto/) — Related structural entity representing the soluble cytoplasmic domain of GlpG
- [HiGlpG (Haemophilus influenzae GlpG)](/xray-mp-wiki/proteins/hiGlpG/) — Homologous rhomboid protease from Haemophilus influenzae
- [Isocoumarin](/xray-mp-wiki/reagents/ligands/isocoumarin/) — Isocoumarin inhibitor class that binds to GlpG; amino-methoxy-isocoumarin forms acyl enzyme complex (PDB 2XOW)
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Cryoprotectant (25%) used for flash-freezing GlpG crystals
- [Bis-Tris Buffer](/xray-mp-wiki/reagents/buffers/bis-tris/) — Buffer (25 mM, pH 7.0) used in crystallization soaking solution for inhibitor-bound GlpG
