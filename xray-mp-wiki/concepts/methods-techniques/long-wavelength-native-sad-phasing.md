---
title: "Long-Wavelength Native-SAD Phasing"
created: 2026-06-08
updated: 2026-06-08
type: concept
category: concepts
layout: default
tags: [concept-crystallography-principle, membrane-protein, subdirectory-methods-techniques]
sources: [doi/10.1038##s42004-023-01014-0, doi/10.1107##s205225252200971x]
verified: regex
---

# Long-Wavelength Native-SAD Phasing

## Overview
Long-wavelength native-SAD phasing is an experimental X-ray crystallographic phasing technique that exploits the anomalous scattering of naturally occurring light atoms (sulfur, phosphorus, chlorine, potassium, calcium, vanadium, cadmium, iodine) at X-ray wavelengths beyond the typical synchrotron range (lambda = 1.1-5.9 A). By accessing the K-edges of biologically important lighter atoms and the L-edges of heavier elements, this method enables experimental phasing without the need for [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) labeling or heavy atom derivatization.

## Mechanism/Details
The method is based on the principle that the anomalous scattering factor f''
increases as the X-ray wavelength approaches the absorption edge of an element.
For native-SAD, the most commonly exploited element is sulfur (S K-edge at
lambda = 5.02 A), which is naturally present in cysteine and methionine residues.
At the Diamond Light Source beamline I23, operating at wavelengths up to
lambda = 5.9 A, absorption edges of multiple elements become accessible: K-edges
of P, S, Cl, K, Ca, V, Cr, Mn, Fe, Co, Ni, Cu, Zn; L-edges of I, Cd, Ag, Pb;
and M-edges of Pb, Hg, Au, Pt.

The I23 beamline overcomes three major technical challenges of long-wavelength
crystallography: (1) X-ray absorption by the crystal, sample holder, and
surrounding materials is minimized by an in-vacuum endstation with the
sample maintained at cryogenic temperatures (<55 K) via thermal conductance
and pulse-tube coolers; (2) detector background noise is reduced by operating
all Pilatus 12 M modules in vacuum with ultra-high gain settings at a threshold
of 1.8 keV; (3) the semi-cylindrical detector geometry covers 2Theta = 40.3
degrees with +/-100 degrees along the cylinder axis.

The optimal wavelength for S-SAD on I23 was determined to be lambda = 2.75 A
(f'' = 1.6 e-), balancing increased anomalous signal against absorption effects.
A typical data collection strategy requires 3 x 360 degrees of data from a
single crystal taken at multiple orientations using a multi-axis goniometer
with a flux of ~2 x 10^10 photons s-1 from a non-focused beam matching crystal
size. The number of datasets required for structure solution is determined in
real-time by evaluating substructure solution success and secondary structure
identification in electron density maps.

A key metric for predicting S-SAD success on I23 at lambda = 2.75 A is the
ratio of unique acentric reflections to the number of anomalous scatterers.
A ratio over 1000 typically ensures successful phasing, corresponding to 89%
of deposited PDB structures. A web app (Yosoku-I23 Resolution Requirement
for Phasing) is available to predict required resolution based on space group,
unit cell parameters, and sulfur content.

For crystals with non-uniform shapes, two approaches mitigate absorption
artifacts: (1) analytical absorption correction using X-ray tomography to
measure sample shape and path lengths; (2) laser crystal shaping using a
deep-UV laser (193 nm, 1 ns pulse) to machine crystals into uniform spheres
or cylinders, which also allows selection of smaller crystals that absorb
less X-rays at long wavelengths.

## Examples in Membrane Protein Work
- [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/) (RND multidrug efflux pump) — Solved by S-SAD on I23 at 3.4 A resolution with 45 sulfur atoms and a unique reflections/scatterers ratio of 650. Required five datasets of 360 degrees each from a single crystal (multiplicity 86.9) due to non-isomorphism.
- [A2AR](/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/) (human adenosine A2A receptor, GPCR) — A single crystal of 20x20x5 um collected 18,000 images at I23, sufficient for successful S-SAD phasing. Demonstrates applicability to GPCRs with limited crystal availability.
- SERCA (P-type ATPase) — Solved by V-SAD using a single vanadium atom bound as reaction mechanism inhibitor (VO3-). 110 kDa membrane protein diffracting to 3.1 A resolution. Demonstrates use of non-physiological elements in protein ligands.
- NaK2K (K+ selective transporter) — Solved by K-SAD (potassium K-edge at 3.43 A) with four K+ ions in the selectivity filter. Demonstrates phasing using physiological K+ ions without any exogenous heavy atoms.
- OmpK36 (beta-barrel porin) — Laser-shaped cylindrical crystals collected at lambda = 4.13 A for S-SAD phasing. Six datasets of 360 degrees from a single crystal (multiplicity 22.3) at 2.7 A resolution (detector limited).
- BphA4 (NADH-dependent ferredoxin reductase) — Laser-shaped spherical crystal collected at the phosphorus edge (lambda = 5.76 A) on I23. Two phosphorus atoms of [FAD](/xray-mp-wiki/reagents/additives/flavin-adenine-dinucleotide/) were sufficient for P-SAD phasing at 3.7 A resolution despite low multiplicity (12). The two closely spaced phosphorus atoms behaved as a super-phosphorus with anomalous peak height of 39.7 sigma.
- AlgE (beta-barrel membrane protein) — Solved by combined S-SAD and Ca-SAD. Crystallized in C2 space group with 6 sulfur and 2 calcium atoms. Required merging datasets from 2 crystals (7 x 360 degrees) with multiplicity 26.7 for interpretable maps.

## Related Concepts


## Cross-References
- [Single-Wavelength Anomalous Diffraction](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — Long-wavelength native-SAD is a specific application of the SAD technique
- [Multi-Wavelength Anomalous Diffraction](/xray-mp-wiki/methods/structure-determination/multi-wavelength-anomalous-diffraction/) — Alternative phasing method that also exploits anomalous scattering
- [SeMet SAD Phasing](/xray-mp-wiki/methods/structure-determination/semet-sad-phasing/) — Standard SAD phasing method using selenomethionine labeling, contrast with native-SAD
- [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/) — Related protein structure
- [A2AR](/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/) — Related protein structure
- [FAD](/xray-mp-wiki/reagents/additives/flavin-adenine-dinucleotide/) — Additive used in purification or crystallization buffers
- [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) — Additive used in purification or crystallization buffers
