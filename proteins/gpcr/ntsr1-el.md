---
title: "NTSR1-EL Constitutively Active Mutant"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##srep38564]
verified: false
---

# NTSR1-EL Constitutively Active Mutant

## Overview

NTSR1-EL is a constitutively active mutant of the rat [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) receptor 1 ([NTSR1](/xray-mp-wiki/proteins/gpcr/neurotensin-receptor-1/)), a class A GPCR. It contains three thermostabilizing mutations from the parent NTSR1-GW5 construct (A86L, G215A, V360A) with the F358A mutation (7.42) retained, while wild-type residues are present at positions E166 (3.49) and L310 (6.37). The F358A mutation severs the hydrophobic cascade linking the ligand-binding pocket to the connector region, resulting in pronounced constitutive activity (IP production in the absence of agonist) but reduced [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) efficacy compared to wild-type. The crystal structure of NTSR1-EL-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) with bound NTS(8-13) was determined at 3.3 A resolution (PDB 5T04). Molecular dynamics simulations show that the connector residues remain tightly packed regardless of agonist presence, explaining the constitutive activity.


## Publications

### doi/10.1038##srep38564

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5t04">5T04</a></td>
      <td>3.3</td>
      <td>unknown</td>
      <td>Rat NTSR1-EL-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a>: Residues T43-K396 with mutations A86L(1.54), G215A(ECL2), F358A(7.42), V360A(7.44); ICL3 residues H269-E296 replaced by cysteine-free T4 lysozyme (N2-Y161, C54T, C97A) with GSGS linker; C-terminal deca-histidine tag</td>
      <td>NTS(8-13) agonist peptide</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression)
- **Construct**: NTSR1-EL-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) with hemagglutinin signal peptide and [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) replacing ICL3

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
      <td>Expression</td>
      <td>Baculovirus expression in Sf9 insect cells</td>
      <td>—</td>
      <td>Not specified</td>
      <td>NTSR1-EL-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> construct expressed via baculovirus</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Urea-washed P2 insect cell membranes</td>
      <td>—</td>
      <td>Not specified</td>
      <td>Membranes washed with <a href="/xray-mp-wiki/reagents/substrates/urea/">UREA</a> to remove peripherally bound proteins</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/CHS detergent</td>
      <td>—</td>
      <td>50 mM TrisHCl pH 7.4, 30% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 200 mM NaCl, 1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 10 uM NTS(8-13) + 1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Solubilized for 2 h at 4 C. NaCl adjusted to 200 mM. Final volume 280 mL. Clarified by centrifugation at 125,000 g for 1 h.</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> resin (Co-NTA)</td>
      <td>—</td>
      <td>50 mM TrisHCl pH 7.4, 30% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 200 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 1 uM NTS(8-13), 0.1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Batch incubation overnight. Washed with Talon-A+ and Talon-A2+ buffers. Eluted with 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> in Talon-B+ buffer (0.05% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/0.005% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 10 uM NTS(8-13)). Peak fractions collected (2.5 mL).</td>
    </tr>
    <tr>
      <td>Desalting</td>
      <td>PD10 desalting column</td>
      <td>—</td>
      <td>50 mM TrisHCl pH 7.4, 200 mM NaCl, 0.003% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/0.0003% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.003% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>/0.0003% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Desalted into PD10 buffer. NTS(8-13) added to 20 uM after desalting. ~3.3 mg from 3 L culture.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Purified NTSR1-EL-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> adjusted to 100 uM TCEP and 350 uM NTS(8-13), concentrated to ~60 mg/mL. Mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>:<a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> (10:1) in LCP using two-syringe method. 60-70 nL drops dispensed onto Laminex plates. Crystals grown at 20 C.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5t04">5T04</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">DYKDDDDATS</span><span class="topo-inside">TSESDTAGPNSDLDVNTDIY</span><span class="topo-membrane">SKVLVTAIYLALFVVGTVGNSVTLFTLA</span><span class="topo-outside">R</span><span class="topo-unknown">K</span></span>
<span class="topo-line"><span class="topo-unknown">KSLQSLQ</span><span class="topo-outside">STVHY</span><span class="topo-membrane">HLGSLALSDLLILLLAMPVELYNFIW</span><span class="topo-inside">VHHPWAFGD</span><span class="topo-membrane">AGCRGYYFLRDAC</span></span>
<span class="topo-line"><span class="topo-membrane">TYATALNVASLS</span><span class="topo-outside">VERYLAICHPFKAKTLMSRSRTKK</span><span class="topo-membrane">FISAIWLASALLAIPMLFTMG</span><span class="topo-inside">LQN</span></span>
<span class="topo-line"><span class="topo-inside">RSADGTHPGGLVCTPIVDT</span><span class="topo-membrane">ATVKVVIQVNTFMSFLFPMLVISIL</span><span class="topo-outside">NTVIANKLTVMVNIFE</span></span>
<span class="topo-line"><span class="topo-outside">MLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEK</span></span>
<span class="topo-line"><span class="topo-outside">LFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLNNKR</span></span>
<span class="topo-line"><span class="topo-outside">WDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYGSGSPGRVQALRHGVL</span><span class="topo-membrane">VLRAVVIA</span></span>
<span class="topo-line"><span class="topo-membrane">FVVCWLPYHVRRLMFCYI</span><span class="topo-inside">SDEQWTTFLFDF</span><span class="topo-membrane">YHYFYMLTNALAYASSAINPILYN</span><span class="topo-outside">LV</span><span class="topo-unknown">SANF</span></span>
<span class="topo-line"><span class="topo-unknown">RQVFLSTLACLCPGWRHRRKAHHHHHHHHHHGG</span></span>
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
      <td>11</td>
      <td>30</td>
      <td>43</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>58</td>
      <td>63</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>59</td>
      <td>59</td>
      <td>91</td>
      <td>91</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>68</td>
      <td>72</td>
      <td>100</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>98</td>
      <td>105</td>
      <td>130</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>107</td>
      <td>131</td>
      <td>139</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>132</td>
      <td>140</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>156</td>
      <td>165</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>177</td>
      <td>189</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>199</td>
      <td>210</td>
      <td>231</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>224</td>
      <td>232</td>
      <td>256</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>412</td>
      <td>257</td>
      <td>308</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>413</td>
      <td>438</td>
      <td>309</td>
      <td>334</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>439</td>
      <td>450</td>
      <td>335</td>
      <td>346</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>451</td>
      <td>474</td>
      <td>347</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>475</td>
      <td>476</td>
      <td>371</td>
      <td>372</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### F358A severs the hydrophobic cascade

In NTSR1-EL, the F358A mutation removes the aromatic side chain at position 7.42, severing a network of van der Waals contacts (the hydrophobic cascade) involving Y324(6.51), F358(7.42), W321(6.48), and F317(6.44). This network is intact in NTSR1-ELF. The disruption causes W321(6.48) to adopt a perpendicular side chain orientation (chi2 angle of 103 deg) compared to the parallel orientation in NTSR1-ELF (chi2 ~55 deg).

### Constitutive activity from tight connector packing

MD simulations show that NTSR1-EL maintains tight packing of connector residues A157(3.40)-P249(5.50)-F317(6.44) regardless of agonist presence. In contrast, NTSR1-ELF shows tight packing only with agonist and looser packing without agonist. This constitutively packed connector correlates with the pronounced basal IP production of NTSR1-EL in the absence of [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/).

### Reduced NTS efficacy due to uncoupled binding pocket

The severing of the hydrophobic cascade in NTSR1-EL uncouples the ligand-binding pocket from the connector region. This reduces the ability of bound NTS to propagate conformational changes, explaining the reduced fold-stimulation of IP production by NTS in NTSR1-EL compared to NTSR1-ELF and wild-type.

### Increased flexibility at G protein interface

MD simulations show that NTSR1-EL displays a more open intracellular cleft between TM3 and TM6 and fewer interhelical contacts in the intracellular half of the receptor compared to NTSR1-ELF. This suggests that the constitutively active conformation has higher conformational flexibility that facilitates the initial docking of G protein in the absence of agonist.

### Distinct agonist binding mode

The NTSR1-EL crystal structure reveals subtle differences in NTS(8-13) binding compared to NTSR1-ELF. TM5 movement allows Arg9 of NTS to form a hydrogen bond with T231(5.32) that is absent in NTSR1-ELF. Hydrogen bonds between the NTS C-terminal carboxylate of Leu13 and Y351(7.35)/R328(6.55) are lost in NTSR1-EL. Instead, R328(6.55) engages N241(5.42).


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/neurotensin-receptor-1/">Rat Neurotensin Receptor 1 (NTSR1)</a> — NTSR1-EL is a constitutively active mutant derivative of NTSR1
- <a href="/xray-mp-wiki/proteins/gpcr/ntsr1-lf/">NTSR1-LF Mutant</a> — Related thermostabilized mutant; NTSR1-EL compared with NTSR1-LF and NTSR1-ELF for G protein activation
- <a href="/xray-mp-wiki/proteins/gpcr/tm86v-delta-ic3a/">TM86V-deltaIC3A NTSR1 Mutant</a> — Inactive-state NTSR1 mutant used for comparison with NTSR1-EL connector region
- <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4 Lysozyme (T4L)</a> — T4L fusion replacing ICL3 in NTSR1-EL-T4L crystallization construct
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">Lauryl Maltose Neopentyl Glycol (LMNG)</a> — Detergent used for solubilization, purification, and crystallization of NTSR1-EL-T4L
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">Cholesteryl Hemisuccinate (CHS)</a> — CHS used in combination with LMNG for solubilization and LCP crystallization
- <a href="/xray-mp-wiki/reagents/ligands/neurotensin/">Neurotensin (NTS)</a> — Endogenous agonist peptide used in co-crystallization of NTSR1-EL
- <a href="/xray-mp-wiki/reagents/ligands/sr48692/">SR48692</a> — Non-peptide antagonist used in docking studies with NTSR1 for comparison
- <a href="/xray-mp-wiki/concepts/gpcr-activation-mechanism/">GPCR Activation Mechanism</a> — NTSR1-EL provides insights into the structural basis of GPCR constitutive activity
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
