---
title: Bacteriorhodopsin (bR) — Purple Membrane at 1.9 Å
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [gpcr, proton-pump, membrane-protein, xray-crystallography, lipidic-cubic-phase, retinal-protein]
sources: [doi/10.1016##S0969-2126(99)80118-X]
---

# Bacteriorhodopsin (bR) — Purple Membrane at 1.9 Å Resolution

## Overview

Bacteriorhodopsin (bR) from *Halobacterium salinarum* is a light-driven proton pump that converts light energy into a proton gradient for ATP synthesis. This paper reports the ground-state structure at 1.9 Å resolution from crystals grown in a lipidic cubic phase, revealing native lipids and water molecules in the proton translocation pathway — the biologically relevant structure.

## Structure

- **Organism**: *Halobacterium salinarum*
- **Resolution**: 1.9 Å
- **PDB ID**: Not explicitly stated (1999 pre-PDB deposition era; electron crystallography structures 1KZU, 1KZV existed)
- **Crystal system**: Hexagonal (implied from "hexagonal plate-like crystals")
- **Asymmetric unit**: Single bR monomer
- **Refinement**: R = 22.3%, Rfree = 24.5%
- **Data collection**: ESRF (European Synchrotron Radiation Facility)

### Protein Architecture

- **7 transmembrane α helices** (A-G)
- **Retinal chromophore**: Covalently bound to Lys216 via Schiff base (all-trans configuration in ground state)
- **Photocycle**: Photon absorption → isomerization to 13-cis,15-anti → proton transfer from Schiff base to Asp85 → proton release to extracellular medium → reprotonation from cytoplasmic side

### Water Molecules in Proton Translocation Pathway

- **8 well-ordered water molecules** in extracellular half of proton pathway
- **Continuous H-bond network** from Schiff-base nitrogen (Lys216) to:
  - Asp85 (primary proton acceptor)
  - Asp212
  - Arg82
  - Glu194
  - Glu204
- This network mediates proton translocation during photocycle AND stabilizes ground-state structure
- **No ordered waters** detected on cytoplasmic side — hydrophobic seal (Val49-Leu93) shelters Schiff base from cytosol

### Lipid Molecules (Native Purple Membrane Lipids)

- **9 lipid phytanyl moieties** modeled per monomer (4 cytoplasmic, 5 extracellular)
- **Lipid head groups not resolved** — only alkyl chains visible in electron density
- **Lipid-protein contacts**: Hydrophobic interactions of alkyl chains with helix residues
- **Key structural lipids**:
  - 502, 503, 507, 508: Form vdW contacts between symmetry-related trimers (maintain PM integrity)
  - 500: Center of trimer
  - 506: Rim of trimer
- **MALDI-MS of single crystals** identified 4 charged lipid species:
  - PGP-Me (phosphatidylglycerol phosphate methylester)
  - TGD (triglycosyldiether)
  - S-TGA-1 (sulfated triglycoside lipid)
  - S-TeGa (sulfated tetraglycosyl-diphytanylglycerol)
- **Native PM lipids** also contained: PG (phosphatidylglycerol), PGS (phosphatidylglycerol sulfate)

### Dynamics

- **Cytoplasmic side more flexible** than extracellular side (higher B-factors)
  - Cytoplasmic half B-factors: 24-33 Å²
  - Extracellular half B-factors: 19-26 Å²
- Flexibility consistent with conformational changes needed for cytoplasmic reprotonation
- **BC loop**: Reconstructed completely (vs partial in earlier twinned structures)
- **EF loop**: Partially resolved (residues 157-162 non-continuous density)

## Crystallization

### Lipidic Cubic Phase (LCP) Method

- **Matrix**: Monoolein-based lipidic cubic phase
- **Crystal morphology**: Hexagonal plate-like, up to 80 × 8 μm
- **Key advantage**: Native-like membrane environment preserved; bR fully functional in photocycle
- **Crystal packing**: Layers of native-like membranes stacked; ab-plane packing indistinguishable from PM
- **Stacking mechanism**: Polar interactions between cytosolic and extracellular loops of adjacent layers

### Crystal Release

- **Enzymatic hydrolysis**: Monoolein hydrolyzed to release crystals from cubic phase matrix
- **Washing**: Free-floating crystals washed in distilled water
- **MALDI-MS sample prep**: In situ lipid extraction from single crystals using matrix solution (2,5-dihydroxybenzoic acid + 10% 2-hydroxy-5-methoxybenzoic acid in methanol/chloroform 2:1)

## Expression and Purification

- **Source**: Native purple membrane (PM) from *Halobacterium salinarum*
- **Note**: bR is naturally abundant (~50% of total membrane protein in halobacteria grown under salt stress)
- **No detergent solubilization** required for crystallization — grown directly in LCP from native PM
- **Lipids**: Remain bound during any detergent solubilization steps

## Photocycle Mechanism

1. **Ground state**: All-trans retinal, Schiff base protonated (Lys216)
2. **Light absorption**: Isomerization to 13-cis,15-anti
3. **Proton transfer**: Schiff base → Asp85
4. **Proton release**: To extracellular medium (via Glu194, Glu204, water network)
5. **Reprotonation**: From cytoplasmic side (requires conformational changes in helices F and G)
6. **Reset**: Retinal re-isomerizes to all-trans

## Biological Significance

- **Energy transduction**: First light-driven proton pump structure at atomic resolution
- **Lipid-protein interactions**: Native lipids essential for trimer stability and PM integrity
- **Water-mediated proton conduction**: H-bond network enables efficient proton translocation
- **LCP crystallization**: Pioneering demonstration that LCP preserves native lipid environment
- **Spectroscopic similarity**: Photocycle kinetics in LCP crystals match native PM

## Related Proteins

- [[opsin-gpcr]] — Animal rhodopsin (G protein-coupled, not light-driven proton pump)
- [[bovine-rhodopsin]] — Bovine rhodopsin trigonal crystal form
- [[5ht2b-receptor]] — Serotonin GPCR with BRIL fusion

## References

- Belrhali et al. (1999) Structure 7:917-925 — Bacteriorhodopsin at 1.9 Å in LCP
- Pebay-Peyroula et al. (1997) Nature 388:165-168 — Preliminary LCP structure at 2.5 Å
- Henderson et al. (1990) JMB 213:899-929 — Electron crystallography at 3.7 Å
- Lanyi & Luecke (2001) — Bacteriorhodopsin review