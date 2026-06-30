---
title: "Pseudomonas aeruginosa LptB2FG LPS Extraction Complex"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.3399]
verified: false
---

# Pseudomonas aeruginosa LptB2FG LPS Extraction Complex

## Overview

LptB2FG is an ATP-binding cassette (ABC) transporter complex responsible for extracting lipopolysaccharide (LPS) molecules from the outer leaflet of the inner membrane and transporting them to the periplasmic chaperone LptC in Gram-negative bacteria. The complex consists of two copies of the cytoplasmic ATPase LptB and two transmembrane proteins, LptF and LptG, each containing six transmembrane helices and a periplasmic beta-jellyroll-like domain. The crystal structure of nucleotide-free LptB2FG from Pseudomonas aeruginosa reveals a large outward-facing V-shaped cavity formed by the LptF and LptG transmembrane domains, which is proposed to accommodate the [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) moiety of LPS. The structure represents a resting state distinct from classical ABC transporters that transport substrates across the membrane.


## Publications

### doi/10.1038##nsmb.3399

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5x5y">5X5Y</a></td>
      <td>3.46</td>
      <td>P2(1)2(1)2(1)</td>
      <td>Pseudomonas aeruginosa LptB with C-terminal hexahistidine tag, LptF, and LptG co-expressed</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C43(DE3)
- **Construct**: C-terminal hexahistidine-tagged LptB co-expressed with untagged LptF and LptG using pQLink vectors
- **Induction**: 0.1 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at 20 degC overnight
- **Media**: LB medium

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
      <td>French press</td>
      <td></td>
      <td>20 mM Tris, pH 8.0, 150 mM NaCl</td>
      <td>Single passage at 16,000 psi; debris removed by centrifugation at 18,000 rpm for 1 hour; total membranes collected</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a>, pH 8.0, 300 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Solubilized for 1 hour at 4 degC; supernatant collected by centrifugation at 18,000 rpm for 1 hour</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA agarose</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a>, pH 8.0, 150 mM NaCl, 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluted from Ni-NTA agarose beads</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 (GE Healthcare)</td>
      <td>20 mM Tris, pH 7.5, 150 mM NaCl + 0.06% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Used for ATPase activity assays; protein concentrations determined by Bradford assay</td>
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
      <td>LptB2FG complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M HEPES, pH 7.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 degC</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>1 ul protein mixed with 1 ul reservoir solution. Best crystals obtained in solution containing 0.1 M HEPES pH 7.0.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5x5y">5X5Y</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">ATLKAQHLAKSYKGRQVVRDVSMSIDSGQIVGLLGPNGAGKTTCFYMIVGLVQADQGVVRIDEQNVTHLPMHGRARAGIGYLPQEASIFRKLSVSDNIMAILETRSDLDRNGRKEALEG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LLQEFHIHHIRDNLGMSLSGGERRRVEIARALASAPKFILLDEPFAGVDPISVGDIKQIIHHLKAKGIGILITDHNVRETLDICETAYIVNDGQLIAEGDAESILANDLVKEVYLGHEFR</span></span>
<span class="topo-ruler">       </span>
<span class="topo-line"><span class="topo-unknown">LHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>240</td>
      <td>2</td>
      <td>240</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5x5y">5X5Y</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">ATLKAQHLAKSYKGRQVVRDVSMSIDSGQIVGLLGPNGAGKTTCFYMIVGLVQADQGVVRIDEQNVTHLPMHGRARAGIGYLPQEASIFRKLSVSDNIMAILETRSDLDRNGRKEALEG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LLQEFHIHHIRDNLGMSLSGGERRRVEIARALASAPKFILLDEPFAGVDPISVGDIKQIIHHLKAKGIGILITDHNVRETLDICETAYIVNDGQLIAEGDAESILANDLVKEVYLGHEFR</span></span>
<span class="topo-ruler">       </span>
<span class="topo-line"><span class="topo-unknown">LHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>240</td>
      <td>2</td>
      <td>240</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5x5y">5X5Y</a> — Chain G (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MVKLDRYI</span><span class="topo-membrane">GVTVFVAILAVLGVILGLALLFAFIDEL</span><span class="topo-inside">NDISASYGIGDA</span><span class="topo-membrane">LRFIFLTAPRRAYDMLPMAALIGCLVGLG</span><span class="topo-outside">TLASNS</span><span class="topo-unknown">ELTIMR</span><span class="topo-outside">AAGVSLS</span><span class="topo-membrane">RIVWAVMKPMLVLMLAGILVGEYV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">AP</span><span class="topo-inside">WTENIAQSGRALAQGGGDSQSSKRGLWHRQGREYIHINAVQPNGVLYGVTRYRFDEQRGLESASFAKRARFETDHWQLEEVTTTLLHP</span><span class="topo-unknown">REK</span><span class="topo-inside">RSEVVKLPTERWDAQLSPQLLNTVVME</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350     </span>
<span class="topo-line"><span class="topo-inside">PEALSISGLWQYIHYLADQGLNNNRYWL</span><span class="topo-membrane">AFWTKVLQPLVTAALVLMAISFIF</span><span class="topo-outside">GPLRSVTL</span><span class="topo-membrane">GQRIFTGVLVGFVFRIAQDLLGPSS</span><span class="topo-inside">LVFDF</span><span class="topo-membrane">PPLLAVVIPASICALAGVWLLR</span><span class="topo-outside">RA</span><span class="topo-unknown">G</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>8</td>
      <td>1</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>36</td>
      <td>9</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>48</td>
      <td>37</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>77</td>
      <td>49</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>83</td>
      <td>78</td>
      <td>83</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>89</td>
      <td>84</td>
      <td>89</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>90</td>
      <td>96</td>
      <td>90</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>122</td>
      <td>97</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>210</td>
      <td>123</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>268</td>
      <td>214</td>
      <td>268</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>269</td>
      <td>292</td>
      <td>269</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>293</td>
      <td>300</td>
      <td>293</td>
      <td>300</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>301</td>
      <td>325</td>
      <td>301</td>
      <td>325</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>326</td>
      <td>330</td>
      <td>326</td>
      <td>330</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>352</td>
      <td>331</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>354</td>
      <td>353</td>
      <td>354</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5x5y">5X5Y</a> — Chain F (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MIVFRYL</span><span class="topo-membrane">SREVLVTMSAVSAVLLVIIMSGRFIK</span><span class="topo-inside">YLAQAAQGLLDPGSLFLIM</span><span class="topo-membrane">AFRIPGFLQLILPLGLFLGILLAYG</span><span class="topo-outside">RLYLES</span><span class="topo-unknown">EMTVLS</span><span class="topo-outside">ATGMSQK</span><span class="topo-membrane">RLLGYTMAPALLVAILVAWLSLFL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-inside">PQGINQFALLLNKQDTLTEFDTLVPGRFQAMRDGTRVTYTEELSKDRGELAGIFISQKDL</span><span class="topo-unknown">NS</span><span class="topo-inside">SNQERGISILVAEKGTQNIQADGSRYLILHNGYRYDGNPGQANYRAIQYDTYGVMLP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KP</span><span class="topo-unknown">EASSEVSER</span><span class="topo-inside">DAVPTADLFGSDNPRYQAEL</span><span class="topo-membrane">QWRLSTPLLVFVVTLLAVPLSR</span><span class="topo-outside">VNPRQG</span><span class="topo-membrane">RFLKLLPAILLYMGYLALLIAVR</span><span class="topo-inside">GQLDKGKIPM</span><span class="topo-membrane">AIGLWWVHGLFLAIGLLLFYW</span><span class="topo-unknown">EPLRLKL</span></span>
<span class="topo-ruler">  </span>
<span class="topo-line"><span class="topo-unknown">A</span><span class="topo-outside">S</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>33</td>
      <td>8</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>52</td>
      <td>34</td>
      <td>52</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>77</td>
      <td>53</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>83</td>
      <td>78</td>
      <td>83</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>89</td>
      <td>84</td>
      <td>89</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>90</td>
      <td>96</td>
      <td>90</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>121</td>
      <td>97</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>181</td>
      <td>122</td>
      <td>181</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>242</td>
      <td>184</td>
      <td>242</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>271</td>
      <td>252</td>
      <td>271</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>293</td>
      <td>272</td>
      <td>293</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>294</td>
      <td>299</td>
      <td>294</td>
      <td>299</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>322</td>
      <td>300</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>323</td>
      <td>332</td>
      <td>323</td>
      <td>332</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>333</td>
      <td>353</td>
      <td>333</td>
      <td>353</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>354</td>
      <td>361</td>
      <td>354</td>
      <td>361</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>362</td>
      <td>362</td>
      <td>362</td>
      <td>362</td>
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

### LPS extraction mechanism by LptB2FG

The nucleotide-free LptB2FG structure reveals a large V-shaped cavity (approximately 25 A x 45 A at the membrane-periplasm interface, 10 A deep) formed by the 12 TM helices of LptF and LptG, which are all bent outward. The inner surface of the IM cavity is hydrophobic, while the IM-periplasm interface is positively charged, suggesting the cavity accommodates the hydrophobic fatty acyl chains and negatively charged phosphate groups of [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/). Limited van der Waals contacts between LptF TM1-LptG TM5 and LptF TM5-LptG TM1 suggest these interfaces may open further upon ATP binding to allow LPS lateral entry from the IM outer leaflet. Mutational analysis of conserved hydrophobic residues lining the cavity caused growth defects in E. coli, supporting the cavity's role in LPS binding.

### Coupling helices and LptB interactions

The coupling helices connecting TM2 and TM3 of LptF and LptG each interact with one LptB subunit on the cytoplasmic side. Residues LptF(S83, E84, V87) and LptG(N82, E84) contribute hydrogen bonds to LptB, supported by van der Waals contacts (V87 of LptF, I87 of LptG with F90 of LptB). Complementation assays showed that E84K mutation in LptF_Ec and E88K in LptG_Ec were lethal. The LptB dimer in the nucleotide-free structure resembles the inward-facing state of canonical ABC exporters; ATP binding is predicted to induce dimerization and closure similar to that seen in E. coli AMP-PNP-bound LptB, potentially enlarging the cavity for LPS loading.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/lptb2fgc-complex/">LptB2FGC LPS Transport Complex</a> — Related LPS transport complex from Enterobacter cloacae and Vibrio cholerae that includes the accessory protein LptC
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Used in crystallization reservoir at 0.1 M, pH 7.0
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Used at 1% for membrane solubilization and 0.06-0.1% in purification buffers
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/lipids/lipid-a/">Lipid A</a> — Additive used in purification or crystallization buffers
