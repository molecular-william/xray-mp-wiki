---
title: "XylE (Escherichia coli Sugar Transporter)"
created: 2026-06-02
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11524, doi/10.1038##nature13306, doi/10.1038##ncomms5521, doi/10.1038##nsmb.2569]
verified: false
---

# XylE (Escherichia coli Sugar Transporter)

## Overview

XylE is an Escherichia coli homologue of the human [Glucose](/xray-mp-wiki/reagents/additives/glucose) transporters [SLC2A1](/xray-mp-wiki/proteins/glut1)-4. It belongs to the sugar porter (SP) family within the major facilitator superfamily (MFS) of secondary transporters. XylE functions as a proton-coupled xylose (H+/xylose) symporter. XylE has been crystallized in multiple conformations: an outward-facing partly occluded conformation, an inward-facing partly occluded conformation, and a new inward-facing open conformation with a detached cytoplasmic domain. The inward-open structure reveals an asymmetric rocker-switch movement of the N-domain against the C-domain during transport. Key proton-coupling residues include Asp27 (TM1), Arg133, and Glu206 (TM6); sugar-binding residues include Gln168 (TM5) and Trp392 (TM10).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature11524 | 4GBZ | 2.8 | unknown | Full-length wild-type XylE from E. coli O157:H7 | D-xylose |
| doi/10.1038##nature11524 | 4GBX | 2.9 | unknown | Full-length wild-type XylE from E. coli O157:H7 | D-glucose |
| doi/10.1038##nature11524 | 4GBY | 2.6 | unknown | Full-length wild-type XylE from E. coli O157:H7 | 6-bromo-6-deoxy-D-glucose |
| doi/10.1038##ncomms5521 | 4QIQ | 3.5 | P3;21 | Truncated XylE residues 6-480 from E. coli BL21(DE3) genomic DNA | D-glucose (30 mM, crystallization additive) |
| doi/10.1038##nsmb.2569 | 4JA4 | 4.2 | P6_1 | Full-length wild-type XylE from E. coli C41(DE3), N-terminal His6-TEV tag | None (apoprotein) |
| doi/10.1038##nsmb.2569 | 4JA3 | 3.8 | C2 | Full-length wild-type XylE from E. coli C41(DE3), N-terminal His6-TEV tag | None (apoprotein) |

## Expression and Purification

- **Expression system**: E. coli BL21(DE3) and E. coli BL21 C43(DE3)
- **Construct**: Full-length XylE, N-terminal His6-tag (pET15b); Truncated XylE residues 6-480 (pET-15b)
- **Induction**: 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at D600 of 1.5 (full-length); 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at OD600 0.5, shifted to 18C (truncated)
- **Media**: Luria-Bertani medium and Luria-Bertani (LB) medium at 37C, 250 rpm

### Purification Workflow

#### Source: doi/10.1038##nature11524

- **Expression system**: E. coli BL21(DE3)
- **Expression construct**: Full-length XylE with N-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag) (pET15b)
- **Tag info**: [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag), removed by protease

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | — | Luria-Bertani medium | 12 flasks, 300 r.p.m., 4 h at 37 C after [IPTG](/xray-mp-wiki/reagents/additives/iptg) induction |
| Cell harvest and homogenization | French press cell lysis | — | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM NaCl | Two passes at 10,000-15,000 lb/in2 |
| Membrane preparation | Ultracentrifugation | — | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM NaCl | 150,000g for 1 h; membrane fraction harvested |
| Membrane solubilization | Detergent solubilization | -- | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM NaCl + 1.5% (w/v) [DDM](/xray-mp-wiki/reagents/detergents/ddm) | 1 h incubation at 4 C |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA (Qiagen) | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM NaCl, 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole), 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm) + 0.02% [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Wash with 20 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole); elute with 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) |
| Tag removal | Protease cleavage | — |  | Hexahistidine tag removed |
| Size-exclusion chromatography | SEC | [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200) (GE Healthcare) | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM NaCl, various detergents + various |  |

**Final sample**: 10 mg/ml in 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM NaCl

#### Source: doi/10.1038##ncomms5521

- **Expression system**: E. coli BL21 C43(DE3)
- **Expression construct**: Truncated XylE residues 6-480, N-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag) (pET-15b)
- **Tag info**: [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag), removed by thrombin protease overnight at 4C with 2.5 mM CaCl2

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation | — | Luria-Bertani (LB) medium at 37C, 250 rpm | Shifted to 18C at OD600 0.5; induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg); overnight culture |
| Cell harvest and homogenization | Microfluidizer M110-P cell lysis | — | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM NaCl | 20,000 psi |
| Membrane preparation | Ultracentrifugation | — | 25 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 8.0, 150 mM NaCl | 10,000g for 30 min at 4C, then 1 h at 4C |
| Membrane solubilization | Detergent solubilization | -- | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5 + 1% (w/v) DM (decyl-beta-D-maltopyranoside) | 5% w/v DM added, rotated 2 h at 4C; centrifuged 150,000g for 45 min at 4C |
| Affinity chromatography | Ni-NTA affinity chromatography | Ni-NTA (Qiagen) | 25 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) + 0.2% w/v DM | Wash with 25 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) then 50 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole); elute with 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) in 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5, 150 mM NaCl, 0.2% DM |
| Tag removal | Protease cleavage | — |  | His-tag cleaved overnight at 4C using 1 unit human alpha-thrombin per 1 mg XylE with 2.5 mM CaCl2 |
| Size-exclusion chromatography | SEC | Superdex S200 | 10 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris-hcl) pH 7.5, 150 mM NaCl, various detergents + various (screened for optimal detergent) |  |

**Final sample**: 5-6 mg/ml

#### Source: doi/10.1038##nsmb.2569

- **Expression system**: E. coli C41(DE3)
- **Expression construct**: Full-length wild-type XylE from E. coli C41(DE3), N-terminal His6-TEV tag (modified pTH27 vector)
- **Tag info**: [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag) with TEV protease cleavage site, removed by TEV protease

##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture | Fermentation in Terrific broth (TB) medium | — | Terrific broth (TB) | 220 r.p.m., 37 C; overexpression induced by 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at OD600 0.7-1.0; harvested after 16-20 h at 20 C |
| Cell lysis | Emulsiflex microfluidizer at 15,000 p.s.i. chamber pressure | — | 20 mM sodium phosphate (Na-P) pH 7.5, 300 mM NaCl, 0.5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 1 mg/ml lysozyme, 5 U/ml DNaseI, [EDTA](/xray-mp-wiki/reagents/additives/edta)-free Complete Protease Inhibitor Cocktail | Resuspension at 4 C for 45 min; debris removed by centrifugation at 10,000g for 10 min at 4 C |
| Membrane preparation | Ultracentrifugation | — | Same as lysis buffer | 104,000g (Beckman Coulter, Ti45 rotor) at 4 C for 50 min |
| Membrane solubilization | Detergent solubilization | -- | 20 mM Na-P pH 7.5, 300 mM NaCl, 15 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep), Complete Protease Inhibitor Cocktail + 1% decyl-beta-D-maltoside (DM) | 60 min incubation at 4 C; clarified by ultracentrifugation at 104,000g for 30 min at 4 C |
| IMAC purification | Immobilized metal ion affinity chromatography (IMAC) with Ni-NTA beads | Ni-NTA beads | 20 mM Na-P pH 7.5, 300 mM NaCl, 15-30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole), 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep), 0.2% DM + 0.2% DM | Beads incubated with supernatant for 1 h; column washed with 15-30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole) wash buffer |
| Tag removal | TEV protease cleavage | -- | Same as IMAC buffer | 1 mg TEV per ml of IMAC beads, incubated overnight at 4 C; cleavage >95% complete |
| Size-exclusion chromatography | SEC on HiLoad Superdex 200 16/60 GL column | HiLoad Superdex 200 16/60 GL (ÄKTAexplorer 10) | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes), 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep), 0.2% DM + 0.2% DM | Peak fractions collected, concentrated to 8-18 mg/ml |

**Final sample**: 8-18 mg/ml


## Crystallization

### doi/10.1038##nature11524

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | XylE purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm) |
| Notes | Crystallized with 20 mM [D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose); diffraction to 2.8 A |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | XylE purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm) |
| Notes | Crystallized with 40 mM D-[Glucose](/xray-mp-wiki/reagents/additives/glucose); diffraction to 2.9 A |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | XylE purified in [DDM](/xray-mp-wiki/reagents/detergents/ddm) |
| Notes | Crystallized with 40 mM 6-bromo-6-deoxy-D-[Glucose](/xray-mp-wiki/reagents/additives/glucose); Br anomalous signal; diffraction to 2.6 A |

### doi/10.1038##ncomms5521

| Parameter | Value |
|---|---|
| Method | Sitting drop vapor diffusion |
| Protein sample | XylE purified in 1% DM, concentrated to 5-6 mg/ml |
| Temperature | 20C |
| Notes | Inward-facing open conformation with detached cytoplasmic domain; PDB 4QIQ |

### doi/10.1038##nsmb.2569

| Parameter | Value |
|---|---|
| Method | Vapor diffusion crystallization; P6_1 space group; 3-fold averaging for phase improvement |
| Protein sample | Tag-free XylE at 8-18 mg/ml in 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes), 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep), 0.2% DM |
| Reservoir | Not specified in text |
| Notes | Inward open conformation; PDB 4JA4; 4.2 A resolution; data collected at Diamond Light Source beamline I02 (proposal MX5873/MX6603) |

| Parameter | Value |
|---|---|
| Method | Vapor diffusion crystallization; C2 space group; 2-fold averaging for phase improvement |
| Protein sample | Tag-free XylE at 8-18 mg/ml in 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes), 150 mM NaCl, 5% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol), 0.5 mM [TCEP](/xray-mp-wiki/reagents/additives/tcep), 0.2% DM |
| Reservoir | Not specified in text |
| Notes | Partially occluded inward open conformation; PDB 4JA3; 3.8 A resolution; data collected at SOLEIL synchrotron beamline PROXIMA1 (proposal 20110314) |


## Biological / Functional Insights

### Outward-facing, partly occluded conformation

XylE was captured in an outward-facing, partly occluded conformation. The ligand ([D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose)) resides in the centre of the transmembrane domain, completely occluded from the intracellular side yet solvent-accessible from the extracellular side through a narrow channel. This conformation represents an important expansion to the collection of MFS conformations.

### Substrate binding site and coordination

[D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose) is bound between the N and C domains, coordinated by eight hydrogen bonds with polar residues including Gln 168 (TM5), Gln 288/Gln 289/Asn 294 (TM7), Trp 392 (TM10), and Gln 415 (TM11). Aromatic residues Phe 24, Tyr 298, Trp 392 and Trp 416 surround the substrate. Tyr 298 constitutes the constriction that prevents escape of [D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose) to the extracellular side.

### Intracellular four-helix domain

Unlike other MFS transporters of known structure, XylE contains an intracellular domain comprising four helices — three connecting the N and C domains and one at the C-terminal end. The residues constituting these helices are highly conserved in [SLC2A1](/xray-mp-wiki/proteins/glut1)-4. Extensive polar interactions with the cytosolic portion of TMs suggest a similar cytoplasmic domain likely exists in [SLC2A1](/xray-mp-wiki/proteins/glut1)-4.

### D-glucose binding and inhibition

D-[Glucose](/xray-mp-wiki/reagents/additives/glucose) binds to XylE with a Kd of about 0.77 +/- 0.01 mM but is not a transport substrate. It binds similarly to [D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose) but the extra 6-hydroxymethyl group is coordinated through van der Waals contacts by Ile 171 (TM5) and Phe 383 (TM10), and through an extra hydrogen bond with Gln 175 (TM5). D-[Glucose](/xray-mp-wiki/reagents/additives/glucose) inhibits [D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose) transport by nearly 90%.

### Sugar porter signature motifs

Conserved SP family signature motifs are found in XylE: D(N)RXGRR between TMs 2-3 and 8-9, E------R between TMs 4-5 and 10-11, PESPR at TM6C, and PETK at TM12C. These motifs are positioned on the cytoplasmic side and form an intricate hydrogen-bond network mediating interactions between TMs and the intracellular domain. More than half of single point mutations in these motifs resulted in completely abrogated or seriously impaired activities.

### Disease-related GLUT1 mutations mapped to XylE model

Homology-based structural model of [SLC2A1](/xray-mp-wiki/proteins/glut1) was generated from XylE structure and sequence conservation. Disease-related mutations from [SLC2A1](/xray-mp-wiki/proteins/glut1) deficiency syndrome were mapped: Asn 34, Ser 66, Thr 295 and Thr 310 are on the extracellular side; Gly 75 and Gly 130 are in the middle of TM2 and TM4; Arg 126 and His 337 are buried within domains suggesting regulatory role. Mutations of corresponding residues in XylE (R133C, R133H, R133L, R341W) completely lost transport activity for [D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose).

### Inward-facing open conformation with detached cytoplasmic domain

The 3.5 A resolution crystal structure (PDB 4QIQ) of XylE in a new inward-facing open conformation reveals a detached cytoplasmic domain. The N-domain (residues 8-220) and C-domain (residues 276-463) form the transmembrane core. The intracellular linker between TM6 and TM7 (residues 221-273) folds into three alpha-helices (IC1-IC3) in the outward-facing conformation but becomes disordered in the inward-open state. The N-domain r.m.s.d. is 1.1 A between conformations; C-domain r.m.s.d. is 2.9 A with large changes in helix-loop-helix between TM7-8, TM10-11 and TM11-12.

### Asymmetric rocker-switch movement

Molecular dynamics simulations reveal that XylE functions through a non-symmetric rocker-switch movement in a membrane. The periplasmic half of the N-domain shows significant movement towards the C-domain to close the periplasmic vestibule while the cytoplasmic domain detaches. This differs from the symmetric rigid body movement previously reported based on crystal structure overlays alone.

### Proton-coupling mechanism via Asp27-Arg133

Conserved Asp27 (TM1) and Arg133 form a proton-coupling pair. In the outward-facing conformation at basic pH, deprotonated Asp27 interacts with Arg133 and Glu206 (TM6). In the inward-open conformation at acidic pH, Asp27 is partially protonated and no longer interacts with Arg133. Protonation of Asp27 weakens these interactions and triggers the conformational switch from outward to inward-facing. TMD simulations with protonated vs deprotonated Asp27 showed significantly altered transport dynamics.

### Sugar binding and release mechanism

Gln168 (TM5) and Trp392 (TM10) are key sugar-binding residues. Trp392 acts as a cytoplasmic substrate-release gate, swinging ~6 A away from Gln168 in the inward- facing conformation to open a tunnel to the transporter center. Mutants Q168A and W392A showed significantly reduced transport activities. During SMD simulations, [D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose) translocates through the substrate tunnel with a total energy barrier of ~7 kcal/mol at the tunnel exit point.

### Water co-transport mechanism

MD simulations indicate XylE transports water molecules along with the substrate. A solvent-filled cavity connects the Asp27-Arg133 site to the sugar-binding site. A hydrogen bond network among water molecules forms a water wire connecting protonated Asp27 to bulk water in the cytoplasm during the inward-facing conformation. This water wire was stable during TMD simulations and broken after sugar release in SMD simulations.

### First MFS transporter with multiple conformational states resolved

This study represents the first major facilitator superfamily (MFS) transporter for which structures have been determined in more than one conformational state. The two structures — inward open (PDB 4JA4, P6_1, 4.2 A) and partially occluded inward open (PDB 4JA3, C2, 3.8 A) — together with the previously reported partially occluded outward-facing structure (PDB 4GBY) provide three snapshots along the transport cycle, establishing XylE as an important MFS model protein.

### Alternate access mechanism captured in crystal structures

The XylE structures reveal the alternate access mechanism of MFS transporters. In the inward open state, the N and C subdomains form a V-shaped structure with a wide cytoplasmic opening extending to the binding site. In the partially occluded inward open state, the C-terminal half of the interrupted transmembrane helix 10 (TM10b) moves closer to the N subdomain, partially blocking the cytoplasmic opening. The rigid body movement of the two subdomains relative to each other drives the conformational transitions.

### Conserved cytoplasmic salt bridges control substrate access

Three intersubdomain salt bridges (Glu153-Arg404, Arg160-Glu397, Arg225-Glu472) form in the partially occluded outward-facing conformation and are broken in the inward open state, controlling access to the binding site from the cytoplasm. In the partially occluded inward open state, Glu397 forms a new interaction with the N terminus of TM5. The break in TM10 renders TM10b highly dynamic, facilitating partial occlusion through interaction with TM5.

### Substrate binding site and release mechanism

The [D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose)-binding site is composed of residues from both N and C subdomains. In the inward open state, the two half-sites move apart, and Trp392 moves substantially, lowering affinity and facilitating substrate release. This explains the asymmetric transport of [SLC2A1](/xray-mp-wiki/proteins/glut1) with higher affinity for binding at the extracellular than the intracellular side.

### Periplasmic interface dominated by hydrophobic interactions

At the periplasmic side, interactions between the N and C subdomains are tighter in the inward open conformation than in the partially occluded outward open conformation, but the differences are modest. The periplasmic interface is dominated by van der Waals and hydrophobic interactions with no evidence for conserved salt bridges, suggesting a different mechanistic model is needed to explain the transition between occluded and outward open states.


## Cross-References

- [Human Glucose Transporter GLUT1 (SLC2A1)](/xray-mp-wiki/proteins/mfs-transporters/glut1/) — Human homologue; structural comparison reveals 16 degree domain rotation between inward-open GLUT1 and outward-facing XylE
- [Major Facilitator Superfamily (MFS)](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — XylE belongs to the MFS, specifically the sugar porter subfamily
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — XylE captures an outward-facing conformation in the alternating-access cycle
- [Rocker-Switch Mechanism](/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/) — XylE asymmetric rocker-switch movement revealed by MD simulations
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for XylE solubilization and purification
- [Decylmaltoside (DM)](/xray-mp-wiki/reagents/detergents/dm/) — Used at 1% for XylE solubilization in ncomms5521 study
- [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/) — Crystallization precipitant at 20% for inward-open conformation
- [Calcium Acetate](/xray-mp-wiki/reagents/additives/calcium-acetate/) — Crystallization additive at 0.2 M for inward-open conformation
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used for Ni-NTA elution of His-tagged XylE at 300 mM
- [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) — Affinity purification of His-tagged XylE
- [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) — SEC polishing of XylE
- [Thrombin Protease](/xray-mp-wiki/reagents/protein-tags/thrombin-protease/) — Used to cleave His-tag from XylE
- [D-Xylose](/xray-mp-wiki/reagents/substrates/d-xylose/) — Primary ligand studied; substrate for XylE transport
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Competitive inhibitor of XylE; binds with Kd 0.77 mM; also used as crystallization additive
- [Molecular Dynamics Simulation](/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/) — Used to investigate transport cycle and proton-coupling mechanism
- [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used for SEC purification and final sample preparation (20 mM HEPES pH adjusted)
- [Tris(2-carboxyethyl)phosphine (TCEP)](/xray-mp-wiki/reagents/additives/tcep/) — Reducing agent used at 0.5 mM in lysis, solubilization, and purification buffers
- [His6-tag](/xray-mp-wiki/reagents/protein-tags/histidine-tag/) — N-terminal His6-TEV tag used for IMAC purification of XylE in nsmb.2569 study
