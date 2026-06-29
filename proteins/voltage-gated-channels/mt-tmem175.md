---
title: "MtTMEM175 K+ channel from Marivirga tractuosa"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, channel, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.53683]
verified: false
---

# MtTMEM175 K+ channel from Marivirga tractuosa

## Overview

TMEM175 is a family of non-canonical K⁺ channels found in animals, eubacteria,
and archaea that are essential for lysosomal pH regulation and autophagosome
turnover. Unlike all known K⁺ channels, TMEM175 channels lack a P-loop selectivity
filter. The X-ray crystal structure of MtTMEM175 from Marivirga tractuosa was
determined at 2.4 Å resolution in complex with a novel nanobody-MBP fusion chaperone
('macrobody', Mb₅₁H₀₁). MtTMEM175 assembles as a tetramer with each subunit
containing six transmembrane helices. The structure reveals two K⁺ ion binding
sites: a hydrated K⁺ ion (1K⁺) at the extracellular pore entrance coordinated
by backbone carbonyl oxygens of Leu42, Ser43, and Ser44 in an eightfold square
antiprism geometry, and a second K⁺ ion (2K⁺) deeper in the pore. A highly
conserved threonine layer (Thr38 in MtTMEM175; Thr49/Thr274 in human TMEM175)
conveys basal K⁺ selectivity, with an additional serine layer (Ser45 in human
TMEM175) contributing to the higher selectivity of the human channel (PK/PNa
~10-35 vs ~4 in bacterial channels). A bulky hydrophobic gate formed by Leu35
occludes the pore in the closed state. Channel opening is proposed to involve
iris-like rotation of helix 1, simultaneously relocating the gate and exposing
the selectivity filter residues to the pore lumen. The human TMEM175 channel
is a Parkinson disease risk gene.


## Publications

### doi/10.7554##eLife.53683

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hd8">6HD8</a></td>
      <td>2.4</td>
      <td>P2₁2₁2₁</td>
      <td>MtTMEM175 tetramer in complex with macrobody Mb₅₁H₀₁ (nanobody fused to N-terminally truncated MBP)</td>
      <td>K⁺ ions (1K⁺ hydrated at extracellular entrance, 2K⁺ in pore)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hd9">6HD9</a></td>
      <td>2.4</td>
      <td>P2₁2₁2₁</td>
      <td>MtTMEM175 tetramer with Rb⁺ soak</td>
      <td>Rb⁺</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hda">6HDA</a></td>
      <td>2.4</td>
      <td>P2₁2₁2₁</td>
      <td>MtTMEM175 tetramer with Cs⁺ soak</td>
      <td>Cs⁺</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hdb">6HDB</a></td>
      <td>2.4</td>
      <td>P2₁2₁2₁</td>
      <td>MtTMEM175 tetramer with Zn²⁺ soak</td>
      <td>Zn²⁺</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6hdc">6HDC</a></td>
      <td>2.4</td>
      <td>P2₁2₁2₁</td>
      <td>MtTMEM175 T38A mutant in complex with Mb₅₁H₀₁</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6swr">6SWR</a></td>
      <td>2.4</td>
      <td>P2₁2₁2₁</td>
      <td>MtTMEM175 tetramer, additional dataset</td>
      <td>K⁺</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli MC1061
- **Construct**: MtTMEM175 (UniProt E4TN31) from Marivirga tractuosa (DSM 4126) cloned into pBXC3H with C-terminal deca-histidine tag and HRV 3C protease cleavage site. For HEK expression, cloned into pcDXC3MS with C-terminal SBP tag.

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
      <td>Cell lysis and membrane preparation</td>
      <td>Microfluidizer</td>
      <td>--</td>
      <td>150 mM KCl, 10 mM Hepes-NaOH pH 7.6, 10% glycerol + --</td>
      <td>Membranes pelleted by ultracentrifugation</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>150 mM KCl, 10 mM Hepes-NaOH pH 7.6, 10% glycerol + 1% (w/v) n-dodecyl-β-D-maltopyranoside (DDM)</td>
      <td>Solubilized for 1 hr at 4°C with protease inhibitors. Insoluble material removed by centrifugation at 42,000 rpm (45 Ti rotor)</td>
    </tr>
    <tr>
      <td>Streptactin affinity</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td>Strep-Tactin Superflow high capacity</td>
      <td>150 mM KCl, 10 mM Hepes-NaOH pH 7.6, 10% glycerol, 50 µg/mL E. coli polar lipids, 0.03% DDM + 0.03% DDM</td>
      <td>Eluted with wash buffer containing 5 mM d-desthiobiotin. Tag cleaved with HRV 3C protease</td>
    </tr>
    <tr>
      <td>Complex formation and SEC</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-Exclusion Chromatography</a></td>
      <td>Superdex 200 10/300</td>
      <td>150 mM KCl, 5 mM Hepes-NaOH pH 7.6, 2.5 mM maltose, 0.03% DDM + 0.03% DDM</td>
      <td>MtTMEM175 mixed with Mb₅₁H₀₁ at 2.2-2.5:1 molar ratio. Peak fractions concentrated to 8-16 mg/mL for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>MtTMEM175-Mb₅₁H₀₁ complex at 8-16 mg/mL, mixed with E. coli polar lipids (100 µg/mL) and DM (0.3% final)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM Tris-HCl pH 8.5, 150 mM NaCl, 150 mM MgCl₂, 28-30% PEG400</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>14 days (plus 3-4 hr dehydration with 36% PEG400)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryo-protected with mother liquor at 36% PEG400, flash-frozen in liquid propane or liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Best crystals obtained after dehydration. Some crystals soaked with 5 mM KPtCl₄ followed by back-soaking for phasing. Crystals soaked with Cs⁺, Rb⁺ by replacing 150 mM KCl in cryo-protecting solution with 150 mM CsCl or RbCl. Zn²⁺ soaks with 0.5-2.5 mM ZnCl₂.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hd8">6HD8</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hd8">6HD8</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTRI</span><span class="topo-membrane">ETFSDAVFALAITLLVLSSTIP</span><span class="topo-outside">ETFEDLWAS</span><span class="topo-membrane">MRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHY</span><span class="topo-inside">IFFLKYGLQDK</span><span class="topo-membrane">VTILLNTILLFVLLVYVYPLKFLARFLSEI</span></span>
<span class="topo-line"><span class="topo-membrane">YG</span><span class="topo-outside">GIFGIIETDLSRFGEYSHQNLK</span><span class="topo-membrane">LLMVNYGLGAFAIFLVFSLM</span><span class="topo-inside">YWRAYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKSSII</span><span class="topo-membrane">ANLLMCSVPLLSLIITLIDP</span><span class="topo-outside">WGNFR</span><span class="topo-membrane">TTILSGFLYFLYVPIMIVFGRIT</span><span class="topo-inside">SK</span></span>
<span class="topo-line"><span class="topo-inside">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>26</td>
      <td>9</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>48</td>
      <td>26</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>57</td>
      <td>48</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>90</td>
      <td>79</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>122</td>
      <td>90</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>144</td>
      <td>122</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>164</td>
      <td>144</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>190</td>
      <td>164</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>210</td>
      <td>190</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>215</td>
      <td>210</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>238</td>
      <td>215</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>241</td>
      <td>238</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hd8">6HD8</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hd8">6HD8</a> — Chain E (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTRI</span><span class="topo-membrane">ETFSDAVFALAITLLVLSSTIP</span><span class="topo-outside">ETFEDLWAS</span><span class="topo-membrane">MRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHY</span><span class="topo-inside">IFFLKYGLQDK</span><span class="topo-membrane">VTILLNTILLFVLLVYVYPLKFLARFLSEI</span></span>
<span class="topo-line"><span class="topo-membrane">YG</span><span class="topo-outside">GIFGIIETDLSRFGEYSHQNLK</span><span class="topo-membrane">LLMVNYGLGAFAIFLVFSLM</span><span class="topo-inside">YWRAYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKSSII</span><span class="topo-membrane">ANLLMCSVPLLSLIITLIDP</span><span class="topo-outside">WGNFR</span><span class="topo-membrane">TTILSGFLYFLYVPIMIVFGRIT</span><span class="topo-inside">SK</span></span>
<span class="topo-line"><span class="topo-inside">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>26</td>
      <td>9</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>48</td>
      <td>26</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>57</td>
      <td>48</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>90</td>
      <td>79</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>122</td>
      <td>90</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>144</td>
      <td>122</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>164</td>
      <td>144</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>190</td>
      <td>164</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>210</td>
      <td>190</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>215</td>
      <td>210</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>238</td>
      <td>215</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>241</td>
      <td>238</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hd8">6HD8</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hd8">6HD8</a> — Chain G (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTRI</span><span class="topo-membrane">ETFSDAVFALAITLLVLSSTIP</span><span class="topo-outside">ETFEDLWAS</span><span class="topo-membrane">MRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHY</span><span class="topo-inside">IFFLKYGLQDK</span><span class="topo-membrane">VTILLNTILLFVLLVYVYPLKFLARFLSEI</span></span>
<span class="topo-line"><span class="topo-membrane">YG</span><span class="topo-outside">GIFGIIETDLSRFGEYSHQNLK</span><span class="topo-membrane">LLMVNYGLGAFAIFLVFSLM</span><span class="topo-inside">YWRAYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKSSII</span><span class="topo-membrane">ANLLMCSVPLLSLIITLIDP</span><span class="topo-outside">WGNFR</span><span class="topo-membrane">TTILSGFLYFLYVPIMIVFGRIT</span><span class="topo-inside">SK</span></span>
<span class="topo-line"><span class="topo-inside">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>26</td>
      <td>9</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>48</td>
      <td>26</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>57</td>
      <td>48</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>90</td>
      <td>79</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>122</td>
      <td>90</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>144</td>
      <td>122</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>164</td>
      <td>144</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>190</td>
      <td>164</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>210</td>
      <td>190</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>215</td>
      <td>210</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>238</td>
      <td>215</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>241</td>
      <td>238</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hd8">6HD8</a> — Chain H (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hd8">6HD8</a> — Chain I (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTRI</span><span class="topo-membrane">ETFSDAVFALAITLLVLSSTIP</span><span class="topo-outside">ETFEDLWAS</span><span class="topo-membrane">MRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHY</span><span class="topo-inside">IFFLKYGLQDK</span><span class="topo-membrane">VTILLNTILLFVLLVYVYPLKFLARFLSEI</span></span>
<span class="topo-line"><span class="topo-membrane">YG</span><span class="topo-outside">GIFGIIETDLSRFGEYSHQNLK</span><span class="topo-membrane">LLMVNYGLGAFAIFLVFSLM</span><span class="topo-inside">YWRAYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKSSII</span><span class="topo-membrane">ANLLMCSVPLLSLIITLIDP</span><span class="topo-outside">WGNFR</span><span class="topo-membrane">TTILSGFLYFLYVPIMIVFGRIT</span><span class="topo-inside">SK</span></span>
<span class="topo-line"><span class="topo-inside">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>26</td>
      <td>9</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>48</td>
      <td>26</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>57</td>
      <td>48</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>90</td>
      <td>79</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>122</td>
      <td>90</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>144</td>
      <td>122</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>164</td>
      <td>144</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>190</td>
      <td>164</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>210</td>
      <td>190</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>215</td>
      <td>210</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>238</td>
      <td>215</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>241</td>
      <td>238</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hd9">6HD9</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hd9">6HD9</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTR</span><span class="topo-membrane">IETFSDAVFALAITLLVLSS</span><span class="topo-outside">TIPETFEDLWASMRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHY</span><span class="topo-inside">IFFLKYGLQDKVTI</span><span class="topo-membrane">LLNTILLFVLLVYVYPLKFLAR</span><span class="topo-outside">FLSEI</span></span>
<span class="topo-line"><span class="topo-outside">YGGIFGIIETDLSRFGEYSHQNLK</span><span class="topo-membrane">LLMVNYGLGAFAIFLVFSLM</span><span class="topo-inside">YWRAYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKSSII</span><span class="topo-membrane">ANLLMCSVPLLSLIITLIDPW</span><span class="topo-outside">GNFR</span><span class="topo-membrane">TTILSGFLYFLYVPIMIVFGRIT</span><span class="topo-inside">SK</span></span>
<span class="topo-line"><span class="topo-inside">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>25</td>
      <td>9</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>45</td>
      <td>25</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>60</td>
      <td>45</td>
      <td>59</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>79</td>
      <td>60</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>93</td>
      <td>79</td>
      <td>92</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>115</td>
      <td>93</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>144</td>
      <td>115</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>164</td>
      <td>144</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>190</td>
      <td>164</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>211</td>
      <td>190</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>212</td>
      <td>215</td>
      <td>211</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>238</td>
      <td>215</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>241</td>
      <td>238</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hda">6HDA</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hda">6HDA</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTR</span><span class="topo-membrane">IETFSDAVFALAITLLVLSSTIP</span><span class="topo-outside">ETFEDLWAS</span><span class="topo-membrane">MRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHY</span><span class="topo-inside">IFFLKYGLQDK</span><span class="topo-membrane">VTILLNTILLFVLLVYVYPLKFLARFLSEI</span></span>
<span class="topo-line"><span class="topo-membrane">YG</span><span class="topo-outside">GIFGIIETDLSRFGEYSHQNLK</span><span class="topo-membrane">LLMVNYGLGAFAIFLVFSLM</span><span class="topo-inside">YWRAYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKSSI</span><span class="topo-membrane">IANLLMCSVPLLSLIITLIDP</span><span class="topo-outside">WGNFR</span><span class="topo-membrane">TTILSGFLYFLYVPIMIVFGRIT</span><span class="topo-inside">SK</span></span>
<span class="topo-line"><span class="topo-inside">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>25</td>
      <td>9</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>48</td>
      <td>25</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>57</td>
      <td>48</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>90</td>
      <td>79</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>122</td>
      <td>90</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>144</td>
      <td>122</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>164</td>
      <td>144</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>164</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>210</td>
      <td>189</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>215</td>
      <td>210</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>238</td>
      <td>215</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>241</td>
      <td>238</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hda">6HDA</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hda">6HDA</a> — Chain E (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTR</span><span class="topo-membrane">IETFSDAVFALAITLLVLSSTIP</span><span class="topo-outside">ETFEDLWAS</span><span class="topo-membrane">MRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHY</span><span class="topo-inside">IFFLKYGLQDK</span><span class="topo-membrane">VTILLNTILLFVLLVYVYPLKFLARFLSEI</span></span>
<span class="topo-line"><span class="topo-membrane">YG</span><span class="topo-outside">GIFGIIETDLSRFGEYSHQNLK</span><span class="topo-membrane">LLMVNYGLGAFAIFLVFSLM</span><span class="topo-inside">YWRAYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKSSI</span><span class="topo-membrane">IANLLMCSVPLLSLIITLIDP</span><span class="topo-outside">WGNFR</span><span class="topo-membrane">TTILSGFLYFLYVPIMIVFGRIT</span><span class="topo-inside">SK</span></span>
<span class="topo-line"><span class="topo-inside">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>25</td>
      <td>9</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>48</td>
      <td>25</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>57</td>
      <td>48</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>90</td>
      <td>79</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>122</td>
      <td>90</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>144</td>
      <td>122</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>164</td>
      <td>144</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>164</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>210</td>
      <td>189</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>215</td>
      <td>210</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>238</td>
      <td>215</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>241</td>
      <td>238</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hda">6HDA</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hda">6HDA</a> — Chain G (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTR</span><span class="topo-membrane">IETFSDAVFALAITLLVLSSTIP</span><span class="topo-outside">ETFEDLWAS</span><span class="topo-membrane">MRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHY</span><span class="topo-inside">IFFLKYGLQDK</span><span class="topo-membrane">VTILLNTILLFVLLVYVYPLKFLARFLSEI</span></span>
<span class="topo-line"><span class="topo-membrane">YG</span><span class="topo-outside">GIFGIIETDLSRFGEYSHQNLK</span><span class="topo-membrane">LLMVNYGLGAFAIFLVFSLM</span><span class="topo-inside">YWRAYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKSSI</span><span class="topo-membrane">IANLLMCSVPLLSLIITLIDP</span><span class="topo-outside">WGNFR</span><span class="topo-membrane">TTILSGFLYFLYVPIMIVFGRIT</span><span class="topo-inside">SK</span></span>
<span class="topo-line"><span class="topo-inside">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>25</td>
      <td>9</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>48</td>
      <td>25</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>57</td>
      <td>48</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>90</td>
      <td>79</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>122</td>
      <td>90</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>144</td>
      <td>122</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>164</td>
      <td>144</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>164</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>210</td>
      <td>189</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>215</td>
      <td>210</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>238</td>
      <td>215</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>241</td>
      <td>238</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hda">6HDA</a> — Chain H (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hda">6HDA</a> — Chain I (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTR</span><span class="topo-membrane">IETFSDAVFALAITLLVLSSTIP</span><span class="topo-outside">ETFEDLWAS</span><span class="topo-membrane">MRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHY</span><span class="topo-inside">IFFLKYGLQDK</span><span class="topo-membrane">VTILLNTILLFVLLVYVYPLKFLARFLSEI</span></span>
<span class="topo-line"><span class="topo-membrane">YG</span><span class="topo-outside">GIFGIIETDLSRFGEYSHQNLK</span><span class="topo-membrane">LLMVNYGLGAFAIFLVFSLM</span><span class="topo-inside">YWRAYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKSSI</span><span class="topo-membrane">IANLLMCSVPLLSLIITLIDP</span><span class="topo-outside">WGNFR</span><span class="topo-membrane">TTILSGFLYFLYVPIMIVFGRIT</span><span class="topo-inside">SK</span></span>
<span class="topo-line"><span class="topo-inside">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>25</td>
      <td>9</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>48</td>
      <td>25</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>57</td>
      <td>48</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>90</td>
      <td>79</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>122</td>
      <td>90</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>144</td>
      <td>122</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>164</td>
      <td>144</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>164</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>210</td>
      <td>189</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>215</td>
      <td>210</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>238</td>
      <td>215</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>241</td>
      <td>238</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hdb">6HDB</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hdb">6HDB</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTR</span><span class="topo-membrane">IETFSDAVFALAITLLVLSS</span><span class="topo-outside">TIPETFEDLWASMRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHY</span><span class="topo-inside">IFFLKYGLQDKVTI</span><span class="topo-membrane">LLNTILLFVLLVYVYPLKFLAR</span><span class="topo-outside">FLSEI</span></span>
<span class="topo-line"><span class="topo-outside">YGGIFGIIETDLSRFGEYSHQNLK</span><span class="topo-membrane">LLMVNYGLGAFAIFLVFSLM</span><span class="topo-inside">YWRAYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKSSII</span><span class="topo-membrane">ANLLMCSVPLLSLIITLIDP</span><span class="topo-outside">WGNFRT</span><span class="topo-membrane">TILSGFLYFLYVPIMIVFGRIT</span><span class="topo-inside">SK</span></span>
<span class="topo-line"><span class="topo-inside">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>25</td>
      <td>9</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>45</td>
      <td>25</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>60</td>
      <td>45</td>
      <td>59</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>79</td>
      <td>60</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>93</td>
      <td>79</td>
      <td>92</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>115</td>
      <td>93</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>144</td>
      <td>115</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>164</td>
      <td>144</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>190</td>
      <td>164</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>210</td>
      <td>190</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>216</td>
      <td>210</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>238</td>
      <td>216</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>241</td>
      <td>238</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hdb">6HDB</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hdb">6HDB</a> — Chain E (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTR</span><span class="topo-membrane">IETFSDAVFALAITLLVLSSTIP</span><span class="topo-outside">ETFEDLWAS</span><span class="topo-membrane">MRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHY</span><span class="topo-inside">IFFLKYGLQD</span><span class="topo-membrane">KVTILLNTILLFVLLVYVYPLKFLARFLSEI</span></span>
<span class="topo-line"><span class="topo-membrane">YG</span><span class="topo-outside">GIFGIIETDLSRFGEYSHQNLKLL</span><span class="topo-membrane">MVNYGLGAFAIFLVFSLMYWR</span><span class="topo-inside">AYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKSS</span><span class="topo-membrane">IIANLLMCSVPLLSLIITLI</span><span class="topo-outside">DPWGNFRT</span><span class="topo-membrane">TILSGFLYFLYVPIMIVFGRITSK</span></span>
<span class="topo-line"><span class="topo-membrane">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>25</td>
      <td>9</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>48</td>
      <td>25</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>57</td>
      <td>48</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>89</td>
      <td>79</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>122</td>
      <td>89</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>146</td>
      <td>122</td>
      <td>145</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>167</td>
      <td>146</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>188</td>
      <td>167</td>
      <td>187</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>189</td>
      <td>208</td>
      <td>188</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>216</td>
      <td>208</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>241</td>
      <td>216</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hdb">6HDB</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hdb">6HDB</a> — Chain G (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTR</span><span class="topo-membrane">IETFSDAVFALAITLLVLSS</span><span class="topo-outside">TIPETFEDLWASMRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHYIFF</span><span class="topo-inside">LKYGLQDK</span><span class="topo-membrane">VTILLNTILLFVLLVYVYPLK</span><span class="topo-outside">FLARFLSEI</span></span>
<span class="topo-line"><span class="topo-outside">YGGIFGIIETDLSRFGEYSHQNLKLLM</span><span class="topo-membrane">VNYGLGAFAIFLVFSLMYWR</span><span class="topo-inside">AYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTK</span><span class="topo-membrane">SSIIANLLMCSVPLLSLII</span><span class="topo-outside">TLIDPWGNFRTTILS</span><span class="topo-membrane">GFLYFLYVPIMIVFGRITSK</span></span>
<span class="topo-line"><span class="topo-membrane">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>25</td>
      <td>9</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>45</td>
      <td>25</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>60</td>
      <td>45</td>
      <td>59</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>82</td>
      <td>60</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>90</td>
      <td>82</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>111</td>
      <td>90</td>
      <td>110</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>147</td>
      <td>111</td>
      <td>146</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>148</td>
      <td>167</td>
      <td>147</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>168</td>
      <td>186</td>
      <td>167</td>
      <td>185</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>187</td>
      <td>205</td>
      <td>186</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>220</td>
      <td>205</td>
      <td>219</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>221</td>
      <td>241</td>
      <td>220</td>
      <td>240</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hdb">6HDB</a> — Chain H (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hdb">6HDB</a> — Chain I (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTR</span><span class="topo-membrane">IETFSDAVFALAITLLVLSSTI</span><span class="topo-outside">PETFEDLWAS</span><span class="topo-membrane">MRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQH</span><span class="topo-inside">YIFFLKYGLQDKVTI</span><span class="topo-membrane">LLNTILLFVLLVYVYPLKFLARFLSEI</span></span>
<span class="topo-line"><span class="topo-membrane">YG</span><span class="topo-outside">GIFGIIETDLSRFGEYSHQN</span><span class="topo-membrane">LKLLMVNYGLGAFAIFLVFSL</span><span class="topo-inside">MYWRAYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKSSIIAN</span><span class="topo-membrane">LLMCSVPLLSLIITLIDPWGN</span><span class="topo-unknown">F</span><span class="topo-membrane">RTTILSGFLYFLYVPIMIVF</span><span class="topo-inside">GRITSK</span></span>
<span class="topo-line"><span class="topo-inside">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>25</td>
      <td>9</td>
      <td>24</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>47</td>
      <td>25</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>57</td>
      <td>47</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>78</td>
      <td>57</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>93</td>
      <td>78</td>
      <td>92</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>122</td>
      <td>93</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>142</td>
      <td>122</td>
      <td>141</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>163</td>
      <td>142</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>192</td>
      <td>163</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>213</td>
      <td>192</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>215</td>
      <td>234</td>
      <td>214</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>241</td>
      <td>234</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hdc">6HDC</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hdc">6HDC</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTRI</span><span class="topo-membrane">ETFSDAVFALAIALLVLSSTIP</span><span class="topo-outside">ETFEDLWAS</span><span class="topo-membrane">MRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHY</span><span class="topo-inside">IFFLKYGLQDK</span><span class="topo-membrane">VTILLNTILLFVLLVYVYPLKFLARFLSEI</span></span>
<span class="topo-line"><span class="topo-membrane">YG</span><span class="topo-outside">GIFGIIETDLSRFGEYSHQNLK</span><span class="topo-membrane">LLMVNYGLGAFAIFLVFSLM</span><span class="topo-inside">YWRAYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKSSI</span><span class="topo-membrane">IANLLMCSVPLLSLIITLIDP</span><span class="topo-outside">WGNFR</span><span class="topo-membrane">TTILSGFLYFLYVPIMIVFGRIT</span><span class="topo-inside">SK</span></span>
<span class="topo-line"><span class="topo-inside">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>26</td>
      <td>9</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>48</td>
      <td>26</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>57</td>
      <td>48</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>90</td>
      <td>79</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>122</td>
      <td>90</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>144</td>
      <td>122</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>164</td>
      <td>144</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>164</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>210</td>
      <td>189</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>215</td>
      <td>210</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>238</td>
      <td>215</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>241</td>
      <td>238</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hdc">6HDC</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hdc">6HDC</a> — Chain E (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTRI</span><span class="topo-membrane">ETFSDAVFALAIALLVLSSTIP</span><span class="topo-outside">ETFEDLWAS</span><span class="topo-membrane">MRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHY</span><span class="topo-inside">IFFLKYGLQDK</span><span class="topo-membrane">VTILLNTILLFVLLVYVYPLKFLARFLSEI</span></span>
<span class="topo-line"><span class="topo-membrane">YG</span><span class="topo-outside">GIFGIIETDLSRFGEYSHQNLK</span><span class="topo-membrane">LLMVNYGLGAFAIFLVFSLM</span><span class="topo-inside">YWRAYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKSSI</span><span class="topo-membrane">IANLLMCSVPLLSLIITLIDP</span><span class="topo-outside">WGNFR</span><span class="topo-membrane">TTILSGFLYFLYVPIMIVFGRIT</span><span class="topo-inside">SK</span></span>
<span class="topo-line"><span class="topo-inside">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>26</td>
      <td>9</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>48</td>
      <td>26</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>57</td>
      <td>48</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>90</td>
      <td>79</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>122</td>
      <td>90</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>144</td>
      <td>122</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>164</td>
      <td>144</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>164</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>210</td>
      <td>189</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>215</td>
      <td>210</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>238</td>
      <td>215</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>241</td>
      <td>238</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hdc">6HDC</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hdc">6HDC</a> — Chain G (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTRI</span><span class="topo-membrane">ETFSDAVFALAIALLVLSSTIP</span><span class="topo-outside">ETFEDLWAS</span><span class="topo-membrane">MRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHY</span><span class="topo-inside">IFFLKYGLQDK</span><span class="topo-membrane">VTILLNTILLFVLLVYVYPLKFLARFLSEI</span></span>
<span class="topo-line"><span class="topo-membrane">YG</span><span class="topo-outside">GIFGIIETDLSRFGEYSHQNLK</span><span class="topo-membrane">LLMVNYGLGAFAIFLVFSLM</span><span class="topo-inside">YWRAYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKSSI</span><span class="topo-membrane">IANLLMCSVPLLSLIITLIDP</span><span class="topo-outside">WGNFR</span><span class="topo-membrane">TTILSGFLYFLYVPIMIVFGRIT</span><span class="topo-inside">SK</span></span>
<span class="topo-line"><span class="topo-inside">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>26</td>
      <td>9</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>48</td>
      <td>26</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>57</td>
      <td>48</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>90</td>
      <td>79</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>122</td>
      <td>90</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>144</td>
      <td>122</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>164</td>
      <td>144</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>164</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>210</td>
      <td>189</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>215</td>
      <td>210</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>238</td>
      <td>215</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>241</td>
      <td>238</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hdc">6HDC</a> — Chain H (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPS</span><span class="topo-inside">QRQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>282</td>
      <td>4</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6hdc">6HDC</a> — Chain I (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQTRI</span><span class="topo-membrane">ETFSDAVFALAIALLVLSSTIP</span><span class="topo-outside">ETFEDLWAS</span><span class="topo-membrane">MRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHY</span><span class="topo-inside">IFFLKYGLQDK</span><span class="topo-membrane">VTILLNTILLFVLLVYVYPLKFLARFLSEI</span></span>
<span class="topo-line"><span class="topo-membrane">YG</span><span class="topo-outside">GIFGIIETDLSRFGEYSHQNLK</span><span class="topo-membrane">LLMVNYGLGAFAIFLVFSLM</span><span class="topo-inside">YWRAYKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKSSI</span><span class="topo-membrane">IANLLMCSVPLLSLIITLIDP</span><span class="topo-outside">WGNFR</span><span class="topo-membrane">TTILSGFLYFLYVPIMIVFGRIT</span><span class="topo-inside">SK</span></span>
<span class="topo-line"><span class="topo-inside">K</span><span class="topo-unknown">SRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>26</td>
      <td>9</td>
      <td>25</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>48</td>
      <td>26</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>57</td>
      <td>48</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>79</td>
      <td>57</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>90</td>
      <td>79</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>122</td>
      <td>90</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>144</td>
      <td>122</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>164</td>
      <td>144</td>
      <td>163</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>164</td>
      <td>188</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>210</td>
      <td>189</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>215</td>
      <td>210</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>238</td>
      <td>215</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>241</td>
      <td>238</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>255</td>
      <td>241</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6swr">6SWR</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GPSQ</span><span class="topo-inside">RQLVESGGGLVQPGGSLRLSCAASGSILYFNRMGWYRQAPGKQRELVAAITSGDST</span></span>
<span class="topo-line"><span class="topo-inside">NYADPVKGRFTISRDNAKNTVYLQMNSLKPEDTAVYYCNAKEKGWSFSLYDYWGQGTPVT</span></span>
<span class="topo-line"><span class="topo-inside">VVKLVIWINGDKGYNGLAEVGKKFEKDTGIKVTVEHPDKLEEKFPQVAATGDGPDIIFWA</span></span>
<span class="topo-line"><span class="topo-inside">HDRFGGYAQSGLLAEITPDKAFQDKLYPFTWDAVRYNGKLIAYPIAVEALSLIYNKDLLP</span></span>
<span class="topo-line"><span class="topo-inside">NPPKTWEEIPALDKELKAKGKSALMFNLQEPYFTWPLIAADG</span><span class="topo-unknown">GYAFKYENGKYDIKDVGV</span></span>
<span class="topo-line"><span class="topo-unknown">D</span><span class="topo-inside">NAGAKAGLTFLVDLIKNKHMNADTDYSIAEAAFNKGETAMTINGPWAWSNIDTSKVNYG</span></span>
<span class="topo-line"><span class="topo-inside">VTVLPTFKGQPSKPFVGVLSAGINAASPNKELAKEFLENYLLTDEGLEAVNKDKPLGAVA</span></span>
<span class="topo-line"><span class="topo-inside">LKSYEEELAKDPRIAATMENAQKGEIMPNIPQMSAFWYAVRTAVINAASGRQTVDEALKD</span></span>
<span class="topo-line"><span class="topo-inside">AQT</span><span class="topo-unknown">PGA</span></span>
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
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>282</td>
      <td>5</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>301</td>
      <td>283</td>
      <td>301</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>302</td>
      <td>483</td>
      <td>302</td>
      <td>483</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>484</td>
      <td>486</td>
      <td>484</td>
      <td>486</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6swr">6SWR</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MSRKVFETV</span><span class="topo-inside">VGLNPNFSFRGKQQ</span><span class="topo-membrane">TRIETFSDAVFALAIALLVLSSTI</span><span class="topo-outside">PETFEDLWAS</span><span class="topo-membrane">MRD</span></span>
<span class="topo-line"><span class="topo-membrane">VIPFAICVALIIVIWYQHYIFFL</span><span class="topo-inside">KYGL</span><span class="topo-membrane">QDKVTILLNTILLFVLLVYVYPLKFLARFLS</span><span class="topo-outside">EI</span></span>
<span class="topo-line"><span class="topo-outside">YGGIFGIIETDLSRFGEYSHQNLK</span><span class="topo-membrane">LLMVNYGLGAFAIFLVFSLMYWRA</span><span class="topo-inside">YKMKSLLDLNSY</span></span>
<span class="topo-line"><span class="topo-inside">EIFDTKS</span><span class="topo-membrane">SIIANLLMCSVPLLSLIITLIDP</span><span class="topo-outside">WGNFR</span><span class="topo-membrane">TTILSGFLYFLYVPIMIVFGRI</span><span class="topo-inside">TS</span><span class="topo-unknown">K</span></span>
<span class="topo-line"><span class="topo-unknown">KSRRLLQDALEVLFQ</span></span>
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
      <td>9</td>
      <td>0</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>23</td>
      <td>9</td>
      <td>22</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>47</td>
      <td>23</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>57</td>
      <td>47</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>83</td>
      <td>57</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>87</td>
      <td>83</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>118</td>
      <td>87</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>119</td>
      <td>144</td>
      <td>118</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>168</td>
      <td>144</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>169</td>
      <td>187</td>
      <td>168</td>
      <td>186</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>210</td>
      <td>187</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>215</td>
      <td>210</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>237</td>
      <td>215</td>
      <td>236</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>239</td>
      <td>237</td>
      <td>238</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>240</td>
      <td>255</td>
      <td>239</td>
      <td>254</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Non-canonical K+ selectivity without P-loop

MtTMEM175 achieves K⁺ selectivity without a canonical P-loop selectivity filter — a hallmark of all other known K⁺ channels. Instead, a conserved threonine layer (Thr38 in MtTMEM175, Thr49/Thr274 in hTMEM175) provides selectivity through side-chain hydroxyl groups that are exposed to the pore lumen only in the open (conductive) conformation.

### Two-tier selectivity in human TMEM175

The human TMEM175 channel achieves higher K⁺ selectivity (PK/PNa ~10-35) than bacterial homologs (PK/PNa ~2-5) through an additional serine layer (Ser45 in hTMEM175 first repeat) that works in conjunction with the conserved threonine layer. Mutating Ser45 to alanine reduces selectivity to bacterial levels and abolishes Zn²⁺ and 4-AP sensitivity.

### Hydrophobic gate and iris-like opening mechanism

The pore is occluded by Leu35, a bulky hydrophobic residue that forms a physical gate in the closed state. Channel opening is proposed to involve an 8-15° clockwise rotation of helix 1 (viewed from intracellular), which simultaneously swings the bulky gate residues out of the pathway and exposes the conserved threonine selectivity layer to the pore lumen.

### Macrobody chaperone for crystallization

The structure was solved using a novel 'macrobody' chaperone — a nanobody fused to a C-terminal N-terminally truncated maltose-binding protein (MBP) — which greatly improved crystal diffraction from ~10 Å to 2.4 Å. This chaperone scaffold may have broad applications in membrane protein crystallography.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KcsA K+ channel</a> — Canonical P-loop K+ channel with different selectivity filter architecture
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/nak-channel/">NaK channel</a> — Non-selective cation channel sharing tetrameric architecture
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating access mechanism</a> — Channel gating mechanism vs transporter alternating access
