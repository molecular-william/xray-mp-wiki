---
title: Gas-Phase Unfolding Analysis
created: 2026-06-03
updated: 2026-06-03
type: method
category: methods
layout: default
tags: [quality-assessment, subdirectory-quality-assessment]
sources: [doi/10.1038##nature13419]
verified: false
---

# Gas-Phase Unfolding Analysis

## Overview

Gas-phase unfolding is an ion mobility mass spectrometry (IM-MS) technique used to assess the stability of membrane protein complexes by measuring their collision cross sections (CCS) across a range of collision voltages. By gradually increasing the collision voltage, the protein complex unfolds in a stepwise manner through distinct intermediate states. The unfolding trajectory (CCS vs. collision voltage) reveals the stabilization imparted by bound ligands such as lipids. This method enables direct comparison of apo and ligand-bound states within the same experiment, allowing quantification of lipid-protein interactions and ranking of lipid binding selectivity.

## Principle

Ion mobility measurements are performed over a range of collision voltages (typically 50-240 V). Ion arrival time is converted to collision cross section (CCS) using the Mason-Schamp equation. Plotting CCS against collision voltage reveals unfolding trajectories from the native state through intermediates to extended forms. The oligomeric state is maintained throughout the unfolding experiment. An equilibrium unfolding model (similar to chemical denaturation models) is fitted to the data to extract stabilization values. The transition midpoint (CV50) and the stabilization imparted by each bound lipid are calculated from the unfolding curve.

## Protocol

### Reagents and Materials

- [n-octyl beta-D-glucopyranoside (OG)]
- [octyltetraoxyethylene (C8E4)]
- [phosphatidylglycerol (PG)]
- [phosphatidylcholine (PC)]
- [phosphatidylethanolamine (PE)]
- [phosphatidylserine (PS)]
- [phosphatidic acid (PA)]
- [phosphatidylinositol (PI)]
- [cardiolipin (CDL)]

### Steps

1. {'step': 'Protein preparation', 'description': 'Purify membrane protein in optimal detergent (e.g., C8E4) and buffer exchange into volatile buffer (200 mM ammonium acetate, pH 7.2-8.0)'}
2. {'step': 'Lipid addition', 'description': 'Add phospholipids to protein complexes at optimized protein:lipid:detergent ratio; equilibrate 10-30 minutes at room temperature'}
3. {'step': 'IM-MS measurement', 'description': 'Collect ion mobility mass spectra over range of collision voltages (5 V or 2 V steps); measure ion arrival times'}
4. {'step': 'CCS calculation', 'description': 'Convert ion arrival time to CCS using Mason-Schamp equation; apply correction factor for missing residues'}
5. {'step': 'Unfolding trajectory analysis', 'description': 'Plot CCS vs. collision voltage; identify intermediate states; fit equilibrium unfolding model to extract stabilization values'}


## Advantages

- Direct comparison of apo and lipid-bound states within the same experiment
- Resolves discrete lipid-bound states individually
- Quantitative values for lipid stabilization
- No detergent micelle interference when optimal detergent used
- Oligomeric state maintained throughout unfolding

## Disadvantages

- Gas-phase conditions may not fully reflect native membrane environment
- Requires specialized IM-MS instrumentation
- Unfolding model fitting can be complex with multiple intermediates
- Detergent choice critical for maintaining native state
