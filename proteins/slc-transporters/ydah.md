---
title: "A. borkumensis YdaH transporter"
created: 2026-06-05
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms7874]
verified: false
---

# A. borkumensis YdaH transporter

## Overview

YdaH is an integral membrane protein from Alcanivorax borkumensis encoded by the ydaH gene. It belongs to the AbgT family of transporters and was the first member of this family to have a crystal structure reported. YdaH is a 492-amino acid dimeric transporter that forms a bowl-shaped structure with a solvent-filled basin extending from the cytoplasm to halfway across the membrane bilayer. Each subunit contains nine transmembrane helices and two hairpins. Functional assays demonstrate that YdaH functions as a proton-motive-force (PMF)-dependent efflux pump that exports p-aminobenzoic acid (PABA) and confers resistance to sulfonamide antimetabolites, suggesting a role in antibiotic resistance.


## Publications

### doi/10.1038##ncomms7874

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4r0c">4R0C</a></td>
      <td>2.96 A</td>
      <td>P2$_{1}$</td>
      <td>Full-length A. borkumensis YdaH with N-terminal 6xHis tag</td>
      <td>None (apo structure)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) delta [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/acrB)
- **Construct**: Full-length YdaH with N-terminal 6xHis tag, cloned into pET15b vector as pET15b_Omega ydaH. Expressed in E. coli BL21(DE3) delta acrB strain which harbors a deletion in the chromosomal acrB gene. Cells grown in 12 L LB medium with 100 ug/mL ampicillin. Induced with 0.2 mM IPTG at OD600=0.5.


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
      <td>Cell culture and membrane isolation</td>
      <td>Cells grown in 12 L LB medium with 100 ug/mL <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin">Ampicillin</a> at 37 C. Induced with 0.2 mM <a href="/xray-mp-wiki/reagents/additives/iptg">IPTG</a> at OD600=0.5, harvested within 2 h. Membranes isolated by ultracentrifugation.
</td>
      <td>--</td>
      <td>-- + --</td>
      <td>E. coli BL21(DE3) delta <a href="/xray-mp-wiki/proteins/acrB">AcrB multidrug efflux pump</a> strain transformed with pET15b_Omega ydaH</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane solubilization</td>
      <td>--</td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> (n-Dodecyl-beta-D-maltopyranoside)</td>
      <td>Membranes solubilized with <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> detergent</td>
    </tr>
    <tr>
      <td>Ni-affinity chromatography</td>
      <td>Ni-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (Ni-NTA)</td>
      <td>Ni-NTA agarose</td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>His-tag purification using Ni-NTA resin</td>
    </tr>
    <tr>
      <td>Size exclusion chromatography</td>
      <td>Superdex 200 16/60 column (GE Healthcare) with mobile phase containing 20 mM Na-<a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> (pH 7.5) and 0.05% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>. Blue dextran used to determine column void volume.
</td>
      <td>Superdex 200 16/60 (GE Healthcare)</td>
      <td>20 mM Na-<a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> (pH 7.5), 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Gel filtration suggested an average molecular weight of 107.0 +/- 8.8 kDa, in good agreement with the theoretical value of 105.6 kDa for two YdaH protomers (dimer).
</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified YdaH in Na-<a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> buffer with <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Native crystals grown in space group P2_1. Additional crystals obtained with [beta-SiW9O34H]9- polyoxometalate (7.70 A) and Se-derivative (4.10 A) for phasing. Na+ ions present at all stages of purification and crystallization. A strong spherical electron density was observed in the flexible loops between HP2 and TM8, identified as a Na+ ion coordinated by N390, D429, N433, backbone carbonyl oxygens of G394 and D429, and a water molecule.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4r0c">4R0C</a> — Chain A (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTRTHGWLARLEQLGN</span><span class="topo-outside">RL</span><span class="topo-membrane">PHPTLLFVWFCLLLLPLT</span><span class="topo-inside">AVLGALDVTATHPLTDETITAHSL</span></span>
<span class="topo-line"><span class="topo-inside">LDADGLRYLFTT</span><span class="topo-membrane">LVGNFTGFAPLGVVLVAMLGLGVAE</span><span class="topo-outside">QSG</span><span class="topo-unknown">LLSVSLASLVRR</span><span class="topo-outside">SSGGA</span><span class="topo-unknown">LVF</span></span>
<span class="topo-line"><span class="topo-unknown">TVAFAGVLSSLTV</span><span class="topo-outside">DAGYVVLIPLAGLVFQLAGRPPIAGIATAFAA</span><span class="topo-membrane">VSGGFSANLLVGPVD</span></span>
<span class="topo-line"><span class="topo-membrane">ATLAGLSTEA</span><span class="topo-inside">AHIIDPDRTVA</span><span class="topo-membrane">ATGNYWFIIASTFLVTGLVTL</span><span class="topo-outside">ITRTLTEPRLAHANTVAD</span></span>
<span class="topo-line"><span class="topo-outside">ASVDAPQIHSRAMK</span><span class="topo-membrane">WTGLTLAILLAGLALL</span><span class="topo-inside">VLPNDAPLRHPDTGSVLGSPF</span><span class="topo-membrane">IHGLVVIVA</span></span>
<span class="topo-line"><span class="topo-membrane">LIAGICGAVY</span><span class="topo-outside">GRVSGQFRNSGAV</span><span class="topo-membrane">ITAMEVTMASMAGYLVLMFFAAQFVAWF</span><span class="topo-inside">NYSQ</span><span class="topo-unknown">LGLLL</span></span>
<span class="topo-line"><span class="topo-unknown">AVKGAAWLGA</span><span class="topo-inside">LTVPKV</span><span class="topo-membrane">VLLLLFVVLTALINLMI</span><span class="topo-outside">G</span><span class="topo-membrane">SASAKWSILAPVFI</span><span class="topo-inside">PMLMLLGISPE</span><span class="topo-membrane">A</span></span>
<span class="topo-line"><span class="topo-membrane">SQAAYRVGDSSTN</span><span class="topo-outside">IITPLMPYFVLVLGFARRYQPETGIGTLIALMLPY</span><span class="topo-membrane">SLTLLLGWSVLL</span></span>
<span class="topo-line"><span class="topo-membrane">GVWI</span><span class="topo-inside">GFGWP</span><span class="topo-unknown">LGP</span></span>
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
      <td>17</td>
      <td>18</td>
      <td>17</td>
      <td>18</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>36</td>
      <td>19</td>
      <td>36</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>37</td>
      <td>72</td>
      <td>37</td>
      <td>72</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>97</td>
      <td>73</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>100</td>
      <td>98</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>112</td>
      <td>101</td>
      <td>112</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>117</td>
      <td>113</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>133</td>
      <td>118</td>
      <td>133</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>134</td>
      <td>165</td>
      <td>134</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>190</td>
      <td>166</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>201</td>
      <td>191</td>
      <td>201</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>222</td>
      <td>202</td>
      <td>222</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>254</td>
      <td>223</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>270</td>
      <td>255</td>
      <td>270</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>271</td>
      <td>291</td>
      <td>271</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>310</td>
      <td>292</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>323</td>
      <td>311</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>351</td>
      <td>324</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>352</td>
      <td>355</td>
      <td>352</td>
      <td>355</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>370</td>
      <td>356</td>
      <td>370</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>371</td>
      <td>376</td>
      <td>371</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>393</td>
      <td>377</td>
      <td>393</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>394</td>
      <td>394</td>
      <td>394</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>408</td>
      <td>395</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>419</td>
      <td>409</td>
      <td>419</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>420</td>
      <td>433</td>
      <td>420</td>
      <td>433</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>434</td>
      <td>468</td>
      <td>434</td>
      <td>468</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>469</td>
      <td>484</td>
      <td>469</td>
      <td>484</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>485</td>
      <td>489</td>
      <td>485</td>
      <td>489</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>490</td>
      <td>492</td>
      <td>490</td>
      <td>492</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4r0c">4R0C</a> — Chain B (11 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTRTHGWLARLEQLGNRL</span><span class="topo-outside">P</span><span class="topo-membrane">HPTLLFVWFCLLLLPL</span><span class="topo-inside">TAVLGALDVTATHPLTDETITAHSL</span></span>
<span class="topo-line"><span class="topo-inside">LDADGLRYLFTT</span><span class="topo-membrane">LVGNFTGFAPLGVVLVAMLGLGVAE</span><span class="topo-outside">QSG</span><span class="topo-unknown">LLSVSLASL</span><span class="topo-outside">VR</span><span class="topo-unknown">RSSGGA</span><span class="topo-outside">L</span><span class="topo-unknown">VF</span></span>
<span class="topo-line"><span class="topo-unknown">TVAFAGVLSSL</span><span class="topo-outside">TVDAGYVVLIPLAGLVFQLAGRPPIAGIATAFAA</span><span class="topo-membrane">VSGGFSANLLVGPVD</span></span>
<span class="topo-line"><span class="topo-membrane">ATLAGLSTEA</span><span class="topo-inside">AHIIDPDRTV</span><span class="topo-membrane">AATGNYWFIIASTFLVTGLV</span><span class="topo-outside">TLITRTLTEPRLAHANTVAD</span></span>
<span class="topo-line"><span class="topo-outside">ASVDAPQIHSRAMK</span><span class="topo-membrane">WTGLTLAILLAGLALL</span><span class="topo-inside">VLPNDAPLRHPDTGSVLGSPF</span><span class="topo-membrane">IHGLVVIVA</span></span>
<span class="topo-line"><span class="topo-membrane">LIAGICGAVY</span><span class="topo-outside">GRVSGQFRNSGAV</span><span class="topo-membrane">ITAMEVTMASMAGYLVLMFFAAQFVAWF</span><span class="topo-inside">NYSQ</span><span class="topo-unknown">LGLLL</span></span>
<span class="topo-line"><span class="topo-unknown">AVKGAAWLGA</span><span class="topo-inside">LTVPKV</span><span class="topo-membrane">VLLLLFVVLTALINLMI</span><span class="topo-outside">G</span><span class="topo-membrane">SASAKWSILAPVFI</span><span class="topo-inside">PMLMLLGISP</span><span class="topo-membrane">EA</span></span>
<span class="topo-line"><span class="topo-membrane">SQAAYRVGDSSTN</span><span class="topo-outside">IITPLMPYFVLVLGFARRYQPETGIGTLIALMLPYS</span><span class="topo-membrane">LTLLLGWSVLL</span></span>
<span class="topo-line"><span class="topo-membrane">GVWIG</span><span class="topo-inside">FGWPLGP</span></span>
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
      <td>19</td>
      <td>19</td>
      <td>19</td>
      <td>19</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>35</td>
      <td>20</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>72</td>
      <td>36</td>
      <td>72</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>97</td>
      <td>73</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>100</td>
      <td>98</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>109</td>
      <td>101</td>
      <td>109</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>110</td>
      <td>111</td>
      <td>110</td>
      <td>111</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>118</td>
      <td>118</td>
      <td>118</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>131</td>
      <td>119</td>
      <td>131</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>132</td>
      <td>165</td>
      <td>132</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>190</td>
      <td>166</td>
      <td>190</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>200</td>
      <td>191</td>
      <td>200</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>220</td>
      <td>201</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>254</td>
      <td>221</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>270</td>
      <td>255</td>
      <td>270</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>271</td>
      <td>291</td>
      <td>271</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>292</td>
      <td>310</td>
      <td>292</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>323</td>
      <td>311</td>
      <td>323</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>324</td>
      <td>351</td>
      <td>324</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>352</td>
      <td>355</td>
      <td>352</td>
      <td>355</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>356</td>
      <td>370</td>
      <td>356</td>
      <td>370</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>371</td>
      <td>376</td>
      <td>371</td>
      <td>376</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>393</td>
      <td>377</td>
      <td>393</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>394</td>
      <td>394</td>
      <td>394</td>
      <td>394</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>408</td>
      <td>395</td>
      <td>408</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>409</td>
      <td>418</td>
      <td>409</td>
      <td>418</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>433</td>
      <td>419</td>
      <td>433</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>434</td>
      <td>469</td>
      <td>434</td>
      <td>469</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>470</td>
      <td>485</td>
      <td>470</td>
      <td>485</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>492</td>
      <td>486</td>
      <td>492</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Bowl-shaped dimer architecture

YdaH forms a dimeric molecule with a bowl-shaped architecture distinct from other families of transporters. The dimer creates a concave aqueous basin facing the intracellular solution. Each protomer forms an internal cavity accessible to the cytoplasm, constituted by loop regions of HP1, HP2, TM3 and TM8. The inner core comprises TMs 1, 2, 5, 6 and 7 contributing to dimerization and a frame-like structure. The outer core cylinder (TMs 3, 4, 8, 9 and HPs 1 and 2) forms a channel spanning approximately from the middle of the inner membrane up to the periplasmic space.

### Conserved channel residues

Several conserved residues line the wall of the outer core channel: D180, W400, P418 and R426. These residues are expected to play an important role in the function of the transporter. Mutational analysis of D180A, W400A, P418A, and R426A showed that R426A retained partial function in decreasing PABA concentration while D180A, W400A, and P418A showed significantly increased intracellular PABA levels, indicating loss of efflux function.

### Na+ binding site

Each protomer of YdaH binds a Na+ ion in the flexible loops between HP2 and TM8. The Na+ coordination sphere includes side chains of N390, D429, N433 and backbone carbonyl oxygens of G394 and D429, plus a water molecule forming a coordinate bond. Valence calculations indicated this site is Na+ specific. Functional assays showed that 5 or 100 mM NaCl significantly decreased intracellular sulfamethazine accumulation compared to YdaH-producing strain without Na+, and efflux assays confirmed Na+ but not K+ has a strong effect on sulfamethazine efflux, indicating YdaH functions more efficiently in the presence of Na+.

### PMF-dependent efflux mechanism

YdaH functions as a proton-motive-force (PMF)-dependent efflux pump. The uncoupler CCCP (carbonyl cyanide m-chlorophenylhydrazone) drastically increased intracellular sulfamethazine accumulation in YdaH-expressing cells, confirming PMF dependence. This is consistent with the hypothesis that AbgT family members use the PMF to transport substrates across the membrane.

### Sulfonamide efflux and antibiotic resistance

YdaH acts as an antibiotic efflux pump capable of extruding sulfonamide antimetabolites. It exports PABA (p-aminobenzoic acid) from the cell and confers resistance to sulfonamides including sulfanilamide (Ki=0.41 uM), sulfathiazole (Ki=0.60 uM), sulfadiazine (Ki=4.97 uM), and sulfamethazine (Ki=7.04 uM). All mutants D180A, N390A, W400A, P418A, R426A, D429A and N433A showed hypersensitivity to sulfonamides compared to wild-type YdaH, confirming these residues are essential for drug resistance function.

### AbgT family functional diversity

The AbgT family (~13,000 putative members) includes both transporters and resistance proteins. E. coli AbgT imports p-aminobenzoyl-glutamate for de novo folate synthesis, while N. gonorrhoeae MtrF confers high-level resistance to hydrophobic antimicrobials. YdaH represents a third functional class: an efflux pump for sulfonamide antimetabolites. This suggests other AbgT family members may also serve as antimetabolite efflux pumps.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abgt-family/">AbgT Family of Transporters</a> — YdaH is the first structurally characterized member of the AbgT family
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/antibiotic-efflux-pump/">Antibiotic Efflux Pumps</a> — YdaH functions as a sulfonamide efflux pump
- <a href="/xray-mp-wiki/concepts/miscellaneous/sulfonamide-resistance/">Sulfonamide Resistance</a> — YdaH confers resistance to sulfonamide antimetabolites
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for YdaH solubilization and purification
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Na-HEPES buffer (pH 7.5) used in SEC and purification
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Agarose Resin</a> — Ni-NTA used for His-tag purification of YdaH
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 Increase SEC Resin</a> — Superdex 200 16/60 used for size exclusion chromatography of YdaH
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG (Isopropyl-beta-D-thiogalactopyranoside)</a> — 0.2 mM IPTG used for induction of ydaH expression
- <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a> — 100 ug/mL ampicillin used for selection during YdaH expression
- <a href="/xray-mp-wiki/reagents/additives/cccp/">CCCP (Carbonyl Cyanide m-Chlorophenylhydrazone)</a> — Protonophore uncoupler used to demonstrate PMF-dependence of YdaH
- <a href="/xray-mp-wiki/reagents/ligands/sulfanilamide/">Sulfanilamide</a> — YdaH binds sulfanilamide with Ki=0.41 uM and exports it from cells
- <a href="/xray-mp-wiki/reagents/ligands/sulfamethazine/">Sulfamethazine</a> — YdaH binds sulfamethazine with Ki=7.04 uM and exports it from cells
- <a href="/xray-mp-wiki/reagents/ligands/sulfathiazole/">Sulfathiazole</a> — YdaH binds sulfathiazole with Ki=0.60 uM
- <a href="/xray-mp-wiki/reagents/ligands/sulfadiazine/">Sulfadiazine</a> — YdaH binds sulfadiazine with Ki=4.97 uM
- <a href="/xray-mp-wiki/reagents/additives/paba/">p-Aminobenzoic Acid (PABA)</a> — YdaH exports PABA from bacterial cells
- <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">AcrB multidrug efflux pump</a> — Related efflux pump; E. coli BL21(DE3) delta acrB strain used for YdaH expression
- <a href="/xray-mp-wiki/concepts/miscellaneous/sodium-motive-force/">Sodium Motive Force</a> — Na+ enhances YdaH transporter function
