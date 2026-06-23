---
title: "HiGlpG (Haemophilus influenzae Rhomboid Protease)"
created: 2026-05-26
updated: 2026-06-17
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0609981104, doi/10.1016##j.jmb.2011.01.046]
verified: false
---

# HiGlpG (Haemophilus influenzae Rhomboid Protease)

## Overview

HiGlpG is the rhomboid intramembrane protease from Haemophilus influenzae, a member of the serine protease family that cleaves transmembrane substrates within the lipid bilayer. The original 2.2-A resolution crystal structure (Lemieux et al., 2007) revealed the catalytic architecture of hiGlpG, including the nucleophilic Ser-116, general base His-169, and a distinctive oxyanion hole comprising His-65 and the main-chain NH of Ser-116. The structure identified three lipids (phosphatidic acid) bound to the protein and highlighted the roles of the L1, L3, and L5 loops in substrate gating. A later high-resolution study (PDB 3ODJ, 2.85 A) revealed persistent disorder in loop 4, helix 5, and loop 5, which together form the substrate gate. Mutagenesis combined with functional assays demonstrates that flexibility in helix 5 and loop 5 is essential for substrate access to the buried active site, while loop 4 requires structural rigidity. The studies also predict that rhomboid cleavage occurs on the si-face of the scissile peptide bond.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.0609981104 | 2NR9 | 2.2 A | C2 / P2(1)2(1)2(1) | Full-length hiGlpG from Haemophilus influenzae (residues 1-276) | Three phosphatidic acid (PA) molecules; two C12E8 detergent molecules |
| doi/10.1016##j.jmb.2011.01.046 | 3ODJ | 2.85 A | C2 | HiGlpG from H. influenzae (residues 1-133 and 165-164, with residues 134-164 disordered and not modeled; loop 4, helix 5, and loop 5 lack electron density) | None (no inhibitor or ligand bound; detergent molecules present from purification) |

## Expression and Purification

- **Expression system**: Escherichia coli Top10 cells (Invitrogen) transformed with pBAD-Myc-HisA expression vector
- **Construct**: HiGlpG with N-terminal Myc epitope tag and His6 tag. Grown in LB media supplemented with [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/), induced with 0.002% arabinose at 24 C for 5 h.

### Purification Workflow

#### Source: doi/10.1073##pnas.0609981104


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and induction | Expression | — | LB medium supplemented with [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) + — | Cells grown to OD600 0.4, induced with 0.0002% arabinose at 24 C for 16 h |
| Membrane fraction isolation | Ultracentrifugation | — | TBS supplemented with EDTA-free peptidase-inhibitor mixture, 1 mM PMSF, 0.1 mg/ml DNase + — | Cells lysed by EmulsiFlex-C3 homogenizer; membranes pelleted at 100,000 x g in 45Ti rotor |
| Solubilization | Detergent solubilization | — | 50 mM Tris, 300 mM NaCl, 30 mM imidazole, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 1% DDM | Membrane fractions homogenized, stirred 30 min, then ultracentrifuged at 110,000 x g |
| Affinity purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA resin (Qiagen) | 50 mM Tris, 300 mM NaCl, 30 mM imidazole, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/); elution with 250-1000 mM imidazole step gradient + 0.1% DDM | Protein eluted in stepwise manner with 3 x 2 CV of 250, 500, and 1000 mM imidazole |
| Detergent exchange and gel filtration | Size-exclusion chromatography | Superdex200 (16/60) column (Amersham) | 50 mM Tris (pH 8.0), 20 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) + 0.05% C12E8 | Protein concentrated by 30K centrifugal filter and subjected to detergent exchange on Superdex200 column |

#### Source: doi/10.1016##j.jmb.2011.01.046


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and induction | Expression | -- | LB media supplemented with [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) + -- | Cells grown at 24 C and induced with 0.002% arabinose for 5 h |
| Membrane isolation | Ultracentrifugation | -- | -- + -- | Crude membrane fraction isolated by high-speed ultracentrifugation |
| Solubilization | Detergent solubilization | -- | -- + 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) ([DDM](/xray-mp-wiki/reagents/detergents/ddm/)) | Membranes solubilized in buffer containing 1% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (Anatrace, USA) |
| Affinity purification | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA resin | Buffer containing [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) for elution + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | His-tag affinity purification of HiGlpG |
| Tag removal | Protease digestion | -- | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Thrombin cleavage at 30 U/mg [GLPG](/xray-mp-wiki/proteins/enzymes/glpg/) for 1 h at room temperature to remove N-terminal Myc-His tag |
| Concentration and dialysis | Ultrafiltration and dialysis | -- | -- + -- | Protein dialyzed to remove [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) and concentrated using Millipore Amicon ultracentrifugal concentrators (30,000 MWCO) to 10-15 mg/ml |
| Gel filtration | Size-exclusion chromatography | [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) column | 50 mM Tris, 200 mM NaCl, 0.5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) (pH 8.0) + 0.005% AnaPOE [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/) | Final purification and detergent exchange. Buffer contained 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/). Gel filtration carried out using [Superdex 200](/xray-mp-wiki/reagents/additives/superdex-200/) column with detergent exchange (Anatrace). |


## Crystallization

### doi/10.1016##j.jmb.2011.01.046

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (hanging drop or sitting drop, as previously described) |
| Protein sample | HiGlpG at 10-15 mg/ml in 50 mM Tris, 200 mM NaCl, 0.005% AnaPOE [C12E8](/xray-mp-wiki/reagents/detergents/c12e8/), 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.5 mM [EDTA](/xray-mp-wiki/reagents/additives/edta/) (pH 8.0) |
| Reservoir | Not specified in this paper (prepared as previously described in reference 24) |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals diffracted to 2.85 A resolution, space group C2. Disorder in residues 134-164 (loop 4, helix 5, loop 5) was observed across 6 different data sets collected around 2.8 A. Approximately 150 crystals were searched for covalent inhibitors and heavy-atom derivatives. X-ray diffraction data collected on beamline 8.3.1 at the Advanced Light Source (ALS), Lawrence Berkeley Laboratory. |

### doi/10.1073##pnas.0609981104

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, hanging drop |
| Protein sample | HiGlpG at 5 mg/ml in 50 mM Tris (pH 8.0), 0.05% C12E8, 20 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Reservoir | 25% [PEG](/xray-mp-wiki/reagents/additives/peg/) 4000, 0.1 M citrate (pH 6.0), 1 M NaCl, 3% ethanol, 15% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |
| Temperature | Not specified (room temperature) |
| Growth time | 1-2 weeks |
| Cryoprotection | Crystals directly flash-cooled in liquid nitrogen (reservoir already contained 15% glycerol) |
| Notes | Crystals grew to 100 x 50 x 20 micrometers. Two space groups obtained: monoclinic C2 and orthorhombic P2(1)2(1)2(1). Monoclinic data diffracted to higher resolution (2.2 A) with one molecule in the AU. Molecular replacement with MolRep using ecGlpG coordinates (2IC8.pdb). Refinement with Refmac5. Data collected at ALS beamline 8.3.1. |


## Biological / Functional Insights

### Catalytic dyad and oxyanion hole in hiGlpG

The 2.2-A crystal structure of hiGlpG revealed the complete active-site architecture of a rhomboid intramembrane protease. The catalytic dyad consists of Ser-116 (nucleophile) and His-169 (general base), with a hydrogen bond already established between Ser116O-gamma and His169N-epsilon2 in the native unbound form. Unlike classical serine proteases, rhomboid lacks an aspartate equivalent for the third member of the catalytic triad. Instead, Tyr-120 packs against the imidazole ring of His-169 to stabilize the general base. The oxyanion hole is formed by the main-chain NH of Ser-116 and the protonated N-epsilon2 of His-65. A distinctive water molecule (W40) occupies the oxyanion hole in the resting state, bridging Ser116NH and His65N-epsilon2 and forming H-bonds to Phe113O and Val162O. This water would be displaced by the carbonyl oxygen of the P1 residue upon substrate binding. Additional stabilization of the tetrahedral intermediate comes from the helix dipole of helix H4 (Ser-116 is at the N-terminus of H4), analogous to the peptide dipole stabilization in subtilisin.

### Substrate gating by the L1, L3, and L5 loops

In the resting state, the active site of hiGlpG is buried and inaccessible to solvent. Three loops - L1 (Gly-29 to Ser-55), L3 (Gly-109 to Gly-114), and L5 (Gly-161 to Gly-165) - must move substantially to allow substrate access. These loops exhibit elevated B-factors (60-70 A^2 for L1, 50 A^2 for L3, 60 A^2 for L5) compared to the overall B-factor of 35.5 A^2, supporting their conformational flexibility. The loops are demarcated by glycine residues that confer conformational flexibility. A hypothetical sequence of events includes: (1) the destabilized transmembrane helix of the substrate docks to rhomboid, displacing the L1 gate; (2) L3 and L5 loops are displaced; (3) the substrate enters the active site. A model of the Drosophila spitz substrate (Ala-Ser-Gly-Ala) docked into the active site showed the P1 carbonyl positioned ideally for nucleophilic attack by Ser-116, with small side chains (Ala, Gly) accommodated in the active site.

### Bound lipids and membrane-mimetic environment

Three phosphatidic acid (PA) molecules were observed bound to hiGlpG in the crystal structure. Two PA molecules flank the L1 loop, and one is located near helix H6. The lipids may play a structural role, acting as chaperones, or may play a role in rhomboid function. Two additional C12E8 detergent molecules were also visible. The bound lipids may alternatively be cardiolipin (CL), phosphatidylserine (PS), or phosphatidylethanolamine (PE), the main lipids found in the E. coli lipid bilayer.

### Substrate gating by loop 4, helix 5, and loop 5 flexibility

The new hiGlpG crystal structure (3ODJ) reveals persistent disorder in loop 4 (residues 134-137), helix 5 (residues 138-144), and loop 5 (residues 145-164) across multiple crystal forms, confirming that these regions are conformationally mobile. Mutagenesis of loop 5 residues F160A and M164A retained 46-60% of wild-type peptidase activity, indicating that loop 5 flexibility is tolerated. Mutations in helix 5 F144A reduced activity by 40%. In contrast, loop 4 mutations L136A, F137A, and F84A dramatically reduced activity to 5-22%, suggesting loop 4 requires structural rigidity. Disrupting hydrophobic interactions between helix 2 and helix 5 (triple mutants W72A/F76A/F144A and W72V/F76V/F144V) actually increased substrate cleavage 2.5- and 2-fold, respectively, indicating the gate opens more readily when these contacts are weakened.

### si-face cleavage mechanism in rhomboid proteases

The structural evidence for substrate gating via helix 5 movements, combined with the active-site geometry, predicts that rhomboid cleavage occurs on the si-face of the scissile peptide bond (rather than the re-face typical of soluble serine proteases such as [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/)). The oxyanion hole is composed of the main-chain NH from Ser116 and the protonated N-epsilon from His65. This si-face attack mechanism is shared with other serine peptidases having a Ser-Lys catalytic dyad, including signal peptidase (SPase), Lon protease, LexA peptidase, and VP4 protease. A cocrystal of SPase with a beta-lactam inhibitor confirmed this stereochemistry.

### Comparison with ecGlpG gating reveals conserved rhomboid dynamics

HiGlpG differs from the E. coli rhomboid [GLPG](/xray-mp-wiki/proteins/enzymes/glpg/) (ecGlpG) in the intramolecular connections between helix 5 and helix 2: in hiGlpG, helix 5 is partially unwound and tilted away from the helical bundle, while in ecGlpG, helix 5 runs parallel to helix 2. Despite these structural differences, both rhomboids show comparable gating mechanisms with subtle variations. The disorder in loop 4, helix 5, and loop 5 observed in hiGlpG is a common feature of the rhomboid family, indicating conserved substrate access dynamics. Both gating hypotheses (loop 5 cap movement and helix 5 lateral movement) may apply, with substrate recognition possibly involving an exosite on the enzyme surface in the lipid bilayer.


## Cross-References

- [Rhomboid Protease Family](/xray-mp-wiki/concepts/protein-families/rhomboid-protease/) — HiGlpG is a member of the rhomboid intramembrane protease family
- [Intramembrane Proteolysis](/xray-mp-wiki/concepts/membrane-mimetics/intramembrane-proteolysis/) — HiGlpG cleaves transmembrane substrates within the lipid bilayer
- [GlpG (E. coli Rhomboid Protease)](/xray-mp-wiki/proteins/enzymes/glpg/) — Homologous rhomboid protease from E. coli with comparable gating mechanism
- [Cytoplasmic Domain of E. coli Rhomboid Protease GlpG (EcGlpG-Cyto)](/xray-mp-wiki/proteins/enzymes/ecglpg-cyto/) — Related structural entity representing the soluble cytoplasmic domain of the GlpG homolog
- [DDM (N-Dodecyl-beta-D-maltoside)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary solubilization detergent (1%) for HiGlpG membrane extraction
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Used at 20% in the final purification buffer for HiGlpG stability
- [Tris Buffer](/xray-mp-wiki/reagents/buffers/tris/) — Primary buffer component (50 mM, pH 8.0) for purification and crystallization
- [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) — Used for His-tag affinity purification of HiGlpG
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Superdex 200 gel filtration used for final purification and detergent exchange
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
