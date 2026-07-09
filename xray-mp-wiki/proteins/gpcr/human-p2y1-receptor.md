---
title: "Human P2Y1 Receptor"
created: 2026-06-03
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature14287]
verified: regex
uniprot_id: Q7K4Y6
---

# Human P2Y1 Receptor

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q7K4Y6">UniProt: Q7K4Y6</a>

<span class="expr-badge">Drosophila melanogaster</span>

## Overview

The human P2Y1 receptor (P2Y1R) is a class A [G Protein](/xray-mp-wiki/concepts/signaling-receptors/g-protein/)-coupled receptor ([GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/)) that serves as a critical target for antithrombotic therapy. It is activated by adenosine 5'-diphosphate ([ADP](/xray-mp-wiki/reagents/ligands/adp/)) and facilitates platelet aggregation, playing a pivotal role in thrombosis formation. Unlike the Gi-coupled P2Y12 receptor, P2Y1R is Gq-coupled and has been suggested to offer a safety advantage over P2Y12R inhibitors with reduced bleeding liabilities. The receptor is also involved in vascular inflammation and calcium wave propagation in astrocytes. Two distinct ligand-binding sites were revealed: an orthosteric site within the transmembrane bundle and an allosteric site on the external receptor interface with the lipid bilayer.


## Publications

### doi/10.1038##nature14287

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4m48">4M48</a></td>
      <td>2.70 A</td>
      <td>P1</td>
      <td>Human P2Y1R construct 1: residues 1-341 with N-terminal HA signal sequence, Flag tag, and C-terminal PreScission protease site plus 10x His tag. ICL3 (residues K247-P253) replaced by rubredoxin (M1-E54). D320(7.49)N mutation for improved yield and stability.
</td>
      <td>MRS2500</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4m49">4M49</a></td>
      <td>2.20 A</td>
      <td>R3H</td>
      <td>Human P2Y1R construct 2: residues 1-341 with N-terminal HA signal sequence, Flag tag, and C-terminal PreScission protease site plus 10x His tag. A23-L128 of thermostabilized BRIL (PDB 1M6T) fused before residue A8. D320(7.49)N mutation for improved yield and stability.
</td>
      <td>BPTU</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: [Sf9](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) insect cells ([Bac-to-Bac](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) [Baculovirus](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) Expression System)
- **Construct**: Two engineered constructs: Construct 1 with rubredoxin (M1-E54) fused into ICL3 at K247-P253 and D320N mutation. Construct 2 with A23-L128 of thermostabilized BRIL fused before residue A8 and D320N mutation. High-titre recombinant baculovirus (>10^8 viral particles per ml) used to infect Sf9 cells at 2x10^6 to 3x10^6 cells/ml at MOI of 5.


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
      <td>Cell lysis and differential centrifugation</td>
      <td>--</td>
      <td>Hypotonic: 10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a>, 20 mM KCl, <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>-free protease inhibitor. High osmotic: 1 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a>, 20 mM KCl. Storage: 10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 30% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a>, 20 mM KCl.
 + --</td>
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Sf9</a> cell membranes disrupted by dounce homogenization. Extensive washing by centrifugation in hypotonic buffer, then high osmotic buffer (3x), then hypotonic buffer again. Purified membranes flash-frozen in liquid nitrogen and stored at -80C.
</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Purified membranes solubilized in 0.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> and 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> for 3h at 4C in presence of 1 mM <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> and 2 mg/ml <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a>. Supernatant isolated by centrifugation at 160,000g for 30 min.
</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a></td>
      <td>Wash: 25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 40 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 1 mM <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a>. Elution: 25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>.
</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> resin incubated overnight at 4C. Resin washed with 10 column volumes of wash buffer, then eluted with 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>.
</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>X-ray crystallography</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>P2Y1R construct 1 (<a href="/xray-mp-wiki/reagents/protein-tags/rubredoxin/">Rubredoxin</a> fusion) in complex with <a href="/xray-mp-wiki/reagents/ligands/mrs2500/">MRS2500</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collection statistics from Extended Data Table 1. 50.0-2.70 A resolution (2.80-2.70 A shell). Rmerge 16.1% (83.2% in shell).
</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>X-ray crystallography</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>P2Y1R construct 2 (<a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL</a> fusion) in complex with <a href="/xray-mp-wiki/reagents/ligands/bptu/">BPTU</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collection statistics from Extended Data Table 1. 50.0-2.20 A resolution (2.30-2.20 A shell). Rmerge 10.1% (97.9% in shell).
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4m48">4M48</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNSIS</span><span class="topo-inside">DERETWSGKV</span><span class="topo-membrane">DFLLSVIGFAVDLANVWRFPYLC</span><span class="topo-outside">YKNGG</span><span class="topo-membrane">GAFLVPYGIMLAVGGIPLFY</span><span class="topo-inside">MELALGQHNRKGAITCWGRLVPLFKGIGY</span><span class="topo-membrane">AVVLIAFYVDFYYNVIIAWSLR</span><span class="topo-outside">FFFASF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">TNSLPWTSCNNIWNTPNCRPFESQGFQSAASEYFNRYILELNRSEGIHDLGAIKW</span><span class="topo-membrane">DMALCLLIVYLICYFSLW</span><span class="topo-inside">KGIST</span><span class="topo-membrane">SGKVVWFTALFPYAALLILLI</span><span class="topo-outside">RGLTLPGSFLGIQYYLTPNFS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">A</span><span class="topo-membrane">IYKAEVWADAATQVFFSLGPGFGVL</span><span class="topo-inside">LAYASYNKYHNNVYKD</span><span class="topo-membrane">ALLTSFINSATSFIAGFV</span><span class="topo-outside">IFSVLGYMAHTLGVRIEDVATEGPGLVFVVYPAAIATMPASTFWAL</span><span class="topo-membrane">IFFMMLATLGLDSS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">FGGSEAI</span><span class="topo-inside">ITALSDEFPKIKRNRELF</span><span class="topo-membrane">VAGLFSLYFVVGLASCT</span><span class="topo-outside">QGG</span><span class="topo-membrane">FYFFHLLDRYAAGYSILVAVFFEA</span><span class="topo-inside">IAVSWIYGTNRFSEDIRDMIGFPPG</span><span class="topo-unknown">RYWQVCWR</span><span class="topo-inside">F</span><span class="topo-membrane">VAPIFLLFITVYLLIGY</span></span>
<span class="topo-ruler">       490       500       510       520       530       540   </span>
<span class="topo-line"><span class="topo-membrane">EPL</span><span class="topo-outside">TYADYVYPS</span><span class="topo-membrane">WANALGWCIAGSSVVMIP</span><span class="topo-inside">AVAIFKLLSTPGSLRQRFTILTTPWRD</span><span class="topo-unknown">QQLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>5</td>
      <td>20</td>
      <td>24</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>15</td>
      <td>25</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>16</td>
      <td>38</td>
      <td>35</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>43</td>
      <td>58</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>63</td>
      <td>63</td>
      <td>82</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>64</td>
      <td>92</td>
      <td>83</td>
      <td>111</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>93</td>
      <td>114</td>
      <td>112</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>175</td>
      <td>134</td>
      <td>237</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>176</td>
      <td>193</td>
      <td>238</td>
      <td>255</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>194</td>
      <td>198</td>
      <td>256</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>199</td>
      <td>219</td>
      <td>261</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>241</td>
      <td>282</td>
      <td>303</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>266</td>
      <td>304</td>
      <td>328</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>282</td>
      <td>329</td>
      <td>344</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>300</td>
      <td>345</td>
      <td>362</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>301</td>
      <td>346</td>
      <td>363</td>
      <td>408</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>367</td>
      <td>409</td>
      <td>429</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>385</td>
      <td>430</td>
      <td>447</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>386</td>
      <td>402</td>
      <td>448</td>
      <td>464</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>403</td>
      <td>405</td>
      <td>465</td>
      <td>467</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>429</td>
      <td>468</td>
      <td>491</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>430</td>
      <td>454</td>
      <td>492</td>
      <td>516</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>462</td>
      <td>517</td>
      <td>524</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>463</td>
      <td>463</td>
      <td>525</td>
      <td>525</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>464</td>
      <td>483</td>
      <td>526</td>
      <td>545</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>484</td>
      <td>492</td>
      <td>546</td>
      <td>554</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>493</td>
      <td>510</td>
      <td>555</td>
      <td>572</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>511</td>
      <td>537</td>
      <td>573</td>
      <td>599</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>538</td>
      <td>543</td>
      <td>600</td>
      <td>605</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Two distinct ligand-binding sites

The P2Y1R structures reveal two distinct ligand-binding sites. [MRS2500](/xray-mp-wiki/reagents/ligands/mrs2500/) recognizes an orthosteric binding site within the seven transmembrane bundle, located closer to the extracellular surface than typical [GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) antagonist binding sites. [BPTU](/xray-mp-wiki/reagents/ligands/bptu/) binds to an allosteric pocket on the external receptor interface with the lipid bilayer, making it the first structurally characterized selective [GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) ligand located entirely outside of the helical bundle.

### MRS2500 orthosteric binding mode

[MRS2500](/xray-mp-wiki/reagents/ligands/mrs2500/) occupies a pocket defined by residues from the N terminus, ECL2, and helices VI and VII. The adenine ring inserts into a binding crevice with R287(6.62) and L44 on either side, and its N6H and N7 are coordinated by hydrogen bonds with N283(6.58). The 2-iodo group fits into a small sub-pocket shaped by the N terminus, interacting with the main chain carbonyl of C42. The N6-methyl group extends into a sub-pocket between helices VI and VII, forming hydrophobic interactions with A286(6.61) and N299(7.28). A salt bridge forms between [MRS2500](/xray-mp-wiki/reagents/ligands/mrs2500/) and R195. Key residues K46, R195, Y303(7.32), and Y306(7.35) surround the 3'-phosphate binding region.

### Distinct nucleotide binding between P2Y1R and P2Y12R

Despite recognizing the same endogenous ligand [ADP](/xray-mp-wiki/reagents/ligands/adp/), P2Y1R and P2Y12R reveal very different nucleotide-binding features. The [MRS2500](/xray-mp-wiki/reagents/ligands/mrs2500/) binding site in P2Y1R and the 2MeSADP binding site in P2Y12R are spatially distinct, with only minor overlap of phosphate binding regions near position 7.35. In P2Y1R, the adenine ring is adjacent to helices VI and VII, whereas in P2Y12R the adenine group reaches deep into the binding pocket for hydrophobic interactions with helices III and IV. The adenine groups adopt different orientations in the two receptors.

### BPTU allosteric binding at the lipid bilayer interface

[BPTU](/xray-mp-wiki/reagents/ligands/bptu/) binds to a shallow pocket on the external receptor interface with the lipid bilayer, not within the transmembrane bundle. The [Urea](/xray-mp-wiki/reagents/substrates/urea/) group forms two hydrogen bonds with the mainchain carbonyl of L102(2.55), which is available for bidentate coordination because P105(2.58) precludes intrahelical hydrogen bonding. The pyridyl group forms hydrophobic interactions with A106(2.59) and F119. The phenoxy benzene ring wedges into a cavity between helices II and III, interacting with T103(2.56), M123(3.24), L126(3.27), and Q127(3.28). The ligand likely enters the binding pocket via the lipid bilayer due to its high lipophilicity (HPLC logP = 5.7).

### P2Y1R selectivity determinant A106(2.59)

A106(2.59) is unique to P2Y1 among P2Y receptors; other subtypes have larger side chains at this position that would sterically hinder [BPTU](/xray-mp-wiki/reagents/ligands/bptu/) binding. Mutants A106(2.59)W/F/L lost [BPTU](/xray-mp-wiki/reagents/ligands/bptu/) binding ability while retaining recognition of nucleotide agonist 2MeSADP and antagonist [MRS2500](/xray-mp-wiki/reagents/ligands/mrs2500/). This explains the P2Y1R selectivity of diarylurea antagonists like [BPTU](/xray-mp-wiki/reagents/ligands/bptu/).

### GPCR structural comparison

The P2Y1R structures share a canonical seven-transmembrane helical bundle architecture with other class A GPCRs. Two disulfide bonds stabilize the extracellular loops: one connecting the N terminus to helix VII, and another connecting helix III to ECL2. The extracellular end of helix V is displaced by over 4 A compared to P2Y12R due to a helical kink, and helix III shifts away from the bundle axis by over 5 A. The intracellular halves of P2Y1R and P2Y12R are very similar.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/p2y12-receptor/">Human P2Y12 Receptor</a> — Direct structural comparison; related Gq-coupled vs Gi-coupled P2YR subfamilies
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL Fusion Protein</a> — BRIL fused to N-terminus of P2Y1R construct 2 for crystallization
- <a href="/xray-mp-wiki/reagents/ligands/mrs2500/">MRS2500</a> — Co-crystallized nucleotide antagonist (PDB 4M48)
- <a href="/xray-mp-wiki/reagents/ligands/bptu/">BPTU</a> — Co-crystallized non-nucleotide allosteric antagonist (PDB 4M49)
- <a href="/xray-mp-wiki/reagents/ligands/2me-sadp/">2-Methylthio-ADP (2MeSADP)</a> — Radiolabeled agonist analog used in binding assays for mutagenesis
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for membrane protein solubilization
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hemisuccinate (CHS)</a> — Lipid additive used in combination with DDM for protein stabilization
- <a href="/xray-mp-wiki/concepts/signaling-receptors/p2y-receptor-family/">P2Y Receptor Family</a> — P2Y1R is a Gq-coupled member of the P2Y purinergic GPCR family
- <a href="/xray-mp-wiki/concepts/signaling-receptors/g-protein/">G Protein</a> — Related protein
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr/">Gpcr</a> — Related protein
