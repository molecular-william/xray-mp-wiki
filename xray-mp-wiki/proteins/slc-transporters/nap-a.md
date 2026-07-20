---
title: "Na+/H+ Antiporter NapA from Thermus thermophilus"
created: 2026-06-03
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12484, doi/10.1038##nsmb.3164]
verified: agent
uniprot_id: ['Q5SIA2', 'Q72IM4']
---

# Na+/H+ Antiporter NapA from Thermus thermophilus

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q5SIA2">UniProt: Q5SIA2</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q72IM4">UniProt: Q72IM4</a>

<span class="expr-badge">Thermus thermophilus</span>

## Overview

NapA from Thermus thermophilus is a Na+/H+ antiporter belonging to the CPA2 clade of the monovalent cation proton antiporter (CPA) superfamily. It catalyzes the electrogenic exchange of Na+ (or Li+) for H+ across the membrane, playing a critical role in intracellular pH homeostasis and sodium concentration regulation. The protein consists of 13 transmembrane helices organized into a core domain (helices 1-6) and a dimerization domain (helices -1 and 7-12), forming a homodimer in the membrane. NapA was initially crystallized in an outward-facing conformation at 3.0 A resolution, revealing a negatively charged extracellular cavity with the strictly conserved aspartate residue (Asp 157) positioned for ion binding. Later structures trapped NapA in an inward-facing conformation via disulfide crosslinking (PDB 5BZ2, 3.7 A) and refined the outward-facing conformation in lipidic cubic phase (PDB 5BZ3, 2.3 A), confirming an elevator-like alternating-access mechanism for ion translocation with the core domain moving ~8 A relative to the fixed dimer domain.


## Publications

### doi/10.1038##nature12484

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4bwz">4BWZ</a></td>
      <td>\'3.0\'</td>
      <td>C222_1</td>
      <td>Full-length NapA from Thermus thermophilus (Uniprot Q72IM4), GFP-His8 fusion with TEV cleavage site</td>
      <td>zinc (2 ions per monomer)</td>
    </tr>
  </tbody>
</table>
 - R-work not specified%, R-free not specified%; Data collection: X-ray diffraction at 3.0 A resolution, solved by multiple isomorphous replacement with anomalous scattering (MIRAS) with Mercury (HgCl2) and Selenomethionine (SeMet) derivatization, multi-crystal averaging

**Expression:**

- **Expression system**: Escherichia coli Lemo21(DE3)
- **Construct**: Full-length NapA from Thermus thermophilus (Uniprot Q72IM4) cloned into pWaldoGFPe vector as GFP-His8 fusion; expressed with IPTG induction at 25 C overnight

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
      <td>Membrane preparation</td>
      <td>Cell lysis and membrane fractionation</td>
      <td>not specified</td>
      <td>1x PBS, 150 mM NaCl + not specified</td>
      <td>Membranes isolated from 5 L <a href="/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/">E. coli</a> cultures</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>not specified</td>
      <td>1x PBS, 150 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/buffers/imidazole/">Imidazole</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Solubilized in 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> for 2 h</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> affinity capture</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) Superflow resin</td>
      <td>1x PBS, 150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/imidazole/">Imidazole</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Washed with 20 mM and 50 mM <a href="/xray-mp-wiki/reagents/buffers/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Elution</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) affinity elution</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) Superflow resin</td>
      <td>1x PBS, 150 mM NaCl, 250 mM <a href="/xray-mp-wiki/reagents/buffers/imidazole/">Imidazole</a>, 0.6% NM + 0.6% NM</td>
      <td>Eluted in NM-containing buffer</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease cleavage</td>
      <td>not specified</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> pH 7.5, 150 mM NaCl, 0.5% NM + 0.5% NM</td>
      <td>Dialyzed overnight with <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His6-tag</a>ged <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease</td>
    </tr>
    <tr>
      <td>Second <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) His-Trap column</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> pH 7.5, 150 mM NaCl, 0.5% NM + 0.5% NM</td>
      <td>Cleaved NapA collected in flow-through</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapour diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Cleaved NapA in NM detergent</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>not specified</td>
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
      <td>Notes</td>
      <td>Crystals grown at pH 7.8 or 9.0; data collected at Diamond Light Source I02, I03 and ESRF ID 23-1, 23-2; protein derivatized with 2.5 mM <a href="/xray-mp-wiki/reagents/additives/mercury/">Mercury</a> (HgCl2) in Acetate Buffer; structure solved by MIRAS with multi-crystal averaging at 3.0 A resolution in space group C222_1; crystals contain 4 molecules in asymmetric unit; 2 zinc ions bound per monomer on periplasmic surface</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4bwz">4BWZ</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MH</span><span class="topo-outside">G</span><span class="topo-membrane">AEHLLEIFYLLLAAQVCAFIF</span><span class="topo-inside">KRLNQ</span><span class="topo-membrane">PVVIGEVLAGVLVGPAL</span><span class="topo-outside">L</span><span class="topo-membrane">GLVHEGEILEFLAELGAVFLLFMVG</span><span class="topo-inside">LETRLKDILAVG</span><span class="topo-membrane">KEAFLVAVLGVALPFLGGYLY</span><span class="topo-outside">GLEIGFETLPALFL</span><span class="topo-membrane">G</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">TALVATSVGITARV</span><span class="topo-inside">LQELGVLSRPYSRI</span><span class="topo-membrane">ILGAAVIDDVLGLIVLA</span><span class="topo-outside">CVNGVAETGQVEVGAI</span><span class="topo-membrane">TRLIVLSVVFVGLAVFL</span><span class="topo-inside">STLIARLPLERLPVGSPLG</span><span class="topo-membrane">FALALGVGMAALAASI</span><span class="topo-outside">G</span><span class="topo-membrane">LAPIVG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AFLGGML</span><span class="topo-inside">LSEVREKYRLEEPIFAI</span><span class="topo-membrane">ESFLAPIFFAMVGVRLEL</span><span class="topo-outside">SALASPVVL</span><span class="topo-membrane">VAGTVVTVIAILGKVLGGFLGA</span><span class="topo-inside">LTQGVRSA</span><span class="topo-membrane">LTVGCGMAPRGEVGLIVA</span><span class="topo-outside">ALGLKAGAVNEEEYAI</span><span class="topo-membrane">VLFMV</span></span>
<span class="topo-ruler">       370       380       390    </span>
<span class="topo-line"><span class="topo-membrane">VFTTLFAPFAL</span><span class="topo-inside">KPLIAWTERERAAKE</span><span class="topo-unknown">GSENLYFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>24</td>
      <td>4</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>29</td>
      <td>25</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>30</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>47</td>
      <td>47</td>
      <td>47</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>72</td>
      <td>48</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>84</td>
      <td>73</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>105</td>
      <td>85</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>119</td>
      <td>106</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>134</td>
      <td>120</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>148</td>
      <td>135</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>165</td>
      <td>149</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>181</td>
      <td>166</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>182</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>217</td>
      <td>199</td>
      <td>217</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>233</td>
      <td>218</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>234</td>
      <td>234</td>
      <td>234</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>247</td>
      <td>235</td>
      <td>247</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>248</td>
      <td>264</td>
      <td>248</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>282</td>
      <td>265</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>283</td>
      <td>291</td>
      <td>283</td>
      <td>291</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>313</td>
      <td>292</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>321</td>
      <td>314</td>
      <td>321</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>322</td>
      <td>339</td>
      <td>322</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>340</td>
      <td>355</td>
      <td>340</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>371</td>
      <td>356</td>
      <td>371</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>386</td>
      <td>372</td>
      <td>386</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>387</td>
      <td>394</td>
      <td>387</td>
      <td>394</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nsmb.3164

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5bz2">5BZ2</a></td>
      <td>\'3.7\'</td>
      <td>C222_1</td>
      <td>Full-length NapA V31C I130C mutant (Uniprot Q72IM4), TEV-cleaved</td>
      <td>none</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5bz3">5BZ3</a></td>
      <td>\'2.3\'</td>
      <td>C222_1</td>
      <td>Full-length NapA wild-type (Uniprot Q72IM4), TEV-cleaved</td>
      <td>LCP lipid MAG7.7 modeled at core-dimer interface</td>
    </tr>
  </tbody>
</table>
 - R-work 0.292%, R-free 0.325%; Data collection: X-ray diffraction at 3.7 A resolution; molecular replacement with dimer and core domains of PDB 4BWZ as separate search models; refined in autoBUSTER/Phenix
 - R-work 0.206%, R-free 0.218%; Data collection: X-ray diffraction at 2.3 A resolution; LCP crystallization; data collected at Diamond Light Source; refined in autoBUSTER/Phenix

**Expression:**

- **Expression system**: Escherichia coli Lemo21(DE3)
- **Construct**: Full-length NapA from Thermus thermophilus (Uniprot Q72IM4) cloned into pWaldoGFPe vector as GFP-His8 fusion; expressed with IPTG induction at 25 C overnight

**Purification:**

- **Expression system**: Escherichia coli Lemo21(DE3)
- **Expression construct**: Full-length NapA (wild-type and mutants V31C, I130C, V31C/I130C, I55C) in pWaldoGFPe vector, GFP-His8 fusion with [TEV](/xray-mp-wiki/reagents/additives/tev-protease/) cleavage site
- **Tag info**: C-terminal [GFP](/xray-mp-wiki/reagents/protein-tags/gfp/)-His8 tag, removed by [TEV protease](/xray-mp-wiki/reagents/additives/tev-protease/)

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
      <td>Cell culture</td>
      <td>MemStar overexpression</td>
      <td>not specified</td>
      <td>not specified + not specified</td>
      <td>Transformed into <a href="/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/">E. coli</a> Lemo21(DE3), overexpressed with MemStar protocol</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td><a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">Ultracentrifugation</a></td>
      <td>not specified</td>
      <td>1x PBS, 150 mM NaCl + not specified</td>
      <td>Membranes isolated from 6 L <a href="/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/">E. coli</a> cultures</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>not specified</td>
      <td>1x PBS, 150 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/buffers/imidazole/">Imidazole</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Solubilized in 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> for 1 h at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> affinity capture</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) Superflow resin</td>
      <td>1x PBS, 150 mM NaCl, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Washed with 10, 20, 45 mM <a href="/xray-mp-wiki/reagents/buffers/imidazole/">Imidazole</a> (3 x 10 CV each)</td>
    </tr>
    <tr>
      <td>Elution</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) affinity elution</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) Superflow resin</td>
      <td>1x PBS, 150 mM NaCl, 250 mM <a href="/xray-mp-wiki/reagents/buffers/imidazole/">Imidazole</a>, 0.6% NM + 0.6% NM</td>
      <td>Eluted in NM-containing buffer</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease cleavage</td>
      <td>not specified</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> pH 7.5, 150 mM NaCl, 0.5% NM + 0.5% NM</td>
      <td>Dialyzed overnight with <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His6-tag</a>ged <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a> protease and 5 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a></td>
    </tr>
    <tr>
      <td>Second <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) His-Trap column (GE Healthcare)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> pH 7.5, 150 mM NaCl, 0.5% NM + 0.5% NM</td>
      <td>Cleaved NapA collected in flow-through</td>
    </tr>
    <tr>
      <td>Oxidation and gel filtration (functional studies)</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> pH 7.5, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Pre-incubated with 1 mM CuSO4 for 30 min for reoxidation; <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Gel filtration (structural studies)</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> pH 7.5, 150 mM NaCl, 0.6% NM + 0.6% NM</td>
      <td>No CuSO4 treatment; <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) in NM</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified NapA in 20 mM [Tris-HCl](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl with either 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) or 0.6% NM

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapour diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>NapA V31C I130C mutant, <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV</a>-cleaved</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>not specified</td>
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
      <td>Notes</td>
      <td>Inward-facing disulfide-trapped structure (PDB 5BZ2); data collected at Diamond Light Source; <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> with PDB 4BWZ dimer and core domains; refined to 3.7 A resolution in space group C222_1; disulfide bond between C31 and C130</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Cleaved wild-type NapA</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>MAG7.7 (monoacyl<a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>not specified</td>
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
      <td>Notes</td>
      <td>Outward-facing <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> structure (PDB 5BZ3); data collected at Diamond Light Source; refined to 2.3 A resolution in space group C222_1; bilayer-type crystal packing; <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> lipid MAG7.7 modeled at core-dimer interface; half helices TM4a and TM11b more open than detergent structure</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5bz2">5BZ2</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MH</span><span class="topo-outside">GAEH</span><span class="topo-membrane">LLEIFYLLLAAQVMAFIFKRL</span><span class="topo-inside">N</span><span class="topo-membrane">QPCVIGEVLAGVLVG</span><span class="topo-outside">PALLGLVHEGEIL</span><span class="topo-membrane">EFLAELGAVFLLFMVGLET</span><span class="topo-inside">RLKDILAVGKEA</span><span class="topo-membrane">FLVAVLGVALPFLGGYLYG</span><span class="topo-outside">LEIGFETLPAL</span><span class="topo-membrane">FLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">TALVATSVGCT</span><span class="topo-inside">ARVLQELGVLSRPYSRII</span><span class="topo-membrane">LGAAVIDDVLGLIVLAVV</span><span class="topo-outside">NGVAETGQVEVGAI</span><span class="topo-membrane">TRLIVLSVVFVGLAVFLS</span><span class="topo-inside">TLIARLPLER</span><span class="topo-membrane">LPVGSPLGFALALGVGMAALAASI</span><span class="topo-outside">G</span><span class="topo-membrane">LAPIVG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AFLGGMLLS</span><span class="topo-inside">EVREKYRLEEP</span><span class="topo-membrane">IFAIESFLAPIFFAMVGV</span><span class="topo-outside">RLELSALASPVV</span><span class="topo-membrane">LVAGTVVTVIAILGKVLGGFLG</span><span class="topo-inside">ALTQGVRSALTVG</span><span class="topo-membrane">VGMAPRGEVGLIVAAL</span><span class="topo-outside">GLKAGAVNEEEY</span><span class="topo-membrane">AIVLFMV</span></span>
<span class="topo-ruler">       370       380      </span>
<span class="topo-line"><span class="topo-membrane">VFTTLFAPFA</span><span class="topo-inside">LKPLIAWTERERAAKE</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>3</td>
      <td>6</td>
      <td>3</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>27</td>
      <td>7</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>28</td>
      <td>28</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>43</td>
      <td>29</td>
      <td>43</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>44</td>
      <td>56</td>
      <td>44</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>75</td>
      <td>57</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>87</td>
      <td>76</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>106</td>
      <td>88</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>117</td>
      <td>107</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>131</td>
      <td>118</td>
      <td>131</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>149</td>
      <td>132</td>
      <td>149</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>150</td>
      <td>167</td>
      <td>150</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>181</td>
      <td>168</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>199</td>
      <td>182</td>
      <td>199</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>209</td>
      <td>200</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>233</td>
      <td>210</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>234</td>
      <td>234</td>
      <td>234</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>249</td>
      <td>235</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>260</td>
      <td>250</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>278</td>
      <td>261</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>290</td>
      <td>279</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>312</td>
      <td>291</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>325</td>
      <td>313</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>341</td>
      <td>326</td>
      <td>341</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>342</td>
      <td>353</td>
      <td>342</td>
      <td>353</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>370</td>
      <td>354</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>371</td>
      <td>386</td>
      <td>371</td>
      <td>386</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5bz2">5BZ2</a> — Chain B (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MH</span><span class="topo-outside">GAEH</span><span class="topo-membrane">LLEIFYLLLAAQVMAFIFKRL</span><span class="topo-inside">N</span><span class="topo-membrane">QPCVIGEVLAGVLV</span><span class="topo-outside">GPALLGLVHEGEILEF</span><span class="topo-membrane">LAELGAVFLLFMVGLET</span><span class="topo-inside">RLKDILAVG</span><span class="topo-membrane">KEAFLVAVLGVALPFLGG</span><span class="topo-outside">YLYGLEIGFETLPALFLG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">TALVATSVGCTARV</span><span class="topo-inside">LQELGVLSRPYSRI</span><span class="topo-membrane">ILGAAVIDDVLGLIVLA</span><span class="topo-outside">VVNGVAETGQVEVGAITRL</span><span class="topo-membrane">IVLSVVFVGLAVFLSTLI</span><span class="topo-inside">ARLPLER</span><span class="topo-membrane">LPVGSPLGFALALGVGMAALAASI</span><span class="topo-outside">GL</span><span class="topo-membrane">APIVG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AFLGGMLLS</span><span class="topo-inside">EVREKYRL</span><span class="topo-membrane">EEPIFAIESFLAPIFFAMVG</span><span class="topo-outside">VRLELSALASPVVLVAG</span><span class="topo-membrane">TVVTVIAILGKVLGGFLGAL</span><span class="topo-inside">TQGVRSA</span><span class="topo-membrane">LTVGVGMAPRGEVGLIVAA</span><span class="topo-outside">LGLKAGAVNEEEYAIV</span><span class="topo-membrane">LFMV</span></span>
<span class="topo-ruler">       370       380      </span>
<span class="topo-line"><span class="topo-membrane">VFTTLFAPFALK</span><span class="topo-inside">PLIAWTERERAAKE</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>3</td>
      <td>6</td>
      <td>3</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>27</td>
      <td>7</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>28</td>
      <td>28</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>42</td>
      <td>29</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>58</td>
      <td>43</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>75</td>
      <td>59</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>84</td>
      <td>76</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>102</td>
      <td>85</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>120</td>
      <td>103</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>134</td>
      <td>121</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>148</td>
      <td>135</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>165</td>
      <td>149</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>184</td>
      <td>166</td>
      <td>184</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>202</td>
      <td>185</td>
      <td>202</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>203</td>
      <td>209</td>
      <td>203</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>233</td>
      <td>210</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>235</td>
      <td>234</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>249</td>
      <td>236</td>
      <td>249</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>250</td>
      <td>257</td>
      <td>250</td>
      <td>257</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>258</td>
      <td>277</td>
      <td>258</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>294</td>
      <td>278</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>314</td>
      <td>295</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>315</td>
      <td>321</td>
      <td>315</td>
      <td>321</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>322</td>
      <td>340</td>
      <td>322</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>356</td>
      <td>341</td>
      <td>356</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>357</td>
      <td>372</td>
      <td>357</td>
      <td>372</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>373</td>
      <td>386</td>
      <td>373</td>
      <td>386</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5bz3">5BZ3</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">G</span><span class="topo-membrane">AEHLLEIFYLLLAAQVCAFIF</span><span class="topo-outside">KRLNQ</span><span class="topo-membrane">PVVIGEVLAGVLVGPAL</span><span class="topo-inside">L</span><span class="topo-membrane">GLVHEGEILEFLAELGAVFLLFMVG</span><span class="topo-outside">LETRLKDILAVG</span><span class="topo-membrane">KEAFLVAVLGVALPFLGGYLYG</span><span class="topo-inside">LEIGFETLPAL</span><span class="topo-membrane">FLGT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ALVATSVGITARV</span><span class="topo-outside">LQELGVLSRPYSRI</span><span class="topo-membrane">ILGAAVIDDVLGLIVLACV</span><span class="topo-inside">NGVAETGQVEV</span><span class="topo-membrane">GAITRLIVLSVVFVGLAVFL</span><span class="topo-outside">STLIARLPLERLPVGSPLG</span><span class="topo-membrane">FALALGVGMAALAASI</span><span class="topo-inside">G</span><span class="topo-membrane">LAPIVGA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">FLGG</span><span class="topo-outside">MLLSEVREKYRLEEPIFAI</span><span class="topo-membrane">ESFLAPIFFAMVGVRLELSAL</span><span class="topo-inside">ASPVV</span><span class="topo-membrane">LVAGTVVTVIAILGKVLGGFLGA</span><span class="topo-outside">LTQGVRSA</span><span class="topo-membrane">LTVGCGMAPRGEVGLIVA</span><span class="topo-inside">ALGLKAGAVNEEEYA</span><span class="topo-membrane">IVLFMVV</span></span>
<span class="topo-ruler">       370       380     </span>
<span class="topo-line"><span class="topo-membrane">FTTLFAPFALK</span><span class="topo-outside">PLIAWTERERAAKE</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>23</td>
      <td>4</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>28</td>
      <td>25</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>45</td>
      <td>30</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>46</td>
      <td>47</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>71</td>
      <td>48</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>83</td>
      <td>73</td>
      <td>84</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>105</td>
      <td>85</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>116</td>
      <td>107</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>118</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>147</td>
      <td>135</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>166</td>
      <td>149</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>177</td>
      <td>168</td>
      <td>178</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>197</td>
      <td>179</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>216</td>
      <td>199</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>232</td>
      <td>218</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>233</td>
      <td>234</td>
      <td>234</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>244</td>
      <td>235</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>263</td>
      <td>246</td>
      <td>264</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>264</td>
      <td>284</td>
      <td>265</td>
      <td>285</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>285</td>
      <td>289</td>
      <td>286</td>
      <td>290</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>312</td>
      <td>291</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>320</td>
      <td>314</td>
      <td>321</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>338</td>
      <td>322</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>339</td>
      <td>353</td>
      <td>340</td>
      <td>354</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>371</td>
      <td>355</td>
      <td>372</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>385</td>
      <td>373</td>
      <td>386</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5bz3">5BZ3</a> — Chain B (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">G</span><span class="topo-membrane">AEHLLEIFYLLLAAQVCAFIF</span><span class="topo-outside">KRLNQ</span><span class="topo-membrane">PVVIGEVLAGVLVGPAL</span><span class="topo-inside">L</span><span class="topo-membrane">GLVHEGEILEFLAELGAVFLLFMVG</span><span class="topo-outside">LETRLKDILAVG</span><span class="topo-membrane">KEAFLVAVLGVALPFLGGYLYG</span><span class="topo-inside">LEIGFETLPAL</span><span class="topo-membrane">FLGT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ALVATSVGITARV</span><span class="topo-outside">LQELGVLSRPYSRI</span><span class="topo-membrane">ILGAAVIDDVLGLIVLACV</span><span class="topo-inside">NGVAETGQVEV</span><span class="topo-membrane">GAITRLIVLSVVFVGLAVFL</span><span class="topo-outside">STLIARLPLERLPVGSPLG</span><span class="topo-membrane">FALALGVGMAALAASI</span><span class="topo-inside">G</span><span class="topo-membrane">LAPIVGA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">FLGG</span><span class="topo-outside">MLLSEVREKYRLEEPIFAI</span><span class="topo-membrane">ESFLAPIFFAMVGVRLELSAL</span><span class="topo-inside">ASPVV</span><span class="topo-membrane">LVAGTVVTVIAILGKVLGGFLGA</span><span class="topo-outside">LTQGVRSA</span><span class="topo-membrane">LTVGCGMAPRGEVGLIVA</span><span class="topo-inside">ALGLKAGAVNEEEYA</span><span class="topo-membrane">IVLFMVV</span></span>
<span class="topo-ruler">       370       380     </span>
<span class="topo-line"><span class="topo-membrane">FTTLFAPFALK</span><span class="topo-outside">PLIAWTERERAAKE</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>23</td>
      <td>4</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>28</td>
      <td>25</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>45</td>
      <td>30</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>46</td>
      <td>47</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>71</td>
      <td>48</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>83</td>
      <td>73</td>
      <td>84</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>105</td>
      <td>85</td>
      <td>106</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>116</td>
      <td>107</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>133</td>
      <td>118</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>147</td>
      <td>135</td>
      <td>148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>166</td>
      <td>149</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>177</td>
      <td>168</td>
      <td>178</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>197</td>
      <td>179</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>216</td>
      <td>199</td>
      <td>217</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>232</td>
      <td>218</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>233</td>
      <td>234</td>
      <td>234</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>244</td>
      <td>235</td>
      <td>245</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>263</td>
      <td>246</td>
      <td>264</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>264</td>
      <td>284</td>
      <td>265</td>
      <td>285</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>285</td>
      <td>289</td>
      <td>286</td>
      <td>290</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>312</td>
      <td>291</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>320</td>
      <td>314</td>
      <td>321</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>338</td>
      <td>322</td>
      <td>339</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>339</td>
      <td>353</td>
      <td>340</td>
      <td>354</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>354</td>
      <td>371</td>
      <td>355</td>
      <td>372</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>372</td>
      <td>385</td>
      <td>373</td>
      <td>386</td>
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

### Two-domain elevator mechanism for alternating access

The NapA structure reveals a two-domain architecture with a core domain (helices 1-6) and a dimerization domain (helices -1 and 7-12). The core and dimerization domains are in different positions compared to the inward-facing NhaA structure, with a 20-degree rotation of the core domain relative to the dimerization domain. This rotation opens a negatively charged cavity to the extracellular side, allowing access to the strictly conserved aspartate (Asp 157) that coordinates ion binding. The elevator movement carries the substrate-binding domain across the membrane, resembling the mechanism seen in the glutamate transporter GltPh and the bile acid sodium symporter ASBT_NM.

### Dimer assembly and dimerization interface

NapA purifies as a homodimer with an extensive interface burying 1,800 A^2 of surface area. The dimer has a crystallographic two-fold operator approximately parallel to the transmembrane helices, formed by tight hydrophobic helix-helix packing between TM-1 on one monomer and TM7 on the other, with additional contacts between the ends of TM2 and TM9. NapA lacks the beta-hairpin domain present in NhaA that mediates extracellular dimer contacts; instead, the dimer interface resembles that modeled in the NhaP1 electron crystallography structure.

### Ion-binding site and conserved residues

The substrate-binding cavity is open to the extracellular side and is negatively charged, lined with glutamate residues. Near the base of the cavity are two highly conserved aspartates, Asp 156 and Asp 157, located on TM5. Asp 157 is strictly conserved and ideally positioned for binding both protons and sodium ions. Lys 305 (TM10) forms a salt bridge with Asp 156 in the outward-facing state. Mutation of Glu 333 (TM11b) decreased Na+ affinity (>15-fold) and Lys 305 mutation decreased both Na+ and Li+ affinity (>20-fold), confirming their functional importance.

### Disulfide trapping of inward-facing conformation confirms elevator mechanism

An engineered disulfide bond between V31C (dimer domain) and I130C (core domain) traps NapA in an inward-facing conformation (PDB 5BZ2), abolishing ~90% of transport activity. The disulfide bond can form spontaneously in a membrane environment. ITC measurements of the trapped mutant give Kd values for Na+ (1.6 mM) and Li+ (0.25 mM) at pH 8.0, similar to apparent Km values, confirming the trapped state is functionally competent for binding. The C-alpha atom of D157 is relocated ~8 A vertically between outward and inward states, with the side chain rotating ~55 degrees.

### LCP structure reveals physiological outward-facing conformation

The 2.3 A LCP structure (PDB 5BZ3) shows bilayer-type crystal packing, unlike the detergent-grown crystal. The core domain adopts the same overall conformation, but half helices TM11b and TM4a are tilted ~6 A further from the cavity, making it more open. MD simulations show these half helices fluctuate between positions seen in both structures, indicating high mobility. The open vestibule provides an open path for Na+ ions to bind D157 from extracellular solvent.

### MD simulations confirm core domain movement against fixed dimer

Molecular dynamics simulations of outward- and inward-facing NapA in a POPE/POPG (4:1) bilayer show the dimer domain vertical position differs by only ~2 A between states, while the core domain moves ~6 A relative to the membrane and ~7 A relative to the dimer domain. Morph analysis shows the core domain undergoes a large rotation and translation, with D157 relocated ~11 A between the two states. Flexible hinge regions between TM9-10 (extracellular) and TM6-7 (intracellular) containing glycine residues (G193, G213, G277, G294) facilitate the movement.

### Alternating salt bridges and half-helix gating

Positively charged residues K344 (TM11b) and R133 (TM4b) form alternating ionic interactions with negatively charged residues in the dimer domain to stabilize alternate conformations. K344A and R133E mutations negatively affect transport; a charge-swapped double mutant (E35R/R133E) rescues activity. Acyl chains (modeled as LCP lipids) located between TM4b/TM11b half helices and the dimer domain in the outward-facing LCP structure suggest in vivo lipids may facilitate the elevator-like structural transitions.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/nhaa/">Na+/H+ Antiporter NhaA from Escherichia coli</a> — Structural homologue and comparison protein; inward-facing NhaA structure used for alternating access model
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/elevator-mechanism/">Elevator Mechanism</a> — NapA provides structural evidence for the elevator transport mechanism
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — NapA operates by alternating access between outward-facing and inward-facing states
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rocking-bundle-mechanism/">Rocking-Bundle Mechanism</a> — Contrasted with elevator mechanism as alternative transport model for Na+/H+ antiporters
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent for NapA membrane solubilization at 1%
- <a href="/xray-mp-wiki/reagents/detergents/nm/">n-Nonyl-beta-D-maltopyranoside (NM)</a> — Used for NapA elution and purification at 0.6% and 0.5%
- <a href="/xray-mp-wiki/reagents/additives/dtt/">Dithiothreitol (DTT)</a> — Used as reducing agent in TEV cleavage and functional assays
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP method used to obtain outward-facing NapA structure at 2.3 A (PDB 5BZ3)
- <a href="/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/">Isothermal Titration Calorimetry (ITC)</a> — ITC used to measure Na+, Li+, and K+ binding affinities of trapped inward-facing NapA
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/">Molecular Dynamics Simulations</a> — MD simulations confirmed core domain movement against fixed dimer domain
