---
title: "F1-ATPase from Fusobacterium nucleatum"
created: 2026-06-11
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1098##rsob.190066]
verified: agent
uniprot_id: ['Q8RGE0', 'Q8RGE1', 'Q8RGE2', 'Q8RGE3']
---

# F1-ATPase from Fusobacterium nucleatum

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8RGE0">UniProt: Q8RGE0</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8RGE1">UniProt: Q8RGE1</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8RGE2">UniProt: Q8RGE2</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8RGE3">UniProt: Q8RGE3</a>

<span class="expr-badge">Fusobacterium nucleatum subsp. nucleatum ATCC 25586</span>

## Overview

The [F1-ATPase from Trypanosoma brucei](/xray-mp-wiki/proteins/pumps-atpases/tbrucei-f1-atpase/) from Fusobacterium nucleatum is the water-soluble catalytic domain of the
F1Fo- synthase from the obligately anaerobic opportunistic periodontal pathogen
F. nucleatum. The F1-catalytic domain was expressed in E. coli, purified, and its crystal
structure determined at 3.6 A resolution. The enzyme can hydrolyse  but is partially
inhibited. The structure is similar to those of F1-ATPases from Caldalkalibacillus thermarum
(more strongly inhibited) and Mycobacterium smegmatis (very low  hydrolytic activity).
The betaE-subunit in all three enzymes is in the conventional 'open' state. In
F. nucleatum, occupancy by  in the betaE site appears to be partial (unlike
C. thermarum and M. smegmatis where betaE is occupied by  and phosphate/sulfate).
The hydrolytic activity is likely regulated by  concentration, as in mitochondria.


## Publications

### doi/10.1098##rsob.190066

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6q45">6Q45</a></td>
      <td>3.6</td>
      <td>P2_1</td>
      <td>F. nucleatum <a href="/xray-mp-wiki/proteins/pumps-atpases/tbrucei-f1-atpase/">F1-ATPase from Trypanosoma brucei</a> (alpha3beta3gammaepsilon subunits, His10-tagged epsilon-subunit)</td>
      <td> (alpha-subunits), +Mg2+ (betaTP, betaDP), partial  or  (betaE)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli DK8 (Delta-unc) with pRARE helper plasmid
- **Construct**: F. nucleatum atpAGDC genes (alpha, gamma, beta, epsilon) cloned into pTrc99a. His10-tag with TEV cleavage site on epsilon-subunit.
- **Notes**: Expressed from pJP3 and pJP5 constructs. Cells grown in 2x YT medium with , , 0.2% . Induced with 1 mM  at 37 C for 3-4 h then 16 h at 30 C.

**Purification:**

- **Expression system**: Escherichia coli DK8 (Delta-unc)
- **Expression construct**: F. nucleatum [F1-ATPase from Trypanosoma brucei](/xray-mp-wiki/proteins/pumps-atpases/tbrucei-f1-atpase/) with His10-TEV tag on epsilon-subunit
- **Tag info**: His10 tag on epsilon-subunit, cleavable by [TEV Protease (Tobacco Etch Virus Protease)](/xray-mp-wiki/reagents/additives/tev-protease/)

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
      <td>Cell lysis and membrane isolation</td>
      <td>French press or sonication</td>
      <td>—</td>
      <td>50 mM  Hcl]] pH 8.0, 100 mM NaCl, 20 mM , 10% , 2 mM </td>
      <td>Cells resuspended and lysed; membranes isolated by ultracentrifugation</td>
    </tr>
    <tr>
      <td>Nickel <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>50 mM  Hcl]] pH 8.0, 100 mM NaCl, 20-250 mM , 10% , 2 mM </td>
      <td>His10-tagged <a href="/xray-mp-wiki/proteins/pumps-atpases/tbrucei-f1-atpase/">F1-ATPase from Trypanosoma brucei</a> bound and eluted with  gradient</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease (Tobacco Etch Virus Protease)</a> cleavage</td>
      <td>On-column or dialysis cleavage</td>
      <td>—</td>
      <td></td>
      <td>His10 tag removed by <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease (Tobacco Etch Virus Protease)</a>; further polishing by <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, hanging drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>2-2.5 mg/ml <a href="/xray-mp-wiki/proteins/pumps-atpases/tbrucei-f1-atpase/">F1-ATPase from Trypanosoma brucei</a> in 20 mM  Hcl]] pH 8.0, 100 mM NaCl, 2 mM , 10% </td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM sodium  pH 6.0, 100 mM magnesium , 15.5% (w/v)  5000 monomethyl ether</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:0.8:0.2 (protein:precipitant:0.2% low melting-point agarose)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-4 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>30% (v/v) <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a> in reservoir buffer</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals harvested after 3-4 days. Diffraction data collected at Australian Synchrotron MX2 beamline. Four datasets merged due to radiation damage.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Partial ADP occupancy in betaE site

Unlike the F1-ATPases from C. thermarum and M. smegmatis where the betaE site is clearly occupied by  + phosphate (or sulfate), the betaE site in F. nucleatum shows only weak density that may be  at low occupancy or a molecule from the crystallization buffer. This partial occupancy correlates with the intermediate level of hydrolysis inhibition in F. nucleatum compared to C. thermarum (strong inhibition) and M. smegmatis (very low activity).

### ADP-dependent regulation of ATP hydrolysis

The  hydrolase activity of F. nucleatum [F1-ATPase from Trypanosoma brucei](/xray-mp-wiki/proteins/pumps-atpases/tbrucei-f1-atpase/) (specific activity 3.5 U/mg) was inhibited by Mg2+-: 2.5 mM Mg2+- inhibited 45% of activity, and 25 mM Mg2+- inhibited completely. Basal activity was stimulated 3-fold by 0.05% .  hydrolysis depended on Mg2+ or Ca2+ ions, with Ca2+ showing lower Km and higher Vmax than Mg2+. The enzyme is likely regulated by intracellular  concentration, similar to the mitochondrial enzyme.

### Structural comparison with other bacterial F1-ATPases

The F. nucleatum [F1-ATPase from Trypanosoma brucei](/xray-mp-wiki/proteins/pumps-atpases/tbrucei-f1-atpase/) structure (6q45) is most similar to M. smegmatis (6foc) and C. thermarum (5ik2) F1-ATPases. The gamma-subunit most closely resembles bacterial orthologues. The epsilon-subunit is in the 'down' conformation, with its two C-terminal alpha-helices lying alongside the beta-sandwich, similar to the epsilon-subunits from E. coli and C. thermarum. The betaE adenine-binding pocket has Phe-411 displaced outward by ~4 A relative to C. thermarum, explaining weaker nucleotide binding in the betaE site.

### Crystallization in sodium citrate explains potential citrate in betaE

The crystallization buffer contained 100 mM sodium  pH 6.0, and the weak density observed in the betaE nucleotide-binding site may be partially accounted for by a  molecule rather than . This ambiguity was noted by the authors and could not be definitively resolved at 3.6 A resolution.


## Cross-References

- <a href="/xray-mp-wiki/proteins/pumps-atpases/c-thermarum-f1-atpase/">F1-ATPase from Caldalkalibacillus thermarum</a> — Most similar F1-ATPase structure; betaE occupied by ADP+phosphate; used as MR search model
- <a href="/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/">Bovine F1-ATPase (Mitochondrial ATP Synthase Catalytic Domain)</a> — Homologous enzyme; F. nucleatum F1-ATPase regulation by ADP concentration similar to mitochondrial enzyme
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/f1-atpase-rotary-mechanism/">F1-ATPase Rotary Catalytic Mechanism</a> — The rotary catalytic mechanism is the fundamental operating principle of F1-ATPases
- <a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a> — Referenced in f-nucleatum-f1-atpase text
- <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> — Referenced in f-nucleatum-f1-atpase text
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate</a> — Referenced in f-nucleatum-f1-atpase text
- <a href="/xray-mp-wiki/reagents/additives/iptg/">Iptg</a> — Referenced in f-nucleatum-f1-atpase text
- <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a> — Referenced in f-nucleatum-f1-atpase text
- <a href="/xray-mp-wiki/reagents/antibiotics/chloramphenicol/">Chloramphenicol</a> — Referenced in f-nucleatum-f1-atpase text
- <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> — Referenced in f-nucleatum-f1-atpase text
