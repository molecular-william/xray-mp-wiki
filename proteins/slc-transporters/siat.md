---
title: "SiaT Sialic Acid Transporter from Proteus mirabilis"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1038##s41467-018-04045-7]
verified: false
---

# SiaT Sialic Acid Transporter from Proteus mirabilis

## Overview

SiaT is a secondary active sialic acid transporter from the uropathogen Proteus mirabilis, belonging to the [Sodium Solute Symporter (SSS) Family](/xray-mp-wiki/concepts/transport-mechanisms/sss-family/). It uses Na+ electrochemical gradients to drive the uptake of extracellular sialic acids, which bacteria utilise as an energy source or for molecular mimicry. The substrate-bound outward-open structure of SiaT was determined at 1.95 Å resolution, revealing the LeuT-fold with 14 transmembrane helices and a central substrate-binding site for N-acetylneuraminic acid (Neu5Ac) coordinated by Thr58, Thr63, Ser60, Gln82, and Arg135. A distinctive feature is the identification of two Na+ binding sites: the conserved Na2 site and a newly identified Na3 site positioned close to Na2 but not in contact with the substrate. The Na3 site is conserved in ~19.6% of SSS family members, including hSGLT1 (which transports 2 Na+ per substrate) but not in [VSGLT](/xray-mp-wiki/proteins/slc-transporters/vsglt/) or hSGLT2 (which transport 1 Na+). Molecular dynamics simulations demonstrate that Na3 binding allosterically stabilizes the substrate and pre-organises the binding site. This structure provides the first high-resolution view of a bacterial sialic acid SSS transporter and reveals how stoichiometric variation in Na+ coupling arises within the SSS family.

## Publications

### doi/10.1038##s41467-018-04045-7

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5nv9">5NV9</a></td>
      <td>1.95</td>
      <td>C2</td>
      <td>Full-length SiaT from Proteus mirabilis with C-terminal His6 tag</td>
      <td>Neu5Ac (N-acetylneuraminic acid), 2 Na+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5nva">5NVA</a></td>
      <td>2.26</td>
      <td>P22_12_1</td>
      <td>Full-length SiaT from Proteus mirabilis with C-terminal His6 tag</td>
      <td>Neu5Ac, 2 Na+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli Lemo21(DE3) (NEB)
- **Construct**: Full-length SiaT from Proteus mirabilis (strain HI4320) with C-terminal His6 tag
- **Notes**: Grown in Terrific Broth with [Kanamycin](/xray-mp-wiki/reagents/additives/kanamycin/) (50 µg/mL), [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/) (34 µg/mL), L-rhamnose (250 µM). Induced with 0.4 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at 25°C overnight with shaking at 200 rpm. SeMet protein produced using PASM-5052 autoinduction media.

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
      <td>1. Cell lysis</td>
      <td>Emulsiflex-C3 homogenizer at 20,000 psi</td>
      <td>—</td>
      <td>PBS supplemented with cOmplete EDTA-free protease inhibitors, lysozyme (0.5 mg/mL), DNaseI (5 µg/mL), MgCl2 (2 mM)</td>
      <td>Cell debris removed at 24,000×g</td>
    </tr>
    <tr>
      <td>2. Membrane preparation</td>
      <td>Ultracentrifugation at 235,000×g for 2 h</td>
      <td>—</td>
      <td></td>
      <td>Membranes stored at -80°C until use</td>
    </tr>
    <tr>
      <td>3. Solubilization</td>
      <td>Detergent solubilization for 2 h at 4°C</td>
      <td>—</td>
      <td>2% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Unsolubilized material removed at 150,000×g</td>
    </tr>
    <tr>
      <td>4. <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA</td>
      <td>PBS, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>; eluted with 250-300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> in PBS, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Purified protein buffer exchanged into PBS, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified SiaT at ~9 mg/mL in PBS, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M HEPES pH 7.5, 30% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 0.2 M MgCl2 (SeMet crystals); varying conditions for native crystals</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Cryoprotection: 30% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400 in mother liquor. SeMet data from 13 crystals merged using BLEND. Native data collected from space group P22_12_1. Structure determined by SeMet-SAD at 1.95 Å.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5nv9">5NV9</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MQLH</span><span class="topo-inside">DFGFINYA</span><span class="topo-membrane">VLFGYLAAMLLVGVYFSK</span><span class="topo-outside">RQKTADDYFRGGGRVPGW</span><span class="topo-membrane">AAGVSVFATTLS</span></span>
<span class="topo-line"><span class="topo-membrane">SITFMSI</span><span class="topo-inside">PAKAYTSDW</span><span class="topo-membrane">TFIIGQYLAIAILPLV</span><span class="topo-outside">FYFY</span><span class="topo-unknown">IPFFRK</span><span class="topo-outside">LKITSAYEYLEARFDV</span><span class="topo-membrane">RS</span></span>
<span class="topo-line"><span class="topo-membrane">RLFASLSFMLFHIGRVAIIT</span><span class="topo-inside">YLTVLALRPFMGIDPVVLI</span><span class="topo-membrane">VLISLLCIIYTWMGGIE</span><span class="topo-outside">G</span><span class="topo-membrane">VIW</span></span>
<span class="topo-line"><span class="topo-membrane">TDVIQGLLLSGGAVLIFI</span><span class="topo-inside">MICFKVDG</span><span class="topo-unknown">GISEIFTTTAQ</span><span class="topo-inside">ADKFFPTTQWRWSWTDS</span><span class="topo-membrane">TIPVLM</span></span>
<span class="topo-line"><span class="topo-membrane">IGFLFANIQQFTAS</span><span class="topo-outside">QDVVQRYIVTDSIKETKRT</span><span class="topo-membrane">LITNAKLVAIIPIFFFAI</span><span class="topo-inside">GSALFVYYQ</span></span>
<span class="topo-line"><span class="topo-inside">QNPSLLPAGFN</span><span class="topo-unknown">TGGILPLFIVTE</span><span class="topo-inside">MPIGIAG</span><span class="topo-membrane">LIIAAIFAAAQSSISSSLNSISSCFNSDIY</span></span>
<span class="topo-line"><span class="topo-outside">TRLSKSSPSPEQKM</span><span class="topo-membrane">KVAKLVIIVAGIFSSLAA</span><span class="topo-inside">IWLVLSD</span><span class="topo-unknown">EAEI</span><span class="topo-inside">WDA</span><span class="topo-membrane">FNSLIGLMGGPMTG</span></span>
<span class="topo-line"><span class="topo-membrane">LFML</span><span class="topo-outside">GIFVKRANAG</span><span class="topo-membrane">SAVVGIIVSIIAVLAARY</span><span class="topo-inside">GSDL</span><span class="topo-membrane">NFFFYGVIGSMSVVIAGTIT</span><span class="topo-outside">APLF</span></span>
<span class="topo-line"><span class="topo-outside">APAKQLSL</span><span class="topo-unknown">DDSETSEN</span></span>
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
      <td>5</td>
      <td>12</td>
      <td>5</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>30</td>
      <td>13</td>
      <td>30</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>48</td>
      <td>31</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>67</td>
      <td>49</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>76</td>
      <td>68</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>92</td>
      <td>77</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>96</td>
      <td>93</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>97</td>
      <td>102</td>
      <td>97</td>
      <td>102</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>103</td>
      <td>118</td>
      <td>103</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>140</td>
      <td>119</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>159</td>
      <td>141</td>
      <td>159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>176</td>
      <td>160</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>177</td>
      <td>177</td>
      <td>177</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>198</td>
      <td>178</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>206</td>
      <td>199</td>
      <td>206</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>217</td>
      <td>207</td>
      <td>217</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>218</td>
      <td>234</td>
      <td>218</td>
      <td>234</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>235</td>
      <td>254</td>
      <td>235</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>255</td>
      <td>273</td>
      <td>255</td>
      <td>273</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>291</td>
      <td>274</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>311</td>
      <td>292</td>
      <td>311</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>323</td>
      <td>312</td>
      <td>323</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>324</td>
      <td>330</td>
      <td>324</td>
      <td>330</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>360</td>
      <td>331</td>
      <td>360</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>361</td>
      <td>374</td>
      <td>361</td>
      <td>374</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>392</td>
      <td>375</td>
      <td>392</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>393</td>
      <td>399</td>
      <td>393</td>
      <td>399</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>404</td>
      <td>406</td>
      <td>404</td>
      <td>406</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>424</td>
      <td>407</td>
      <td>424</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>425</td>
      <td>434</td>
      <td>425</td>
      <td>434</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>435</td>
      <td>452</td>
      <td>435</td>
      <td>452</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>453</td>
      <td>456</td>
      <td>453</td>
      <td>456</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>457</td>
      <td>476</td>
      <td>457</td>
      <td>476</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>477</td>
      <td>488</td>
      <td>477</td>
      <td>488</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5nva">5NVA</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MQLH</span><span class="topo-inside">DFG</span><span class="topo-membrane">FINYAVLFGYLAAMLLVG</span><span class="topo-outside">VYFSKRQKTADDYFRGGGRVPGWAAG</span><span class="topo-membrane">VSVFATTLS</span></span>
<span class="topo-line"><span class="topo-membrane">SITFMSI</span><span class="topo-inside">PAKAYTSDW</span><span class="topo-membrane">TFIIGQYLAIAILPLV</span><span class="topo-outside">FYFYIPFFRKLKITSAYEYLEARFDVRS</span></span>
<span class="topo-line"><span class="topo-outside">RLF</span><span class="topo-membrane">ASLSFMLFHIGRVAIITYLTV</span><span class="topo-unknown">LALRPFM</span><span class="topo-inside">GID</span><span class="topo-membrane">PVVLIVLISLLCIIYTW</span><span class="topo-outside">MGGIEGV</span><span class="topo-membrane">IW</span></span>
<span class="topo-line"><span class="topo-membrane">TDVIQGLLLSGGAVLIFI</span><span class="topo-inside">MICFKVDG</span><span class="topo-unknown">GISEIFTTTAQ</span><span class="topo-inside">ADKFFPTTQWRWSWTDSTI</span><span class="topo-membrane">PVLM</span></span>
<span class="topo-line"><span class="topo-membrane">IGFLFANIQQFTAS</span><span class="topo-outside">QDVVQRYIVTDSIKETKRTL</span><span class="topo-membrane">ITNAKLVAIIPIFFFA</span><span class="topo-inside">IGSALFVYYQ</span></span>
<span class="topo-line"><span class="topo-inside">QNPSLLPAGFNTGGI</span><span class="topo-unknown">LPLFIVT</span><span class="topo-inside">EMPI</span><span class="topo-membrane">GIAGLIIAAIFAAAQSSISSSLNSIS</span><span class="topo-outside">SCFNSDIY</span></span>
<span class="topo-line"><span class="topo-outside">TRLSKSSPSPEQKMKVAKLV</span><span class="topo-membrane">IIVAGIFSSLAAIWLV</span><span class="topo-inside">LS</span><span class="topo-unknown">DEAEIWDAFN</span><span class="topo-inside">S</span><span class="topo-membrane">LIGLMGGPMTG</span></span>
<span class="topo-line"><span class="topo-membrane">LFML</span><span class="topo-outside">GIFVKRANAGSA</span><span class="topo-membrane">VVGIIVSIIAVLAARYG</span><span class="topo-inside">SDL</span><span class="topo-membrane">NFFFYGVIGSMSVVIAGTIT</span><span class="topo-outside">APLF</span></span>
<span class="topo-line"><span class="topo-outside">APAKQL</span><span class="topo-unknown">SLDDSETSEN</span></span>
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
      <td>5</td>
      <td>7</td>
      <td>5</td>
      <td>7</td>
      <td>Inside</td>
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
      <td>51</td>
      <td>26</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>67</td>
      <td>52</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>76</td>
      <td>68</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>92</td>
      <td>77</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>123</td>
      <td>93</td>
      <td>123</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>144</td>
      <td>124</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>151</td>
      <td>145</td>
      <td>151</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>152</td>
      <td>154</td>
      <td>152</td>
      <td>154</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>171</td>
      <td>155</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>172</td>
      <td>178</td>
      <td>172</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>198</td>
      <td>179</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>206</td>
      <td>199</td>
      <td>206</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>217</td>
      <td>207</td>
      <td>217</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>218</td>
      <td>236</td>
      <td>218</td>
      <td>236</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>237</td>
      <td>254</td>
      <td>237</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>255</td>
      <td>274</td>
      <td>255</td>
      <td>274</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>290</td>
      <td>275</td>
      <td>290</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>291</td>
      <td>315</td>
      <td>291</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>322</td>
      <td>316</td>
      <td>322</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>323</td>
      <td>326</td>
      <td>323</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>352</td>
      <td>327</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>380</td>
      <td>353</td>
      <td>380</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>381</td>
      <td>396</td>
      <td>381</td>
      <td>396</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>397</td>
      <td>398</td>
      <td>397</td>
      <td>398</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>409</td>
      <td>409</td>
      <td>409</td>
      <td>409</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>410</td>
      <td>424</td>
      <td>410</td>
      <td>424</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>425</td>
      <td>436</td>
      <td>425</td>
      <td>436</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>437</td>
      <td>453</td>
      <td>437</td>
      <td>453</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>454</td>
      <td>456</td>
      <td>454</td>
      <td>456</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>457</td>
      <td>476</td>
      <td>457</td>
      <td>476</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>477</td>
      <td>486</td>
      <td>477</td>
      <td>486</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### LeuT-fold and outward-open conformation

SiaT adopts the canonical LeuT-fold with 14 transmembrane helices (Tm0-Tm13) arranged in two inverted five-helix repeats (Tm1-Tm5 and Tm6-Tm10). The structure is in an outward-open conformation with a substrate-binding site accessible from the extracellular side. The substrate Neu5Ac is coordinated by residues from Tm1 (Thr58, Leu59, Ser60, Thr63) and Tm2 (Gln82), and forms a salt bridge with Arg135 from Tm3.

### Neu5Ac substrate binding site

The sialic acid N-acetylneuraminic acid (Neu5Ac) is bound in an extended conformation with its N-acetyl group pointing toward Tm10. Key interactions include hydrogen bonds with Thr58 (hydroxyl of Neu5Ac), Thr63 ([Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) moiety), Ser60, and Gln82, plus a salt bridge between Arg135 and the carboxylate group of Neu5Ac. Water-mediated hydrogen bonds further stabilize binding via Gln82, Asn247, Gln250, and Phe78. Binding affinity measured by MST (Kd = 58 ± 1 µM) and [ITC](/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/) (Kd = 50 ± 4 µM). SiaT also binds Neu5Gc (Kd = 85 ± 2 µM) but much more weakly binds KDN (Kd > 10 mM).

### Na2 sodium binding site

The Na2 site is the conserved sodium binding site found in all LeuT-fold transporters. It is located ~7 Å from the substrate between Tm1 and Tm8 at a prominent kink in Tm1. The Na+ is coordinated by the backbone carbonyls of Leu59, Gly61, and Ser342, and the side chain hydroxyls of Ser342 and Ser343. This site is universally conserved among SSS family members.

### Na3 novel sodium binding site

A second Na+ binds to a newly identified Na3 site positioned close to the Na2 site but not contacting the substrate. The Na3 site is coordinated by Asp182 (side chain), Ser345 and Ser346 (side chain hydroxyls), and Ser342 (main chain carbonyl). Bioinformatic analysis of 39,612 SSS sequences shows Na3 is present in 19.6% of sequences (4,212) including hSGLT1 (2 Na+:1 substrate) but absent in [VSGLT](/xray-mp-wiki/proteins/slc-transporters/vsglt/) and hSGLT2 (1 Na+:1 substrate). The Na3 site is unique to a SSS family subgroup and distinct from the Na1/Na1' sites found in [LEUT](/xray-mp-wiki/proteins/enzymes/leut/), dDAT, and [BETP](/xray-mp-wiki/proteins/slc-transporters/betp/).

### Allosteric role of Na3 in substrate binding

Molecular dynamics simulations demonstrate that Na3 binding allosterically stabilizes the substrate without directly coordinating it. When both Na2 and Na3 are bound, Neu5Ac remains stably bound. In the absence of Na3, the substrate shows higher conformational flexibility. The Na3 site may help pre-organise the binding site through effects on the Leu59 backbone (φ/ψ angles), which in turn affects the unwound region of Tm1 that coordinates the substrate.

### Structural basis for Na+ stoichiometry variation in SSS family

The discovery of the Na3 site provides a structural explanation for the variable Na+:substrate stoichiometry within the SSS family. Members with the Na3 site (conserved D182, S345, S346) can couple 2 Na+ per transport cycle, while those lacking the Na3 site (conserved hydrophobic residues at corresponding positions) couple only 1 Na+. This suggests that evolutionary acquisition of the Na3 site allows transporters to harness additional energy from the Na+ gradient, enabling transport against steeper substrate concentration gradients.

### Inward-open model and gating mechanism

An inward-open model of SiaT was generated using molecular dynamics, showing predicted movement of transmembrane helices. The periplasmic gate helices (Ilh0, Tm7, Tm8, Tm10) close during the transition, while the cytoplasmic gate opens via movement of Ilh0, Tm1, Tm6, and Tm8. Arg260 (Tm6) stabilizes the inner gate in a closed conformation through interactions with Ser53, Asp256, and Ser346. The inward-open model reveals how the [Alternating Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) operates in this SSS family member.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — Related biological concept
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/sss-family/">Sodium Solute Symporter (SSS) Family</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/quality-assessment/isothermal-titration-calorimetry/">ITC</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/enzymes/leut/">LEUT</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/slc-transporters/betp/">BETP</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/slc-transporters/vsglt/">VSGLT</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
