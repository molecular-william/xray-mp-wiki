---
title: "NsXeR (Xenorhodopsin from Nanosalina)"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.1603187]
verified: false
---

# NsXeR (Xenorhodopsin from Nanosalina)

## Overview

NsXeR is a light-driven inward proton pump (xenorhodopsin) from the nanohaloarchaeon Nanosalina, belonging to the xenorhodopsin (XeR) family of microbial rhodopsins. It functions as an inwardly directed H+ pump, generating a depolarizing current that can elicit action potentials in rat hippocampal neurons. The crystal structure was determined at 2.5 Å resolution by the in meso (LCP) method, revealing a seven-transmembrane α-helix architecture (A-G) with a covalently bound all-trans retinal cofactor via Lys213 Schiff base. The protein forms a trimer in the asymmetric unit (P2₁2₁2₁ space group). Key structural features include a proton uptake cavity accessible from the bulk through Gln122, a unique His48-Asp220 proton acceptor pair (analogous to PRs), and a chain of strong hydrogen bonds (Ile6-Thr199-w5-Ser13-Ser202-w3-Trp73) connecting the extracellular side with the active center. Pro209 is critical for pumping activity, replacing the Asp212 found in bacteriorhodopsin. The photocycle has a turnover rate of ~160 s⁻¹, making NsXeR suitable for optogenetic applications at neuronal firing frequencies up to 40-80 Hz.

## Publications

### doi/10.1126##sciadv.1603187

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6eyu">6EYU</a></td>
      <td>2.50</td>
      <td>P2_12_12_1</td>
      <td>Full-length NsXeR from Nanosalina with C-terminal LEHHHHHH tag</td>
      <td>all-trans retinal (covalently bound to Lys213)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41 (DE3)
- **Construct**: NsXeR with C-terminal LEHHHHHH tag in pET15b

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
      <td>Cell growth and membrane preparation</td>
      <td>E. coli cells transformed with pET15b-NsXeR, grown in autoinducing medium ZYP-5052 at 37°C with 100 mg/L <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a>. Induced at OD600 0.6-0.7 with 1 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a>. 10 μM all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> supplemented. Cells disrupted in M-110P Lab Homogenizer at 25,000 psi. Membrane fraction isolated by ultracentrifugation at 90,000g for 1 h at 4°C.</td>
      <td>--</td>
      <td>20 mM Tris-HCl pH 8.0, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.5% Triton X-100, 50 mg/L DNase I + 0.5% Triton X-100</td>
      <td>Cells disrupted in lysis buffer</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane pellet resuspended in solubilization buffer and stirred overnight at 4°C. Insoluble fraction removed by ultracentrifugation at 90,000g for 1 h.</td>
      <td>--</td>
      <td>50 mM NaH2PO4/Na2HPO4 pH 8.0, 0.1 M NaCl, 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (Ni-NTA)</td>
      <td>Supernatant loaded onto Ni-NTA column. Eluted with <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>.</td>
      <td>Ni-NTA (Qiagen)</td>
      <td>50 mM NaH2PO4/Na2HPO4 pH 7.5, 0.1 M NaCl, 0.3 M <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluate dialyzed against 100 volumes of 50 mM NaH2PO4/Na2HPO4 pH 7.5, 0.1 M NaCl buffer twice for 2 h to remove <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>. Protein concentrated to 70 mg/mL for crystallization.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization (in meso)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>30 mg/mL NsXeR (mixed with monoolein-based LCP at 1:1 ratio)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22°C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1-4 weeks</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in 96-well LCP glass sandwich plates using NT8 crystallization robot. 150 nL protein-mesophase mixture overlaid with 600 nL precipitant. Crystal appearance in 1-4 weeks. Space group P2₁2₁2₁ with one trimer per asymmetric unit. X-ray data collected at ESRF ID23-1, ID29, and ID30B beamlines at 0.969 and 0.972 Å with PILATUS 6M detector. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using <a href="/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-2/">Archaerhodopsin-2</a> (PDB 2EI4) with MoRDa pipeline. Refined with REFMAC5 and PHENIX.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6eyu">6EYU</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">VYEAIT</span><span class="topo-outside">AGGFGSQPF</span><span class="topo-membrane">ILAYIITAMISGLLFLY</span><span class="topo-inside">LPRKLDVPQKFG</span><span class="topo-membrane">IIHFFIVVWSGLMYT</span></span>
<span class="topo-line"><span class="topo-outside">NFLNQSFLSDYA</span><span class="topo-membrane">WYMDWMVSTPLILLAL</span><span class="topo-inside">GLTAFHGADTKRYDLLG</span><span class="topo-membrane">ALLGAEFTLVITGLL</span></span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-outside">QAQGSIT</span><span class="topo-membrane">PYYVGVLLLLGVVYLLA</span><span class="topo-inside">KPFREIAEESSDGLARAYKIL</span><span class="topo-membrane">AGYIGIFFLSYPTV</span></span>
<span class="topo-line"><span class="topo-membrane">WY</span><span class="topo-outside">ISGIDALPGSLNILDPTQTSI</span><span class="topo-membrane">ALVVLPFFCKQVYGFLD</span><span class="topo-inside">MYLIHKAELEHH</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>16</td>
      <td>8</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>33</td>
      <td>17</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>45</td>
      <td>34</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>60</td>
      <td>46</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>72</td>
      <td>61</td>
      <td>72</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>73</td>
      <td>88</td>
      <td>73</td>
      <td>88</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>105</td>
      <td>89</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>121</td>
      <td>106</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>128</td>
      <td>122</td>
      <td>128</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>145</td>
      <td>129</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>166</td>
      <td>146</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>182</td>
      <td>167</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>203</td>
      <td>183</td>
      <td>203</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>220</td>
      <td>204</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>232</td>
      <td>221</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6eyu">6EYU</a> — Chain B (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">MVYEAITAGGFGSQPF</span><span class="topo-membrane">ILAYIITAMISGLLFLY</span><span class="topo-inside">LPRKLDVPQKFG</span><span class="topo-membrane">IIHFFIVVWSGLMYT</span></span>
<span class="topo-line"><span class="topo-outside">NFLNQSFLSDY</span><span class="topo-membrane">AWYMDWMVSTPLILLA</span><span class="topo-inside">LGLTAFHGADTKRYDLLG</span><span class="topo-membrane">ALLGAEFTLVITGLL</span></span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-outside">QAQGSI</span><span class="topo-membrane">TPYYVGVLLLLGVVY</span><span class="topo-inside">LLAKPFREIAEESSDGLARAYKILAG</span><span class="topo-membrane">YIGIFFLSYPTV</span></span>
<span class="topo-line"><span class="topo-membrane">WYI</span><span class="topo-outside">SGIDALPGSLNILDPTQT</span><span class="topo-membrane">SIALVVLPFFCKQVYGFL</span><span class="topo-inside">DMYLIHKAELEHH</span></span>
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
      <td>16</td>
      <td>1</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>33</td>
      <td>17</td>
      <td>33</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>45</td>
      <td>34</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>60</td>
      <td>46</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>71</td>
      <td>61</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>87</td>
      <td>72</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>105</td>
      <td>88</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>121</td>
      <td>106</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>127</td>
      <td>122</td>
      <td>127</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>142</td>
      <td>128</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>168</td>
      <td>143</td>
      <td>168</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>169</td>
      <td>183</td>
      <td>169</td>
      <td>183</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>201</td>
      <td>184</td>
      <td>201</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>202</td>
      <td>219</td>
      <td>202</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>232</td>
      <td>220</td>
      <td>232</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6eyu">6EYU</a> — Chain C (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-unknown">VYEAIT</span><span class="topo-outside">AGGFGSQPF</span><span class="topo-membrane">ILAYIITAMISGLLFL</span><span class="topo-inside">YLPRKLDVPQKFGI</span><span class="topo-membrane">IHFFIVVWSGLMYT</span></span>
<span class="topo-line"><span class="topo-outside">NFLNQSFLSDY</span><span class="topo-membrane">AWYMDWMVSTPLILLA</span><span class="topo-inside">LGLTAFHGADTKRYDLLG</span><span class="topo-membrane">ALLGAEFTLVITGLL</span></span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-outside">QAQGSIT</span><span class="topo-membrane">PYYVGVLLLLGVVYLL</span><span class="topo-inside">AKPFREIAEESSDGLARAYKIL</span><span class="topo-membrane">AGYIGIFFLSYPTV</span></span>
<span class="topo-line"><span class="topo-membrane">WY</span><span class="topo-outside">ISGIDALPGSLNILDPTQTSI</span><span class="topo-membrane">ALVVLPFFCKQVYGFL</span><span class="topo-inside">DMYLIHKAEL</span><span class="topo-unknown">EHH</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>16</td>
      <td>8</td>
      <td>16</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>32</td>
      <td>17</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>46</td>
      <td>33</td>
      <td>46</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>60</td>
      <td>47</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>71</td>
      <td>61</td>
      <td>71</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>87</td>
      <td>72</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>105</td>
      <td>88</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>121</td>
      <td>106</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>128</td>
      <td>122</td>
      <td>128</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>144</td>
      <td>129</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>166</td>
      <td>145</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>167</td>
      <td>182</td>
      <td>167</td>
      <td>182</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>203</td>
      <td>183</td>
      <td>203</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>219</td>
      <td>204</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>229</td>
      <td>220</td>
      <td>229</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Inward proton pumping mechanism

NsXeR is an inwardly directed proton pump, demonstrated by pH changes in E. coli cell suspensions and liposome experiments. Upon illumination, the pH of the cell suspension increases (H+ uptake), opposite to the behavior of outward pumps like bacteriorhodopsin. The effect is abolished by CCCP, confirming active proton transport. Pumping activity is maintained across a wide pH range (pH 5-9).

### Unique proton acceptor pair His48-Asp220

NsXeR features a His48-Asp220 pair as the proton acceptor, analogous to proteorhodopsins but unique among known microbial rhodopsins. His48 is not present at a similar position in other rhodopsins and is essential for retinal binding. Asp220 substitution with Asn completely disrupts pumping. These residues are connected via a hydrogen bond and located 10-12 Å from the Schiff base.

### Distinct proton translocation pathway

The NsXeR structure reveals a proton translocation pathway distinct from bacteriorhodopsin. A proton uptake cavity accessible through Gln122 is filled with water molecules. Pro209 replaces the conserved Asp212 of BR and is critical for pumping. The protein lacks an ionizable residue at the position equivalent to BR Asp96 (Ala71 in NsXeR). A chain of strong hydrogen bonds (Ile6-Thr199-w5-Ser13-Ser202-w3-Trp73) connects the extracellular bulk to the active center. Trp73 separates the active center from the proton uptake pathway and substitution of this residue disrupts pumping.

### Optogenetic application for neuronal activation

NsXeR was functionally expressed in HEK293 cells, NG108-15 cells, and rat hippocampal neurons using adeno-associated virus-mediated gene transfer. Photocurrents of 40-150 pA at -60 mV (current density 1.4 ± 0.5 pA/pF) were recorded in HEK cells. In rat hippocampal neurons, photocurrents of -189 ± 80 pA at -70 mV (6.7 ± 4.4 pA/pF) were sufficient to elicit action potentials at frequencies up to 40-80 Hz, matching the maximal intrinsic firing frequency of hippocampal neurons. Light pulses as short as 3 ms were sufficient to trigger spiking, shorter than the pump turnover time (6.2 ± 2.8 ms).

### Photocycle with 160 s⁻¹ turnover rate

The NsXeR photocycle in nanodiscs is 27 ms (faster than in liposomes at 50 ms). The 160 s⁻¹ turnover rate is approximately 10-fold faster than PoXeR from Parvularcula oceani. Time-resolved photocurrent measurements reveal two relaxation times: τ₁ = 1.1 ms (MI/MII transition) and τ₂ = 11.6 ms (M2 decay). At physiological membrane potential (-60 mV), τ₂ = 6.2 ms, enabling the high turnover rate.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/bcxer/">BcXeR (Xenorhodopsin from Bacillus coahuilensis)</a> — Related bacterial xenorhodopsin with similar inward proton pumping function and detailed proton wire mechanism
- <a href="/xray-mp-wiki/proteins/rhodopsins/schizorhodopsin/">Schizorhodopsin SzR4</a> — Another class of inward proton pumps from Asgard archaea, providing a mechanistic comparison to XeRs
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/microbial-rhodopsins/">Microbial Rhodopsins</a> — NsXeR is a member of the microbial rhodopsin family
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/">Rhodopsin Photocycle</a> — NsXeR exhibits a photocycle with MI and M2 intermediate states
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a> — All-trans retinal is the chromophore covalently bound via Schiff base to Lys213
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — NsXeR was crystallized using the in meso (LCP) method
- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> — Archetypal outward proton pump for comparison of pumping mechanisms
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/rhodopsins/archaerhodopsin-2/">Archaerhodopsin-2</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/sodium-malonate/">Sodium Malonate</a> — Additive used in purification or crystallization buffers
