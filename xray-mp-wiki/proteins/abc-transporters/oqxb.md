---
title: "OqxB efflux pump from Klebsiella pneumoniae"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-021-25679-0]
verified: regex
uniprot_id: ['P20789', 'P62873', 'P63096', 'P63211']
---

# OqxB efflux pump from Klebsiella pneumoniae

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P20789">UniProt: P20789</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P62873">UniProt: P62873</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P63096">UniProt: P63096</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P63211">UniProt: P63211</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

OqxB is a Resistance-Nodulation-Division (RND) efflux pump from *Klebsiella pneumoniae* that contributes to multidrug antibiotic resistance. OqxB underwent horizontal gene transfer and is now found in other Gram-negative bacterial pathogens including *Escherichia coli*, *Enterobacter cloacae*, and *Salmonella* spp. It confers resistance against fluoroquinolones, nitrofurantoin, quinoxalines, tigecycline, and [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol). The crystal structure at 1.85 Angstrom resolution reveals a symmetric trimer wherein all three protomers adopt a binding/tight conformation, unlike the asymmetric trimers observed in other RND pumps ([ACRB](/xray-mp-wiki/proteins/acrB), [MEXB](/xray-mp-wiki/proteins/mexB)). Each protomer contains two bound [DDM](/xray-mp-wiki/reagents/detergents/ddm) molecules in the substrate-binding pocket. A unique charged arginine residue R157 in the substrate-binding pocket, absent in [ACRB](/xray-mp-wiki/proteins/acrB) and [MEXB](/xray-mp-wiki/proteins/mexB), forms hydrogen bonds with substrates and is critical for fluoroquinolone binding and efflux. The longer gate loop (g-loop) with two proline residues and a unique phenylalanine cage architecture distinguish OqxB from related pumps. Functional complementation assays demonstrated 8- to 16-fold increased MIC for fluoroquinolones upon OqxB expression, and the R157A mutant showed 4- to 8-fold improved MIC, validating the structural predictions.


## Publications

### doi/10.1038##s41467-021-25679-0

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7l0q">7L0Q</a></td>
      <td>1.85</td>
      <td>P 65 2 2</td>
      <td>OqxB (residues 1-977) symmetric trimer</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> (2 molecules per protomer)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: OqxB (residues 1-977) with C-terminal hexa-histidine tag, cloned into modified pET-22b vector
- **Notes**: Expressed in E. coli C43(DE3) at 25 C for 8 hours with 0.1 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) induction at A600nm of 0.6

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
      <td>1</td>
      <td>Cell lysis by Microfluidizer</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 7.0, 0.5 mM Na-<a href="/xray-mp-wiki/reagents/additives/edta">EDTA</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/mgcl2">MGCL2</a></td>
      <td>3 passes at 15,000 psi. Membrane fraction collected by ultracentrifugation</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Solubilization</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 7.0, 300 mM NaCl + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Solubilized from membrane fraction</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Affinity chromatography (Ni-NTA)</td>
      <td>Ni-NTA Superflow (Qiagen)</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 7.0, 300 mM NaCl, 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag">Polyhistidine Tag (His6)</a> purification</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Size-exclusion chromatography</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 150 mM NaCl + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Final polishing step for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, sitting drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>OqxB purified in <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> at ~10 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a> pH 5.5, 0.1 M Li2SO4, 0.1 M NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/mgcl2">MGCL2</a>, 34% <a href="/xray-mp-wiki/reagents/additives/peg400">PEG400</a>, 5 mM <a href="/xray-mp-wiki/reagents/ligands/atp">ATP</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Symmetric trimer structure with <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> molecules bound in substrate pocket</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7l0q">7L0Q</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GPGSGP</span><span class="topo-outside">NSDLDVNTDI</span><span class="topo-membrane">YSKVLVTAIYLALFVVGTVGNSV</span><span class="topo-inside">TLFTLAR</span><span class="topo-unknown">KKSLQS</span><span class="topo-inside">LQSTVDYYLGS</span><span class="topo-membrane">LALSDLLILLLAMPVELYNFIWV</span><span class="topo-outside">HHPW</span><span class="topo-membrane">AFGDAGCRGYYFLRDACTYATALNVV</span><span class="topo-inside">SLSV</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ERYLAICHPFKAKTLMSRSRTKKFIS</span><span class="topo-membrane">AIWLASALLAIPMLFTMGL</span><span class="topo-outside">QNLSGDGTHPGGLVC</span><span class="topo-membrane">TPIVDTATLKVVIQVNTFMSFLFPMLVAS</span><span class="topo-inside">ILNTVIANKLTVMVHQAA</span><span class="topo-unknown">F</span><span class="topo-inside">NMTIEPGRVQAL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330      </span>
<span class="topo-line"><span class="topo-inside">RRGVLVLRA</span><span class="topo-membrane">VVIAFVVCWLPYHVRRLMFCYI</span><span class="topo-outside">SDEQWTTFLFDF</span><span class="topo-membrane">YHYFYMLTNALVYVSAAINPIL</span><span class="topo-inside">YNLVS</span><span class="topo-unknown">ANFRQVFLSTL</span><span class="topo-inside">A</span><span class="topo-unknown">CLCPGTRELEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>7</td>
      <td>16</td>
      <td>52</td>
      <td>61</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>39</td>
      <td>62</td>
      <td>84</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>46</td>
      <td>85</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>63</td>
      <td>98</td>
      <td>108</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>86</td>
      <td>109</td>
      <td>131</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>90</td>
      <td>132</td>
      <td>135</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>116</td>
      <td>136</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>146</td>
      <td>162</td>
      <td>191</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>165</td>
      <td>192</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>166</td>
      <td>180</td>
      <td>211</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>209</td>
      <td>226</td>
      <td>254</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>210</td>
      <td>227</td>
      <td>255</td>
      <td>272</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>249</td>
      <td>292</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>271</td>
      <td>313</td>
      <td>334</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>272</td>
      <td>283</td>
      <td>335</td>
      <td>346</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>284</td>
      <td>305</td>
      <td>347</td>
      <td>368</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>310</td>
      <td>369</td>
      <td>373</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>321</td>
      <td>374</td>
      <td>384</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>322</td>
      <td>322</td>
      <td>385</td>
      <td>385</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7l0q">7L0Q</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">GCTLSAEDKAAVERSKMIDRNLREDGEKAAREVKLLLLGAGESGKSTIVKQMKII</span><span class="topo-unknown">HEAGYSE</span><span class="topo-inside">EECKQYKAVVYSNTIQSIIAIIRAMGRLKIDFGDSARADDARQLFVLAGAAEEGFMT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AELAGVIKRLWKDSGVQACFNRSREYQLNDSAAYYLNDLDRIAQPNYIPTQQDVLRT</span><span class="topo-unknown">RVKT</span><span class="topo-inside">TGIVETHFTFKDLHFKMFDVGGQRSERKKWIHCFEGVTAIIFCVALSDYDLVL</span><span class="topo-unknown">AEDEE</span><span class="topo-inside">M</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350    </span>
<span class="topo-line"><span class="topo-inside">NRMHESMKLFDSICNNKWFTDTSIILFLNKKDLFEEKIKKSPLTICYPEYAGSNTYEEAAAYIQCQFEDLNKRKDTKEIYTHFTCATDTKNVQFVFDAVTDVIIKNNLKDCGLF</span></span>
<details class="topo-details"><summary>Topology coordinates (4 regions)</summary>
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
      <td>56</td>
      <td>2</td>
      <td>56</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>177</td>
      <td>64</td>
      <td>177</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>234</td>
      <td>182</td>
      <td>234</td>
      <td>Inside</td>
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
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7l0q">7L0Q</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRGSHHHHHHHHHHLEVLFQGPSELDQLRQEAEQLKNQIRDARKACADAT</span><span class="topo-inside">LSQITNNIDPVGRIQMRTRRTLRGHLAKIYAMHWGTDSRLLVSASQDGKLIIWDSYTTNKVHAIPLRSSW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">VMTCAYAPSGNYVACGGLDNICSIYNLKTREGNVRVSRELAGHTGYLSCCRFLDDNQIVTSSGDTTCALWDIETGQQTTTFTGHTGDVMSLSLAPDTRLFVSGACDASAKLWDVREGMCR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">QTFTGHESDINAICFFPNGNAFATGSDDATCRLFDLRADQELMTYSHDNIICGITSVSFSKSGRLLLAGYDDFNCNVWDALKADRAGVLAGHDNRVSCLGVTDDGMAVATGSWDSFLKIW</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-inside">N</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>51</td>
      <td>361</td>
      <td>30</td>
      <td>340</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7l0q">7L0Q</a> — Chain G (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80   </span>
<span class="topo-line"><span class="topo-unknown">MYPYDVPDYAPVINIEDLTEKDKLKMEVDQLKKEVTLER</span><span class="topo-inside">MLVSKCCEEVRDYVEERSGEDPLVKGIPEDKNPFKELKG</span><span class="topo-unknown">GCVIS</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>40</td>
      <td>78</td>
      <td>31</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Unique charged residue R157 in substrate-binding pocket

R157 is a unique positively charged arginine residue in the OqxB substrate-binding pocket that is absent in related pumps [ACRB](/xray-mp-wiki/proteins/acrB) and [MEXB](/xray-mp-wiki/proteins/mexB) (which have a small hydrophilic serine at the equivalent position). R157 forms hydrogen bond interactions with the [DDM](/xray-mp-wiki/reagents/detergents/ddm) molecule and is proposed to interact with zwitterionic fluoroquinolone antibiotics through its guanidino side chain. Molecular docking and MD simulations showed that ciprofloxacin interacts with R157, forming stable hydrogen bonds (>80% occupancy) between the fluoroquinolone carboxyl and carbonyl groups. The R157A mutation reduced efflux liability for fluoroquinolones by 4- to 8-fold, confirming its critical role in drug binding and efflux.

### Extended gate loop and phenylalanine cage

The OqxB gate loop (g-loop) is longer by two residues (16 vs. 14) than [ACRB](/xray-mp-wiki/proteins/acrB) and [MEXB](/xray-mp-wiki/proteins/mexB), containing two proline residues (P619 and P630) on either side of the loop. The conserved phenylalanine residues (F615 and F617) in [ACRB](/xray-mp-wiki/proteins/acrB) and [MEXB](/xray-mp-wiki/proteins/mexB) g-loops are replaced with L621 and A623 in OqxB. This is compensated by F626, which swings back toward the substrate-binding pocket, contributing to the unique phenylalanine cage architecture. These structural differences are responsible for the distinct binding mode of [DDM](/xray-mp-wiki/reagents/detergents/ddm) molecules in OqxB compared to [MEXB](/xray-mp-wiki/proteins/mexB).


## Cross-References

- <a href="/xray-mp-wiki/reagents/additives/edta">EDTA</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/antibiotics/chloramphenicol">Chloramphenicol</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/iptg">IPTG</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag">Polyhistidine Tag (His6)</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/ligands/atp">ATP</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/peg400">PEG400</a> — Entity mentioned in text
