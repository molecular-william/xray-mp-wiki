---
title: MexB (Pseudomonas aeruginosa multidrug exporter)
created: 2026-05-26
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [transporter, pump, membrane-protein, xray-crystallography]
sources: [doi/10.1016##J.JMB.2009.04.001, doi/10.1038##nature12300]
verified: false
---

# MexB (Pseudomonas aeruginosa multidrug exporter)

## Overview

MexB is the inner-membrane component of the MexAB-OprM tripartite efflux pump in Pseudomonas aeruginosa, a major multidrug resistance system. It belongs to the resistance-nodulation-cell division (RND) superfamily of secondary active transporters. The crystal structure was solved at 3.0 A resolution, revealing an asymmetric homotrimer where each subunit adopts a distinct conformation representing three snapshots of the transport cycle. A DDM molecule was found bound in the internal multidrug-binding cavity, supporting the model that RND transporters can transport detergent molecules as substrates. The first inhibitor-bound structure of MexB was solved with the pyridopyrimidine derivative ABI-PP, revealing that the inhibitor binds to a hydrophobic trap in the distal drug-binding pocket, similar to AcrB.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##J.JMB.2009.04.001 | not specified in paper text (search model was 2J8S, asymmetric AcrB from Escherichia coli) | 3.0 A | P1 | MexB from P. aeruginosa PAO1 (1046 amino acids); C-terminal hexahistidine tag; two almost structurally identical trimers (chains ABC and DEF) in the asymmetric unit | DDM (n-dodecyl-D-maltoside) bound in the multidrug-binding cavity of subunit B |
| doi/10.1038##nature12300 | not specified | 3.15 A | P1 | MexB from P. aeruginosa with C-terminal polyhistidine tag, complexed with ABI-PP inhibitor | ABI-PP (tert-butyl thiazolyl aminocarboxyl pyridopyrimidine) |
| doi/10.1038##nature12300 | not specified | 2.70 A | P1 | Drug-free MexB from P. aeruginosa with C-terminal polyhistidine tag | DDM (n-dodecyl-beta-D-maltoside) bound in distal pocket |
| doi/10.1038##nature12300 | not specified | 3.30 A | P1 | Drug-free MexB(F178W) mutant with C-terminal polyhistidine tag | None (drug-free) |
| doi/10.1038##nature12300 | not specified | 3.00 A | P1 | MexB(F178W) mutant with C-terminal polyhistidine tag, complexed with ABI-PP inhibitor | ABI-PP (tert-butyl thiazolyl aminocarboxyl pyridopyrimidine) |

## Expression and Purification

- **Expression system**: Escherichia coli strain C43 (DE3) (wild-type), E. coli MG1655 (acrB-deficient, for F178W mutant)
- **Construct**: MexB from P. aeruginosa PAO1 with C-terminal hexahistidine tag, overproduced from plasmid pUCP20-B_His. MexB(F178W) mutant expressed from plasmid pUC118mexB F178W (pUC118 DNA, Takara Bio) in acrB-deficient E. coli strain MG1655. Expression induced with 0.1 mM IPTG for 4 h at 37 deg.C.

### Purification Workflow

*Source: doi/10.1016##J.JMB.2009.04.001*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis | French press | -- | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 1 mM PMSF, DNase I, complete protease inhibitor cocktail + -- | Membranes collected by centrifugation at 100,000g for 1 h |
| Solubilization | Detergent solubilization | -- | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 10 mM imidazole, 1 mM PMSF, 10% glycerol + 1% (wt/vol) DDM (D310LA Anagrade; Anatrace) | Solubilized for 2 h at 4 deg.C; insoluble material removed by centrifugation at 100,000g for 1 h |
| Ni-NTA affinity chromatography | Metal affinity chromatography (Ni-NTA) | Ni-NTA affinity column (Qiagen) | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 10 mM imidazole, 1 mM PMSF, 10% glycerol, 0.03% DDM (equilibration); 30 mM imidazole (wash); 200 mM imidazole (elution) + 0.03% DDM | C-terminal hexahistidine tag purification; column equilibrated with buffer A containing 0.03% DDM |
| Size-exclusion chromatography | Size-exclusion chromatography | Tricorn Superdex 200 column (Amersham Biosciences) | 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 10% glycerol + 0.03% DDM | Further purification and buffer exchange for crystallization |

### Purification Workflow

*Source: doi/10.1038##nature12300*


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and membrane isolation | High-pressure homogenizer (APV 1000, SPX) at 180 MPa, membrane fractions collected by ultracentrifugation at 158,000g for 90 min | -- | -- + -- | E. coli MG1655 (acrB-deficient) grown to A580nm of 0.7 at 37 deg.C; MexB expression induced with 0.1 mM IPTG for 4 h |
| Solubilization | Membrane solubilization | -- | 20 mM Tris-HCl (pH 7.5), 300 mM NaCl, 10% glycerol + 1.5% DDM (D316, Dojindo) | Membrane fractions solubilized in 1.5% DDM; solubilized mixture centrifuged for 1 h at 172,000g |
| Ni-affinity chromatography | Ni-affinity chromatography (Ni Sepharose Fast Flow) | Ni Sepharose Fast Flow (GE Healthcare) | 20 mM Tris-HCl (pH 7.5), 300 mM NaCl, 10% glycerol, 0.05% DDM (equilibration); 25 mM imidazole (wash); 140 mM imidazole (wash); 350 mM imidazole (elution) + 0.05% DDM | Column pre-equilibrated with buffer A containing 0.05% DDM; washed with 25 mM and 140 mM imidazole; MexB eluted with 350 mM imidazole |
| Concentration and buffer exchange | Concentration-dilution using Amicon stirred cell (Model 8010, Millipore) | -- | 10 mM Tris-HCl (pH 7.5), 50 mM NaCl, 0.05% DDM + 0.05% DDM | Three concentration-dilution steps; final protein concentration approximately 30 mg/mL |


## Crystallization

### doi/10.1016##J.JMB.2009.04.001

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | SEC-purified MexB in 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 10% glycerol, 0.03% DDM; concentrated prior to crystallization |
| Reservoir | not specified in paper text |
| Temperature | not specified |
| Growth time | not specified |
| Cryoprotection | not specified |
| Notes | Crystals belong to space group P1 with two trimers in the asymmetric unit. Structure solved at 3.0 A resolution by molecular replacement using the asymmetric AcrB structure (PDB 2J8S) as search model. R-factors: R = 24.3%, R_free = 28.7%, with 2-fold noncrystallographic symmetry applied. |

### doi/10.1038##nature12300

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 25 mg/mL MexB |
| Reservoir | 50 mM Na acetate-HCl (pH 5.5), 300 mM NaCl, 26% (v/v) polyethylene glycol 400 |
| Mixing ratio | equal volumes protein to reservoir |
| Temperature | 25 C |
| Growth time | Crystals appeared within 5 days, collected after further 5 days |
| Cryoprotection | Polyethylene glycol 400 concentration increased to 40% (v/v) in three steps; crystals flash frozen in liquid nitrogen or cryostream (100 K) |
| Notes | Drug-free MexB crystallized using DDM. P1 crystals solved at 2.70 A resolution. Electron density corresponding to entire DDM molecule evident in distal pocket. Data collected at BL44XU beamline at SPring-8 with MX225-HE CCD detector at 100 K. Crystals processed using HKL2000. Structure largely identical to 3.0 A structure in ref. 25. |

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | 25 mg/mL MexB with ABI-PP, inhibitor:protein molar ratio 5:1 |
| Reservoir | 50 mM Na acetate-HCl (pH 5.5), 300 mM NaCl, 26% (v/v) polyethylene glycol 400 |
| Mixing ratio | equal volumes protein to reservoir |
| Temperature | 25 C |
| Growth time | Crystals appeared within 5 days, collected after further 5 days |
| Cryoprotection | Polyethylene glycol 400 concentration increased to 40% (v/v) in three steps; crystals flash frozen in liquid nitrogen or cryostream (100 K) |
| Notes | ABI-PP-bound MexB crystallized using DDM. P1 crystals solved at 3.15 A resolution. Fo-Fc omit map contoured at 3.0 sigma. The hydrophobic TAP moiety of ABI-PP inserts into narrow hydrophobic trap surrounded by F136, F178, F610, F615, F628 and F573. Hydrophilic tetrazole ring interacts with D274, R620 and K151. PAEA moiety extends towards R128 in MexB (different from AcrB where it is bent between piperidine ring and aceto-amino ethylene ammonio-acetate group). |

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | Drug-free MexB(F178W) mutant |
| Reservoir | Similar conditions to wild-type MexB, except n-octyl-beta-D-thioglucoside used as additive |
| Mixing ratio | Similar to wild-type |
| Temperature | 25 C |
| Growth time | Similar to wild-type |
| Cryoprotection | Polyethylene glycol 400 concentration increased to 40% (v/v) in three steps; crystals flash frozen in liquid nitrogen or cryostream (100 K) |
| Notes | Drug-free MexB(F178W) crystallized using DDM with n-octyl-beta-D-thioglucoside as additive. P1 crystals solved at 3.30 A resolution. Overall structure almost identical to wild-type MexB. Indolyl side chain of W178 does not protrude towards hydrophobic trap because space is partially occupied by bound DDM molecule. |

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | MexB(F178W) mutant with ABI-PP, inhibitor:protein molar ratio 5:1 |
| Reservoir | Similar conditions to wild-type MexB |
| Mixing ratio | Similar to wild-type |
| Temperature | 25 C |
| Growth time | Similar to wild-type |
| Cryoprotection | Polyethylene glycol 400 concentration increased to 40% (v/v) in three steps; crystals flash frozen in liquid nitrogen or cryostream (100 K) |
| Notes | ABI-PP-bound MexB(F178W) crystallized using DDM. P1 crystals solved at 3.00 A resolution. ABI-PP detected in hydrophobic trap as in wild-type MexB. Indolyl ring of W178 fits into position capable of forming pi-pi interactions with pyridopyrimidine ring without large conformational change relative to ABI-PP-free structure. |


## Biological / Functional Insights

### Asymmetric homotrimer transport mechanism

MexB adopts an asymmetric homotrimeric conformation where each subunit represents a different
state in the transport cycle. Subunit B (binding) exhibits a channel open to the periplasm
for substrate capture. Subunit C (extrusion) has a channel open toward the outer-membrane
factor docking site. Subunit A shows an altered conformation, likely representing a transitional
state, potentially influenced by crystal packing. The progression through conformations is
ABC rather than BAC.

### Multidrug-binding cavity with bound DDM

A large drug-binding cavity is formed by the four pore domain subdomains (PN1, PN2, PC1, PC2).
A DDM molecule was observed bound in subunit B, with the maltoside group interacting with
Val47, Ser48, Gln125, Val177, Gly179, Ser180, Gln273, and Arg620. The binding site corresponds
to minocycline and doxorubicin sites in AcrB, demonstrating that RND transporters can transport
detergent molecules as substrates. The cavity is rich in polar residues at the distal end and
aromatic residues at the proximal end.

### Proton translocation mechanism conserved with AcrB

The transmembrane region is highly conserved between MexB and AcrB, with key charged residues
Asp407, Asp408 (TM4) and Lys939 (TM10) forming a salt-bridge involved in proton translocation.
In subunit C, the lysine is tilted towards Thr976 (TM11), implicating a rigid-body shift of
TM5 towards TM4 and TM10, and conformational changes in TM8. The N-terminal end of TM8,
connecting the transmembrane domain to the PC2 subdomain, adopts different conformations across
subunits and is believed to trigger the large conformational changes in the pore domains.

### Structural differences in pore domain subunit A

Compared to AcrB, a shift of the PC2 subdomain results in closure of the periplasmic portal
in one subunit, with no access to the binding cavity observed. The portal from the membrane
bilayer leading to the channel of subunit B in MexB is more constricted than in AcrB, likely
due to a more helical conformation of the N-terminal part of TM8. In MexB, TM8 in subunit B
is fully helical, whereas in AcrB it varies from random-coil (subunit A) to fully helical
(subunit C).

### Electrostatic differences in binding pocket

The electrostatic surface potential of the MexB binding pocket is slightly more positive than
AcrB due to two exposed arginine residues. Since minocycline is positively charged at the
crystallization pH of 4.5, the positive electrostatic potential may explain difficulties in
obtaining crystals of MexB-minocycline complexes. These subtle differences in binding pockets
likely underlie the altered substrate specificity between MexB and AcrB.

### Assembly of the tripartite MexAB-OprM system

The docking domains of MexB and AcrB are very similar, each consisting of two subdomains with
a long protruding loop inserting into the neighboring subunit. Despite high structural
similarity, OprM and TolC are not interchangeable between MexAB and AcrAB systems. The high
specificity likely relies on the membrane fusion protein (MFP) rather than the outer-membrane
factor (OMF), consistent with the finding that RND transporters interact transiently with OMFs
at low affinity.

### Crystal packing influences subunit A conformation

The two trimers of MexB in the asymmetric unit pack head-to-head, substantially involving the
periplasmic part with approximately 700 A^2 of surface area buried at this interface, mainly
through the PC2 subdomain of subunit A. The altered conformation of subunit A could be a result
of crystal contacts, but evidence suggests functional significance: the symmetry-related trimer
has an identical conformation, and the PC1 and PC2 domains show the smallest sequence
conservation between MexB and AcrB, suggesting this difference could be an intrinsic property
of MexB.

### ABI-PP binding to hydrophobic trap in MexB

The first inhibitor-bound structure of MexB was solved with ABI-PP at 3.15 A resolution. The
ABI-PP binding site in MexB is similar to that in AcrB. The hydrophobic TAP moiety inserts
into a narrow hydrophobic trap surrounded by F136, F178, F610, F615, F628 and F573. The
hydrophilic tetrazole ring interacts with D274, R620 and K151. The conformations of the ABI-PP
moieties are almost the same as in AcrB. However, the PAEA moiety in MexB extends towards R128,
whereas in AcrB it is bent between the piperidine ring and the aceto-amino ethylene ammonio-acetate
group. The distal pocket is separated into two parts: a relatively hydrophilic
substrate-translocation channel and a hydrophobic trap forming a deep and narrow fissure.

### DDM molecule bound in MexB distal pocket

The crystal structure of drug-free MexB at 2.70 A resolution revealed clear electron density
corresponding to an entire molecule of DDM in the distal pocket. The bound DDM partially
overlaps with the bound ABI-PP in the narrow hydrophobic trap. This demonstrates that the
hydrophobic trap can accommodate both detergent molecules and small-molecule inhibitors, and
that DDM binding in this site may influence inhibitor accessibility.

### MexB(F178W) mutant retains ABI-PP sensitivity unlike AcrB(F178W)

Despite introducing the same F178W mutation in both AcrB and MexB, the two mutants showed
different responses to ABI-PP. While AcrB(F178W) lost sensitivity to ABI-PP, MexB(F178W)
remained fully inhibitable. Crystal structures revealed that the indolyl side chain of W178
in MexB(F178W) does not protrude towards the hydrophobic trap because that space is partially
occupied by a DDM molecule, as in wild-type MexB. In contrast, the indolyl side chain of
W178 in AcrB(F178W) protrudes into the narrow space of the hydrophobic trap, blocking ABI-PP
binding. This difference is attributed to steric hindrance with V139 in AcrB and I138 in
MexB at corresponding positions.

### Hydrophobic trap architecture separates substrate channel from inhibitor site

The distal drug-binding pocket of MexB is separated into two parts: a relatively hydrophilic
substrate-translocation channel with sufficient space for multisite drug binding, and a
hydrophobic trap forming a deep and narrow fissure. The hydrophobic trap is rich in
phenylalanine residues that do not directly interact with exported drugs but indirectly
affect drug binding. ABI-PP binds tightly to this trap and inhibits the functional rotation
mechanism of MexB monomers, potentiating the activities of all antibiotics exported by MexB.
The inhibitor specificity between MexB and MexY is determined by subtle differences in the
amount of space in the hydrophobic trap.


## Cross-References

- [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/acrB/) — Close homologue (69.8% identity, 83.2% similarity); structure solved by molecular replacement using asymmetric AcrB (PDB 2J8S) as search model; shares same asymmetric transport mechanism
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent used for solubilization (1% DDM), purification (0.03% DDM), and crystallization; also observed bound in the multidrug-binding cavity of subunit B and distal pocket, suggesting RND transporters can transport detergents as substrates
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Used at 10 mM in solubilization buffer, 25-140 mM for Ni-NTA wash, and 350 mM for elution of C-terminal hexahistidine-tagged MexB
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — 10% glycerol included in all purification buffers for protein stability
- [PMSF (Phenylmethylsulfonyl Fluoride)](/xray-mp-wiki/reagents/additives/pmsf/) — 1 mM PMSF added during cell lysis and solubilization as a serine protease inhibitor
- [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin/) — Used for plasmid maintenance during E. coli expression
- [Tris Buffer (Tris-HCl)](/xray-mp-wiki/reagents/buffers/tris/) — 20 mM Tris-HCl pH 7.5 used as the primary buffer in cell lysis, solubilization, affinity chromatography, and SEC purification steps
- [Sodium Acetate](/xray-mp-wiki/reagents/buffers/sodium-acetate/) — 50 mM Na acetate-HCl (pH 5.5) used as crystallization buffer component for MexB
- [Polyethylene Glycol 400 (PEG 400)](/xray-mp-wiki/reagents/additives/peg-400/) — 26% (v/v) PEG 400 used as precipitant in MexB crystallization; increased to 40% for cryoprotection
- [ABI-PP (tert-butyl thiazolyl aminocarboxyl pyridopyrimidine)](/xray-mp-wiki/reagents/ligands/abi-pp/) — Inhibitor bound in hydrophobic trap of MexB; first inhibitor-bound structure of MexB solved
- [n-Octyl-beta-D-thioglucoside](/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-thioglucoside/) — Used as crystallization additive for MexB(F178W) mutant
- [MexY (Pseudomonas aeruginosa multidrug exporter)](/xray-mp-wiki/proteins/mexY/) — Close homologue; MexY(W177F) mutant studied in parallel to understand inhibitor specificity
