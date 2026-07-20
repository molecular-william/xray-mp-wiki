---
title: "Sodium-dependent Phosphate Transporter TmPiT from Thermotoga maritima"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.abb4024]
verified: agent
uniprot_id: Q9WY99
---

# Sodium-dependent Phosphate Transporter TmPiT from Thermotoga maritima

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9WY99">UniProt: Q9WY99</a>

<span class="expr-badge">Thermotoga maritima MSB8</span>

## Overview

TmPiT (locus Tm0261) is a sodium-dependent phosphate transporter from the hyperthermophilic bacterium Thermotoga maritima, belonging to the inorganic phosphate transporter (PiT/SLC20) family. The structure of the TmPiT-Na/Pi complex was determined at 2.3 A resolution, revealing a dimeric architecture with each protomer containing 12 transmembrane helices organized into a transport domain (5+5 inverted repeat fold with two PD001131 repeats) and a scaffold domain. The structure captured one phosphate and three sodium ions (Pi-2Na bound at the core and Na_fore near the inner membrane boundary) in an inward occluded conformation. TmPiT exhibits high-affinity phosphate binding (Kd = 57.0 uM) and strictly sodium-dependent transport, with an elevator-like mechanism proposed for substrate translocation. The structure provides a framework for understanding disease-associated mutations in human PiT homologues (hPiT1/hPiT2/SLC20A1/SLC20A2), which are linked to primary familial brain calcification and neuropsychiatric disorders.


## Publications

### doi/10.1126##sciadv.abb4024

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6l85">6L85</a></td>
      <td>2.3</td>
      <td></td>
      <td>Full-length TmPiT (locus Tm0261, residues 1-420?) from T. maritima MSB8</td>
      <td>One phosphate ion, three sodium ions</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli (inferred)
- **Construct**: Full-length TmPiT amplified from T. maritima MSB8 genomic DNA
- **Notes**: Protein expressed and purified for crystallization and functional studies

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
      <td>Microsome preparation</td>
      <td>Cell lysis and membrane fractionation</td>
      <td>--</td>
      <td>Not specified + --</td>
      <td>Microsomes prepared from expression culture</td>
    </tr>
    <tr>
      <td>Solubilization and purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Nickel affinity resin</td>
      <td>25 mM MES (pH 6.5), 3% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 120 mM NaCl + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Purified in the presence of <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> detergent; final buffer for crystallization contained 10 mM KH2PO4</td>
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
      <td>Purified TmPiT in 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 10 mM KH2PO4, 25 mM MES (pH 6.5), 120 mM NaCl, 3% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>50 mM sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> (pH 5.5), 10% <a href="/xray-mp-wiki/reagents/additives/peg3000/">PEG 3000</a> (approximate)</td>
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
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected at 2.3 A resolution. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> or SAD. TmPiT forms a dimer in the asymmetric unit with subunits A and B showing different conformations at the inner gate (inward occluded for subunit A, inward open-like for subunit B).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6l85">6L85</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MTILII</span><span class="topo-membrane">AGILGFIMAFSIGANDVANS</span><span class="topo-inside">MATAVGARAITVRQAA</span><span class="topo-membrane">LIAMFLEFLGAVMFGSHVS</span><span class="topo-outside">QTIVKGIVEVEKVQPVELMYGALS</span><span class="topo-membrane">ALIAASFWILIATNW</span><span class="topo-inside">GY</span><span class="topo-membrane">PVSTTHSIVGG</span><span class="topo-outside">MMGFGLV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">AVGINGVNWKTFLF</span><span class="topo-membrane">IVLSWVVSPVLGGLISFVM</span><span class="topo-inside">FKLISLSVFHTKNPKKSSTVAIPF</span><span class="topo-membrane">FISLAIFTMISLFVK</span><span class="topo-outside">KTLKQPLS</span><span class="topo-membrane">ESFLLGIAFSLVTFFV</span><span class="topo-inside">VHFAVRKLINEKKDVYDAVENVFK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">RAQIL</span><span class="topo-membrane">TSCYVSFSHGANDVANAA</span><span class="topo-outside">GPVAAVMIVASTGVVPKTVEIPFL</span><span class="topo-membrane">ALLLGGIGISLGVFFLG</span><span class="topo-inside">QKVMETVGEKITTLTNSRGFTV</span><span class="topo-membrane">DFSTATTVLLASSLG</span><span class="topo-outside">L</span><span class="topo-membrane">PISTTHVVVGA</span><span class="topo-inside">VTGVGFA</span></span>
<span class="topo-ruler">       370       380       390       400  </span>
<span class="topo-line"><span class="topo-inside">RGLEMVNVGVLK</span><span class="topo-membrane">NIVISWLLIVPTVAATS</span><span class="topo-outside">AAVYWVLKLIL</span><span class="topo-unknown">KF</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>26</td>
      <td>7</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>42</td>
      <td>27</td>
      <td>42</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>61</td>
      <td>43</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>85</td>
      <td>62</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>100</td>
      <td>86</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>102</td>
      <td>101</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>113</td>
      <td>103</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>134</td>
      <td>114</td>
      <td>134</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>135</td>
      <td>153</td>
      <td>135</td>
      <td>153</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>177</td>
      <td>154</td>
      <td>177</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>192</td>
      <td>178</td>
      <td>192</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>200</td>
      <td>193</td>
      <td>200</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>216</td>
      <td>201</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>217</td>
      <td>245</td>
      <td>217</td>
      <td>245</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>263</td>
      <td>246</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>287</td>
      <td>264</td>
      <td>287</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>304</td>
      <td>288</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>305</td>
      <td>326</td>
      <td>305</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>341</td>
      <td>327</td>
      <td>341</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>342</td>
      <td>342</td>
      <td>342</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>353</td>
      <td>343</td>
      <td>353</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>354</td>
      <td>372</td>
      <td>354</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>373</td>
      <td>389</td>
      <td>373</td>
      <td>389</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>390</td>
      <td>400</td>
      <td>390</td>
      <td>400</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6l85">6L85</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MT</span><span class="topo-membrane">ILIIAGILGFIMAFSIGANDVANS</span><span class="topo-inside">MATAVGARAITVRQAALI</span><span class="topo-membrane">AMFLEFLGAVMFGS</span><span class="topo-unknown">HVSQTIVK</span><span class="topo-outside">GIVEVEKVQPVELMYGA</span><span class="topo-membrane">LSALIAASFWILIAT</span><span class="topo-inside">NWGY</span><span class="topo-membrane">PVSTTHSIVGGMMG</span><span class="topo-outside">FGLV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">AVGINGVNWKTFLFI</span><span class="topo-membrane">VLSWVVSPVLGGLISFVMFKLI</span><span class="topo-inside">SLSVFHTKNPKKSSTV</span><span class="topo-membrane">AIPFFISLAIFTMISLFV</span><span class="topo-outside">KKTLKQPLSES</span><span class="topo-membrane">FLLGIAFSLVTFFVVH</span><span class="topo-inside">FAVRKLINEKKDVYDAVENVFK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">RAQIL</span><span class="topo-membrane">TSCYVSFSHGANDVANAAGPV</span><span class="topo-outside">AAVMIVASTGVVPKTVEIPF</span><span class="topo-membrane">LALLLGGIGISLGV</span><span class="topo-inside">FFL</span><span class="topo-unknown">GQKVMETVGEKI</span><span class="topo-inside">TTLTNSRGF</span><span class="topo-membrane">TVDFSTATTVLLASS</span><span class="topo-outside">LGL</span><span class="topo-membrane">PISTTHVVVGAVTGV</span><span class="topo-inside">GFA</span></span>
<span class="topo-ruler">       370       380       390       400  </span>
<span class="topo-line"><span class="topo-inside">RGLEMVNVGVLK</span><span class="topo-membrane">NIVISWLLIVPTVAATSAAVYWVL</span><span class="topo-outside">KLILK</span><span class="topo-unknown">F</span></span>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>26</td>
      <td>3</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>44</td>
      <td>27</td>
      <td>44</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>58</td>
      <td>45</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>66</td>
      <td>59</td>
      <td>66</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>67</td>
      <td>83</td>
      <td>67</td>
      <td>83</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>98</td>
      <td>84</td>
      <td>98</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>102</td>
      <td>99</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>116</td>
      <td>103</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>135</td>
      <td>117</td>
      <td>135</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>157</td>
      <td>136</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>158</td>
      <td>173</td>
      <td>158</td>
      <td>173</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>191</td>
      <td>174</td>
      <td>191</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>202</td>
      <td>192</td>
      <td>202</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>218</td>
      <td>203</td>
      <td>218</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>245</td>
      <td>219</td>
      <td>245</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>266</td>
      <td>246</td>
      <td>266</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>286</td>
      <td>267</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>300</td>
      <td>287</td>
      <td>300</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>301</td>
      <td>303</td>
      <td>301</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>315</td>
      <td>304</td>
      <td>315</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>316</td>
      <td>324</td>
      <td>316</td>
      <td>324</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>325</td>
      <td>339</td>
      <td>325</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>342</td>
      <td>340</td>
      <td>342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>343</td>
      <td>357</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>372</td>
      <td>358</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>373</td>
      <td>396</td>
      <td>373</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>401</td>
      <td>397</td>
      <td>401</td>
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

### Sodium-dependent phosphate binding and coordination

The TmPiT-Na/Pi complex reveals one phosphate and three sodium ions bound at distinct sites. The Pi-2Na site at the core of the transporter comprises phosphate associated with two sodium ions (Na1-Pi-Na2) through conserved aspartates D22 and D258. The phosphate is coordinated via 12 interactions with eight conserved residues: D22/TM1, D258/TM6, and six polar residues from the reentrant helical hairpins — S105/T106/T107 (HP1b) and S345/T346/T347 (HP2b). Na1 is pentacoordinated by N21, D22, V104, T347, and K314; Na2 by N257, D258, T107, I344, and a water molecule. A third sodium (Na_fore) is located near the inner membrane boundary, coordinated by T29, Q243, S247, and D327. Mutation of D22A or D258A maintains Pi binding but abolishes uptake, while D22/258A double mutant fails to bind Pi.

### Elevator-like transport mechanism

TmPiT is proposed to use a two-gated elevator-like mechanism for phosphate and sodium transport, analogous to the [GLTPH](/xray-mp-wiki/proteins/slc-transporters/glt-ph/) glutamate transporter and [VCINDY](/xray-mp-wiki/proteins/slc-transporters/vcindy/) dicarboxylate transporter. The transport cycle involves at least four sequential states: outward open, outward occluded, inward occluded, and inward open. The structure captures the inward occluded state. The two inverted PD001131 repeats (N-PD001131: TM1-TM2-HP1-TM3; C-PD001131: TM6-TM7-HP2-TM8) form reentrant helical hairpins HP1 and HP2 that control the inner and outer gates. Subunits A and B of the dimer reveal different inner gate conformations (closed vs. open), suggesting asymmetric functional states and possible cooperative behavior.

### Structural basis for human PiT disease mutations

The TmPiT structure informs disease-associated mutations in human PiT (hPiT1/SLC20A1 and hPiT2/SLC20A2), which cause primary familial brain calcification (PFBC) and neuropsychiatric disorders. Key correspondences include: D22 (TmPiT) → D28N (hPiT2, PFBC-linked); D258 → D506N; D327 → E575K (PFBC-linked); W378 → W626 duplication (PFBC-linked). Mutations cluster in Pi/Na-binding residues, the N- and C-PD001131 repeats, dimer interface, and scaffold domain. The D22A/D258A double mutant fails to bind Pi, and the D327Q mutant (corresponding to hPiT2 E575K) loses Pi binding entirely, explaining the disease mechanism.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/">Elevator Mechanism</a> — TmPiT uses an elevator-like mechanism for phosphate/sodium transport
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — TmPiT operates via alternating access between outward and inward conformations
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/slc-transporters/glt-ph/">GLTPH</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/slc-transporters/vcindy/">VCINDY</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg3000/">PEG 3000</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Buffer component used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
