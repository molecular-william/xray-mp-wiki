---
title: "Ion-Exchange Chromatography"
created: 2026-06-02
updated: 2026-06-03
type: method
category: methods
layout: default
tags: [purification-ion-exchange, subdirectory-purification]
sources: [doi/10.1038##nature08156, doi/10.1038##nature12232]
verified: regex
---

# Ion-Exchange Chromatography

## Overview

Ion-exchange chromatography (IEX) is a purification method that separates proteins based on their net surface charge at a given pH. Proteins bind to oppositely charged resin beads and are eluted by increasing salt concentration or changing pH. In membrane protein biochemistry, IEX is widely used after affinity chromatography to further purify proteins and remove contaminants. It is performed in the presence of detergent to maintain membrane protein solubility and activity.

## Principle

Proteins carry a net positive or negative charge depending on the pH relative to their isoelectric point (pI). In cation-exchange chromatography, positively charged proteins bind to negatively charged resin and are eluted by increasing NaCl concentration. In anion-exchange chromatography, negatively charged proteins bind to positively charged resin. Membrane proteins are typically solubilized in detergent micelles, and IEX is performed in detergent-containing buffers to prevent aggregation and precipitation.

## Protocol

### Reagents and Materials

- Protein sample in loading buffer
- Equilibration buffer (low salt)
- Elution buffer (high salt gradient)
- Detergent (maintained at constant concentration)
- NaCl or other salt for gradient elution

### Steps

1. {'step': 'Column equilibration', 'method': 'Equilibrate ion-exchange column with starting buffer (low salt, appropriate pH)', 'notes': 'Maintain detergent at constant concentration throughout'}
2. {'step': 'Sample loading', 'method': 'Apply protein sample to equilibrated column', 'notes': 'Protein binds to resin if net charge is opposite to resin charge'}
3. {'step': 'Gradient elution', 'method': 'Elute bound proteins with increasing salt gradient (e.g., 50-500 mM NaCl)', 'notes': 'Monitor absorbance at 280 nm; collect fractions containing target protein'}
4. {'step': 'Fraction analysis', 'method': 'Analyze fractions by SDS-PAGE or other methods', 'notes': 'Pool fractions containing pure target protein'}


## Advantages

- High resolution separation based on protein charge
- Can achieve high purity in a single step
- Scalable from analytical to preparative scale
- Compatible with membrane proteins in detergent
- Gentle conditions preserve protein activity

## Disadvantages

- Requires protein to be stable in detergent
- Resolution depends on charge differences between proteins
- Detergent can interfere with binding in some cases
- May require optimization of pH and salt conditions

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [Maltose Transporter (MalFGK2)](/xray-mp-wiki/proteins/abc-transporters/maltose-transporter-malfgk2/) / EIIA^Glc | not applicable | not specified | EIIA^Glc purified by ion-exchange (Source 15Q, GE Healthcare) in 10 mM Tris-HCl pH 8.0, 200 mM NaCl; MalFGK2 purified by ion-exchange as part of complex purification in 10 mM Tris-HCl pH 8.0, 200 mM NaCl, 0.012% DDM |
| [Syntaxin-1A from rat](/xray-mp-wiki/proteins/structural-adhesion/syntaxin-1a/) | not applicable | TBA | Ion-exchange chromatography used for purification of syntaxin-1A after Ni-NTA affinity chromatography and tag removal |
| [Synaptobrevin-2 from rat](/xray-mp-wiki/proteins/structural-adhesion/synaptobrevin-2/) | not applicable | TBA | Ion-exchange chromatography used for purification of synaptobrevin-2 in presence of n-octyl beta-D-glucopyranoside |
| [SNARE complexes](/xray-mp-wiki/concepts/structural-mechanisms/snare-complex/) | not applicable | TBA | SNARE complexes separated from free monomers by ion-exchange chromatography in presence of n-octyl or n-nonyl beta-D-glucopyranoside |

## Related Methods

- [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography/) — Often used before ion-exchange chromatography in purification workflows
- [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) — Often used after ion-exchange chromatography for final polishing

## Related Reagents

- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Commonly used buffer in ion-exchange chromatography
- [Sodium Chloride (NaCl)](/xray-mp-wiki/reagents/additives/sodium-chloride/) — Used for salt gradient elution in ion-exchange chromatography
- [n-Octyl beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/og/) — Detergent used in ion-exchange purification of SNARE complexes
