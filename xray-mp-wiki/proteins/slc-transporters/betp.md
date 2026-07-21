---
title: "BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)"
created: 2026-05-29
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NATURE07819, doi/10.1038##nature11403, doi/10.1038##EMBOJ.2013.226]
verified: agent
uniprot_id: P54582
---

# BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span> <span class="expr-badge expr-native-tissue">Native tissue</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P54582">UniProt: P54582</a>

<span class="expr-badge">Corynebacterium GLUTAMICUM</span>

## Overview

BetP is a Na+-coupled glycine betaine symporter from the bacterium [Corynebacterium glutamicum](/xray-mp-wiki/organisms/corynebacterium-glutamicum). It belongs to the BCCT (Betaine/Carnitine/Choline Transporter) family and plays a critical role in osmoregulation by accumulating the compatible solute glycine betaine in response to hyperosmotic stress. BetP is activated by intracellular K+ and other osmotic stimuli through its C-terminal regulatory domain. The crystal structure revealed a homotrimeric assembly with each monomer containing 10 transmembrane helices and a distinctive 4-helix bundle regulatory domain, providing the first structural insights into osmo-sensing in a secondary transporter.


## Publications

### doi/10.1038##NATURE07819

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3jeo">3JEO</a></td>
      <td>3.35</td>
      <td>P212121</td>
      <td>SeMet-substituted BetP with N-terminal 29-residue deletion (Delta N29), N-terminal StrepII tag</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/glycine-betaine">Glycine Betaine</a>, sodium ions</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Corynebacterium glutamicum](/xray-mp-wiki/organisms/corynebacterium-glutamicum) (native expression system); also expressed in E. coli (DH5alpha) for proteoliposome reconstitution assays
- **Construct**: BetP Delta N29 (residues 30-437 of full-length 437 aa protein) with N-terminal StrepII tag; [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine)-substituted variant for SAD phasing; surface-engineered mutant BetP Delta N29/E44E45E46/AAA; substrate-specificity mutant G153D

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
      <td>Detergent solubilization from C. glutamicum membrane fractions</td>
      <td>StrepTactin resin (StrepII tag affinity)</td>
      <td>Buffer containing <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a> + Not specified</td>
      <td>Expression in C. glutamicum; mutants assessed by immuno-blotting against N-terminal StrepII tag</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging drop <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Se-Met labeled BetP Delta N29 construct</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in supplementary information</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Space group P212121; unit cell a=118.09, b=129.42, c=182.94 A; alpha=beta=gamma=90 degrees; SAD phasing with selenium sites</td>
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
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
  </tbody>
</table>
### doi/10.1038##nature11403

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ain">4AIN</a></td>
      <td>3.1</td>
      <td>Not specified</td>
      <td>Surface-engineered BetP mutant (BetP Delta N29/E44E45E46/AAA) crystallized in presence of 5 mM betaine</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/glycine-betaine">Glycine Betaine</a>, sodium ions</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4amr">4AMR</a></td>
      <td>3.25</td>
      <td>Not specified</td>
      <td>BetP G153D mutant (Gly 153 to aspartate in unfolded stretch of TMH1') co-crystallized with <a href="/xray-mp-wiki/reagents/ligands/choline">Choline</a>; sixfold increased affinity for sodium</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/choline">Choline</a>, sodium ions</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Corynebacterium glutamicum](/xray-mp-wiki/organisms/corynebacterium-glutamicum) (native expression system); also expressed in E. coli (DH5alpha) for proteoliposome reconstitution assays
- **Construct**: BetP Delta N29 (residues 30-437 of full-length 437 aa protein) with N-terminal StrepII tag; [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine)-substituted variant for SAD phasing; surface-engineered mutant BetP Delta N29/E44E45E46/AAA; substrate-specificity mutant G153D

**Purification:**

- **Expression system**: E. coli DH5alpha
- **Expression construct**: Surface-engineered BetP mutants (BetP Delta N29/E44E45E46/AAA and BetP G153D) with N-terminal StrepII tag

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
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>Not specified + beta-dodecyl-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>)</td>
      <td>Membranes solubilized using <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> for heterologously expressed BetP</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td>Strep-Tactin macroprep</td>
      <td>Strep-Tactin</td>
      <td>Not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Affinity purification via Strep-Tactin macroprep for StrepII-tagged BetP</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography)</td>
      <td>Not specified</td>
      <td>Not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) for final polishing of BetP sample</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>BetP Delta N29/E44E45E46/AAA crystallized in presence of 5 mM betaine</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected to 3.1 A at PXII beamline of Swiss Light Source (SLS); structure determined by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement">Molecular Replacement</a> using BetP (PDB 4AMR) as search model</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Co-crystallization with substrate</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>BetP G153D mutant co-crystallized with <a href="/xray-mp-wiki/reagents/ligands/choline">Choline</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected to 3.2 A at beamline id29 at ESRF; structure determined by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement">Molecular Replacement</a> using BetP (PDB 3P03) as search model</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ain">4AIN</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">ADAEEEIILEGEDTQASL</span><span class="topo-membrane">NWSVIVPALVIVLATVV</span><span class="topo-outside">WGIGFKDSFTNFASSALSAVVDN</span><span class="topo-membrane">LGWAFILFGTVFVFFIVVIA</span><span class="topo-inside">ASKFGTIRLGRIDEAPEFRTV</span><span class="topo-membrane">SWISMMFAAGMGIGLMF</span><span class="topo-outside">YGTT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EPLTFYRNGVPGHDEHNVGVAMS</span><span class="topo-membrane">TTMFHWTLHPWAIYAIVGLA</span><span class="topo-inside">IAYSTFRVGRKQLLSSAFVPLIGEKGAEGW</span><span class="topo-membrane">LGKLIDILAIIATVFGTACSLG</span><span class="topo-outside">LGALQIGAGLSAAN</span><span class="topo-unknown">II</span><span class="topo-outside">EDPSDWTIV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">G</span><span class="topo-membrane">IVSVLTLAFIFSAIS</span><span class="topo-unknown">GVGK</span><span class="topo-membrane">GIQYLSNANMVLAALLAIFVFV</span><span class="topo-outside">VGPTVSILNLLPGSIGNYLSNFFQMAGRTAMSADGTAGEWLGSWT</span><span class="topo-membrane">IFYWAWWISWSPFVGMFL</span><span class="topo-inside">ARISRGRSIREF</span><span class="topo-membrane">ILG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">VLLVPAGVSTVWFSI</span><span class="topo-outside">FGGTAIVFEQNGESIWGDGAAEEQLFGLLHALPGGQIMGII</span><span class="topo-membrane">AMILLGTFFITSADSASTVMGTMS</span><span class="topo-inside">QHGQLEA</span><span class="topo-membrane">NKWVTAAWGVATAAIGL</span><span class="topo-outside">TLLLS</span><span class="topo-unknown">GGDNA</span><span class="topo-outside">LSNLQN</span></span>
<span class="topo-ruler">       490       500       510       520       530         </span>
<span class="topo-line"><span class="topo-outside">V</span><span class="topo-membrane">TIVAATPFLFVVIGLMF</span><span class="topo-inside">ALVKDLSNDVIYLEYREQQRFNARLARERRVHNEHRKRELA</span></span>
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
      <td>18</td>
      <td>41</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>35</td>
      <td>59</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>58</td>
      <td>76</td>
      <td>98</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>78</td>
      <td>99</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>99</td>
      <td>119</td>
      <td>139</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>116</td>
      <td>140</td>
      <td>156</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>143</td>
      <td>157</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>163</td>
      <td>184</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>193</td>
      <td>204</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>215</td>
      <td>234</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>229</td>
      <td>256</td>
      <td>269</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>230</td>
      <td>231</td>
      <td>270</td>
      <td>271</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>232</td>
      <td>241</td>
      <td>272</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>256</td>
      <td>282</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>257</td>
      <td>259</td>
      <td>297</td>
      <td>299</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>261</td>
      <td>282</td>
      <td>301</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>283</td>
      <td>327</td>
      <td>323</td>
      <td>367</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>345</td>
      <td>368</td>
      <td>385</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>346</td>
      <td>357</td>
      <td>386</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>358</td>
      <td>375</td>
      <td>398</td>
      <td>415</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>376</td>
      <td>416</td>
      <td>416</td>
      <td>456</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>440</td>
      <td>457</td>
      <td>480</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>441</td>
      <td>447</td>
      <td>481</td>
      <td>487</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>448</td>
      <td>464</td>
      <td>488</td>
      <td>504</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>465</td>
      <td>469</td>
      <td>505</td>
      <td>509</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>470</td>
      <td>474</td>
      <td>510</td>
      <td>514</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>475</td>
      <td>481</td>
      <td>515</td>
      <td>521</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>482</td>
      <td>498</td>
      <td>522</td>
      <td>538</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>499</td>
      <td>539</td>
      <td>539</td>
      <td>579</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ain">4AIN</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ADAEEEIILEGEDTQ</span><span class="topo-inside">ASL</span><span class="topo-membrane">NWSVIVPALVIVLATVV</span><span class="topo-outside">WGIGFKDSFTNFASSALSAVVDN</span><span class="topo-membrane">LGWAFILFGTVFVFFIVVIA</span><span class="topo-inside">ASKFGTIRLGR</span><span class="topo-unknown">IDEAP</span><span class="topo-inside">EFRTV</span><span class="topo-membrane">SWISMMFAAGMGIGLM</span><span class="topo-outside">FYGTT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EPLTFYRNGVPGHDEHNVGVAMS</span><span class="topo-membrane">TTMFHWTLHPWAIYAIVGLA</span><span class="topo-inside">IAYSTFRVGRKQLLSSAFVPLIGEKGAEGW</span><span class="topo-membrane">LGKLIDILAIIATVFGTACSLG</span><span class="topo-outside">LGALQIGAGLSAANIIEDPSDWTIV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">G</span><span class="topo-membrane">IVSVLTLAFIFSAISGVG</span><span class="topo-unknown">K</span><span class="topo-membrane">GIQYLSNANMVLAALLAIFVFV</span><span class="topo-outside">VGPTVSILNLLPGSIGNYLSNFFQMAGRTAMSADGTAGEWLGSWT</span><span class="topo-membrane">IFYWAWWISWSPFVGMFLA</span><span class="topo-inside">RISRGRSIREF</span><span class="topo-membrane">ILG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">VLLVPAGVSTVWFSI</span><span class="topo-outside">FGGTAIVFEQNGESIWGDGAAEEQLFGLLHALPGGQIMGII</span><span class="topo-membrane">AMILLGTFFITSADSASTVMGTMS</span><span class="topo-inside">QHGQLEAN</span><span class="topo-membrane">KWVTAAWGVATAAIGL</span><span class="topo-outside">TLLLSGGDNALSNLQN</span></span>
<span class="topo-ruler">       490       500       510       520       530         </span>
<span class="topo-line"><span class="topo-outside">V</span><span class="topo-membrane">TIVAATPFLFVVIGLMF</span><span class="topo-inside">ALVKDLSNDVIYLEYREQQ</span><span class="topo-unknown">RFNARLARERRVHNEHRKRELA</span></span>
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
      <td>15</td>
      <td>41</td>
      <td>55</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>16</td>
      <td>18</td>
      <td>56</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>35</td>
      <td>59</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>58</td>
      <td>76</td>
      <td>98</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>78</td>
      <td>99</td>
      <td>118</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>89</td>
      <td>119</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>94</td>
      <td>130</td>
      <td>134</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>95</td>
      <td>99</td>
      <td>135</td>
      <td>139</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>115</td>
      <td>140</td>
      <td>155</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>143</td>
      <td>156</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>163</td>
      <td>184</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>193</td>
      <td>204</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>215</td>
      <td>234</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>216</td>
      <td>241</td>
      <td>256</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>259</td>
      <td>282</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>261</td>
      <td>282</td>
      <td>301</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>283</td>
      <td>327</td>
      <td>323</td>
      <td>367</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>346</td>
      <td>368</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>347</td>
      <td>357</td>
      <td>387</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>358</td>
      <td>375</td>
      <td>398</td>
      <td>415</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>376</td>
      <td>416</td>
      <td>416</td>
      <td>456</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>440</td>
      <td>457</td>
      <td>480</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>441</td>
      <td>448</td>
      <td>481</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>464</td>
      <td>489</td>
      <td>504</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>465</td>
      <td>481</td>
      <td>505</td>
      <td>521</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>482</td>
      <td>498</td>
      <td>522</td>
      <td>538</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>499</td>
      <td>517</td>
      <td>539</td>
      <td>557</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>518</td>
      <td>539</td>
      <td>558</td>
      <td>579</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ain">4AIN</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">ADAEEEIILEGEDT</span><span class="topo-inside">QASLNW</span><span class="topo-membrane">SVIVPALVIVLATVVW</span><span class="topo-outside">GIGFKDSFTNFASSALSAVVDN</span><span class="topo-membrane">LGWAFILFGTVFVFFIVVIAA</span><span class="topo-inside">SKFGTIRLGRIDEAPEFRTVSW</span><span class="topo-membrane">ISMMFAAGMGIGLMFYG</span><span class="topo-outside">TT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EPLTFYRNGVPGHDEHNVGVAM</span><span class="topo-membrane">STTMFHWTLHPWAIYAIVGL</span><span class="topo-inside">AIAYSTFRVGRKQLLSSAFVPLIGEKGAEGW</span><span class="topo-membrane">LGKLIDILAIIATVFGTACSLGLGA</span><span class="topo-outside">LQIGAGLSAANIIEDPSDWTIV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">GI</span><span class="topo-membrane">VSVLTLAFIFSAISGV</span><span class="topo-unknown">G</span><span class="topo-membrane">KGIQYLSNANMVLAALLAIFVFV</span><span class="topo-outside">VGPTVSILNLLPGSIGNYLSNFFQMAGRTAMSADGTAGEWLGSWT</span><span class="topo-membrane">IFYWAWWISWSPFVGMFL</span><span class="topo-inside">ARISRGRSIREFI</span><span class="topo-membrane">LG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">VLLVPAGVSTVWFSI</span><span class="topo-outside">FGGTAIVFEQNGESIWGDGAAEEQLFGLLHALPGGQIMGII</span><span class="topo-membrane">AMILLGTFFITSADSASTVMGTMS</span><span class="topo-inside">QHGQLEAN</span><span class="topo-membrane">KWVTAAWGVATAAIGLTL</span><span class="topo-outside">LLSGGDNALSNLQN</span></span>
<span class="topo-ruler">       490       500       510       520       530         </span>
<span class="topo-line"><span class="topo-outside">V</span><span class="topo-membrane">TIVAATPFLFVVIGLMF</span><span class="topo-inside">ALVKDLSNDVIYLEY</span><span class="topo-unknown">REQQRFNARLARERRVHNEHRKRELA</span></span>
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
      <td>1</td>
      <td>14</td>
      <td>41</td>
      <td>54</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>20</td>
      <td>55</td>
      <td>60</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>21</td>
      <td>36</td>
      <td>61</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>58</td>
      <td>77</td>
      <td>98</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>79</td>
      <td>99</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>101</td>
      <td>120</td>
      <td>141</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>118</td>
      <td>142</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>142</td>
      <td>159</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>162</td>
      <td>183</td>
      <td>202</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>193</td>
      <td>203</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>218</td>
      <td>234</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>219</td>
      <td>242</td>
      <td>259</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>243</td>
      <td>258</td>
      <td>283</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>260</td>
      <td>282</td>
      <td>300</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>283</td>
      <td>327</td>
      <td>323</td>
      <td>367</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>345</td>
      <td>368</td>
      <td>385</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>346</td>
      <td>358</td>
      <td>386</td>
      <td>398</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>359</td>
      <td>375</td>
      <td>399</td>
      <td>415</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>376</td>
      <td>416</td>
      <td>416</td>
      <td>456</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>440</td>
      <td>457</td>
      <td>480</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>441</td>
      <td>448</td>
      <td>481</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>466</td>
      <td>489</td>
      <td>506</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>467</td>
      <td>481</td>
      <td>507</td>
      <td>521</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>482</td>
      <td>498</td>
      <td>522</td>
      <td>538</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>499</td>
      <td>513</td>
      <td>539</td>
      <td>553</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>514</td>
      <td>539</td>
      <td>554</td>
      <td>579</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##EMBOJ.2013.226

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4c7r">4C7R</a></td>
      <td>2.70</td>
      <td>Not specified</td>
      <td>BetP Delta N29/E44E45E46/AAA surface-engineered mutant, all three protomers in inward-open (Ci) state with 8 bound POPG lipids</td>
      <td><a href="/xray-mp-wiki/reagents/additives/citrate">Citrate</a> (bound in cytoplasmic funnel), 8 POPG lipids (16:0/18:1)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Corynebacterium glutamicum](/xray-mp-wiki/organisms/corynebacterium-glutamicum) (native expression system); also expressed in E. coli (DH5alpha) for proteoliposome reconstitution assays
- **Construct**: BetP Delta N29 (residues 30-437 of full-length 437 aa protein) with N-terminal StrepII tag; [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine)-substituted variant for SAD phasing; surface-engineered mutant BetP Delta N29/E44E45E46/AAA; substrate-specificity mutant G153D

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
      <td>Detergent exchange and thorough washing</td>
      <td>StrepTactin <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> with Cymal-5 exchange</td>
      <td>StrepTactin</td>
      <td>100 mM 3Na-Citrate pH 5.4-5.5, 300 mM NaCl, 20-21% PEG400 + 1.2% Cymal-5 (detergent exchanged from <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Washing steps removed unspecifically bound lipids. TLC analysis confirmed presence of PG lipids (not PE) in the purified BetP sample.</td>
    </tr>
    <tr>
      <td>Lipid analysis by TLC</td>
      <td>Thin layer chromatography (HPTLC)</td>
      <td>Not applicable</td>
      <td>Chloroform:methanol:water (13:7:0.8) solvent system for 1D separation + Cymal-5</td>
      <td>Phospholipid analysis confirmed negatively charged PG/CL species. Cymal-5 confounded initial separation. PG identity confirmed by acetone:methanol:acetic acid:water:chloroform (2:1:1:0.5:5) system.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>BetP Delta N29/E44E45E46/AAA at ~12 mg/ml in 1.2% Cymal-5</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM 3Na-Citrate pH 5.4-5.5, 300 mM NaCl, 20-21% PEG400</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown by vapor diffusion at 18 C using 1:2 volume ratio of protein to reservoir. Single crystal yielded isotropic diffraction to 2.7 A at ESRF beamline id29. Structure determined by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement">Molecular Replacement</a> using BetP trimer (PDB 2WIT) as search model. No NCS imposed during refinement. 8 POPG lipids modeled into clear Fo-Fc densities.</td>
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
      <td>pH</td>
      <td>5.4</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>18 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Sodium Chloride: 300 mM [salt]  
- Peg 400: 20-21 % [precipitant] (PEG400)</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4c7r">4C7R</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">LENPTNLEGKLADAAAAIILEGEDTQ</span><span class="topo-inside">ASL</span><span class="topo-membrane">NWSVIVPALVIVLATVVW</span><span class="topo-outside">GIGFKDSFTNFASSALSAVVDN</span><span class="topo-membrane">LGWAFILFGTVFVFFIVVIAA</span><span class="topo-inside">SKFGTIRLGRIDEAPEFRTV</span><span class="topo-membrane">SWISMMFAAG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MGIGLMFYG</span><span class="topo-outside">TTEPLTFYRNGVPGHDEHNVGVAM</span><span class="topo-membrane">STTMFHWTLHPWAIYAIVGLAI</span><span class="topo-inside">AYSTFRVGRKQLLSSAFVPLIGEKGAEGW</span><span class="topo-membrane">LGKLIDILAIIATVFGTACSLGLGA</span><span class="topo-outside">LQIGAGLSAAN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">IIEDPSDWTIVGI</span><span class="topo-membrane">VSVLTLAFIFSAISGVG</span><span class="topo-unknown">K</span><span class="topo-membrane">GIQYLSNANMVLAALLAIFVFV</span><span class="topo-outside">VGPTVSILNLLPGSIGNYLSNFFQMAGRTAMSADGTAGEWLGSWT</span><span class="topo-membrane">IFYWAWWISWSPFVGMFLA</span><span class="topo-inside">RIS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">RGRSIREF</span><span class="topo-membrane">ILGVLLVPAGVSTVWFSIF</span><span class="topo-outside">GGTAIVFEQNGESIWGDGAAEEQLFGLLHALPGGQIMGI</span><span class="topo-membrane">IAMILLGTFFITSADSASTVMGTMSQ</span><span class="topo-inside">HGQLEA</span><span class="topo-membrane">NKWVTAAWGVATAAIGLT</span><span class="topo-outside">LLLS</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560      </span>
<span class="topo-line"><span class="topo-outside">GGDNALSNLQNV</span><span class="topo-membrane">TIVAATPFLFVVIGLMFA</span><span class="topo-inside">LVKDLSNDVIYLEYREQQRFNARLARERRVHNEHRKRELAAKRRRER</span><span class="topo-unknown">KASGAGKRR</span></span>
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
      <td>1</td>
      <td>26</td>
      <td>30</td>
      <td>55</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>29</td>
      <td>56</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>47</td>
      <td>59</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>69</td>
      <td>77</td>
      <td>98</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>90</td>
      <td>99</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>110</td>
      <td>120</td>
      <td>139</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>129</td>
      <td>140</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>153</td>
      <td>159</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>175</td>
      <td>183</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>204</td>
      <td>205</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>229</td>
      <td>234</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>253</td>
      <td>259</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>270</td>
      <td>283</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>293</td>
      <td>301</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>294</td>
      <td>338</td>
      <td>323</td>
      <td>367</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>339</td>
      <td>357</td>
      <td>368</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>368</td>
      <td>387</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>387</td>
      <td>398</td>
      <td>416</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>388</td>
      <td>426</td>
      <td>417</td>
      <td>455</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>452</td>
      <td>456</td>
      <td>481</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>453</td>
      <td>458</td>
      <td>482</td>
      <td>487</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>459</td>
      <td>476</td>
      <td>488</td>
      <td>505</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>477</td>
      <td>492</td>
      <td>506</td>
      <td>521</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>493</td>
      <td>510</td>
      <td>522</td>
      <td>539</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>511</td>
      <td>557</td>
      <td>540</td>
      <td>586</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>558</td>
      <td>566</td>
      <td>587</td>
      <td>595</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4c7r">4C7R</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">LENPTNLEGKLADAAAAIILEGEDTQ</span><span class="topo-inside">ASL</span><span class="topo-membrane">NWSVIVPALVIVLATVVW</span><span class="topo-outside">GIGFKDSFTNFASSALSAVVDN</span><span class="topo-membrane">LGWAFILFGTVFVFFIVVIAA</span><span class="topo-inside">SKFGTIRLGRIDEAPEFRTV</span><span class="topo-membrane">SWISMMFAAG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MGIGLMFYG</span><span class="topo-outside">TTEPLTFYRNGVPGHDEHNVGVAM</span><span class="topo-membrane">STTMFHWTLHPWAIYAIVGLA</span><span class="topo-inside">IAYSTFRVGRKQLLSSAFVPLIGEKGAEGW</span><span class="topo-membrane">LGKLIDILAIIATVFGTACSLGLGA</span><span class="topo-outside">LQIGAGLSAAN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">IIEDPSDWTIVGI</span><span class="topo-membrane">VSVLTLAFIFSAISGV</span><span class="topo-unknown">G</span><span class="topo-membrane">KGIQYLSNANMVLAALLAIFVFV</span><span class="topo-outside">VGPTVSILNLLPGSIGNYLSNFFQMAGRTAMSADGTAGEWLGSWT</span><span class="topo-membrane">IFYWAWWISWSPFVGMFLA</span><span class="topo-inside">RIS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">RGRSIREF</span><span class="topo-membrane">ILGVLLVPAGVSTVWFSIF</span><span class="topo-outside">GGTAIVFEQNGESIWGDGAAEEQLFGLLHALPGGQIMGI</span><span class="topo-membrane">IAMILLGTFFITSADSASTVMGTMSQ</span><span class="topo-inside">HGQLEA</span><span class="topo-membrane">NKWVTAAWGVATAAIGLT</span><span class="topo-outside">LLLS</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560      </span>
<span class="topo-line"><span class="topo-outside">GGDNALSNLQNV</span><span class="topo-membrane">TIVAATPFLFVVIGLMFA</span><span class="topo-inside">LVKDLSNDVIYLE</span><span class="topo-unknown">YREQQRFNARLARERRVHNEHRKRELAAKRRRERKASGAGKRR</span></span>
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
      <td>1</td>
      <td>26</td>
      <td>30</td>
      <td>55</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>29</td>
      <td>56</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>47</td>
      <td>59</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>69</td>
      <td>77</td>
      <td>98</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>90</td>
      <td>99</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>110</td>
      <td>120</td>
      <td>139</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>129</td>
      <td>140</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>153</td>
      <td>159</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>183</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>204</td>
      <td>204</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>229</td>
      <td>234</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>253</td>
      <td>259</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>269</td>
      <td>283</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>271</td>
      <td>293</td>
      <td>300</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>294</td>
      <td>338</td>
      <td>323</td>
      <td>367</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>339</td>
      <td>357</td>
      <td>368</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>368</td>
      <td>387</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>387</td>
      <td>398</td>
      <td>416</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>388</td>
      <td>426</td>
      <td>417</td>
      <td>455</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>427</td>
      <td>452</td>
      <td>456</td>
      <td>481</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>453</td>
      <td>458</td>
      <td>482</td>
      <td>487</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>459</td>
      <td>476</td>
      <td>488</td>
      <td>505</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>477</td>
      <td>492</td>
      <td>506</td>
      <td>521</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>493</td>
      <td>510</td>
      <td>522</td>
      <td>539</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>511</td>
      <td>523</td>
      <td>540</td>
      <td>552</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>524</td>
      <td>566</td>
      <td>553</td>
      <td>595</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4c7r">4C7R</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">LENPTNLEGKLADAAAAIILEGEDTQ</span><span class="topo-inside">ASL</span><span class="topo-membrane">NWSVIVPALVIVLATVVW</span><span class="topo-outside">GIGFKDSFTNFASSALSAVVDN</span><span class="topo-membrane">LGWAFILFGTVFVFFIVVIAA</span><span class="topo-inside">SKFGTIRLGRIDEAPEFRTV</span><span class="topo-membrane">SWISMMFAAG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">MGIGLMFYG</span><span class="topo-outside">TTEPLTFYRNGVPGHDEHNVGVAM</span><span class="topo-membrane">STTMFHWTLHPWAIYAIVGLA</span><span class="topo-inside">IAYSTFRVGRKQLLSSAFVPLIGEKGAEGW</span><span class="topo-membrane">LGKLIDILAIIATVFGTACSLGLGA</span><span class="topo-outside">LQIGAGLSAAN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">IIEDPSDWTIVGI</span><span class="topo-membrane">VSVLTLAFIFSAISGVG</span><span class="topo-unknown">K</span><span class="topo-membrane">GIQYLSNANMVLAALLAIFVFV</span><span class="topo-outside">VGPTVSILNLLPGSIGNYLSNFFQMAGRTAMSADGTAGEWLGSWT</span><span class="topo-membrane">IFYWAWWISWSPFVGMFLA</span><span class="topo-inside">RIS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">RGRSIREF</span><span class="topo-membrane">ILGVLLVPAGVSTVWFSIF</span><span class="topo-outside">GGTAIVFEQNGESIWGDGAAEEQLFGLLHALPGGQIMGII</span><span class="topo-membrane">AMILLGTFFITSADSASTVMGTMSQ</span><span class="topo-inside">HGQLEA</span><span class="topo-membrane">NKWVTAAWGVATAAIGLTL</span><span class="topo-outside">LLS</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560      </span>
<span class="topo-line"><span class="topo-outside">GGDNALSNLQNV</span><span class="topo-membrane">TIVAATPFLFVVIGLMFA</span><span class="topo-inside">LVKDLSNDVIYLEYREQQRFNA</span><span class="topo-unknown">RLARERRVHNEHRKRELAAKRRRERKASGAGKRR</span></span>
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
      <td>1</td>
      <td>26</td>
      <td>30</td>
      <td>55</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>29</td>
      <td>56</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>47</td>
      <td>59</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>69</td>
      <td>77</td>
      <td>98</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>90</td>
      <td>99</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>110</td>
      <td>120</td>
      <td>139</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>111</td>
      <td>129</td>
      <td>140</td>
      <td>158</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>153</td>
      <td>159</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>183</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>175</td>
      <td>204</td>
      <td>204</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>205</td>
      <td>229</td>
      <td>234</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>253</td>
      <td>259</td>
      <td>282</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>270</td>
      <td>283</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>293</td>
      <td>301</td>
      <td>322</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>294</td>
      <td>338</td>
      <td>323</td>
      <td>367</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>339</td>
      <td>357</td>
      <td>368</td>
      <td>386</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>368</td>
      <td>387</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>369</td>
      <td>387</td>
      <td>398</td>
      <td>416</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>388</td>
      <td>427</td>
      <td>417</td>
      <td>456</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>452</td>
      <td>457</td>
      <td>481</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>453</td>
      <td>458</td>
      <td>482</td>
      <td>487</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>459</td>
      <td>477</td>
      <td>488</td>
      <td>506</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>478</td>
      <td>492</td>
      <td>507</td>
      <td>521</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>493</td>
      <td>510</td>
      <td>522</td>
      <td>539</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>511</td>
      <td>532</td>
      <td>540</td>
      <td>561</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>533</td>
      <td>566</td>
      <td>562</td>
      <td>595</td>
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

### Trimeric assembly with central cavity

BetP forms a homotrimer with a central cavity at the interface. Aromatic side chains from helix 7 and TM2 of each monomer point into the cavity, where unmodelled Fo-Fc density (at 1.8 sigma) represents bound lipid or detergent. The trimeric interface involves residues in TM8 and TM9. The C-terminal domain of each monomer makes crystal contacts with the adjacent trimer, suggesting the regulatory domain extends beyond the transmembrane core.

### Sodium ion coordination sites

Two sodium ion binding sites (Na1 and Na2) were identified by structural superposition with [LeuT](/xray-mp-wiki/proteins/enzymes/leut)_M. Na1 is coordinated by residues in TM3i, TM3e, TM4, TM5, TM7, TM8, and TM10. Na2 involves a conserved g-x-g-x-g motif in TM3 characteristic of sodium-coupled transporters in the BCCT family. The sodium ions were not included in the refinement process but their coordination geometry supports a Na+/betaine co-transport mechanism.

### Aromatic substrate pathway

Twenty-three aromatic side chains line the substrate pathway along a central 4-helix bundle (TM3, TM4/TM8, TM9). These aromatic boxes create surface properties that allow a wide variety of osmolytes to be transported without direct interaction with the protein backbone. The [Glycine Betaine](/xray-mp-wiki/reagents/ligands/glycine-betaine) binding pocket shows homology with the periplasmic binding protein ProX from E. coli, particularly in the orientation of Trp box residues. The aromatic boxes in TM3/TM4/TM8/TM9 include W188, W189, W194, Y197, W362, W366, W371, W374, W377, and W374.

### Osmo-sensing and regulation

BetP is regulated by intracellular K+ concentration and hyperosmotic stress through its C-terminal regulatory domain. Functional analysis of mutants showed that residues E135, R210, G301, R387, and R392 are essential for transport activity. The N-terminal 29 residues (Delta N29 construct) were deleted to facilitate crystallization but the protein retained substantial activity in E. coli polar lipid proteoliposomes (268 nmol [Glycine](/xray-mp-wiki/reagents/buffers/glycine) betaine/ min mg protein vs 771 for WT).

### BCCT family structural conservation

The BetP structure was compared with other transporters of the BCCT family, including OpuD from B. subtilis, ButA from Tetragenococcus halophila, BetT from E. coli, and EctP from C. glutamicum. Sequence alignment revealed strictly conserved residues across the family. The overall fold is related to the [LeuT](/xray-mp-wiki/proteins/enzymes/leut) scaffold (RMSD 3.7 A for scaffold comparison), with similar repeat domain architecture to MFS transporters like SGLT and Mhp1. The BetP repeat domains show RMSD of 3.5 A between repeat 1 and repeat 2.

### Conformational asymmetry in BetP trimers

Crystal structures of surface-engineered BetP mutants reveal trimers that lack non-crystallographic three-fold symmetry. Each protomer within one trimer adopts a different conformation of the alternating-access cycle: a substrate-free outward-occluded (C_eoc), a substrate-free outward-open (C_e), a closed substrate-free (C_c), and a closed substrate-bound (C_cS) state. Additionally, an inward-open betaine-bound (C_iS) and inward-open [Choline](/xray-mp-wiki/reagents/ligands/choline)-bound state were captured. This conformational asymmetry allows observation of up to six distinct transport states within a single trimer, providing a comprehensive view of the transport cycle. The closed states reported for the first time for a LeuT-like fold transporter represent an intermediate between outward- and inward-facing states.

### Tryptophan prism and betaine binding

The closed substrate-bound state (C_cS) is characterized by a central binding site (S1 site) closed by nearly 14 A of protein bulk from either side of the membrane. The trimethylammonium group of betaine in the S1 site forms cation-pi interactions with Trp 373, Trp 374, and Trp 377, arranged in a tryptophan prism entirely within TMH6'. These residues comprise the signature motif of the BCCT family. Trp 377 has a dominant role and any exchange against another residue renders BetP inactive, whereas substitution of Trp 373 or Trp 374 decreases affinity. In the inward-open state (C_iS), betaine shifts towards the cytoplasm so that it solely interacts with Trp 377 in TMH6' and backbone carbonyls from TMH1'. The binding energy is exploited fully only in the transient C_cS transition state, where betaine fits perfectly.

### Sodium-binding sites Na1 and Na2

Both sodium ions bind at the interface between scaffold and bundle helices. The Na2 site provides reasonable coordination in outward-open and closed states but coordinating residues are too distant in the inward-open state due to conformational changes of TMH1a'. The Na1 site, formed by Phe 380 in TMH6', Thr 246 and Thr 250 in TMH3', is only properly coordinated in the closed state. Sodium binding to Na2 relates to opening-closing of cytoplasmic gates, while Na1 binding relates to opening-closing of periplasmic gates. The conservation of the Na2 site is the unifying element in the [LeuT](/xray-mp-wiki/proteins/enzymes/leut)-like fold transport mechanism.

### Alternating-access mechanism and gating

The alternating-access mechanism in BetP is a hybrid of rigid body movements and individual flexing of symmetry-related helices. The scaffold motif (TMH3', TMH4' in repeat 1 and TMH8', TMH9' in repeat 2) tilts about 13 degrees relative to the 4-TMH bundle. TMH1a' is displaced by approximately 5 A and tilted by 18 degrees to open the cytoplasmic gate, while TMH10' (periplasmic thin gate) moves 5.7 A with a 41 degree tilt. TMH5' (cytoplasmic thin gate) undergoes a 9 degree tilt. The presence of a closed transition state implies uncoupled hinge movements of periplasmic and cytoplasmic gates. The spring-like movement of the unfolded region of TMH1' transiently coordinates sodium ions during the alternating-access cycle, correlating with the absolute requirement of sodium for betaine symport.

### Substrate specificity and G153D mutant

Exchange of Gly 153 against aspartate in the unfolded stretch of TMH1' results in a sixfold increased affinity for sodium and additional specificity for [Choline](/xray-mp-wiki/reagents/ligands/choline). This mutation demonstrates the plasticity of the TMH1' region and its role in ion coupling. Side-chain rotations of aromatic residues in TMH1' and TMH6' (Phe 156, Phe 369, Phe 380, Phe 384) are highly conserved in the BCCT family and contribute to betaine recruitment, predominantly from outside to inside. Alanine substitution of periplasmic occluding residues decreases affinity for betaine, while mutation of cytoplasmic pathway residues did not have a major effect on affinity.

### Eight specifically bound PG lipids in the BetP trimer

The 2.7 A resolution structure of BetP (PDB 4C7R) revealed eight ordered POPG (palmitoyl-oleoyl phosphatidyl glycerol) lipids bound to the trimer at specific sites. Five lipids (L1-L5) occupy the central hydrophobic cavity of the trimer (non-annular sites), while three (L6, L7, U1) are annular lipids at the trimer periphery. Head groups were assigned to PG based on 2Fo-Fc and Fo-Fc difference maps and primarily positively charged coordinating residues. Acyl chains were assigned as 16:0/18:1 based on E. coli phospholipidome composition. The head groups of L1-L3 in the symmetrical trimer core sites are coordinated by residues from loop 2 (K121) and IL3 (R395) - both important in conformational changes during transport.

### Lipid L7 interaction with the glycine-rich unwound region of TM1 prime

Annular lipid L7 is positioned at the trimer periphery, nested between TM5 prime and TM1 prime. One of its acyl chains interacts directly with Met150 in the glycine-rich unwound stretch of TM1 prime, a region critical for conformational changes. Mutation of Met150 to isoleucine significantly alters the osmoregulation profile of BetP (requires higher osmolality for maximal activity). Mutation to phenylalanine combined with I152A results in only slightly altered osmoprofile. This suggests that the lipid L7 interaction with the catalytic core modulates osmotic stress activation.

### PG lipids as cofactors for trimer assembly and regulation

Negatively charged PG lipids constitute only 15% of the E. coli membrane but are selectively retained during affinity purification of BetP, indicating their structural necessity. The central non-annular lipids (L1-L5) are coordinated by residues from loop 2 and IL3 of adjacent chains, effectively crosslinking the trimer. Lipid L4 specifically involves the C-terminal helix of chain A (R554, R558, Q557), providing an electrostatic interaction site that restrains the positively charged C-terminal domain. These lipid-mediated interactions are proposed to regulate gating helix (TM1 prime, TM6 prime) movements during the transport cycle.

### State-dependent lipid occupancy during transport cycle

Comparing the 2.7 A inward-facing structure with lower-resolution structures of outward and closed states revealed different lipid occupancy patterns. Central non-annular lipids showed density in outward states (four lipids), only partial density in closed states (one lipid), and full occupancy in the inward-facing state (five lipids). Annular lipids were only resolved in the inward-facing state. This suggests that specific lipid-protein interactions are linked to the conformational state of BetP, potentially contributing to inactivation or activation during the transport cycle.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — BetP is a secondary active transporter using alternating-access mechanism
- <a href="/xray-mp-wiki/concepts/miscellaneous/sodium-motive-force/">Sodium-Motive Force (SMF)</a> — BetP is a Na+-coupled symporter driven by sodium electrochemical gradient
- <a href="/xray-mp-wiki/reagents/ligands/glycine-betaine/">Glycine Betaine</a> — Primary substrate/osmolyte transported by BetP
- <a href="/xray-mp-wiki/reagents/ligands/choline/">Choline</a> — Secondary substrate for BetP G153D mutant with sixfold increased sodium affinity
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for BetP membrane solubilization and purification
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/bcct-family/">BCCT Family</a> — BetP is the founding member of the BCCT transporter family
- <a href="/xray-mp-wiki/proteins/enzymes/leut/">LeuT Amino Acid Transporter</a> — [LeuT](/xray-mp-wiki/proteins/enzymes/leut) used as structural reference for BetP conformational analysis
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Used for structure determination of both BetP structures from this paper
- <a href="/xray-mp-wiki/proteins/enzymes/leut/">LeuT Amino Acid Transporter from Aquifex aeolicus</a> — BetP shares [LeuT](/xray-mp-wiki/proteins/enzymes/leut) fold topology (RMSD 3.7 A) but lacks Leu25-like side chain rotation in substrate-free states
- <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a> — Crystallization method used for structure determination
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-Exclusion Chromatography (SEC)</a> — Purification method used in protein preparation
