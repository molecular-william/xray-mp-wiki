---
title: c-Ring (c11 Rotor Ring of Na+-ATP Synthase from I. tartaricus)
created: 2026-04-28
updated: 2026-04-28
type: protein
tags: [rotor, atp-synthase, membrane-protein, ion-channel, xray-crystallography]
sources: [doi/10.1016##J.JMB.2009.05.082, doi/10.1126##science.1108259]
---
layout: default

# c-Ring — c11 Rotor Ring from *Ilyobacter tartaricus* Na+-ATP Synthase

## Overview

The c-ring (c11 rotor ring) is the membrane-embedded rotary component of the F-type Na+-dependent ATP synthase from the bacterium *Ilyobacter tartaricus*. It consists of 11 c-subunits forming a symmetric ring with 11 Na+ binding sites located between adjacent subunits. The c-ring rotates within the membrane as part of the F0 motor complex, driven by the sodium-motive force (smf), and transfers mechanical energy to the F1 catalytic head via the central gamma subunit to produce ATP.

## Structure

- **Resolution**: 2.35 Å (updated refinement, PDB 2WGM)
- **Space group**: P2₁
- **Unit cell**: a=146.7, b=139.3, c=151.9 Å, β=118.4°
- **Asymmetric unit**: 4 symmetric c11 rings (44 c-subunits)
- **c-subunit**: 2 transmembrane α-helices connected by a short cytoplasmic loop
- **N-terminus and C-terminus**: Both located in the periplasm
- **PDB IDs**: 1YCE (original 2005), 2WGM (updated 2009 refinement)
- **Solvent content**: 66.1%
- **Refinement**: R=22.0%, R-free=24.5%, 423 solvent waters, 44 ions, 44 fatty acid chains

### Hourglass Architecture

The c11 ring forms a symmetric hourglass-shaped assembly:
- **Outer surface**: Nonpolar (facing lipid bilayer)
- **Inner surface**: Polar (containing Na+ binding sites between subunits)
- **Channel diameter**: Accommodates Na+ ions at 11 inter-subunit interfaces

## Na+ Binding Sites — Complete Coordination Structure

Each of the 11 Na+ binding sites is located between adjacent c-subunits with **5 ligands**:

| Ligand | Residue | Distance (Å) |
|--------|---------|-------------|
| Gln32 Oε1 | Side chain | 2.39 |
| Val63 O | Backbone carbonyl | 2.38 |
| Glu65 Oδ2 | Side chain | 2.48 |
| Ser66 Oγ | Side chain | 2.26 |
| **HOH** | **Buried structural water** | **2.37** |

### Key Structural Features

- **Glu65** serves dual role: Na+ ligand AND acceptor of 3 hydrogen bonds (from Gln32-NH2, Ser66-OH, Tyr70-OH)
- This H-bond network provides a "locked conformation" of the binding site
- **Thr67** hydroxyl coordinates the buried water molecule (2.75 Å from HOH)
- **Ala64** carbonyl also H-bonds to the water (2.79 Å)
- The water's molecular dipole is oriented optimally for Na+ coordination

### Na+ vs H+ Selectivity — Thr67 as the Key Distinction

- **Thr67 is the ONLY residue that distinguishes Na+-ATP synthases from H+-ATP synthases**
- In H+-ATP synthases, position 67 is replaced by other residues (e.g., Ile in mycoplasma)
- Bacteria with Thr67 at position 67 grow anaerobically in Na+-rich environments
- MD simulations show: without the water molecule, Thr67 fluctuates between rotamers A and B, destabilizing the binding site
- With the water molecule, Thr67 is locked in a single rotamer — maintaining the coordination shell

### Fatty Acid Chains

- 44 fatty acid chains observed in the refined structure (one per c-subunit)
- Likely from membrane lipids incorporated during purification
- Located near the transmembrane helices

## Ion Translocation Mechanism

1. Na+ binds to the c-ring at the periplasmic side
2. The c-ring rotates within the membrane, driven by the sodium-motive force
3. At the a/c interface, the conserved arginine in subunit a neutralizes Glu65
4. Na+ is released to the cytoplasmic side
5. The c-ring continues rotation, completing the cycle

## Expression and Purification

**Note**: This paper is a re-refinement of the structure originally reported in Meier et al. (2005) Science 308:659-662. The original purification and crystallization methods are described in that paper. The raw paper is not available in the wiki's raw papers folder.

- **Original PDB**: 1YCE (Meier et al. 2005 Science)
- **Updated PDB**: 2WGM (this paper, 2009)
- **Data set**: Same diffraction data as Meier et al. 2005
- **Refinement improvements**: More stable TLS model, unbiased ion/water positions, MD simulations

## Biological Context

- **Organism**: *Ilyobacter tartaricus* — anaerobic bacterium growing in Na+-rich environments
- **Energy coupling**: Uses sodium-motive force (smf) rather than proton-motive force (pmf)
- **Stoichiometry**: F0 complex = a:b2:c10-15 (11 c-subunits in *I. tartaricus*)
- **Evolutionary significance**: Na+-bioenergetics predates H+-bioenergetics; this structure reveals an ancient strategy for selective ion coupling in ATP synthases
- **Comparison with V-ATPase K-ring**: *Enterococcus hirae* V-ATPase K-ring also pumps Na+ but uses Gln65 carbonyl (not water) as the fifth ligand

## Related Proteins

- [[acrB]] — RND multidrug exporter from *P. aeruginosa*
- [[mexb]] — RND multidrug exporter from *P. aeruginosa*
- Other ion-coupled membrane transporters

## References

- Meier et al. (2009) JMB 391:498-507 — Updated c-ring structure (PDB 2WGM) with complete Na+ coordination
- Meier et al. (2005) Science 308:659-662 — Original c-ring structure (PDB 1YCE)
- Murata et al. (2005) Science 308:654-659 — K-ring of V-ATPase from *E. hirae*