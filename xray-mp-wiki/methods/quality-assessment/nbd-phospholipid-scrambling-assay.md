---
title: NBD-Phospholipid Scrambling Assay
created: 2026-06-03
updated: 2026-06-03
type: method
category: methods
layout: default
tags: [quality-assessment, subdirectory-quality-assessment]
sources: [doi/10.1038##nature12535, doi/10.1038##nature13984]
verified: false
---

# NBD-Phospholipid Scrambling Assay

## Overview

The NBD-phospholipid scrambling assay is a functional assay used to measure lipid scramblase activity. It employs nitrobenzoxadiazole (NBD)-labeled phospholipids ([NBD-PE](/xray-mp-wiki/reagents/lipids/nbd-pe/) and [NBD-PS](/xray-mp-wiki/reagents/lipids/nbd-ps/)) incorporated into liposomes to monitor the translocation of lipids between the inner and outer leaflets of the bilayer.

## Principle

NBD-labeled phospholipids are incorporated into the outer leaflet of proteoliposomes. Sodium dithionite (Na2S2O4) is a membrane-impermeable reducing agent that selectively quenches the fluorescence of NBD groups on the outer leaflet. Lipids that flip to the inner leaflet are protected from quenching. The rate of fluorescence recovery upon addition of a scramblase protein reflects the lipid scrambling activity. The assay measures the decrease in fluorescence as dithionite reduces outer-leaflet NBD fluorophores, with the kinetics providing a quantitative measure of scrambling.

## Protocol

### Reagents and Materials

- {'NBD-PE or NBD-PS': 'Nitrobenzoxadiazole-labeled phospholipid probe'}
- {'Egg yolk L-alpha-phosphatidylcholine (egg PC)': 'Major lipid component of liposomes'}
- {'E. coli polar lipids': 'Anionic lipid component of liposomes'}
- {'Sodium dithionite (Na2S2O4)': 'Membrane-impermeable reducing agent for NBD quenching'}
- {'HEPES buffer': 'Buffering agent'}
- {'EGTA': 'Calcium chelator for Ca2+-free conditions'}
- {'CaCl2 or other divalent cation salts': 'Ca2+ or alternative cations for activation'}

### Steps

1. {'step': 'Liposome preparation', 'description': 'Prepare liposomes from a mixture of egg PC and [E. coli Polar Lipids](/xray-mp-wiki/reagents/lipids/e-coli-polar-lipids/) (3:1 wt/wt ratio) by extrusion through a 400-nm filter after three freeze-thaw cycles'}
2. {'step': 'Protein reconstitution', 'description': 'Reconstitute purified scramblase protein into liposomes by detergent dilution or freeze-thaw cycles'}
3. {'step': 'Assay setup', 'description': 'Dilute proteoliposome suspension into assay buffer (60 mM HEPES pH 7.4) containing 2 mM [EGTA](/xray-mp-wiki/reagents/additives/egta/) or 2 mM [EGTA](/xray-mp-wiki/reagents/additives/egta/) plus divalent cations in a stirred cuvette at 23 C'}
4. {'step': 'Dithionite addition and fluorescence measurement', 'description': 'Add sodium dithionite to final concentration of 30 mM and record fluorescence decay on a spectrofluorometer (excitation 470 nm, emission 530 nm)'}
5. {'step': 'Data analysis', 'description': 'Normalize fluorescence intensity to F/Fmax and fit to exponential decay functions to determine scrambling kinetics'}


## Advantages

- Direct functional readout of lipid scramblase activity
- Can distinguish between different lipid species (PE vs PS)
- Sensitive to submicromolar Ca2+ activation
- Can be used to determine Ca2+ dependence (EC50)
- Can test alternative divalent cation activation (Sr2+, Mg2+)

## Disadvantages

- Requires purified scramblase protein and liposome reconstitution
- NBD fluorophore may alter lipid properties compared to native lipids
- Dithionite is oxygen-sensitive and must be freshly prepared
- Cannot distinguish between scrambling and permeation artifacts without controls
