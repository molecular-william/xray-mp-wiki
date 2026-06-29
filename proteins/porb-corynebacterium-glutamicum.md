---
title: "Porin B (PorB) from Corynebacterium glutamicum"
created: 2026-05-26
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [porin, membrane-protein, xray-crystallography]
sources: [doi/10.1016##JMB.2008.04.017]
verified: false
---

# Porin B (PorB) from Corynebacterium glutamicum

## Overview

Porin B (PorB) is an alpha-helical porin from Corynebacterium glutamicum, a mycolata bacterium with a mycolic acid cell wall layer similar to the outer membrane of Gram-negative bacteria. PorB forms an anion-selective channel in the bacterial outer envelope. The crystal structure was determined at 1.8 A resolution (crystal form I) using a platinum derivative for phasing, with 16 independent molecular structures solved in four different crystal forms. The core structure consists of 70 residues forming four alpha-helices tied together by a disulfide bridge (Cys22-Cys81). The native channel is proposed to be a pentameric oligomer based on conductivity measurements and crystal packing analysis. This is the first reported alpha-helical porin in a bacterial outer envelope, as all other known porins from mycolata consist of beta-barrels.

## Publications

### doi/10.1016##JMB.2008.04.017

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2k5a">2K5A</a></td>
      <td>1.8 A (Form I), 2.9 A (Form II), 3.2 A (Form III), 4.2 A (Form IV)</td>
      <td>P41212 (I), P6522 (II), P43212 (III), P6422 (IV)</td>
      <td>Mature PorB (99 residues, 10,638 Da); 70-residue core (residues 18-87) defined in all forms</td>
      <td>42 Zn2+ ion sites; platinum derivative; <a href="/xray-mp-wiki/reagents/buffers/cacodylate/">cacodylate</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli (recombinant expression as GST fusion)
- **Construct**: PorB fused to glutathione S-transferase (GST), cleaved with [factor Xa](/xray-mp-wiki/reagents/enzymes/factor-xa/) protease; 3 additional N-terminal linker residues (Gly, Ile, Leu) retained

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
      <td>GST affinity chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a> using GST affinity column (GE Healthcare)</td>
      <td>Glutathione-Sepharose</td>
      <td>Buffer A: 140 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">sodium chloride</a>, 2.7 mM KCl, 10 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">sodium phosphate</a> pH 7.3, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF</a>, Benzonase</td>
      <td>GST fusion protein expressed in E. coli; cleaved on-column with factor Xa (11 U per gram wet cells) in buffer B</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a> using S75-26/60 SEC column (GE Healthcare)</td>
      <td>Sephacryl S-75</td>
      <td>150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">sodium chloride</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>-HCl pH 8.0</td>
      <td>Separated monomer (11 +/- 2 kDa, major peak) from dimer/trimer (29 +/- 3 kDa, minor peak); only monomer peak yielded analyzable crystals. Purification performed without detergent.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop and hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PorB monomer peak at 1.0-3.5 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Multiple crystal forms with different conditions (see Tables in paper); screens from <a href="/xray-mp-wiki/reagents/crystallization-hampton-research/">Hampton Research</a>, Jena Bioscience, and Emerald</td>
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
      <td>Reservoir buffer with <a href="/xray-mp-wiki/reagents/additives/mpd/">MPD</a> increased by 2% (v/v); shock-frozen in nitrogen at 100 K</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Four crystal forms obtained from monomer peak material; dimer/trimer peak yielded only disordered crystals. Platinum derivatives obtained by adding solid K2Pt(NO2)4 to the drop.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Pentameric channel model

The native PorB channel is proposed as a C5-symmetric pentamer based on conductivity measurements (0.7 nS), anion selectivity, and crystal packing analysis. Contact type C from crystal forms (polar interior, nonpolar exterior) was expanded from C2 to C5 symmetry. The channel is ~40 A long, matching the [mycolic acid](/xray-mp-wiki/concepts/mycolic-acid/) layer thickness. Arg42 defines the channel constriction. The channel is inactivated by [citrate](/xray-mp-wiki/reagents/buffers/citrate/) (chelating divalent cations) and by EDTA (~35 mM), suggesting the native channel is stabilized by divalent metal ion cross-links.

### Alpha-helical porin architecture

PorB represents a novel porin architecture: all four alpha-helices surround a nonpolar interior with a conserved disulfide bridge (Cys22-Cys81). The strictly conserved core residues (Cys22, Gly33, Leu44, Ala45, Ala75, Arg77, Ala78, Cys81, Gly82, Val84) maintain structural stability. The N- and C-terminal extensions (29 residues total) are highly variable in conformation across crystal forms but conserved in sequence, suggesting a role in oligomerization.


## Cross-References

- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — SEC used to separate monomer from dimer/trimer peaks using Sephacryl S-75 column
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — GST affinity column (Glutathione-Sepharose) used for initial purification
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl buffer)</a> — Used in SEC buffer (50 mM Tris-HCl pH 8.0)
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride (NaCl)</a> — Major salt component in all purification buffers
- <a href="/xray-mp-wiki/reagents/additives/calcium-chloride/">Calcium Chloride (CaCl2)</a> — Required for factor Xa cleavage (1 mM CaCl2 in buffer B)
- <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF (Phenylmethylsulfonyl fluoride)</a> — Used as protease inhibitor during cell lysis (0.1 mM)
- <a href="/xray-mp-wiki/reagents/buffers/cacodylate/">Cacodylate (Sodium Dimethylarsenate)</a> — Observed as bound ligand in crystal form I contact type C dimers alongside Zn2+ ion sites
- <a href="/xray-mp-wiki/reagents/additives/mpd/">MPD (2-Methyl-2,4-pentanediol)</a> — Used as cryoprotectant for all crystal forms (increased by 2% v/v)
