---
title: ZneA Zn(II)/Proton Antiporter from Cupriavidus metallidurans
created: 2026-06-08
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1318705110]
verified: false
---

# ZneA Zn(II)/Proton Antiporter from Cupriavidus metallidurans

## Overview

ZneA is a proton-driven efflux pump specific for Zn(II) from the heavy metal-resistant bacterium Cupriavidus metallidurans CH34. It belongs to the heavy metal efflux (HME) family of the resistance-nodulation-cell division (RND) superfamily. ZneA forms a homotrimer, with each protomer consisting of 12 transmembrane α-helices and two large periplasmic loops forming the porter (pore) domain and the outer membrane factor (OMF)-coupling docking domain. Two X-ray crystal structures were determined at 3.0 and 3.7 A resolution, capturing intermediate transport conformations at low and high pH. The structures reveal proximal and distal Zn(II) binding sites in the porter domain, with transport regulated by a 14-aa access loop.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1073##pnas.1318705110 | 4K0E | 3.7 A | Not specified | Full-length ZneA from Cupriavidus metallidurans CH34 (high-pH structure)
 | Zn(II) |
| doi/10.1073##pnas.1318705110 | 4K0J | 3.0 A | Not specified | Full-length ZneA from Cupriavidus metallidurans CH34 (low-pH structure)
 | Zn(II) |

## Expression and Purification

No purification described.

## Crystallization

No crystallization described.

## Biological / Functional Insights

### ZneA is a Zn(II)-specific proton-dependent antiporter

Functional reconstitution assays in proteoliposomes demonstrate that ZneA transports Zn(II) in response to a pH gradient (ΔpH, inside-alkaline). Of five divalent metal ions tested (Zn(II), Cd(II), Co(II), Ni(II), Mn(II)), only Zn(II) was efficiently exported (~95% of maximal signal), while other cations showed only 10-28% release. Transport is electrogenic with a proton-to-Zn(II) ratio other than 2:1, as demonstrated by stimulation of Zn(II) efflux by membrane potential (ΔΨ, inside-negative).

### Proximal and distal Zn(II) binding sites

The high-pH structure shows a fully occupied Zn(II) site in the center of the porter domain (proximal site) and one near the exit funnel (distal site) in all three protomers. The proximal site is an anionic pocket coordinated by carboxylates of E136, D602, E610, D654, and D658. This site is conserved in the divalent metal-ion transporters CzcA and CnrA but absent from the monovalent metal-ion transporter [CusA Inner Membrane Efflux Pump](/xray-mp-wiki/proteins/abc-transporters/cusA/) and drug transporter [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/). At low pH, the proximal site is occupied in only two of three protomers, with D602 displaced ~1.3 A in the unbound protomer.

### Access loop regulates substrate transport

A 14-aa access loop (connecting Cβ2 and Cβ3 strands of the PC1 subdomain) lines the transport tunnel between the proximal and distal sites. The loop can adopt different conformations that alternately permit and gate substrate extrusion, ensuring unidirectional transport by preventing backflow from the distal to the proximal site. This mechanism differs from the corresponding G-loop/Phe-617 loop in [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/), which regulates transport by alternately occluding substrate binding.

### Proton translocation via TM4 carboxylates

Three conserved acidic residues on TM4 (D393, D399, and E406) span ~19 A from the center of the transmembrane domain toward the cytoplasm. Their carboxylate side chains all orient between TM4 and TM11, forming a network of titratable residues ~40-60 A from the proximal binding site. Mutagenesis of the corresponding residues in CzcA (D402N, D408N, E415Q) leads to loss of proton-dependent transport activity, supporting their role as proton translocation sites.


## Cross-References

- [CusA Inner Membrane Efflux Pump](/xray-mp-wiki/proteins/abc-transporters/cusA/) — Related RND efflux pump with different substrate specificity (Cu(I) vs Zn(II))
- [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/) — Related protein structure
