---
title: BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)
created: 2026-05-29
updated: 2026-06-02
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NATURE07819, doi/10.1038##nature11403, doi/10.1038##nsmb.1788, doi/10.1038##EMBOJ.2013.226]
verified: false
---

# BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)

## Overview

BetP is a Na+-coupled glycine betaine symporter from the bacterium [Corynebacterium glutamicum](/xray-mp-wiki/organisms/corynebacterium-glutamicum). It belongs to the BCCT (Betaine/Carnitine/Choline Transporter) family and plays a critical role in osmoregulation by accumulating the compatible solute glycine betaine in response to hyperosmotic stress. BetP is activated by intracellular K+ and other osmotic stimuli through its C-terminal regulatory domain. The crystal structure revealed a homotrimeric assembly with each monomer containing 10 transmembrane helices and a distinctive 4-helix bundle regulatory domain, providing the first structural insights into osmo-sensing in a secondary transporter.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##NATURE07819 | 3JEO | 3.35 | P212121 | SeMet-substituted BetP with N-terminal 29-residue deletion (Delta N29), N-terminal StrepII tag | [Glycine Betaine](/xray-mp-wiki/reagents/ligands/glycine-betaine), sodium ions |
| doi/10.1038##nature11403 | 4AIN | 3.1 | Not specified | Surface-engineered BetP mutant (BetP Delta N29/E44E45E46/AAA) crystallized in presence of 5 mM betaine | [Glycine Betaine](/xray-mp-wiki/reagents/ligands/glycine-betaine), sodium ions |
| doi/10.1038##nature11403 | 4AMR | 3.25 | Not specified | BetP G153D mutant (Gly 153 to aspartate in unfolded stretch of TMH1') co-crystallized with [Choline](/xray-mp-wiki/reagents/ligands/choline); sixfold increased affinity for sodium | [Choline](/xray-mp-wiki/reagents/ligands/choline), sodium ions |
| doi/10.1038##EMBOJ.2013.226 | 4C7R | 2.70 | Not specified | BetP Delta N29/E44E45E46/AAA surface-engineered mutant, all three protomers in inward-open (Ci) state with 8 bound POPG lipids | [Citrate](/xray-mp-wiki/reagents/additives/citrate) (bound in cytoplasmic funnel), 8 POPG lipids (16:0/18:1) |

## Expression and Purification

- **Expression system**: [Corynebacterium glutamicum](/xray-mp-wiki/organisms/corynebacterium-glutamicum) (native expression system); also expressed in E. coli (DH5alpha) for proteoliposome reconstitution assays
- **Construct**: BetP Delta N29 (residues 30-437 of full-length 437 aa protein) with N-terminal StrepII tag; [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine)-substituted variant for SAD phasing; surface-engineered mutant BetP Delta N29/E44E45E46/AAA; substrate-specificity mutant G153D

### Purification Workflow

*Source: doi/10.1038##NATURE07819*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | Detergent solubilization from C. glutamicum membrane fractions | StrepTactin resin (StrepII tag affinity) | Buffer containing [Tris](/xray-mp-wiki/reagents/buffers/tris) + Not specified | Expression in C. glutamicum; mutants assessed by immuno-blotting against N-terminal StrepII tag |

### Purification Workflow

*Source: doi/10.1038##EMBOJ.2013.226*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Detergent exchange and thorough washing | StrepTactin affinity chromatography with Cymal-5 exchange | StrepTactin | 100 mM 3Na-Citrate pH 5.4-5.5, 300 mM NaCl, 20-21% PEG400 + 1.2% Cymal-5 (detergent exchanged from DDM) | Washing steps removed unspecifically bound lipids. TLC analysis confirmed presence of PG lipids (not PE) in the purified BetP sample. |
| Lipid analysis by TLC | Thin layer chromatography (HPTLC) | Not applicable | Chloroform:methanol:water (13:7:0.8) solvent system for 1D separation + Cymal-5 | Phospholipid analysis confirmed negatively charged PG/CL species. Cymal-5 confounded initial separation. PG identity confirmed by acetone:methanol:acetic acid:water:chloroform (2:1:1:0.5:5) system. |

### Purification Workflow

*Source: doi/10.1038##nature11403*

- **Expression system**: E. coli DH5alpha
- **Expression construct**: Surface-engineered BetP mutants (BetP Delta N29/E44E45E46/AAA and BetP G153D) with N-terminal StrepII tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane solubilization | Detergent solubilization | -- | Not specified + beta-dodecyl-maltoside ([DDM](/xray-mp-wiki/reagents/detergents/ddm)) | Membranes solubilized using [DDM](/xray-mp-wiki/reagents/detergents/ddm) for heterologously expressed BetP |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | Strep-Tactin macroprep | Strep-Tactin | Not specified + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | Affinity purification via Strep-Tactin macroprep for StrepII-tagged BetP |
| [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | Not specified | Not specified + [DDM](/xray-mp-wiki/reagents/detergents/ddm) | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) for final polishing of BetP sample |


## Crystallization

### doi/10.1038##NATURE07819

| Parameter | Value |
|---|---|
| Method | Hanging drop [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | Se-Met labeled BetP Delta N29 construct |
| Reservoir | Not specified in supplementary information |
| Temperature | 20 |
| Growth time | Not specified |
| Notes | Space group P212121; unit cell a=118.09, b=129.42, c=182.94 A; alpha=beta=gamma=90 degrees; SAD phasing with selenium sites |

### doi/10.1038##nature11403

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | BetP Delta N29/E44E45E46/AAA crystallized in presence of 5 mM betaine |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Data collected to 3.1 A at PXII beamline of Swiss Light Source (SLS); structure determined by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement) using BetP (PDB 4AMR) as search model |

| Parameter | Value |
|---|---|
| Method | Co-crystallization with substrate |
| Protein sample | BetP G153D mutant co-crystallized with [Choline](/xray-mp-wiki/reagents/ligands/choline) |
| Reservoir | Not specified |
| Temperature | Not specified |
| Growth time | Not specified |
| Notes | Data collected to 3.2 A at beamline id29 at ESRF; structure determined by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement) using BetP (PDB 3P03) as search model |

### doi/10.1038##EMBOJ.2013.226

| Parameter | Value |
|---|---|
| Method | [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) |
| Protein sample | BetP Delta N29/E44E45E46/AAA at ~12 mg/ml in 1.2% Cymal-5 |
| Reservoir | 100 mM 3Na-Citrate pH 5.4-5.5, 300 mM NaCl, 20-21% PEG400 |
| Temperature | 18 |
| Growth time | Not specified |
| Notes | Crystals grown by vapor diffusion at 18 C using 1:2 volume ratio of protein to reservoir. Single crystal yielded isotropic diffraction to 2.7 A at ESRF beamline id29. Structure determined by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement) using BetP trimer (PDB 2WIT) as search model. No NCS imposed during refinement. 8 POPG lipids modeled into clear Fo-Fc densities. |


## Biological / Functional Insights

### Trimeric assembly with central cavity

BetP forms a homotrimer with a central cavity at the interface. Aromatic side chains from helix 7 and TM2 of each monomer point into the cavity, where unmodelled Fo-Fc density (at 1.8 sigma) represents bound lipid or detergent. The trimeric interface involves residues in TM8 and TM9. The C-terminal domain of each monomer makes crystal contacts with the adjacent trimer, suggesting the regulatory domain extends beyond the transmembrane core.

### Sodium ion coordination sites

Two sodium ion binding sites (Na1 and Na2) were identified by structural superposition with [LeuT](/xray-mp-wiki/proteins/leut)_M. Na1 is coordinated by residues in TM3i, TM3e, TM4, TM5, TM7, TM8, and TM10. Na2 involves a conserved g-x-g-x-g motif in TM3 characteristic of sodium-coupled transporters in the BCCT family. The sodium ions were not included in the refinement process but their coordination geometry supports a Na+/betaine co-transport mechanism.

### Aromatic substrate pathway

Twenty-three aromatic side chains line the substrate pathway along a central 4-helix bundle (TM3, TM4/TM8, TM9). These aromatic boxes create surface properties that allow a wide variety of osmolytes to be transported without direct interaction with the protein backbone. The [Glycine Betaine](/xray-mp-wiki/reagents/ligands/glycine-betaine) binding pocket shows homology with the periplasmic binding protein ProX from E. coli, particularly in the orientation of Trp box residues. The aromatic boxes in TM3/TM4/TM8/TM9 include W188, W189, W194, Y197, W362, W366, W371, W374, W377, and W374.

### Osmo-sensing and regulation

BetP is regulated by intracellular K+ concentration and hyperosmotic stress through its C-terminal regulatory domain. Functional analysis of mutants showed that residues E135, R210, G301, R387, and R392 are essential for transport activity. The N-terminal 29 residues (Delta N29 construct) were deleted to facilitate crystallization but the protein retained substantial activity in E. coli polar lipid proteoliposomes (268 nmol [Glycine](/xray-mp-wiki/reagents/buffers/glycine) betaine/ min mg protein vs 771 for WT).

### BCCT family structural conservation

The BetP structure was compared with other transporters of the BCCT family, including OpuD from B. subtilis, ButA from Tetragenococcus halophila, BetT from E. coli, and EctP from C. glutamicum. Sequence alignment revealed strictly conserved residues across the family. The overall fold is related to the [LeuT](/xray-mp-wiki/proteins/leut) scaffold (RMSD 3.7 A for scaffold comparison), with similar repeat domain architecture to MFS transporters like SGLT and Mhp1. The BetP repeat domains show RMSD of 3.5 A between repeat 1 and repeat 2.

### Conformational asymmetry in BetP trimers

Crystal structures of surface-engineered BetP mutants reveal trimers that lack non-crystallographic three-fold symmetry. Each protomer within one trimer adopts a different conformation of the alternating-access cycle: a substrate-free outward-occluded (C_eoc), a substrate-free outward-open (C_e), a closed substrate-free (C_c), and a closed substrate-bound (C_cS) state. Additionally, an inward-open betaine-bound (C_iS) and inward-open [Choline](/xray-mp-wiki/reagents/ligands/choline)-bound state were captured. This conformational asymmetry allows observation of up to six distinct transport states within a single trimer, providing a comprehensive view of the transport cycle. The closed states reported for the first time for a LeuT-like fold transporter represent an intermediate between outward- and inward-facing states.

### Tryptophan prism and betaine binding

The closed substrate-bound state (C_cS) is characterized by a central binding site (S1 site) closed by nearly 14 A of protein bulk from either side of the membrane. The trimethylammonium group of betaine in the S1 site forms cation-pi interactions with Trp 373, Trp 374, and Trp 377, arranged in a tryptophan prism entirely within TMH6'. These residues comprise the signature motif of the BCCT family. Trp 377 has a dominant role and any exchange against another residue renders BetP inactive, whereas substitution of Trp 373 or Trp 374 decreases affinity. In the inward-open state (C_iS), betaine shifts towards the cytoplasm so that it solely interacts with Trp 377 in TMH6' and backbone carbonyls from TMH1'. The binding energy is exploited fully only in the transient C_cS transition state, where betaine fits perfectly.

### Sodium-binding sites Na1 and Na2

Both sodium ions bind at the interface between scaffold and bundle helices. The Na2 site provides reasonable coordination in outward-open and closed states but coordinating residues are too distant in the inward-open state due to conformational changes of TMH1a'. The Na1 site, formed by Phe 380 in TMH6', Thr 246 and Thr 250 in TMH3', is only properly coordinated in the closed state. Sodium binding to Na2 relates to opening-closing of cytoplasmic gates, while Na1 binding relates to opening-closing of periplasmic gates. The conservation of the Na2 site is the unifying element in the [LeuT](/xray-mp-wiki/proteins/leut)-like fold transport mechanism.

### Alternating-access mechanism and gating

The alternating-access mechanism in BetP is a hybrid of rigid body movements and individual flexing of symmetry-related helices. The scaffold motif (TMH3', TMH4' in repeat 1 and TMH8', TMH9' in repeat 2) tilts about 13 degrees relative to the 4-TMH bundle. TMH1a' is displaced by approximately 5 A and tilted by 18 degrees to open the cytoplasmic gate, while TMH10' (periplasmic thin gate) moves 5.7 A with a 41 degree tilt. TMH5' (cytoplasmic thin gate) undergoes a 9 degree tilt. The presence of a closed transition state implies uncoupled hinge movements of periplasmic and cytoplasmic gates. The spring-like movement of the unfolded region of TMH1' transiently coordinates sodium ions during the alternating-access cycle, correlating with the absolute requirement of sodium for betaine symport.

### Substrate specificity and G153D mutant

Exchange of Gly 153 against aspartate in the unfolded stretch of TMH1' results in a sixfold increased affinity for sodium and additional specificity for [Choline](/xray-mp-wiki/reagents/ligands/choline). This mutation demonstrates the plasticity of the TMH1' region and its role in ion coupling. Side-chain rotations of aromatic residues in TMH1' and TMH6' (Phe 156, Phe 369, Phe 380, Phe 384) are highly conserved in the BCCT family and contribute to betaine recruitment, predominantly from outside to inside. Alanine substitution of periplasmic occluding residues decreases affinity for betaine, while mutation of cytoplasmic pathway residues did not have a major effect on affinity.

### Eight specifically bound PG lipids in the BetP trimer

The 2.7 A resolution structure of BetP (PDB 4C7R) revealed eight ordered POPG (palmitoyl-oleoyl phosphatidyl glycerol) lipids bound to the trimer at specific sites. Five lipids (L1-L5) occupy the central hydrophobic cavity of the trimer (non-annular sites), while three (L6, L7, U1) are annular lipids at the trimer periphery. Head groups were assigned to PG based on 2Fo-Fc and Fo-Fc difference maps and primarily positively charged coordinating residues. Acyl chains were assigned as 16:0/18:1 based on E. coli phospholipidome composition. The head groups of L1-L3 in the symmetrical trimer core sites are coordinated by residues from loop 2 (K121) and IL3 (R395) - both important in conformational changes during transport.

### Lipid L7 interaction with the glycine-rich unwound region of TM1 prime

Annular lipid L7 is positioned at the trimer periphery, nested between TM5 prime and TM1 prime. One of its acyl chains interacts directly with Met150 in the glycine-rich unwound stretch of TM1 prime, a region critical for conformational changes. Mutation of Met150 to isoleucine significantly alters the osmoregulation profile of BetP (requires higher osmolality for maximal activity). Mutation to phenylalanine combined with I152A results in only slightly altered osmoprofile. This suggests that the lipid L7 interaction with the catalytic core modulates osmotic stress activation.

### PG lipids as cofactors for trimer assembly and regulation

Negatively charged PG lipids constitute only 15% of the E. coli membrane but are selectively retained during affinity purification of BetP, indicating their structural necessity. The central non-annular lipids (L1-L5) are coordinated by residues from loop 2 and IL3 of adjacent chains, effectively crosslinking the trimer. Lipid L4 specifically involves the C-terminal helix of chain A (R554, R558, Q557), providing an electrostatic interaction site that restrains the positively charged C-terminal domain. These lipid-mediated interactions are proposed to regulate gating helix (TM1 prime, TM6 prime) movements during the transport cycle.

### State-dependent lipid occupancy during transport cycle

Comparing the 2.7 A inward-facing structure with lower-resolution structures of outward and closed states revealed different lipid occupancy patterns. Central non-annular lipids showed density in outward states (four lipids), only partial density in closed states (one lipid), and full occupancy in the inward-facing state (five lipids). Annular lipids were only resolved in the inward-facing state. This suggests that specific lipid-protein interactions are linked to the conformational state of BetP, potentially contributing to inactivation or activation during the transport cycle.


## Cross-References

- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — BetP is a secondary active transporter using alternating-access mechanism
- [Sodium-Motive Force (SMF)](/xray-mp-wiki/concepts/sodium-motive-force/) — BetP is a Na+-coupled symporter driven by sodium electrochemical gradient
- [Glycine Betaine](/xray-mp-wiki/reagents/ligands/glycine-betaine/) — Primary substrate/osmolyte transported by BetP
- [Choline](/xray-mp-wiki/reagents/ligands/choline/) — Secondary substrate for BetP G153D mutant with sixfold increased sodium affinity
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for BetP membrane solubilization and purification
- [BCCT Family](/xray-mp-wiki/concepts/bcct-family/) — BetP is the founding member of the BCCT transporter family
- [LeuT Amino Acid Transporter](/xray-mp-wiki/proteins/enzymes/leut/) — [LeuT](/xray-mp-wiki/proteins/leut) used as structural reference for BetP conformational analysis
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Used for structure determination of both BetP structures from this paper
- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/) — BetP shares [LeuT](/xray-mp-wiki/proteins/leut) fold topology (RMSD 3.7 A) but lacks Leu25-like side chain rotation in substrate-free states
- [Vapor Diffusion](/xray-mp-wiki/methods/crystallization/vapor-diffusion) — Crystallization method used for structure determination
- [Size-Exclusion Chromatography (SEC)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) — Purification method used in protein preparation
