---
title: "Cannabinoid Receptor 2 (CNR2/CB2)"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2020.01.008, doi/10.1016##j.cell.2018.12.011]
verified: false
---

# Cannabinoid Receptor 2 (CNR2/CB2)

## Overview

[Cannabinoid](/xray-mp-wiki/concepts/cannabinoid) receptor 2 (CNR2, commonly known as CB2) is a class A G protein-coupled receptor that is the principal peripheral target of cannabinoids. Unlike CB1, CB2 is primarily expressed in the immune system and periphery, with minimal expression in the central nervous system. CB2 modulates immune responses, inflammation, and pain sensation without psychoactive effects. CB2 shares 44% total sequence identity and 68% sequence similarity in the transmembrane regions with CB1. CB2 is activated by endogenous cannabinoids and synthetic agonists, coupling primarily to Gi proteins. CB2 has therapeutic potential for inflammatory and neuropathic pain management without CB1 psychoactivity.


## Publications

### doi/10.1016##j.cell.2020.01.008

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6kpc">6KPC</a></td>
      <td>3.2</td>
      <td></td>
      <td>Wild-type human CB2 (14656 construct); N-terminal BRIL fusion for stability; agonist <a href="/xray-mp-wiki/reagents/ligands/am12033">AM12033</a> bound</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/am12033">AM12033</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6kpf">6KPF</a></td>
      <td>2.9</td>
      <td></td>
      <td>CB2-N-BRIL fusion; co-expressed with heterotrimeric <a href="/xray-mp-wiki/proteins/gi-protein">Gi Protein</a> and scFv16 antibody fragment; agonist AM12033 bound; active state</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/am12033">AM12033</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (Bac-to-Bac [Baculovirus Expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression))
- **Construct**: N-BRIL fused wild-type human CB2; N-terminal HA signal sequence followed by 10x His-tag and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag); human Gαi1 and Gβ1γ2 subunits cloned into pFastBac1 and pFastDual vector individually
- **Notes**: CB2 and Gi heterotrimer co-expressed in [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/sf9-insect-cells) at 27C for 48 h. Sf9 cells infected at 2-2.5 x 10^6 cells/mL with three separate virus preparations for CB2, Gαi1, and Gβ1γ2 at ratio of 1:2:2.

**Purification:**

- **Expression system**: Sf9 insect cells (Bac-to-Bac [Baculovirus Expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression))
- **Expression construct**: CB2-N-BRIL fusion with HA signal, 10x His-tag, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag)
- **Tag info**: HA signal, 10x His (N-terminal), [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag)

<<<<<<< HEAD
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
      <td>Cell infection</td>
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression">Baculovirus</a> infection</td>
      <td></td>
      <td></td>
      <td>Sf9 cells infected at 2-2.5 x 10^6 cells/mL with CB2, Gαi1, Gβ1γ2 viruses at 1:2:2 ratio, 27C for 48 h</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Cell lysis</td>
      <td></td>
      <td></td>
      <td>Infected cells cultured at 27C for 48 h, harvested by centrifugation, pellets stored at -80C</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Centrifugation</td>
      <td></td>
      <td></td>
      <td>Cell pellets harvested by centrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng">LMNG</a> + 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>CB2-Gi-<a href="/xray-mp-wiki/reagents/antibodies/scfv16">scFv16</a> complex solubilized with <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> and <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td>Metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> IMAC</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>, 20 uM AM841 + 0.1% <a href="/xray-mp-wiki/reagents/detergents/lmng">LMNG</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his-tag">His Tag</a> capture on <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC resin overnight at 4C</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Protease cleavage</td>
      <td></td>
      <td></td>
      <td>C-terminal 10x His tag cleaved by human <a href="/xray-mp-wiki/reagents/additives/human-rhinovirus-3c-protease">Human Rhinovirus 3C Protease</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td>Hiload Superdex 75 10/300</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 100 mM NaCl</td>
      <td>Monomeric fractions pooled, concentrated, flash frozen</td>
    </tr>
  </tbody>
</table>
=======
##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell infection | [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression) infection |  |  | Sf9 cells infected at 2-2.5 x 10^6 cells/mL with CB2, Gαi1, Gβ1γ2 viruses at 1:2:2 ratio, 27C for 48 h |
| Cell lysis | Cell lysis |  |  | Infected cells cultured at 27C for 48 h, harvested by centrifugation, pellets stored at -80C |
| Membrane isolation | Centrifugation |  |  | Cell pellets harvested by centrifugation |
| Solubilization | Detergent solubilization |  | 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng) + 0.001% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | CB2-Gi-[scFv16](/xray-mp-wiki/reagents/antibodies/scfv16) complex solubilized with [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) and [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) |
| [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | Metal [Affinity Chromatography](/xray-mp-wiki/methods/purification/affinity-chromatography) | [TALON](/xray-mp-wiki/reagents/additives/talon) IMAC | 25 mM HEPES pH 7.5, 100 mM NaCl, 10% glycerol, 0.1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole), 20 uM AM841 + 0.1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng) + 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | [His Tag](/xray-mp-wiki/reagents/protein-tags/his-tag) capture on [TALON](/xray-mp-wiki/reagents/additives/talon/) IMAC resin overnight at 4C |
| Tag cleavage | Protease cleavage |  |  | C-terminal 10x His tag cleaved by human [Human Rhinovirus 3C Protease](/xray-mp-wiki/reagents/additives/human-rhinovirus-3c-protease) |
| [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography) | Hiload Superdex 75 10/300 | 20 mM [HEPES](/xray-mp-wiki/reagents/buffers/hepes) pH 7.5, 100 mM NaCl | Monomeric fractions pooled, concentrated, flash frozen |

>>>>>>> d0e2c437136bdf2885afc6a99e0a9d4117821696
**Final sample**: not specified
**Purity**: Monomeric fractions by [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic Cubic Phase</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/am12033">AM12033</a>-bound CB2</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
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
      <td>2 weeks; dehydrated to 40 mm x 20 mm after 2 weeks</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown by <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a>; harvested with micro-mounts (MiTeGen) and flash frozen in liquid nitrogen; data collected at Spring-8 beamline 41XU with Pilatus3 6M detector at 1.0000 A wavelength</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6kpc">6KPC</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFAG</span><span class="topo-inside">APPMKDYMILSGPQKTA</span><span class="topo-membrane">VAVLCTLLGLLSALENVAVLYLILSS</span></span>
<span class="topo-line"><span class="topo-outside">HQLRRKP</span><span class="topo-membrane">SYLFIGSLALADFLASVVFACSFV</span><span class="topo-inside">NFHVFHGVDSKAVFLL</span><span class="topo-membrane">KIGSVTMTFTASV</span></span>
<span class="topo-line"><span class="topo-membrane">GSLLLAAIDRY</span><span class="topo-outside">LCLRYPPSYKALLTR</span><span class="topo-membrane">GRALVLLGIMWVLSALVSYLPLM</span><span class="topo-inside">GWTCCPRPCSE</span></span>
<span class="topo-line"><span class="topo-inside">LFPLIPND</span><span class="topo-membrane">YLLSWLLFIAFLFSGIIYTYAHVL</span><span class="topo-outside">WKAHQHVASNIFEMLRIDEGLRLKIYKD</span></span>
<span class="topo-line"><span class="topo-outside">TEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILR</span></span>
<span class="topo-line"><span class="topo-outside">NAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYN</span></span>
<span class="topo-line"><span class="topo-outside">QTPNRAKRVITTFRTGTWDAYARMRLDVEL</span><span class="topo-membrane">AKTLGLVLAVLLICWFPVLALMAH</span><span class="topo-inside">SLATTL</span></span>
<span class="topo-line"><span class="topo-inside">SDQVKKA</span><span class="topo-membrane">FAFCSMLCLINSMVNPVIYALRS</span><span class="topo-outside">EEIRSSAHHCLA</span><span class="topo-unknown">HWKKCVRGLGEFLEVLFQ</span></span>
<span class="topo-line"><span class="topo-unknown">GPHHHHHHHHHHDYKDDDDK</span></span>
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
      <td>17</td>
      <td>2</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>34</td>
      <td>19</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>60</td>
      <td>36</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>67</td>
      <td>62</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>91</td>
      <td>69</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>107</td>
      <td>93</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>131</td>
      <td>109</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>146</td>
      <td>133</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>169</td>
      <td>148</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>188</td>
      <td>171</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>212</td>
      <td>190</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>221</td>
      <td>214</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>381</td>
      <td>1001</td>
      <td>1160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>390</td>
      <td>235</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>391</td>
      <td>414</td>
      <td>244</td>
      <td>267</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>415</td>
      <td>427</td>
      <td>268</td>
      <td>280</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>450</td>
      <td>281</td>
      <td>303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>451</td>
      <td>462</td>
      <td>304</td>
      <td>315</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>463</td>
      <td>500</td>
      <td>316</td>
      <td>353</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6kpf">6KPF</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MG</span><span class="topo-inside">CTLSAEDKAAVERSKMIDRNLREDGEKAAREVKLLLLGAGESGKSTIVKQMK</span><span class="topo-unknown">IIHEAG</span></span>
<span class="topo-line"><span class="topo-unknown">YSEEECKQYKAVVYSNTIQSIIAIIRAMGRLKIDFGDSARADDARQLFVLAGAAEEGFMT</span></span>
<span class="topo-line"><span class="topo-unknown">AELAGVIKRLWKDSGVQACFNRSREYQLNDSAAYYLNDLDRIAQPNYIPTQQDVLRTRVK</span></span>
<span class="topo-line"><span class="topo-unknown">T</span><span class="topo-inside">TGIVETHFTFKDLHFKMFDVGGQRSERKKWIHCFEGVTAIIFCVALSDYDL</span><span class="topo-unknown">VLAEDEE</span><span class="topo-inside">M</span></span>
<span class="topo-line"><span class="topo-inside">NRMHESMKLFDSICNNKWFTDTSIILFLNKKDLFEEKIKKSPLTICYPEYAGSNTYEEAA</span></span>
<span class="topo-line"><span class="topo-inside">AYIQCQFEDLNKRKDTKEIYTHFTCATDTKNVQFVFDAVTDVIIKNNLKDCGLF</span></span>
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
      <td>54</td>
      <td>3</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>181</td>
      <td>55</td>
      <td>181</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>182</td>
      <td>232</td>
      <td>182</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>239</td>
      <td>233</td>
      <td>239</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>240</td>
      <td>354</td>
      <td>240</td>
      <td>354</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6kpf">6KPF</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MS</span><span class="topo-inside">ELDQLRQEAEQLKNQIRDARKACADATLSQITNNIDPVGRIQMRTRRTLRGHLAKIYA</span></span>
<span class="topo-line"><span class="topo-inside">MHWGTDSRLLVSASQDGKLIIWDSYTTNKVHAIPLRSSWVMTCAYAPSGNYVACGGLDNI</span></span>
<span class="topo-line"><span class="topo-inside">CSIYNLKTREGNVRVSRELAGHTGYLSCCRFLDDNQIVTSSGDTTCALWDIETGQQTTTF</span></span>
<span class="topo-line"><span class="topo-inside">TGHTGDVMSLSLAPDTRLFVSGACDASAKLWDVREGMCRQTFTGHESDINAICFFPNGNA</span></span>
<span class="topo-line"><span class="topo-inside">FATGSDDATCRLFDLRADQELMTYSHDNIICGITSVSFSKSGRLLLAGYDDFNCNVWDAL</span></span>
<span class="topo-line"><span class="topo-inside">KADRAGVLAGHDNRVSCLGVTDDGMAVATGSWDSFLKIWN</span></span>
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
      <td>340</td>
      <td>3</td>
      <td>340</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6kpf">6KPF</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MASNNT</span><span class="topo-inside">ASIAQARKLVEQLKMEANIDRIKVSKAAADLMAYCEAHAKEDPLLTPVPASENP</span></span>
<span class="topo-line"><span class="topo-inside">FRE</span><span class="topo-unknown">KKFFCAIL</span></span>
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
      <td>63</td>
      <td>7</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>71</td>
      <td>64</td>
      <td>71</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6kpf">6KPF</a> — Chain R (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MEECWVTEIANGSKDGLDSN</span><span class="topo-outside">PMKDYMILSGP</span><span class="topo-membrane">QKTAVAVLCTLLGLLSALENVAVLYLILS</span></span>
<span class="topo-line"><span class="topo-inside">SHQLRRKPSY</span><span class="topo-membrane">LFIGSLAGADFLASVVFACSFVNFH</span><span class="topo-outside">VFHGVDSKAV</span><span class="topo-membrane">FLLKIGSVTMTFTAS</span></span>
<span class="topo-line"><span class="topo-membrane">VGSLLLTAI</span><span class="topo-inside">DRYLCLRYPPSYKALLTRGRA</span><span class="topo-membrane">LVTLGIMWVLSALVSYLPLMGWT</span><span class="topo-outside">CCPRPCS</span></span>
<span class="topo-line"><span class="topo-outside">ELFPLI</span><span class="topo-membrane">PNDYLLSWLLFIAFLFSGIIYTYG</span><span class="topo-inside">HVLWKAHQHVASLSGHQ</span><span class="topo-unknown">DRQVPGMAR</span><span class="topo-inside">MRLD</span></span>
<span class="topo-line"><span class="topo-inside">VRLAKT</span><span class="topo-membrane">LGLVLAVLLICWFPVLALMAHSLAT</span><span class="topo-outside">TLSDQ</span><span class="topo-membrane">VKKAFAFCSMLCLINSMVNPVIYA</span></span>
<span class="topo-line"><span class="topo-membrane">LR</span><span class="topo-inside">SGEIRSSAHHCLAHWKK</span><span class="topo-unknown">CVRGLGSEAKEEAPRSSVTETEADGKITPWPDSRDLDLSDC</span></span>
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
      <td>20</td>
      <td>1</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>21</td>
      <td>31</td>
      <td>21</td>
      <td>31</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>60</td>
      <td>32</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>70</td>
      <td>61</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>95</td>
      <td>71</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>105</td>
      <td>96</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>129</td>
      <td>106</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>150</td>
      <td>130</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>173</td>
      <td>151</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>186</td>
      <td>174</td>
      <td>186</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>210</td>
      <td>187</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>227</td>
      <td>211</td>
      <td>227</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>236</td>
      <td>228</td>
      <td>236</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>237</td>
      <td>246</td>
      <td>237</td>
      <td>246</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>271</td>
      <td>247</td>
      <td>271</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>276</td>
      <td>272</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>302</td>
      <td>277</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>303</td>
      <td>319</td>
      <td>303</td>
      <td>319</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>320</td>
      <td>360</td>
      <td>320</td>
      <td>360</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1016##j.cell.2018.12.011

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5zty">5ZTY</a></td>
      <td>2.8</td>
      <td>P2(1)2(1)2(1)</td>
      <td>CB2-T4L fusion (ICL3 replaced with T4L); N-term 1-20 and C-term 326-360 truncated; G78L, T127A, T153L, R242E, G304E mutations</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/am10257">AM10257</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (Bac-to-Bac [Baculovirus Expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression))
- **Construct**: N-BRIL fused wild-type human CB2; N-terminal HA signal sequence followed by 10x His-tag and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag); human Gαi1 and Gβ1γ2 subunits cloned into pFastBac1 and pFastDual vector individually
- **Notes**: CB2 and Gi heterotrimer co-expressed in [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/sf9-insect-cells) at 27C for 48 h. Sf9 cells infected at 2-2.5 x 10^6 cells/mL with three separate virus preparations for CB2, Gαi1, and Gβ1γ2 at ratio of 1:2:2.

**Purification:**

- **Expression system**: [Sf9 Insect Cells](/xray-mp-wiki/methods/expression-systems/sf9-insect-cells) (Bac-to-Bac [Baculovirus Expression](/xray-mp-wiki/methods/expression-systems/baculovirus-expression))
- **Expression construct**: CB2-T4L fusion (ICL3 residues 222-235 replaced by T4L); N-term residues 1-20 and C-term 326-360 truncated; G78L, T127A, T153L, R242E, G304E mutations
- **Tag info**: None (no affinity tag)

<<<<<<< HEAD
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
      <td>Cell infection</td>
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression">Baculovirus</a> infection</td>
      <td></td>
      <td></td>
      <td>Sf9 cells infected at 2-2.5 x 10^6 cells/mL with high-titer viral stock, MOI 5.0; harvested 48 h post-infection</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Centrifugation and washing</td>
      <td></td>
      <td>10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl (hypotonic); 10 mM HEPES pH 7.5, 1.0 M NaCl, 10 mM MgCl2, 20 mM KCl (high osmotic)</td>
      <td>Membranes lysed by repeated washing and centrifugation; incubated with 20 uM AM10257 and inhibitor cocktail at 4C for 3 h; 1.0 mg/mL <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> added for 1 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>50 mM HEPES pH 7.5, 500 mM NaCl + 0.75% (w/v) <a href="/xray-mp-wiki/reagents/detergents/lmng">LMNG</a> + 0.15% (w/v) <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Membranes solubilized for 2.5-3 h at 4C; supernatant isolated by ultracentrifugation</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography">IMAC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> <a href="/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography">IMAC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> IMAC resin</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 500 mM NaCl, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.02% (w/v) <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>, 20 uM AM10257 + 0.1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Wash I: 15 CV wash buffer I; Wash II: 15 CV wash buffer II (0.03% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 50 mM imidazole); elution with 250 mM imidazole</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>100 kDa cutoff concentrator</td>
      <td>—</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 500 mM NaCl, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.01% (w/v) <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.002% (w/v) <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 25 uM AM10257 + 0.01% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> + 0.002% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Concentrated to 20 mg/mL for crystallization</td>
    </tr>
  </tbody>
</table>
=======
##### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell infection | [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression) infection |  |  | Sf9 cells infected at 2-2.5 x 10^6 cells/mL with high-titer viral stock, MOI 5.0; harvested 48 h post-infection |
| Membrane preparation | Centrifugation and washing |  | 10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl (hypotonic); 10 mM HEPES pH 7.5, 1.0 M NaCl, 10 mM MgCl2, 20 mM KCl (high osmotic) | Membranes lysed by repeated washing and centrifugation; incubated with 20 uM AM10257 and inhibitor cocktail at 4C for 3 h; 1.0 mg/mL iodoacetamide added for 1 h |
| Solubilization | Detergent solubilization |  | 50 mM HEPES pH 7.5, 500 mM NaCl + 0.75% (w/v) [LMNG](/xray-mp-wiki/reagents/detergents/lmng) + 0.15% (w/v) [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Membranes solubilized for 2.5-3 h at 4C; supernatant isolated by ultracentrifugation |
| [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) | [TALON](/xray-mp-wiki/reagents/additives/talon) [IMAC](/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography) | [TALON](/xray-mp-wiki/reagents/additives/talon) IMAC resin | 25 mM HEPES pH 7.5, 500 mM NaCl, 10% (v/v) glycerol, 0.1% (w/v) [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.02% (w/v) [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 30 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole), 20 uM AM10257 + 0.1% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) + 0.02% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Wash I: 15 CV wash buffer I; Wash II: 15 CV wash buffer II (0.03% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 50 mM imidazole); elution with 250 mM imidazole |
| Concentration | 100 kDa cutoff concentrator | — | 25 mM HEPES pH 7.5, 500 mM NaCl, 10% (v/v) glycerol, 0.01% (w/v) [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.002% (w/v) [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 25 uM AM10257 + 0.01% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/) + 0.002% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) | Concentrated to 20 mg/mL for crystallization |

>>>>>>> d0e2c437136bdf2885afc6a99e0a9d4117821696
**Final sample**: CB2-T4L-AM10257 complex at 20 mg/mL

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic Cubic Phase</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/am10257">AM10257</a>-bound CB2-T4L</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>90% (w/v) <a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a> + 10% (w/v) <a href="/xray-mp-wiki/reagents/lipids/cholesterol">Cholesterol</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3 (w/w)</td>
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
      <td>Crystals grown by <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">LCP</a> using syringe mixer; 96-well glass sandwich plates; 50 nL protein-lipid mesophase dispensed per well; data collected at Spring-8 BL32XU; 7 crystals merged; multiple small wedge data collection scheme</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5zty">5ZTY</a> — Chain A (7 TMs, alpha)**

<<<<<<< HEAD
<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFAG</span><span class="topo-inside">APPMKDYMILSGPQKTA</span><span class="topo-membrane">VAVLCTLLGLLSALENVAVLYLILS</span><span class="topo-outside">S</span></span>
<span class="topo-line"><span class="topo-outside">HQLRRKP</span><span class="topo-membrane">SYLFIGSLALADFLASVVFACSFV</span><span class="topo-inside">NFHVFHGVDSKAVFL</span><span class="topo-membrane">LKIGSVTMTFTASV</span></span>
<span class="topo-line"><span class="topo-membrane">GSLLLAAIDRY</span><span class="topo-outside">LCLRYPPSYKALLTR</span><span class="topo-membrane">GRALVLLGIMWVLSALVSYLPLM</span><span class="topo-inside">GWTCCPRPCSE</span></span>
<span class="topo-line"><span class="topo-inside">LFPLIPND</span><span class="topo-membrane">YLLSWLLFIAFLFSGIIYTYGHVL</span><span class="topo-outside">WKAHQHVASNIFEMLRIDEGLRLKIYKD</span></span>
<span class="topo-line"><span class="topo-outside">TEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILR</span></span>
<span class="topo-line"><span class="topo-outside">NAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYN</span></span>
<span class="topo-line"><span class="topo-outside">QTPNRAKRVITTFRTGTWDAYARMRLDVEL</span><span class="topo-membrane">AKTLGLVLAVLLICWFPVLALMAH</span><span class="topo-inside">SLATTL</span></span>
<span class="topo-line"><span class="topo-inside">SDQVKKA</span><span class="topo-membrane">FAFCSMLCLINSMVNPVIYALRS</span><span class="topo-outside">EEIRSSAHHCLAHWKK</span><span class="topo-unknown">CVRGLGEFLEVLFQ</span></span>
<span class="topo-line"><span class="topo-unknown">GPHHHHHHHHHHDYKDDDDK</span></span>
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
      <td>17</td>
      <td>2</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>18</td>
      <td>34</td>
      <td>19</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>59</td>
      <td>36</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>67</td>
      <td>61</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>91</td>
      <td>69</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>106</td>
      <td>93</td>
      <td>107</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>107</td>
      <td>131</td>
      <td>108</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>146</td>
      <td>133</td>
      <td>147</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>169</td>
      <td>148</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>188</td>
      <td>171</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>212</td>
      <td>190</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>221</td>
      <td>214</td>
      <td>222</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>381</td>
      <td>1001</td>
      <td>1160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>390</td>
      <td>235</td>
      <td>243</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>391</td>
      <td>414</td>
      <td>244</td>
      <td>267</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>415</td>
      <td>427</td>
      <td>268</td>
      <td>280</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>450</td>
      <td>281</td>
      <td>303</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>451</td>
      <td>466</td>
      <td>304</td>
      <td>319</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>467</td>
      <td>500</td>
      <td>320</td>
      <td>353</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>
=======
| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) ([LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) |
| Protein sample | [AM12033](/xray-mp-wiki/reagents/ligands/am12033)-bound CB2 |
| Lipid | [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) |
| Protein-to-lipid ratio | not specified |
| Temperature | not specified |
| Growth time | 2 weeks; dehydrated to 40 mm x 20 mm after 2 weeks |
| Notes | Crystals grown by [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase); harvested with micro-mounts (MiTeGen) and flash frozen in liquid nitrogen; data collected at Spring-8 beamline 41XU with Pilatus3 6M detector at 1.0000 A wavelength |

### doi/10.1016##j.cell.2018.12.011

| Parameter | Value |
|---|---|
| Method | [Lipidic Cubic Phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) ([LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) |
| Protein sample | [AM10257](/xray-mp-wiki/reagents/ligands/am10257)-bound CB2-T4L |
| Lipid | 90% (w/v) [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein) + 10% (w/v) [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) |
| Protein-to-lipid ratio | 2:3 (w/w) |
| Temperature | not specified |
| Growth time | not specified |
| Notes | Crystals grown by [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase) using syringe mixer; 96-well glass sandwich plates; 50 nL protein-lipid mesophase dispensed per well; data collected at Spring-8 BL32XU; 7 crystals merged; multiple small wedge data collection scheme |
>>>>>>> d0e2c437136bdf2885afc6a99e0a9d4117821696

</div>

## Biological / Functional Insights

### CB2-Gi complex structure and interaction interface

The CB2-Gi complex reveals extensive contacts mediated through the Gαi subunit.
The primary interaction interface comprises TM3, TM5, TM6, and ICL2 of CB2 and the
α5 helix, αN helix, and αN-β1 loop of Gαi. Two large hydrophobic side chains
L353 and L348 of the Gαi α5 helix are directed toward a hydrophobic pocket formed
by Val212^5.61, Leu243^6.33, Leu247^6.37, Leu239^6.29, and Leu135^3.54 from the
cytosolic ends of TM5, TM6, and TM3 of CB2. The Gi proteins in CB2-Gi complex show
a ~20 degree anticlockwise rotation when aligned with other GPCR-Gi complexes.
No electron density for [GDP](/xray-mp-wiki/reagents/ligands/gdp) is observed, suggesting Gi is nucleotide-free.

### AM12033 binding in CB2

[AM12033](/xray-mp-wiki/reagents/ligands/am12033) adopts an L-shape conformation in the orthosteric binding pocket.
Interactions are mainly hydrophobic and aromatic, involving residues from ECL2,
TM3, TM5, TM6, and TM7. The tricyclic tetrahydrocannabinol system forms pi-pi
interactions with Phe183^ECL2, Phe281^7.35, and Phe94^2.64. The phenolic hydroxyl
at C1 forms a hydrogen bond with Ser285^7.39. The alkyl chain extends into a long
channel forming hydrophobic interactions with TM3, TM5, and TM6 residues. The
agonist-bound CB2 crystal structure shares almost identical binding pose with the
cryo-EM structure.

### CB2 activation mechanism

CB2 activation involves the "toggle switch" residue Trp258^6.48 undergoing major
conformational change, accompanied by a large outward movement of the intracellular
part of TM6 by 11 angstroms (Arg238 as reference) to accommodate the α5 helix from
Gαi. The cytoplasmic portion of TM5 extended and moved outward by about 6 angstroms
(V220 as reference) to form extensive interactions with the α5 helix of Gαi. Unlike
[CB1](/xray-mp-wiki/proteins/cnr1) which uses a "twin toggle switch" (Phe3.36 and Trp6.48), CB2 requires only the
single "toggle switch" Trp6.48 to trigger activation and downstream signaling.

### CB2 activation vs CB1 activation differences

CB2 and [CB1](/xray-mp-wiki/proteins/cnr1) exhibit distinct activation processes. CB1 shows a more complicated
activation involving synergistic conformational change of the "twin toggle switch"
(Phe3.36 and Trp6.48) to unleash large conformational changes. CB2 experiences
only minor conformational changes upon agonist binding, behaving like most class A
GPCRs. The extracellular region of CB2, including the N terminus, undergoes very
minor changes during activation. CB1 displays larger conformational changes when
modulated by agonists, suggesting a "balloon-like plasticity" that facilitates
CB1's ability to respond to diverse ligands.

### Thr3.46 role in Gi coupling

An atypical polar amino acid Thr3.46 exists in both CB2 and [CB1](/xray-mp-wiki/proteins/cnr1), compared to
conserved non-polar residues (I/L/M/V) in 95% of class A GPCRs. T3.46A mutation
disables CB2 and CB1 in coupling to Gi. Upon activation, Tyr7.53 establishes new
contacts with Thr3.46, Leu3.43, and Arg3.50. Asp6.30 in TM6 interrupts its
salt-bridge interaction with Arg3.50, strengthening TM3-TM7 interaction, weakening
TM6 constraint from TM3, and unlocking outward movement of TM6.

### CB2-Gi complex rotation compared to other GPCRs

The Gi proteins in CB2- and CB1-Gi complexes show a ~20 degree anticlockwise
rotation when viewed from intracellular to extracellular direction, compared to
mu-opioid receptor, A1 adenosine, 5HT1B, and M2 Gi complexes. This distinct
orientation may contribute to G protein selectivity differences between [Cannabinoid](/xray-mp-wiki/concepts/cannabinoid)
receptors and other Gi-coupled GPCRs.

### CB1 cholesterol binding as endogenous allosteric modulation

[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) binds to CB1 at a specific site involving Phe155^2.42 and Phe237^4.46.
In the CB1-Gi complex structure, these side chains undergo large conformational
changes and occupy the same position that cholesterol had in agonist-bound crystal
structures. Phe4.46 is unique to CB1 in class A GPCRs. Cholesterol is not observed
in CB2 structures, suggesting CB1-specific allosteric modulation. Pregnenolone, a
cholesterol derivative, may also bind to the same region and act as a CB1 allosteric
modulator.

### CB1 and CB2 G protein coupling diversity

CB2 couples specifically to Gi only, while [CB1](/xray-mp-wiki/proteins/cnr1) can couple to Gi, Gs, and Gq. The
single residue difference in ICL2 (L222 in CB1 and P139 in CB2) may contribute to
this G protein-coupling diversity. L222 in CB1 facilitates its coupling with Gs and
likely Gq as well. The high structural similarity in orthosteric binding pockets between agonist-bound CB2 and CB1 imposes challenges for highly selective agonist design.

### Antagonist-bound CB2 structure reveals binding pocket differences from CB1

The crystal structure of human CB2 bound to the antagonist [AM10257](/xray-mp-wiki/reagents/ligands/am10257) at 2.8 A resolution (PDB 5ZTY) reveals a distinctly different binding pose compared to CB1. The CB2 antagonist-binding pocket (447 A^3) is smaller than the CB1 antagonist-binding pocket (822 A^3) and is more similar in size to the CB1 agonist-binding pocket (384 A^3). The toggle switch residue Trp258^6.48 adopts a relatively rare rotamer that confines helix VI in the inactive state. The unique yin-yang relationship between CB2 and CB1 - where [AM10257](/xray-mp-wiki/reagents/ligands/am10257) is an inverse agonist at CB2 but a partial agonist at CB1 - provides insights for selective [Cannabinoid](/xray-mp-wiki/concepts/cannabinoid) drug design.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/cnr1/">Cannabinoid Receptor 1 (CNR1/CB1)</a> — [CB1](/xray-mp-wiki/proteins/cnr1) shares 44% sequence identity and 68% TM similarity; compared in activation and signaling
- <a href="/xray-mp-wiki/reagents/ligands/am12033/">AM12033</a> — Synthetic [Cannabinoid](/xray-mp-wiki/concepts/cannabinoid) agonist bound in both cryo-EM (6KPF) and crystal (6KPC) structures
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">Lauryl Maltose Neopentyl Glycol (LMNG)</a> — Detergent used for CB2-Gi complex solubilization and purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesterol Hydrogen Succinate (CHS)</a> — [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol) derivative used as stabilizer in CB2-Gi complex purification
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> — N-terminal fusion partner used to improve CB2 expression and stability
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — CB2-[AM12033](/xray-mp-wiki/reagents/ligands/am12033) crystal structure (6KPC) determined by LCP method
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — CB2-Gi-scFv16 complex (6KPF) solved by [Cryo-EM](/xray-mp-wiki/methods/structure-determination/cryo-em) at 2.9 A resolution
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid used in LCP crystallization matrix for CB2-[AM12033](/xray-mp-wiki/reagents/ligands/am12033)
- <a href="/xray-mp-wiki/concepts/cannabinoid">Cannabinoid</a> — Related structural or functional concept
- <a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression">Baculovirus Expression</a> — Expression system used for protein production
