---
title: Multi-Wavelength Anomalous Diffraction
created: 2026-05-28
updated: 2026-05-28
type: method
category: methods
layout: default
tags: [structure-mad, structure-xray, subdirectory-structure-determination]
sources: [doi/10.1074##jbc.M114.622688, doi/10.1016##j.str.2005.11.015, doi/10.1038##NATURE10963, doi/10.1038##ncomms8947]
verified: false
---

# Multi-Wavelength Anomalous Diffraction

## Overview

Multi-wavelength anomalous diffraction (MAD) is an X-ray crystallographic phasing method that exploits the anomalous scattering of atoms at multiple wavelengths near their absorption edge. By collecting diffraction data at several wavelengths, MAD provides both anomalous and dispersive differences that can be used to locate anomalous scatterers and calculate phases. MAD is particularly powerful when using selenomethionine-labeled protein, as selenium provides a strong anomalous signal at synchrotron beamlines. MAD can also be applied to heavy atom derivatives (e.g., osmium tetroxide, platinum compounds, tantalum clusters) to solve membrane protein structures.

## Principle

In MAD phasing, diffraction data are collected at multiple wavelengths across the absorption edge of an anomalous scatterer (typically selenium in Se-Met labeled protein). At the peak wavelength, the imaginary component of the anomalous scattering factor (f'') is maximized, providing strong anomalous differences. At the inflection point, the real component (f') changes most rapidly, providing dispersive differences. These differences between measurements at different wavelengths allow unambiguous determination of the positions of anomalous scatterers and calculation of phases without requiring isomorphous heavy-atom derivatives.

## Protocol

### Reagents and Materials

- {'selenomethionine_labeled_protein': 'Protein expressed in methionine-auxotrophic E. coli strain grown in minimal media supplemented with selenomethionine (Se-Met) as the methionine substitute. Se-Met incorporation replaces methionine residues throughout the protein, providing multiple anomalous scatterers.'}
- {'native_protein': 'Unlabeled protein for comparison or for data collection at a remote wavelength.'}

### Steps

1. {'step': 'Se-Met protein preparation', 'description': 'Express protein in methionine-auxotrophic E. coli (e.g., B834 DE3) grown in M9 minimal media supplemented with methionine and selenomethionine. Pre-induction with methionine for 15 min before Se-Met addition improves incorporation efficiency.'}
2. {'step': 'Crystal preparation', 'description': 'Grow Se-Met labeled protein crystals under the same conditions as native crystals. The crystals should be isomorphous with native crystals for best results.'}
3. {'step': 'Data collection', 'description': "Collect diffraction data at multiple wavelengths (typically 3) across the selenium absorption edge at a synchrotron beamline. Common wavelengths: peak (f'' maximum, ~0.979 A), inflection (f' minimum, ~0.9795 A), and remote (~1.000 A). Inverse beam or oscillation data collection is used."}
4. {'step': 'Phasing', 'description': 'Process data with programs like HKL2000 or XDS. Use MAD phasing programs such as SHARP, SHELXL, or PHENIX AUTOSOL to locate selenium sites and calculate initial phases. Multiple wavelengths provide both anomalous and dispersive information for more reliable phasing.'}
5. {'step': 'Model building', 'description': 'Use the calculated phases to generate electron density maps. Programs like AUTOBUILD (PHENIX) can automatically build a significant portion of the polypeptide chain. Remaining model is completed manually using COOT.'}


## Advantages

- Multiple wavelengths provide both anomalous and dispersive differences
- More robust phasing than single-wavelength methods
- No need for isomorphous heavy-atom derivatives
- Se-Met labeling is well-established and reliable
- Works well with synchrotron radiation and tunable beamlines

## Disadvantages

- Requires Se-Met labeled crystals (additional expression/purification step)
- Requires synchrotron beamline access with tunable wavelength
- Multiple data sets needed (one per wavelength)
- May fail for small proteins with few methionine residues
- Radiation damage can reduce anomalous signal during data collection

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [AcrA multidrug efflux pump periplasmic protein](/xray-mp-wiki/proteins/abc-transporters/acra/) | 2.71 A | 2HJ9 | Crystals of AcrA(45-312)-4M (quadruple methionine mutant) collected at three wavelengths (0.97938 A, 0.97955 A, 0.96415 A) at APS-BM19 and one wavelength (1.000 A) at ALS-8.2.2. 16 Se sites located with SHELXL, refined with SHARP. Structure refined to 2.71 A resolution with R_work 23.7% and R_free 27.5%. |
| [VrH+PPase (Vigna radiata H+-Pumping Inorganic Pyrophosphatase)](/xray-mp-wiki/proteins/pumps-atpases/vrh-ppase/) | 2.6 A | TBA | Ta6Br12 (tantalum bromide cluster) derivative collected at NSRRC BL13B1 at three wavelengths: peak (1.2545 A), inflection (1.2548 A), remote (1.2299 A) at the Tl LIII absorption edge. 10 Ta sites located. Used MAD phasing to solve the structure. Space group C2. Cell dimensions: a=218.6, b=88.2, c=162.1. |

## Related Methods

- [Single-Wavelength Anomalous Diffraction (SAD)](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — Related phasing method using a single wavelength at the absorption edge
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Alternative phasing method when a homologous structure is available

## Related Reagents

- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — Primary anomalous scatterer used in MAD phasing of Se-Met labeled protein
