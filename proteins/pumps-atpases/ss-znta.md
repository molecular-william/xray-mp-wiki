---
title: "SsZntA (Shigella sonnei Zn2+-ATPase)"
created: 2026-06-09
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1107##S2052252515008969]
verified: false
---

# SsZntA (Shigella sonnei Zn2+-ATPase)

## Overview

SsZntA is a Zn2+-ATPase from Shigella sonnei, a P-type ATPase that functions
as a heavy metal transporter. It belongs to the P1B-type ATPase subfamily that
exports heavy metals such as Zn2+, Cd2+, and Pb2+ from the cytoplasm. The protein
was used as a model system for testing [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) (SFX)
at the LCLS XFEL as a method for ligand screening with P-type ATPases. Microcrystals
of SsZntA bound to the inhibitor aluminium tetrafluoride (AlF4-) were grown by
batch crystallization and diffracted to ~4 A resolution at the LCLS XFEL. However,
only 55 of ~280,000 collected diffraction images could be indexed due to the long
c axis of 320 A, preventing successful phasing by [Molecular Replacement](/xray-mp-wiki/methods/structure-determination/molecular-replacement/).


## Publications

### doi/10.1107##S2052252515008969

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4xou">4XOU</a></td>
      <td>4.0</td>
      <td>P422</td>
      <td>Shigella sonnei Zn2+-ATPase (SsZntA) expressed in E. coli C41 cells,
purified by Ni2+-NTA and gel filtration, crystallized with AlF4- inhibitor</td>
      <td>AlF4-</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41 cells
- **Construct**: SsZntA from Shigella sonnei expressed with 1 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at 20 C
- **Notes**: Cells resuspended in 50 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.6, 200 mM KCl, 20% [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/), 5 mM BME; lysed with high-pressure homogenizer

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
      <td>Differential centrifugation</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.6, 200 mM KCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 5 mM BME, 1 mM MgCl2 + --</td>
      <td>Membranes isolated by ultracentrifugation at 250,000g at 4 C for 5 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.6, 200 mM KCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 5 mM BME, 1 mM MgCl2 + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a></td>
      <td>Solubilization for 1 h at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (IMAC)</td>
      <td>Ni2+-NTA</td>
      <td>Buffer D (20 mM MOPS-KOH pH 6.8, 80 mM KCl, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 5 mM BME, 1 mM MgCl2, 0.15 mg/ml <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a>) + <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a></td>
      <td>Solid KCl and <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> added to final concentrations of 500 and 50 mM before loading</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography</td>
      <td>Superose 6 10/300 GL</td>
      <td>Buffer D + <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a></td>
      <td>Purified protein concentrated to 8 mg/ml</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Batch crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>8 mg/ml SsZntA in buffer D, supplemented with 2 mM AlF4-, 2 mM <a href="/xray-mp-wiki/reagents/additives/egta/">EGTA</a>, 10 uM N,N,N',N'-tetrakis-2-pyridylmethyl-ethylenediamine, 72x CMC <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM MOPS pH 6.8, 0.5 M lithium acetate, 15% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 2K MME, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 3% <a href="/xray-mp-wiki/reagents/additives/tert-butanol/">tert-Butanol</a>, 5% D-<a href="/xray-mp-wiki/reagents/additives/sorbitol/">Sorbitol</a>, 5 mM BME</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>19</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Rod-shaped microcrystals ~5 um in length, grown in clusters surrounded by amorphous precipitate. Suspension passed through 400 um syringe needle to homogenize before SFX injection. SFX data collected at LCLS, 6 keV, 120 Hz repetition rate using CSPAD detector. Only 0.3% indexing rate due to long c axis.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4xou">4XOU</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MEAAHSKSTEECLAYFGVSETTGLTPDQVKRHLEKYGHNELPAEEGKSLWELVI</span><span class="topo-membrane">EQFEDL</span></span>
<span class="topo-line"><span class="topo-membrane">LVRILLLAACISFVLAWF</span><span class="topo-outside">EEGEETI</span><span class="topo-membrane">TAFVEPFVILLILIANAIVG</span><span class="topo-inside">VWQERNAENAIEALK</span></span>
<span class="topo-line"><span class="topo-inside">EYEPEMGKVYRADRKSVQRIKARDIVPGDIVEVAVGDKVPADIRILSIKSTTLRVDQSIL</span></span>
<span class="topo-line"><span class="topo-inside">TGESVSVIKHTEPVPDPRAVNQDKKNMLFSGTNIAAGKALGIVATTGVSTEIGKIRDQMA</span></span>
<span class="topo-line"><span class="topo-inside">ATEQDKTPLQQKLDEF</span><span class="topo-membrane">GEQLSKVISLICVAVWLINI</span><span class="topo-outside">GHFNDPVHGGSWIRGA</span><span class="topo-membrane">IYYFKIAV</span></span>
<span class="topo-line"><span class="topo-membrane">ALAVAAIPEGLPA</span><span class="topo-inside">VITTCLALGTRRMAKKNAIVRSLPSVETLGCTSVICSDKTGTLTTNQ</span></span>
<span class="topo-line"><span class="topo-inside">MSVCKMFIIDKVDGDFCSLNEFSITGSTYAPEGEVLKNDKPIRSGQFDGLVELATICALC</span></span>
<span class="topo-line"><span class="topo-inside">NDSSLDFNETKGVYEKVGEATETALTTLVEKMNVFNTEVRNLSKVERANACNSVIRQLMK</span></span>
<span class="topo-line"><span class="topo-inside">KEFTLEFSRDRKSMSVYCSPAKSSRAAVGNKMFVKGAPEGVIDRCNYVRVGTTRVPMTGP</span></span>
<span class="topo-line"><span class="topo-inside">VKEKILSVIKEWGTGRDTLRCLALATRDTPPKREEMVLDDSSRFMEYETDLTFVGVVGML</span></span>
<span class="topo-line"><span class="topo-inside">DPPRKEVMGSIQLCRDAGIRVIMITGDNKGTAIAICRRIGIFGENEEVADRAYTGREFDD</span></span>
<span class="topo-line"><span class="topo-inside">LPLAEQREACRRACCFARVEPSHKSKIVEYLQSYDEITAMTGDGVNDAPALKKAEIGIAM</span></span>
<span class="topo-line"><span class="topo-inside">GSGTAVAKTASEMVLADDNFSTIVAAVEEGRAIYNNMKQ</span><span class="topo-membrane">FIRYLISSNVGEVVCIFLTAA</span></span>
<span class="topo-line"><span class="topo-membrane">L</span><span class="topo-outside">GLPE</span><span class="topo-membrane">ALIPVQLLWVNLVTDGLPATAL</span><span class="topo-inside">GFNPPDLDIMDRPPRSPKEPLISGW</span><span class="topo-membrane">LFFRYMAI</span></span>
<span class="topo-line"><span class="topo-membrane">GGYVGAATVGAA</span><span class="topo-outside">AWWFMYAEDGPGVTYHQLTHFMQCTEDHPHFEGLDCEIFEAPEPM</span><span class="topo-membrane">TMA</span></span>
<span class="topo-line"><span class="topo-membrane">LSVLVTIEMCNALNSL</span><span class="topo-inside">SENQSLMRMPPWVN</span><span class="topo-membrane">IWLLGSICLSMSLHFLILYV</span><span class="topo-outside">D</span><span class="topo-unknown">PLPMIF</span><span class="topo-outside">KLK</span></span>
<span class="topo-line"><span class="topo-outside">ALD</span><span class="topo-membrane">LTQWLMVLKISLPVIGLDEILKFI</span><span class="topo-inside">ARNYLEG</span></span>
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
      <td>54</td>
      <td>1</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>78</td>
      <td>55</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>105</td>
      <td>86</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>256</td>
      <td>106</td>
      <td>256</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>276</td>
      <td>257</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>292</td>
      <td>277</td>
      <td>292</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>313</td>
      <td>293</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>759</td>
      <td>314</td>
      <td>759</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>760</td>
      <td>781</td>
      <td>760</td>
      <td>781</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>782</td>
      <td>785</td>
      <td>782</td>
      <td>785</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>786</td>
      <td>807</td>
      <td>786</td>
      <td>807</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>808</td>
      <td>832</td>
      <td>808</td>
      <td>832</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>833</td>
      <td>852</td>
      <td>833</td>
      <td>852</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>853</td>
      <td>897</td>
      <td>853</td>
      <td>897</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>898</td>
      <td>916</td>
      <td>898</td>
      <td>916</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>917</td>
      <td>930</td>
      <td>917</td>
      <td>930</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>950</td>
      <td>931</td>
      <td>950</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>951</td>
      <td>951</td>
      <td>951</td>
      <td>951</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>952</td>
      <td>957</td>
      <td>952</td>
      <td>957</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>958</td>
      <td>963</td>
      <td>958</td>
      <td>963</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>964</td>
      <td>987</td>
      <td>964</td>
      <td>987</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>988</td>
      <td>994</td>
      <td>988</td>
      <td>994</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### SFX feasibility for recombinant heavy metal P-type ATPase

SsZntA served as a model for testing SFX with recombinantly expressed P-type ATPase microcrystals. Despite the very low indexing rate (0.3%), the microcrystals diffracted to ~4 A resolution, demonstrating that SFX is feasible for bacterial P-type ATPase ligand complexes. However, the long c axis of 320 A in the P422 space group remains a challenge for SFX data processing with CrystFEL.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/p-type-atpase/">P-type ATPase Family</a> — SsZntA belongs to the P1B-type (heavy metal transporting) ATPase subfamily
- <a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/">Serial Femtosecond Crystallography (SFX)</a> — SFX at LCLS XFEL used for structure determination attempt
- <a href="/xray-mp-wiki/proteins/pumps-atpases/serca1a/">SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)</a> — SERCA1a is a related P-type ATPase studied in the same SFX ligand screening project
- <a href="/xray-mp-wiki/proteins/pumps-atpases/sulfitobacter-scoat/">sCoaT (Co2+/Zn2+-transporting PIB-4-ATPase)</a> — Related PIB-ATPase; sCoaT structures used SsZntA as MR search model
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/egta/">EGTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
