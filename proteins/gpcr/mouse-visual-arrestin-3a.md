---
title: "Mouse Visual Arrestin (3A)"
created: 2026-06-03
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature14656]
verified: false
---

# Mouse Visual Arrestin (3A)

## Overview

Mouse visual arrestin 1 (arrestin-1) is a cytosolic protein that binds to phosphorylated [G Protein](/xray-mp-wiki/concepts/g-protein)-coupled receptors (GPCRs) to terminate [G Protein](/xray-mp-wiki/concepts/g-protein) signaling and redirect signaling to G-protein-independent pathways. The 3A mutant (L374A, V375A, F376A) in the C-terminal tail adopts a pre-activated conformation that binds to activated receptors with high affinity without requiring receptor phosphorylation. The crystal structure of the 3A arrestin bound to constitutively active human rhodopsin (E113Q/M257Y) revealed the molecular basis for arrestin recruitment and biased signaling.


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
      <td>Mouse visual arrestin 1 (residues 12-361, with missing loop 340-342), 3A mutant (L374A/V375A/F376A)</td>
      <td>Human rhodopsin (E113Q/M257Y)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293S cells for fusion protein expression. In vitro translation for pull-down assays with 35S labeling.

- **Construct**: 3A arrestin mutant (L374A/V375A/F376A, residues 10-392) fused at C-terminus of rhodopsin-T4L fusion via 15 amino acid linker (AAAGSAGSAGSAGSA)


**Purification:**

- **Expression system**: In vitro translation (for pull-down assays)
- **Expression construct**: 3A arrestin (L374A/V375A/F376A, residues 10-392)
- **Tag info**: 35S-labeled for pull-down assays

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
      <td>In vitro translation</td>
      <td>Cell-free translation</td>
      <td>--</td>
      <td>not specified + not specified</td>
      <td>Labeled with 35S for bead binding pull-down assays</td>
    </tr>
    <tr>
      <td>Bead binding pull-down</td>
      <td>Amylose bead pull-down</td>
      <td>Amylose beads</td>
      <td>not specified + not specified</td>
      <td>Wild-type arrestin has weak background binding to wild-type rhodopsin; 3A arrestin shows strong binding</td>
    </tr>
  </tbody>
</table>
**Final sample**: Complex with rhodopsin purified as fusion protein
**Yield**: not specified
**Purity**: not specified

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

### Pre-activated arrestin conformation

The 3A arrestin mutant (L374A, V375A, F376A) in the C-terminal tail adopts
a pre-activated conformation that obviates the need for receptor phosphorylation
for high-affinity binding. In the absence of all-trans [Retinal](/xray-mp-wiki/reagents/ligands/retinal), the 3A arrestin
shows a nearly 30-fold increase in binding to the E113Q/M257Y rhodopsin mutant
compared to wild-type arrestin. Upon binding to activated rhodopsin, arrestin
undergoes a ~20 degree rotation between its amino and carboxy domains, opening
a cleft that accommodates the ICL2 helix of rhodopsin.

### Arrestin interface with rhodopsin

The rhodopsin-arrestin interface involves four distinct patches: (1) the
arrestin finger loop (residues Q70-L78) forming a short alpha helix that
interacts with TM7 and helix 8 of rhodopsin; (2) the arrestin middle loop
(V140 region) and C loop (Y251 region) interacting with rhodopsin ICL2;
(3) the arrestin beta strand (residues 79-86) interacting with rhodopsin
TM5, TM6, and ICL3; (4) the arrestin N-terminal beta strand (residues 11-19)
interacting with the rhodopsin C-terminal tail. The asymmetric binding
arrangement brings the arrestin C domain toward the membrane, with conserved
hydrophobic residues (F197, F198, M199, F339, L343) at the C tip potentially
functioning as a lipid-interacting module.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/human-rhodopsin-e113q-m257y/">Human Rhodopsin E113Q/M257Y Mutant</a> — Arrestin binding partner in the rhodopsin-arrestin complex structure
- <a href="/xray-mp-wiki/concepts/signaling-receptors/beta-arrestin-signaling/">Beta-Arrestin Signaling</a> — Arrestin-mediated GPCR signaling pathway and biased signaling
- <a href="/xray-mp-wiki/proteins/gpcr/bovine-rhodopsin/">Bovine Rhodopsin</a> — Bovine rhodopsin is the classical rhodopsin model system studied with arrestin
- <a href="/xray-mp-wiki/methods/quality-assessment/thermal-shift-assay/">Thermal Shift Assay</a> — Used to assess stability of the T4L rhodopsin-arrestin fusion complex (Tm 59 C)
- <a href="/xray-mp-wiki/reagents/ligands/retinal">Retinal</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/concepts/g-protein">G Protein</a> — Entity mentioned in text
