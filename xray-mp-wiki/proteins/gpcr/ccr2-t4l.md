---
title: "CC Chemokine Receptor 2 with T4 Lysozyme Fusion (CCR2-T4L)"
created: 2026-06-03
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature20605]
verified: agent
uniprot_id: P41597
---

# CC Chemokine Receptor 2 with T4 Lysozyme Fusion (CCR2-T4L)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P41597">UniProt: P41597</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

CC chemokine receptor 2 (CCR2) is a class A G protein-coupled receptor expressed on monocytes, immature dendritic cells, and T-cell subpopulations. It mediates cell migration towards CC chemokine ligands such as CCL2 and is implicated in inflammatory and neurodegenerative diseases including atherosclerosis, multiple sclerosis, asthma, neuropathic pain, and diabetic nephropathy. The CCR2-T4L construct is an engineered version of human CCR2 isoform B with T4 lysozyme (T4L) inserted into the third intracellular loop (ICL3), enabling crystal structure determination at 2.8 A resolution. This structure revealed both an orthosteric and a novel intracellular allosteric antagonist binding site.


## Publications

### doi/10.1038##nature20605

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5t1a">5T1A</a></td>
      <td>2.80</td>
      <td>P212121</td>
      <td>Human CCR2 isoform B (Uniprot P41597-2) with C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation">Truncation</a> (residues 329-360 removed) and T4 lysozyme (T4L) inserted into ICL3. Native CCR2 residues L226(5.62)-R240(6.32) replaced with M2 muscarinic receptor residues (PDB 3UON): S226(5.62)-RASKSRI-T4L-PPPSREK-K240(6.32). N-terminal HA signal sequence, Flag tag, PreScission protease site, and C-terminal 10xHis tag plus Flag tag. Crystallized in ternary complex with orthosteric antagonist BMS-681 and allosteric antagonist CCR2-RA-[R].</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/bms-681">Bms 681</a> (orthosteric antagonist), CCR2-RA-[R] (allosteric antagonist)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (Spodoptera frugiperda), baculovirus expression system
- **Construct**: CCR2-T4L coding sequence cloned into modified pFastBac1 vector with HA signal sequence, N-terminal Flag tag, PreScission protease site, and C-terminal 10xHis tag plus Flag tag. High-titre recombinant baculovirus (>10^9 viral particles/mL) obtained using Bac-to-Bac Baculovirus Expression System (Invitrogen). Sf9 cells infected at 2-3 x 10^6 cells/mL with P1 virus at multiplicity of infection of 5. Cells harvested 48 h post-infection, stored at -80 C.

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
      <td>Cell lysis and membrane preparation</td>
      <td>Hypotonic buffer lysis with repeated douncing and centrifugation</td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 10 mM MgCl2, 20 mM KCl, EDTA-free protease inhibitor + --</td>
      <td>Membranes washed in hypotonic buffer, then in high osmotic buffer (1.0 M NaCl) to separate soluble from integral membrane proteins</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Solubilization of membranes with detergent</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 400 mM NaCl + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, 0.2% (w/v) <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Solubilized at 4 C for 3 h with 50 uM BMS-681 and 2 mg/mL <a href="/xray-mp-wiki/reagents/additives/iodoacetamide">Iodoacetamide</a>; clarified by centrifugation at 50,000g for 30 min</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> IMAC (Ni-IMAC)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> IMAC resin (Clontech)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 400 mM NaCl + --</td>
      <td>Incubated with resin overnight at 4 C; washed without ligands with ten column volumes of Wash I Buffer (50 mM HEPES pH 7.5, 400 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">ddm</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)); eluted with <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> gradient</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/))</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a> (LCP matrix)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal also contains a Zn2+ ion coordinated by H144(3.56) from CCR2, E238(6.30) from engineered region, and E1005 from T4L, identified by X-ray fluorescence emission analysis</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Protein:lipid ratio</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein (LCP matrix)</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5t1a">5T1A</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDDKPGTLSTSRSRFIRNTNESGEEVTTFFDYDYGAPCHKFD</span><span class="topo-inside">VKQIGAQL</span><span class="topo-membrane">LPPLYSLVFIFGFVGNMLVVLILIN</span><span class="topo-outside">CKKLKCLT</span><span class="topo-membrane">DIYLLNLAISDLLFLITLPLWAH</span><span class="topo-inside">SAANEWVFGN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">A</span><span class="topo-membrane">MCKLFTGLYHIGYFGGIFFIILLTID</span><span class="topo-outside">RYLAIVHAVFALKARTVTF</span><span class="topo-membrane">GVVTSVITWLVAVFASVPGIIFT</span><span class="topo-inside">KCQKEDSVYVCGPYFPRG</span><span class="topo-membrane">WNNFHTIMRNILGLVLPLLIMVICYS</span><span class="topo-outside">GISRASK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">SRINIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">RMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYPPPSREKKAV</span><span class="topo-membrane">RVIFTIMIVYFLFWTPYNIVILLNTFQ</span><span class="topo-inside">EFFGLSNCESTSQLDQA</span><span class="topo-membrane">TQVTETLGMTHCCINPIIYAFVG</span></span>
<span class="topo-ruler">       490       500        </span>
<span class="topo-line"><span class="topo-outside">EKFRRYLSVFF</span><span class="topo-unknown">RKHITKRFGRPLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>46</td>
      <td>-9</td>
      <td>36</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>47</td>
      <td>54</td>
      <td>37</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>79</td>
      <td>45</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>87</td>
      <td>70</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>110</td>
      <td>78</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>111</td>
      <td>121</td>
      <td>101</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>147</td>
      <td>112</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>166</td>
      <td>138</td>
      <td>156</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>189</td>
      <td>157</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>207</td>
      <td>180</td>
      <td>197</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>233</td>
      <td>198</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>243</td>
      <td>224</td>
      <td>233</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>404</td>
      <td>1002</td>
      <td>1162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>405</td>
      <td>413</td>
      <td>234</td>
      <td>242</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>414</td>
      <td>440</td>
      <td>243</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>441</td>
      <td>457</td>
      <td>270</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>480</td>
      <td>287</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>481</td>
      <td>491</td>
      <td>310</td>
      <td>320</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>492</td>
      <td>508</td>
      <td>321</td>
      <td>337</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Novel intracellular allosteric pocket in CCR2

CCR2-RA-[R] binds in a highly enclosed allosteric pocket more than 30 A away from the orthosteric site, located at the intracellular side caged by helices I-III and VI-VIII. This pocket buries 297.8 A^2 of surface area and is formed by hydrophobic residues (V63^1.53, L67^1.57, L81^2.43, L134^3.46, A241^6.33, V244^6.36, I245^6.37, Y305^7.53, F312^8.50) and polar residues (T77^2.39, R138^3.50, G309^8.47, K311^8.49, Y315^8.53). This site overlaps the G-protein-binding interface in homologous GPCRs, representing the most intracellular allosteric site observed in class A GPCRs to date. The pocket is druggable due to balanced hydrophobic and polar features.

### Bi-directional allosteric communication between orthosteric and allosteric sites

[Bms 681](/xray-mp-wiki/reagents/ligands/bms-681) and CCR2-RA-[R] cooperatively stabilize an inactive conformation of CCR2. BMS-681 occupies the orthosteric pocket and prevents chemokine binding, while CCR2-RA-[R] prevents G-protein coupling at the intracellular allosteric site. This creates bi-directional communication: BMS-681 allosterically inhibits CCL2 binding (which requires active receptor), while CCR2-RA-[R] sterically blocks G-protein binding. The double-antagonist-bound structure shows pronounced inactive-state conformational signatures, including the most inactive GPCR conformation solved to date.

### Inactive-state conformational microswitches

Double-antagonist-bound CCR2 exhibits the full inactive-state conformational signature: intracellular ends of TM3 and TM6 are close together, conserved R138^3.50 (DRY motif) interacts with D137^3.49 and T77^2.39, Y305^7.53 (NPxxY motif) is twisted outward toward TM2, and helix VII is in a repositioned inactive conformation. This contrasts with agonist-bound active states (e.g., US28) where helix VI moves outward and Y7.53 rotates inward. The double-antagonist structure represents the most inactive chemokine receptor conformation solved.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/bms-681/">BMS-681</a> — Co-crystallized orthosteric antagonist; occupies orthosteric pocket
- <a href="/xray-mp-wiki/reagents/ligands/ccr2-ra-r/">CCR2-RA-[R]</a> — Co-crystallized allosteric antagonist; binds intracellular allosteric pocket
- <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4 Lysozyme (T4L)</a> — Fusion partner inserted into ICL3 for crystallization
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Primary lipid component of LCP crystallization matrix
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent for membrane solubilization
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesterol Hydrogen Succinate (CHS)</a> — Co-detergent used during solubilization and purification
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> — Ni-IMAC resin used for His-tag affinity purification
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Primary crystallization method used
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation">Protein Truncation for Crystallization</a> — Entity mentioned in overview or biological insights
- <a href="/xray-mp-wiki/reagents/additives/iodoacetamide">Iodoacetamide</a> — Entity mentioned in overview or biological insights
