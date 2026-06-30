---
title: "Archaeoglobus fulgidus Oligosaccharyltransferase AfAglB"
created: 2026-06-10
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, enzyme]
sources: [doi/10.1038##s42003-021-02473-8]
verified: false
---

# Archaeoglobus fulgidus Oligosaccharyltransferase AfAglB

## Overview

AfAglB is the catalytic subunit of the oligosaccharyltransferase (OST) from the archaeon Archaeoglobus fulgidus. It catalyzes the transfer of oligosaccharides from a dolichol-phosphate-linked oligosaccharide (LLO) donor to the asparagine residue in the N-glycosylation sequon (Asn-X-Ser/Thr), where X is any amino acid except proline. The structure of AfAglB in complex with a sequon-containing acceptor peptide and dolichol-phosphate was solved at 2.7 Å resolution using lipidic cubic phase (LCP) crystallization. The structure reveals the molecular basis for the strict exclusion of proline from the N-glycosylation sequon through the TIXE motif in the external loop 5 (EL5), which forms two inter-chain hydrogen bonds with the sequon. The conserved motifs (two DXD motifs, TIXE, WWDYG, DGGK, and DK motifs) are spatially arranged similarly across archaeal, eukaryotic, and eubacterial OST enzymes, suggesting a conserved catalytic mechanism.


## Publications

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
      <td>2.7</td>
      <td></td>
      <td>AfAglB G617C mutant with tethered sequon peptide (TAMRA-APY(Dab)VTASCR-OH) and bound dolichol-phosphate</td>
      <td>Dolichol-phosphate, Mn2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43 (DE3)
- **Construct**: Full-length AfAglB (868 residues, UniProt O29867) with C-terminal His-tag in pET-52b(+)
- **Induction**: 1 mM IPTG at OD600 0.8-1.0
- **Media**: Terrific Broth

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
      <td>Cell growth</td>
      <td><a href="/xray-mp-wiki/organisms/e-coli/">E. coli</a> C43 (DE3) fermentation</td>
      <td>—</td>
      <td></td>
      <td>Induced at OD600 0.8-1.0 with 1 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG (Isopropyl-beta-D-thiogalactopyranoside)</a></td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td><a href="/xray-mp-wiki/methods/cell-lysis/french-press/">Microfluidizer</a> or sonication</td>
      <td>—</td>
      <td>Standard lysis buffer</td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (n-Dodecyl β-D-maltopyranoside)</td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin</td>
      <td></td>
      <td>C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his-tag/">His-tag</a> purification</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>—</td>
      <td></td>
      <td>Final polishing step</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td>7.7 MAG (1-(7Z-tetradecenoyl)-rac-<a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C (cryo stream at 100 K)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td><a href="/xray-mp-wiki/reagents/peg400/">PEG400</a> in crystallization condition</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in lipidic sponge mesophase. Microcrystals identified by magenta color of TAMRA dye. Data collected from 2529 microcrystals at microfocus beamline BL32XU, SPring-8. 483 datasets merged and scaled to 2.7 Å using KAMO.</td>
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

### TIXE motif forms inter-chain hydrogen bonds with the sequon

The TIXE motif (Thr357-Ile-Ala-Glu360) in the EL5 loop of AfAglB forms two inter-chain hydrogen bonds with the sequon-containing acceptor peptide. The carbonyl oxygen of Thr357 hydrogen bonds with the amide group of Ala+3, and the carbonyl oxygen of Val+1 hydrogen bonds with the amide group of Ala359, creating an antiparallel β-sheet-like arrangement. This interaction forces the sequon segment (Dab-Val-Thr) to adopt an extended conformation. The essential role of the TIXE motif was confirmed by extensive alanine-scanning mutagenesis of 44 residues in the EL5 loop, where the C-terminal segment containing TIXE (Leu356-Phe365) showed the most critical activity decreases.

### Structural basis for proline exclusion from the N-glycosylation sequon

The rigid sequon-TIXE frame structure forces the amino acid residues at positions +1 (middle of sequon) and +3 to adopt high φ dihedral angles around -150°. A Ramachandran plot analysis reveals that the ring structure of the proline side chain is incompatible with this φ backbone dihedral angle, as the proline φ angle is constrained to approximately -60° due to its pyrrolidine ring. This provides the structural basis for the absolute exclusion of proline from the N-glycosylation sequon observed across all domains of life — no glycosylated Asn-Pro-Thr or Asn-Pro-Ser sites exist in the N-GlycositeAtlas database of over 35,000 reviewed N-glycosylated sequences from human glycoproteins.

### Conserved catalytic architecture across domains of life

The spatial arrangements of conserved amino acid motifs — two DXD motifs, TIXE/SVSE, WWDYG, DGGK/DNXTZNX[T/S], and DK/MI motifs — are strikingly similar between archaeal AfAglB and eubacterial ClPglB. The metal ion (Mn2+) is coordinated by Asp47 in the first DXD motif, Asp161 and His163 in the second DXD motif, and three water molecules in a regular octahedral arrangement. Glu360 in the TIXE motif indirectly participates in metal coordination through two of the three water molecules. The phosphate group of dolichol-phosphate also interacts with the metal ion through two water molecules. The WWDYG and DK/MI motifs form the Ser/Thr-binding pocket in the C-terminal globular domain, explaining the requirement for hydroxy amino acids at position +2 of the sequon.

### LLO entry gate mechanism

The dolichol-phosphate ω-terminus binds in a tunnel structure at the interface between TM helices 8 and 9, suggesting that the LLO molecule enters the binding site through the gap between these helices. TM helix 9 must move in concert with the conformational change of the EL5 loop to enlarge the gap upon LLO binding. A similar mechanism was proposed for the Stt3 subunit in yeast OST. This differs from ClPglB where LLO was assumed to thread into the binding site under the disordered EL5 while TM helix 9 stayed in place, reflecting the different LLO structures (dolichol-based in Archaea/Eukarya vs. polypropenol-based in Eubacteria).


## Cross-References

- <a href="/xray-mp-wiki/concepts/n-glycosylation/">N-Glycosylation</a> — AfAglB catalyzes the central oligosaccharide transfer step in N-glycosylation
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — The AfAglB structure was solved using LCP crystallization
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Method used in the study
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/proteins/enzymes/aglB/">A. fulgidus AglB-L Oligosaccharyltransferase</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/proteins/cys-loop-receptors/elic/">ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel)</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Reagent used in the study
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG (Isopropyl-beta-D-thiogalactopyranoside)</a> — Reagent used in the study
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Reagent used in the study
- <a href="/xray-mp-wiki/reagents/detergents/og/">n-Octyl beta-D-glucopyranoside (OG)</a> — Detergent used in purification
