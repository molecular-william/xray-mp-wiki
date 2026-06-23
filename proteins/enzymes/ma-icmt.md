---
title: "Isoprenylcysteine Carboxyl Methyltransferase (ICMT) from Methanosarcina acetivorans"
created: 2026-05-26
updated: 2026-05-26
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.molcel.2011.10.020]
verified: false
---

# Isoprenylcysteine Carboxyl Methyltransferase (ICMT) from Methanosarcina acetivorans

## Overview

ICMT (isoprenylcysteine carboxyl methyltransferase) is an integral membrane methyltransferase that catalyzes the final step of CAAX processing — the carboxyl methylation of prenylated cysteine residues in proteins such as Ras and Rho GTPases. The crystal structure of a prokaryotic ortholog from Methanosarcina acetivorans (Ma-ICMT) reveals a unique architecture with five transmembrane helices and a cytosolic cofactor-binding pocket, with a substrate access tunnel linking the catalytic site to the inner membrane. This structure explains how an integral membrane methyltransferase achieves recognition of both a hydrophilic cofactor ([SAM](/xray-mp-wiki/reagents/cofactors/sam/)) and a lipophilic prenyl substrate within the lipid bilayer.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1016##j.molcel.2011.10.020 | 4A2N | 3.4 A | P6222 | Ma-ICMT (MA2698 from Methanosarcina acetivorans) in complex with SAH cofactor | SAH ([S-Adenosyl-L-Homocysteine (AdoHcy)](/xray-mp-wiki/reagents/cofactors/s-adenosyl-l-homocysteine/)), endogenous C9 alkyl chain lipid |

## Expression and Purification

- **Expression system**: E. coli strain C41(DE3)
- **Construct**: Ma-ICMT (MA2698) fused with TEV-cleavable C-terminal GFP-His7 tag. Cloned into pTriEX-based plasmid (pOPIN-GFP).

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Expression | Protein expression in E. coli | -- | -- + -- | Ma-ICMT-GFP-His7 expressed in E. coli strain C41(DE3) at 20 degrees C overnight |
| Ni-NTA [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) | Ni-NTA resin (His-tag affinity) | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Ma-ICMT-GFP-His7 purified with Ni-NTA using the C-terminal His7 tag |
| [Ion-Exchange Chromatography](/xray-mp-wiki/methods/purification/ion-exchange-chromatography/) | [Ion-Exchange Chromatography](/xray-mp-wiki/methods/purification/ion-exchange-chromatography/) | Ion exchange resin | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Ion exchange purification step to further purify Ma-ICMT |
| Size-exclusion chromatography | Size-exclusion chromatography | Size-exclusion resin | -- + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Final polishing step using size-exclusion chromatography |


## Crystallization

### doi/10.1016##j.molcel.2011.10.020

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | 8 mg/ml Ma-ICMT in buffer (20 mM MES [pH 6.5], 200 mM [[Sodium Chloride](/xray-mp-wiki/reagents/additives/sodium-chloride/)], 10% [v/v] [[Glycerol](/xray-mp-wiki/reagents/additives/glycerol/)], and 0.024% [[DDM](/xray-mp-wiki/reagents/detergents/ddm/)]) |
| Reservoir | 5 mM SAH ([S-Adenosyl-L-Homocysteine (AdoHcy)](/xray-mp-wiki/reagents/cofactors/s-adenosyl-l-homocysteine/)) and 0.5 mg/ml [polar lipids] (Avanti Polar Lipids) |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals were obtained in complex with SAH (Sigma) but not in its absence, suggesting that cofactor influences the protein conformation and is required for conformational homogeneity necessary for crystallization. Two derivatives were collected: EMTS (ethylmercurithiosalicylate) at DLS beam line I02, and gold derivative (KAu(CN)2) at DLS beam line I03. Structure determined from SAD phases obtained from EMTS and gold derivatives and multicrystal averaging. |


## Biological / Functional Insights

### Unique integral membrane methyltransferase architecture

Unlike all known aqueous methyltransferases, ICMT is an integral membrane protein with five transmembrane helices (H1 to H5) and a short C-terminal cytosolic alpha helix (H6). The cofactor-binding pocket is completely enclosed within a highly conserved C-terminal catalytic subdomain of approximately 90 amino acids, and a substrate access tunnel connects the catalytic site to the inner membrane. The tunnel features a hydrophobic upper region within the membrane (for prenyl lipid access) and a hydrophilic lower region in the cytosol (for the polar protein substrate C terminus).

### Substrate access tunnel architecture and lipid binding

A substrate access tunnel located between helices H1 and H2 provides the only access to the [SAM](/xray-mp-wiki/reagents/cofactors/sam/) cofactor, specifically the catalytic methyl group. Strong and continuous rod-like electron density was interpreted as a C9 alkyl chain derived from endogenous lipid bound within Ma-ICMT, suggesting it might mimic a substrate prenyl lipid. The hydrophobic upper tunnel region is positioned within the inner membrane, whereas the hydrophilic lower regions open into the cytosol.

### Catalytic mechanism and substrate positioning

The guanidinium side chain of Arg163 (invariant residue of the M2 motif) is positioned at the inner entrance of the tunnel to form electrostatic interactions with the substrate carboxylate group, aligning it for direct in-line nucleophilic attack onto the reactive methyl group of [SAM](/xray-mp-wiki/reagents/cofactors/sam/). Mutation of Arg163 abolished carboxyl methyltransferase activity. Arg163 is absent from [Phosphatidylethanolamine](/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/) methyltransferase, an enzyme that methylates a positively charged amine group rather than a carboxylate.

### Conserved cofactor-binding residues and catalytic mechanism

The cofactor-binding cavity (volume of 1291 A^3) is generated from the L3 loop and cytosolic segments of H5 and H6. Conserved residues His126 and Glu167 (charge-neutralizing residues from M1 and M2 motifs) are essential for cofactor binding — their mutation completely eliminated methylation activity. Residues interacting with the adenine ring (His113) or indirectly contacting cofactor (Tyr129) impaired catalytic activity by approximately 75%. The cofactor adopts a closed conformation most similar to class IV methyltransferases.

### Substrate specificity toward prenyl lipids

Ma-ICMT displayed robust catalytic activity toward the AFC analog S-farnesylthioacetic acid (FTA), at a 6-fold lower rate than AFC-catalyzed methylation by yeast ICMT, and some substantially weaker activity toward AFC. No activity was detected toward a farnesylated peptide substrate or the straight-chain fatty acid palmitic acid, suggesting the enzyme may not recognize straight-chain alkyl lipids. This mirrors the much lower affinity of rat ICMT toward S-alkyl peptide derivatives compared with S-prenyl peptides.

### ICMT as an anticancer therapeutic target

ICMT is essential for proper subcellular localization of CAAX proteins including Ras and Rho GTPases, which regulate diverse cellular processes. Carboxyl methylation augments the hydrophobicity of the prenyl membrane anchor, and pharmacological inhibition of ICMT disrupts Rho-mediated cell migration and adhesion. ICMT inhibition negatively regulates Ras and Rho signaling, implicating ICMT as an anticancer therapeutic target. Existing substrate-competitive ICMT inhibitors are lipophilic and compromise bioavailability; the Ma-ICMT structure provides a framework for rational design of [SAM](/xray-mp-wiki/reagents/cofactors/sam/) antagonists as an alternative approach.


## Cross-References

- [SAM (S-Adenosyl-L-Methionine)](/xray-mp-wiki/reagents/ligands/sam/) — Essential cofactor for ICMT methyltransferase activity, binds in the enclosed cofactor-binding pocket
- [DDM (N-Dodecyl-beta-D-maltoside)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization and purification of Ma-ICMT
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Included in purification and crystallization buffer (10% v/v)
- [MES (2-(N-morpholino)ethanesulfonic acid)](/xray-mp-wiki/reagents/buffers/mes/) — Buffer used in crystallization (20 mM MES, pH 6.5)
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Salt component in crystallization buffer (200 mM NaCl)
- [Ni-NTA Agarose Resin](/xray-mp-wiki/reagents/additives/nickel-nta/) — Used for His-tag affinity purification of Ma-ICMT-GFP-His7
- [Superdex 200 Increase SEC Resin](/xray-mp-wiki/reagents/additives/superdex-200/) — Size-exclusion chromatography resin used for final purification step
- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Method used in structure determination or purification
- [Ion-Exchange Chromatography](/xray-mp-wiki/methods/purification/ion-exchange-chromatography/) — Method used in structure determination or purification
- [S-Adenosyl-L-Homocysteine (AdoHcy)](/xray-mp-wiki/reagents/cofactors/s-adenosyl-l-homocysteine/) — Related ligand or cofactor
