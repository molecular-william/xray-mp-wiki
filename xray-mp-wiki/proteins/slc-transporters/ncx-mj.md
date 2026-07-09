---
title: "NCX_Mj Sodium/Calcium Exchanger from Methanococcus jannaschii"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1215759]
verified: regex
uniprot_id: Q57556
---

# NCX_Mj Sodium/Calcium Exchanger from Methanococcus jannaschii

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q57556">UniProt: Q57556</a>

<span class="expr-badge">Methanocaldococcus jannaschii</span>

## Overview

NCX_Mj is a sodium/calcium exchanger (NCX) from the archaeon Methanococcus jannaschii, belonging to the cation-Ca2+ exchanger superfamily. It is a membrane transporter that catalyzes the electrogenic exchange of three Na+ ions for one Ca2+ ion across the cell membrane, playing an essential role in maintaining Ca2+ homeostasis. Like all NCX proteins, it contains two highly conserved homologous alpha repeat sequence motifs arising from a gene-duplication event. NCX_Mj lacks the large intracellular regulatory domain found in eukaryotic NCX homologs, making it a minimal functional unit for ion transport. Its 1.9 A crystal structure revealed an outward-facing conformation with 10 transmembrane helices and four clustered ion-binding sites, providing the first structural insight into the NCX ion-exchange mechanism.


## Publications

### doi/10.1126##science.1215759

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3v5u">3V5U</a></td>
      <td>1.9</td>
      <td>P212121</td>
      <td>Full-length NCX_Mj</td>
      <td>Ca2+, Na+ (modeled in binding sites)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3v5u">3V5U</a></td>
      <td>3.6</td>
      <td>P212121</td>
      <td>Full-length NCX_Mj (conventional crystallization in detergent)</td>
      <td>Cd2+ or Mn2+ (at divalent blockage site)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length NCX_Mj from Methanococcus jannaschii
- **Notes**: Expressed in E. coli cells for functional characterization via 45Ca2+ flux assays. Purification and crystallization construct details not specified in main text.

**Purification:**

- **Expression system**: Escherichia coli
- **Expression construct**: Full-length NCX_Mj

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
      <td>Expression</td>
      <td>E. coli expression</td>
      <td>—</td>
      <td></td>
      <td>NCX_Mj expressed in E. coli cells</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td>Not detailed in main text</td>
      <td>—</td>
      <td></td>
      <td>Purification details in Supporting Online Material. Protein used for both LCP and conventional crystallization.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified NCX_Mj in detergent (buffer details not specified in main text)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>LCP crystallization yielded well-diffracting crystals of P212121 space group with one subunit per asymmetric unit. Structure determined by SIRAS using samarium-derivatized crystals and refined to 1.9 A resolution.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified NCX_Mj in detergent</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Conventional crystallization in detergent yielded crystals diffracting to 3.6 A. Structure determined by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using LCP structure as search model. CdCl2 or MnCl2 were essential additives, binding at the Smid site (divalent blockage site). Structure virtually identical to LCP structure.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3v5u">3V5U</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MVI</span><span class="topo-membrane">LGVGYFLLGLILLYYGSDWFV</span><span class="topo-inside">LGSERIARHFNVSNFVI</span><span class="topo-membrane">GATVMAIGTSLPEILTSA</span><span class="topo-outside">YASYMHAPGISI</span><span class="topo-membrane">GNAIGSCICNIGLVLGLSAII</span><span class="topo-inside">SPIIVDKNLQK</span><span class="topo-membrane">NILVYLLFVIFAAVIGI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">DGFSW</span><span class="topo-membrane">IDGVVLLILFIIYLRWT</span><span class="topo-inside">VKNGSA</span><span class="topo-unknown">EIEENND</span><span class="topo-inside">KNNPSVVFSLV</span><span class="topo-membrane">LLIIGLIGVLVGAELFVDGA</span><span class="topo-outside">KKIALALDISDKVIGFTL</span><span class="topo-membrane">VAFGTSLPELMVSLAAA</span><span class="topo-inside">KRNLGGM</span><span class="topo-membrane">VLGNVIGSNIAD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320</span>
<span class="topo-line"><span class="topo-membrane">IGGALAVGSL</span><span class="topo-outside">FMHLPAEN</span><span class="topo-membrane">VQMAVLVIMSLLLYLFA</span><span class="topo-inside">KYSKI</span><span class="topo-membrane">GRWQGILFLALYIIAIAS</span><span class="topo-outside">LRMGGG</span><span class="topo-unknown">SLVPRGSRSHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (24 regions)</summary>
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
      <td>41</td>
      <td>25</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>59</td>
      <td>42</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>71</td>
      <td>60</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>92</td>
      <td>72</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>103</td>
      <td>93</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>120</td>
      <td>104</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>125</td>
      <td>121</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>142</td>
      <td>126</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>148</td>
      <td>143</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>155</td>
      <td>149</td>
      <td>155</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>166</td>
      <td>156</td>
      <td>166</td>
      <td>Inside</td>
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
      <td>204</td>
      <td>187</td>
      <td>204</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>221</td>
      <td>205</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>228</td>
      <td>222</td>
      <td>228</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>250</td>
      <td>229</td>
      <td>250</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>258</td>
      <td>251</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>275</td>
      <td>259</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>280</td>
      <td>276</td>
      <td>280</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>298</td>
      <td>281</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>304</td>
      <td>299</td>
      <td>304</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>320</td>
      <td>305</td>
      <td>320</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3v5u">3V5U</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MVI</span><span class="topo-membrane">LGVGYFLLGLILLYYGSDWFV</span><span class="topo-inside">LGSERIARHFNVSNFVI</span><span class="topo-membrane">GATVMAIGTSLPEILTSA</span><span class="topo-outside">YASYMHAPGISI</span><span class="topo-membrane">GNAIGSCICNIGLVLGLSAII</span><span class="topo-inside">SPIIVDKNLQK</span><span class="topo-membrane">NILVYLLFVIFAAVIGI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">DGFSW</span><span class="topo-membrane">IDGVVLLILFIIYLRWT</span><span class="topo-inside">VKNGSA</span><span class="topo-unknown">EIEENND</span><span class="topo-inside">KNNPSVVFSLV</span><span class="topo-membrane">LLIIGLIGVLVGAELFVDGA</span><span class="topo-outside">KKIALALDISDKVIGFTL</span><span class="topo-membrane">VAFGTSLPELMVSLAAA</span><span class="topo-inside">KRNLGGM</span><span class="topo-membrane">VLGNVIGSNIAD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320</span>
<span class="topo-line"><span class="topo-membrane">IGGALAVGSL</span><span class="topo-outside">FMHLPAEN</span><span class="topo-membrane">VQMAVLVIMSLLLYLFA</span><span class="topo-inside">KYSKI</span><span class="topo-membrane">GRWQGILFLALYIIAIAS</span><span class="topo-outside">LRMGGG</span><span class="topo-unknown">SLVPRGSRSHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (24 regions)</summary>
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
      <td>41</td>
      <td>25</td>
      <td>41</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>42</td>
      <td>59</td>
      <td>42</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>71</td>
      <td>60</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>92</td>
      <td>72</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>103</td>
      <td>93</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>120</td>
      <td>104</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>125</td>
      <td>121</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>142</td>
      <td>126</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>148</td>
      <td>143</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>149</td>
      <td>155</td>
      <td>149</td>
      <td>155</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>156</td>
      <td>166</td>
      <td>156</td>
      <td>166</td>
      <td>Inside</td>
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
      <td>204</td>
      <td>187</td>
      <td>204</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>221</td>
      <td>205</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>222</td>
      <td>228</td>
      <td>222</td>
      <td>228</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>250</td>
      <td>229</td>
      <td>250</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>258</td>
      <td>251</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>275</td>
      <td>259</td>
      <td>275</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>280</td>
      <td>276</td>
      <td>280</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>298</td>
      <td>281</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>299</td>
      <td>304</td>
      <td>299</td>
      <td>304</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>305</td>
      <td>320</td>
      <td>305</td>
      <td>320</td>
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

### Overall architecture and topology

NCX_Mj exists as a monomer with 10 transmembrane (TM) helices and
both termini on the extracellular side. Eight helices (TMs 2-5 and
7-10) form a tightly packed core perpendicularly embedded in the
membrane. TMs 1 and 6 are exceptionally long (~35 residues each),
oriented at ~45 degrees to the membrane surface, and loosely packed
against the core. The two alpha repeats (TMs 2-3 for alpha-1 and
TMs 7-8 for alpha-2) are bundled in the center surrounded by other
helices. Based on sequence similarity, eukaryotic NCX likely shares
the same 10-TM topology rather than the previously predicted 9-TM
topology.

### Four ion-binding sites with distinct specificities

Four ion-binding sites cluster at the center of NCX_Mj, related by
a two-fold rotational axis. SCa is specifically designed for Ca2+
binding with six oxygen ligands (backbone carbonyls of Thr50 and
Thr209, carboxylates of Glu54 and Glu213) from the GTSLPE signature
sequence within the alpha repeats. Three Na+ sites (Sext, Smid, Sint)
are arranged in a winding single file. Sext and Sint are optimized
for Na+ with five coordinating ligands. Smid has only four oxygen
ligands (tetradentate), making it suboptimal and allowing Na+
binding only at high concentration. The four sites share ligands -
Glu54 and Glu213 are shared by multiple sites, creating competition
between Na+ and Ca2+ binding.

### Outward-facing conformation and ion passageways

The NCX_Mj structure represents an outward-facing conformation with
two deep cavities on the extracellular surface providing independent
solvent-accessible passageways for external ion access to the
central binding sites. One passage connects to Sext and is surrounded
by TMs 3A, 7A, 7B, 9, and 10. The second connects to SCa and is
surrounded by TMs 3A, 7A, 5, and 6.

### Proposed inward-facing model and alternating access mechanism

Based on the two-fold symmetry of NCX_Mj, an inward-facing model
was proposed involving a simple sliding motion of TMs 1, 2A, 6,
and 7A hinged at bends between TMs 2A-2B and 7A-7B. The movement
slides these peripheral helices across a central hydrophobic patch,
closing the two outward-facing passageways and forming two
inward-facing ones. This rapid interchange between outward and
inward conformations enables the [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) for
consecutive ion-exchange reactions.

### Mechanism of 3:1 Na+:Ca2+ exchange stoichiometry

The exchange mechanism explains the 3:1 stoichiometry. Starting
with Ca2+ bound at SCa in the outward-facing state, two Na+ ions
first occupy Sext and Sint, competing for negatively charged ligands
shared with SCa and reducing Ca2+ affinity. A third Na+ occupies
Smid, further reducing Ca2+ affinity and causing Ca2+ release to the
extracellular side. After conformational change to the inward-facing
state, bound Na+ ions are released sequentially into the low
intracellular Na+ environment. Na+ release restores high Ca2+
affinity at SCa, and the cycle repeats. The mechanism does not
preclude alternative exchange ratios (e.g., transport of four Na+
ions when Ca2+ site is occupied by Na+).


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/nhaa/">Na+/H+ Antiporter NhaA from Escherichia coli</a> — Related Na+-coupled membrane transporter with alternating access mechanism
- <a href="/xray-mp-wiki/proteins/slc-transporters/clc-ec1/">CLC-ec1 Cl-/H+ Antiporter</a> — Another ion-coupled antiporter with known structure and mechanistic studies
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rocker-switch-mechanism/">Rocker-Switch Mechanism</a> — NCX_Mj alternating access transport mechanism shares principles with rocker-switch
- <a href="/xray-mp-wiki/proteins/abc-transporters/maltose-transporter-malfgk2/">Maltose Transporter MalFGK2 (E. coli)</a> — ABC transporter with alternating access mechanism for comparison
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
