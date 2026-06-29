---
title: "AvGluR1 Ligand-Binding Domain (LBD)"
created: 2026-05-28
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2013.01.006]
verified: false
---

# AvGluR1 Ligand-Binding Domain (LBD)

## Overview

The ligand-binding domain (LBD) of AvGluR1, an ionotropic glutamate receptor from the freshwater bdelloid rotifer Adineta vaga. AvGluR1 is proposed as an evolutionary link between prokaryotic and eukaryotic iGluRs, possessing both an amino-terminal domain and three membrane-spanning segments with the SYTAN motif characteristic of AMPA, kainate, and NMDA receptors. The LBD exhibits unusual ligand binding properties, accommodating chemically diverse amino acids including alanine, cysteine, methionine, and phenylalanine alongside glutamate, aspartate, and serine. A key discovery is that [Chloride Ion](/xray-mp-wiki/reagents/additives/chloride/) ions act as surrogate ligand atoms, replacing the gamma-carboxyl group for neutral amino acids.


## Publications

### doi/10.1016##j.str.2013.01.006

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4io2">4IO2</a></td>
      <td>1.37</td>
      <td>P21</td>
      <td>S1 A433-K543 + GT linker + S2 L656-P788</td>
      <td>L-glutamate</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4io3">4IO3</a></td>
      <td>1.66</td>
      <td>P21</td>
      <td>S1 A433-K543 + GT linker + S2 L656-P788</td>
      <td>L-aspartate</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4io4">4IO4</a></td>
      <td>1.94</td>
      <td>P21</td>
      <td>S1 A433-K543 + GT linker + S2 L656-P788</td>
      <td>L-serine</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4io5">4IO5</a></td>
      <td>1.72</td>
      <td>P21</td>
      <td>S1 A433-K543 + GT linker + S2 L656-P788</td>
      <td>L-alanine</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4io6">4IO6</a></td>
      <td>1.60</td>
      <td>P21</td>
      <td>S1 A433-K543 + GT linker + S2 L656-P788</td>
      <td>L-methionine</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4io7">4IO7</a></td>
      <td>1.92</td>
      <td>P21</td>
      <td>S1 A433-K543 + GT linker + S2 L656-P788</td>
      <td>L-phenylalanine</td>
    </tr>
  </tbody>
</table>
 - Data collection: SER-CAT 22-ID beamline, APS, Advanced Photon Source
 - Data collection: SER-CAT 22-ID beamline, APS, Advanced Photon Source
 - Data collection: SER-CAT 22-ID beamline, APS, Advanced Photon Source
 - Data collection: SER-CAT 22-ID beamline, APS, Advanced Photon Source
 - Data collection: SER-CAT 22-ID beamline, APS, Advanced Photon Source
 - Data collection: SER-CAT 22-ID beamline, APS, Advanced Photon Source

**Expression:**

- **Expression system**: Escherichia coli Origami B(DE3)
- **Construct**: S1 residues A433-K543 connected via a GT dipeptide linker to S2 residues L656-P788, with N-terminal MH8SSGLVPRGS affinity tag and thrombin cleavage site
- **Induction**: 30 uM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) for 15 hr at 18 C
- **Media**: pET22b vector

**Purification:**

- **Expression system**: E. coli Origami B(DE3)
- **Expression construct**: S1 A433-K543 + GT linker + S2 L656-P788, N-terminal MH8SSGLVPRGS affinity tag
- **Tag info**: MH8SSGLVPRGS [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/) with [Thrombin](/xray-mp-wiki/reagents/additives/thrombin/) cleavage site

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
      <td>Cell lysis and solubilization</td>
      <td>Bacterial cell lysis, soluble fraction isolated</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>Soluble fraction from bacterial cell lysates</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Resin</a></td>
      <td>N/A</td>
      <td>N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His Tag</a> purification</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Thrombin cleavage</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>Extended native N-terminal sequence by four residues (ARLK) to enable <a href="/xray-mp-wiki/reagents/additives/thrombin/">Thrombin</a> cleavage</td>
    </tr>
    <tr>
      <td>Ion exchange chromatography</td>
      <td>SP sepharose ion exchange</td>
      <td>SP sepharose</td>
      <td>N/A</td>
      <td>Final purification step</td>
    </tr>
  </tbody>
</table>
**Yield**: 8-10 mg from 12 L cultures

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>AvGluR1 LBD with <a href="/xray-mp-wiki/reagents/substrates/l-glutamate/">L-Glutamate</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized as back-to-back dimers, canonical arrangement found in full-length GluA2. P21 space group</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Unusual ligand binding profile

AvGluR1 LBD binds glutamate with Kd 203 +/- 18 nM, comparable to GluR0 from Synechocystis (193 nM) but distinct from GluA2 AMPA receptor (821 nM). It shows preference for kainate-receptor-like binding, with higher affinity for the kainate receptor-preferring agonist SYM2081 (Kd 49.5 uM) and the GluK1-preferring antagonist UBP-310 (Kd 160 uM). It binds AMPA (Kd 130 uM) and quisqualate (Kd 39 uM) but has very low affinity for kainate (Kd 2.7 mM) and NMDA (Kd 9.9 mM). Uniquely, AvGluR1 is activated by neutral amino acids alanine, cysteine, methionine, and phenylalanine in addition to acidic amino acids glutamate and aspartate.

### Chloride ions act as surrogate ligand atoms

Crystal structures of alanine, serine, and methionine complexes reveal that [Chloride Ion](/xray-mp-wiki/reagents/additives/chloride/) ions occupy positions equivalent to the gamma-carboxyl group oxygen atoms in the glutamate complex. In the alanine complex, a Cl- ion is coordinated by Arg676 side chain, the main chain amide of Asp720, and water molecules W3 and W7. In the serine complex, the Cl- ion is displaced by 2.3 A and coordinated by both Arg702 and Arg676 side chains and the main-chain amide of Asp720. Removal of Cl- lowers affinity for alanine (53-fold) and serine (19-fold) but not for glutamate or aspartate. The methionine affinity decreases only 18-fold in [HEPES](/xray-mp-wiki/reagents/buffers/hepes/) buffer despite strong Cl- electron density, suggesting methionine can adopt an alternative rotamer.

### Prokaryotic iGluR-like features

The AvGluR1 LBD has a two-domain closed-cleft clamshell structure typical of iGluRs. It shares deletions with bacterial iGluRs, lacking loop 2 and alpha helix G that are present in AMPA and kainate receptor LBDs. A structure-based phylogenetic analysis reveals clustering of AvGluR1 with bacterial iGluRs rather than vertebrate iGluRs. However, AvGluR1 has a large amino-terminal domain like eukaryotic iGluRs and shows weak LBD self-association in solution (similar to eukaryotic iGluRs), despite phylogenetic clustering with bacterial receptors.

### Dimer assembly and desensitization

AvGluR1 LBD amino acid complexes crystallized as back-to-back dimers with a buried surface of 1,305 A2 per subunit. The dimer interface is formed primarily by polar interactions between alpha helices C and H, with salt bridges between Arg523-Asp762, Glu524-Lys759, and Asp743-Arg769. The dimer has an upright orientation (45 degrees between alpha helix H vectors) compared to the GluA2 dimer (61 degrees), similar to the bacterial GluR0 dimer. Introduction of Cys mutations at Ser520 and Leu766 (S520C/L766C) to form disulfide crosslinks abolishes desensitization completely, consistent with the model that LBD dimer rupture drives desensitization.

### Desensitization attenuated by concanavalin A

Treatment with [Concanavalin A](/xray-mp-wiki/reagents/additives/concanavalin-a/) (0.5 mg/ml for 4 min) strongly attenuates desensitization of AvGluR1, similar to the effect on kainate receptors in mammalian iGluRs. This is consistent with the greater sequence similarity of AvGluR1 to kainate versus AMPA receptors and the larger number of predicted N-linked glycosylation sites in AvGluR1 compared to GluA2.


## Cross-References

- <a href="/xray-mp-wiki/reagents/substrates/l-glutamate/">L-Glutamate</a> — Primary orthosteric ligand of AvGluR1 with Kd 203 nM
- <a href="/xray-mp-wiki/reagents/substrates/l-aspartate/">L-Aspartate</a> — Acidic amino acid ligand binding to AvGluR1 LBD
- <a href="/xray-mp-wiki/reagents/substrates/l-alanine/">L-Alanine</a> — Neutral amino acid ligand using chloride ion as surrogate
- <a href="/xray-mp-wiki/reagents/substrates/l-serine/">L-Serine</a> — Neutral amino acid ligand using chloride ion as surrogate
- <a href="/xray-mp-wiki/reagents/ligands/l-methionine/">L-Methionine</a> — Neutral amino acid ligand with reduced chloride dependence
- <a href="/xray-mp-wiki/reagents/ligands/l-phenylalanine/">L-Phenylalanine</a> — Hydrophobic amino acid ligand that occludes anion binding site
- <a href="/xray-mp-wiki/proteins/other-ion-channels/glua2-lbd/">GluA2 LBD</a> — AMPA receptor LBD used for structural comparison of dimer assembly
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/allosteric-regulation/">Allosteric Regulation</a> — ATD-LBD linker conformation and allosteric regulation of activation
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Referenced in avglur1
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Nickel Sepharose</a> — Referenced in avglur1
