---
title: "BioY - Biotin S Component from Lactococcus lactis"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1073##pnas.1203219109]
verified: false
---

# BioY - Biotin S Component from Lactococcus lactis

## Overview

BioY is the biotin-specific S component of the Energy-Coupling Factor (ECF) transporter from [Lactococcus lactis](/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter/). It is a six-transmembrane helix integral membrane protein that binds D-biotin with subnanomolar affinity (Kd 0.3 [NM](/xray-mp-wiki/reagents/detergents/nm/)) and delivers it to the ECF module (EcfA-EcfA'-EcfT) for ATP-driven translocation. BioY shares only 16% sequence identity with the thiamin-specific S component [Thit](/xray-mp-wiki/proteins/pumps-atpases/thit/) from the same organism, yet both interact with the same ECF module. The 2.1 A crystal structure revealed that S components contain a structurally conserved N-terminal domain (helices 1-3) involved in ECF module interaction and a highly divergent C-terminal domain (helices 4-6) that binds substrate. The conserved AXXXA motif in helix 1 is essential for ECF module interaction.


## Publications

### doi/10.1073##pnas.1203219109

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4dve">4DVE</a></td>
      <td>2.10</td>
      <td>C2</td>
      <td>SeMet-substituted BioY with N-terminal decahistidine tag</td>
      <td>D-biotin</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Lactococcus lactis strain NZ9000, grown semi-anaerobically in chemically defined medium (CDM) at 30 C; expression induced with 0.1% nisin A culture supernatant

- **Construct**: N-terminal decahistidine-tagged BioY; SeMet-substituted for crystallography
- **Notes**: Cells grown to OD600 1.5, then resuspended in CDM with SeMet instead of methionine for 20 min before induction. Harvested at OD600 4.


**Purification:**

- **Expression system**: L. lactis NZ9000
- **Expression construct**: N-terminal decahistidine-tagged BioY
- **Tag info**: Decahistidine tag (not removed)

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
      <td>Cell lysis</td>
      <td>Cell disruptor (Constant Systems)</td>
      <td>—</td>
      <td>50 mM Na-Hepes pH 7.5, 300 mM NaCl, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
      <td>Passed twice at 39 kpsi, 4 C. MgSO4 (5 mM) and DNase (100 ug/mL) added prior to disruption.</td>
    </tr>
    <tr>
      <td>Membrane collection</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td>50 mM Na-Hepes pH 7.5, 300 mM NaCl, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
      <td>Unbroken cells removed at 6,000 x g for 15 min. Membranes collected at 267,000 x g for 80 min, resuspended to 40 mg/mL, flash frozen.</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>1% (w/v) dodecyl-beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Membranes diluted to 5 mg/mL total protein in buffer A. 1 h at 4 C with gentle rotation. Unsolubilized material removed at 267,000 x g.</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Ni-Sepharose batch binding</td>
      <td>Ni-Sepharose</td>
      <td>50 mM Na-Hepes pH 7.5, 300 mM NaCl, 50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.35% (w/v) <a href="/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/">NG</a> (NG)</td>
      <td>15 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> added to supernatant before incubation with resin. Washed with 20 CV buffer B. Eluted with 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> in buffer B.</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>Superdex 200 10/300 GL</td>
      <td>20 mM Na-Hepes pH 7.5, 150 mM NaCl + 0.35% (w/v) NG</td>
      <td>Peak fractions concentrated to 7 mg/mL using Vivaspin 30 kDa MWCO concentrator.</td>
    </tr>
  </tbody>
</table>
**Final sample**: 7 mg/mL in 20 mM Na-Hepes pH 7.5, 150 mM NaCl, 0.35% NG

- **Expression system**: L. lactis NZ9000
- **Expression construct**: N-terminal decahistidine-tagged BioY (biotin-free)
- **Tag info**: Decahistidine tag (not removed)

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
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>50 mM potassium-phosphate pH 7.5, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 1% maltose-neopentyl glycol 3 (MNG-3)</td>
      <td>Alternative solubilization for biochemical characterization</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Ni-Sepharose</td>
      <td>Ni-Sepharose</td>
      <td>50 mM potassium phosphate pH 7.5, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.03% MNG-3</td>
      <td>Washed with 20 CV, eluted with 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Notes</td>
      <td>Crystallization details for SeMet-BioY. Protein at 7 mg/mL in 20 mM Na-Hepes pH 7.5, 150 mM NaCl, 0.35% NG. Crystals belong to space group C2.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4dve">4DVE</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MHHHHHHHH</span><span class="topo-outside">AMTNNQKVKTLTYS</span><span class="topo-membrane">AFMTAFIIILGFLPG</span><span class="topo-inside">IPIGFIPVPI</span><span class="topo-membrane">ILQNMGIMMAG</span><span class="topo-outside">G</span></span>
<span class="topo-line"><span class="topo-outside">LLGPKY</span><span class="topo-membrane">GTISVGAFLALALIGL</span><span class="topo-inside">PVLTGGNGGAASFLGPS</span><span class="topo-membrane">GGYRIAWLFTPFLI</span><span class="topo-outside">GFFLKKL</span></span>
<span class="topo-line"><span class="topo-outside">KITTSQNWFGEL</span><span class="topo-membrane">IIVLLFGVIFVDFVGAIW</span><span class="topo-inside">LSFQSNIP</span><span class="topo-unknown">LLTSLISN</span><span class="topo-membrane">LVFIPGDCIKAILT</span></span>
<span class="topo-line"><span class="topo-membrane">VVI</span><span class="topo-outside">VRRLRKQGGFELYFR</span></span>
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
      <td>9</td>
      <td>-9</td>
      <td>-1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>23</td>
      <td>0</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>38</td>
      <td>14</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>48</td>
      <td>29</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>59</td>
      <td>39</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>60</td>
      <td>66</td>
      <td>50</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>82</td>
      <td>57</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>99</td>
      <td>73</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>113</td>
      <td>90</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>132</td>
      <td>104</td>
      <td>122</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>150</td>
      <td>123</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>158</td>
      <td>141</td>
      <td>148</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>166</td>
      <td>149</td>
      <td>156</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>157</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>198</td>
      <td>174</td>
      <td>188</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Conserved N-terminal domain mediates ECF module interaction

BioY and [Thit](/xray-mp-wiki/proteins/pumps-atpases/thit/) share only 16% sequence identity but both interact with the same ECF module. The crystal structure reveals that helices 1-3 form a structurally conserved N-terminal domain (rmsd 5.1 A overall, but helices 1 and 3 superimpose well). The conserved AXXXA motif in helix 1 positions two alanine residues on the lipid-exposed face, essential for interaction with EcfT. This domain architecture explains how structurally divergent S components can interact with the same ECF module.

### Divergent C-terminal domain determines substrate specificity

Helices 4-6 form the highly variable C-terminal domain that binds the substrate. BioY binds D-biotin near the extracellular face, with the ligand mostly occluded except for the carboxylate tail accessible via a narrow tunnel. Biotin interacts with helices 4, 5, and 6 and the loop between helices 3 and 4. The structural divergence of this domain between BioY, [Thit](/xray-mp-wiki/proteins/pumps-atpases/thit/) (thiamin-specific), and [Ribu](/xray-mp-wiki/proteins/pumps-atpases/ribu/) (riboflavin-specific) reflects the chemical diversity of their respective substrates.

### BioY is monomeric and does not transport without ECF module

SEC-MALLS experiments confirm that BioY is monomeric in detergent solution, consistent with other S components ([Thit](/xray-mp-wiki/proteins/pumps-atpases/thit/), [Ribu](/xray-mp-wiki/proteins/pumps-atpases/ribu/)). Solitary BioY binds D-biotin with high affinity (Kd 0.3 [NM](/xray-mp-wiki/reagents/detergents/nm/), 1:1 stoichiometry) but does not transport substrate across the membrane in the absence of the ECF module. This demonstrates that S components are binding proteins that require the ECF module for transport, supporting a unifying mechanism for all ECF transporters.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/ecf-transporter/">ECF Transporter (Energy-Coupling Factor Transporter)</a> — BioY is the biotin-specific S component of ECF transporters from L. lactis
- <a href="/xray-mp-wiki/reagents/detergents/nm/">NM</a> — Referenced in the context of NM
- <a href="/xray-mp-wiki/proteins/pumps-atpases/thit/">Thit</a> — Referenced in the context of Thit
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Referenced in the context of DDM
- <a href="/xray-mp-wiki/reagents/detergents/n-nonyl-beta-d-glucopyranoside/">NG</a> — Referenced in the context of NG
- <a href="/xray-mp-wiki/proteins/pumps-atpases/ribu/">Ribu</a> — Referenced in the context of Ribu
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in the context of Glycerol
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Referenced in the context of Imidazole
