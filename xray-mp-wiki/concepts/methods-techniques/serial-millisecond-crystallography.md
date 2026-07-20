---
title: "Serial Millisecond Crystallography (SMX)"
created: 2026-06-16
updated: 2026-06-16
type: concept
category: concepts
layout: default
tags: [concept-crystallography-principle, xray-crystallography, subdirectory-methods-techniques]
sources: [doi/10.1038##s41467-017-00630-4]
verified: regex
---

# Serial Millisecond Crystallography (SMX)

## Overview
Serial millisecond crystallography (SMX) is a room-temperature crystallographic method that combines high-viscosity sample injectors with high frame-rate detectors at synchrotron beamlines to distribute the X-ray radiation dose over thousands of microcrystals. SMX enables routine room-temperature structure determination without the severe radiation damage that limits conventional rotation-method data collection at ambient temperature. Unlike serial femtosecond crystallography (SFX) at X-ray free-electron lasers, SMX cannot outrun radiation damage by the diffraction-before-destruction principle, but it can mitigate damage by spreading the dose across many crystals. Using a crystal scanning approach with a micro-focused beam, high-viscosity injector, and detectors operating at 50 Hz or higher, SMX can produce complete datasets from 1,000–10,000 diffraction patterns, collected in as little as 3–82 minutes.


## Mechanism/Details
In SMX, crystals embedded in a viscous delivery medium (typically lipidic cubic phase, LCP) are extruded through a nozzle at controlled speed (e.g., 250 µm/s) as a continuous stream. A micro-focused X-ray beam intersects the stream, and a high-frame-rate detector (e.g., EIGER 16M at 50 Hz, PILATUS3 at 10 Hz) records diffraction patterns continuously (shutterless). The jet speed is matched to the beam width so that each crystal traverses one beam width per frame, allowing collection of multiple diffraction patterns per crystal without re-exposing the same portion. Typical parameters include: beam size 5×5 to 20×5 µm², 50 µm nozzle diameter, LCP or other viscous carrier medium. The small beam reduces background and improves signal-to-noise. Data processing uses software suites such as CrystFEL (indexamajig, partialator) to index, integrate, and merge patterns from thousands of individual crystal snapshots. For molecular replacement, data converges rapidly (1,000–10,000 patterns). For de novo phasing by native single-wavelength anomalous dispersion (native-SAD), approximately 140,000–240,000 patterns may be needed.


## Examples in Membrane Protein Work
- [Molybdenum Storage Protein](/xray-mp-wiki/proteins/gpcr/molybdenum-storage-protein/) — High-resolution (1.3 Å) SMX structure of the radiation-sensitive MOSTO, demonstrating that SMX can determine structures of radiation-sensitive metalloproteins at room temperature with minimal damage.
- [Human Adenosine A2A Receptor (A2AR)](/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/) — SMX structure of thermostabilized A2AR at 2.1 Å resolution, enabling native-SAD phasing in under 5 hours. Comparison with SFX (1.7 Å) and cryo-crystallography (1.95 Å) data demonstrated comparable quality.
- [Tubulin-DARPin Complex (TD1)](/xray-mp-wiki/proteins/gpcr/tubulin-darpin-complex-td1/) — Ligand soaking with colchicine into pre-formed TD1 crystals demonstrated SMX for structure-based drug design. Data convergence for ligand detection reached 90% of final SA-omit map cross-correlation in 3–35 minutes.

## Related Concepts
- [Serial Femtosecond Crystallography (SFX)](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) — SMX is the synchrotron-based analog of SFX, using the same injector technology but with longer (millisecond) exposures and multi-pattern-per-crystal data collection.
- [High-Viscosity Sample Injection for SFX](/xray-mp-wiki/concepts/methods-techniques/high-viscosity-sample-injection-for-sfx/) — The high-viscosity injectors developed for SFX are directly adapted for SMX.
- [In Situ Crystallography](/xray-mp-wiki/concepts/methods-techniques/in-situ-crystallography/) — Related room-temperature crystallography approach.
- [Lipidic Cubic Phase (LCP)](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) — LCP is the standard delivery medium for SMX, accommodating both soluble and membrane protein crystals.
- [Native SAD Phasing](/xray-mp-wiki/concepts/methods-techniques/long-wavelength-native-sad-phasing/) — SMX data quality enables native-SAD phasing using sulfur anomalous scattering.

## Cross-References
- [Molybdenum Storage Protein (MOSTO)](/xray-mp-wiki/proteins/gpcr/molybdenum-storage-protein/) — Key SMX application demonstrating radiation-damage-free structure of a metalloprotein.
- [Human Adenosine A2A Receptor (A2AR)](/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/) — SMX structure of a GPCR pharmaceutical target; native-SAD phasing at room temperature.
- [Tubulin-DARPin Complex (TD1)](/xray-mp-wiki/proteins/gpcr/tubulin-darpin-complex-td1/) — Ligand soaking and fragment screening using SMX.
