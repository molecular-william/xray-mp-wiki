---
title: Phospholamban (PLB)
created: 2026-06-03
updated: 2026-06-03
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography, pump]
sources: [doi/10.1038##nature11900, doi/10.1038##nature07152]
verified: false
---

# Phospholamban (PLB)

## Overview

Phospholamban (PLB, also known as PLN) is a small (~52 amino acid) membrane protein that regulates the sarcoplasmic reticulum Ca2+-ATPase (SERCA) by binding to it and lowering its apparent Ca2+ affinity. PLB is primarily expressed in heart muscle in humans, whereas sarcolipin (SLN) predominates in skeletal muscle. PLB and SLN are homologous regulators that bind SERCA in a similar fashion. Phosphorylation of PLB by protein kinase A or CaMKII relieves its inhibitory effect on SERCA, providing a key mechanism for beta-adrenergic regulation of cardiac contractility.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature11900 | TBD | Low resolution (~20 A) | Not determined | PLB-SERCA complex observed by electron microscopy | Not determined |

## Expression and Purification

- **Expression system**: Mammalian heart muscle, native expression
- **Construct**: Native PLB from cardiac sarcoplasmic reticulum; no heterologous expression

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Membrane preparation | Isolation of sarcoplasmic reticulum from heart muscle | -- | Not specified in this paper | PLB co-purifies with SERCA from cardiac SR membranes |


## Crystallization

No crystallization described.

## Biological / Functional Insights

### PLB and SLN are homologous SERCA regulators

PLB and SLN are believed to bind to and regulate SERCA in a similar fashion. Binding of PLB or SLN to SERCA lowers the apparent Ca2+ affinity, thus modulating the threshold Ca2+ concentration at which SERCA gains transport activity. PLB expression predominates in the heart, whereas SLN is primarily expressed in skeletal muscle.

### Phosphorylation relieves PLB inhibition of SERCA

Phosphorylation of PLB is a key regulatory mechanism of SERCA activity, as SERCA is only inhibited by non-phosphorylated PLB at resting Ca2+ conditions. During beta-adrenergic stimulation, PLB is phosphorylated by protein kinase A or CaMKII, resulting in a rapid increase in Ca2+ uptake to the sarcoplasmic reticulum, which strongly affects relaxation and contraction.

### PLB pentamerization interface is opposite SERCA-binding interface

Both PLB and SLN exist in monomeric and multimeric free forms and as monomers and dimers in SERCA-bound forms. Mutational analysis shows that PLB can interact with SERCA at least in part as pentamers, as the pentamerization-interface residues and SERCA-binding residues are on opposite sides of the helix, allowing simultaneous formation of both PLB-PLB and SERCA-PLB interactions.

### PLB mutations in cardiomyopathy map to specific faces of the helix

Loss-of-function mutations in PLB map to the SERCA-binding interface, while gain-of-function mutations map to the outside of the helix. Gain-of-function mutations are presumably due to impaired PLB pentamerization leading to more active monomer forms that cannot bind SERCA effectively.

### SLN-bound SERCA structure reveals shared regulatory mechanism

The crystal structure of SERCA in complex with SLN suggests a mechanism for how both SLN and PLB inhibit SERCA: by stabilizing an E1 intermediate state without bound Ca2+. This provides new insight into autoinhibitory regulation of P-type ATPases and may prove useful in studying how regulatory domains of other ion pumps modulate transport.


## Cross-References

- [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase 1a)](/xray-mp-wiki/proteins/serca1a/) — Primary target of PLB regulation; PLB binds and inhibits SERCA
- [Sarcolipin (SLN)](/xray-mp-wiki/proteins/sarcolipin/) — Homologous regulator of SERCA; similar binding mechanism and regulatory role
- [Phosphoenzyme E2P State](/xray-mp-wiki/concepts/phosphoenzyme-e2p-state/) — PLB regulates the E1-E2 conformational cycle of SERCA
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/alternating-access-mechanism/) — PLB modulates the alternating-access transport cycle of SERCA
