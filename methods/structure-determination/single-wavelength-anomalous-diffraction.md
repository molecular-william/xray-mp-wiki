---
title: Single-Wavelength Anomalous Diffraction
created: 2026-05-27
updated: 2026-06-02
type: method
category: methods
layout: default
tags: [structure-sad, structure-xray, subdirectory-structure-determination]
sources: [doi/10.1016##j.jmb.2007.11.080, doi/10.1038##NATURE10963, doi/10.1038##NATURE11683, doi/10.1038##NATURE12179, doi/10.1038##nature04508, doi/10.1038##nature06163, doi/10.1038##nsmb.2417]
verified: false
---

# Single-Wavelength Anomalous Diffraction

## Overview

Single-wavelength anomalous diffraction (SAD) is an X-ray crystallographic phasing method that exploits the anomalous scattering of atoms at a single wavelength near their absorption edge. SAD is one of the most widely used experimental phasing methods, particularly when selenomethionine (Se-Met) labeled protein is used, as selenium provides a strong anomalous signal at the wavelength of a typical synchrotron beamline. SAD can also be applied to heavy atom derivatives such as osmium tetroxide, platinum compounds, and mercury derivatives.

## Protocol

### Reagents and Materials

- {'selenomethionine_labeled_protein': 'Protein expressed in methionine-auxotrophic E. coli strain grown in minimal media supplemented with selenomethionine (Se-Met) as the methionine substitute. Se-Met incorporation replaces methionine residues throughout the protein, providing multiple anomalous scatterers.'}
- {'native_protein': 'Unlabeled protein for data collection at a second wavelength (if using multi-wavelength SAD, though single-wavelength SAD uses only the Se-Met data).'}

### Steps

1. {'step': 'Se-Met protein preparation', 'description': 'Express protein in methionine-auxotrophic E. coli (e.g., B834 DE3) grown in M9 minimal media supplemented with methionine and selenomethionine. Pre-induction with methionine for 15 min before Se-Met addition improves incorporation efficiency. Typical Se-Met supplement: 60 mg/L.'}
2. {'step': 'Crystal preparation', 'description': 'Grow Se-Met labeled protein crystals under the same conditions as native crystals. The crystals should be isomorphous with native crystals for best results.'}
3. {'step': 'Data collection', 'description': 'Collect anomalous diffraction data at the peak wavelength of the selenium absorption edge (typically ~0.979 A at a synchrotron beamline). Data should have sufficient anomalous signal (anomalous correlation > 20% at high resolution) for successful phasing.'}
4. {'step': 'Phasing', 'description': 'Process data with programs like HKL2000 or XDS. Use SAD phasing programs such as HKL2MAP, SHELXD, or AUTOSOL (within PHENIX) to locate selenium sites and calculate initial phases. Typical success requires 2-4 selenium sites per asymmetric unit for a moderate-sized protein.'}
5. {'step': 'Model building', 'description': 'Use the calculated phases to generate electron density maps. Programs like AUTOBUILD (PHENIX) can automatically build approximately 80% of the polypeptide chain. Remaining model is completed manually using COOT.'}


## Advantages

- Requires only one data set (single wavelength)
- Se-Met labeling is well-established and reliable
- Automation-friendly (HKL2MAP, PHENIX AUTOSOL)
- No need for heavy atom derivatization
- Works well with synchrotron radiation

## Disadvantages

- Requires Se-Met labeled crystals (additional expression/purification step)
- May fail for small proteins with few methionine residues
- Radiation damage can reduce anomalous signal during data collection
- Requires synchrotron beamline access

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [Signal Peptide Peptidase A from Escherichia coli (SppA_EC)](/xray-mp-wiki/proteins/sppa-ec/) | 2.6 A | 3BF0 | Se-Met incorporated SppA_EC delta2-46 crystals collected at NSLS beamline X4A at peak wavelength 0.97925 A. Structure solved with HKL2MAP and PHENIX AUTOSOL. Four molecules in the asymmetric unit (P2_1 space group). |
| [E. coli YbgH Peptide Transporter](/xray-mp-wiki/proteins/ybgH/) | 3.4 A | 4Q65 | Se-Met labeled YbgH crystals solved by SAD phasing. Also tested mercury derivative (C9H9O2HgNaS) for additional phasing information. Space group P21212. |
| [VrH+PPase (Vigna radiata H+-Pumping Inorganic Pyrophosphatase)](/xray-mp-wiki/proteins/vrh-ppase/) | 2.8 A | TBA | OsO4 derivative collected at NSRRC BL13C1 at peak wavelength 0.9762 A. 2 Os sites located with phasing power iso/ano of 0.55/0.44. Orange-Pt derivative with 4 Pt sites (phasing power 0.61/0.19). Both derivatives used SAD phasing. Space group C2. |
| [Aquifex aeolicus TatC](/xray-mp-wiki/proteins/tatc/) | 3.5 A | TBD | Se-Met substituted TatC expressed in E. coli L56 cells using feedback inhibition of methionine biosynthesis. Four crystals collected at Diamond light source (Beamline I04-1) at 0.92 A wavelength. Crystals belonged to space group H32. Data phased by SAD with Molprobity Score 3.1 (84th percentile). |
| [Diacylglycerol Kinase (DgkA)](/xray-mp-wiki/proteins/Diacylglycerol Kinase (DgkA)/) | 2.05 A | not specified in paper | Se-Met labeled Delta7 DgkA expressed in B893(DE3) methionine auxotroph strain in M9 minimal media supplemented with Se-Met. SAD phasing used to solve the Delta7 structure; wild-type and Delta4 structures solved by molecular replacement using Delta7 as search model. |
| [NaK Channel from Bacillus cereus](/xray-mp-wiki/proteins/nak-channel/) | 2.4 A | 2NKA | Na+ bound NaK structure solved by SIRAS (Single Isomorphous Replacement with Anomalous Scattering) using a mercury derivative. Hg binding sites determined with SHELXD and initial phases improved by solvent flattening. Data collected at Advanced Photon Source (APS) and processed with HKL2000. R_work 23.5%, R_free 26.0%. |
| [Chicken Acid-Sensing Ion Channel 1a (cASIC1a)](/xray-mp-wiki/proteins/asic1a/) | 1.9 A | 3HV4 | Se-Met labeled chicken delta ASIC1 (residues 147-526) crystals solved by SAD phasing at peak wavelength 0.97957 A. Space group P2_1. Resolution 50-3.0 A (outer shell 3.11-3.00 A). Completeness 95.8% (76.8% outer shell). Additional platinum and bromine derivatives collected for complementary phasing. |
| [HmuUV](/xray-mp-wiki/proteins/hmuuv/) | 3.0 A | not specified | SIRAS (Single-Wavelength Anomalous Diffraction) phasing using two mercury derivatives: EMP (ethylmercaptopyrimidine) and EMTS (sodium ethylmercurythiosalicylate). Data collected on native and derivative crystals in P2_1 space group. Diffraction data anisotropic: 3.0 A best, 3.2 A worst direction. |

## Related Methods

- [Multi-Wavelength Anomalous Diffraction (MAD)](/xray-mp-wiki/methods/structure-determination/multi-wavelength-anomalous-diffraction/) — Related phasing method using multiple wavelengths at the absorption edge
- [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) — Alternative phasing method when a homologous structure is available

## Related Reagents

- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — Primary anomalous scatterer used in SAD phasing
