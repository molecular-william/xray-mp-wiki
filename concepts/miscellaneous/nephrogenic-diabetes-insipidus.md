---
title: Nephrogenic Diabetes Insipidus
created: 2026-06-08
updated: 2026-06-08
type: concept
category: concepts
layout: default
tags: [concept-functional, membrane-protein]
sources: [doi/10.1038##s41598-023-41616-1]
verified: false
---

# Nephrogenic Diabetes Insipidus

## Overview
Nephrogenic diabetes insipidus (NDI) is a water balance disorder
characterized by the inability to concentrate urine in response to the
antidiuretic hormone arginine vasopressin (AVP). In contrast to central
diabetes insipidus (caused by reduced AVP secretion), NDI results from
resistance to AVP in the distal nephron. Patients void large volumes
(typically ~12 L/day) of hypo-osmotic urine and are at high risk of
severe dehydration and hypernatremia if fluid intake does not compensate
for urinary losses. NDI may be acquired (most commonly from chronic
lithium treatment) or congenital.


## Mechanism/Details
The urinary concentration defect in NDI arises from dysregulation of the
membrane-bound water channel aquaporin-2 ([AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/)) in kidney collecting duct
principal cells. Under basal conditions, [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) resides in subapical storage
vesicles. Upon AVP binding to the vasopressin V2 receptor (V2R) in the
basolateral membrane, a signaling cascade increases cAMP production via
adenylyl cyclase, stimulating PKA-mediated phosphorylation of Ser-256 in
the [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) C-terminus. This promotes translocation of AQP2-containing
vesicles to the apical membrane and inhibits endocytosis, thereby
increasing apical [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) abundance. Additional phosphorylation at Ser-264
and Thr-269 contributes to AVP-dependent [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) accumulation, while
dephosphorylation of Ser-261 promotes retention. Once water balance is
restored and AVP levels drop, changes in [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) phosphorylation and
C-terminal ubiquitination trigger endocytosis, after which [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) may be
stored in vesicles, degraded, or released in exosomes.

Congenital NDI is typically caused by mutations in the genes for either
the V2 receptor (X-linked NDI, ~90% of cases) or [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) (autosomal NDI,
~10% of cases). Most [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) mutations are inherited autosomal recessively;
dominant mutations are less common and located in the C-terminus where
trafficking control sites are clustered. Recessive mutations are unable
to form hetero-tetramers with wild-type [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/), likely due to misfolding,
and are retained in the endoplasmic reticulum (ER). Mutations occur
throughout the six transmembrane helices and connecting loops. The T125M,
T126M, and A147T mutations — all associated with recessive NDI — have
been shown to retain functional water channel activity yet are prevented
from reaching the plasma membrane by ER quality control. T125M lacks
N-glycosylation due to disruption of the N123 glycosylation consensus
site. T126M acquires a hydrophobic residue at position +3 relative to the
glycosylation site, becoming a preferred substrate for [UDP-Glucose (UDP-Glc)](/xray-mp-wiki/reagents/substrates/udp-glucose/)
glycoprotein glucosyltransferase (UGT), prolonging calnexin/calreticulin
cycle retention. A147T significantly destabilizes the [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) tetramer,
promoting monomeric states and aggregation.


## Examples in Membrane Protein Work
- [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) T125M — Disrupts N-glycosylation consensus site (N123); non-glycosylated; retained in ER/Golgi; functional water channel (74.3% of WT Pf); structure essentially identical to WT
- [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) T126M — Glycosylated but high-mannose form; hydrophobic residue at position +3 relative to N123; substrate for UGT; prolonged CNX/CRT cycle; functional water channel (92.6% of WT Pf)
- [AQP2](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) A147T — Located in TM4 near Ca2+-binding site; significant tetramer destabilization (Tm reduced ~9 °C); monomeric/aggregated states; functional water channel (49.9% of WT Pf); poor crystallization quality

## Related Concepts
- []() — 
- []() — 

## Cross-References
- [Aquaporin-2 (AQP2)](/xray-mp-wiki/proteins/other-ion-channels/aqp2/) — AQP2 mutations are the direct cause of congenital NDI
- [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) — Aquaporin water channels mediate the water transport dysregulated in NDI
- [N-Glycosylation Sequon](/xray-mp-wiki/concepts/membrane-mimetics/n-glycosylation-sequon/) — N-glycosylation quality control in ER is central to recessive NDI mechanism
- [UDP-Glucose (UDP-Glc)](/xray-mp-wiki/reagents/substrates/udp-glucose/) — Entity mentioned in text
