---
title: GlpG (Escherichia coli Rhomboid Protease)
created: 2026-06-16
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##nature05255, doi/10.1073##pnas.0609773104, doi/10.1073##pnas.0611080104, doi/10.1016##j.jmb.2011.01.029, doi/10.1038##nsmb1179, doi/10.1038##s41594-019-0296-9]
verified: false
---

# GlpG (Escherichia coli Rhomboid Protease)

## Overview

GlpG is an Escherichia coli rhomboid intramembrane serine protease. It consists of a core of six transmembrane helices with the catalytic dyad (Ser201/His254) residing in a water-filled cavity. The first crystal structures of any intramembrane protease were solved concurrently by three independent groups in 2006-2007: Wang et al. (Nature 2006) at 2.1 A resolution, Ben-Shem et al. (PNAS 2007) at 2.3 A resolution using SIRAS phasing with ethylmercury chloride, and Wu et al. (NSMB 2006) at 2.6 A resolution. These structures revealed the rhomboid core architecture with six transmembrane segments, a V-shaped lateral opening for substrate access gated by loop L1, and a water-filled hydrophilic active site embedded within the membrane bilayer. A key feature of the PNAS 2007 structure is TM4, which starts deep within the membrane at the catalytic serine residue, placing the active site in an externally exposed cavity that provides a hydrophilic environment for proteolysis. Subsequent structures were determined in a lipid environment (PDB 2XTV) at 1.7 A resolution using bicelle crystallization, revealing ordered lipid molecules forming an annulus around the protein, and in a delipidated detergent environment (PDB 2XTU) at 1.85 A resolution. Wang and Ha (PNAS 2007) described an open-cap conformation using PDB 2IC8 as starting model (2.5 A resolution, space group R32) where the capping loop L5 is lifted, exposing the catalytic Ser-201 to aqueous solution, with a water molecule occupying the putative oxyanion hole (His-150/Asn-154). This structure revealed the L5 cap as a dynamic gate regulating active-site access and proposed si-face cleavage by rhomboid proteases. Cho et al. (2019) reported ten time-resolved crystallographic snapshots of GlpG catalysis from gate opening to peptide release, capturing apoenzyme, aldehyde inhibitor complex, scission complex, tetrahedral intermediate, acyl intermediate, hydrolytic complex, and catalytic resolution states. These snapshots revealed the complete catalytic cycle of rhomboid intramembrane proteolysis at atomic resolution, including L5 loop dynamics, water recruitment, and the role of conserved active-site residues.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature05255 |  | 2.1 |  | Core domain of GlpG (E. coli rhomboid protease) |  |
| doi/10.1073##pnas.0609773104 |  | 2.3 | P2(1) | Trypsin-treated rhomboid core (residues 93-276) of E. coli GlpG with C-terminal His6 tag |  |
| doi/10.1073##pnas.0611080104 |  | 2.5 | R32 | Core domain of GlpG (E. coli rhomboid protease), residues 87-276 | DCI (3,4-dichloroisocoumarin, serine protease inhibitor, 2.5 mM soak) |
| doi/10.1038##nsmb1179 | 2NRF | 2.6 | P2(1) | Transmembrane core domain (residues 87-276) of GlpG from E. coli, with N-terminal His6 tag removed by thrombin |  |
| doi/10.1016##j.jmb.2011.01.029 | 2XTV | 1.7 | P2(1)2(1)2(1) | N-terminally truncated GlpG S201T active-site mutant from E. coli, with C-terminal His-tag | None (S201T inactive mutant) |
| doi/10.1016##j.jmb.2011.01.029 | 2XTU | 1.85 | R32 | N-terminally truncated GlpG S201T active-site mutant from E. coli, with C-terminal His-tag | None (S201T inactive mutant) |
| doi/10.1038##s41594-019-0296-9 | 6UL0 |  |  | E. coli GlpG in bicelle membrane (apoenzyme) |  |
| doi/10.1038##s41594-019-0296-9 | 6UL1 |  |  | E. coli GlpG in bicelle membrane soaked with Ac-VRMA-CHO | Ac-VRMA-CHO (aldehyde inhibitor) |
| doi/10.1038##s41594-019-0296-9 | 6UL2 |  |  | E. coli GlpG in bicelle membrane soaked with Ac-VRMA-CHO | Ac-VRMA-CHO (aldehyde inhibitor) |
| doi/10.1038##s41594-019-0296-9 | 6UL3 |  |  | E. coli GlpG in bicelle membrane soaked with Ac-VRMA-CHO | Ac-VRMA-CHO (aldehyde inhibitor) |
| doi/10.1038##s41594-019-0296-9 | 6UL4 |  |  | E. coli GlpG in bicelle membrane soaked with Ac-VRMA-CHO | Ac-VRMA-CHO (aldehyde inhibitor) |
| doi/10.1038##s41594-019-0296-9 | 6UL5 |  |  | E. coli GlpG in bicelle membrane soaked with Ac-VRMA-CHO | Ac-VRMA-CHO (aldehyde inhibitor) |
| doi/10.1038##s41594-019-0296-9 | 6UL6 |  |  | E. coli GlpG in bicelle membrane soaked with Ac-VRMA-CHO | Ac-VRMA-CHO (aldehyde inhibitor) |
| doi/10.1038##s41594-019-0296-9 | 6UL7 |  |  | E. coli GlpG in bicelle membrane soaked with Ac-VRMA-CHO | Ac-VRMA-CHO (aldehyde inhibitor) |

## Expression and Purification

- **Expression system**: Escherichia coli C43 (DE3)
- **Construct**: Full-length GlpG in pET15b vector with N-terminal His6 tag; transmembrane core domain (residues 87-276) generated by limited proteolysis during purification

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Protein expression and membrane preparation | Expression in E. coli C43 (DE3), French press lysis, ultracentrifugation at 150,000g for 1h to isolate membranes |  | 25 mM Tris (pH 8.0), 500 mM NaCl | Membrane fraction solubilized with 2% (w/v) n-nonyl-beta-D-glucoside |
| Affinity chromatography | Nickel-nitrilotriacetic acid (Ni-NTA) affinity chromatography | Ni-NTA (Qiagen) | 25 mM Tris (pH 8.0), 150 mM NaCl, 250 mM imidazole, 0.4% (w/v) NG | N-terminal His6 tag removed by thrombin |
| Size-exclusion chromatography | Superdex-200 gel filtration | Superdex-200 (GE Healthcare) | 10 mM Tris (pH 8.0), 150 mM NaCl, 0.4% (w/v) NG | Peak fraction collected at ~20 mg/ml for crystallization |


## Crystallization

### doi/10.1038##nature05255

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | GlpG core domain at 5 mg/mL in 10 mM Tris-HCl pH 7.6, 20 mM nonylglucoside |
| Reservoir | 3 M NaCl, 100 mM Bis-Tris propane pH 7.0 |
| Temperature | Room temperature |
| Growth time | ~1 month (selenomethionine crystals) |
| Notes | Cryo-protection by stepwise transfer to mother liquor with 25% glycerol. Native and selenomethionine crystals grown. SeMet crystals required 2 mM DTT and 0.1 mM EDTA. Data collected at BNL-NSLS beamlines X6A, X26C, X29. |

### doi/10.1073##pnas.0609773104

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Trypsin-treated GlpG core (residues 93-276) at 5 mg/ml in 20 mM Hepes pH 7.5, 90 mM NaCl, 10% glycerol, lauryl dimethylamine oxide (LDAO) |
| Reservoir | 30% PEG 400, 200 mM CaCl2, 100 mM MES pH 6.5 |
| Temperature | 4 C |
| Growth time | Not specified |
| Notes | Trypsin removed N-terminal cytoplasmic region. Expressed in E. coli C43(DE3) with mipA deletion. Purified by Ni-NTA, trypsinized overnight at 4 C, trypsin removed by para-aminobenzamidine and Sephadex G-50 columns. Dialyzed and concentrated to 5 mg/ml. SIRAS phasing from ethylmercury chloride derivative. Native data collected at 120 K on a Rigaku RU-H3R generator (home source). Derivative data collected at ESRF beamline ID29-1. Processed with Denzo/Scalepack. SOLVE for heavy atom positions, RESOLVE for density modification and auto-building. Refined in CNS. Verified with MolProbity and PROCHECK. |

### doi/10.1073##pnas.0611080104

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion with inhibitor soaking |
| Protein sample | GlpG core domain (residues 87-276) at ~20 mg/ml in 10 mM Tris (pH 8.0), 150 mM NaCl, 0.4% (w/v) n-nonyl-beta-D-glucoside |
| Reservoir | 3 M NaCl, 100 mM Bis-Tris propane pH 7.0 (from 2IC8 protocol) |
| Temperature | Room temperature |
| Growth time | Crystals grown as described in Wang 2006; soaked 5 days with DCI/DMSO |
| Notes | Crystals grown from the original 2IC8 protocol. Stepwise cryoprotection to 25% glycerol, 0.6% NG, 3.0 M NaCl, 100 mM Bis-Tris propane pH 7.0. Inhibitor soaking: 2.5 mM DCI (3,4-dichloroisocoumarin) in 2% DMSO, 5 days at room temperature before flash freezing. The open-cap conformation was observed in DCI-soaked crystals (Phe-245 and L5 loop 245-249 disordered). Control crystals treated identically without DCI showed the closed conformation. Data collected at NSLS beamline X25. |

### doi/10.1038##nsmb1179

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | GlpG core domain (residues 87-276) at ~20 mg/ml in 10 mM Tris (pH 8.0), 150 mM NaCl, 0.4% (w/v) n-nonyl-beta-D-glucoside |
| Reservoir | Not specified (physiological pH 7.4 and normal ionic strength) |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Native data set collected and heavy-atom derivatives prepared. Molecular replacement phasing. Data collected at BNL-NSLS. Two molecules per asymmetric unit. |

### doi/10.1016##j.jmb.2011.01.029

| Parameter | Value |
|---|---|
| Method | Bicelle crystallization |
| Protein sample | Truncated GlpG S201T at 9 mg/ml in nonyl glucoside, mixed with 2% DMPC/CHAPSO bicelles (2.6:1 ratio) |
| Reservoir | 1.5 M NaCl, 0.1 M Bis-Tris (pH 7) |
| Temperature | 298 K (25 C) |
| Growth time | 20-30 days |
| Notes | Crystals appeared after one week, grew to max 0.3 x 0.08 x 0.05 mm. Type I membrane protein crystals with alternating up-down orientation of molecules. |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop) |
| Protein sample | Completely delipidated truncated GlpG S201T at ~8 mg/ml in nonyl glucoside |
| Reservoir | 2.5-3.0 M ammonium chloride |
| Temperature | 298 K (25 C) |
| Notes | Detergent environment; trigonal crystal form (R32). |

### doi/10.1038##s41594-019-0296-9

| Parameter | Value |
|---|---|
| Method | Bicelle crystallization with time-resolved soaking |
| Protein sample | E. coli GlpG in DMPC/CHAPSO bicelle membrane |
| Notes | Crystals of GlpG in bicelle membrane were soaked with Ac-VRMA-CHO peptide aldehyde for increasing lengths of time prior to freezing and X-ray diffraction analysis. This time-resolved approach captured 10 catalytic snapshots from gate opening to peptide release. |


## Biological / Functional Insights

### First structure of an intramembrane protease - rhomboid core architecture

The 2.1 A structure of E. coli GlpG is the first atomic-resolution structure of any intramembrane protease. The core domain contains six transmembrane segments (S1-S6) arranged in a helical bundle. The structure establishes that peptide bond scission occurs within the hydrophobic environment of the membrane bilayer.

### Membrane-embedded Ser-His catalytic dyad active site

The catalytic dyad (Ser201/His254) is positioned at the protein interior at a depth below the membrane surface. The two residues interact via a strong hydrogen bond. The lone base (His254) is sufficient to activate the serine for direct nucleophilic attack, similar to other serine hydrolases. A water molecule mediates hydrogen bonding between His254 and Asn251, and His254 stacks onto Tyr205 via pi-pi interaction.

### TM4 starts deep within the membrane at the catalytic serine

The Ben-Shem et al. (PNAS 2007) structure revealed that TM4 starts deep within the membrane at the catalytic serine residue Ser201. This means the active site residues are not at the end of a TM helix but are embedded within the helix itself. This arrangement places Ser201 in an externally exposed cavity that opens toward the periplasm, providing the hydrophilic environment necessary for peptide bond hydrolysis within the membrane.

### Hydrophilic active-site cavity exposed to the periplasm enables water access

The PNAS 2007 structure showed that the active site cavity is sealed from the bilayer on three sides (TM2, TM3/TM5/TM6, and loop 3/H2) but has a lateral entrance between TM2 and TM5 that opens toward the lipid. A phospholipid was found bound between TM2 and TM5 with its phosphate group near the catalytic His254. The cavity is filled with polar residues that can stabilize the nonhelical conformation of the substrate scissile bond. The hydrophilic environment allows water-dependent catalysis at the depth of the hydrophobic milieu.

### V-shaped lateral opening for substrate access

A large V-shaped opening between S1 and S3 faces laterally towards the lipid. This opening is wide enough to accommodate an alpha-helix and is the likely route for substrate entry into the active site. The lower portion is shallow and hydrophobic for favorable interactions with hydrophobic substrates, while the upper portion connects to the hydrophilic cavity.

### L1 lateral gate controls substrate access

The membrane-embedded loop L1 blocks the V-shaped lateral opening of the active site. L1 has an amphiphilic characteristic: its upper surface is polar while its lower surface is hydrophobic. The WR motif (Trp136/Arg137) at the membrane-water interface modulates gate dynamics. L1 contains a stretch of four consecutive 3_10 helices, an unusual feature suggesting a metastable, dynamic structure consistent with gating function.

### Water molecules in the membrane-embedded active site

The active site of GlpG contains a number of water molecules widely distributed throughout the cavity. The wide distribution combined with the extensiveness of the protein surface they interact with suggests that reactant water may enter the membrane-embedded active site by different routes from the outside aqueous solution, rather than through a single path or channel.

### Lipid annulus around GlpG and asymmetric bilayer

The 1.7 A structure of GlpG in bicelles reveals 14 ordered lipid molecules forming an annulus around the protein. Most lipids cluster around TM1, L1, and TM3. The bilayer is asymmetric with well-ordered lipids found only on the cytoplasmic side. The hydrophobic belt of GlpG is ~23 A wide, and the average bilayer thickness is ~25 A, close to the lamellar phase of DMPC bilayers.

### Ten catalytic snapshots of rhomboid intramembrane proteolysis

Cho et al. (2019) captured ten time-resolved crystallographic snapshots of GlpG catalysis using aldehyde inhibitor soaking in bicelle crystals. The snapshots span the complete catalytic cycle: apoenzyme (6UL0), initial inhibitor interaction (Snapshot-I1, 6UL1), scission complex (Snapshot-S1, 6UL2), early tetrahedral intermediate (Snapshot-S2, 6UL3), late tetrahedral intermediate (Snapshot-S3, 6UL4), acyl intermediate (Snapshot-S4, 6UL5), hydrolytic complex (Snapshot-S5, 6UL6), and catalytic resolution (Snapshot-S6, 6UL7). These structures reveal the stepwise mechanism of gate opening, substrate binding, peptide bond cleavage, water entry, and product release.

### L5 cap as a dynamic gate for active-site access

Wang and Ha (PNAS 2007) discovered that the capping loop L5 can adopt an open conformation where it is lifted away from the active site, exposing the catalytic Ser-201 to aqueous solution. In the closed structure (2IC8), L5 tightly caps the Ser-His dyad from above, preventing substrate binding. In the open-cap conformation (DCI-soaked crystals, space group R32 at 2.5 A resolution), residues 245-249 of L5 become disordered, lifting the cap. This movement also destabilizes Phe-245 (previously buried between TM helices S2 and S5), creating a side portal from the lipid bilayer to the protease active site.

### Putative oxyanion hole defined by His-150 and Asn-154

With the capping loop L5 removed in the open-cap conformation, a water molecule moved ~1.3 A to a new location hydrogen-bonded to Ser-201, His-150, and Asn-154. This corresponds to the oxyanion hole position in classic serine proteases. The backbone amide of Gly-199 (of the conserved GXSG motif) points away from the Ser-His dyad, so Asn-154 and flexible His-150 compensate for the loss. Both His-150 and Asn-154 are highly conserved in the rhomboid family.

### Si-face cleavage prediction and substrate entry model

Based on the open-cap conformation and the putative oxyanion hole geometry, Wang and Ha (PNAS 2007) proposed that rhomboid proteases cleave substrates from the si-face of the scissile peptide bond, similar to E. coli signal peptidase but different from most serine proteases (which attack the re-face). The model predicts that the transmembrane substrate enters the protease active site through the gap between TM helices S2 and S5, with only the top portion of the substrate membrane-spanning sequence bending into the protease.

### L5 loop dynamics during the catalytic cycle

The time-resolved snapshots reveal that the L5 loop undergoes conformational changes throughout catalysis. In the apoenzyme, L5 is in a closed conformation. Upon inhibitor/substrate binding, L5 moves to accommodate the substrate. During the tetrahedral intermediate and acyl intermediate states, L5 adopts specific conformations that stabilize the reaction intermediates. The L5 loop acts as a dynamic cap that controls access to the active site and stabilizes reaction intermediates.

### Role of conserved active-site residues in catalysis

The catalytic snapshots reveal the specific roles of conserved residues during each step of the reaction. His254 acts as a general base, activating Ser201 for nucleophilic attack. The oxyanion hole (formed by main-chain amides of residues in the active site) stabilizes the tetrahedral intermediate. Conserved water molecules participate in proton transfer and are recruited during the hydrolytic step.

### Transmembrane substrate binding and cleavage

Time-resolved experiments with a peptide substrate (Ac-RKVRMAAIVFSFP-amide) revealed how a full transmembrane substrate binds and is cleaved. The substrate adopts an abrupt bend at the scissile bond, allowing access to the membrane-embedded active site. This bending is facilitated by glycine and proline residues near the cleavage site, and the structure rationalizes the sequence specificity of rhomboid proteases.


## Cross-References
