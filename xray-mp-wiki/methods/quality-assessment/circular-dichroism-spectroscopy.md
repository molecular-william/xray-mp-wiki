---
title: "Circular Dichroism Spectroscopy"
created: 2026-06-02
updated: 2026-06-02
type: method
category: methods
layout: default
tags: [quality-assessment, subdirectory-quality-assessment]
sources: [doi/10.1073##pnas.2006997117, doi/10.1038##nature08156]
verified: regex
---

# Circular Dichroism Spectroscopy

## Overview

Circular dichroism (CD) spectroscopy measures the differential absorption of left- and right-circularly polarized light by chiral molecules, particularly the peptide bonds in alpha-helices and beta-sheets. In membrane protein biochemistry, CD spectroscopy is used to monitor secondary structure content, assess protein folding and stability, and determine melting temperatures (Tm) through thermal or chemical denaturation experiments. The ellipticity at 222 nm is commonly used to track alpha-helical content during unfolding transitions.

## Principle

Alpha-helical proteins exhibit characteristic CD spectra with negative bands at 208 nm and 222 nm and a positive band near 190 nm. The ellipticity at 222 nm is particularly sensitive to alpha-helical content and is widely used to monitor helix-coil transitions during thermal or chemical denaturation. By measuring the change in ellipticity at 222 nm as a function of temperature or denaturant concentration, the melting temperature (Tm) and free energy of unfolding can be determined.

## Protocol

### Reagents and Materials

- Protein sample in appropriate buffer and detergent
- [Guanidine Hydrochloride](/xray-mp-wiki/reagents/additives/guanidine-hydrochloride/) (chemical denaturant)
- Quartz cuvettes (appropriate path length)

### Steps

1. {'step': 'Sample preparation', 'method': 'Prepare protein sample in suitable buffer with detergent at appropriate concentration', 'notes': 'Use quartz cuvette with path length appropriate for protein concentration'}
2. {'step': 'Thermal unfolding', 'method': 'Record CD spectrum at 222 nm while increasing temperature at constant rate', 'notes': 'Monitor ellipticity at 222 nm as function of temperature; determine Tm from midpoint of transition'}
3. {'step': 'Chemical denaturation', 'method': 'Record CD at 222 nm at increasing concentrations of [Guanidine Hydrochloride](/xray-mp-wiki/reagents/additives/guanidine-hydrochloride/)', 'notes': 'Monitor ellipticity at 222 nm as function of denaturant concentration'}
4. {'step': 'Data analysis', 'method': 'Fit unfolding transitions to sigmoidal curves to determine Tm or free energy of unfolding', 'notes': 'Experiments performed in triplicate; data normalized to molar ellipticity'}


## Advantages

- Direct measurement of secondary structure content
- Requires relatively small amounts of protein
- Can monitor thermal and chemical denaturation
- Works with membrane proteins in detergent solution
- Provides quantitative Tm values for comparing stability

## Disadvantages

- Detergent absorption in far-UV range can interfere with measurements
- Requires optically clear samples (no turbidity)
- Limited to proteins with sufficient secondary structure signal
- Cuvette path length must be optimized for sample concentration

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [Syntaxin-1A (Rat Neuronal Qa-SNARE Protein)](/xray-mp-wiki/proteins/structural-adhesion/syntaxin-1a/)/SNAP-25A/Synaptobrevin-2 [SNARE Complex](/xray-mp-wiki/concepts/structural-mechanisms/snare-complex/) | not applicable | [TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/) | Thermal and chemical unfolding of neuronal SNARE complexes monitored by CD spectroscopy at 222 nm; crystallization complex unfolded at approximately 97 C |

## Related Methods

- [Thermal Shift Assay (Fluorescent CPM)](/xray-mp-wiki/methods/quality-assessment/thermal-shift-assay/) — Alternative method for measuring protein thermal stability

## Related Reagents

- [Guanidine Hydrochloride](/xray-mp-wiki/reagents/additives/guanidine-hydrochloride/) — Chemical denaturant used in CD chemical unfolding experiments
- [Dithiothreitol (DTT)](/xray-mp-wiki/reagents/additives/dtt/) — Reducing agent used in protein samples for CD spectroscopy
- [beta-Mercaptoethanol](/xray-mp-wiki/reagents/additives/mercaptoethanol/) — Reducing agent used in protein samples for CD spectroscopy
