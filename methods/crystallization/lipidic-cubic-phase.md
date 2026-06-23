---
title: Lipidic Cubic Phase Crystallization
created: 2026-05-04
updated: 2026-06-16
type: method
category: methods
layout: default
tags: [crystallization-lcp, subdirectory-crystallization]
sources: [doi/10.1002##1873-3468.14136, doi/10.1006##jmbi.1999.3027, doi/10.1016##S0022-2836(02)00681-2, doi/10.1016##S0022-2836(03)00751-4, doi/10.1016##j.cell.2015.04.011, doi/10.1016##j.cell.2015.04.045, doi/10.1016##j.cell.2015.06.002, doi/10.1016##j.cell.2016.09.056, doi/10.1016##j.cell.2018.12.006, doi/10.1016##j.cell.2020.01.008, doi/10.1016##j.jbc.2021.100479, doi/10.1016##j.jmb.2011.04.038, doi/10.1016##j.jmb.2011.06.028, doi/10.1016##j.jmb.2020.05.017, doi/10.1016##j.str.2014.08.022, doi/10.1016##j.str.2016.04.003, doi/10.1016##j.str.2017.07.009, doi/10.1016##j.str.2018.01.005, doi/10.1021##acs.jmedchem.5b00892, doi/10.1021##bi900545e, doi/10.1021##jacs.8b06741, doi/10.1038##NATURE01109, doi/10.1038##NATURE12179, doi/10.1038##NSMB.2894, doi/10.1038##nature10753, doi/10.1038##nature12357, doi/10.1038##nature13083, doi/10.1038##nature14549, doi/10.1038##nature14656, doi/10.1038##nature20606, doi/10.1038##nature22035, doi/10.1038##ncomms15103, doi/10.1038##ncomms4309, doi/10.1038##ncomms8895, doi/10.1038##s41467-018-03477-5, doi/10.1038##s41467-018-07939-8, doi/10.1074##jbc.m112.415091, doi/10.1107##s205979832001517x, doi/10.1107##s2059798322004144, doi/10.1126##scisignal.ado8741, doi/10.7554##eLife.34995]
verified: false
---

# Lipidic Cubic Phase Crystallization

## Overview

Lipidic cubic phase (LCP) crystallization, also known as the in meso method, is a membrane protein crystallization technique where the protein is embedded in a bicontinuous lipid cubic mesophase (typically monoolein-based) that acts as a native-like membrane environment. The protein-lipid mixture is deposited in wells containing precipitant solution, and crystallization occurs as water diffuses across the lipid bilayer, concentrating the protein within the mesophase. LCP has been particularly successful for GPCRs, transporters, and transmembrane peptide complexes.

## Protocol

### Reagents and Materials

- {'name': '[Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) (9.9 [MAG](/xray-mp-wiki/reagents/lipids/mag/))', 'amount': 'Typically used as the lipid for LCP formation'}
- {'name': 'Protein solution', 'amount': 'Typically mixed with lipid at 2:3 or 3:2 protein-to-lipid ratio (v/v)'}

### Steps

1. {'step': 'LCP formation', 'description': 'Lipid and protein solution are mixed in a coupled syringe device to form a viscous, transparent cubic mesophase'}
2. {'step': 'Dispensing', 'description': 'The LCP bolus is dispensed into a glass sandwich plate or 96-well LCP glass plate'}
3. {'step': 'Overlay with precipitant', 'description': 'Precipitant solution is dispensed over the LCP bolus in each well'}
4. {'step': 'Incubation', 'description': 'The plate is sealed and incubated at a controlled temperature (typically 20°C) for crystal growth, which may take days to weeks'}


## Advantages

- Provides a native-like lipid bilayer environment for membrane proteins
- Particularly successful for GPCRs and other difficult-to-crystallize membrane proteins
- Reduces protein mobility and stabilizes conformational states
- Compatible with room-temperature and low-temperature data collection

## Disadvantages

- Requires specialized equipment (coupled syringe device, LCP glass plates)
- Crystal harvesting can be technically challenging
- Limited to relatively small volumes and sample amounts
- Not suitable for all membrane protein types

## Proteins Using This Method

| Protein | Resolution | PDB | Notes |
|---|---|---|---|
| [Bacteriorhodopsin](/xray-mp-wiki/proteins/Bacteriorhodopsin/) | 1.55 | 1C3W | First membrane protein structure solved by CLP method; atomic resolution. |
| [Rhodobacter sphaeroides reaction centre](/xray-mp-wiki/proteins/Rhodobacter sphaeroides reaction centre/) | 2.35 | 1ogv | First type I crystal packing for a purple bacterial reaction centre; cardiolipin-mediated crystal contacts identified. |
| [Blastochloris viridis Photosynthetic Reaction Center (RC_vir)](/xray-mp-wiki/proteins/Blastochloris viridis Photosynthetic Reaction Center (RC_vir)/) | 1.86 | 2WJM | LSP-grown (lipidic sponge phase variant of LCP) crystals revealing diacylglycerol modification, monoolein at QB site, and 36 Å lipid feature. Type I crystal packing, no membrane-plane crystal contacts. |
| [Human GPR40 Receptor (FFAR1)](/xray-mp-wiki/proteins/Human GPR40 Receptor (FFAR1)/) | 2.3 | 4PHU | First GPCR structure of the free fatty-acid receptor 1. TAK-875 (fasiglifam) bound to a non-canonical allosteric pocket. T4L fusion in ICL3. 2.3 A structure solved by molecular replacement. |
| [Human OX2 Orexin Receptor (OX2R)](/xray-mp-wiki/proteins/Human OX2 Orexin Receptor (OX2R)/) | 2.5 | 4S0V | First structure of the human OX2 orexin receptor. Suvorexant (Belsomra) bound in orthosteric pocket. Novel PGS fusion chimera in ICL3. 2.5 A structure solved by molecular replacement. |
