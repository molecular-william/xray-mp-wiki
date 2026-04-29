---

title: P2Y12 Receptor
created: 2026-04-26
updated: 2026-04-27
type: protein
tags: [gpcr, membrane-protein, receptor]
sources: [doi/10.1016##j.bcp.2022.115291]

category: proteins
---
layout: default


# P2Y12 Receptor

## Overview

The P2Y12 receptor is a G-protein-coupled receptor (GPCR) expressed on platelets that mediates ADP-induced platelet activation and aggregation. It couples to Gi/Go proteins and is a major target for antiplatelet drugs in the prevention of thrombosis and acute coronary syndrome.

## Structure Determination

- **Resolution**: 2.8 Å (2.78 Å)
- **Method**: X-ray crystallography, lipidic cubic phase (LCP)
- **Space group**: C2
- **Cell dimensions**: a=98.1 Å, b=155.3 Å, c=47.3 Å, β=111.5°
- **Ligand**: Selatogrel (ACT-246475)
- **Construct**: P2Y12-BRIL (thermostabilized BRIL fusion in ICL3)
- **PDB ID**: 7PP1
- **Key mutation**: D294⁷·⁴⁹N — improves yield of purified protein

## Expression and Purification

- **Expression system**: [sf9-cells](/methods/expression-systems/sf9-cells/) (baculovirus [baculovirus-expression](/methods/expression-systems/baculovirus-expression/))
- **Construct design**:
  - Human P2Y12 receptor with thermostabilized [bril](/reagents/protein-tags/bril/) (Apafant [bril](/reagents/protein-tags/bril/), PDB: 1M6T) fused into ICL3 at positions T223–R224
  - Intact N and C termini
  - D294⁷·⁴⁹N mutation for improved purification yield
- **Detergent**: [ddm](/reagents/detergents/ddm/) (n-dodecyl-β-D-maltopyranoside) for membrane solubilization
- **Purification**: [imac](/methods/purification/imac/) (Ni-NTA immobilized metal affinity chromatography), elution in presence of 2 mM [selatogrel](/reagents/ligands/selatogrel/)
- **SEC**: [superdex-columns](/methods/purification/superdex-columns/) increase column, buffer containing 20 mM [hepes-buffer](/reagents/buffers/hepes-buffer/) pH 7.5, 150 mM [sodium-chloride](/reagents/additives/sodium-chloride/), 0.05% [ddm](/reagents/detergents/ddm/), 2 mM [selatogrel](/reagents/ligands/selatogrel/)

## Crystallization

- **Method**: [lipidic-cubic-phase](/methods/crystallization/lipidic-cubic-phase/) (LCP) — [monoolein](/methods/crystallization/monoolein/)-based mesophase
- **Lipid**: [monoolein](/methods/crystallization/monoolein/) (Sigma M8410)
- **Protein-to-lipid ratio**: 1:1.5 (w/w)
- **Precipitant**: 0.1 M [sodium-citrate](/reagents/additives/sodium-citrate/) pH 5.6, 18–20% [peg-400](/reagents/additives/peg-400/)
- **Temperature**: 20 °C
- **Crystal growth**: 1–2 weeks

## Pharmacology

- **[selatogrel](/reagents/ligands/selatogrel/)**: Reversible, highly selective antagonist; Kd = 1.5 nM; IC50 = 14 nM for ADP-induced aggregation
- **Inverse agonism**: [selatogrel](/reagents/ligands/selatogrel/) completely abolishes constitutive P2Y12 activity in human platelets
- **100-fold more potent than [ticagrelor](/reagents/ligands/ticagrelor/)** in inverse agonist efficacy
- **Clinical profile**: Improved blood-loss profile vs. [clopidogrel](/reagents/ligands/clopidogrel/) and [ticagrelor](/reagents/ligands/ticagrelor/) at equivalent antithrombotic efficacy
- **No off-target effects** on vascular tone regulation (unlike [ticagrelor](/reagents/ligands/ticagrelor/))

## Binding Pocket

- **Pocket 1**: Spans helix III to VII
- **Selatogrel binding mode**: Orthosteric, steric overlap with proposed ADP/2MeSADP binding site
- **Conformation**: Inverse agonist stabilizes the inactive, basal state of the receptor
- **Plasticity**: P2Y12 exhibits striking conformational changes in extracellular regions, setting it apart from other class A GPCRs

## Related Ligands

- **[ticagrelor](/reagents/ligands/ticagrelor/)**: Reversible P2Y12 antagonist with inverse agonist efficacy (market approved)
- **[elinogrel](/reagents/ligands/elinogrel/)**: Reversible P2Y12 antagonist with inverse agonist efficacy
- **AZD1283**: Allosteric modulator (PDB: 4NTJ)
- **2MeSADP**: Agonist (2-methylthioadenosine diphosphate)
- **[clopidogrel](/reagents/ligands/clopidogrel/)**: Irreversible antagonist (market approved)
- **Prasugrel**: Irreversible antagonist (market approved)

## Therapeutic Relevance

- Enhanced constitutive P2Y12 activation in type 2 diabetes associated with thrombotic risk
- Inverse agonists may be superior to neutral antagonists for preventing basal platelet activation

## Related GPCRs

- [a2a-adenosine-receptor](/proteins/a2a-adenosine-receptor.html) — Another GPCR with extensive structural studies
- [opsin-gpcr](/proteins/opsin-gpcr.html) — Class A GPCR structural model
- [kappa-opioid-receptor](/proteins/kappa-opioid-receptor.html) — Opioid GPCR with [nanobody](/reagents/antibodies/nanobody/) stabilization
- [5ht2b-receptor](/proteins/5ht2b-receptor.html) — Serotonin GPCR with [bril](/reagents/protein-tags/bril/) fusion and [lipidic-cubic-phase](/methods/crystallization/lipidic-cubic-phase/) crystallization