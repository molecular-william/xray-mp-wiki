---
title: "Carbon Catabolite Repression"
created: 2026-06-03
updated: 2026-06-03
type: concept
category: concepts
layout: default
tags: [concept-functional, subdirectory-miscellaneous]
sources: [doi/10.1038##nature12232]
verified: regex
---

# Carbon Catabolite Repression

## Overview
Carbon catabolite repression (CCR) is a global regulatory phenomenon in bacteria and higher organisms where the availability of a preferred carbon source (such as [Glucose](/xray-mp-wiki/reagents/additives/glucose/)) represses the synthesis and activities of proteins required for transport and metabolism of secondary carbon sources. In enteric bacteria like Escherichia coli, CCR is mediated by the phosphotransferase system (PTS), specifically through the phosphorylation state of enzyme IIA^Glc (EIIA^Glc). Up to 5-10% of all bacterial genes are subject to CCR regulation. CCR optimizes energy usage by ensuring bacteria preferentially uptake carbohydrates that support rapid growth.


## Mechanism/Details
In E. coli, CCR is mediated by modulation of the phosphorylation state of EIIA^Glc. The influx of PTS substrates and other readily metabolizable carbon sources increases the level of unphosphorylated EIIA^Glc by affecting the intracellular [PEP]/[pyruvate] ratio. Phosphorylated EIIA^Glc stimulates cAMP synthesis, leading to transcriptional activation of many catabolic genes. Unphosphorylated EIIA^Glc directly inhibits several non-PTS sugar transport systems including the [Maltose](/xray-mp-wiki/reagents/additives/maltose/) transporter (MalFGK2), lactose permease (LacY), [Melibiose](/xray-mp-wiki/reagents/ligands/melibiose/) permease ([MELB](/xray-mp-wiki/proteins/mfs-transporters/melbst/)), and raffinose permease (RafB). It also prevents [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) uptake by binding to [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) kinase. This direct inhibition of transporters is known as [Inducer Exclusion](/xray-mp-wiki/concepts/miscellaneous/inducer-exclusion/). The regulation of the lac operon is the best known example of this feedback mechanism.


## Examples in Membrane Protein Work
- [Maltose](/xray-mp-wiki/reagents/additives/maltose/) Transporter (MalFGK2) — Unphosphorylated EIIA^Glc binds to the cytoplasmic ATPase subunits ([MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/)) of the [Maltose](/xray-mp-wiki/reagents/additives/maltose/) transporter, stabilizing it in an inward-facing conformation and preventing ATP hydrolysis. Two EIIA^Glc molecules bind to the [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/) subunits, wedging between the NBD of one [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/) and the regulatory domain of the opposite [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/). This allosteric inhibition prevents the NBD closure required for the transport cycle. The IC50 of full-length EIIA^Glc is 1.61 uM for inhibition of maltose-MBP stimulated ATPase activity.
- Lactose Permease (LacY) — Unphosphorylated EIIA^Glc directly inhibits the lactose permease LacY, a major facilitator superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/)) transporter. Binding of EIIA^Glc to LacY is enhanced by the presence of the sugar substrate. The mechanism is likely different from that of the [Maltose](/xray-mp-wiki/reagents/additives/maltose/) transporter since LacY is an [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) transporter, not an ABC transporter.
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) Kinase — Unphosphorylated EIIA^Glc binds to [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) kinase, preventing [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) uptake and metabolism. The binding interface overlaps with that used for [Maltose](/xray-mp-wiki/reagents/additives/maltose/) transporter inhibition, involving a canonical surface on EIIA^Glc that also interacts with EIIB^Glc and HPr.

## Related Concepts


## Cross-References
- [EIIA^Glc (Escherichia coli Enzyme IIA^Glc)](/xray-mp-wiki/proteins/abc-transporters/eiiaglc/) — Key regulatory protein; unphosphorylated form mediates CCR
- [Maltose Transporter (MalFGK2)](/xray-mp-wiki/proteins/abc-transporters/maltose-transporter-malfgk2/) — Primary ABC transporter target of EIIA^Glc-mediated CCR
- [Inducer Exclusion](/xray-mp-wiki/concepts/miscellaneous/inducer-exclusion/) — Mechanism by which unphosphorylated EIIA^Glc inhibits transporters
- [Allosteric Regulation in Membrane Proteins](/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/) — EIIA^Glc acts as an allosteric inhibitor of target transporters
- [ABC Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/) — Maltose transporter is an ABC importer subject to CCR regulation
- [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) — Related biological concept
- [MalK (Escherichia coli Maltose Transporter ATPase Subunit)](/xray-mp-wiki/proteins/abc-transporters/malK/) — Related protein structure
- [MELB](/xray-mp-wiki/proteins/mfs-transporters/melbst/) — Related protein structure
- [Glucose](/xray-mp-wiki/reagents/additives/glucose/) — Additive used in purification or crystallization buffers
- [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) — Additive used in purification or crystallization buffers
