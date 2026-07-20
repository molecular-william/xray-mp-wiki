---
title: "Selenomethionine Single-Wavelength Anomalous Dispersion (SeMet SAD) Phrasing"
created: 2026-06-02
updated: 2026-06-02
type: method
category: methods
layout: default
tags: [structure-sad, structure-refinement, subdirectory-structure-determination]
sources: [doi/10.1038##nature09487, doi/10.1038##ncomms8947, doi/10.1073##pnas.1120087109, doi/10.1073##pnas.1120113109, doi/10.1128##mBio.03277-19]
verified: none
---

# Selenomethionine Single-Wavelength Anomalous Dispersion (SeMet SAD) Phrasing

## Overview

[Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) single-wavelength anomalous dispersion (SeMet SAD) phrasing is an X-ray crystallographic phrasing method that uses [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) (SeMet)-substituted proteins to provide anomalous scatterers for structure solution. SeMet is incorporated into recombinant proteins during expression in methionine-auxotrophic E. coli strains, where selenium replaces sulfur in methionine residues. The selenium atom provides a strong anomalous signal at typical synchrotron X-ray wavelengths near the Se K-edge (~0.98 A), enabling structure solution by single-wavelength anomalous dispersion without requiring heavy-atom derivatives.

## Principle

[Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) is incorporated into recombinant proteins expressed in E. coli grown in methionine-depleted minimal media. Selenium atoms at methionine positions serve as anomalous scatterers. X-ray data collected at a wavelength near the Se K-edge (~0.98 A) yield measurable anomalous differences between Friedel pairs. These anomalous signals are used to locate selenium sites and solve the phase problem via SAD phrasing. The resulting electron density map is then used for model building and refinement.

## Protocol

### Reagents and Materials

- {'selenomethionine': '[Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) amino acid supplement', 'expression_host': 'Escherichia coli methionine-auxotrophic strain (e.g., B834, B893, L56)', 'minimal_media': 'M9 minimal medium depleted of methionine', 'induction': '[IPTG](/xray-mp-wiki/reagents/additives/iptg/) induction of SeMet-labeled protein expression'}

### Steps

1. {'step': 'Bacterial growth in SeMet media', 'description': 'Grow methionine-auxotrophic E. coli in M9 minimal medium lacking methionine'}
2. {'step': 'SeMet incorporation', 'description': 'Supplement with SeMet to replace methionine during protein expression'}
3. {'step': 'Protein purification', 'description': 'Purify SeMet-labeled protein using standard protocols'}
4. {'step': 'Crystal growth', 'description': 'Crystallize SeMet-labeled protein under same conditions as native protein'}
5. {'step': 'X-ray data collection', 'description': 'Collect anomalous diffraction data at Se absorption edge wavelength (~0.98 A)'}
6. {'step': 'Selenium site identification', 'description': 'Locate Se sites using programs such as SHELXD'}
7. {'step': 'SAD phrasing', 'description': 'Solve phases using SAD method with AUTOSHARP or similar'}
8. {'step': 'Model building and refinement', 'description': 'Build initial model and refine against SAD and native data'}


## Advantages

- No heavy-atom derivative required; SeMet substitution is straightforward
- Strong anomalous signal from selenium at synchrotron wavelengths
- Single data set sufficient for phrasing (unlike MAD)
- Works well for membrane proteins expressed in E. coli
- Selenium sites are naturally positioned at methionine residues

## Disadvantages

- Requires methionine-free protein or limited number of methionines for unambiguous site identification
- SeMet incorporation efficiency can vary between proteins
- Methionine-rich proteins may have too many Se sites, complicating phrasing
- Requires access to synchrotron radiation for optimal wavelength tuning
