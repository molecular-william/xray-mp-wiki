---
title: "ATP11C-CDC50A (Human Plasma Membrane Phospholipid Flippase)"
created: 2020-06-03
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1074##jbc.RA120.014144]
verified: false
---

# ATP11C-CDC50A (Human Plasma Membrane Phospholipid Flippase)

## Overview

ATP11C is a member of the P4-ATPase family that functions as an aminophospholipid-specific

## Publications

### doi/10.1074##jbc.RA120.014144

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6lkn">6LKN</a></td>
      <td>3.9</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [BacMam](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) expression in Expi293 cells
- **Construct**: ATP11C (ΔN7/ΔC38) with N-terminal Flag-EGFP-His₆-TEV tag; CDC50A (N190Q/S292W)

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
      <td>1. Cell harvesting and solubilization</td>
      <td>Direct solubilization</td>
      <td>—</td>
      <td>40 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a><a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 6.5, 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 2 mM Mg(CH₃COO)₂, 1 mM <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/egta/">EGTA</a>, protease inhibitor cocktail + 1.5% (w/v) n-Decyl-β-D-Maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>Cells solubilized on ice for 20 min. Insoluble material removed by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> at 200,000×g for 1 h</td>
    </tr>
    <tr>
      <td>2. Anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">Flag</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Anti-<a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">Flag</a> M2 affinity resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a><a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 6.5, 200 mM NaCl, 2 mM Mg(CH₃COO)₂, 1 mM ATP, 0.1% DM, 0.5 mM BeSO₄, 1.5 mM NaF</td>
      <td>Resin washed with 20 column volumes; eluted with <a href="/xray-mp-wiki/reagents/additives/flag-peptide/">Flag peptide</a> or by <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV protease</a> cleavage</td>
    </tr>
    <tr>
      <td>3. Deglycosylation and <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Gel Filtration</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a><a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 6.5, 200 mM NaCl, 2 mM Mg(CH₃COO)₂, 0.5 mM BeSO₄, 1.5 mM NaF, 0.1% DM</td>
      <td>Endoglycosidase treatment before SEC to remove excess glycans. Fractions containing the ATP11C-CDC50A complex were pooled</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion</a>, <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">sitting drop</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified ATP11C-CDC50A at ~10 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a><a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 6.5, 50 mM NaCl, 5 mM MgCl₂, 0.5 mM BeSO₄, 1.5 mM NaF, 0.1 mg/mL DOPS (dioleoylphosphatidylserine)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 14–17% <a href="/xray-mp-wiki/reagents/additives/peg-4000/">PEG 4000</a>, 0.4 M <a href="/xray-mp-wiki/reagents/additives/magnesium-sulfate/">MgSO₄</a>, 2–5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">β-Mercaptoethanol</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 °C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals harvested in reservoir solution supplemented with 4 mg/mL DOPS, 2% C₁₂E₈, 1 mM ADP, 0.5 mM BeSO₄, 1.5 mM NaF; flash frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein was reconstituted with DOPC lipids (lipid-to-protein ratio 0.2) and C₁₂E₈ detergent before crystallization. Crystals were plate-like, 800 × 500 × 50 µm. Space group P2₁2₁2₁. Structure solved at 3.9 Å by MR using ATP8A1 E2P structure (PDB 6K7L). Data merged from 1,588 crystals. PDB 6LKN.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6lkn">6LKN</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MFRRSLNRFCAGEEKRVGTRTVFVGNH</span><span class="topo-outside">PVSETEAYIAQRFCDNRIVSSKYTLWNFLPKN</span><span class="topo-membrane">L</span></span>
<span class="topo-line"><span class="topo-membrane">FEQFRRIANFYFLIIFLVQVT</span><span class="topo-inside">VDTPT</span><span class="topo-membrane">SPVTSGLPLFFVITVTAI</span><span class="topo-outside">KQGYEDWLRHRADNEV</span></span>
<span class="topo-line"><span class="topo-outside">NKSTVYIIENAKRVRKESEKIKVGDVVEVQADETFPCDLILLSSCTTDGTCYVTTASLDG</span></span>
<span class="topo-line"><span class="topo-outside">ESNCKTHYAVRDTIALCTAESIDTLRAAIECEQPQPDLYKFVGRINIYSNSLEAVARSLG</span></span>
<span class="topo-line"><span class="topo-outside">PENLLLKGATLKNTEKIYGVAVYTGMETKMALNYQGKSQKRSAVE</span><span class="topo-membrane">KSINAFLIVYLFILL</span></span>
<span class="topo-line"><span class="topo-membrane">TKAAVC</span><span class="topo-inside">TTLKYVWQSTPYNDEPWYNQKTQKERETLKVLKMFTDF</span><span class="topo-membrane">LSFMVLFNFIIPVSMY</span></span>
<span class="topo-line"><span class="topo-membrane">VTVEM</span><span class="topo-outside">QKFLGSFFISWDKDFYDEEINEGALVNTSDLNEELGQVDYVFTDKTGTLTENSME</span></span>
<span class="topo-line"><span class="topo-outside">FIECCIDGHKYKGVTQEVDGLSQTDGTLTYFDKVDKNREELFLRALCLCHTVEIKTNDAV</span></span>
<span class="topo-line"><span class="topo-outside">DGATESAELTYISSSPDEIALVKGAKRYGFTFLGNRNGYMRVENQRKEIEEYELLHTLNF</span></span>
<span class="topo-line"><span class="topo-outside">DAVRRRMSVIVKTQEGDILLFCKGADSAVFPRVQNHEIELTKVHVERNAMDGYRTLCVAF</span></span>
<span class="topo-line"><span class="topo-outside">KEIAPDDYERINRQLIEAKMALQDREEKMEKVFDDIETNMNLIGATAVEDKLQDQAAETI</span></span>
<span class="topo-line"><span class="topo-outside">EALHAAGLKVWVLTGDKMETAKSTCYACRLFQTNTELLELTTKTIEESERKEDRLHELLI</span></span>
<span class="topo-line"><span class="topo-outside">EYRKKLLHEFPKSTRSFKKAWTEHQEYGLIIDGSTLSLILNSSQDSSSNNYKSIFLQICM</span></span>
<span class="topo-line"><span class="topo-outside">KCTAVLCCRMAPLQKAQIVRMVKNLKGSPITLSIGDGANDVSMILESHVGIGIKGKEGRQ</span></span>
<span class="topo-line"><span class="topo-outside">AARNSDYSVPKFKHLKKLLLAHGHLYYVRIA</span><span class="topo-membrane">HLVQYFFYKNLCFILPQFLY</span><span class="topo-inside">QFFCGFSQQ</span></span>
<span class="topo-line"><span class="topo-inside">P</span><span class="topo-membrane">LYDAAYLTMYNICFTSLPILAY</span><span class="topo-outside">SLLEQHINIDTLTSDPRLYMKISGNAML</span><span class="topo-membrane">QLGPFLYWT</span></span>
<span class="topo-line"><span class="topo-membrane">FLAAFEGTVFFFGT</span><span class="topo-inside">YFLFQTASLEENGKVYGNWTFG</span><span class="topo-membrane">TIVFTVLVFTVTLKLALDT</span><span class="topo-outside">RFWTW</span></span>
<span class="topo-line"><span class="topo-outside">I</span><span class="topo-membrane">NHFVIWGSLAFYVFFSFFWGGII</span><span class="topo-inside">WPFLKQQRMYF</span><span class="topo-unknown">VFAQML</span><span class="topo-inside">SSV</span><span class="topo-membrane">STWLAIILLIFISLFP</span></span>
<span class="topo-line"><span class="topo-membrane">EILLIVL</span><span class="topo-outside">KNVR</span><span class="topo-unknown">RRSARRNLSCRRASDSLSARPSVRPLLLRTFSDESNVL</span></span>
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
      <td>28</td>
      <td>59</td>
      <td>28</td>
      <td>59</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>81</td>
      <td>60</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>86</td>
      <td>82</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>104</td>
      <td>87</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>285</td>
      <td>105</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>306</td>
      <td>286</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>344</td>
      <td>307</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>365</td>
      <td>345</td>
      <td>365</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>366</td>
      <td>871</td>
      <td>366</td>
      <td>871</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>872</td>
      <td>891</td>
      <td>872</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>901</td>
      <td>892</td>
      <td>901</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>902</td>
      <td>923</td>
      <td>902</td>
      <td>923</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>924</td>
      <td>951</td>
      <td>924</td>
      <td>951</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>952</td>
      <td>974</td>
      <td>952</td>
      <td>974</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>975</td>
      <td>996</td>
      <td>975</td>
      <td>996</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>997</td>
      <td>1015</td>
      <td>997</td>
      <td>1015</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1016</td>
      <td>1021</td>
      <td>1016</td>
      <td>1021</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1022</td>
      <td>1044</td>
      <td>1022</td>
      <td>1044</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1045</td>
      <td>1055</td>
      <td>1045</td>
      <td>1055</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1056</td>
      <td>1061</td>
      <td>1056</td>
      <td>1061</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1062</td>
      <td>1064</td>
      <td>1062</td>
      <td>1064</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1065</td>
      <td>1087</td>
      <td>1065</td>
      <td>1087</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1088</td>
      <td>1091</td>
      <td>1088</td>
      <td>1091</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6lkn">6LKN</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MAMNYNAKDEVDGGPPCAPGGTAKTR</span><span class="topo-outside">RPDNTAFKQQRLPAWQPILTA</span><span class="topo-membrane">GTVLPIFFIIGLI</span></span>
<span class="topo-line"><span class="topo-membrane">FIPIGIG</span><span class="topo-inside">IFVTSNNIREIEIDYTGTEPSSPCNKCLSPDVTPCFCTINFTLEKSFEGNVFM</span></span>
<span class="topo-line"><span class="topo-inside">YYGLSNFYQNHRRYVKSRDDSQLNGDSSALLNPSKECEPYRRNEDKPIAPCGAIANSMFN</span></span>
<span class="topo-line"><span class="topo-inside">DTLELFLIGQDSYPIPIALKKKGIAWWTDKNVKFRNPPGGDNLEERFKGTTKPVNWLKPV</span></span>
<span class="topo-line"><span class="topo-inside">YMLDSDPDNNGFINEDFIVWMRTAALPTFRKLYRLIERKSDLHPTLPAGRYWLNVTYNYP</span></span>
<span class="topo-line"><span class="topo-inside">VHYFDGRKRMILSTISWMGGKNPFL</span><span class="topo-membrane">GIAYIAVGSISFLLGVVLLVI</span><span class="topo-outside">NHKY</span><span class="topo-unknown">RNSSNTADIT</span></span>
<span class="topo-line"><span class="topo-unknown">I</span></span>
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
      <td>27</td>
      <td>47</td>
      <td>27</td>
      <td>47</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>67</td>
      <td>48</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>325</td>
      <td>68</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>346</td>
      <td>326</td>
      <td>346</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>347</td>
      <td>350</td>
      <td>347</td>
      <td>350</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights


## Cross-References

- <a href="/xray-mp-wiki/concepts/p-type-atpase-mechanism/">P-type ATPase Mechanism</a> — ATP11C is a P4-ATPase flippase
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/phosphoenzyme-e2p-state/">Phosphoenzyme E2P State</a> — ATP11C-CDC50A trapped in E2P-like state
