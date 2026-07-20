---
title: "Molecular Replacement"
created: 2026-06-11
updated: 2026-06-11
type: method
category: methods
layout: default
tags: [structure-molecular-replacement, subdirectory-structure-determination]
sources: [doi/10.1107##s2059798322004144, doi/10.1107##s205979832001517x, doi/10.1128##jb.187.19.6804-6815.2005, doi/10.1016##j.jmb.2007.04.082, doi/10.1107##s2052252521013178, doi/10.1107##s205225252100213x, doi/10.1186##s12915-021-01102-4, doi/10.7554##eLife.34995, doi/10.1126##science.1222505, doi/10.1126##science.aad3873, doi/10.1085##jgp.201411219, doi/10.1073##pnas.240224997, doi/10.1073##pnas.2215072120, doi/10.1073##pnas.2006997117, doi/10.1073##pnas.2006526117, doi/10.1073##pnas.2016328118, doi/10.1073##pnas.1908929116, doi/10.1073##pnas.1903024116, doi/10.1073##pnas.1901822116, doi/10.1073##pnas.1114944109, doi/10.1038##s41586-018-0083-5, doi/10.1016##j.str.2012.11.010, doi/10.1021##acs.jmedchem.5b00892, doi/10.1038##NATURE12179, doi/10.1038##NATURE13293, doi/10.1038##SJ.EMBOJ.7601028, doi/10.1038##nature04508, doi/10.1038##nature10753, doi/10.1038##nature12232, doi/10.1038##nature13306, doi/10.1038##nature20606, doi/10.1038##nature22035, doi/10.1038##ncomms3911, doi/10.1073##pnas.0700979104, doi/10.1073##pnas.0706563104, doi/10.15252##embj.2020105164, doi/10.15252##embj.2020105246, doi/10.15252##embj.2021108341, doi/10.1186##s12915-015-0167-8, doi/10.1186##s12915-016-0295-9, doi/10.1074##jbc.M508926200, doi/10.1074##jbc.M608325200, doi/10.1126##science.1243352, doi/10.1085##jgp.201711884, doi/10.1074##jbc.RA118.003876, doi/10.1126##scisignal.ado8741, doi/10.1126##science.286.5445.1700, doi/10.1128##jb.00684-06, doi/10.1093##jb##mvs051, doi/10.1093##mp##ssu005, doi/10.1128##mBio.03277-19, doi/10.1107##s2053230x14024558, doi/10.1107##s2053230x1600279x]
verified: none
---

# Molecular Replacement

## Overview

Molecular replacement is an X-ray crystallographic phasing method that uses a known homologous structure as a search model to solve the phase problem. The search model is rotated and translated within the unit cell to find the orientation and position that best fits the observed diffraction data. Once phases are obtained, an electron density map is calculated and the model is iteratively refined.

## Protocol

### Steps

1. {'step': 'Search model preparation', 'description': 'A homologous structure is selected and trimmed (remove non-conserved loops, mutations, ligands, and solvent)'}
2. {'step': 'Rotation search', 'description': 'The search model is rotated in all possible orientations in the asymmetric unit to find the best fit with the Patterson map calculated from observed data'}
3. {'step': 'Translation search', 'description': 'For each promising rotation, the model is translated to find the position that best explains the observed diffraction'}
4. {'step': 'Phasing and refinement', 'description': 'Once the correct orientation and position are found, phases from the placed model are used to calculate an initial electron density map, followed by iterative model building and refinement'}


## Advantages

- Fast and computationally efficient compared to experimental phasing methods
- Does not require heavy atom derivatives or anomalous scattering data
- Works well when a closely related homologous structure is available

## Disadvantages

- Requires a suitable homologous structure (typically >30% sequence identity)
- Model bias can be a significant problem — the final model may be biased toward the search model
- May fail for novel folds or highly divergent structures
