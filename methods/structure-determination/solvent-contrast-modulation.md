---
title: X-ray Solvent Contrast Modulation
created: 2026-06-16
updated: 2026-06-16
type: method
category: methods
layout: default
tags: [structure-xray, subdirectory-structure-determination]
sources: [doi/10.1038##nature22357]
verified: false
---

# X-ray Solvent Contrast Modulation

## Overview

X-ray solvent contrast modulation is a crystallographic technique that resolves low-resolution electron density features such as lipid bilayers in membrane protein crystals by systematically varying the electron density of the solvent phase. Using a contrast medium like iohexol that is dissolved in the crystallization buffer at multiple concentrations, the method separates the constant scattering contribution (protein + lipid bilayer) from the variable solvent contribution, enabling visualization of features that are invisible in conventional electron density maps.

## Principle

In solvent contrast modulation, the electron density at a point (x, y, z) in a crystal can be separated into two parts: ρ_protein+lipid (constant) and ρ_solvent (variable). The solvent contribution is expressed using the solvent exchange probability P_ex(x, y, z) and the mean solvent density ⟨ρ_solvent⟩(ξ) which varies linearly with contrast medium concentration ξ:

ρ_total(x,y,z; ξ) = ρ_protein+lipid(x,y,z) + ⟨ρ_solvent⟩(ξ) · P_ex(x,y,z)

By collecting diffraction data from crystals soaked in buffers containing different concentrations of iohexol (0-80% w/v), the structure factors vary as a quadratic function of solvent electron density. Least-squares fitting of these data allows extraction of the protein+lipid structure factors and phases, producing electron density maps that reveal the lipid bilayer surrounding the membrane protein.

The technique is analogous to solvent contrast variation used in small-angle neutron and X-ray scattering but is applied to macromolecular crystallography. It is particularly effective at low resolution (10-200 Å Bragg spacing) where the lipid bilayer contributes most strongly to the diffraction pattern.

## Protocol

### Reagents and Materials

- [Iohexol](/xray-mp-wiki/reagents/additives/iohexol) (Histodenz, Sigma-Aldrich)
- Crystallization buffer (for SERCA: C₁₂E₈ detergent, phospholipids)

### Steps

1. {'step': '1. Prepare crystals of membrane protein', 'method': 'Standard crystallization method (e.g., microdialysis, vapor diffusion)', 'notes': 'Crystals must be stable across a range of iohexol concentrations'}
2. {'step': '2. Soak crystals in buffers with varying iohexol concentrations', 'method': 'Solvent exchange by dialysis or soaking', 'notes': 'For SERCA: 0%, 10%, 20%, 30%, 45%, 60%, 70%, 80% (w/v) iohexol. For >40%, dialysis for at least 48 h'}
3. {'step': '3. Collect diffraction data at each concentration', 'method': 'Synchrotron X-ray data collection', 'notes': 'Camera distance optimized for low-resolution data. Record reflections from ~200 Å to 3.2 Å Bragg spacing'}
4. {'step': '4. Fit structure factor amplitudes as function of solvent density', 'method': 'Least-squares fitting (quadratic)', 'notes': 'Fit |F_obs(h,k,l;ξ)|² to equation (2) for each reflection independently'}
5. {'step': '5. Calculate solvent exchange probability map', 'method': 'Phase determination from fitted parameters', 'notes': 'P_ex map reveals solvent accessibility; protein/lipid regions have P_ex ≈ 0, solvent regions have P_ex ≈ 1'}
6. {'step': '6. Generate electron density map of protein + lipid bilayer', 'method': 'Contrast modulation map', 'notes': '|F_protein+lipid| and phases from the fitting produce maps showing the lipid bilayer'}
7. {'step': '7. Build atomic model of lipid bilayer', 'method': 'Simulated annealing refinement', 'notes': 'Phospholipid head groups visible at 4.5 Å resolution; atomic models built for head group to carbonyl region'}

### Typical Conditions

- **temperature**: 40-100 K (cryocooled)
- **detector_distance**: ~600 mm
- **wavelength**: 1.0-1.5 Å
- **he_path**: 450 mm
- **resolution_range**: 3.2-200 Å
- **notes**: Low-resolution data (10-200 Å) are critical for bilayer visualization

