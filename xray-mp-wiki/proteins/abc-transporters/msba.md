---
title: "MsbA Lipid A Flippase"
created: 2026-06-11
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, pump, xray-crystallography]
sources: [doi/10.1016##j.str.2019.04.007, doi/10.1038##s41586-018-0083-5]
verified: agent
uniprot_id: ['P63359', 'Q8FJB1']
---

# MsbA Lipid A Flippase

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P63359">UniProt: P63359</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8FJB1">UniProt: Q8FJB1</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

MsbA is an essential ATP-binding cassette (ABC) transporter in Gram-negative bacteria that transports [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) and lipopolysaccharide (LPS) from the cytoplasmic leaflet to the periplasmic leaflet of the inner membrane. MsbA functions as a homodimeric lipid flippase powered by ATP binding and hydrolysis in the nucleotide-binding domains (NBDs). The 2.8 A crystal structure of MsbA from Salmonella typhimurium (PDB 6BL6) captured in an inward-facing conformation with [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) bound reveals a large amplitude opening in the transmembrane portal likely required for [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) access. The 2.9 A crystal structure of E. coli MsbA in complex with the quinoline inhibitor G907 (PDB 6BPL) reveals an unprecedented mechanism of ABC transporter inhibition, trapping MsbA in an inward-facing LPS-bound conformation and uncoupling the nucleotide-binding domains.


## Publications

### doi/10.1016##j.str.2019.04.007

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6bl6">6BL6</a></td>
      <td>2.8</td>
      <td>P2(1)2,2</td>
      <td>Full-length MsbA from Salmonella typhimurium; co-crystallized with <a href="/xray-mp-wiki/reagents/lipids/lipid-a/">Lipid A</a> in facial amphiphile <a href="/xray-mp-wiki/reagents/detergents/fa-3/">FA-3 (Facade-EM Facial Amphiphile)</a></td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6o30">6O30</a></td>
      <td>4.46</td>
      <td>P2(1)2,2</td>
      <td>Full-length MsbA; apo (no <a href="/xray-mp-wiki/reagents/lipids/lipid-a/">Lipid A</a> added)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3); expression in LB medium; induction with [IPTG](/xray-mp-wiki/reagents/additives/iptg/)

- **Construct**: Full-length MsbA from S. typhimurium with N-terminal His10 tag in pET19b vector

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: Full-length MsbA with N-terminal His10 tag
- **Tag info**: N-terminal His10 tag

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
      <td>Microfluidizer</td>
      <td>—</td>
      <td></td>
      <td>Membranes isolated by ultracentrifugation</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/udm/">UDM</a> (n-undecyl-beta-D-maltopyranoside)</td>
      <td>Membrane pellets solubilized in 1.5% <a href="/xray-mp-wiki/reagents/detergents/udm/">UDM</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> agarose</td>
      <td></td>
      <td>Column washed with 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> in buffer containing 0.1% <a href="/xray-mp-wiki/reagents/detergents/udm/">UDM</a></td>
    </tr>
    <tr>
      <td>Detergent exchange</td>
      <td>Exchange to <a href="/xray-mp-wiki/reagents/detergents/fa-3/">FA-3 (Facade-EM Facial Amphiphile)</a></td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/fa-3/">FA-3 (Facade-EM Facial Amphiphile)</a> (Facade-EM, 0.04 wt%)</td>
      <td>Detergent exchanged from <a href="/xray-mp-wiki/reagents/detergents/udm/">UDM</a> to <a href="/xray-mp-wiki/reagents/detergents/fa-3/">FA-3 (Facade-EM Facial Amphiphile)</a> using 100 kD cutoff centrifugal filters</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>—</td>
      <td></td>
      <td>Polishing step in buffer containing <a href="/xray-mp-wiki/reagents/detergents/fa-3/">FA-3 (Facade-EM Facial Amphiphile)</a></td>
    </tr>
  </tbody>
</table>
**Final sample**: MsbA in buffer with 0.04% [FA-3 (Facade-EM Facial Amphiphile)](/xray-mp-wiki/reagents/detergents/fa-3/), supplemented with 5 uM [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/), concentrated to ~12 mg/ml

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (hanging drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>MsbA (12 mg/ml) in 0.04% <a href="/xray-mp-wiki/reagents/detergents/fa-3/">FA-3 (Facade-EM Facial Amphiphile)</a>, 5 uM <a href="/xray-mp-wiki/reagents/lipids/lipid-a/">Lipid A</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M Tris, 0.2 M tri-sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> (pH 6.34-7.0), 0.12 M LiSO4, 32.5% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 300</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1 to 1:0.7</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>5 days to ~2 months</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew to 200-500 um. Apo crystals grown under same conditions without <a href="/xray-mp-wiki/reagents/lipids/lipid-a/">Lipid A</a>.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
    <tr>
      <td>Variant</td>
      <td>hanging-drop</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>6.34</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Tris: 0.1 M [buffer]  
- Peg: 32.5 % [precipitant] (PEG 300)</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bl6">6BL6</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">LS</span><span class="topo-unknown">TWQTFRRLWPTIAPFK</span><span class="topo-membrane">AGLIVAGIALILNAASDTFMLSLLKPLLD</span><span class="topo-outside">DGFGATDRSV</span><span class="topo-membrane">LLWMPLVVIGLMILRGITSYISSYCI</span><span class="topo-inside">SWVSGKVVMTMRRRLFGHMMGMPVAFFDKQSTGTLLS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RITYDSEQVASSSSGAL</span><span class="topo-membrane">ITVVREGASIIGLFIMMFYYSW</span><span class="topo-outside">Q</span><span class="topo-membrane">LSIILVVLAPIVSIAIRVVS</span><span class="topo-inside">KRFRSISKNMQNTMGQVTTSAEQMLKGHKEVLIFGGQEVETKRFDKVSNKMRLQGMKMVS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ASS</span><span class="topo-membrane">ISDPIIQLIASLALAFVLYAASF</span><span class="topo-outside">PSVMDS</span><span class="topo-membrane">LTAGTITVVFSSMIALMRPLKSLT</span><span class="topo-inside">NVNAQFQRGMAACQTLFAILDSEQEKDEGKRVIDRATGDLEFRNVTFTYPGREVPALRNINLKI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PAGKTVALVGRSGSGKSTIASLITRFYDIDEGHILMDGHDLREYTLASLRNQVALVSQNVHLFNDTVANNIAYARTEEYSREQIEEAARMAYAMDFINKMDNGLDTIIGENGVLLSGGQR</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570      </span>
<span class="topo-line"><span class="topo-inside">QRIAIARALLRDSPILILDEATSALDTESERAIQAALDELQKNRTSLVIAHRLSTIEQADEIVVVEDGIIVERGTHSELLAQHGVYAQLHKMQFG</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>7</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>18</td>
      <td>9</td>
      <td>24</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>47</td>
      <td>25</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>57</td>
      <td>54</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>83</td>
      <td>64</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>137</td>
      <td>90</td>
      <td>143</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>159</td>
      <td>144</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>160</td>
      <td>166</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>180</td>
      <td>167</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>243</td>
      <td>187</td>
      <td>249</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>266</td>
      <td>250</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>272</td>
      <td>273</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>296</td>
      <td>279</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>575</td>
      <td>303</td>
      <td>581</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bl6">6BL6</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">LS</span><span class="topo-unknown">TWQTFRRLWPTIAPFK</span><span class="topo-membrane">AGLIVAGIALILNAASDTFMLSLLKPLLD</span><span class="topo-outside">DGFGATDRSV</span><span class="topo-membrane">LLWMPLVVIGLMILRGITSYISSYCI</span><span class="topo-inside">SWVSGKVVMTMRRRLFGHMMGMPVAFFDKQSTGTLLS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RITYDSEQVASSSSGAL</span><span class="topo-membrane">ITVVREGASIIGLFIMMFYYSW</span><span class="topo-outside">Q</span><span class="topo-membrane">LSIILVVLAPIVSIAIRVVS</span><span class="topo-inside">KRFRSISKNMQNTMGQVTTSAEQMLKGHKEVLIFGGQEVETKRFDKVSNKMRLQGMKMVS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ASS</span><span class="topo-membrane">ISDPIIQLIASLALAFVLYAASF</span><span class="topo-outside">PSVMDS</span><span class="topo-membrane">LTAGTITVVFSSMIALMRPLKSLT</span><span class="topo-inside">NVNAQFQRGMAACQTLFAILDSEQEKDEGKRVIDRATGDLEFRNVTFTYPGREVPALRNINLKI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PAGKTVALVGRSGSGKSTIASLITRFYDIDEGHILMDGHDLREYTLASLRNQVALVSQNVHLFNDTVANNIAYARTEEYSREQIEEAARMAYAMDFINKMDNGLDTIIGENGVLLSGGQR</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570      </span>
<span class="topo-line"><span class="topo-inside">QRIAIARALLRDSPILILDEATSALDTESERAIQAALDELQKNRTSLVIAHRLSTIEQADEIVVVEDGIIVERGTHSELLAQHGVYAQLHKMQFG</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>7</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>18</td>
      <td>9</td>
      <td>24</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>47</td>
      <td>25</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>57</td>
      <td>54</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>83</td>
      <td>64</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>137</td>
      <td>90</td>
      <td>143</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>138</td>
      <td>159</td>
      <td>144</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>160</td>
      <td>166</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>180</td>
      <td>167</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>243</td>
      <td>187</td>
      <td>249</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>266</td>
      <td>250</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>272</td>
      <td>273</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>296</td>
      <td>279</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>575</td>
      <td>303</td>
      <td>581</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6o30">6O30</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">LS</span><span class="topo-unknown">TWQTFRRLWPTIAPFK</span><span class="topo-membrane">AGLIVAGIALILNAASDTFMLSLLKPLLD</span><span class="topo-outside">DGFGKTDRSV</span><span class="topo-membrane">LLWMPLVVIGLMILRGITSYISSYCI</span><span class="topo-inside">SWVSGKVVMTMRRRLFGHMMGMPVAFFDKQSTGTLLS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RITYDSEQVASSSSGA</span><span class="topo-membrane">LITVVREGASIIGLFIMMFYYSW</span><span class="topo-outside">Q</span><span class="topo-membrane">LSIILVVLAPIVSIAIRVVS</span><span class="topo-inside">KRFRSISKNMQNTMGQVTTSAEQMLKGHKEVLIFGGQEVETKRFDKVSNKMRLQGMKMVS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ASS</span><span class="topo-membrane">ISDPIIQLIASLALAFVLYAASF</span><span class="topo-outside">PSVMDS</span><span class="topo-membrane">LTAGTITVVFSSMIALMRPLKSLT</span><span class="topo-inside">NVNAQFQRGMAACQTLFAILDSEQEKDEGKRVIDRATGDLEFRNVTFTYPGREVPALRNINLKI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PAGKTVALVGRSGSGKSTIASLITRFYDIDEGHILMDGHDLREYTLASLRNQVALVSQNVHLFNDTVANNIAYARTEEYSREQIEEAARMAYAMDFINKMDNGLDTIIGENGVLLSGGQR</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570      </span>
<span class="topo-line"><span class="topo-inside">QRIAIARALLRDSPILILDEATSALDTESERAIQAALDELQKNRTSLVIAHRLSTIEQADEIVVVEDGIIVERGTHSELLAQHGVYAQLHKMQFG</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>7</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>18</td>
      <td>9</td>
      <td>24</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>47</td>
      <td>25</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>57</td>
      <td>54</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>83</td>
      <td>64</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>136</td>
      <td>90</td>
      <td>142</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>159</td>
      <td>143</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>160</td>
      <td>166</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>180</td>
      <td>167</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>243</td>
      <td>187</td>
      <td>249</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>266</td>
      <td>250</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>272</td>
      <td>273</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>296</td>
      <td>279</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>575</td>
      <td>303</td>
      <td>581</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6o30">6O30</a> — Chain C (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">LS</span><span class="topo-unknown">TWQTFRRLWPTIAPFK</span><span class="topo-membrane">AGLIVAGIALILNAASDTFMLSLLKPLLD</span><span class="topo-outside">DGFGKTDRSV</span><span class="topo-membrane">LLWMPLVVIGLMILRGITSYISSYCI</span><span class="topo-inside">SWVSGKVVMTMRRRLFGHMMGMPVAFFDKQSTGTLLS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RITYDSEQVASSSSGA</span><span class="topo-membrane">LITVVREGASIIGLFIMMFYYSW</span><span class="topo-outside">Q</span><span class="topo-membrane">LSIILVVLAPIVSIAIRVVS</span><span class="topo-inside">KRFRSISKNMQNTMGQVTTSAEQMLKGHKEVLIFGGQEVETKRFDKVSNKMRLQGMKMVS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ASS</span><span class="topo-membrane">ISDPIIQLIASLALAFVLYAASF</span><span class="topo-outside">PSVMDS</span><span class="topo-membrane">LTAGTITVVFSSMIALMRPLKSLT</span><span class="topo-inside">NVNAQFQRGMAACQTLFAILDSEQEKDEGKRVIDRATGDLEFRNVTFTYPGREVPALRNINLKI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PAGKTVALVGRSGSGKSTIASLITRFYDIDEGHILMDGHDLREYTLASLRNQVALVSQNVHLFNDTVANNIAYARTEEYSREQIEEAARMAYAMDFINKMDNGLDTIIGENGVLLSGGQR</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570      </span>
<span class="topo-line"><span class="topo-inside">QRIAIARALLRDSPILILDEATSALDTESERAIQAALDELQKNRTSLVIAHRLSTIEQADEIVVVEDGIIVERGTHSELLAQHGVYAQLHKMQFG</span><span class="topo-unknown">Q</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>7</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>18</td>
      <td>9</td>
      <td>24</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>47</td>
      <td>25</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>57</td>
      <td>54</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>83</td>
      <td>64</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>136</td>
      <td>90</td>
      <td>142</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>159</td>
      <td>143</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>160</td>
      <td>166</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>161</td>
      <td>180</td>
      <td>167</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>243</td>
      <td>187</td>
      <td>249</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>266</td>
      <td>250</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>272</td>
      <td>273</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>296</td>
      <td>279</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>575</td>
      <td>303</td>
      <td>581</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s41586-018-0083-5

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6bpl">6BPL</a></td>
      <td>2.9</td>
      <td></td>
      <td>E. coli MsbA in complex with G907 and LPS</td>
      <td>G907</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6bpp">6BPP</a></td>
      <td></td>
      <td></td>
      <td>E. coli MsbA in complex with G247 and LPS</td>
      <td>G247</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6bpl">6BPL</a></td>
      <td></td>
      <td></td>
      <td>E. coli MsbA in complex with G592 and LPS</td>
      <td>G592</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3); expression in LB medium; induction with [IPTG](/xray-mp-wiki/reagents/additives/iptg/)

- **Construct**: Full-length MsbA from S. typhimurium with N-terminal His10 tag in pET19b vector

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bpl">6BPL</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SHN</span><span class="topo-inside">DKDLSTWQTFRRLWPTIAPFKAGLI</span><span class="topo-membrane">VAGVALILNAASDTFMLSLLKPLLD</span><span class="topo-outside">DGFGKTDRS</span><span class="topo-membrane">VLVWMPLVVIGLMILRGITSYVSS</span><span class="topo-inside">YCISWVSGKVVMTMRRRLFGHMMGMPVSFFDKQS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TGTLLSRITYDSEQVASSSSGALI</span><span class="topo-membrane">TVVREGASIIGLFIMMFYYSW</span><span class="topo-unknown">Q</span><span class="topo-membrane">LSIILIVLAPIVSIAIRVVS</span><span class="topo-inside">KRFRNISKNMQNTMGQVTTSAEQMLKGHKEVLIFGGQEVETKRFDKVSNRMRLQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GMKMVSASSI</span><span class="topo-membrane">SDPIIQLIASLALAFVLYAASF</span><span class="topo-outside">PSVMDSL</span><span class="topo-membrane">TAGTITVVFSSMIALMRPLKSLT</span><span class="topo-inside">NVNAQFQRGMAACQTLFTILDSEQEKDEGKRVIERATGDVEFRNVTFTYPGRDVPALR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NINLKIPAGKTVALVGRSGSGKSTIASLITRFYDIDEGEILMDGHDLREYTLASLRNQVALVSQNVHLFNDTVANNIAYARTEQYSREQIEEAARMAYAMDFINKMDNGLDTVIGENGVL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580  </span>
<span class="topo-line"><span class="topo-inside">LSGGQRQRIAIARALLRDSPILILDEATSALDTESERAIQAALDELQKNRTSLVIAHRLSTIEKADEIVVVEDGVIVERGTHNDLLEHRGVYAQLHKMQ</span><span class="topo-unknown">FGQ</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>28</td>
      <td>4</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>53</td>
      <td>29</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>62</td>
      <td>54</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>86</td>
      <td>63</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>144</td>
      <td>87</td>
      <td>144</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>165</td>
      <td>145</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>186</td>
      <td>167</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>250</td>
      <td>187</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>272</td>
      <td>251</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>279</td>
      <td>273</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>302</td>
      <td>280</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>303</td>
      <td>579</td>
      <td>303</td>
      <td>579</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>580</td>
      <td>582</td>
      <td>580</td>
      <td>582</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bpl">6BPL</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SHNDKD</span><span class="topo-inside">LSTWQTFRRLWPTIAPFKAGLIVAG</span><span class="topo-membrane">VALILNAASDTFMLSLLKPLLDDGF</span><span class="topo-outside">GKTD</span><span class="topo-membrane">RSVLVWMPLVVIGLMILRGITSYVS</span><span class="topo-inside">SYCISWVSGKVVMTMRRRLFGHMMGMPVSFFDKQS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TGTLLSRITYDSEQVASSSSGALIT</span><span class="topo-membrane">VVREGASIIGLFIMMFYYSW</span><span class="topo-unknown">Q</span><span class="topo-membrane">LSIILIVLAPIVSIAIRVVS</span><span class="topo-inside">KRF</span><span class="topo-unknown">RNISKNMQ</span><span class="topo-inside">NTMGQVTTSAEQMLKGHKEVLIFGGQEVETKRFDKVSNRMRLQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GMKMVSASS</span><span class="topo-membrane">ISDPIIQLIASLALAFVLYAASF</span><span class="topo-outside">PSVMDS</span><span class="topo-membrane">LTAGTITVVFSSMIALMRPLKSLT</span><span class="topo-inside">NVNAQFQRGMAACQTLFTILDSEQEKDEGKRVIERATGDVEFRNVTFTYPGRDVPALR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NINLKIPAGKTVALVGRSGSGKSTIASLITRFYDIDEGEILMDGHDLREYTLASLRNQVALVSQNVHLFNDTVANNIAYARTEQYSREQIEEAARMAYAMDFINKMDNGLDTVIGENGVL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580  </span>
<span class="topo-line"><span class="topo-inside">LSGGQRQRIAIARALLRDSPILILDEATSALDTESERAIQAALDELQKNRTSLVIAHRLSTIEKADEIVVVEDGVIVERGTHNDLLEHRGVYAQLHKMQ</span><span class="topo-unknown">FGQ</span></span>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>31</td>
      <td>7</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>56</td>
      <td>32</td>
      <td>56</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>60</td>
      <td>57</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>85</td>
      <td>61</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>145</td>
      <td>86</td>
      <td>145</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>165</td>
      <td>146</td>
      <td>165</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>186</td>
      <td>167</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>189</td>
      <td>187</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>197</td>
      <td>190</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>249</td>
      <td>198</td>
      <td>249</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>272</td>
      <td>250</td>
      <td>272</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>278</td>
      <td>273</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>302</td>
      <td>279</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>303</td>
      <td>579</td>
      <td>303</td>
      <td>579</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>580</td>
      <td>582</td>
      <td>580</td>
      <td>582</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bpp">6BPP</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SHN</span><span class="topo-inside">DKDLSTWQTFRRLWPTIAPF</span><span class="topo-membrane">KAGLIVAGVALILNAASDTFMLSLL</span><span class="topo-outside">KPLLDDGFGKTDRSVLVWMP</span><span class="topo-membrane">LVVIGLMILRGITSYVSSYCISW</span><span class="topo-inside">VSGKVVMTMRRRLFGHMMGMPVSFFDKQS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TGTLLSRITYDSEQVASSSS</span><span class="topo-membrane">GALITVVREGASIIGLFIMMFY</span><span class="topo-outside">YSW</span><span class="topo-membrane">QLSIILIVLAPIVSIAIRVVSKRF</span><span class="topo-inside">RNISKNMQNTMGQVTTSAEQMLKGHKEVLIFGGQEVETKRFDKVSNRMRLQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GMKMVS</span><span class="topo-membrane">ASSISDPIIQLIASLALAFVLYA</span><span class="topo-outside">ASFPSVMDSLTAGTIT</span><span class="topo-membrane">VVFSSMIALMRPLKSLTNVN</span><span class="topo-inside">AQFQRGMAACQTLFTILDSEQEKDEGKRVIERATGDVEFRNVTFTYPGRDVPALR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NINLKIPAGKTVALVGRSGSGKSTIASLITRFYDIDEGEILMDGHDLREYTLASLRNQVALVSQNVHLFNDTVANNIAYARTEQYSREQIEEAARMAYAMDFINKMDNGLDTVIGENGVL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580  </span>
<span class="topo-line"><span class="topo-inside">LSGGQRQRIAIARALLRDSPILILDEATSALDTESERAIQAALDELQKNRTSLVIAHRLSTIEKADEIVVVEDGVIVERGTHNDLLEHRGVYAQLHKMQ</span><span class="topo-unknown">FGQ</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>23</td>
      <td>4</td>
      <td>23</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>48</td>
      <td>24</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>68</td>
      <td>49</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>69</td>
      <td>91</td>
      <td>69</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>140</td>
      <td>92</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>162</td>
      <td>141</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>165</td>
      <td>163</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>189</td>
      <td>166</td>
      <td>189</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>246</td>
      <td>190</td>
      <td>246</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>269</td>
      <td>247</td>
      <td>269</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>285</td>
      <td>270</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>305</td>
      <td>286</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>579</td>
      <td>306</td>
      <td>579</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>580</td>
      <td>582</td>
      <td>580</td>
      <td>582</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bpp">6BPP</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SHNDKDL</span><span class="topo-inside">STWQTFRRLWPTIAPFKA</span><span class="topo-membrane">GLIVAGVALILNAASDTFMLSLL</span><span class="topo-outside">KPLLDDGFGKTDRSVLV</span><span class="topo-membrane">WMPLVVIGLMILRGITSYVSSYCI</span><span class="topo-inside">SWVSGKVVMTMRRRLFGHMMGMPVSFFDKQS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TGTLLSRITYDSEQVASSSS</span><span class="topo-membrane">GALITVVREGASIIGLFIMMF</span><span class="topo-outside">YYSWQLS</span><span class="topo-membrane">IILIVLAPIVSIAIRVVS</span><span class="topo-unknown">KRFRNISKNMQ</span><span class="topo-inside">NTMGQVTTSAEQMLKGHKEVLIFGGQEVETKRFDKVSNRMRLQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">GMKMV</span><span class="topo-membrane">SASSISDPIIQLIASLALAFV</span><span class="topo-outside">LYAASFPSVMDSLTAGTIT</span><span class="topo-membrane">VVFSSMIALMRPLKSLTNVNAQF</span><span class="topo-inside">QRGMAACQTLFTILDSEQEKDEGKRVIERATGDVEFRNVTFTYPGRDVPALR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NINLKIPAGKTVALVGRSGSGKSTIASLITRFYDIDEGEILMDGHDLREYTLASLRNQVALVSQNVHLFNDTVANNIAYARTEQYSREQIEEAARMAYAMDFINKMDNGLDTVIGENGVL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580  </span>
<span class="topo-line"><span class="topo-inside">LSGGQRQRIAIARALLRDSPILILDEATSALDTESERAIQAALDELQKNRTSLVIAHRLSTIEKADEIVVVEDGVIVERGTHNDLLEHRGVYAQLHKMQ</span><span class="topo-unknown">FGQ</span></span>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>8</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>48</td>
      <td>26</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>66</td>
      <td>89</td>
      <td>66</td>
      <td>89</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>90</td>
      <td>140</td>
      <td>90</td>
      <td>140</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>161</td>
      <td>141</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>168</td>
      <td>162</td>
      <td>168</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>169</td>
      <td>186</td>
      <td>169</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>197</td>
      <td>187</td>
      <td>197</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>198</td>
      <td>245</td>
      <td>198</td>
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
      <td>285</td>
      <td>267</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>308</td>
      <td>286</td>
      <td>308</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>309</td>
      <td>579</td>
      <td>309</td>
      <td>579</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>580</td>
      <td>582</td>
      <td>580</td>
      <td>582</td>
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

### Intermediate inward-facing conformation with open membrane portals

The MsbA structure at 2.8 A reveals an inward-facing conformation with NBD separation of 75.6 A (between T561 Calpha), intermediate between the wide-open 5.3 A structure (PDB 3B5W) and the more closed [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure (PDB 5TV4). Large portals open between TM4 and TM6 on opposite sides, lined by positively charged residues (K194, R190, K187, R183 on TM4; R310, Q309, N305, N303, K299 on TM6) that may recognize the negatively charged sugar groups of LPS/lipid A. This intermediate state is proposed to represent an active transport-competent conformation.

### Putative lipid A binding sites inside and outside MsbA

Electron density attributed to [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) was observed both inside the TM cavity (canonical binding site) and on an outer surface cleft at the periplasmic ends of TM1-3. The internal binding site is consistent with the trap and flip model. The external surface site, formed upon closure of the V-shaped opening between TM1 and TM3 as MsbA resets from outward- to inward-facing, may serve as a post-transport docking site where [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) briefly resides after export, prior to downstream processing by LPS transport proteins.

### Dual-mode inhibition by quinoline compounds

The 2.9 A structure of E. coli MsbA in complex with G907 (PDB 6BPL) reveals dual-mode inhibition: (1) transmembrane trapping - G907 wedges into an architecturally conserved transmembrane pocket, locking MsbA in an inward-facing, LPS-bound conformation that prevents transition to the outward-facing state; (2) NBD uncoupling - the two NBDs adopt an asymmetric conformation not previously observed, uncoupling ATP binding/hydrolysis from the LPS transport cycle.

### Conformational cycle for lipid A transport

Based on comparative analysis with existing MsbA structures, a sequential transport pathway is proposed: (1) lateral opening of membrane portals allows bulky [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) entry from the cytoplasmic leaflet; (2) inward motion of TMDs increases affinity for bound [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) and shuttles it toward the periplasmic side; (3) ATP binding dimerizes NBDs, switching to an outward-facing conformation; (4) ATP hydrolysis and phosphate/ADP release resets the transporter to inward-facing. The inward-facing state may represent both the starting and end state of one complete transport cycle.

### Facial amphiphile FA-3 enables high-resolution MsbA structure

The facial amphiphile [FA-3 (Facade-EM Facial Amphiphile)](/xray-mp-wiki/reagents/detergents/fa-3/) (Facade-EM, 3alpha-hydroxy-7alpha,12alpha-di-((O-beta-D-maltosyl)-2-hydroxyethoxy)-cholane) was essential for obtaining well-diffracting crystals of MsbA. [FA-3 (Facade-EM Facial Amphiphile)](/xray-mp-wiki/reagents/detergents/fa-3/) maintained MsbA ATPase activity comparable to lipid bilayer conditions (~200 nmol/min/mg at 5 mM ATP) and provided superior thermal stability (Tm ~57 C) compared to conventional detergents. Co-crystallization with [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) further stabilized the protein, enabling 2.8 A resolution.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-allosteric-regulation/">ABC Transporter Allosteric Regulation</a> — MsbA is an ABC transporter; its conformational cycle involves allosteric coupling between NBDs and TMDs
- <a href="/xray-mp-wiki/reagents/lipids/pope/">POPE (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine)</a> — POPE lipids used in MD simulations to study MsbA-lipid A interactions and in ATPase activity measurements
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/dual-mode-inhibition-abc-transporters/">Dual-Mode Inhibition of ABC Transporters</a> — Quinoline inhibitors (G907, G247) exhibit dual-mode inhibition of MsbA
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Buffer component in purification or crystallization
