---
title: "Sf9 Insect Cell Expression System"
created: 2026-05-29
updated: 2026-05-29
type: method
category: methods
layout: default
tags: [expression-system, subdirectory-expression-systems]
sources: [doi/10.1016##j.str.2017.11.005, doi/10.1073##pnas.2024651118]
verified: regex
---

# Sf9 Insect Cell Expression System

## Overview

The Sf9 insect cell expression system uses Spodoptera frugiperda (fall armyworm) ovarian cells for recombinant protein production via baculovirus infection. It is one of the most widely used expression systems for membrane proteins, particularly GPCRs, due to its ability to perform eukaryotic post-translational modifications and produce properly folded membrane proteins. The Bac-to-Bac system (Invitrogen) or BestBac system (Expression Systems) are commonly used for baculovirus generation. Typical infection density is 2-4 x 10^6 cells/ml, harvested 48 hours post-infection at 27 degrees Celsius.

## Protocol

### Reagents and Materials

- Sf9 cells (Invitrogen or Expression Systems)
- Bac-to-Bac or BestBac baculovirus expression system
- Sf900 II or ESF 921 insect cell culture medium
- Fetal bovine serum (optional)
- Penicillin/streptomycin

### Steps

1. {'step': 'Plasmid preparation', 'description': 'Clone target gene into baculovirus transfer vector (e.g., pFastBac1, pVL1393) with appropriate signal sequence and tags'}
2. {'step': 'Bacmid generation', 'description': 'Transform transfer vector into DH10Bac competent cells for bacmid production using Bac-to-Bac system'}
3. {'step': 'Sf9 cell infection', 'description': 'Infect Sf9 cells at 2-4 x 10^6 cells/ml with recombinant baculovirus at MOI of 0.1-5'}
4. {'step': 'Expression', 'description': 'Grow infected cells at 27 degrees Celsius for 48 hours'}
5. {'step': 'Harvest', 'description': 'Collect cells by centrifugation, wash, and store at -80 degrees Celsius'}

