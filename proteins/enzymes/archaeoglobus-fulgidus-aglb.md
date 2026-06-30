---
title: "Archaeoglobus fulgidus AglB (AfAglB)"
created: 2026-05-29
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1021##acs.biochem.6b01089, doi/10.1073##pnas.1314195110, doi/10.1038##s42003-021-02473-8]
verified: false
---

# Archaeoglobus fulgidus AglB (AfAglB)

## Overview

Archaeoglobus fulgidus AglB (AfAglB) is the catalytic subunit of the archaeal oligosaccharyltransferase (OST), a single-subunit membrane enzyme that transfers an oligosaccharide chain to Asn residues in the Asn-X-Ser/Thr sequon of substrate proteins. AfAglB comprises 13 transmembrane helices in the N-terminal region and a C-terminal globular domain. Despite low sequence identity (<20%) to eubacterial PglB homologs, AfAglB shares a highly conserved catalytic architecture including the [Carboxylate Dyad](/xray-mp-wiki/concepts/enzyme-mechanisms/carboxylate-dyad/) (Asp47 and Glu360 with a metal ion) that activates the acceptor Asn side chain for nucleophilic attack on the lipid-linked oligosaccharide donor.

## Publications

### doi/10.1021##acs.biochem.6b01089

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5gmy">5GMY</a></td>
      <td>3.5 A</td>
      <td>Not specified in paper</td>
      <td>AfAglB G617C mutant cross-linked with acceptor peptide Ac-RYNVTAC-NH2 via engineered disulfide bond at position 617</td>
      <td>Acceptor peptide (Ac-RYNVTAC-NH2) containing N-glycosylation sequon Asn-Val-Thr</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43 (DE3) cells
- **Construct**: AfAglB G617C mutant (cysteine introduced at position 617 for peptide tethering); native AfAglB lacks cysteine residues

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
      <td>Cell disruption</td>
      <td>Sonication of E. coli C43 (DE3) membrane fractions</td>
      <td>--</td>
      <td>TS buffer (50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a>, pH 8.0, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>) + --</td>
      <td>Cells grown at 310 K in Terrific Broth with 100 mg/L <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a>; induced with 0.5 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> at 298 K</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td><a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">Ultracentrifugation</a> at 100,000 x g for 2 h</td>
      <td>--</td>
      <td>TS buffer (50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a>, pH 8.0, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>) + --</td>
      <td>Pellets containing membrane fractions collected</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization of membrane pellets</td>
      <td>--</td>
      <td>TS buffer (50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a>, pH 8.0, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>) + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>-solubilized protein recovered after <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> at 100,000 x g for 1 h</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Nickel Sepharose High Performance resin</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Nickel Sepharose</a> High Performance (GE Healthcare)</td>
      <td>TS buffer (50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a>, pH 8.0, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>) containing 0.1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>His-tagged recombinant protein purified by <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
    </tr>
  </tbody>
</table>

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
      <td>Gel filtration chromatography</td>
      <td>Gel filtration in <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
      <td>Not specified</td>
      <td>Not specified in paper + 0.06% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
      <td>Performed for crystallization; G617C mutant purified by gel filtration</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging drop vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>AfAglB G617C mutant cross-linked with acceptor peptide Ac-RYNVTAC-NH2, concentrated to 15 mg/ml, dialyzed against 10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a>, pH 7.5, 0.1 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 0.06% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.01 M <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride</a>, 0.1 M Bis-<a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a>, pH 6.5, 22% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg-550-mme/">PEG 550 MME</a>, 5% (v/v) Jeffamine M-600, pH 7.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293 K</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>0.01 M <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride</a>, 0.1 M Bis-<a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a>, pH 6.5, 30% (v/v) <a href="/xray-mp-wiki/reagents/additives/peg-550-mme/">PEG 550 MME</a>, 0.06% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>; cryocooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Initial screening with MemGold I, MemGold II, and MemStart+MemSys Kits (Molecular Dimensions). X-ray data collected at SPring-8 BL44XU to 3.50 A resolution. Solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using apo AfAglB (3WAK) as search model. R_work/R_free = 20.7%/27.8%. Calculated solvent content 63.2% (Vm = 3.35 A^3/Da).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5gmy">5GMY</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQNA</span><span class="topo-outside">E</span><span class="topo-membrane">SWFKKYWHLSVLVIAALI</span><span class="topo-inside">SVKLRILNPWNSVFTWTVRLGGNDPWYYYRLIENTIHNFPHRIWFDPFTYYPYGSYTHFG</span><span class="topo-unknown">PFLVYLGSIAGII</span><span class="topo-inside">FSATSGESLRAVLAFIPAIGGV</span><span class="topo-membrane">LA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ILPVYLLTREVF</span><span class="topo-outside">D</span><span class="topo-membrane">KRAAVIAAFLIAIV</span><span class="topo-inside">PGQFLQRSILGFNDHHIWE</span><span class="topo-membrane">AFWQVSALGTFLLAYNRW</span><span class="topo-outside">KGHDLSHNL</span><span class="topo-membrane">TARQMAYPVIAGITIGLYV</span><span class="topo-inside">LSWGAG</span><span class="topo-membrane">FIIAPIILAFMFFAFVL</span><span class="topo-outside">AGFVN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ADRKN</span><span class="topo-membrane">LSLVAVVTFAVSALIYLP</span><span class="topo-inside">FAFNYPGFSTIFYSP</span><span class="topo-membrane">FQLLVLLGSAVIAAAFYQ</span><span class="topo-outside">IEKWNDVGFFERVGLGRKGMP</span><span class="topo-membrane">LAVIVLTALIMGLFFVI</span><span class="topo-unknown">SPDFARNLLSVVRVVQ</span><span class="topo-inside">PKGGALTIAE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VYPFFFTHNGEFTL</span><span class="topo-unknown">TNAVLHF</span><span class="topo-membrane">GALFFFGMAGILYSAYRFL</span><span class="topo-outside">KRRS</span><span class="topo-membrane">FPEMALLIWAIAMFIALW</span><span class="topo-inside">GQNRFAYY</span><span class="topo-membrane">FAAVSAVYSALALSVVFDKL</span><span class="topo-outside">HLYRALENAIGARNKLS</span><span class="topo-membrane">YFRVAFALLIALA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">AIYPT</span><span class="topo-inside">YILADAQSSYAGGPNKQWYDALTWMRENTPDGEKYDEYYLQLYPTPQSNKEPFSYPFETYGVISWWDYGHWIEAVAHRMPIANPFQAGIGNKYNNVPGASSFFTAENESYAEFVA</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">EKLNVKYVVSDIEMETCKYYAMAVWAEGDLPLAEKYYGGYFYYSPTGTFGYANSQWDIPLNSIIIPLRIPSELYYSTMEAKLHLFDGSGLSHYRMIYESDYPAEWKSYSSQVNLNNESQV</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">LQTALYEAVMRARYGVSPTMGTQEVLYKYAYTQLYEKKMGIPVKIAPSGYVKIFERVKGAVVTGKVSANVTEVSVNATIKTNQNRTFEYWQTVEVKNGTYTVVLPYSHNSDYPVKPITPY</span></span>
<span class="topo-ruler">       850       860       870     </span>
<span class="topo-line"><span class="topo-inside">HIKAGNVVKEITIYESQVQNGEIIQLDL</span><span class="topo-unknown">ELALVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>23</td>
      <td>6</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>83</td>
      <td>24</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>96</td>
      <td>84</td>
      <td>96</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>97</td>
      <td>118</td>
      <td>97</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>132</td>
      <td>119</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>133</td>
      <td>133</td>
      <td>133</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>147</td>
      <td>134</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>166</td>
      <td>148</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>184</td>
      <td>167</td>
      <td>184</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>185</td>
      <td>193</td>
      <td>185</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>194</td>
      <td>212</td>
      <td>194</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>218</td>
      <td>213</td>
      <td>218</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>235</td>
      <td>219</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>236</td>
      <td>245</td>
      <td>236</td>
      <td>245</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>246</td>
      <td>263</td>
      <td>246</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>278</td>
      <td>264</td>
      <td>278</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>296</td>
      <td>279</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>317</td>
      <td>297</td>
      <td>317</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>318</td>
      <td>334</td>
      <td>318</td>
      <td>334</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>351</td>
      <td>374</td>
      <td>351</td>
      <td>374</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>381</td>
      <td>375</td>
      <td>381</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>382</td>
      <td>400</td>
      <td>382</td>
      <td>400</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>401</td>
      <td>404</td>
      <td>401</td>
      <td>404</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>405</td>
      <td>422</td>
      <td>405</td>
      <td>422</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>430</td>
      <td>423</td>
      <td>430</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>431</td>
      <td>450</td>
      <td>431</td>
      <td>450</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>451</td>
      <td>467</td>
      <td>451</td>
      <td>467</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>468</td>
      <td>485</td>
      <td>468</td>
      <td>485</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>868</td>
      <td>486</td>
      <td>868</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1073##pnas.1314195110

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3wak">3WAK</a></td>
      <td>Not specified in paper</td>
      <td>Not specified in paper</td>
      <td>Apo AfAglB (wild-type, full-length)</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43 (DE3) cells
- **Construct**: AfAglB G617C mutant (cysteine introduced at position 617 for peptide tethering); native AfAglB lacks cysteine residues

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3wak">3WAK</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQNA</span><span class="topo-outside">ESW</span><span class="topo-membrane">FKKYWHLSVLVIAALIS</span><span class="topo-inside">VKLRILNPWNSVFTWTVRLGGNDPWYYYRLIENTIHNFPHRIWFDPFTYYPYGSYTHFG</span><span class="topo-unknown">PFLVYLGSIAGII</span><span class="topo-inside">FSATSGESLRAVLAFIPAIGG</span><span class="topo-membrane">VLA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ILPVYLLTREVFDK</span><span class="topo-outside">R</span><span class="topo-membrane">AAVIAAFLIAIV</span><span class="topo-inside">PGQFLQRSILGFNDHHIWE</span><span class="topo-membrane">AFWQVSALGTFLLAY</span><span class="topo-outside">NRWKGHDLSHNLTARQM</span><span class="topo-membrane">AYPVIAGITIGLYV</span><span class="topo-inside">LSWGAG</span><span class="topo-membrane">FIIAPIILAFMFFA</span><span class="topo-outside">FVLAGFVN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ADRKNL</span><span class="topo-membrane">SLVAVVTFAVSALIYL</span><span class="topo-inside">PFAFNYPGFSTIFYSPFQ</span><span class="topo-membrane">LLVLLGSAVIAAAF</span><span class="topo-outside">YQIEKWNDVGFFERVGLGRKGMPLAV</span><span class="topo-membrane">IVLTALIMGLFFVIS</span><span class="topo-inside">PD</span><span class="topo-unknown">FARNLLSVV</span><span class="topo-inside">RVVQPKGGALTIAE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VYPFFFTHNGEFTL</span><span class="topo-unknown">TNAVLHF</span><span class="topo-membrane">GALFFFGMAGILYSAY</span><span class="topo-outside">RFLKRRSFP</span><span class="topo-membrane">EMALLIWAIAMFIAL</span><span class="topo-inside">WGQNRFAYY</span><span class="topo-membrane">FAAVSAVYSALALSVVF</span><span class="topo-outside">DKLHLYRALENAIGARNKLSYF</span><span class="topo-membrane">RVAFALLIALA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">AIYPTY</span><span class="topo-inside">ILADAQSSYAGGPNKQWYDALTWMRENTPDGEKYDEYYLQLYPTPQSNKEPFSYPFETYGVISWWDYGHWIEAVAHRMPIANPFQAGIGNKYNNVPGASSFFTAENESYAEFVA</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">EKLNVKYVVSDIEMETGKYYAMAVWAEGDLPLAEKYYGGYFYYSPTGTFGYANSQWDIPLNSIIIPLRIPSELYYSTMEAKLHLFDGSGLSHYRMIYESDYPAEWKSYSSQVNLNNESQV</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">LQTALYEAVMRARYGVSPTMGTQEVLYKYAYTQLYEKKMGIPVKIAPSGYVKIFERVKGAVVTGKVSANVTEVSVNATIKTNQNRTFEYWQTVEVKNGTYTVVLPYSHNSDYPVKPITPY</span></span>
<span class="topo-ruler">       850       860       870     </span>
<span class="topo-line"><span class="topo-inside">HIKAGNVVKEITIYESQVQNGEIIQLDL</span><span class="topo-unknown">ELALVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (34 regions)</summary>
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
      <td>7</td>
      <td>5</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>24</td>
      <td>8</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>83</td>
      <td>25</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>96</td>
      <td>84</td>
      <td>96</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>97</td>
      <td>117</td>
      <td>97</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>134</td>
      <td>118</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>135</td>
      <td>135</td>
      <td>135</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>136</td>
      <td>147</td>
      <td>136</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>166</td>
      <td>148</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>181</td>
      <td>167</td>
      <td>181</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>182</td>
      <td>198</td>
      <td>182</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>212</td>
      <td>199</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>213</td>
      <td>218</td>
      <td>213</td>
      <td>218</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>232</td>
      <td>219</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>246</td>
      <td>233</td>
      <td>246</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>247</td>
      <td>262</td>
      <td>247</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>263</td>
      <td>280</td>
      <td>263</td>
      <td>280</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>294</td>
      <td>281</td>
      <td>294</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>295</td>
      <td>320</td>
      <td>295</td>
      <td>320</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>321</td>
      <td>335</td>
      <td>321</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>336</td>
      <td>337</td>
      <td>336</td>
      <td>337</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>338</td>
      <td>346</td>
      <td>338</td>
      <td>346</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>347</td>
      <td>374</td>
      <td>347</td>
      <td>374</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>381</td>
      <td>375</td>
      <td>381</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>382</td>
      <td>397</td>
      <td>382</td>
      <td>397</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>406</td>
      <td>398</td>
      <td>406</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>421</td>
      <td>407</td>
      <td>421</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>422</td>
      <td>430</td>
      <td>422</td>
      <td>430</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>431</td>
      <td>447</td>
      <td>431</td>
      <td>447</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>448</td>
      <td>469</td>
      <td>448</td>
      <td>469</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>470</td>
      <td>486</td>
      <td>470</td>
      <td>486</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>487</td>
      <td>868</td>
      <td>487</td>
      <td>868</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>869</td>
      <td>875</td>
      <td>869</td>
      <td>875</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s42003-021-02473-8

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7e9s">7E9S</a></td>
      <td>2.7 A</td>
      <td>Not specified in paper</td>
      <td>AfAglB G617C mutant with tethered sequon peptide (TAMRA-APY(Dab)VTASCR-OH), ternary complex with dolichol-phosphate</td>
      <td>Dolichol-phosphate, Mn2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43 (DE3) cells
- **Construct**: AfAglB G617C mutant (cysteine introduced at position 617 for peptide tethering); native AfAglB lacks cysteine residues

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>AfAglB G617C mutant cross-linked to sequon peptide, in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> detergent</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>7.7 MAG (1-(7Z-tetradecenoyl)-rac-<a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>100 K (cryo)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Lipidic sponge mesophase. Crystals identified by magenta color of TAMRA dye. Data collected from 2529 microcrystals at microfocus BL32XU, SPring-8. 483 datasets merged and scaled to 2.7 A using KAMO.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7e9s">7E9S</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQNAE</span><span class="topo-inside">SWFKKYW</span><span class="topo-membrane">HLSVLVIAALISVKL</span><span class="topo-outside">RILNPWNSVFTWTVRLGGNDPWYYYRLIENTIHNFPHRIWFDPFTYYPYGSYTHFG</span><span class="topo-unknown">PFLVYLGSIAGII</span><span class="topo-outside">FSATSGESLRAVLAFIPAI</span><span class="topo-membrane">GGVLA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ILPVYLLTREV</span><span class="topo-inside">FDKRA</span><span class="topo-membrane">AVIAAFLIAIVP</span><span class="topo-outside">GQFLQRSILGFNDHHI</span><span class="topo-membrane">WEAFWQVSALGTFLLA</span><span class="topo-inside">YNRWKGHDLSHNLTARQM</span><span class="topo-membrane">AYPVIAGITIGLYVL</span><span class="topo-outside">SWGAG</span><span class="topo-membrane">FIIAPIILAFMFFA</span><span class="topo-inside">FVLAGFVN</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ADRKNLS</span><span class="topo-membrane">LVAVVTFAVSALIYLP</span><span class="topo-outside">FAFNYPGFSTIFYSPFQ</span><span class="topo-membrane">LLVLLGSAVIAAAF</span><span class="topo-inside">YQIEKWNDVGFFERVGLGRKGMPL</span><span class="topo-membrane">AVIVLTALIMGLFFV</span><span class="topo-outside">I</span><span class="topo-unknown">SPDFARNLLSVV</span><span class="topo-outside">RVVQPKGGALTIAE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">VYPFFFTHNGEFTL</span><span class="topo-unknown">TNAVLH</span><span class="topo-membrane">FGALFFFGMAGILYSA</span><span class="topo-inside">YRFLKRRSFP</span><span class="topo-membrane">EMALLIWAIAMFIALW</span><span class="topo-outside">GQNRFA</span><span class="topo-membrane">YYFAAVSAVYSALALS</span><span class="topo-inside">VVFDKLH</span><span class="topo-unknown">LYRALEN</span><span class="topo-inside">AIGARNKLSYFRVA</span><span class="topo-membrane">FALLIALA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">AIYPTYILA</span><span class="topo-outside">DAQSSYAGGPNKQWYDALTWMRENTPDGEKYDEYYLQLYPTPQSNKEPFSYPFETYGVISWWDYGHWIEAVAHRMPIANPFQAGIGNKYNNVPGASSFFTAENESYAEFVA</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">EKLNVKYVVSDIEMETCKYYAMAVWAEGDLPLAEKYYGGYFYYSPTGTFGYANSQWDIPLNSIIIPLRIPSELYYSTMEAKLHLFDGSGLSHYRMIYESDYPAEWKSYSSQVNLNNESQV</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">LQTALYEAVMRARYGVSPTMGTQEVLYKYAYTQLYEKKMGIPVKIAPSGYVKIFERVKGAVVTGKVSANVTEVSVNATIKTNQNRTFEYWQTVEVKNGTYTVVLPYSHNSDYPVKPITPY</span></span>
<span class="topo-ruler">       850       860       870     </span>
<span class="topo-line"><span class="topo-outside">HIKAGNVVKEITIYESQVQNGEIIQLDLELAL</span><span class="topo-unknown">VPR</span></span>
<details class="topo-details"><summary>Topology coordinates (34 regions)</summary>
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
      <td>6</td>
      <td>12</td>
      <td>6</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>27</td>
      <td>13</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>83</td>
      <td>28</td>
      <td>83</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>84</td>
      <td>96</td>
      <td>84</td>
      <td>96</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>97</td>
      <td>115</td>
      <td>97</td>
      <td>115</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>131</td>
      <td>116</td>
      <td>131</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>132</td>
      <td>136</td>
      <td>132</td>
      <td>136</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>148</td>
      <td>137</td>
      <td>148</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>164</td>
      <td>149</td>
      <td>164</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>180</td>
      <td>165</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>198</td>
      <td>181</td>
      <td>198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>213</td>
      <td>199</td>
      <td>213</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>214</td>
      <td>218</td>
      <td>214</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>219</td>
      <td>232</td>
      <td>219</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>247</td>
      <td>233</td>
      <td>247</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>248</td>
      <td>263</td>
      <td>248</td>
      <td>263</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>264</td>
      <td>280</td>
      <td>264</td>
      <td>280</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>294</td>
      <td>281</td>
      <td>294</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>295</td>
      <td>318</td>
      <td>295</td>
      <td>318</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>333</td>
      <td>319</td>
      <td>333</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>334</td>
      <td>334</td>
      <td>334</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>346</td>
      <td>335</td>
      <td>346</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>347</td>
      <td>374</td>
      <td>347</td>
      <td>374</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>380</td>
      <td>375</td>
      <td>380</td>
      <td>Unknown</td>
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
      <td>406</td>
      <td>397</td>
      <td>406</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>422</td>
      <td>407</td>
      <td>422</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>423</td>
      <td>428</td>
      <td>423</td>
      <td>428</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>429</td>
      <td>444</td>
      <td>429</td>
      <td>444</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>445</td>
      <td>451</td>
      <td>445</td>
      <td>451</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>452</td>
      <td>458</td>
      <td>452</td>
      <td>458</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>459</td>
      <td>472</td>
      <td>459</td>
      <td>472</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>473</td>
      <td>489</td>
      <td>473</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>872</td>
      <td>490</td>
      <td>872</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Conserved sequon recognition mechanism between archaeal and eubacterial OSTs

The crystal structure of the cross-linked AfAglB-sequon complex reveals that the [N-Glycosylation Sequon](/xray-mp-wiki/concepts/membrane-mimetics/n-glycosylation-sequon/) binds in the same manner as in the C. lari PglB-peptide complex. The acceptor peptide adopts an extended conformation with the Asn-Val-Thr sequon positioned at the boundary between the N-terminal transmembrane region and the C-terminal globular domain. Two conserved interactions are observed: (1) the Asn side-chain carboxamide group interacts with Asp47 and Glu360 ([Carboxylate Dyad](/xray-mp-wiki/concepts/enzyme-mechanisms/carboxylate-dyad/)) and a bound metal ion, and (2) the Thr residue at the +2 position is recognized by the Ser/Thr-binding pocket formed by the W550-W551-D552 motif and K618. This demonstrates evolutionary conservation of sequon recognition between archaeal and eubacterial OSTs despite low sequence identity (<20%).

### Carboxylate dyad catalytic mechanism

The [Carboxylate Dyad](/xray-mp-wiki/concepts/enzyme-mechanisms/carboxylate-dyad/) consists of Asp47 (in the GND motif of external loop 1) and Glu360 (in the TIAE motif of external loop 5), which together coordinate a divalent metal ion. Their side-chain carboxylate groups contact the carboxamide group of the acceptor Asn side chain, twisting the planar carboxamide geometry to enable nucleophilic attack on the C1 carbon of the lipid-linked oligosaccharide donor. Single alanine mutations (D47A, E360A) retained reduced but significant activity in the cross-linked state, whereas the double mutation (D47A/E360A) completely abolished catalysis. In contrast, without tethering, both single mutants showed complete loss of activity.

### EL5 loop conformational dynamics

The EL5 loop exhibits dynamic behavior upon acceptor peptide binding. In the apo state (3WAK), the EL5 loop is fully ordered and Glu360 is not involved in metal-ion coordination. Upon acceptor peptide binding, the N-terminal half of EL5 (Ser335-Gln350) becomes disordered while the C-terminal half (Pro351-Thr373) remains ordered. This partially ordered state is an intrinsic property observed in both AfAglB and C. lari PglB complexes. The conformational change positions Glu360 to participate in the [Carboxylate Dyad](/xray-mp-wiki/concepts/enzyme-mechanisms/carboxylate-dyad/) interactions with the acceptor Asn side chain and metal ion.

### TIXE motif forms inter-chain hydrogen bonds with the sequon

The TIXE motif (Thr357-Ile-Ala-Glu360) in the EL5 loop of AfAglB forms two inter-chain hydrogen bonds with the sequon-containing acceptor peptide. The carbonyl oxygen of Thr357 H-bonds with the amide group of Ala+3, and the carbonyl oxygen of Val+1 H-bonds with the amide group of Ala359, creating an antiparallel beta-sheet-like arrangement. This interaction was revealed by the ternary complex structure at 2.7 A resolution. Extensive alanine-scanning mutagenesis of 44 residues in the EL5 loop confirmed the essential role of the TIXE motif, where the C-terminal segment (Leu356-Phe365) showed the most critical activity decreases.

### Structural basis for proline exclusion from the N-glycosylation sequon

The rigid sequon-TIXE frame structure forces the amino acid residues at position +1 (middle of sequon) to adopt a high phi dihedral angle around -150 degrees. A Ramachandran plot analysis reveals that the ring structure of the proline side chain is incompatible with this phi backbone dihedral angle, as proline phi is constrained to approximately -60 degrees due to its pyrrolidine ring. This provides the structural basis for the absolute exclusion of proline from the N-glycosylation sequon observed across all domains of life. No glycosylated Asn-Pro-Thr or Asn-Pro-Ser sites exist in the N-GlycositeAtlas database of over 35,000 reviewed N-glycosylated sequences from human glycoproteins.

### LLO entry gate mechanism via TM helix 8-9 tunnel

The dolichol-phosphate omega-terminus binds in a tunnel structure at the interface between TM helices 8 and 9, suggesting that the LLO molecule enters the binding site through the gap between these helices. TM helix 9 must move in concert with the conformational change of the EL5 loop to enlarge the gap upon LLO binding. This differs from eubacterial ClPglB where LLO was assumed to thread under the disordered EL5 while TM helix 9 stayed in place, reflecting different LLO structures (dolichol-based vs polypropenol-based).

### Relaxed sequon consensus requirements in cross-linked state

In the cross-linked complex, the stringent N-glycosylation consensus requirements are greatly relaxed: (1) A Gln residue at the Asn position functions as an acceptor (QVT sequon), with MS analysis confirming heptasaccharide attachment, (2) The hydroxy group at the +2 position is not required (NVA sequon accepted, though slower than NVT), (3) Amino acid preferences at the X position disappear except for Pro rejection. This contrasts with free-peptide assays where strong X-position preferences (Glu/Gln favored, Arg/Lys/Trp disfavored) are observed. The cross-linked state mimics co-translational oligosaccharyl transfer coupled with membrane protein permeation.


## Cross-References

- <a href="/xray-mp-wiki/concepts/membrane-mimetics/n-glycosylation-sequon/">N-Glycosylation Sequon</a> — AfAglB recognizes and catalyzes glycosylation of the Asn-X-Ser/Thr sequon
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/carboxylate-dyad/">Carboxylate Dyad</a> — Catalytic mechanism of AfAglB involves the Asp47-Glu360 carboxylate dyad
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for solubilization and purification of AfAglB
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">Lauryldimethylamine N-oxide (LDAO)</a> — Detergent used for gel filtration and crystallization of AfAglB
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Buffer used throughout AfAglB expression, purification, and assays
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Referenced in archaeoglobus-fulgidus-aglb
- <a href="/xray-mp-wiki/reagents/additives/peg-550-mme/">PEG 550 MME</a> — Referenced in archaeoglobus-fulgidus-aglb
- <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a> — Referenced in archaeoglobus-fulgidus-aglb
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Referenced in archaeoglobus-fulgidus-aglb
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Nickel Sepharose</a> — Referenced in archaeoglobus-fulgidus-aglb
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase (LCP) crystallization</a> — LCP method used for ternary complex crystallization at 2.7 A
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/n-glycosylation-sequon/">N-glycosylation sequon</a> — AfAglB recognizes the Asn-X-Ser/Thr sequon; the TIXE motif explains Pro exclusion
