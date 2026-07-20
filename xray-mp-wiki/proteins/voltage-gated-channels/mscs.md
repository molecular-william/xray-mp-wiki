---
title: "E. coli MscS (Mechanosensitive Channel of Small Conductance)"
created: 2026-06-02
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3120]
verified: agent
uniprot_id: P0C0S1
---

# E. coli MscS (Mechanosensitive Channel of Small Conductance)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0C0S1">UniProt: P0C0S1</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

MscS (mechanosensitive channel of small conductance) is a mechanosensitive ion channel from Escherichia coli that gates in response to increased tension in the cytoplasmic membrane. It forms a heptameric assembly that opens in response to osmotic downshock, releasing cytoplasmic solutes to prevent cell lysis. MscS consists of four transmembrane helices (TM1, TM2, TM3a, TM3b) per subunit, with the TM3a helices lining the central pore. The channel features hydrophobic pockets between transmembrane helices that are filled by lipid acyl chains, and the extent of lipid interdigitation in these pockets is proposed to control channel gating.


## Publications

### doi/10.1038##nsmb.3120

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5aji">5AJI</a></td>
      <td>3.0</td>
      <td>C2</td>
      <td>MscS D67R1 single-cysteine MTSSL spin-labeled mutant, heptameric assembly</td>
      <td>Phospholipid acyl chains in transmembrane pockets</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: MscS from Escherichia coli, D67R1 single-cysteine MTSSL spin-labeled mutant

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
      <td>Concentration</td>
      <td>Vivaspin concentrators (100 kDa cutoff)</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a> pH 7.5, 300 mM NaCl + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Concentrated to 9-13 mg/mL</td>
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
      <td>MscS D67R1, 9-13 mg/mL in 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a> pH 7.5, 300 mM NaCl</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.07 M sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 4.5, 0.07 M NaCl, 23% v/v <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>100 K (data collection)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew to 0.3 x 0.1 x 0.1 mm in 2 d. Data collected at ID14-4, ESRF. Resolution determined by Diederichs-Karplus method as implemented in PDB REDO.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aji">5AJI</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDLNVVDSINGAGSWL</span><span class="topo-inside">VANQALLLSYAVNIVAA</span><span class="topo-membrane">LAIIIVGLIIARMISNAVNRLMISR</span><span class="topo-outside">KIDATVA</span><span class="topo-membrane">CFLSALVRYGIIAFTLIAALG</span><span class="topo-inside">RVGV</span><span class="topo-membrane">QTASVIAVLGAAGLAVG</span><span class="topo-outside">LALQGSLSNLAA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">GVLLVMFRPFRAGEYVDLGGVAGTVLSVQIFSTTMRTADGKIIVIPNGKIIAGNIINFSREPVRRNEFIIGVAYDSDIDQVKQILTNIIQSEDRILKDREMTVRLNELGASSINFVVRVW</span></span>
<span class="topo-ruler">       250       260       270       280      </span>
<span class="topo-line"><span class="topo-outside">SNSGDLQNVYWDVLERIKREFDAAGISFPYPQMDVNFKRVK</span><span class="topo-unknown">EDKAA</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>18</td>
      <td>34</td>
      <td>18</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>59</td>
      <td>35</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>66</td>
      <td>60</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>87</td>
      <td>67</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>91</td>
      <td>88</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>108</td>
      <td>92</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>281</td>
      <td>109</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aji">5AJI</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDLNVVDSINGAGSWLVANQALL</span><span class="topo-inside">LSYAVNIVAA</span><span class="topo-membrane">LAIIIVGLIIARMISNAVNRLMISR</span><span class="topo-outside">KIDATVA</span><span class="topo-membrane">CFLSALVRYGIIAFTLIAALG</span><span class="topo-inside">RVGV</span><span class="topo-membrane">QTASVIAVLGAAGLAVG</span><span class="topo-outside">LALQGSLSNLAA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">GVLLVMFRPFRAGEYVDLGGVAGTVLSVQIFSTTMRTADGKIIVIPNGKIIAGNIINFSREPVRRNEFIIGVAYDSDIDQVKQILTNIIQSEDRILKDREMTVRLNELGASSINFVVRVW</span></span>
<span class="topo-ruler">       250       260       270       280      </span>
<span class="topo-line"><span class="topo-outside">SNSGDLQNVYWDVLERIKREFDAAGISFPYPQMDVNFKR</span><span class="topo-unknown">VKEDKAA</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>25</td>
      <td>34</td>
      <td>25</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>59</td>
      <td>35</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>66</td>
      <td>60</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>87</td>
      <td>67</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>91</td>
      <td>88</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>108</td>
      <td>92</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>279</td>
      <td>109</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aji">5AJI</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDLNVVDSINGAGSWLVANQALL</span><span class="topo-inside">LSYAVNIVAA</span><span class="topo-membrane">LAIIIVGLIIARMISNAVNRLMISR</span><span class="topo-outside">KIDATVA</span><span class="topo-membrane">CFLSALVRYGIIAFTLIAALG</span><span class="topo-inside">RVGV</span><span class="topo-membrane">QTASVIAVLGAAGLAVG</span><span class="topo-outside">LALQGSLSNLAA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">GVLLVMFRPFRAGEYVDLGGVAGTVLSVQIFSTTMRTADGKIIVIPNGKIIAGNIINFSREPVRRNEFIIGVAYDSDIDQVKQILTNIIQSEDRILKDREMTVRLNELGASSINFVVRVW</span></span>
<span class="topo-ruler">       250       260       270       280      </span>
<span class="topo-line"><span class="topo-outside">SNSGDLQNVYWDVLERIKREFDAAGISFPYPQMDVNFKR</span><span class="topo-unknown">VKEDKAA</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>25</td>
      <td>34</td>
      <td>25</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>59</td>
      <td>35</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>66</td>
      <td>60</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>87</td>
      <td>67</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>91</td>
      <td>88</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>108</td>
      <td>92</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>279</td>
      <td>109</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aji">5AJI</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDLNVVDSINGAGSW</span><span class="topo-inside">LVANQALLLSYAVNIVAA</span><span class="topo-membrane">LAIIIVGLIIARMISNAVNRLMISR</span><span class="topo-outside">KIDATVA</span><span class="topo-membrane">CFLSALVRYGIIAFTLIAALG</span><span class="topo-inside">RVGV</span><span class="topo-membrane">QTASVIAVLGAAGLAVG</span><span class="topo-outside">LALQGSLSNLAA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">GVLLVMFRPFRAGEYVDLGGVAGTVLSVQIFSTTMRTADGKIIVIPNGKIIAGNIINFSREPVRRNEFIIGVAYDSDIDQVKQILTNIIQSEDRILKDREMTVRLNELGASSINFVVRVW</span></span>
<span class="topo-ruler">       250       260       270       280      </span>
<span class="topo-line"><span class="topo-outside">SNSGDLQNVYWDVLERIKREFDAAGISFPYPQMDVNFKR</span><span class="topo-unknown">VKEDKAA</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>17</td>
      <td>34</td>
      <td>17</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>59</td>
      <td>35</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>66</td>
      <td>60</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>87</td>
      <td>67</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>91</td>
      <td>88</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>108</td>
      <td>92</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>279</td>
      <td>109</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aji">5AJI</a> — Chain E (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDLNVVDSINGAGSW</span><span class="topo-inside">LVANQALLLSYAVNIVAA</span><span class="topo-membrane">LAIIIVGLIIARMISNAVNRLMISR</span><span class="topo-outside">KIDATVA</span><span class="topo-membrane">CFLSALVRYGIIAFTLIAALG</span><span class="topo-inside">RVGV</span><span class="topo-membrane">QTASVIAVLGAAGLAVG</span><span class="topo-outside">LALQGSLSNLAA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">GVLLVMFRPFRAGEYVDLGGVAGTVLSVQIFSTTMRTADGKIIVIPNGKIIAGNIINFSREPVRRNEFIIGVAYDSDIDQVKQILTNIIQSEDRILKDREMTVRLNELGASSINFVVRVW</span></span>
<span class="topo-ruler">       250       260       270       280      </span>
<span class="topo-line"><span class="topo-outside">SNSGDLQNVYWDVLERIKREFDAAGISFPYPQMDVNFK</span><span class="topo-unknown">RVKEDKAA</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>17</td>
      <td>34</td>
      <td>17</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>59</td>
      <td>35</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>66</td>
      <td>60</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>87</td>
      <td>67</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>91</td>
      <td>88</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>108</td>
      <td>92</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>278</td>
      <td>109</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aji">5AJI</a> — Chain F (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDLNVVDSINGAGSWLVANQALL</span><span class="topo-inside">LSYAVNIVAA</span><span class="topo-membrane">LAIIIVGLIIARMISNAVNRLMISR</span><span class="topo-outside">KIDATVA</span><span class="topo-membrane">CFLSALVRYGIIAFTLIAALG</span><span class="topo-inside">RVGV</span><span class="topo-membrane">QTASVIAVLGAAGLAVG</span><span class="topo-outside">LALQGSLSNLAA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">GVLLVMFRPFRAGEYVDLGGVAGTVLSVQIFSTTMRTADGKIIVIPNGKIIAGNIINFSREPVRRNEFIIGVAYDSDIDQVKQILTNIIQSEDRILKDREMTVRLNELGASSINFVVRVW</span></span>
<span class="topo-ruler">       250       260       270       280      </span>
<span class="topo-line"><span class="topo-outside">SNSGDLQNVYWDVLERIKREFDAAGISFPYPQMDVNFKRV</span><span class="topo-unknown">KEDKAA</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>25</td>
      <td>34</td>
      <td>25</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>59</td>
      <td>35</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>66</td>
      <td>60</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>87</td>
      <td>67</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>91</td>
      <td>88</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>108</td>
      <td>92</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>280</td>
      <td>109</td>
      <td>280</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5aji">5AJI</a> — Chain G (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDLNVVDSINGAGSWLVANQALL</span><span class="topo-inside">LSYAVNIVAA</span><span class="topo-membrane">LAIIIVGLIIARMISNAVNRLMISR</span><span class="topo-outside">KIDATVA</span><span class="topo-membrane">CFLSALVRYGIIAFTLIAALG</span><span class="topo-inside">RVGV</span><span class="topo-membrane">QTASVIAVLGAAGLAVG</span><span class="topo-outside">LALQGSLSNLAA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">GVLLVMFRPFRAGEYVDLGGVAGTVLSVQIFSTTMRTADGKIIVIPNGKIIAGNIINFSREPVRRNEFIIGVAYDSDIDQVKQILTNIIQSEDRILKDREMTVRLNELGASSINFVVRVW</span></span>
<span class="topo-ruler">       250       260       270       280      </span>
<span class="topo-line"><span class="topo-outside">SNSGDLQNVYWDVLERIKREFDAAGISFPYPQMDVNFK</span><span class="topo-unknown">RVKEDKAA</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>25</td>
      <td>34</td>
      <td>25</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>59</td>
      <td>35</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>66</td>
      <td>60</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>87</td>
      <td>67</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>91</td>
      <td>88</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>108</td>
      <td>92</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>109</td>
      <td>278</td>
      <td>109</td>
      <td>278</td>
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

### Lipid-filled pockets between transmembrane helices

Several phospholipid acyl chains were experimentally located in pockets formed between TM1, TM2, and TM3b helices in the heptameric MscS structure. Two alkyl chains penetrate into the pocket while a third packs against TM3b. Native mass spectrometry of purified MscS resolved lipid adducts of 620-790 Da, consistent with E. coli [Phosphatidylethanolamine](/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/) (PE) and [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) (PG) species. PE was the predominant phospholipid, with PG 30:1, PE 14:0/14:0, and PE 16:1/14:0 enriched relative to natural abundance in E. coli.

### Lipid exchange between pockets and bilayer

Molecular dynamics simulations (1 microsecond coarse-grained and 100 nanosecond atomistic) showed that lipids migrate to fill TM pockets in both closed and open states, with more lipids in the lower than upper half of the pocket. Fluorescence quenching with single-tryptophan mutants (A119W, A103W, V107W) demonstrated that phospholipid acyl chains exchange between the bilayer and TM pockets. Brominated lipids (BrPC) were used to confirm that pockets are accessible from the cytosolic leaflet. Lipids in pockets are mobile and in continuous contact with the bulk membrane bilayer.

### Mechanosensitive gating via lipid interdigitation

As MscS opens, the volume of the interhelical pockets decreases by approximately 1200 cubic angstroms per pocket, and the lipid content decreases by approximately one lipid per pocket. The loss occurs between TM2 and TM3a. Phospholipids with one acyl chain per head group (lysolipids, e.g. [LPC](/xray-mp-wiki/reagents/lipids/lysophosphatidylcholine/) 18:1) displace normal phospholipids (with two acyl chains) from MscS pockets and trigger channel opening, creating a subconducting state. The model proposes that the extent of acyl-chain interdigitation in these pockets determines the conformation of MscS, and that this lipid partitioning between pockets and bilayer is the missing component of tension-sensing models.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent for MscS purification and crystallization
- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/">Phosphatidylethanolamine (PE)</a> — Predominant phospholipid bound in MscS transmembrane pockets
- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/">Phosphatidylglycerol (PG)</a> — Major E. coli phospholipid co-purifying with MscS
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">Polyethylene Glycol 400 (PEG 400)</a> — Crystallization precipitant
- <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate Buffer</a> — 50 mM sodium phosphate pH 7.5 in purification buffer
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/mechanosensitive-gating/">Mechanosensitive Gating in Ion Channels</a> — MscS is a canonical mechanosensitive channel
- <a href="/xray-mp-wiki/reagents/lipids/lysophosphatidylcholine/">Lysophosphatidylcholine (LPC)</a> — Lysolipids displace normal phospholipids from MscS pockets and trigger channel opening
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Buffer component in purification or crystallization
