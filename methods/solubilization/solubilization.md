---
title: Solubilization
created: 2026-04-27
updated: 2026-04-27
type: method
tags: [solubilization-detergent, membrane-protein, sample-preparation]
sources: [doi/10.1016##j.jmb.2009.08.029, doi/10.1016##j.cell.2017.01.042, doi/10.1016##j.cell.2017.03.010, doi/10.1016##j.bbrc.2019.12.091, doi/10.1016##j.str.2018.10.027, doi/10.1016##j.jmb.2018.02.026, doi/10.1073##PNAS.1105687108, doi/10.1016##j.cell.2018.11.025, doi/10.1016##j.str.2020.11.014, doi/10.1038##s41586-018-0039-9, doi/10.7554##eLife.84006, doi/10.1074##jbc.RA120.014118]


category: methods
layout: default
---




# Solubilization

## Overview

Solubilization is the first critical step in membrane protein purification workflows. It involves extracting membrane proteins from their native lipid bilayer environment into an aqueous-compatible form using detergents or other amphipathic molecules. Successful solubilization must preserve protein structure, function, and oligomeric state while removing the bulk of membrane lipids and insoluble cellular debris.

The solubilization process consists of three main stages: (1) cell lysis and membrane preparation, (2) detergent-mediated extraction, and (3) clarification of the solubilized material.

## Cell Lysis Methods

Multiple lysis methods are used depending on the expression system and protein type:

- **French pressure cell / high-pressure homogenizer**: Used for bacterial membranes (e.g., *E. coli*). Cells are forced through a narrow orifice at high pressure (e.g., 20,000 psi). Example: CusA from *E. coli* membranes were disrupted with a French pressure cell, yielding membranes washed with 2 M KCl to remove periplasmic contaminants [10.1016##j.jmb.2009.08.029].
- **Sonication**: Cell suspensions are subjected to ultrasonic waves to disrupt membranes. Used for bacterial and some eukaryotic systems. Example: LbSemiSWEET membranes were lysed by sonication before DDM solubilization [10.1016##j.cell.2017.03.010].
- **Dounce / Potter-Elvehjem homogenizer**: Used for mammalian cell membranes and tissue homogenates. Example: Ton complex from rat brain was homogenized with a Dounce homogenizer [10.1038##nature19757].
- **Freeze-thaw cycles**: Repeated freezing in liquid nitrogen and thawing at room temperature, often used in combination with other methods.
- **Lytic enzymes**: Lysozyme treatment for bacterial cell walls, often followed by mechanical disruption.

## Membrane Isolation

After lysis, membranes are separated from cytosolic content by centrifugation:

- **Low-speed spin**: 10,000-25,000 g for 15-30 min at 4°C to remove unbroken cells and large debris
- **Ultracentrifugation**: 100,000-370,000 g for 30-120 min at 4°C to pellet membranes
- **Washing**: Membrane pellets are often resuspended and washed 1-3 times with buffer (sometimes containing high salt, e.g., 0.5-2 M NaCl or 2 M KCl, to remove peripheral membrane proteins and contaminants)
- **Storage**: Pelleted membranes are typically snap-frozen in liquid nitrogen and stored at -80°C

Example protocols:
- *E. coli* membranes: 300,000 g for 90 min [10.1016##j.jmb.2009.08.029]
- Sf9 insect cell membranes: 180,000 g for 1 h [10.1016##j.bbrc.2019.12.091]
- Mammalian tissue: 25,000 g for 30 min at 4°C, then ultracentrifugation [10.1038##s41594-018-0067-z]

## Detergent Selection

The choice of detergent is the most critical parameter in solubilization. Key considerations include detergent mildness, CMC, and compatibility with downstream steps.

### Default: DDM (n-Dodecyl-β-D-Maltopyranoside)

DDM is the universal first-choice detergent for solubilization across all membrane protein classes:

| Protein class | Typical DDM concentration | Notes |
|