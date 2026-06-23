---
title: "E. coli Lipoprotein Diacylglyceryl Transferase (Lgt)"
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms10198]
verified: false
---

# E. coli Lipoprotein Diacylglyceryl Transferase (Lgt)

## Overview

Lgt (phosphatidylglycerol:prolipoprotein diacylglyceryl transferase) is an integral membrane enzyme from Escherichia coli that catalyses the first step of bacterial lipoprotein biogenesis: the transfer of a diacylglyceryl group from [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) (PG) to the thiol group of the conserved cysteine residue in the lipobox motif of prolipoproteins. The crystal structures of E. coli Lgt were determined at 1.6 and 1.9 A resolution, revealing a novel 7-transmembrane helix fold with a periplasmic head domain, two amphipathic arms, and a central cavity containing two PG-binding sites. The catalytic centre involves a conserved hydrogen bond network centred on R143 and R239. Lgt is an essential enzyme in Gram-negative bacteria and a potential target for broad-spectrum antibiotics.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##ncomms10198 | 5AZC | 1.6 | P2_12_12_1 | wild-type E. coli Lgt (residues 3-286) | palmitic acid, [OG](/xray-mp-wiki/reagents/detergents/og/), PG |
| doi/10.1038##ncomms10198 | 5AZC | 1.9 | P2_12_12_1 | wild-type E. coli Lgt (residues 3-286) | PG, diacylglycerol ([DAG](/xray-mp-wiki/reagents/lipids/dag/)) |

## Expression and Purification

- **Expression system**: E. coli C43(DE3) with pET28a vector; [Iptg](/xray-mp-wiki/reagents/additives/iptg/) induction at 16 C for 20 h
- **Construct**: full-length E. coli Lgt (291 aa) with N-terminal [His6 Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/)

### Purification Workflow


##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell lysis and membrane preparation | Homogenization at 10,000-15,000 psi, differential centrifugation | — | 20 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) |  |
| Solubilization | Detergent solubilization | — | 0.5% [DM](/xray-mp-wiki/reagents/detergents/dm/) ([DM](/xray-mp-wiki/reagents/detergents/dm/)) |  |
| Ni-NTA affinity chromatography | Affinity chromatography | HiTrap nickel column | Elution: 20 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 10% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 0.25% [DM](/xray-mp-wiki/reagents/detergents/dm/), 300 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) |  |
| Size-exclusion chromatography | SEC | — | 20 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 100 mM NaCl, 0.6% [OG](/xray-mp-wiki/reagents/detergents/og/) |  |


## Crystallization

### doi/10.1038##ncomms10198

| Parameter | Value |
|---|---|
| Method | Vapor diffusion (not explicitly specified as hanging/sitting drop) |
| Protein sample | Purified Lgt in 20 mM [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 100 mM NaCl, 0.6% [OG](/xray-mp-wiki/reagents/detergents/og/); concentrated to ~20 mg/mL |
| Reservoir | Not explicitly specified in the raw text |
| Temperature | Not specified |
| Notes | Two crystal forms obtained: form-1 (1.6 A, with palmitic acid/OG) and form-2 (1.9 A, with PG/DAG). Phased using Se-Met SAD. |


## Biological / Functional Insights

### Novel 7-TM fold with central cavity and two substrate-binding sites

Lgt adopts a novel folding topology with seven transmembrane helices (TMs 1-7) organized into a major and minor TM domain, a periplasmic head domain, and two amphipathic arms. The central cavity between the major and minor TM domains contains two distinct PG-binding sites separated by W256. The first PG-binding site (site I) involves E151, and the second (site II) involves the catalytically essential R143. Two clefts (front and side) connect the cavity to the lipid bilayer, providing lateral access for substrates.

### Catalytic mechanism and key residues

The catalytically essential residues include R143, R239, and H103 (from the conserved HGGL motif). R143 directly binds the donor substrate PG at the second binding site, while R239 is part of the buried H-bond network. H103 in the HGGL motif at the N-terminal end of TM3 is critical for activity and likely interacts with the lipobox-containing peptide substrate. The cytoplasmic side is highly positively charged (positive-inside rule). The proposed mechanism involves SN2-like attack of the lipobox cysteine thiol on the diacylglyceryl group of PG.

### Inhibitor binding and substrate specificity

Palmitic acid binds to the active site and acts as a competitive inhibitor of Lgt. The enzyme shows specificity for negatively charged phospholipids as diacylglyceryl donors: DPPG > DPPS > DPPA, while neutral lipids (DPPE, DPPC, [DAG](/xray-mp-wiki/reagents/lipids/dag/)) are not substrates. Saturated alkyl chains stabilize Lgt more effectively than unsaturated chains. A GFP-based in vitro assay (lipoGFP substrate) was developed to monitor Lgt activity. Lyso-PG can serve as a substrate but is less effective than full PG.


## Cross-References

- [OG](/xray-mp-wiki/reagents/detergents/og/) — Referenced in context related to OG
- [DAG](/xray-mp-wiki/reagents/lipids/dag/) — Referenced in context related to DAG
- [Iptg](/xray-mp-wiki/reagents/additives/iptg/) — Referenced in context related to Iptg
- [His6 Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) — Referenced in context related to His6 Tag
- [Tris Hcl](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in context related to Tris Hcl
- [DM](/xray-mp-wiki/reagents/detergents/dm/) — Referenced in context related to DM
- [DM](/xray-mp-wiki/reagents/detergents/dm/) — Referenced in context related to DM
- [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) — Referenced in context related to Phosphatidylglycerol
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Referenced in context related to Glycerol
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Referenced in context related to Imidazole
