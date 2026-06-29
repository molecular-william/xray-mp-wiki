---
title: "CmABCB1 (Homodimeric P-glycoprotein from Cyanidioschyzon merolae)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-018-08007-x, doi/10.1073##pnas.1321562111]
verified: false
---

# CmABCB1 (Homodimeric P-glycoprotein from Cyanidioschyzon merolae)

## Overview

CmABCB1 is a homodimeric P-glycoprotein from the red alga Cyanidioschyzon
merolae, a member of the ABC Transporter Family that mediates active efflux
of diverse hydrophobic xenobiotics. A pair of X-ray crystal structures were
determined in a 2018 study: an outward-facing nucleotide-bound state at
1.9 Å resolution (PDB 6A6M) and an inward-facing apo state at 3.0 Å
resolution (PDB 6A6N), revealing conformational changes between states.

A subsequent study determined the structure of CmABCB1 in an inward-open
conformation at 2.6 Å resolution (unbound) and 2.4 Å resolution (bound to
the macrocyclic peptide inhibitor aCAP). The aCAP clamps the transmembrane
helices from the outside, fixing the inward-open conformation. These
structures reveal the detailed architecture of the transporter gating
apparatus, including extracellular, intramembranous, and cytosolic gates.


## Publications

### doi/10.1038##s41467-018-08007-x

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6a6m">6A6M</a></td>
      <td>1.9</td>
      <td>P4₁32</td>
      <td>QTA CmABCB1 (E610A/E620A/D621A)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/amp-pnp/">Mg²⁺·AMP-PNP</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6a6n">6A6N</a></td>
      <td>3.0</td>
      <td>R32</td>
      <td>QTA CmABCB1 (E610A/E620A/D621A)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae AD1-8u⁻ (for 2018 structures); Pichia pastoris SMD1163 (for WT CmABCB1 in 2014 paper)
- **Construct**: QTA mutant (E610A, E620A, D621A) for ATPase-deficient crystallization

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
      <td>Emulsiflex-C3 homogenization followed by differential centrifugation</td>
      <td>—</td>
      <td>20 mM Tris pH 7.0, 150 mM NaCl</td>
      <td>Crude membranes collected at 100,000 × g</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>20 mM Tris pH 7.0, 300 mM NaCl, 20 mM Imidazole + 1% (w/v) C12E9</td>
      <td>1 h solubilization</td>
    </tr>
    <tr>
      <td>IMAC</td>
      <td>Immobilized metal-ion <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Bio-Rad IMAC resin</td>
      <td>20 mM Tris pH 7.0, 300 mM NaCl, 300 mM imidazole</td>
      <td></td>
    </tr>
    <tr>
      <td>Trypsin cleavage</td>
      <td>Enzymatic cleavage</td>
      <td>—</td>
      <td></td>
      <td>N-terminal flexible region (1–92) cleaved by Trypsin treatment</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase (GE Healthcare)</td>
      <td>20 mM Tris pH 7.0, 150 mM NaCl, 0.2% (w/v) β-<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: 10 mg/mL in 20 mM Tris·HCl pH 7.0, 150 mM NaCl, 0.2% n-decyl-β-D-maltopyranoside

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, sitting drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>10 mg/ml CmABCB1</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>19–21% PEG 2000 MME, 50 mM KNO₃ pH 7.4, 50 mM Mg(NO₃)₂ pH 4.1</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 °C</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>30% PEG 2000 MME, 5% 1,4-Butanediol</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Outward-facing (P4₁32 space group)</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, sitting drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>10 mg/ml CmABCB1</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>14% PEG 2000 MME, 100 mM Mg(NO₃)₂ pH 4.1</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 °C</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>30% PEG 2000 MME, 5% 1,4-Butanediol</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Inward-facing (R32 space group)</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6a6m">6A6M</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">ASGPESAY</span><span class="topo-inside">T</span><span class="topo-unknown">TGVTARRIFALAWSSSA</span><span class="topo-membrane">TMIVIGFIASILEGATLPAFAIVF</span><span class="topo-outside">GRMFAVFTKS</span></span>
<span class="topo-line"><span class="topo-outside">KSQIEGETWKY</span><span class="topo-membrane">SVGFVGIGVFEFIVAGSRTALFG</span><span class="topo-inside">IASERLARDLRVAAFSNLVEQDVTYF</span></span>
<span class="topo-line"><span class="topo-inside">DRRKAGELGGKLNNDVQVIQYS</span><span class="topo-membrane">FSKLGAVLFNLAQCVVGIIVAFIF</span><span class="topo-outside">APAL</span><span class="topo-membrane">TGVLIALSPL</span></span>
<span class="topo-line"><span class="topo-membrane">VVLAGAAQMI</span><span class="topo-inside">EMSGNTKRSSEAYASAGSVAAEVFSNIRTTKAFEAERYETQRYGSKLDPL</span></span>
<span class="topo-line"><span class="topo-inside">YRLGRRRY</span><span class="topo-membrane">ISDGLFFGLSMLVIFCVYALALWW</span><span class="topo-outside">GGQLIARGSLNLGNLLAA</span><span class="topo-membrane">FFSAILGFMG</span></span>
<span class="topo-line"><span class="topo-membrane">VGQAAQVWPDVT</span><span class="topo-inside">RGLGAGGELFAMIDRVPQYRRPDPGAEVVTQPLVLKQGIVFENVHFRY</span></span>
<span class="topo-line"><span class="topo-inside">PTRMNVEVLRGISLTIPNGKTVAIVGGSGAGKSTIIQLLMRFYDIEPQGGGLLLFDGTPA</span></span>
<span class="topo-line"><span class="topo-inside">WNYDFHALRSQIGLVSQEPVLFSGTIRDNILYGKRDATDEEVIQALREANAYSFVMALPD</span></span>
<span class="topo-line"><span class="topo-inside">GLDTEVGERGLALSGGQKQRIAIARAILKHPTLLCLDESTSALDAESEALVQEALDRMMA</span></span>
<span class="topo-line"><span class="topo-inside">SDGVTSVVIAHRLSTVARADLILVMQDGVVVEQGNHSELMALGPSGFYYQLVEKQLA</span><span class="topo-unknown">SGD</span></span>
<span class="topo-line"><span class="topo-unknown">MSAAGSENLYFQ</span></span>
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
      <td>9</td>
      <td>9</td>
      <td>101</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>26</td>
      <td>102</td>
      <td>118</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>50</td>
      <td>119</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>71</td>
      <td>143</td>
      <td>163</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>94</td>
      <td>164</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>142</td>
      <td>187</td>
      <td>234</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>166</td>
      <td>235</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>170</td>
      <td>259</td>
      <td>262</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>190</td>
      <td>263</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>248</td>
      <td>283</td>
      <td>340</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>272</td>
      <td>341</td>
      <td>364</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>290</td>
      <td>365</td>
      <td>382</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>312</td>
      <td>383</td>
      <td>404</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>597</td>
      <td>405</td>
      <td>689</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6a6m">6A6M</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">ASGPESAY</span><span class="topo-inside">T</span><span class="topo-unknown">TGVTARRIFALAWSSSA</span><span class="topo-membrane">TMIVIGFIASILEGATLPAFAIVF</span><span class="topo-outside">GRMFAVFTKS</span></span>
<span class="topo-line"><span class="topo-outside">KSQIEGETWKY</span><span class="topo-membrane">SVGFVGIGVFEFIVAGSRTALFG</span><span class="topo-inside">IASERLARDLRVAAFSNLVEQDVTYF</span></span>
<span class="topo-line"><span class="topo-inside">DRRKAGELGGKLNNDVQVIQYS</span><span class="topo-membrane">FSKLGAVLFNLAQCVVGIIVAFIF</span><span class="topo-outside">APAL</span><span class="topo-membrane">TGVLIALSPL</span></span>
<span class="topo-line"><span class="topo-membrane">VVLAGAAQMI</span><span class="topo-inside">EMSGNTKRSSEAYASAGSVAAEVFSNIRTTKAFEAERYETQRYGSKLDPL</span></span>
<span class="topo-line"><span class="topo-inside">YRLGRRRY</span><span class="topo-membrane">ISDGLFFGLSMLVIFCVYALALWW</span><span class="topo-outside">GGQLIARGSLNLGNLLAA</span><span class="topo-membrane">FFSAILGFMG</span></span>
<span class="topo-line"><span class="topo-membrane">VGQAAQVWPDVT</span><span class="topo-inside">RGLGAGGELFAMIDRVPQYRRPDPGAEVVTQPLVLKQGIVFENVHFRY</span></span>
<span class="topo-line"><span class="topo-inside">PTRMNVEVLRGISLTIPNGKTVAIVGGSGAGKSTIIQLLMRFYDIEPQGGGLLLFDGTPA</span></span>
<span class="topo-line"><span class="topo-inside">WNYDFHALRSQIGLVSQEPVLFSGTIRDNILYGKRDATDEEVIQALREANAYSFVMALPD</span></span>
<span class="topo-line"><span class="topo-inside">GLDTEVGERGLALSGGQKQRIAIARAILKHPTLLCLDESTSALDAESEALVQEALDRMMA</span></span>
<span class="topo-line"><span class="topo-inside">SDGVTSVVIAHRLSTVARADLILVMQDGVVVEQGNHSELMALGPSGFYYQLVEKQLA</span><span class="topo-unknown">SGD</span></span>
<span class="topo-line"><span class="topo-unknown">MSAAGSENLYFQ</span></span>
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
      <td>9</td>
      <td>9</td>
      <td>101</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>10</td>
      <td>26</td>
      <td>102</td>
      <td>118</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>27</td>
      <td>50</td>
      <td>119</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>71</td>
      <td>143</td>
      <td>163</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>94</td>
      <td>164</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>142</td>
      <td>187</td>
      <td>234</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>166</td>
      <td>235</td>
      <td>258</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>170</td>
      <td>259</td>
      <td>262</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>190</td>
      <td>263</td>
      <td>282</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>248</td>
      <td>283</td>
      <td>340</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>249</td>
      <td>272</td>
      <td>341</td>
      <td>364</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>273</td>
      <td>290</td>
      <td>365</td>
      <td>382</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>312</td>
      <td>383</td>
      <td>404</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>597</td>
      <td>405</td>
      <td>689</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6a6n">6A6N</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">ASGPESAYT</span><span class="topo-inside">T</span><span class="topo-unknown">GVTARRIFALAWSS</span><span class="topo-inside">S</span><span class="topo-membrane">ATMIVIGFIASILEGATLPAFAIVF</span><span class="topo-outside">GRMFAVFTKS</span></span>
<span class="topo-line"><span class="topo-outside">KSQIEGETWKYSV</span><span class="topo-membrane">GFVGIGVFEFIVAGSRTALFGIA</span><span class="topo-inside">SERLARDLRVAAFSNLVEQDVTYF</span></span>
<span class="topo-line"><span class="topo-inside">DRRKAGELGGKLNNDVQVIQYSF</span><span class="topo-membrane">SKLGAVLFNLAQCVVGIIVAF</span><span class="topo-outside">IFAPALT</span><span class="topo-membrane">GVLIALSPL</span></span>
<span class="topo-line"><span class="topo-membrane">VVLAGAAQMIEM</span><span class="topo-inside">SGNTKRSSEAYASAGSVAAEVFSNIRTTKAFEAERYETQRYGSKLDPL</span></span>
<span class="topo-line"><span class="topo-inside">YRLGR</span><span class="topo-membrane">RRYISDGLFFGLSMLVIFCVYALA</span><span class="topo-outside">LWWGGQLIARGSLNLGNLLA</span><span class="topo-membrane">AFFSAILGFMG</span></span>
<span class="topo-line"><span class="topo-membrane">VGQAAQVWPDV</span><span class="topo-inside">TRGLGAGGELFAMIDRVPQYRRPDPGAEVVTQPLVLKQGIVFENVHFRY</span></span>
<span class="topo-line"><span class="topo-inside">PTRMNVEVLRGISLTIPNGKTVAIVGGSGAGKSTIIQLLMRFYDIEPQGGGLLLFDGTPA</span></span>
<span class="topo-line"><span class="topo-inside">WNYDFHALRSQIGLVSQEPVLFSGTIRDNILYGKRDATDEEVIQALREANAYSFVMALPD</span></span>
<span class="topo-line"><span class="topo-inside">GLDTEVGERGLALSGGQKQRIAIARAILKHPTLLCLDESTSALDAESEALVQEALDRMMA</span></span>
<span class="topo-line"><span class="topo-inside">SDGVTSVVIAHRLSTVARADLILVMQDGVVVEQGNHSELMALGPSGFYYQLVEKQL</span><span class="topo-unknown">ASGD</span></span>
<span class="topo-line"><span class="topo-unknown">MSAAGSENLYFQ</span></span>
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
      <td>10</td>
      <td>10</td>
      <td>102</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>24</td>
      <td>103</td>
      <td>116</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>25</td>
      <td>25</td>
      <td>117</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>118</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>73</td>
      <td>143</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>96</td>
      <td>166</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>143</td>
      <td>189</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>164</td>
      <td>236</td>
      <td>256</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>171</td>
      <td>257</td>
      <td>263</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>192</td>
      <td>264</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>245</td>
      <td>285</td>
      <td>337</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>269</td>
      <td>338</td>
      <td>361</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>289</td>
      <td>362</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>311</td>
      <td>382</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>596</td>
      <td>404</td>
      <td>688</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6a6n">6A6N</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">ASGPESAYT</span><span class="topo-inside">T</span><span class="topo-unknown">GVTARRIFALAWSS</span><span class="topo-inside">S</span><span class="topo-membrane">ATMIVIGFIASILEGATLPAFAIVF</span><span class="topo-outside">GRMFAVFTKS</span></span>
<span class="topo-line"><span class="topo-outside">KSQIEGETWKYSV</span><span class="topo-membrane">GFVGIGVFEFIVAGSRTALFGIA</span><span class="topo-inside">SERLARDLRVAAFSNLVEQDVTYF</span></span>
<span class="topo-line"><span class="topo-inside">DRRKAGELGGKLNNDVQVIQYSF</span><span class="topo-membrane">SKLGAVLFNLAQCVVGIIVAF</span><span class="topo-outside">IFAPALT</span><span class="topo-membrane">GVLIALSPL</span></span>
<span class="topo-line"><span class="topo-membrane">VVLAGAAQMIEM</span><span class="topo-inside">SGNTKRSSEAYASAGSVAAEVFSNIRTTKAFEAERYETQRYGSKLDPL</span></span>
<span class="topo-line"><span class="topo-inside">YRLGR</span><span class="topo-membrane">RRYISDGLFFGLSMLVIFCVYALA</span><span class="topo-outside">LWWGGQLIARGSLNLGNLLA</span><span class="topo-membrane">AFFSAILGFMG</span></span>
<span class="topo-line"><span class="topo-membrane">VGQAAQVWPDV</span><span class="topo-inside">TRGLGAGGELFAMIDRVPQYRRPDPGAEVVTQPLVLKQGIVFENVHFRY</span></span>
<span class="topo-line"><span class="topo-inside">PTRMNVEVLRGISLTIPNGKTVAIVGGSGAGKSTIIQLLMRFYDIEPQGGGLLLFDGTPA</span></span>
<span class="topo-line"><span class="topo-inside">WNYDFHALRSQIGLVSQEPVLFSGTIRDNILYGKRDATDEEVIQALREANAYSFVMALPD</span></span>
<span class="topo-line"><span class="topo-inside">GLDTEVGERGLALSGGQKQRIAIARAILKHPTLLCLDESTSALDAESEALVQEALDRMMA</span></span>
<span class="topo-line"><span class="topo-inside">SDGVTSVVIAHRLSTVARADLILVMQDGVVVEQGNHSELMALGPSGFYYQLVEKQL</span><span class="topo-unknown">ASGD</span></span>
<span class="topo-line"><span class="topo-unknown">MSAAGSENLYFQ</span></span>
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
      <td>10</td>
      <td>10</td>
      <td>102</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>24</td>
      <td>103</td>
      <td>116</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>25</td>
      <td>25</td>
      <td>117</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>50</td>
      <td>118</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>73</td>
      <td>143</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>96</td>
      <td>166</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>143</td>
      <td>189</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>164</td>
      <td>236</td>
      <td>256</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>165</td>
      <td>171</td>
      <td>257</td>
      <td>263</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>192</td>
      <td>264</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>245</td>
      <td>285</td>
      <td>337</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>269</td>
      <td>338</td>
      <td>361</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>289</td>
      <td>362</td>
      <td>381</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>311</td>
      <td>382</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>596</td>
      <td>404</td>
      <td>688</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.1321562111

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3wme">3WME</a></td>
      <td>2.60</td>
      <td>R32</td>
      <td>WT CmABCB1 with N-terminal region (1-92) cleaved, C-terminal His₁₀ tag removed</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3wme">3WME</a></td>
      <td>2.40</td>
      <td>R32</td>
      <td>WT CmABCB1 with N-terminal region (1-92) cleaved, bound to aCAP</td>
      <td>aCAP (macrocyclic peptide inhibitor)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae AD1-8u⁻ (for 2018 structures); Pichia pastoris SMD1163 (for WT CmABCB1 in 2014 paper)
- **Construct**: QTA mutant (E610A, E620A, D621A) for ATPase-deficient crystallization

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>CmABCB1 at 10 mg/mL in 20 mM Tris·HCl pH 7.0, 150 mM NaCl, 0.2% n-decyl-β-D-maltopyranoside; with or without aCAP (2:1 molar ratio)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>14-16% (wt/vol) PEG 2000 MME, 100 mM magnesium nitrate</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 °C</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Frozen crystal</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected at BL41XU of SPring-8 using MAR225HE detector. Space group R32. Initial phases from <a href="/xray-mp-wiki/methods/structure-determination/multi-wavelength-anomalous-diffraction/">MAD</a> on mercury derivative.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3wme">3WME</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">ASGPESAYT</span><span class="topo-outside">T</span><span class="topo-unknown">GVTARRIFALAWSSS</span><span class="topo-membrane">ATMIVIGFIASILEGATLPAFAI</span><span class="topo-inside">VFGRMFQVFTKS</span></span>
<span class="topo-line"><span class="topo-inside">KSQIEGETWKYSVG</span><span class="topo-membrane">FVGIGVFEFIVAGSRTALFGIA</span><span class="topo-outside">SERLARDLRVAAFSNLVEQDVTYF</span></span>
<span class="topo-line"><span class="topo-outside">DRRKAGELGGKLNNDVQVIQYSF</span><span class="topo-membrane">SKLGAVLFNLAQCVVGIIVAFI</span><span class="topo-inside">FAPALT</span><span class="topo-membrane">GVLIALSPL</span></span>
<span class="topo-line"><span class="topo-membrane">VVLAGAAQMIEM</span><span class="topo-outside">SGNTKRSSEAYASAGSVAAEVFSNIRTTKAFEAERYETQRYGSKLDPL</span></span>
<span class="topo-line"><span class="topo-outside">YRLGRR</span><span class="topo-membrane">RYISDGLFFGLSMLVIFCVYALA</span><span class="topo-inside">LWWGGQLIARGSLNLGNLLT</span><span class="topo-membrane">AFFSAILGFMG</span></span>
<span class="topo-line"><span class="topo-membrane">VGQAAQVWPDV</span><span class="topo-outside">TRGLGAGGELFAMIDRVPQYRRPDPGAEVVTQPLVLKQGIVFENVHFRY</span></span>
<span class="topo-line"><span class="topo-outside">PTRMNVEVLRGISLTIPNGKTVAIVGGSGAGKSTIIQLLMRFYDIEPQGGGLLLFDGTPA</span></span>
<span class="topo-line"><span class="topo-outside">WNYDFHALRSQIGLVSQEPVLFSGTIRDNILYGKRDATDEEVIQALREANAYSFVMALPD</span></span>
<span class="topo-line"><span class="topo-outside">GLDTEVGERGLALSGGQKQRIAIARAILKHPTLLCLDESTSALDAESEALVQEALDRMMA</span></span>
<span class="topo-line"><span class="topo-outside">SDGVTSVVIAHRLSTVARADLILVMQDGVVVEQGNHSELMALGPSGFYYQLVEKQLA</span><span class="topo-unknown">SGD</span></span>
<span class="topo-line"><span class="topo-unknown">MSAAGSENLYFQ</span></span>
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
      <td>93</td>
      <td>101</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>10</td>
      <td>102</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>25</td>
      <td>103</td>
      <td>117</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>48</td>
      <td>118</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>74</td>
      <td>141</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>96</td>
      <td>167</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>143</td>
      <td>189</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>165</td>
      <td>236</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>171</td>
      <td>258</td>
      <td>263</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>192</td>
      <td>264</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>246</td>
      <td>285</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>269</td>
      <td>339</td>
      <td>361</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>289</td>
      <td>362</td>
      <td>381</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>311</td>
      <td>382</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>597</td>
      <td>404</td>
      <td>689</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>598</td>
      <td>612</td>
      <td>690</td>
      <td>704</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3wme">3WME</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">ASGPESAYT</span><span class="topo-outside">T</span><span class="topo-unknown">GVTARRIFALAWSSS</span><span class="topo-membrane">ATMIVIGFIASILEGATLPAFAI</span><span class="topo-inside">VFGRMFQVFTKS</span></span>
<span class="topo-line"><span class="topo-inside">KSQIEGETWKYSVG</span><span class="topo-membrane">FVGIGVFEFIVAGSRTALFGIA</span><span class="topo-outside">SERLARDLRVAAFSNLVEQDVTYF</span></span>
<span class="topo-line"><span class="topo-outside">DRRKAGELGGKLNNDVQVIQYSF</span><span class="topo-membrane">SKLGAVLFNLAQCVVGIIVAFI</span><span class="topo-inside">FAPALT</span><span class="topo-membrane">GVLIALSPL</span></span>
<span class="topo-line"><span class="topo-membrane">VVLAGAAQMIEM</span><span class="topo-outside">SGNTKRSSEAYASAGSVAAEVFSNIRTTKAFEAERYETQRYGSKLDPL</span></span>
<span class="topo-line"><span class="topo-outside">YRLGRR</span><span class="topo-membrane">RYISDGLFFGLSMLVIFCVYALA</span><span class="topo-inside">LWWGGQLIARGSLNLGNLLT</span><span class="topo-membrane">AFFSAILGFMG</span></span>
<span class="topo-line"><span class="topo-membrane">VGQAAQVWPDV</span><span class="topo-outside">TRGLGAGGELFAMIDRVPQYRRPDPGAEVVTQPLVLKQGIVFENVHFRY</span></span>
<span class="topo-line"><span class="topo-outside">PTRMNVEVLRGISLTIPNGKTVAIVGGSGAGKSTIIQLLMRFYDIEPQGGGLLLFDGTPA</span></span>
<span class="topo-line"><span class="topo-outside">WNYDFHALRSQIGLVSQEPVLFSGTIRDNILYGKRDATDEEVIQALREANAYSFVMALPD</span></span>
<span class="topo-line"><span class="topo-outside">GLDTEVGERGLALSGGQKQRIAIARAILKHPTLLCLDESTSALDAESEALVQEALDRMMA</span></span>
<span class="topo-line"><span class="topo-outside">SDGVTSVVIAHRLSTVARADLILVMQDGVVVEQGNHSELMALGPSGFYYQLVEKQLA</span><span class="topo-unknown">SGD</span></span>
<span class="topo-line"><span class="topo-unknown">MSAAGSENLYFQ</span></span>
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
      <td>93</td>
      <td>101</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>10</td>
      <td>102</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>25</td>
      <td>103</td>
      <td>117</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>48</td>
      <td>118</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>74</td>
      <td>141</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>96</td>
      <td>167</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>143</td>
      <td>189</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>165</td>
      <td>236</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>171</td>
      <td>258</td>
      <td>263</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>192</td>
      <td>264</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>246</td>
      <td>285</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>269</td>
      <td>339</td>
      <td>361</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>289</td>
      <td>362</td>
      <td>381</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>311</td>
      <td>382</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>597</td>
      <td>404</td>
      <td>689</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>598</td>
      <td>612</td>
      <td>690</td>
      <td>704</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3wme">3WME</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">ASGPESAYT</span><span class="topo-outside">T</span><span class="topo-unknown">GVTARRIFALAWSSS</span><span class="topo-membrane">ATMIVIGFIASILEGATLPAFAI</span><span class="topo-inside">VFGRMFQVFTKS</span></span>
<span class="topo-line"><span class="topo-inside">KSQIEGETWKYSVG</span><span class="topo-membrane">FVGIGVFEFIVAGSRTALFGIA</span><span class="topo-outside">SERLARDLRVAAFSNLVEQDVTYF</span></span>
<span class="topo-line"><span class="topo-outside">DRRKAGELGGKLNNDVQVIQYSF</span><span class="topo-membrane">SKLGAVLFNLAQCVVGIIVAFI</span><span class="topo-inside">FAPALT</span><span class="topo-membrane">GVLIALSPL</span></span>
<span class="topo-line"><span class="topo-membrane">VVLAGAAQMIEM</span><span class="topo-outside">SGNTKRSSEAYASAGSVAAEVFSNIRTTKAFEAERYETQRYGSKLDPL</span></span>
<span class="topo-line"><span class="topo-outside">YRLGRR</span><span class="topo-membrane">RYISDGLFFGLSMLVIFCVYALA</span><span class="topo-inside">LWWGGQLIARGSLNLGNLLT</span><span class="topo-membrane">AFFSAILGFMG</span></span>
<span class="topo-line"><span class="topo-membrane">VGQAAQVWPDV</span><span class="topo-outside">TRGLGAGGELFAMIDRVPQYRRPDPGAEVVTQPLVLKQGIVFENVHFRY</span></span>
<span class="topo-line"><span class="topo-outside">PTRMNVEVLRGISLTIPNGKTVAIVGGSGAGKSTIIQLLMRFYDIEPQGGGLLLFDGTPA</span></span>
<span class="topo-line"><span class="topo-outside">WNYDFHALRSQIGLVSQEPVLFSGTIRDNILYGKRDATDEEVIQALREANAYSFVMALPD</span></span>
<span class="topo-line"><span class="topo-outside">GLDTEVGERGLALSGGQKQRIAIARAILKHPTLLCLDESTSALDAESEALVQEALDRMMA</span></span>
<span class="topo-line"><span class="topo-outside">SDGVTSVVIAHRLSTVARADLILVMQDGVVVEQGNHSELMALGPSGFYYQLVEKQLA</span><span class="topo-unknown">SGD</span></span>
<span class="topo-line"><span class="topo-unknown">MSAAGSENLYFQ</span></span>
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
      <td>93</td>
      <td>101</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>10</td>
      <td>102</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>25</td>
      <td>103</td>
      <td>117</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>48</td>
      <td>118</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>74</td>
      <td>141</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>96</td>
      <td>167</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>143</td>
      <td>189</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>165</td>
      <td>236</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>171</td>
      <td>258</td>
      <td>263</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>192</td>
      <td>264</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>246</td>
      <td>285</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>269</td>
      <td>339</td>
      <td>361</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>289</td>
      <td>362</td>
      <td>381</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>311</td>
      <td>382</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>597</td>
      <td>404</td>
      <td>689</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>598</td>
      <td>612</td>
      <td>690</td>
      <td>704</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3wme">3WME</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">ASGPESAYT</span><span class="topo-outside">T</span><span class="topo-unknown">GVTARRIFALAWSSS</span><span class="topo-membrane">ATMIVIGFIASILEGATLPAFAI</span><span class="topo-inside">VFGRMFQVFTKS</span></span>
<span class="topo-line"><span class="topo-inside">KSQIEGETWKYSVG</span><span class="topo-membrane">FVGIGVFEFIVAGSRTALFGIA</span><span class="topo-outside">SERLARDLRVAAFSNLVEQDVTYF</span></span>
<span class="topo-line"><span class="topo-outside">DRRKAGELGGKLNNDVQVIQYSF</span><span class="topo-membrane">SKLGAVLFNLAQCVVGIIVAFI</span><span class="topo-inside">FAPALT</span><span class="topo-membrane">GVLIALSPL</span></span>
<span class="topo-line"><span class="topo-membrane">VVLAGAAQMIEM</span><span class="topo-outside">SGNTKRSSEAYASAGSVAAEVFSNIRTTKAFEAERYETQRYGSKLDPL</span></span>
<span class="topo-line"><span class="topo-outside">YRLGRR</span><span class="topo-membrane">RYISDGLFFGLSMLVIFCVYALA</span><span class="topo-inside">LWWGGQLIARGSLNLGNLLT</span><span class="topo-membrane">AFFSAILGFMG</span></span>
<span class="topo-line"><span class="topo-membrane">VGQAAQVWPDV</span><span class="topo-outside">TRGLGAGGELFAMIDRVPQYRRPDPGAEVVTQPLVLKQGIVFENVHFRY</span></span>
<span class="topo-line"><span class="topo-outside">PTRMNVEVLRGISLTIPNGKTVAIVGGSGAGKSTIIQLLMRFYDIEPQGGGLLLFDGTPA</span></span>
<span class="topo-line"><span class="topo-outside">WNYDFHALRSQIGLVSQEPVLFSGTIRDNILYGKRDATDEEVIQALREANAYSFVMALPD</span></span>
<span class="topo-line"><span class="topo-outside">GLDTEVGERGLALSGGQKQRIAIARAILKHPTLLCLDESTSALDAESEALVQEALDRMMA</span></span>
<span class="topo-line"><span class="topo-outside">SDGVTSVVIAHRLSTVARADLILVMQDGVVVEQGNHSELMALGPSGFYYQLVEKQLA</span><span class="topo-unknown">SGD</span></span>
<span class="topo-line"><span class="topo-unknown">MSAAGSENLYFQ</span></span>
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
      <td>93</td>
      <td>101</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>10</td>
      <td>102</td>
      <td>102</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>25</td>
      <td>103</td>
      <td>117</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>48</td>
      <td>118</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>74</td>
      <td>141</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>96</td>
      <td>167</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>143</td>
      <td>189</td>
      <td>235</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>165</td>
      <td>236</td>
      <td>257</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>171</td>
      <td>258</td>
      <td>263</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>172</td>
      <td>192</td>
      <td>264</td>
      <td>284</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>246</td>
      <td>285</td>
      <td>338</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>269</td>
      <td>339</td>
      <td>361</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>270</td>
      <td>289</td>
      <td>362</td>
      <td>381</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>311</td>
      <td>382</td>
      <td>403</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>597</td>
      <td>404</td>
      <td>689</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>598</td>
      <td>612</td>
      <td>690</td>
      <td>704</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Conformational states

The inward-facing apo structure reveals a large kernel-shaped inner chamber surrounded by all 12 TM helices. The outward-facing Mg·AMP-PNP-bound structure shows chamber contraction, driven by NBD dimerization.

### Chamber contraction regulator

Residues Gln398(TM6) and Ala240(TM3) form van der Waals contacts that regulate chamber volume. Mutation decreases transport activity.

### RE-latch

Glu620(α6) and Arg644(α7) form a salt bridge (RE-latch) at the NBD dimer interface that stabilizes the outward-facing conformation.

### Extracellular gate mechanism

TM1, TM2, TM5, and TM6 form a four-layered cluster of aromatic and hydrophobic
residues near the extracellular side. The GXXXG motif in TM2 and TM5 enables
close helix-helix contact. Opening of the extracellular gate occurs when TM1
and TM6 move in opposite directions (11.2 and 7.8 Å, respectively), dissociating
the helix bundle. ATP binding to NBDs causes rigid-body NBD rotation (19°),
tilt (10°), and translation (10 Å), transmitted through IH1 and IH2 to TM2 and TM5.

### Intramembranous gate and TM4 flexibility

A wide cleft between TM4 and TM6 spans the hydrophobic interface between the
TMD and inner leaflet of the lipid bilayer. TM4 exhibits intrinsic flexibility
(Gly277-Gly286 disordered) and is kinked at Pro271 and Gly299, acting as a
"gatekeeper" for substrate entry from the membrane bilayer. GAA/VVV mutation
and P271A substitution both reduce transport activity.

### aCAP allosteric inhibition

aCAP (anti-CmABCB1 peptide) is a macrocyclic peptide inhibitor that acts as a
surface clamp, binding TM2 and TM6 from the extracellular surface. It reinforces
TM1-TM6 interaction and prevents the extracellular gate from opening. aCAP
inhibits both basal and rhodamine 6G-stimulated ATPase activities (K_i 46-fold
tighter than K_m for rhodamine 6G). This confirms that extracellular gate opening
is required for the substrate-dependent ATP hydrolysis cycle.

### Vacuum cleaner model support

Structural comparison between inward-open CmABCB1 and outward-open Sav1866
(RMSD 2.4 Å for Cα) reveals that NBD dimerization drives structural changes.
The movement is transmitted to TM2 and TM5 through IH1 and IH2 coupling helices.
This mechanism is consistent with the "vacuum cleaner" model of ABC multidrug
transport, where substrates are extracted from the inner leaflet of the lipid
bilayer.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/">ABC Transporter Family</a> — CmABCB1 is a member of the ABC transporter superfamily
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/inward-facing-conformation/">Inward-Facing Conformation</a> — Structures capture inward-open apo and inhibitor-bound states
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/outward-facing-conformation/">Outward-Facing Conformation</a> — The 1.9 Å structure captures the outward-facing nucleotide-bound state
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — IMAC was used for initial purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — [SEC](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) was used as a final purification step
- <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting Drop Vapor Diffusion</a> — Crystals were grown by sitting drop vapor diffusion
- <a href="/xray-mp-wiki/proteins/abc-transporters/sav1866/">Sav1866 Multidrug ABC Transporter</a> — Outward-open ABC transporter used for gating comparison
- <a href="/xray-mp-wiki/proteins/abc-transporters/mouse-p-glycoprotein/">Mouse P-glycoprotein (Pgp, ABCB1)</a> — Closest mammalian homolog
- <a href="/xray-mp-wiki/reagents/detergents/dm">n-Decyl-beta-D-Maltoside (DM)</a> — Detergent used for solubilization and purification
- <a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200 Increase SEC Resin</a> — Size-exclusion chromatography resin
