---
title: "CAX_Af H+/Ca2+ Exchanger (Archaeoglobus fulgidus)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.1239002]
verified: agent
uniprot_id: O29988
---

# CAX_Af H+/Ca2+ Exchanger (Archaeoglobus fulgidus)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O29988">UniProt: O29988</a>

<span class="expr-badge">Archaeoglobus fulgidus</span>

## Overview

CAX_Af is a H+/Ca2+ exchanger from the hyperthermophilic archaeon Archaeoglobus
fulgidus, belonging to the Ca2+:cation antiporter (CaCA) superfamily. It catalyzes
the exchange of Ca2+ for H+ across biological membranes to regulate cytosolic
calcium levels. The crystal structure at 2.3 A resolution (PDB 4KPP), determined
by the lipidic cubic phase (LCP) method, revealed an inward-facing conformation
with 12 transmembrane helices. Structural comparison with the Na+/Ca2+ exchanger
[NCX_Mj](/xray-mp-wiki/proteins/slc-transporters/ncx-mj/) in the outward-facing state showed that
the first and sixth transmembrane helices alternately create hydrophilic cavities
on the intra- and extracellular sides. The structures and functional analyses
provide insight into how the inward- to outward-facing state transition is triggered
by Ca2+ and H+ binding. CAX_Af is one of only two CAX family structures determined
(alongside [Vcx1](/xray-mp-wiki/proteins/slc-transporters/vcx1/)) and represents the first H+/Ca2+
exchanger structure captured in an inward-facing conformation.

## Publications

### doi/10.1126##science.1239002

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4kpp">4KPP</a></td>
      <td>2.3</td>
      <td>P212121</td>
      <td>Full-length CAX_Af (residues 1-301)</td>
      <td>none (H+ bound state)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length CAX_Af from Archaeoglobus fulgidus
- **Notes**: Expressed in E. coli for functional characterization; purified and crystallized via LCP method. Mutants (E78A, E78Q, E255A, E255Q, E258A, E258Q) were generated for functional studies.

**Purification:**

- **Expression system**: [E. coli](/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/)
- **Expression construct**: Full-length CAX_Af

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
      <td><a href="/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/">E. coli</a> expression</td>
      <td>—</td>
      <td></td>
      <td>Expressed in <a href="/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/">E. coli</a> cells for 45Ca2+ uptake assays using <a href="/xray-mp-wiki/methods/expression-systems/iptg-induction/">IPTG induction</a></td>
    </tr>
    <tr>
      <td>Purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>Purified protein crystallized by <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) method. Details in Supporting Online Material.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified CAX_Af in detergent</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized under low-pH conditions (pH 6.0-6.5) which stabilizes the H+ bound state. Structure determined by multiple anomalous dispersion (MAD) using <a href="/xray-mp-wiki/reagents/additives/mercury/">mercury</a> derivatives. Final model refined to 2.3 A resolution. Crystallographic asymmetric unit contained two molecules.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4kpp">4KPP</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">DFTKEK</span><span class="topo-membrane">FQLLAISSLTLPWLISLA</span><span class="topo-inside">FNYHHPALTQT</span><span class="topo-membrane">LLSGLAVVSASFLISWAAETAE</span><span class="topo-outside">MDVPRS</span><span class="topo-membrane">FSLAIVALLAVLPEYAVDG</span><span class="topo-inside">YFAWKAGSVGGEYVHYAT</span><span class="topo-membrane">ANMTGANRLLIGIGWSLVA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FI</span><span class="topo-outside">AFRTLKSKEVELDDGI</span><span class="topo-membrane">RLEIFFLFLATLYAFTL</span><span class="topo-inside">PLKGHISPF</span><span class="topo-membrane">DALVFVSLYAIYIYLST</span><span class="topo-outside">KAEREEVEVGGVPAYLCSLKTE</span><span class="topo-membrane">TRRLSVVVLFLFAGFTILMSV</span><span class="topo-inside">EAFSEGLLETARIAGI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">DEFLA</span><span class="topo-membrane">VQWIAPLASESPELIVAIY</span><span class="topo-outside">FVRRFRVSAS</span><span class="topo-membrane">MNALISSKVNQWTLLIGTIAI</span><span class="topo-inside">IYSISAFKLQSLPLDARQSEE</span><span class="topo-membrane">VLLTAAQSLFAVAILL</span><span class="topo-outside">DLKI</span><span class="topo-membrane">SWKEASALFLLFIVQLLF</span><span class="topo-inside">PGVEV</span><span class="topo-membrane">R</span></span>
<span class="topo-ruler">       370       380       390       400     </span>
<span class="topo-line"><span class="topo-membrane">YIISAIYIILSLPILFAKR</span><span class="topo-outside">KEIVESFRTVKRLISLE</span><span class="topo-unknown">SSGENLYFQ</span></span>
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
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>25</td>
      <td>8</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>36</td>
      <td>26</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>58</td>
      <td>37</td>
      <td>58</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>64</td>
      <td>59</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>83</td>
      <td>65</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>101</td>
      <td>84</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>122</td>
      <td>102</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>138</td>
      <td>123</td>
      <td>138</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>155</td>
      <td>139</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>156</td>
      <td>164</td>
      <td>156</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>181</td>
      <td>165</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>203</td>
      <td>182</td>
      <td>203</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>224</td>
      <td>204</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>245</td>
      <td>225</td>
      <td>245</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>264</td>
      <td>246</td>
      <td>264</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>265</td>
      <td>274</td>
      <td>265</td>
      <td>274</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>295</td>
      <td>275</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>316</td>
      <td>296</td>
      <td>316</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>317</td>
      <td>332</td>
      <td>317</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>336</td>
      <td>333</td>
      <td>336</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>337</td>
      <td>354</td>
      <td>337</td>
      <td>354</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>355</td>
      <td>359</td>
      <td>355</td>
      <td>359</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>360</td>
      <td>379</td>
      <td>360</td>
      <td>379</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>380</td>
      <td>396</td>
      <td>380</td>
      <td>396</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>397</td>
      <td>405</td>
      <td>397</td>
      <td>405</td>
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

### Inward-facing conformation with 12 transmembrane helices

CAX_Af contains 12 TM helices with both N and C termini on the intracellular side. The structure comprises a core domain (TMs 2-5, 7-10) homologous to NCX_Mj, a gating bundle (TMs 1 and 6), and two additional N- and C-terminal helices. The gating bundle (TM1 and TM6) creates hydrophilic cavities alternately on the intra- and extracellular sides during the transport cycle. In the inward-facing conformation, TM1 adopts a straight conformation creating an inward-facing cavity, while TM6 is bent and packed against the extracellular halves of TM2 and TM7.

### Mutually exclusive Ca2+ and H+ binding

The crystal structure reveals two hydrogen-bonding networks (Hext and Hmid) involving Glu78, Glu255, and Glu258 that function as H+ binding sites. These residues are also involved in Ca2+ coordination, making Ca2+ and H+ binding mutually exclusive. The structure was obtained under low pH (6.0-6.5) and represents the H+ bound state, which cannot accommodate Ca2+. This mutually exclusive binding is consistent with the counter-transport mechanism of the CaCA superfamily — H+ and Ca2+ compete for the same binding pocket.

### Two protonation states: mol A (fully protonated) and mol B (partially protonated)

The asymmetric unit contains two CAX_Af molecules. Mol A represents a 'fully' protonated state with intact Hext and Hmid hydrogen-bonding networks bridging TM7 and TM8. Mol B represents a 'partially' protonated state where Glu258 is deprotonated and the Hmid network is partially disrupted, causing TM7 to twist and create a gap between Pro77 and Pro257. This gap splits the hydrophobic patch that enables the gating bundle to slide, suggesting that H+ binding closes the hydrophobic patch and enables transition to the outward-facing state.

### Alternating access via gating bundle sliding

Comparison of the inward-facing CAX_Af structure with the outward-facing NCX_Mj structure (PDB 3V5U) revealed a common alternating access mechanism. The gating bundle helices (TM1 and TM6) slide relative to the core domain, alternately creating hydrophilic cavities for cation access. In CAX_Af, a hydrophilic cluster on TM1 (Ser47, Ser51, Glu55, Glu58) faces the inward cavity. In NCX_Mj, a hydrophilic cluster on TM6 faces the outward cavity. The transition involves a sliding motion of the gating bundle across a central hydrophobic patch formed by Pro residues and neighboring hydrophobic side chains.

### Functional importance of conserved glutamate residues

Alanine or glutamine mutations of Glu78, Glu255, or Glu258 decreased H+/Ca2+ exchange activity in liposome-based 45Ca2+ uptake assays. These residues are at equivalent positions to Na+ coordinating residues in NCX_Mj and are involved in both Ca2+ and H+ binding. The results demonstrate the importance of protonation and deprotonation of these conserved carboxylates during the exchange cycle.


## Cross-References

- <a href="/xray-mp-wiki/proteins/slc-transporters/ncx-mj/">NCX_Mj Sodium/Calcium Exchanger</a> — Homologous CaCA superfamily member; outward-facing structure used for structural comparison revealing the alternating access mechanism
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/caca-superfamily/">Ca2+:Cation Antiporter (CaCA) Superfamily</a> — CAX_Af is a member of the CAX family within the CaCA superfamily
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — CAX_Af operates via alternating access with gating bundle sliding
- <a href="/xray-mp-wiki/proteins/slc-transporters/vcx1/">Vcx1</a> — Another CAX family structure; cytosol-facing conformation for comparison
