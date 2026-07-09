---
title: "SARS-CoV-2 Spike Protein C-Terminal Domain"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2020.03.045, doi/10.1038##s41586-020-2180-5, doi/10.1038##s41586-020-2179-y]
verified: regex
uniprot_id: P0DTC2
---

# SARS-CoV-2 Spike Protein C-Terminal Domain

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0DTC2">UniProt: P0DTC2</a>

<span class="expr-badge">Severe acute respiratory syndrome coronavirus 2</span>

## Overview

The C-terminal domain (CTD) of the SARS-CoV-2 spike (S) protein, also known as the receptor-binding domain (RBD), is the region responsible for recognizing and binding to the host cell receptor human ACE2 ([Human Angiotensin-Converting Enzyme 2 (hACE2)](/xray-mp-wiki/proteins/slc-transporters/hace2/)). The SARS-CoV-2 CTD spans residues 319-541 of the S1 subunit and forms a core subdomain with beta strands and an external subdomain. It displays stronger affinity for [Human Angiotensin-Converting Enzyme 2 (hACE2)](/xray-mp-wiki/proteins/slc-transporters/hace2/) compared to the SARS-CoV RBD due to key residue substitutions, and is antigenically distinct from SARS-CoV RBD.


## Publications

### doi/10.1016##j.cell.2020.03.045

**Structures:**

<table class="wiki-table">
  <thead><tr>
    <th>PDB ID</th>
    <th>Resolution</th>
    <th>Space Group</th>
    <th>Construct</th>
    <th>Ligand/Co-factor</th>
  </tr></thead>
  <tbody>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6lzg">6LZG</a></td>
      <td>2.50 A</td>
      <td>P41212</td>
      <td>SARS-CoV-2 spike protein CTD residues 319-541, in complex with <a href="/xray-mp-wiki/proteins/slc-transporters/hace2/">Human Angiotensin-Converting Enzyme 2 (hACE2)</a></td>
      <td><a href="/xray-mp-wiki/proteins/slc-transporters/hace2/">Human Angiotensin-Converting Enzyme 2 (hACE2)</a> (human ACE2 residues 19-615)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Hi5 insect cells (baculovirus)
- **Construct**: SARS-CoV-2 RBD residues Arg319-Phe541, N-terminal gp67 signal peptide for secretion, C-terminal 6xHis tag

**Purification:**

<table class="wiki-table">
  <thead><tr>
    <th>Step</th>
    <th>Method</th>
    <th>Resin / Column</th>
    <th>Buffer + Detergent</th>
    <th>Notes</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>Cell culture and protein expression</td>
      <td>Mammalian transient transfection</td>
      <td>--</td>
      <td>--</td>
      <td>HEK293T cells transfected with pCAGGS plasmid; supernatant collected 24 h post-transfection</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Protein A <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>HiTrap rProtein A FF column</td>
      <td>Binding buffer 20 mM Na3PO4 pH 7.0; elution with 0.1 M glycine-HCl pH 3.0 neutralized with 1 M <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 9.0</td>
      <td>mFc fusion protein captured on Protein A column</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration column</td>
      <td>PBS</td>
      <td>Further purification and buffer exchange</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SARS-CoV-2 CTD/hACE2 complex, protein concentration 15 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M MES pH 6.5, 10% w/v <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 5000 MME, 12% v/v 1-propanol</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir solution supplemented with 20% v/v <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> before flash-cooling in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals diffracted to 2.5 A; data collected at SSRF BL17U (wavelength 0.97919 A)</td>
    </tr>
  </tbody>
</table>
### doi/10.1038##s41586-020-2180-5

**Structures:**

<table class="wiki-table">
  <thead><tr>
    <th>PDB ID</th>
    <th>Resolution</th>
    <th>Space Group</th>
    <th>Construct</th>
    <th>Ligand/Co-factor</th>
  </tr></thead>
  <tbody>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6m0j">6M0J</a></td>
      <td>2.45 A</td>
      <td>P4₁2₁2</td>
      <td>SARS-CoV-2 RBD residues Arg319-Phe541, in complex with ACE2 (residues Ser19-Asp615)</td>
      <td><a href="/xray-mp-wiki/proteins/slc-transporters/hace2/">Human Angiotensin-Converting Enzyme 2 (hACE2)</a> N-terminal peptidase domain, zinc ion</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Hi5 insect cells (baculovirus)
- **Construct**: SARS-CoV-2 RBD residues Arg319-Phe541, N-terminal gp67 signal peptide for secretion, C-terminal 6xHis tag

**Purification:**

<table class="wiki-table">
  <thead><tr>
    <th>Step</th>
    <th>Method</th>
    <th>Resin / Column</th>
    <th>Buffer + Detergent</th>
    <th>Notes</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>Baculovirus expression</td>
      <td>Expression in Hi5 insect cells via Bac-to-Bac system</td>
      <td>--</td>
      <td>HBS (10 mM HEPES pH 7.2, 150 mM NaCl)</td>
      <td>pFastBac-Dual vector with gp67 signal peptide; virus amplified in SF9 cells; Hi5 cells infected at 2 x 10^6 cells/ml; supernatant collected 60 h post-infection</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA affinity</td>
      <td>Ni-NTA resin (GE Healthcare)</td>
      <td>HBS (10 mM HEPES pH 7.2, 150 mM NaCl) + --</td>
      <td>Eluted with 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> in HBS buffer</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> column (GE Healthcare)</td>
      <td>HBS (10 mM HEPES pH 7.2, 150 mM NaCl) + --</td>
      <td>Pre-equilibrated with HBS; complex formed by mixing with ACE2 before SEC; concentrated to 13 mg/ml</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SARS-CoV-2 RBD/ACE2 complex at 13 mg/ml in 20 mM Tris pH 7.5, 150 mM NaCl</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM MES pH 6.5, 10% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 5000 MME, 12% 1-propanol</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir solution supplemented with 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> before flash-cooling in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Sitting drops of 200 nl complex + 200 nl well solution; diffraction at 100 K, wavelength 1.07180 A on BL17U1 at SSRF; data processed with aquarium pipeline</td>
    </tr>
  </tbody>
</table>
### doi/10.1038##s41586-020-2179-y

**Structures:**

<table class="wiki-table">
  <thead><tr>
    <th>PDB ID</th>
    <th>Resolution</th>
    <th>Space Group</th>
    <th>Construct</th>
    <th>Ligand/Co-factor</th>
  </tr></thead>
  <tbody>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6vw1">6VW1</a></td>
      <td>2.68 A</td>
      <td>P 21 21 21</td>
      <td>SARS-CoV-2 chimeric RBD (SARS-CoV-2 core + SARS-CoV side loop) in complex with human ACE2 (residues 1-615)</td>
      <td>human ACE2 (residues 1-615), zinc ion</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Hi5 insect cells (baculovirus)
- **Construct**: SARS-CoV-2 RBD residues Arg319-Phe541, N-terminal gp67 signal peptide for secretion, C-terminal 6xHis tag

**Purification:**

<table class="wiki-table">
  <thead><tr>
    <th>Step</th>
    <th>Method</th>
    <th>Resin / Column</th>
    <th>Buffer + Detergent</th>
    <th>Notes</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>Baculovirus expression</td>
      <td>Expression in Sf9 insect cells via Bac-to-Bac system (Life Technologies)</td>
      <td>--</td>
      <td>20 mM Tris pH 7.2, 200 mM NaCl</td>
      <td>pFastBac vector with honeybee melittin signal peptide and C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">Polyhistidine Tag (His6)</a>; RBD and ACE2 separately expressed and secreted into medium</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA affinity</td>
      <td>Ni-NTA column</td>
      <td>20 mM Tris pH 7.2, 200 mM NaCl + --</td>
      <td>His6-tagged proteins purified from cell culture medium</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> column (GE Healthcare)</td>
      <td>20 mM Tris pH 7.2, 200 mM NaCl + --</td>
      <td>RBD and ACE2 incubated together; complex purified by Superdex200 gel-filtration; concentrated to 13 mg/ml</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SARS-CoV-2 chimeric RBD-ACE2 complex at 13 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM Tris pH 8.5, 18-20% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 6000, 100 mM NaCl</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>100 mM Tris pH 8.5, 30% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 6000, 100 mM NaCl, 30% <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a>; flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>X-ray diffraction data collected at Advanced Photon Source beamline 24-ID-E; structure determined by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using SARS-CoV RBD-ACE2 (PDB 2AJF)</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### SARS-CoV-2 CTD binds hACE2 with higher affinity than SARS-RBD

The SARS-CoV-2 CTD displays stronger affinity for [Human Angiotensin-Converting Enzyme 2 (hACE2)](/xray-mp-wiki/proteins/slc-transporters/hace2/) compared to the SARS-CoV RBD. Atomic details at the binding interface show that key residue substitutions in SARS-CoV-2 CTD slightly strengthen the interaction. Surface plasmon resonance (SPR) analysis confirmed specific interactions between SARS-CoV-2 S1 and SARS-CoV-2 CTD with [Human Angiotensin-Converting Enzyme 2 (hACE2)](/xray-mp-wiki/proteins/slc-transporters/hace2/), while no binding was observed with hCD26 (DPP4) or hAPN (aminopeptidase N). The [Human Angiotensin-Converting Enzyme 2 (hACE2)](/xray-mp-wiki/proteins/slc-transporters/hace2/) binding site on SARS-CoV-2 CTD involves residues Y453, L455, F456, K417, A475, G476, Y473, N487, Y489, E484, F490, Q493, G446, Y449, Q498, T500, N501, and Y505 forming contacts with [Human Angiotensin-Converting Enzyme 2 (hACE2)](/xray-mp-wiki/proteins/slc-transporters/hace2/) residues including F28, Y41, H34, D38, Y41, Q42, and L45.

### Antigenic differences between SARS-CoV-2 and SARS-CoV RBD

Despite structural similarity in the overall protein fold, the SARS-CoV-2 CTD and SARS-RBD are antigenically distinct. A panel of six murine monoclonal antibodies (B30A38, A50A1A1, C31A12 targeting SARS-CoV S1; mAbs 1-3 targeting SARS-RBD) that effectively bound SARS-CoV S showed no interaction with SARS-CoV-2 S. Polyclonal antisera against SARS-RBD also failed to bind SARS-CoV-2 S. Electrostatic surface potential maps revealed divergent electrostatic distributions between the two viral ligands, likely explaining their differing immunogenicity. This suggests that SARS-RBD-based vaccine candidates may not confer effective SARS-CoV-2 prophylaxis.

### Structural comparison of SARS-CoV-2 CTD and SARS-RBD

Superimposition of the SARS-CoV-2 CTD/hACE2 and SARS-RBD/hACE2 structures reveals overall similar receptor binding modes. However, the loop exhibiting variant conformations and specific residue contacts differ between the two viruses. The SARS-CoV-2 CTD contains a core subdomain with beta strands labeled with extra c and an external subdomain with elements labeled with prime symbols. A disulfide bond and an N-glycan linked to N343 are present in the SARS-CoV-2 CTD structure.

### Convergent evolution of RBDs for ACE2 binding

The 2.45 A structure of the SARS-CoV-2 RBD-ACE2 complex (PDB 6M0J) reveals the twisted five-stranded antiparallel beta sheet core (beta1-beta4, beta7) with an extended insertion (RBM) containing beta5, beta6, alpha4 and alpha5 helices. Eight cysteine residues form four disulfide bonds in the core (Cys336-Cys361, Cys379-Cys432, Cys391-Cys525, Cys480-Cys488). Binding affinity measurements by SPR gave KD of 4.7 nM for ACE2/SARS-CoV-2 RBD vs 31 nM for ACE2/SARS-CoV RBD. A unique positively charged patch contributed by Lys417 on the SARS-CoV-2 RBD forms a salt-bridge with Asp30 of ACE2 that is absent in SARS-CoV (Val404). SARS-CoV antibodies m396, S230, 80R and CR3014 showed no cross-binding to SARS-CoV-2 RBD due to epitope differences, though CR3022 binds with KD 6.2 nM.

### Compact ACE2-binding ridge and hotspot stabilization in SARS-CoV-2 RBD

The 2.68 A crystal structure of the SARS-CoV-2 chimeric RBD-ACE2 complex (PDB 6VW1) reveals that the ACE2-binding ridge in SARS-CoV-2 RBD has a more compact conformation compared to SARS-CoV RBD. Several residue changes in SARS-CoV-2 RBM stabilize two virus-binding hotspots at the RBD-ACE2 interface: hotspot 31 (centered on ACE2 residues Lys31-Glu35) and hotspot 353 (centered on ACE2 Lys353). The chimeric RBD design (SARS-CoV-2 core with SARS-CoV side loop) facilitated crystallization while maintaining native RBM conformation. SPR measurements showed the chimeric RBD has higher ACE2-binding affinity (KD 23.2 nM) than wild-type SARS-CoV-2 RBD (KD 44.2 nM), which in turn has significantly higher affinity than SARS-CoV RBD (KD 185 nM).


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/hace2/">Human Angiotensin-Converting Enzyme 2 (hACE2)</a> — Co-crystallized receptor in PDB 6LZG, 6M0J and 6VW1
- <a href="/xray-mp-wiki/reagents/buffers/mes/">2-(N-Morpholino)ethanesulfonic Acid (MES)</a> — Crystallization buffer at pH 6.5
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> — PEG 5000 MME used as crystallization precipitant
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Cryoprotectant (20% v/v) for flash-cooling crystals
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Protein A affinity purification of mFc-fusion protein; Ni-NTA affinity of His-tagged RBD
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Final purification step for SARS-CoV-2 CTD-mFc and RBD-ACE2 complex
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> — 10 mM HEPES pH 7.2 used in HBS purification buffer
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — 500 mM imidazole used for elution from Ni-NTA resin
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a> — Additive used in purification or crystallization buffers
