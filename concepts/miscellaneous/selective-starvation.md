---
title: Selective Starvation of Malaria Parasites
created: 2026-06-11
updated: 2026-06-11
type: concept
category: concepts
layout: default
tags: [concept-functional, subdirectory-concepts]
sources: [doi/10.1073##pnas.2017749118]
verified: false
---

# Selective Starvation of Malaria Parasites

## Overview
The selective starvation strategy is an antimalarial approach that exploits the dependence of blood-stage Plasmodium falciparum parasites on a constant supply of D-glucose as their primary energy source. By selectively inhibiting PfHT1 (the sole hexose transporter in P. falciparum) over human glucose transporters, this strategy aims to "starve out" the parasite by blocking glucose uptake. Since the parasite cannot switch to alternative energy sources under physiological conditions, inhibition of PfHT1 leads to glycolysis shutdown and parasite death. The strategy was validated through the design of orthosteric–allosteric dual inhibitors (TH-PF series) that selectively target PfHT1 over hGLUT1, with potent antiplasmodial activity against both drug-sensitive and multidrug-resistant parasite strains.


## Mechanism/Details
The blood-stage malaria parasites depend entirely on glucose as their primary energy source, with no significant alternative carbon sources available at physiological concentrations. PfHT1 is transcribed from a single-copy gene with no close paralogue, making it an essential and non-redundant target. The "selective starvation" strategy was conceptualized based on the observation that PfHT1 possesses a unique allosteric pocket adjacent to the glucose-binding site that is more hydrophobic than the corresponding region in human GLUT1. This structural difference was exploited to design compounds that simultaneously occupy both the orthosteric glucose-binding site and the allosteric pocket, achieving high selectivity for PfHT1 over hGLUT1.
The strategy was experimentally validated through several lines of evidence: - TH-PF series compounds showed a strong correlation between PfHT1 biochemical
  inhibition (IC50) and parasite growth inhibition (EC50)
- Glucose concentration in culture media directly affected EC50 values of TH-PF
  compounds, confirming on-target competition with glucose
- TH-PF01 and TH-PF03 rapidly shut down glycolysis in blood-stage parasites as
  measured by Seahorse extracellular flux analysis
- The parasites grew only in the presence of glucose or fructose (at super-physiological
  concentrations), confirming that glucose is the sole physiological energy source
- TH-PF compounds showed equipotency against both drug-sensitive (3D7) and
  multidrug-resistant (Dd2) strains, including quinine-resistant parasites

The physiological glucose concentration in human blood (3.9-6.9 mM) is lower than standard culture media (11 mM), suggesting that the inhibitors may be even more effective in vivo. Furthermore, the schizont stage (which consumes the most glucose) was found to be the most sensitive to TH-PF treatment.


## Examples in Membrane Protein Work
- [PfHT1](/xray-mp-wiki/proteins/mfs-transporters/pfht1/) — The selective starvation strategy targets PfHT1, the sole hexose transporter in P. falciparum.
- [hGLUT1](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) — Selectivity over hGLUT1 is critical to avoid inhibiting human glucose uptake, ensuring the "selective" aspect of the starvation strategy.

## Related Concepts
- [Orthosteric–Allosteric Dual Inhibition](/xray-mp-wiki/concepts/transport-mechanisms/orthosteric-allosteric-dual-inhibition/) — The TH-PF series achieves selective starvation through simultaneous targeting of orthosteric and allosteric sites of PfHT1

## Cross-References
- [PfHT1 (Plasmodium falciparum Hexose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/pfht1/) — PfHT1 is the molecular target of the selective starvation strategy
- [hGLUT1 (Human Glucose Transporter 1)](/xray-mp-wiki/proteins/mfs-transporters/hglut1/) — Selectivity over hGLUT1 is essential for the "selective" aspect of the strategy
- [TH-PF01](/xray-mp-wiki/reagents/ligands/th-pf01/) — Lead compound validating the selective starvation strategy
- [TH-PF03](/xray-mp-wiki/reagents/ligands/th-pf03/) — Most potent lead compound in the selective starvation strategy
- [Orthosteric–Allosteric Dual Inhibition](/xray-mp-wiki/concepts/transport-mechanisms/orthosteric-allosteric-dual-inhibition/) — The dual inhibition approach enabled selective PfHT1 targeting
