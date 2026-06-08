---
title: Selenomethionine (SeMet)
created: 2026-06-08
updated: 2026-05-29
type: reagent
category: reagents
layout: default
tags: [additive-stabilizer, subdirectory-additives]
sources: [doi/10.1002##pro.215, doi/10.1016##j.str.2014.06.008, doi/10.1016##j.str.2016.04.003, doi/10.1038##NATURE07819, doi/10.1038##NATURE11683, doi/10.1038##NATURE12179, doi/10.1038##nature11744, doi/10.1038##nsmb.3049]
verified: false
---

# Selenomethionine (SeMet)

## Overview

Selenomethionine (SeMet) is a selenium-containing analog of the amino acid methionine. It is widely used in protein crystallography for experimental phasing via selenomethionine single-wavelength anomalous diffraction (Se-SAD) or multi-wavelength anomalous diffraction (Se-MAD). SeMet is incorporated into recombinant proteins during expression in methionine-auxotrophic E. coli strains grown in minimal media lacking methionine, where SeMet replaces Met in the growing polypeptide chain. The selenium atom provides a strong anomalous signal at typical synchrotron X-ray wavelengths (~0.98 A), enabling structure solution without requiring heavy-atom derivatives.


## Properties

- **Chemical name**: selenomethionine
- **Molecular weight**: 196.08 g/mol
- **Class**: selenium-containing amino acid analog

## Use in Membrane Protein Work

### Experimental phasing in protein crystallography (Se-SAD/Se-MAD)

SeMet-labeled proteins provide selenium atoms that serve as anomalous scatterers. At a wavelength of ~0.98 A (near the Se K-edge), the selenium atoms produce strong anomalous signals suitable for SAD or MAD phasing. This approach is widely used when no homologous structure is available for molecular replacement.


### Methionine residue mapping

SeMet substitution allows identification of methionine positions in the electron density map, aiding in chain tracing and model building.


## Examples from This Wiki

| Protein | Concentration | Context | Result |
|---|---|---|---|
| vp-zntb | not specified | SeMet-substituted Vp-ZntB cytoplasmic domain used for Se-SAD phasing. Data collected at Se absorption edge (0.9793 A peak, 0.9795 A inflection) yielded 30 Se atoms per asymmetric unit (6 per monomer x 5 monomers).
 | Structure solved at 2.10 A resolution (Se-SAD) and 1.90 A (native data). 30 Se atoms and 25 Cl- ions per pentamer identified in anomalous maps.
 |
| [bcMalT (Bacillus cereus Maltose Transporter)](/xray-mp-wiki/proteins/bc-malt/) | not specified | Selenomethionine-derivatized bcMalT EIIC domain expressed in E. coli grown in SeMet-containing minimal media. 15 of 16 selenium sites identified by SHELXD and used for SAD phasing with AUTOSHARP. Data collected at 0.9787 A wavelength.
 | Structure solved at 2.55 A resolution (PDB 5IWS) by Se-SAD method |
| betp | not specified | SeMet-substituted BetP Delta N29 (Corynebacterium glutamicum Na+/betaine symporter) expressed in E. coli for Se-SAD phasing. Data collected at 0.9794 A wavelength (peak). The structure was solved at 3.35 A resolution (PDB 3JEO) with space group P212121. Selenium sites were identified and used for SAD phasing with SHARP/autoSHARP.
 | Structure solved at 3.35 A resolution (Se-SAD) with 11,737 total atoms (11,353 protein, 384 ligand/ion). Rwork/Rfree: 25.68/26.49.
 |
| [Aquifex aeolicus TatC](/xray-mp-wiki/proteins/tatc/) | not specified | Selenomethionine-substituted TatC expressed in E. coli L56 cells grown in M9 minimal medium using feedback inhibition of methionine biosynthesis. Four SeMet-labeled crystals were frozen directly in mother liquor and data collected at Diamond light source (Beamline I04-1) at 0.92 A wavelength. Crystals diffracted to 3.5 A resolution (space group H32).
 | Structure solved by single-wavelength anomalous dispersion (SAD) with Molprobity Score 3.1 (84th percentile for structures 3.5 A +/- 0.25 A) |
| Diacylglycerol Kinase (DgkA) | not specified | Se-Met labeled Delta7 DgkA expressed in methionine auxotroph B893(DE3) strain in M9 minimal media supplemented with Se-Met. Selenium incorporation verified by mass spectrometry. Se-Met SAD phasing used to solve the 2.05 A Delta7 structure.
 | First crystal structure of DgkA solved by Se-Met SAD phasing; wild-type and Delta4 structures solved by molecular replacement using Delta7 as search model |

## Advantages and Disadvantages

No advantages/disadvantages recorded.

## Comparison with Related Reagents

No comparison data available.

## Cross-References

- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Related reagent used in protein purification workflows
- [2-Methyl-2,4-pentanediol (MPD)](/xray-mp-wiki/reagents/additives/mpd/) — Common crystallization additive, often used with SeMet structures
- [Single-Wavelength Anomalous Diffraction (SAD)](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) — Primary phasing method using SeMet labels
