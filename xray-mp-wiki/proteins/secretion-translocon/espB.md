---
title: "EspB"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jsb.2015.06.003]
verified: agent
uniprot_id: P9WJD9
---

# EspB

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P9WJD9">UniProt: P9WJD9</a>

<span class="expr-badge">Mycobacterium tuberculosis</span>

## Overview

EspB is a secreted virulence factor from Mycobacterium tuberculosis, encoded within the ESX-1 (type VII secretion) locus and classified as one of the Esp (ESX-secreted protein) family. EspB contains a unique PE-PPE fusion architecture in its N-terminal domain, adopting an elongated all-helical fold that structurally resembles the PE25-PPE41 heterodimer despite limited sequence similarity. The mature secreted form is a 50 kDa protein resulting from proteolytic cleavage of the C-terminal domain by the MycP1 serine protease. EspB forms oligomeric donut-shaped particles and has been shown to bind phospholipids including [Phosphatidylserine](/xray-mp-wiki/reagents/lipids/phosphatidylserine) and phosphatidic acid. EspB is required for host-cell death, phagosomal escape, and co-dependent secretion of ESAT-6/CFP-10.


## Publications

### doi/10.1016##j.jsb.2015.06.003

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4xwp">4XWP</a></td>
      <td>1.82 A</td>
      <td>C2221</td>
      <td>EspB residues 7-278 (PE-PPE domains only), N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag">Polyhistidine Tag (His6)</a> with TEV cleavage site</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4xxx">4XXX</a></td>
      <td>1.5 A</td>
      <td>C2221</td>
      <td>EspB residues 7-278 (PE-PPE domains only), N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag">Polyhistidine Tag (His6)</a> with TEV cleavage site</td>
      <td>None (crystallized with <a href="/xray-mp-wiki/reagents/lipids/phosphatidylserine">Phosphatidylserine</a> additive but no lipid observed in structure)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4xxn">4XXN</a></td>
      <td>2.14 A</td>
      <td>I222</td>
      <td>EspB residues 7-278 (PE-PPE domains only), N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag">Polyhistidine Tag (His6)</a> with TEV cleavage site</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4xy3">4XY3</a></td>
      <td>3.04 A</td>
      <td>Not specified</td>
      <td>Full-length EspB residues 1-460</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli Rosetta2(DE3)
- **Construct**: EspB residues 7-278 cloned into modified pET-28b vector with N-terminal His6-tag and [TEV Protease](/xray-mp-wiki/reagents/additives/tev-protease) cleavage site

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
      <td>Cell lysis</td>
      <td>Cell disruption</td>
      <td>--</td>
      <td>20 mM Tris pH 8.5, 300 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> + --</td>
      <td>Cells resuspended and passed five times through cell disrupter at 4 C</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) column</td>
      <td>20 mM Tris pH 8.5, 300 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> (wash); gradient to 250 mM imidazole (elution) + --</td>
      <td>Lysate applied to pre-equilibrated <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> column; EspB eluted in gradient with <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Proteolytic cleavage</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 300 mM NaCl + --</td>
      <td>Cleaved protein dialysed overnight at 4 C with <a href="/xray-mp-wiki/reagents/additives/tev-protease">TEV Protease</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography)</td>
      <td>Superdex200 16/30 column</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 100 mM NaCl + --</td>
      <td>Protein concentrated to 10 mg/mL; purity >90%</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>EspB7-278 at 10 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M calcium acetate, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/tris">Tris-HCl Buffer</a>, 20% PEG3000</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir mother liquor supplemented with 25% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>; flash cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Space group C2221; structure refined to 1.82 A resolution (Rwork 0.199, Rfree 0.234); <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement">Molecular Replacement</a> using PE25-PPE41 heterodimer (PDB 2G38) as search model; loop residues 86-115 and 125-130 missing due to disorder</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>EspB7-278 at 10 mg/mL with 1 mM L-alpha-<a href="/xray-mp-wiki/reagents/lipids/phosphatidylserine">Phosphatidylserine</a> additive</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M potassium dihydrogen phosphate, 20% w/v <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a>3350</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>291 K</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Reservoir mother liquor supplemented with 25% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>; flash cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Space group C2221; best dataset diffracted to 1.5 A resolution (Rwork 0.194, Rfree 0.218); refined with seven TLS groups; isomorphous with 4XWP but less disordered (only residues 90-114 missing); no electron density for <a href="/xray-mp-wiki/reagents/lipids/phosphatidylserine">Phosphatidylserine</a> observed despite additive presence</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>EspB7-278 at 10 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M sodium chloride, 0.1 M CAPS pH 10.5, 1.26 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate">Ammonium Sulfate</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Space group I222; structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement">Molecular Replacement</a> using EspB7-278 C2221 structure (PDB 4XWP) as search model; refined to 2.14 A resolution (Rwork 0.204, Rfree 0.251); loop residues 82-114 missing</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Full-length EspB1-460</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M CAPSO pH 10.8, 0.2 M sodium chloride, 1.5 M <a href="/xray-mp-wiki/reagents/additives/ammonium-sulfate">Ammonium Sulfate</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Space group not specified; structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement">Molecular Replacement</a> using EspB7-278 (PDB 4XXN) as search model; refined to 3.04 A resolution (Rwork 0.220, Rfree 0.266); C-terminal domain disordered; only 5 additional C-terminal residues (279-283) added</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### EspB is a PE-PPE fusion protein with heterodimer-like fold

The mature EspB isoform (residues 7-278) represents a fusion of PE and PPE N-terminal regions into a single polypeptide chain. The structure adopts an all-helical, elongated paperclip-like fold superimposable with the PE25-[PPE41](/xray-mp-wiki/proteins/ppe41) heterodimer (RMSD 1.9 A over 249 CA atoms, 17% sequence identity). EspB contains 7 alpha helices: helices alpha1 and alpha2 correspond to PE25 helices and adopt an antiparallel hairpin; helix alpha3 corresponds to PPE41 alpha1. Proline residues P28, P29, P33, and P36 act as knobs-in-the-holes in the groove between helices alpha2 and alpha4. The PE and PPE sequence motifs are not conserved in EspB (residues QQ at 11-12 and DLK at 132-134 replace PE and PPE respectively).

### EspB lacks the EspG chaperone-binding site

EspB is missing residues D121-T129 that contain the characteristic hh motif of PPE proteins and mediate EspG binding. Additionally, EspB lacks about 9 residues compared to the alpha4-alpha5 loop region of [PPE41](/xray-mp-wiki/proteins/ppe41), making it approximately 11 Angstroms shorter at one end. Pull-down experiments confirmed that EspB does not bind the ESX-1-specific chaperone EspG1, indicating that EspB has evolved as a PE-PPE fusion that no longer requires EspG for folding or stability.

### C-terminal domain is disordered and prevents oligomerization

The C-terminal domain of full-length EspB (residues beyond K283) is unstructured in crystal structures and in solution. Mature EspB (50 kDa) forms oligomers in M. tuberculosis culture filtrate, while full-length EspB (60 kDa) in cell lysate does not oligomerize. This suggests the unfolded C-terminal domain prevents self-association in the cytosol. Electron microscopy of the N-terminal fragment (EspB1-338) revealed donut-shaped ring particles approximately 10 x 10 nm in size.

### Putative lipid-binding sites on EspB surface

Structural analysis revealed hydrophobic grooves with adjacent positive charges that may serve as lipid-binding sites. The first groove between helices alpha1 and alpha2 contains residues L60, F159, L163 with a volume of 395 cubic Angstroms. A second smaller groove (53 cubic Angstroms) is located at the tip between helices alpha6 and alpha7 with L232, I246 at the bottom and Y236, Y250 at the rim. This is consistent with previous findings that mature EspB recognizes phosphatidic acid and [Phosphatidylserine](/xray-mp-wiki/reagents/lipids/phosphatidylserine).

### YxxxD/E secretion motif adopts helical conformation

The conserved YxxxD/E secretion motif (residues 81-85) in EspB is located adjacent to the partially disordered PE-PPE linker and adopts a helical conformation in the high-resolution structure. The motif is positioned at the beginning of helix alpha5 where W176 contributes to a tight interface between helices alpha2 and alpha5. The N-epsilon atom of W176 forms a hydrogen bond with the hydroxyl group of Y81, differing from the PE25-[PPE41](/xray-mp-wiki/proteins/ppe41) structure where W56 of PPE41 makes van der Waals contacts with Y87 of PE25.


## Cross-References

- <a href="/xray-mp-wiki/proteins/secretion-translocon/pe25/">PE25</a> — PE25-[PPE41](/xray-mp-wiki/proteins/ppe41) heterodimer structure (PDB 2G38) was used as search model for EspB phasing
- <a href="/xray-mp-wiki/proteins/secretion-translocon/ppe41/">PPE41</a> — [PPE41](/xray-mp-wiki/proteins/ppe41) forms the heterodimer partner of PE25, structurally compared to EspB
- <a href="/xray-mp-wiki/concepts/construct-design/pe-ppe-fusion-proteins/">PE-PPE Fusion Proteins</a> — EspB is the archetypal PE-PPE fusion protein with a heterodimer-like fold
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/esx-1-secretion-system/">ESX-1 Secretion System</a> — EspB is a central secreted substrate of the ESX-1 type VII secretion system
- <a href="/xray-mp-wiki/concepts/protein-families/wxg100-family-proteins/">WxG100 Family Proteins</a> — EspB secretion mechanism is co-dependent with WxG100 proteins EsxA and EsxB
- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylserine/">Phosphatidylserine</a> — EspB binds [Phosphatidylserine](/xray-mp-wiki/reagents/lipids/phosphatidylserine) and crystallized with it as an additive
- <a href="/xray-mp-wiki/proteins/secretion-translocon/espg1/">EspG1</a> — EspG1 chaperone does not bind EspB, unlike PE25-[PPE41](/xray-mp-wiki/proteins/ppe41) heterodimer
- <a href="/xray-mp-wiki/proteins/secretion-translocon/mycp1/">MycP1</a> — [MycP1](/xray-mp-wiki/proteins/mycp1) protease cleaves full-length EspB to generate the mature 50 kDa isoform
- <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a> — Crystallization method used for structure determination
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-Exclusion Chromatography (SEC)</a> — Purification method used in protein preparation
