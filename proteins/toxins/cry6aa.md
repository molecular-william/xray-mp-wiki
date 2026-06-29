---
title: "Cry6Aa (Bacillus thuringiensis Pore-Forming Toxin)"
created: 2026-06-11
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography, enzyme]
sources: [doi/10.1186##s12915-016-0295-9]
verified: false
---

# Cry6Aa (Bacillus thuringiensis Pore-Forming Toxin)

## Overview

Cry6Aa is a pesticidal crystal (Cry) toxin from Bacillus thuringiensis with
activity against coleopteran insects (e.g., Western Corn Rootworm Diabrotica
virgifera virgifera) and a range of nematodes including Caenorhabditis elegans,
Heterodera [Glycine](/xray-mp-wiki/reagents/buffers/glycine/), and Meloidogyne incognita. The X-ray crystal structures
of Cry6Aa in both trypsin-cleaved (2.0 A) and full-length (2.7 A) forms reveal
that Cry6Aa belongs to the alpha-helical pore-forming toxin family,
structurally homologous to hemolysin E (HlyE) from E. coli, and the B. cereus
toxins HblB and NheA (pfam05791). This represents a new structural paradigm
among B. thuringiensis Cry toxins, distinct from the well-known three-domain
Cry toxins, the aegerolysin-like Cry34, the Toxin_10 family Cry35, the
Etx/Mtx2 family Cry51, and the Cyt family toxins. The structure consists of a
bundle of long (~90 A) amphipathic alpha helices with a head domain at one
end. The putative transmembrane region (residues 250-268) forms a hairpin loop
within the head domain. In vivo pore formation assays in C. elegans confirmed
the pore-forming mechanism of action. The L259D mutation in the putative
transmembrane region abolished toxicity, consistent with a pore-forming mode
of action.


## Publications

### doi/10.1186##s12915-016-0295-9

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5kuc">5KUC</a></td>
      <td>2.0</td>
      <td>P 65</td>
      <td>Trypsin-cleaved Cry6Aa core (residues 12-390 disulfide bonded to residues 444-475)</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5kud">5KUD</a></td>
      <td>2.7</td>
      <td>P 21 21 2</td>
      <td>Full-length Cry6Aa (residues Met1-Asn475)</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pseudomonas fluorescens (for crystallography); E. coli Shuffle T7 Express LysY (for recombinant production and bioassays); B. thuringiensis BMB171 (for native crystal production)
- **Construct**: Full-length Cry6Aa1 (GenBank AAA22357) from Dow AgroSciences
- **Notes**: Produced as inclusion bodies in P. fluorescens. Also soluble expression in E. coli Shuffle T7 with [Iptg](/xray-mp-wiki/reagents/additives/iptg/) induction.

**Purification:**

- **Expression system**: P. fluorescens (inclusion bodies)
- **Expression construct**: Full-length Cry6Aa1
- **Tag info**: Untagged

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
      <td>Inclusion body preparation</td>
      <td>Microfluidizer (16,000 psi, 2 passes)</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 7.5, 200 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.5% Triton X-100, 20 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a></td>
      <td>Washed multiple times with lysis buffer and <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> buffer</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Solubilization at pH 11.0</td>
      <td>—</td>
      <td>25 mM CAPS pH 11.0</td>
      <td>Inclusion bodies solubilized at high pH</td>
    </tr>
    <tr>
      <td>Anion exchange chromatography</td>
      <td>Ion exchange</td>
      <td>Source 15Q 16/10</td>
      <td>25 mM CAPS pH 11.0, with 0-1 M NaCl gradient</td>
      <td></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>Superdex 75 26/90</td>
      <td>25 mM CAPS pH 11.0, 50 mM NaCl</td>
      <td></td>
    </tr>
  </tbody>
</table>

- **Expression system**: B. thuringiensis BMB171
- **Expression construct**: Cry6Aa2 in pHT304
- **Tag info**: Untagged

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
      <td>Bt crystal production</td>
      <td>Growth in Embrapa medium to >98% autolysis</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Crystal purification</td>
      <td>Discontinuous <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> density gradient ultracentrifugation</td>
      <td>—</td>
      <td></td>
      <td>Cry6Aa crystals purified, then solubilized at pH 10.0 or pH 12.7 or pH 3.0</td>
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
      <td>Trypsin-cleaved Cry6Aa at 100 mg/mL in 25 mM CAPS pH 11.0, 50 mM NaCl</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 1000, 0.1 M sodium phosphate dibasic/citric acid pH 4.2, 0.2 M lithium sulfate</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected at LS-CAT (APS) on Mar CCD-300 detector at 100 K</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Full-length Cry6Aa</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Full-length structure solved at lower resolution (2.7 A). N-terminal 11 residues, C-terminal 6 residues, and some internal loops not resolved.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Cry6Aa is an alpha-helical pore-forming toxin

The structure of Cry6Aa reveals a bundle of five long (~90 A) amphipathic
alpha helices (alphaA, alphaC, alphaD, alphaG, alphaH) with a head domain
folded across one end. This fold is structurally homologous to hemolysin E
(HlyE/ClyA) from E. coli and the B. cereus hemolytic toxin components HblB
and NheA (pfam05791). Cry6Aa is the first B. thuringiensis Cry toxin
identified with this structural fold, representing a new paradigm among
pesticidal proteins.

### Pore-forming mechanism confirmed by in vivo assay

In vivo propidium iodide (PI) uptake assays in C. elegans demonstrated that
Cry6Aa forms pores in intestinal epithelial cells, with 41.5 +/- 9.7% of
treated worms showing PI entry compared to 1.1 +/- 1.1% for empty vector
control. Mutation of the putative transmembrane residue Leu259 to Asp
(L259D) abolished nematotoxicity, consistent with a pore-forming mechanism
of action.

### Unique structural features

Cry6Aa contains several unusual features not seen in homologous toxins:
(1) internal repeat sequences (WATIGAxI(E/Q), TTNMTSNQY, and C-terminal
WYNNSDWYNNSDWYNN repeats); (2) wing-like intra-helical loops bounded by
[Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residues in helices alphaC and alphaD; (3) two disulfide bonds
(Cys88-Cys451 and Cys402-Cys404) that confer conformational rigidity;
(4) a disulfide-linked C-terminal fragment that remains attached to the
toxin core after [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) activation. The C-terminal region is absent in
Cry6Ba, which has coleopteran activity but reduced nematode toxicity.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/alpha-helical-pore-forming-toxin-family/">Alpha-Helical Pore-Forming Toxin Family</a> — Cry6Aa is a founding member of this structural class among B. thuringiensis Cry toxins
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Trypsin-cleaved Cry6Aa structure solved by MR using hemolysin B (PDB 2NRJ) as search model
- <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> — Referenced in the context of Glycine
- <a href="/xray-mp-wiki/reagents/additives/iptg/">Iptg</a> — Referenced in the context of Iptg
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> — Referenced in the context of Tris Hcl
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in the context of Glycerol
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Referenced in the context of EDTA
- <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a> — Referenced in the context of TCEP
- <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> — Referenced in the context of Sucrose
- <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> — Referenced in the context of Peg
