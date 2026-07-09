---
title: "UlaA Vitamin C Transporter (E. coli)"
created: 2026-06-09
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.2975]
verified: regex
uniprot_id: P04637
---

# UlaA Vitamin C Transporter (E. coli)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P04637">UniProt: P04637</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

UlaA is the membrane-embedded transporter component of the phosphoenolpyruvate-dependent phosphotransferase system (PTS) for vitamin C (L-ascorbic acid) uptake in Escherichia coli. It belongs to the PTS-AG (ascorbate and galactitol) superfamily and, together with the IIB-like UlaB and IIA-like UlaC enzymes, is responsible for the anaerobic uptake of vitamin C and its phosphorylation to L-ascorbate 6-phosphate. UlaA forms a homodimer and exhibits a completely new fold consisting of 11 transmembrane segments arranged into a 'V-motif' domain and a 'core' domain. The V motifs form the dimer interface, and the core-domain residues coordinate vitamin C. The crystal structures of UlaA in two conformations — outward-open (1.65 A, C2 space group) and occluded (2.35 A, P2_1 space group) — reveal that substrate transport may occur via an 'elevator' mechanism involving rigid-body rotation of the core domain relative to the V-motif domain.

## Publications

### doi/10.1038##nsmb.2975

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4rp7">4RP7</a></td>
      <td>1.65 A</td>
      <td>C2</td>
      <td>Full-length E. coli UlaA (residues 1-441) with C-terminal His8 tag; limited <a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> proteolysis removed C-terminal 7 residues and His8 tag during crystallization; purified in <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> (DM) and crystallized with <a href="/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/">NG</a> (beta-NG) additive</td>
      <td>L-Ascorbic acid (vitamin C) bound at the core-domain substrate-binding site</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4rp6">4RP6</a></td>
      <td>2.35 A</td>
      <td>P2_1</td>
      <td>Full-length E. coli UlaA (residues 1-441); same construct as C2 form; crystallized with beta-NG additive</td>
      <td>L-Ascorbic acid (vitamin C) bound at the core-domain substrate-binding site</td>
    </tr>
  </tbody>
</table>
 - Data collection: Data collected at SSRF BL17U, SPring-8 BL41XU, or NSLS X29A; processed with HKL2000; structure solved by [MIRAS](/xray-mp-wiki/methods/structure-determination/miras/) using gold and platinum derivatives
 - Data collection: Data collected at SSRF BL17U, SPring-8 BL41XU, or NSLS X29A; processed with HKL2000; structure solved by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/) using C2 form as search model

**Expression:**

- **Expression system**: E. coli C43(DE3) cells
- **Construct**: Full-length UlaA from E. coli with C-terminal His8 tag; cloned into pET15b or pET21b vectors

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
      <td>Cell culture and induction</td>
      <td>Bacterial expression</td>
      <td></td>
      <td></td>
      <td>C43(DE3) cells grown to OD600 ~1.2; induced with 0.2 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a></td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>French press</td>
      <td></td>
      <td>25 mM Tris-Cl pH 8.0, 150 mM NaCl</td>
      <td>Two passes at 15,000 p.s.i.; low-speed spin followed by high-speed ultracentrifugation to isolate membranes</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent extraction</td>
      <td></td>
      <td>25 mM Tris-Cl pH 8.0, 150 mM NaCl + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/nm/">NM</a> (NM)</td>
      <td>Incubated for 1 h at 4 C; insoluble material removed by centrifugation</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA agarose</td>
      <td>25 mM Tris-Cl pH 8.0, 150 mM NaCl, 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.3% NM</td>
      <td>Protein eluted with <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; concentrated for gel filtration</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>25 mM Tris-Cl pH 8.0, 150 mM NaCl, 2 mM ascorbic acid + 0.3% NM</td>
      <td>Peak fraction collected for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Truncated UlaA (C-terminally cleaved) purified in 1.0% (w/v) n-octyl-beta-D-glucopyranoside (beta-OG)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M MES pH 6.5, 0.1 M NaCl, 30% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>5 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Direct flash freezing in cold nitrogen stream at 100 K</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Initial C2 crystals diffracted to 4 A. Resolution improved to 1.65 A (C2) and 2.35 A (P2_1) by adding <a href="/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/">NG</a> (beta-NG) at 0.4% (v/v) final concentration. Platinum or gold derivatives obtained by soaking native crystals in 10 mg/ml K2Pt(NO2)4 or 2 mg/ml KAu(CN)2 for 2 h.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### First structure of the PTS-AG superfamily

UlaA is the first determined structure of any member of the PTS-AG (ascorbate and galactitol) superfamily. The structure reveals a completely new fold distinct from the previously solved PTS-GFL superfamily member ChbC. Each UlaA protomer contains 11 transmembrane segments organized into a V-motif domain (TM1-5) and a core domain (TM6-11, including two reentrant hairpins HP1 and HP2). The V motifs form the dimer interface, while the core domains contain the substrate-binding site.

### Vitamin C coordination and binding

Vitamin C (L-ascorbic acid) is bound at the interface between the V-motif and core domains through polar and van der Waals contacts. The substrate is deeply buried in a pocket formed by residues from the core domain. The high-resolution 1.65 A structure reveals precise coordination geometry involving hydrogen bonds and hydrophobic interactions that confer specificity for L-ascorbic acid with low-micromolar affinity (Km ~9 uM).

### Elevator transport mechanism

Comparison of the outward-open (C2) and occluded (P2_1) conformations suggests that UlaA employs an 'elevator' mechanism for substrate transport. The V-motif domain remains largely stationary while the core domain undergoes a rigid-body rotation of approximately 4.33 degrees relative to the V motif, with a maximum atom translation of ~7 A. The substrate-binding site within the core domain is not perturbed during this movement. This mechanism is a specialized form of the alternating-access mechanism, similar to sugar transport in the PTS-GFL transporter ChbC.

### Domain architecture and dimer interface

UlaA functions as a homodimer, with the V motifs from each protomer forming the dimer interface. The core domain from each protomer is organized around the substrate-binding site. The domain architecture features V motif 1 (cyan), core 1 (yellow), V motif 2 (magenta), core 2 (orange), and TM11 (gray) subdomains. The contracted lengthy loop connecting HP2a and AH2 likely stretches to keep the V-motif and core domains together during elevator motion.

### Structural distinction from PTS-GFL transporters

The UlaA fold is completely different from that of ChbC (a GFL superfamily PTS transporter), demonstrating that the PTS-AG and PTS-GFL superfamilies have distinct evolutionary origins despite performing similar functions. UlaA homologs are found in numerous human and animal pathogens but not in archaea or eukaryotes, making UlaA a potential antimicrobial target.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/uraA/">Uracil:Proton Symporter UraA (E. coli)</a> — Both are E. coli transporters; UraA belongs to the NAT/NCS2 family, which includes mammalian vitamin C transporters (SVCT1/SVCT2)
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/">Elevator Transport Mechanism</a> — Central mechanistic finding of this paper; proposed elevator mechanism for substrate translocation
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — General framework for transporter function; elevator mechanism is a specialized form
- <a href="/xray-mp-wiki/reagents/ligands/ascorbic-acid/">L-Ascorbic Acid (Vitamin C)</a> — Physiological substrate of UlaA; bound in both crystal structures
- <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion-hanging-drop/">Hanging-Drop Vapor Diffusion Crystallization</a> — Crystallization method used for UlaA
- <a href="/xray-mp-wiki/methods/structure-determination/miras/">Multiple Isomorphous Replacement with Anomalous Scattering (MIRAS)</a> — Experimental phasing method used for initial UlaA structure
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
