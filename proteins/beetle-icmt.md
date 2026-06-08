---
title: Isoprenylcysteine Carboxyl Methyltransferase (ICMT) from Tribolium castaneum
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature25439]
verified: false
---

# Isoprenylcysteine Carboxyl Methyltransferase (ICMT) from Tribolium castaneum

## Overview

ICMT (isoprenylcysteine carboxyl methyltransferase) from the beetle Tribolium castaneum is an integral membrane enzyme that catalyzes the final step of CAAX box processing — the carboxyl methylation of prenylated cysteine residues in proteins such as RAS GTPases, prelamin A, and RAB proteins. The beetle ortholog exhibited superior biochemical stability compared to other eukaryotic ICMT orthologues, making it suitable for crystallization. The structure reveals eight transmembrane alpha-helices and a unique active site architecture spanning both cytosolic and membrane-exposed regions, solving the topographical challenge of bringing two reactants with different cellular localizations together in a membrane environment.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature25439 | Not specified in raw paper | 2.3 A | P21 21 21 | Full-length beetle ICMT (UniProt D6WJ77) with C-terminal YL1/2 antibody-affinity tag (AAEGEEF), in complex with AdoHcy cofactor, monoolein lipid, and MB-15 monobody inhibitor. Surface mutations G151A and E154A introduced for crystallizability. | S-adenosyl-L-homocysteine (AdoHcy), monoolein lipid, MB-15 monobody |
| doi/10.1038##nature25439 | Not specified in raw paper | 4.0 A | C2221 | Beetle ICMT without monobody, in detergent (DMNG) | AdoHcy cofactor, lipid density in cavity |

## Expression and Purification

- **Expression system**: Pichia pastoris strain SMD1168
- **Construct**: Full-length beetle ICMT (D6WJ77) with C-terminal YL1/2 antibody-affinity tag (Ala-Ala-Glu-Gly-Glu-Glu-Phe, AAEGEEF). Cloned into pPICZ-C vector (EcoRI and SalI sites). Surface mutations G151A and E154A introduced to improve crystallizability.

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and solubilization | Detergent solubilization | -- | 10 mM Tris-HCl (pH 7.5), 150 mM KCl, 2 mM TCEP, 2 mM CaCl2, 25 uM AdoHcy + 2 g DMNG (decyl maltose neopentyl glycol) per 40 g cells, 45 min at room temperature | Lysed P. pastoris cells extracted with DMNG detergent |
| Antibody-affinity chromatography | Affinity chromatography | YL1/2 antibody coupled to CNBr-activated sepharose beads | 10 mM Tris-HCl (pH 7.5), 150 mM KCl, 2 mM TCEP, 2 mM CaCl2, 25 uM AdoHcy, 1 mM DMNG + 1 mM DMNG | YL1/2 antibody recognizes C-terminal AAEGEEF tag. Elution with 5 mM Asp-Phe peptide or Glu-Glu-Phe peptide |
| Size-exclusion chromatography | Size-exclusion chromatography | Superdex 200 Increase column (GE Healthcare) | 10 mM Tris-HCl (pH 7.5), 150 mM KCl, 5 mM TCEP, 2 mM CaCl2, 25 uM AdoHcy, 1 mM DMNG + 1 mM DMNG | ICMT-monobody complex purified at 1:3 molar ratio (ICMT:monobody) |


## Crystallization

### doi/10.1038##nature25439

| Parameter | Value |
|---|---|
| Method | Lipidic cubic phase (LCP) |
| Protein sample | Purified beetle ICMT in complex with MB-15 monobody (1:3 molar ratio) |
| Temperature | Not specified |
| Growth time | Not specified |
| Cryoprotection | Not specified |
| Notes | Crystals obtained in lipidic-cubic phase in the presence of AdoHcy cofactor and AGGC substrate analog. SeMet crystals collected for SAD phasing. Native crystals at 2.3 A (P21 21 21) and 4.0 A (C2221, ICMT without monobody in detergent). |


## Biological / Functional Insights

### Integral membrane architecture with eight transmembrane helices

Beetle ICMT contains eight transmembrane alpha-helices (M1-M8) and resides almost entirely within the endoplasmic reticulum membrane. The largest cytosolic region forms the binding site for AdoHcy and is composed of an extension of M8, a structurally ordered M6-M7 connector, and a short cap helix near the C terminus. The M6-M7 connector does not fully reach the luminal side but is stabilized by interactions with the M5-M6 connector.

### Active site spans cytosolic and membrane-exposed regions

The active site uniquely spans both cytosolic and membrane-exposed regions, indicating distinct entry routes for the cytosolic methyl donor AdoHcy and for prenylcysteine substrates associated with the ER membrane. The prenyl-binding cavity is approximately 22 A long and 6 A wide, extending from the cofactor pocket into the transmembrane region. Approximately two-thirds of the cavity is exposed to the cytosolic leaflet via a lateral crevice between helices M5 and M8. The cavity is lined primarily by aromatic amino acids (Tyr95, Met99, Phe102, Val124, Asn126, Tyr131, Trp215, Trp218, Tyr235, Phe242, Phe243) that markedly reduce enzyme activity when mutated.

### Substrate access through membrane crevice

The crevice between M5 and M8, accessible to the hydrophobic core of the membrane, provides a plausible route for prenyl entry by lateral diffusion. The M4-M5 connector, which is highly conserved and greatly diminishes catalytic activity when mutated, creates a hydrophilic depression within the membrane-embedded region that might induce a concomitant depression in proximal lipids of the bilayer, accommodating the upstream peptide portion of substrate proteins.

### Monobody inhibition mechanism

The MB-15 monobody binds ICMT adjacent to the active site, interacting with portions of M5, M8, and the M6-M7 loop. The monobody FG loop dips into the membrane region and presents a tryptophan residue (Trp80) that occupies part of the M5-M8 crevice. Hydrogen bonding between Ser77 of the monobody and Arg246 of ICMT contributes to inhibitory function; Arg246 is predicted to coordinate the C-terminal carboxylate of the prenylcysteine substrate. The monobody would prevent prenylated substrates from reaching the active site and/or block product release.

### Transition state stabilization mechanism

The C-terminal carboxylate of the prenylcysteine substrate forms hydrogen bonds with Arg173 and Arg246 that orient it for inline nucleophilic attack. The transition state is stabilized by additional interactions: a CH-O hydrogen bond with the side chain hydroxyl of Tyr212, a CH-O hydrogen bond with the backbone carbonyl oxygen of Asn185, and a CH-pi interaction with the aromatic face of Phe184. All proposed transition state stabilizing residues are perfectly conserved among ICMT enzymes.

### Comparison with prokaryotic MaMTase

Despite sharing only 14% sequence identity with the prokaryotic methyltransferase MaMTase, the AdoHcy binding sites are analogous. The cofactor-binding domain of ICMT (M6 through cap helix) shares a recognizable fold with MaMTase and with a prokaryotic integral membrane sterol reductase (MaSR1) that uses NADP+, suggesting this domain represents a structural motif for soluble cofactor binding to integral membrane enzymes. However, substrate-binding sites differ significantly in size, amino acid composition, and membrane exposure.


## Cross-References

- [SAM (S-Adenosyl-L-Methionine)](/xray-mp-wiki/reagents/cofactors/sam/) — Methyl donor cofactor for ICMT methylation reaction
- [DMNG (Decyl Maltose Neopentyl Glycol)](/xray-mp-wiki/reagents/detergents/dmng/) — Detergent used for solubilization and purification of beetle ICMT
- [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) — Lipid used in LCP crystallization and modeled in the active site cavity
- [TCEP (Tris(2-carboxyethyl)phosphine)](/xray-mp-wiki/reagents/additives/tcep/) — Reducing agent used throughout purification and crystallization
- [Tris-HCl](/xray-mp-wiki/reagents/buffers/tris/) — Buffer component (10 mM, pH 7.5) in purification and crystallization
- [Potassium Chloride (KCl)](/xray-mp-wiki/reagents/additives/potassium-chloride/) — Salt component (150 mM) in purification buffers
- [Calcium Chloride (CaCl2)](/xray-mp-wiki/reagents/additives/calcium-chloride/) — Added at 2 mM in lysis and purification buffers
- [Ma-ICMT (Isoprenylcysteine Carboxyl Methyltransferase from Methanosarcina acetivorans)](/xray-mp-wiki/proteins/ma-icmt/) — Prokaryotic ortholog with analogous cofactor-binding domain but different substrate access architecture
