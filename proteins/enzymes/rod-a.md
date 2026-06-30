---
title: "Thermus thermophilus RodA"
created: 2026-06-03
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature25985, doi/10.1038##s41564-020-0687-z]
verified: false
---

# Thermus thermophilus RodA

## Overview

RodA is a 359-residue transmembrane peptidoglycan polymerase from the Shape, Elongation, Division, and Sporulation (SEDS) protein family. It is an essential bacterial enzyme that catalyzes the glycosyl transfer reaction in peptidoglycan cell wall synthesis. RodA was the first SEDS protein to be structurally characterized, revealing a unique ten-pass transmembrane fold with a large extracellular cavity and a lipid binding groove. The protein forms a complex with class B penicillin binding proteins (bPBPs) to coordinate glycan strand elongation and peptide crosslinking during cell wall biogenesis. The crystal structure of the RodA-PBP2 complex at 3.3 A resolution reveals a 1:1 stoichiometric complex with two extensive interaction interfaces and a large membrane-accessible cavity formed by a 10 A shift of TM7 when bound to PBP2. RodA and other SEDS proteins represent promising targets for next-generation antibiotics.


## Publications

### doi/10.1038##nature25985

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6bar">6BAR</a></td>
      <td>2.9</td>
      <td>C2</td>
      <td>Thermus thermophilus RodA, 359 residues, N-terminal SUMO-FLAG-3C protease cleavage site tag</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (tentatively modeled)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6bas">6BAS</a></td>
      <td>3.2</td>
      <td>C2</td>
      <td>Thermus thermophilus RodA D255A catalytically inactive mutant, 359 residues, N-terminal SUMO-FLAG-3C protease cleavage site tag</td>
      <td>None resolved</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C43 (DE3) derivative harboring arabinose-inducible Ulp1 protease plasmid (pAM174)
- **Construct**: Thermus thermophilus rodA (Uniprot Q5SIX3) cloned into pAM172 plasmid with N-terminal SUMO-FLAG-3C protease cleavage site tag (SUMO-FLAG-3C-RodA)

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
      <td>Sonication of resuspended cells in lysis buffer containing lysozyme and benzonase nuclease</td>
      <td>--</td>
      <td>50 mM HEPES pH 7.5, 150 mM NaCl, 20 mM MgCl2, 100 ug/mL lysozyme, 2 mg/mL <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> + --</td>
      <td>Membranes collected by ultracentrifugation at 100,000xg for 1 h at 4 C</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Glass dounce tissue grinder extraction in solubilization buffer</td>
      <td>--</td>
      <td>20 mM HEPES pH 7.5, 500 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 2 mg/mL <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> + 1% n-Dodecyl beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Samples stirred for 2 h at 4 C, centrifuged at 100,000xg for 1 h</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>Anti-FLAG antibody <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Anti-Flag antibody affinity resin (4 mL)</td>
      <td>20 mM HEPES pH 7.0, 500 mM NaCl, 2 mM CaCl2, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Washed extensively, then in buffer supplemented with 10 mM ATP magnesium salt and 20 mM KCl to remove bacterial chaperones GroEL and DnaK</td>
    </tr>
    <tr>
      <td>Elution and tag removal</td>
      <td>Elution with Flag peptide, followed by 3C protease cleavage</td>
      <td>--</td>
      <td>20 mM HEPES pH 7.0, 500 mM NaCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 0.2 mg/mL Flag peptide + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>3C protease added at 1:1000 w:w ratio, incubated at 4 C overnight</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization using coupled syringe reconstitution</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified T. thermophilus RodA reconstituted in 10:1 <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>:<a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> (w:w) at 1.0:1.5 protein:lipid ratio by mass</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature (not specified)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-4 weeks for diffraction-quality crystals</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals harvested with mesh loops and stored in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Initial crystallization hits grew within 24 h. Crystals diffracted to 2.9 A (wild-type) and 3.2 A (D255A mutant). Both crystallized in C2 space group with one molecule in the asymmetric unit and approximately 60% solvent content. Data collected at Advanced Photon Source GM/CA beamline 23ID-B at wavelength 1.033 A.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bar">6BAR</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPAR</span><span class="topo-inside">PNWLAYD</span><span class="topo-membrane">WGLVFLVAAIVAL</span><span class="topo-outside">GFVNLGSAAPDPVLLYRQSVA</span><span class="topo-membrane">LGLGLLLAFLLQFL</span><span class="topo-inside">SRRRLFG</span><span class="topo-membrane">LAYPLYGASLLLLAL</span><span class="topo-outside">VLVVGREINGARAWFVLGPLQ</span><span class="topo-membrane">FQPLELAKLGLLL</span><span class="topo-inside">ALAK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ALEGRPIARVWDYALP</span><span class="topo-membrane">ALLTLPVVGLLLL</span><span class="topo-outside">QP</span><span class="topo-membrane">DLGGALVVLFGVFV</span><span class="topo-inside">VVFVRGLPW</span><span class="topo-membrane">RHLLVGLFALALL</span><span class="topo-outside">V</span><span class="topo-unknown">PTAVWPNLKPYQRERVLIVLDPYRDPLGQGFQVIQSTIA</span><span class="topo-outside">IGSGGLFGK</span><span class="topo-unknown">GYGQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350         </span>
<span class="topo-line"><span class="topo-unknown">GTQAQLGFIPF</span><span class="topo-outside">RHTDFVFSVWAEEWGFVG</span><span class="topo-membrane">VVGLLGLYGLLLARL</span><span class="topo-inside">FALALACPRLSDRLFL</span><span class="topo-membrane">SGFAGMLGFQVVVNLG</span><span class="topo-outside">VALG</span><span class="topo-unknown">V</span><span class="topo-outside">MPVTGLTLPLFSYGG</span><span class="topo-membrane">SSLIATLAGLGLVLL</span><span class="topo-inside">VHRDRYQD</span></span>
<details class="topo-details"><summary>Topology coordinates (28 regions)</summary>
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
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>12</td>
      <td>6</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>25</td>
      <td>13</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>46</td>
      <td>26</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>60</td>
      <td>47</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>67</td>
      <td>61</td>
      <td>67</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>82</td>
      <td>68</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>103</td>
      <td>83</td>
      <td>103</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>116</td>
      <td>104</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>136</td>
      <td>117</td>
      <td>136</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>149</td>
      <td>137</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>151</td>
      <td>150</td>
      <td>151</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>165</td>
      <td>152</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>174</td>
      <td>166</td>
      <td>174</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>187</td>
      <td>175</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>188</td>
      <td>188</td>
      <td>188</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>227</td>
      <td>189</td>
      <td>227</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>228</td>
      <td>236</td>
      <td>228</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>237</td>
      <td>251</td>
      <td>237</td>
      <td>251</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>252</td>
      <td>269</td>
      <td>252</td>
      <td>269</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>270</td>
      <td>284</td>
      <td>270</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>285</td>
      <td>300</td>
      <td>285</td>
      <td>300</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>301</td>
      <td>316</td>
      <td>301</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>320</td>
      <td>317</td>
      <td>320</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>321</td>
      <td>321</td>
      <td>321</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>322</td>
      <td>336</td>
      <td>322</td>
      <td>336</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>337</td>
      <td>351</td>
      <td>337</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>352</td>
      <td>359</td>
      <td>352</td>
      <td>359</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bas">6BAS</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MAPARPN</span><span class="topo-inside">WLAY</span><span class="topo-membrane">DWGLVFLVAAIVALGF</span><span class="topo-outside">VNLGSAAPDPVLLYRQ</span><span class="topo-membrane">SVALGLGLLLAFLLQFL</span><span class="topo-inside">S</span><span class="topo-unknown">RRRLFG</span><span class="topo-inside">L</span><span class="topo-membrane">AYPLYGASLLLLALVLVVG</span><span class="topo-outside">REINGARAWFVLGPL</span><span class="topo-membrane">QFQPLELAKLGLLLAL</span><span class="topo-inside">AK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ALEGRPIARVWDYALP</span><span class="topo-membrane">ALLTLPVVGLLLLQP</span><span class="topo-outside">D</span><span class="topo-membrane">LGGALVVLFGVFVVVF</span><span class="topo-inside">VRGLPW</span><span class="topo-membrane">RHLLVGLFALALLV</span><span class="topo-unknown">PTAVWPNLKPYQRERVLIVLDPYRDPLGQGFQVIQSTIA</span><span class="topo-outside">IGSGGLFGK</span><span class="topo-unknown">GYGQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350         </span>
<span class="topo-line"><span class="topo-unknown">GTQAQLGFIPF</span><span class="topo-outside">RHT</span><span class="topo-unknown">AFVFSVWAEE</span><span class="topo-outside">WGF</span><span class="topo-membrane">VGVVGLLGLYGLLLARLFAL</span><span class="topo-inside">ALACPRLSDRLF</span><span class="topo-membrane">LSGFAGMLGFQVVVNLGV</span><span class="topo-outside">ALGVMPVTGLTLPLFSYG</span><span class="topo-membrane">GSSLIATLAGLGLVLL</span><span class="topo-inside">VHRDRYQD</span></span>
<details class="topo-details"><summary>Topology coordinates (26 regions)</summary>
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
      <td>8</td>
      <td>11</td>
      <td>8</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>27</td>
      <td>12</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>43</td>
      <td>28</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>60</td>
      <td>44</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>61</td>
      <td>61</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>67</td>
      <td>62</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>68</td>
      <td>68</td>
      <td>68</td>
      <td>68</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>87</td>
      <td>69</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>102</td>
      <td>88</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>118</td>
      <td>103</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>136</td>
      <td>119</td>
      <td>136</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>151</td>
      <td>137</td>
      <td>151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>152</td>
      <td>152</td>
      <td>152</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>168</td>
      <td>153</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>174</td>
      <td>169</td>
      <td>174</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>188</td>
      <td>175</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>236</td>
      <td>228</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>254</td>
      <td>252</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>264</td>
      <td>255</td>
      <td>264</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>265</td>
      <td>267</td>
      <td>265</td>
      <td>267</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>268</td>
      <td>287</td>
      <td>268</td>
      <td>287</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>288</td>
      <td>299</td>
      <td>288</td>
      <td>299</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>317</td>
      <td>300</td>
      <td>317</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>318</td>
      <td>335</td>
      <td>318</td>
      <td>335</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>336</td>
      <td>351</td>
      <td>336</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>352</td>
      <td>359</td>
      <td>352</td>
      <td>359</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s41564-020-0687-z

**Expression:**

- **Expression system**: Escherichia coli C43 (DE3) derivative harboring arabinose-inducible Ulp1 protease plasmid (pAM174)
- **Construct**: Thermus thermophilus rodA (Uniprot Q5SIX3) cloned into pAM172 plasmid with N-terminal SUMO-FLAG-3C protease cleavage site tag (SUMO-FLAG-3C-RodA)

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
      <td>20 mM Tris pH 7.5, 400 mM NaCl, 1 mM PMSF, benzonase nuclease + --</td>
      <td>Cell lysate pelleted by centrifugation at 50,000g for 45 min at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA affinity</td>
      <td>Ni Sepharose Excel resin (GE Healthcare)</td>
      <td>20 mM Tris pH 7.5, 400 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (load), 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (wash) + --</td>
      <td>Eluted in 20 mM Tris pH 7.5, 400 mM NaCl, 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Dialysis</td>
      <td>Dialysis</td>
      <td>--</td>
      <td>20 mM Tris pH 7.5, 400 mM NaCl + --</td>
      <td>Dialyzed overnight at 4 C; protein flash-frozen in liquid nitrogen</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified T. thermophilus WT RodA-PBP2 or RodA D255A-PBP2 complex at 35 mg/ml</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (Hampton Research)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified (presumed room temperature)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1-4 weeks for diffraction-quality crystals</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals collected using mesh loops and stored in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>D255A mutant complex incubated with 5 mM <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a> before reconstitution. D255A reservoir: 35-45% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 300, 100 mM sodium sulfate, 100 mM MES pH 5.8-6.8, 10 mM strontium chloride. Complete dataset from 2 (WT) and 5 (D255A) crystals. Data collected at APS GM/CA 23ID-B and 23ID-D at 1.033 A wavelength.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Unique ten-pass transmembrane fold with large extracellular loops

RodA possesses a novel ten-pass transmembrane fold with largely straight helices perpendicular to the membrane plane, except TM3 which runs diagonally with a 45 degree kink at Pro71. Extracellular loops 2, 4, and 5 are large and contain many functionally essential residues, consistent with catalytic activity at the extracytoplasmic face. ECL2 includes a highly conserved beta-hairpin capped by Gly100 and Pro101. ECL4 is the largest at 80 residues but is partially disordered (residues 189-227 and 237-251 unresolved). ECL5 is buried within the protein core, unlike other ECLs.

### Central water-filled cavity with essential salt bridge for catalysis

A large water-filled cavity open to the extracellular face is flanked by Glu108, Met306, Leu307, Gln310, and Thr342. Glu108 and Lys111 form an absolutely conserved salt bridge on the cavity edge. Mutagenesis of these residues (E108A, K111A, E108K/K111E double swap) results in dominant-negative phenotypes and abolishes peptidoglycan polymerization activity in vitro. Additional essential cavity residues include Asp255 and Asp152. The cavity is catalytically essential, not merely structural, making it a prime target for antibiotic discovery.

### Hydrophobic groove as lipid-anchored substrate binding site

Between TM2 and TM3 is a long hydrophobic groove containing electron density suggestive of a bound lipid molecule, tentatively modeled as [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) from the crystallization conditions. This groove is adjacent to a collection of highly conserved residues and may represent the binding site for lipid-anchored substrates of RodA, such as lipid II.

### RodA-PBP2 complex structure reveals 1:1 stoichiometry and allosteric activation

The crystal structure of the T. thermophilus RodA-PBP2 complex at 3.3 A resolution reveals a 1:1 stoichiometric complex with two extensive interaction interfaces: one in the membrane plane (TM8-TM9 of RodA interacting with PBP2 transmembrane helix) and one at the extracytoplasmic surface (PBP2 pedestal domain contacting RodA ECL4). When bound to PBP2, RodA shows an approximately 10 A shift of TM7 that exposes a large membrane-accessible cavity (~15 x 30 A) sufficient to accommodate a lipid II molecule. The bPBP pedestal domain acts as the key allosteric activator of RodA both in vitro and in vivo, explaining how the SEDS-bPBP complex coordinates polymerization and crosslinking. Disrupting the pedestal-ECL4 interface by mutating hydrophobic residues (L43R, A186R) in PBP2 abolishes RodA glycosyltransferase activity. Negative-stain EM reveals the complex can adopt compact and extended conformations, with the extended form potentially reaching ~100 A above the membrane plane.

### SEDS proteins as essential cell wall polymerases

SEDS proteins (Shape, Elongation, Division, and Sporulation) are a ubiquitous and essential family of transmembrane enzymes with critical roles in bacterial cell wall biology. RodA was the first SEDS protein demonstrated to be a peptidoglycan polymerase, a role previously attributed exclusively to penicillin binding proteins. SEDS proteins are even more widely distributed than class A penicillin binding proteins and represent promising targets for next-generation antibiotic development.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/sed-s-protein-family/">SEDS Protein Family</a> — RodA is the prototypical member of the SEDS protein family of peptidoglycan polymerases
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Structure solved using molecular replacement with RodA as search template
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — RodA and RodA-PBP2 complex crystallized in LCP with monoolein
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl beta-D-maltoside (DDM)</a> — Primary detergent used for membrane solubilization during protein purification
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Host lipid for LCP crystallization; tentatively modeled as bound lipid in structure
- <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> — Added to monoolein for LCP reconstitution at 10:1 lipid ratio
- <a href="/xray-mp-wiki/methods/quality-assessment/circular-dichroism-spectroscopy/">Circular Dichroism Spectroscopy</a> — Used to verify proper folding of RodA mutants
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
