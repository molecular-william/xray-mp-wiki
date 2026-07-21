---
title: "Human Rhodopsin E113Q/M257Y Mutant"
created: 2026-06-03
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature14656]
verified: agent
uniprot_id: P08100
---

# Human Rhodopsin E113Q/M257Y Mutant

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P08100">UniProt: P08100</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Human rhodopsin is the visual pigment [GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) in vertebrate retina rod cells, responsible for dim-light vision. The E113Q/M257Y mutant is a constitutively active form that mimics the light-activated state. Glu113 (E(D)RY motif) mutation disrupts the inactive-state salt bridge, while Met257 (H6) mutation further stabilizes the active conformation. This mutant was used in complex with pre-activated mouse visual arrestin (3A mutant) to determine the first high-resolution structure of the rhodopsin-arrestin complex by serial femtosecond crystallography (SFX) at an X-ray free-electron laser.


## Publications

### doi/10.1038##nature14656

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4zwj">4ZWJ</a></td>
      <td>3.8 A</td>
      <td>P212121</td>
      <td>Human rhodopsin (residues 1-326) with N2C/N282C disulfide mutations, E113Q/M257Y activating mutations, T4 lysozyme fused at ICL3, fused to 3A arrestin (residues 10-392) via 15 aa linker</td>
      <td>all-trans retinal (ATR)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293S cells transiently transfected with tetracycline-inducible expression cassette. Cells grown in SFM4TransFx 293, diluted tenfold with CDM4HEK293 medium, induced with 1 ug/ml doxycycline after 24 h.

- **Construct**: Fusion protein: His8-MBP-3C protease site-T4L (residues 2-161, C54T C97A) -rhodopsin (residues 1-326, N2C/N282C/E113Q/M257Y)-15 aa linker (AAAGSAGSAGSAGSA)-3A arrestin (residues 10-392, L374A/V375A/F376A)


**Purification:**

- **Expression system**: HEK293S cells
- **Expression construct**: His8-MBP-3C protease site-T4L-rhodopsin(N2C/N282C, E113Q/M257Y)-15aa linker-3A arrestin (residues 10-392)
- **Tag info**: His8-MBP tag at N-terminus, removed by 3C protease cleavage

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
      <td>Cell culture and induction</td>
      <td>Transient transfection with tetracycline-inducible expression</td>
      <td>--</td>
      <td>SFM4TransFx 293, CDM4HEK293 medium + not specified</td>
      <td>Induced with 1 ug/ml doxycycline after 24 h</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Hypotonic lysis, <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">Dounce homogenization</a>, <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a></td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 10 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a> + not specified</td>
      <td>45,000 rpm at 4 C for 1 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.4, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Two hours at 4 C with <a href="/xray-mp-wiki/reagents/additives/protease-inhibitor-cocktail/">protease inhibitor cocktail</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/amylose/">Amylose</a> bead affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/amylose/">Amylose</a> beads (New England Biolabs)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 7.4, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.005% <a href="/xray-mp-wiki/reagents/detergents/mng-3/">MNG-3</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) + 0.005% <a href="/xray-mp-wiki/reagents/detergents/mng-3/">MNG-3</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Overnight at 4 C; eluted with 10 mM <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a></td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/hrv-3c-protease/">3C protease</a> cleavage</td>
      <td>--</td>
      <td>Washing buffer + 0.005% <a href="/xray-mp-wiki/reagents/detergents/mng-3/">MNG-3</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Overnight at 4 C</td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) beads (Qiagen)</td>
      <td>Washing buffer + 0.005% <a href="/xray-mp-wiki/reagents/detergents/mng-3/">MNG-3</a>, 0.001% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>3 hours at 4 C to remove <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His8</a>-MBP tag</td>
    </tr>
  </tbody>
</table>
**Final sample**: 30 mg/ml in washing buffer
**Yield**: not specified
**Purity**: not specified

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>61</td>
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
      <td>Microcrystals 5-15 um; diffracted to 6.8 A at synchrotron; <a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/">SFX</a> data to 3.8/3.8/3.3 A anisotropic</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
    <tr>
      <td>Protein:lipid ratio</td>
      <td>61</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>Monoolein</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4zwj">4ZWJ</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">NIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPS</span><span class="topo-unknown">LNAAKSELDKAI</span><span class="topo-inside">GRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRML</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYMCGTEGPNFYVPFSNATGVVRSPFEYPQYYLAEPWQFSM</span><span class="topo-membrane">LAAYMFLLIVLGFPINFLTLYVTVQH</span><span class="topo-outside">KKL</span><span class="topo-membrane">RTPLNYILLNLA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">VADLFMVLGGFTSTL</span><span class="topo-inside">YTSLHGYFVFGPTGCNL</span><span class="topo-membrane">QGFFATLGGEIALWSLVVLAIERYV</span><span class="topo-outside">VVCKPMSNFRFGE</span><span class="topo-membrane">NHAIMGVAFTWVMALACAAPPLA</span><span class="topo-inside">GWSRYIPEGLQCSCGIDYYTLKPEVNN</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">ES</span><span class="topo-membrane">FVIYMFVVHFTIPMIIIFFCYGQLVF</span><span class="topo-outside">TVKEAAAQQQESATTQKAEKEV</span><span class="topo-membrane">TRMVIIYVIAFLICWVPYASVAFY</span><span class="topo-inside">IFTHQGSCFGPIFMT</span><span class="topo-membrane">IPAFFAKSAAIYNPVIYIMMNKQFR</span><span class="topo-unknown">NCMLTT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-unknown">I</span><span class="topo-outside">CCGKN</span><span class="topo-unknown">PLGDDEASATVSKTETSQVAPAAAAGSAGSAGSAGSASH</span><span class="topo-outside">VIFKKVSRDKSVTIYLGKRDYVDHVSQVEPVDGVVLVDPELVKGKKVYVTLTCAFRYGQEDIDVMGLTFRRDLYF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">SRVQVYPPVGAMSVLTQLQESLLKKLGDNTYPFLLTFPDYLPCSVMLQPAPQDVGKSCGVDFEVKAFASDITDPEEDKIPKKSSVRLLIRKVQHAPPEMGPQPSAEASWQFFMSDKPLNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">SVSLSKEIYFHGEPIPVTVTVTNNTDKVVKKIKVSVEQIANVVLYSSDYYVKPVASEETQEKVQPNSTLTKTLVLVPLLANNRERRGIALDGKIKHEDTNLASSTIIKEGIDRTVMGILV</span></span>
<span class="topo-ruler">       850       860       870       880       890       900      </span>
<span class="topo-line"><span class="topo-outside">SYHIKVKLTVSGF</span><span class="topo-unknown">LGE</span><span class="topo-outside">LTSSEVATEVPFRLMHPQP</span><span class="topo-unknown">EDPAKESVQDENAAAEEFARQNLKDTGENTE</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>37</td>
      <td>1002</td>
      <td>1038</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>49</td>
      <td>1039</td>
      <td>1050</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>50</td>
      <td>199</td>
      <td>1051</td>
      <td>39</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>225</td>
      <td>40</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>226</td>
      <td>228</td>
      <td>66</td>
      <td>68</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>255</td>
      <td>69</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>256</td>
      <td>272</td>
      <td>96</td>
      <td>112</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>273</td>
      <td>297</td>
      <td>113</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>310</td>
      <td>138</td>
      <td>150</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>333</td>
      <td>151</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>362</td>
      <td>174</td>
      <td>202</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>388</td>
      <td>203</td>
      <td>228</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>389</td>
      <td>410</td>
      <td>229</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>411</td>
      <td>434</td>
      <td>251</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>435</td>
      <td>449</td>
      <td>275</td>
      <td>289</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>450</td>
      <td>474</td>
      <td>290</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>481</td>
      <td>315</td>
      <td>321</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>482</td>
      <td>486</td>
      <td>322</td>
      <td>326</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>526</td>
      <td>853</td>
      <td>2012</td>
      <td>2339</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>857</td>
      <td>875</td>
      <td>2343</td>
      <td>2361</td>
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

### Constitutively active rhodopsin mutant

The E113Q mutation disrupts the salt bridge between Glu113 (E(D)RY motif
in H3) and Arg135 (H3), mimicking the charge redistribution that occurs
upon photoisomerization of 11-cis [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) to [All-trans Retinal](/xray-mp-wiki/reagents/ligands/retinal/). The M257Y
mutation in H6 further stabilizes the active conformation. Together, these
mutations yield a constitutively active rhodopsin that recruits arrestin
with high affinity without prior phosphorylation by rhodopsin kinase.
The N2C/N282ECL3C disulfide mutation increases thermal stability without
affecting activity.

### Rhodopsin-arrestin complex architecture

The crystal structure of the T4L-rhodopsin-arrestin fusion complex revealed
an asymmetric binding arrangement where rhodopsin uses distinct structural
elements including transmembrane helix 7 (TM7) and helix 8 (H8) to recruit
arrestin. Arrestin adopts a pre-activated conformation with ~20 degree
rotation between its amino and carboxy domains, opening a cleft that
accommodates a short helix formed by the second intracellular loop (ICL2)
of rhodopsin. The complex has four rhodopsins, four arrestins, and three
T4 lysozymes in the asymmetric unit.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/">Bovine Rhodopsin</a> — Related rhodopsin structure; bovine rhodopsin dark state (PDB 1GZM) solved at 2.65 A
- <a href="/xray-mp-wiki/proteins/gpcr/opsin/">Opsin (Retinal-Free Rhodopsin)</a> — Apoprotein form of rhodopsin; same protein family
- <a href="/xray-mp-wiki/proteins/gpcr/squid-rhodopsin/">Squid Rhodopsin</a> — Invertebrate rhodopsin; structural comparison with vertebrate rhodopsin
- <a href="/xray-mp-wiki/proteins/gpcr/mouse-visual-arrestin-3a/">Mouse Visual Arrestin (3A)</a> — Arrestin partner in the rhodopsin-arrestin complex structure
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for solubilization of rhodopsin-arrestin complex
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hemisuccinate (CHS)</a> — Lipid additive used in solubilization and purification buffers
- <a href="/xray-mp-wiki/reagents/detergents/mng-3/">Lauryl Maltose Neopentyl Glycol (MNG-3)</a> — Mild detergent used in washing buffer for amylose bead purification
- <a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/">Serial Femtosecond Crystallography</a> — Primary method for structure determination at LCLS XFEL
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr/">Gpcr</a> — Related protein
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Related protein
