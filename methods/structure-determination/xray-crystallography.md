---

title: X-ray Crystallography
created: 2026-04-26
updated: 2026-04-27
type: method
tags: [structure-xray]
sources: [doi/10.1002##1873-3468.14136, doi/10.1002##anie.201302374, doi/10.1006##jmbi.1994.0097, doi/10.1016##j.bbabio.2023.148986, doi/10.1016##j.cell.2017.03.010, doi/10.1016##j.cell.2017.12.011, doi/10.1016##j.cell.2018.11.025, doi/10.1016##j.cell.2019.01.003, doi/10.1016##j.cell.2018.12.006, doi/10.1007##s10969-013-9154-x, doi/10.1016##j.cell.2010.05.003]

---
layout: default


# X-ray Crystallography

## Description

X-ray crystallography is the most widely used method for determining atomic-resolution structures of membrane proteins. The technique requires well-ordered crystals and involves diffraction data collection, phase determination, model building, and refinement.

## Workflow

1. **Protein production** — expression in heterologous system
2. **Solubilization** — detergent extraction from membranes
3. **Purification** — affinity chromatography, ion-exchange, size-exclusion chromatography
4. **Crystallization** — vapor diffusion or LCP
5. **Cryoprotection** — soaking in cryoprotectant solution
6. **Data collection** — synchrotron or home source
7. **Phasing** — molecular replacement, SAD, or MAD
8. **Model building** — COOT or similar
9. **Refinement** — PHENIX or similar

## Proteins Using X-ray Crystallography (from this wiki)

- [[nTMATE2-transporter]] — 3.5 Å, P2₁2₁2₁, SPring-8 BL32XU
- [[opsin-gpcr]] — 2.65 Å
- [[a2a-adenosine-receptor]] — 2.25 Å and 2.6 Å
- [[rps-viridis-reaction-center]] — 2.3 Å, landmark structure
- [[psi-lhci-supercomplex]] — 3.2 Å, P2₁, SPring-8 BL44XU
- [[lb-semisweet]] — 2.8 Å outward-open (D57A) and 2.8 Å inward-open (Q20A)
- [[kappa-opioid-receptor]] — 3.1 Å active-state; BRIL-fused, MP1104 agonist + Nb39 [[nanobody]]; P2₁, APS 23ID-B/D
- [[adenine-nucleotide-transporter]] — 3.3 Å matrix-open state; TtAac, BKA-inhibited + nanobody; domain rotation mechanism
- [[mmpL3]] — Mycobacterial lipid transporter; apo + 4 inhibitor-bound structures (2.6 Å); proton-translocat[[ion-channels]]; 12 TM helices
- [[angiotensin-ii-type-1-receptor]] — 2.9 Å active-state; AT1R-S1I8-Nb.AT110i1 complex; P2₁2₁2, APS GM/CA 23ID-B; translational NCS in P1 expanded to P2₁2₁2; MolRep + Phaser molecular replacement; PDB: 6DO1
- [[acrB]] — 3.5 Å, space group R32, symmetric trimer; molecular replacement using CasMATE (PDB ID 5YCK); SPring-8 BL32XU; PDB: 4K7Q
- [[kirbac]] — Multiple structures (2.6–4.2 Å); KirBac1.1 (1P7B) and KirBac3.1 (1XL4, 1XL6) plus 5 new structures (III–VII); Australian Synchrotron 3BM1 and Swiss Light Source X06SA; reveals interdependent gating at selectivity filter and intracellular domain
- [[etb-receptor]] — 3.0 Å; P2₁2₁2; ETB-S6b complex; 32 datasets merged (KAMO); molecular replacement using ET-3-bound receptor (PDB 6IGK); reveals TM5 outward displacement (4 Å) suggesting active conformation
- [[sotb]] — Multiple conformations (occluded, inward-facing, inward-open); MFS antiporter; reveals nonlinear rigid-body movements in [[alternating-access]]
- [[angiotensin-ii-type-1-receptor]] — 2.9 Å; SFX/XFEL (LCP-SFX method at LCLS); AT1R-ZD7155 complex; first GPCR structure by serial femtosecond crystallography; room-temperature structure

## Key Software

- **Data processing**: XDS, HKL2000, MOSFLM
- **Phasing**: PHASER (molecular replacement)
- **Model building**: COOT
- **Refinement**: PHENIX.refine

## Related Methods

- [[molecular-replacement]] — phasing from homologous model
- [[cryoem]] — single particle cryo-EM alternative
- [[lipidic-cubic-phase]] — LCP crystallization method
- [[vapor-diffusion]] — vapor diffusion method
