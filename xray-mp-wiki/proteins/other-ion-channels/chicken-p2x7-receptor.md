---
title: "Chicken P2X7 Receptor (ckP2X7)"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-017-00887-9]
verified: agent
uniprot_id: E1C6P3
---

# Chicken P2X7 Receptor (ckP2X7)

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/E1C6P3">UniProt: E1C6P3</a>

<span class="expr-badge">Gallus gallus</span>

## Overview

The P2X7 receptor is an [ATP](/xray-mp-wiki/reagents/ligands/atp/)-gated non-selective cation channel belonging to the P2X receptor family, which plays a crucial role in the immune and nervous systems. It is mainly expressed in immune cells including macrophages and lymphocytes, where its activation stimulates the release of proinflammatory cytokines. The chicken P2X7 receptor (ckP2X7) structure was determined in complex with the competitive antagonist TNP-[ATP](/xray-mp-wiki/reagents/ligands/atp/), revealing an expanded, incompletely activated conformation distinct from both the apo closed and [ATP](/xray-mp-wiki/reagents/ligands/atp/)-bound open states. TNP-[ATP](/xray-mp-wiki/reagents/ligands/atp/) acts as a wedge, with its trinitrophenyl group inserted between the head and dorsal fin domains to prevent the complete cleft closure motion required for channel activation. The structure provides mechanistic insights into competitive antagonist action and facilitates interpretation of disease-associated SNPs in the human P2X7 receptor.

## Publications

### doi/10.1038##s41467-017-00887-9

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5xw6">5XW6</a></td>
      <td>3.1</td>
      <td>P4(1)2(1)2</td>
      <td>Chicken P2X7 crystallization construct (ckP2X7_cryst) with N-terminal GFP-His8 tag (removed by TEV cleavage) and Endo H deglycosylation, in complex with TNP-<a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a></td>
      <td>TNP-<a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293S GnTI(-)
- **Construct**: Chicken P2X7 (NCBI XP_001235163) expressed in HEK293S GnTI- cells via [PEG (Polyethylene Glycol)](/xray-mp-wiki/reagents/additives/peg/) BacMam vector with N-terminal GFP-His8 tag, TEV cleavage site, and GSGS linker

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
      <td>Sonication</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 8.0, 150 mM NaCl + --</td>
      <td>Supplemented with aprotinin, leupeptin, and pepstatin A</td>
    </tr>
    <tr>
      <td>Membrane collection</td>
      <td>Ultracentrifugation</td>
      <td>--</td>
      <td>-- + --</td>
      <td>138,000 x g, 1 h, 4°C</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 8.0, 150 mM NaCl, 2 mM CaCl2, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>1 h at 4°C; 0.2 U/mL apyrase added</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON Cobalt Affinity Resin</a> (Co2+)</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 8.0, 150 mM NaCl + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Washed with 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, eluted with 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag removal and deglycosylation</td>
      <td>Enzymatic digestion</td>
      <td>--</td>
      <td>-- + --</td>
      <td><a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease digestion and Endo H treatment</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase 10/300 GL</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.0, 100 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Final purification step</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Co-crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified ckP2X7_cryst in 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.0, 100 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> 3350, 0.2 M sodium-potassium phosphate, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals flash-cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Co-crystallized with TNP-<a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a>. X-ray data collected at 100 K at beamline X06SA-PXI (SLS). Structure solved by molecular replacement using the amP2X structure (PDB 4DW0) as search model.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Peg: 20 % [precipitant]  
- Glycerol: 10 % [additive]</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5xw6">5XW6</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSGSG</span><span class="topo-outside">SCV</span><span class="topo-membrane">KWFIYGVIAVYICYTLIVHK</span><span class="topo-inside">RYQEKEELTSSVRVTLKGVAHVDRIWDAAEYTIPTQTRDSFFVMTNIIRTENQIQKTCPEYPTAKAICSSDKSCAKGIVDVHSNGVQTGKCV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">HYNITHKTCEIKAWCPVQGEERPPVPAVLRSSEDFTVFIKNNIHFPTFQYTVQNISPKLNTSCKFNKVTAPLCPIFRLGDILQEAKENFSEMAVKGGIIAIEIKWDCDLDSWSYYCSPEY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       </span>
<span class="topo-line"><span class="topo-inside">SFRRLDDKTRTQYPGFSIRFARHYKLPDGTEQRTLFKAYGIRFDVLVFGMGG</span><span class="topo-membrane">QFKLIELFTFIGSTIAYFGLAVTII</span><span class="topo-outside">EMCFHLYN</span><span class="topo-unknown">LE</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>6</td>
      <td>8</td>
      <td>27</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>30</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>292</td>
      <td>50</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>317</td>
      <td>314</td>
      <td>338</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>318</td>
      <td>325</td>
      <td>339</td>
      <td>346</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5xw6">5XW6</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSGSG</span><span class="topo-outside">SCV</span><span class="topo-membrane">KWFIYGVIAVYICYTLIVHK</span><span class="topo-inside">RYQEKEELTSSVRVTLKGVAHVDRIWDAAEYTIPTQTRDSFFVMTNIIRTENQIQKTCPEYPTAKAICSSDKSCAKGIVDVHSNGVQTGKCV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">HYNITHKTCEIKAWCPVQGEERPPVPAVLRSSEDFTVFIKNNIHFPTFQYTVQNISPKLNTSCKFNKVTAPLCPIFRLGDILQEAKENFSEMAVKGGIIAIEIKWDCDLDSWSYYCSPEY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       </span>
<span class="topo-line"><span class="topo-inside">SFRRLDDKTRTQYPGFSIRFARHYKLPDGTEQRTLFKAYGIRFDVLVFGMGGQ</span><span class="topo-membrane">FKLIELFTFIGSTIAYFGLAVTII</span><span class="topo-outside">EMCFHLYN</span><span class="topo-unknown">LE</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>6</td>
      <td>8</td>
      <td>27</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>30</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>293</td>
      <td>50</td>
      <td>314</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>317</td>
      <td>315</td>
      <td>338</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>318</td>
      <td>325</td>
      <td>339</td>
      <td>346</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5xw6">5XW6</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSGSG</span><span class="topo-outside">SCV</span><span class="topo-membrane">KWFIYGVIAVYICYTLIVHK</span><span class="topo-inside">RYQEKEELTSSVRVTLKGVAHVDRIWDAAEYTIPTQTRDSFFVMTNIIRTENQIQKTCPEYPTAKAICSSDKSCAKGIVDVHSNGVQTGKCV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">HYNITHKTCEIKAWCPVQGEERPPVPAVLRSSEDFTVFIKNNIHFPTFQYTVQNISPKLNTSCKFNKVTAPLCPIFRLGDILQEAKENFSEMAVKGGIIAIEIKWDCDLDSWSYYCSPEY</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       </span>
<span class="topo-line"><span class="topo-inside">SFRRLDDKTRTQYPGFSIRFARHYKLPDGTEQRTLFKAYGIRFDVLVFGMGG</span><span class="topo-membrane">QFKLIELFTFIGSTIAYFGLAVTII</span><span class="topo-outside">EMCFHLYN</span><span class="topo-unknown">LE</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>6</td>
      <td>8</td>
      <td>27</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>28</td>
      <td>30</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>292</td>
      <td>50</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>317</td>
      <td>314</td>
      <td>338</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>318</td>
      <td>325</td>
      <td>339</td>
      <td>346</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### TNP-ATP wedge mechanism of competitive inhibition

The TNP-[ATP](/xray-mp-wiki/reagents/ligands/atp/)-bound ckP2X7 structure reveals an incompletely activated conformation where the trinitrophenyl group of TNP-[ATP](/xray-mp-wiki/reagents/ligands/atp/) inserts between the head and dorsal fin domains, acting as a wedge that prevents the complete cleft closure motion required for channel activation. Molecular dynamics simulations showed that removal of the trinitrophenyl group allowed the head domain to undergo the downward movement characteristic of [ATP](/xray-mp-wiki/reagents/ligands/atp/)-dependent activation. This wedge mechanism explains how TNP-[ATP](/xray-mp-wiki/reagents/ligands/atp/) acts as a competitive antagonist — it occupies the [ATP](/xray-mp-wiki/reagents/ligands/atp/) binding pocket and sterically blocks the conformational changes needed for channel opening, with the phosphate groups adopting a fully extended conformation that forms unique interactions with Lys236 and Lys298.

### Structural mapping of disease-associated P2X7 SNPs

Mapping of human P2X7 receptor SNPs onto the ckP2X7 structure revealed that loss-of-function substitutions are located exclusively in the extracellular domain and cluster within secondary structure regions, suggesting they affect the structural integrity of the inactivated state. Gain-of-function substitutions are observed in both extracellular and transmembrane domains. Notably, substitution Leu196Pro (human; corresponding to ckPhe179) associated with affective mood disorder maps to the TNP-[ATP](/xray-mp-wiki/reagents/ligands/atp/) binding pocket without forming direct hydrogen bonds, while Ala348Thr (toxoplasmosis) and Thr357Ser (bipolar disorder) map near the pore constriction site in the transmembrane domain.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/tnp-atp/">TNP-ATP</a> — Competitive antagonist co-crystallized with ckP2X7; key to understanding inhibition mechanism
- <a href="/xray-mp-wiki/proteins/other-ion-channels/zfp2x4/">Zebrafish P2X4 Receptor (zfP2X4)</a> — Related P2X family receptor structure used for comparison
- <a href="/xray-mp-wiki/proteins/other-ion-channels/human-p2x3-receptor/">Human P2X3 Receptor (hP2X3)</a> — TNP-ATP-bound hP2X3 structure compared with ckP2X7; different binding modes
- <a href="/xray-mp-wiki/concepts/signaling-receptors/p2x-receptor-family/">P2X Receptor Family</a> — ckP2X7 belongs to the P2X receptor family of ATP-gated ion channels
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">Dodecylmaltoside (DDM)</a> — Primary detergent for solubilization and purification
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — 20 mM HEPES pH 7.0 used in SEC and crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a> — 50 mM Tris pH 8.0 used in solubilization and affinity purification buffers
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Phasing method for structure determination using amP2X model
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/other-ion-channels/zfp2x4/">Zebrafish P2X4 Receptor (zfP2X4)</a> — Related protein structure
