---
title: Bac-to-Bac Baculovirus Expression System
created: 2026-06-22
updated: 2026-06-22
type: method
category: methods
layout: default
tags: [subdirectory-expression-systems, expression-system]
sources: [doi/10.1038##nprot.2011.344]
verified: false
---

# Bac-to-Bac Baculovirus Expression System

## Overview

The Bac-to-Bac system is a commercial baculovirus expression system that uses site-specific transposition in E. coli to generate recombinant baculovirus for protein expression in insect cells. The gene of interest is cloned into a donor vector, transposed into a bacmid in DH10Bac E. coli cells, then transfected into Sf9 or High Five insect cells. It enables high-yield expression of complex eukaryotic proteins including membrane proteins, GPCRs, and ion channels, with proper post-translational modifications.

## Principle

The Bac-to-Bac system (Thermo Fisher Scientific) uses a modified Autographa californica multiple nucleopolyhedrovirus (AcMNPV) bacmid DNA propagated in E. coli. The gene of interest is cloned into a pFastBac donor vector under the polyhedrin promoter, flanked by mini-Tn7 transposon elements. This donor vector is transformed into DH10Bac competent E. coli cells, which contain a helper plasmid encoding the Tn7 transposase. Site-specific transposition integrates the expression cassette into the attTn7 site of the bacmid, disrupting the lacZ gene for blue/white screening. Recombinant bacmid DNA is purified from white colonies and transfected into insect cells to generate recombinant baculovirus particles. Viral stocks are amplified and used for protein expression at controlled multiplicity of infection (MOI).

## Protocol

### Reagents and Materials

- {'name': 'pFastBac donor vector', 'description': 'Contains the gene of interest under the polyhedrin promoter, flanked by mini-Tn7 elements'}
- {'name': 'DH10Bac competent cells', 'description': 'E. coli strain containing the bacmid and helper plasmid encoding Tn7 transposase'}
- {'name': 'Sf9 or High Five insect cells', 'description': 'Spodoptera frugiperda (Sf9) or Trichoplusia ni (High Five) cells for baculovirus production and protein expression'}
- {'name': 'Insect cell culture medium', 'description': "Sf-900 II SFM, ESF 921, or Grace's supplemented medium"}

### Steps

1. {'step': 'Cloning', 'description': 'Clone the gene of interest into pFastBac donor vector with appropriate signal sequences and affinity tags'}
2. {'step': 'Transposition', 'description': 'Transform pFastBac construct into DH10Bac cells; select white colonies on plates containing Bluo-gal, IPTG, kanamycin, gentamicin, and tetracycline'}
3. {'step': 'Bacmid isolation', 'description': 'Purify recombinant bacmid DNA from selected white colonies using alkaline lysis or a commercial bacmid purification kit'}
4. {'step': 'Transfection', 'description': 'Transfect purified bacmid into Sf9 cells using Cellfectin or other cationic lipid reagent; incubate at 27 C for 72-96 h to produce P1 viral stock'}
5. {'step': 'Amplification', 'description': 'Infect fresh Sf9 cells at 2 x 10^6 cells/mL with P1 stock at MOI 0.1; harvest P2 viral stock after 48-72 h'}
6. {'step': 'Expression', 'description': 'Infect Sf9 or High Five cells at 2-4 x 10^6 cells/mL with P2/P3 stock at MOI 1-5; express protein for 48-72 h at 27 C'}
7. {'step': 'Harvest', 'description': 'Collect cells by centrifugation, wash with PBS, and store at -80 C or proceed directly to membrane preparation'}

### Typical Conditions

- **temperature**: 27 C
- **infection_density**: 2-4 x 10^6 cells/mL
- **moi_for_expression**: 1-5
- **expression_time**: 48-72 h

