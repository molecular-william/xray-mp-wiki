---
title: "Transhydrogenase dII Domain (Thermus thermophilus)"
created: 2026-05-29
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2017.05.022, doi/10.1126##science.1260451]
verified: agent
uniprot_id: ['Q72GR8', 'Q72GR9', 'Q72GS0']
---

# Transhydrogenase dII Domain (Thermus thermophilus)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q72GR8">UniProt: Q72GR8</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q72GR9">UniProt: Q72GR9</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q72GS0">UniProt: Q72GS0</a>

<span class="expr-badge">Thermus thermophilus</span>

## Overview

The transhydrogenase dII domain from Thermus thermophilus is the transmembrane proton channel component of the nicotinamide nucleotide transhydrogenase (TH), a proton-translocating membrane enzyme that uses the proton-motive force to drive hydride transfer from NADH to NADP+. The first crystal structures of TH from Thermus thermophilus were determined at 2.8 A (membrane domain, PDB 4O93) and 6.9 A (holo-TH, PDB 4O9U) resolution (Leung et al., Science, 2015). The holo-TH is a dimer with each protomer consisting of two hydrophilic nucleotide-binding domains (dI and dIII) and a transmembrane domain (dII). The dII domain serves as the proton channel, and subsequent higher-resolution structures (2.2 A, PDB 5UNI) revealed key residues and water molecules involved in proton translocation across the membrane.

## Publications

### doi/10.1016##j.str.2017.05.022

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5uni">5UNI</a></td>
      <td>2.2</td>
      <td>C2221</td>
      <td>dII domain, alpha2 chain (residues 1-94) + truncated beta chain (residues 1-261)</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a> 8.7</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21DE3 ΔA
- **Construct**: Complete operon of TH from T. thermophilus (alpha2 + beta) with C-terminal His-tag, co-expressed with polypeptide alpha1 in pETDuet-1 vector


**Purification:**

- **Expression system**: E. coli BL21DE3 ΔA
- **Expression construct**: C-terminal His-tag

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
      <td>Overexpression</td>
      <td>Fermentation</td>
      <td>--</td>
      <td>LB with appropriate antibiotics + --</td>
      <td>pETDuet-1 vector, co-expression of alpha2+beta and alpha1</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Cell lysis</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Overexpressed bacterial membranes harvested</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>6xHis affinity resin</td>
      <td>-- + --</td>
      <td>6xHis <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography</td>
      <td>Superose 6</td>
      <td>0.05 M Tris pH 8.0, 0.1 M NaCl, 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Superose 6 gel filtration chromatography</td>
    </tr>
  </tbody>
</table>
**Final sample**: 60 mg/ml in 0.05 M Tris pH 8.0, 0.1 M NaCl, 0.01% [DDM](/xray-mp-wiki/reagents/detergents/ddm/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>60 mg/ml dII domain in 0.05 M Tris pH 8.0, 0.1 M NaCl, 0.01% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a> 8.7</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>1:1</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>dII domain</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a> 8.7</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>1:1</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5uni">5UNI</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90    </span>
<span class="topo-line"><span class="topo-outside">MEFGFWS</span><span class="topo-membrane">ALYIFVLTCFLGYEL</span><span class="topo-inside">ITRVPVILHTPLMS</span><span class="topo-membrane">GSNFIHGVVVVGAM</span><span class="topo-outside">VVLGHAETGLEKLIGF</span><span class="topo-membrane">LGVILGAANAAGGYA</span><span class="topo-inside">VTVRMLEMFERKP</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>22</td>
      <td>8</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>36</td>
      <td>23</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>50</td>
      <td>37</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>66</td>
      <td>51</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>81</td>
      <td>67</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>94</td>
      <td>82</td>
      <td>94</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5uni">5UNI</a> — Chain B (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MDLIQA</span><span class="topo-membrane">AYFVVAILFIVGLK</span><span class="topo-inside">RMAHPTTAKSG</span><span class="topo-membrane">IVWAGWGMVLAVLA</span><span class="topo-outside">TFFWPGMGNFALIL</span><span class="topo-membrane">LALLLGSVVAWWAA</span><span class="topo-inside">VRVAMTDMPQM</span><span class="topo-membrane">VAIYNGMGGGAAATIA</span><span class="topo-outside">AVELLKGAFENTGLMAL</span><span class="topo-membrane">AIL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGLIGSVAFTGSLIAFA</span><span class="topo-inside">KLQGIMKSRPILFPG</span><span class="topo-membrane">QKAVNALVLALTVVIGL</span><span class="topo-outside">SLLWNDATASIVL</span><span class="topo-membrane">FFLLALLFGVLMTL</span><span class="topo-inside">PIGGGDMPVAISF</span><span class="topo-membrane">YNAFTGMAVGFEGF</span><span class="topo-outside">AVGN</span><span class="topo-membrane">PALMVAGTLVGAA</span></span>
<span class="topo-ruler">       250       260    </span>
<span class="topo-line"><span class="topo-membrane">GT</span><span class="topo-inside">LLTVLMARAMNRSVWISVL</span><span class="topo-unknown">VGG</span></span>
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
      <td>1</td>
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>20</td>
      <td>7</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>21</td>
      <td>31</td>
      <td>21</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>45</td>
      <td>32</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>59</td>
      <td>46</td>
      <td>59</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>73</td>
      <td>60</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>84</td>
      <td>74</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>100</td>
      <td>85</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>117</td>
      <td>101</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>137</td>
      <td>118</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>152</td>
      <td>138</td>
      <td>152</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>169</td>
      <td>153</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>182</td>
      <td>170</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>196</td>
      <td>183</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>209</td>
      <td>197</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>223</td>
      <td>210</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>227</td>
      <td>224</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>242</td>
      <td>228</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>261</td>
      <td>243</td>
      <td>261</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5uni">5UNI</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90    </span>
<span class="topo-line"><span class="topo-outside">MEFGFWS</span><span class="topo-membrane">ALYIFVLTCFLGYEL</span><span class="topo-inside">ITRVPVILHTPLMS</span><span class="topo-membrane">GSNFIHGVVVVGAM</span><span class="topo-outside">VVLGHAETGLEKLIGF</span><span class="topo-membrane">LGVILGAANAAGGYA</span><span class="topo-inside">VTVRMLEMFERKP</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>22</td>
      <td>8</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>36</td>
      <td>23</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>50</td>
      <td>37</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>66</td>
      <td>51</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>81</td>
      <td>67</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>94</td>
      <td>82</td>
      <td>94</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5uni">5UNI</a> — Chain D (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MDLIQA</span><span class="topo-membrane">AYFVVAILFIVGLK</span><span class="topo-inside">RMAHPTTAKSG</span><span class="topo-membrane">IVWAGWGMVLAVLA</span><span class="topo-outside">TFFWPGMGNFALIL</span><span class="topo-membrane">LALLLGSVVAWWAA</span><span class="topo-inside">VRVAMTDMPQM</span><span class="topo-membrane">VAIYNGMGGGAAATIA</span><span class="topo-outside">AVELLKGAFENTGLMAL</span><span class="topo-membrane">AIL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGLIGSVAFTGSLIAFA</span><span class="topo-inside">KLQGIMKSRPILFPG</span><span class="topo-membrane">QKAVNALVLALTVVIGL</span><span class="topo-outside">SLLWNDATASIVL</span><span class="topo-membrane">FFLLALLFGVLMTL</span><span class="topo-inside">PIGGGDMPVAISF</span><span class="topo-membrane">YNAFTGMAVGFEGF</span><span class="topo-outside">AVGN</span><span class="topo-membrane">PALMVAGTLVGAA</span></span>
<span class="topo-ruler">       250       260    </span>
<span class="topo-line"><span class="topo-membrane">GT</span><span class="topo-inside">LLTVLMARAMNRSVWISVL</span><span class="topo-unknown">VGG</span></span>
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
      <td>1</td>
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>20</td>
      <td>7</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>21</td>
      <td>31</td>
      <td>21</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>45</td>
      <td>32</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>59</td>
      <td>46</td>
      <td>59</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>73</td>
      <td>60</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>84</td>
      <td>74</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>100</td>
      <td>85</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>117</td>
      <td>101</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>137</td>
      <td>118</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>152</td>
      <td>138</td>
      <td>152</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>169</td>
      <td>153</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>182</td>
      <td>170</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>196</td>
      <td>183</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>209</td>
      <td>197</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>223</td>
      <td>210</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>227</td>
      <td>224</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>242</td>
      <td>228</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>261</td>
      <td>243</td>
      <td>261</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1126##science.1260451

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4o93">4O93</a></td>
      <td>2.77</td>
      <td>C 1 2 1</td>
      <td>dII domain dimer (transmembrane proton channel domain) from Thermus thermophilus transhydrogenase</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4o9p">4O9P</a></td>
      <td>2.89</td>
      <td>P 1 2_1 1</td>
      <td>dII domain dimer (SeMet derivative) from Thermus thermophilus transhydrogenase</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4o9u">4O9U</a></td>
      <td>6.93</td>
      <td>C 1 2 1</td>
      <td>Holo-TH entire enzyme dimer from Thermus thermophilus transhydrogenase</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4o9t">4O9T</a></td>
      <td>3.08</td>
      <td>P 1 2_1 1</td>
      <td>Holo-TH entire enzyme dimer from Thermus thermophilus transhydrogenase, alternative crystal form</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21DE3 ΔA
- **Construct**: Complete operon of TH from T. thermophilus (alpha2 + beta) with C-terminal His-tag, co-expressed with polypeptide alpha1 in pETDuet-1 vector


<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o93">4O93</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90    </span>
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-membrane">EFGFWSALYIFVLTCFLGY</span><span class="topo-inside">ELITRVPVILHTPLMSGS</span><span class="topo-membrane">NFIHGVVVVGAMVVL</span><span class="topo-outside">GHAETGLEKL</span><span class="topo-membrane">IGFLGVILGAANAAGGY</span><span class="topo-inside">AVTVRMLEMFERKP</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>20</td>
      <td>2</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>21</td>
      <td>38</td>
      <td>21</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>53</td>
      <td>39</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>63</td>
      <td>54</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>80</td>
      <td>64</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>94</td>
      <td>81</td>
      <td>94</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o93">4O93</a> — Chain B (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MD</span><span class="topo-membrane">LIQAAYFVVAILFIVGL</span><span class="topo-inside">KRMAHPTTAKSGIV</span><span class="topo-membrane">WAGWGMVLAVLATFF</span><span class="topo-outside">WPGMGNF</span><span class="topo-membrane">ALILLALLLGSVVAWW</span><span class="topo-inside">AAVRVAMTDMPQMVAI</span><span class="topo-membrane">YNGMGGGAAATIAAV</span><span class="topo-outside">ELLKGAFENTGLMA</span><span class="topo-membrane">LAIL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGLIGSVAFTGSLI</span><span class="topo-inside">AFAKLQGIMKSRPILFPG</span><span class="topo-membrane">QKAVNALVLALTVVIGL</span><span class="topo-outside">SLLWNDATASI</span><span class="topo-membrane">VLFFLLALLFGVLMT</span><span class="topo-inside">LPIGGGDMPVAISF</span><span class="topo-membrane">YNAFTGMAVGFEGFAVG</span><span class="topo-outside">N</span><span class="topo-membrane">PALMVAGTLVGAA</span></span>
<span class="topo-ruler">       250       260       270</span>
<span class="topo-line"><span class="topo-membrane">GT</span><span class="topo-inside">LLTVLMARAMNRSVWISVLVGG</span><span class="topo-unknown">HHHHHH</span></span>
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
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>19</td>
      <td>3</td>
      <td>19</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>20</td>
      <td>33</td>
      <td>20</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>48</td>
      <td>34</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>55</td>
      <td>49</td>
      <td>55</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>71</td>
      <td>56</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>87</td>
      <td>72</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>102</td>
      <td>88</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>116</td>
      <td>103</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>134</td>
      <td>117</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>152</td>
      <td>135</td>
      <td>152</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>169</td>
      <td>153</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>180</td>
      <td>170</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>195</td>
      <td>181</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>209</td>
      <td>196</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>226</td>
      <td>210</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>227</td>
      <td>227</td>
      <td>227</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>242</td>
      <td>228</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>264</td>
      <td>243</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o93">4O93</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90    </span>
<span class="topo-line"><span class="topo-outside">MEFGF</span><span class="topo-membrane">WSALYIFVLTCFLGY</span><span class="topo-inside">ELITRVPVILHTPLMSGS</span><span class="topo-membrane">NFIHGVVVVGAMVVL</span><span class="topo-outside">GHAETGLEKL</span><span class="topo-membrane">IGFLGVILGAANAAGGY</span><span class="topo-inside">AVTVRMLEMF</span><span class="topo-unknown">ERKP</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>1</td>
      <td>5</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>20</td>
      <td>6</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>21</td>
      <td>38</td>
      <td>21</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>53</td>
      <td>39</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>63</td>
      <td>54</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>80</td>
      <td>64</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>90</td>
      <td>81</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o93">4O93</a> — Chain D (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MDL</span><span class="topo-membrane">IQAAYFVVAILFIVGL</span><span class="topo-inside">KRMAHPTTAKSGIV</span><span class="topo-membrane">WAGWGMVLAVLATFF</span><span class="topo-outside">WPGMGNFA</span><span class="topo-membrane">LILLALLLGSVVAWWA</span><span class="topo-inside">AVRVAMTDMPQMVA</span><span class="topo-membrane">IYNGMGGGAAATIAA</span><span class="topo-outside">VELLKGAFENTGLMA</span><span class="topo-membrane">LAIL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGLIGSVAFTGSLI</span><span class="topo-inside">AFAKLQGIMKSRPILFPG</span><span class="topo-membrane">QKAVNALVLALTVVIGL</span><span class="topo-outside">SLLWNDATASI</span><span class="topo-membrane">VLFFLLALLFGVLMT</span><span class="topo-inside">LPIGGGDMPVAISF</span><span class="topo-membrane">YNAFTGMAVGFEGFAVG</span><span class="topo-outside">N</span><span class="topo-membrane">PALMVAGTLVGAA</span></span>
<span class="topo-ruler">       250       260       270</span>
<span class="topo-line"><span class="topo-membrane">GT</span><span class="topo-inside">LLTVLMARAMNRSVWISV</span><span class="topo-unknown">LVGGHHHHHH</span></span>
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
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>19</td>
      <td>4</td>
      <td>19</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>20</td>
      <td>33</td>
      <td>20</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>48</td>
      <td>34</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>56</td>
      <td>49</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>72</td>
      <td>57</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>86</td>
      <td>73</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>101</td>
      <td>87</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>116</td>
      <td>102</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>134</td>
      <td>117</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>152</td>
      <td>135</td>
      <td>152</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>169</td>
      <td>153</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>180</td>
      <td>170</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>195</td>
      <td>181</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>209</td>
      <td>196</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>226</td>
      <td>210</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>227</td>
      <td>227</td>
      <td>227</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>242</td>
      <td>228</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>260</td>
      <td>243</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o9p">4O9P</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100</span>
<span class="topo-line"><span class="topo-outside">MEFGF</span><span class="topo-membrane">WSALYIFVLTAFLGYEL</span><span class="topo-inside">ITRVPVILHTPLMSG</span><span class="topo-membrane">SNFIHGVVVVGAM</span><span class="topo-outside">VVLGHAETGLEKLI</span><span class="topo-membrane">GFLGVILGAANAAGGYA</span><span class="topo-inside">VTVRMLEM</span><span class="topo-unknown">FERKPGQGGGR</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>1</td>
      <td>5</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>22</td>
      <td>6</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>37</td>
      <td>23</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>50</td>
      <td>38</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>64</td>
      <td>51</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>81</td>
      <td>65</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>89</td>
      <td>82</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>100</td>
      <td>90</td>
      <td>100</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o9p">4O9P</a> — Chain D (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MDL</span><span class="topo-membrane">IQAAYFVVAILFIVGLK</span><span class="topo-inside">RMAHPTTAKSGI</span><span class="topo-membrane">VWAGWGMVLAVLATF</span><span class="topo-outside">FWPGMGNFAL</span><span class="topo-membrane">ILLALLLGSVVAWWAA</span><span class="topo-inside">VRVAMTDMPQM</span><span class="topo-membrane">VAIYNGMGGGAAATIAA</span><span class="topo-outside">VELLKGAFENTGLMA</span><span class="topo-membrane">LAIL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGLIGSVAFTGSLIAFA</span><span class="topo-inside">KLQGIMKSRPILFPG</span><span class="topo-membrane">QKAVNALVLALTVVIGL</span><span class="topo-outside">SLLWNDATASIV</span><span class="topo-membrane">LFFLLALLFGVLMTL</span><span class="topo-inside">PIGGGDMPVAI</span><span class="topo-membrane">SFYNAFTGMAVGFEGFA</span><span class="topo-outside">VG</span><span class="topo-membrane">NPALMVAGTLVGAA</span></span>
<span class="topo-ruler">       250       260       270       280   </span>
<span class="topo-line"><span class="topo-membrane">GT</span><span class="topo-inside">LLTVLMARAMNRSVWSVL</span><span class="topo-unknown">VGGFGVEQEAGEVKGHHHHHHHH</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>20</td>
      <td>4</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>21</td>
      <td>32</td>
      <td>21</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>47</td>
      <td>33</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>57</td>
      <td>48</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>73</td>
      <td>58</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>84</td>
      <td>74</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>101</td>
      <td>85</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>116</td>
      <td>102</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>137</td>
      <td>117</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>152</td>
      <td>138</td>
      <td>152</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>169</td>
      <td>153</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>181</td>
      <td>170</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>196</td>
      <td>182</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>207</td>
      <td>197</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>224</td>
      <td>208</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>226</td>
      <td>225</td>
      <td>226</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>242</td>
      <td>227</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>260</td>
      <td>243</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>283</td>
      <td>261</td>
      <td>283</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o9p">4O9P</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100</span>
<span class="topo-line"><span class="topo-outside">MEFGF</span><span class="topo-membrane">WSALYIFVLTAFLGYEL</span><span class="topo-inside">ITRVPVILHTPLMSG</span><span class="topo-membrane">SNFIHGVVVVGAMV</span><span class="topo-outside">VLGHAETGLEKL</span><span class="topo-membrane">IGFLGVILGAANAAGGYA</span><span class="topo-inside">VTVRMLEMFERKP</span><span class="topo-unknown">GQGGGR</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>1</td>
      <td>5</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>22</td>
      <td>6</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>37</td>
      <td>23</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>51</td>
      <td>38</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>63</td>
      <td>52</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>81</td>
      <td>64</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>94</td>
      <td>82</td>
      <td>94</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>100</td>
      <td>95</td>
      <td>100</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o9p">4O9P</a> — Chain B (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MDL</span><span class="topo-membrane">IQAAYFVVAILFIVGLK</span><span class="topo-inside">RMAHPTTAKSGI</span><span class="topo-membrane">VWAGWGMVLAVLATF</span><span class="topo-outside">FWPGMGNFAL</span><span class="topo-membrane">ILLALLLGSVVAWWAA</span><span class="topo-inside">VRVAMTDMPQMV</span><span class="topo-membrane">AIYNGMGGGAAATIAA</span><span class="topo-outside">VELLKGAFENTGLMA</span><span class="topo-membrane">LAIL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGLIGSVAFTGSLIAFA</span><span class="topo-inside">KLQGIMKSRPILF</span><span class="topo-membrane">PGQKAVNALVLALTVVIGL</span><span class="topo-outside">SLLWNDATASIV</span><span class="topo-membrane">LFFLLALLFGVLMTL</span><span class="topo-inside">PIGGGDMPVAISF</span><span class="topo-membrane">YNAFTGMAVGFEGFA</span><span class="topo-outside">VGN</span><span class="topo-membrane">PALMVAGTLVGAA</span></span>
<span class="topo-ruler">       250       260       270       280   </span>
<span class="topo-line"><span class="topo-membrane">GT</span><span class="topo-inside">LLTVLMARAMNRSVWSVLVGGF</span><span class="topo-unknown">GVEQEAGEVKGHHHHHHHH</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>20</td>
      <td>4</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>21</td>
      <td>32</td>
      <td>21</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>47</td>
      <td>33</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>57</td>
      <td>48</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>73</td>
      <td>58</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>85</td>
      <td>74</td>
      <td>85</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>101</td>
      <td>86</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>116</td>
      <td>102</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>137</td>
      <td>117</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>150</td>
      <td>138</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>169</td>
      <td>151</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>181</td>
      <td>170</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>196</td>
      <td>182</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>209</td>
      <td>197</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>224</td>
      <td>210</td>
      <td>224</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>227</td>
      <td>225</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>242</td>
      <td>228</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>264</td>
      <td>243</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>283</td>
      <td>265</td>
      <td>283</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o9u">4O9U</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100</span>
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-membrane">EFGFWSALYIFVLTAFLGY</span><span class="topo-inside">ELITRVPVILHTPLMSGS</span><span class="topo-membrane">NFIHGVVVVGAMVVL</span><span class="topo-outside">GHAETGLEKL</span><span class="topo-membrane">IGFLGVILGAANAAGGY</span><span class="topo-inside">AVTVRMLEMFERKP</span><span class="topo-unknown">GQGGGR</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>20</td>
      <td>2</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>21</td>
      <td>38</td>
      <td>21</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>53</td>
      <td>39</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>63</td>
      <td>54</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>80</td>
      <td>64</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>94</td>
      <td>81</td>
      <td>94</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o9u">4O9U</a> — Chain B (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MDL</span><span class="topo-membrane">IQAAYFVVAILFIVG</span><span class="topo-inside">LKRMAHPTTAKSGIVW</span><span class="topo-membrane">AGWGMVLAVLATFF</span><span class="topo-outside">WPGMGNFA</span><span class="topo-membrane">LILLALLLGSVVAWWA</span><span class="topo-inside">AVRVAMTDMPQMVA</span><span class="topo-membrane">IYNGMGGGAAATIAA</span><span class="topo-outside">VELLKGAFENTGLMA</span><span class="topo-membrane">LAIL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGLIGSVAFTGSLI</span><span class="topo-inside">AFAKLQGIMKSRPILFPG</span><span class="topo-membrane">QKAVNALVLALTVVIGL</span><span class="topo-outside">SLLWNDATASI</span><span class="topo-membrane">VLFFLLALLFGVLMT</span><span class="topo-inside">LPIGGGDMPVAISF</span><span class="topo-membrane">YNAFTGMAVGFEGFAVG</span><span class="topo-outside">N</span><span class="topo-membrane">PALMVAGTLVGAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GT</span><span class="topo-inside">LLTVLMARAMNRSVWSVLVGG</span><span class="topo-unknown">FGVEQEAGEV</span><span class="topo-inside">KGSLKPIDVEDAAVMLAYAGKVVFVPGYGMALSQAQHKLKELADLLEARGVEVKFAIHPVAGRMPGHMNVLLAEAGVDYDKLKDLEE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450</span>
<span class="topo-line"><span class="topo-inside">INPEFPTVDVAVVIGANDVVNPAARRPGSPLYGMPILDVDKAKNVIVIKRGQGKGFAGVENELFYAENTRMLYGDAQKVLTELIQALKRL</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>18</td>
      <td>4</td>
      <td>18</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>19</td>
      <td>34</td>
      <td>19</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>48</td>
      <td>35</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>56</td>
      <td>49</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>72</td>
      <td>57</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>86</td>
      <td>73</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>101</td>
      <td>87</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>116</td>
      <td>102</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>134</td>
      <td>117</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>152</td>
      <td>135</td>
      <td>152</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>169</td>
      <td>153</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>180</td>
      <td>170</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>195</td>
      <td>181</td>
      <td>195</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>209</td>
      <td>196</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>226</td>
      <td>210</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>227</td>
      <td>227</td>
      <td>227</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>242</td>
      <td>228</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>263</td>
      <td>243</td>
      <td>263</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>450</td>
      <td>274</td>
      <td>450</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o9u">4O9U</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100</span>
<span class="topo-line"><span class="topo-outside">MEFGF</span><span class="topo-membrane">WSALYIFVLTAFLGY</span><span class="topo-inside">ELITRVPVILHTPLMSGS</span><span class="topo-membrane">NFIHGVVVVGAMV</span><span class="topo-outside">VLGHAETGLEKL</span><span class="topo-membrane">IGFLGVILGAANAAGGY</span><span class="topo-inside">AVTVRMLEMF</span><span class="topo-unknown">ERKPGQGGGR</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>1</td>
      <td>5</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>20</td>
      <td>6</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>21</td>
      <td>38</td>
      <td>21</td>
      <td>38</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>51</td>
      <td>39</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>63</td>
      <td>52</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>80</td>
      <td>64</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>90</td>
      <td>81</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o9u">4O9U</a> — Chain D (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MDL</span><span class="topo-membrane">IQAAYFVVAILFIVGL</span><span class="topo-inside">KRMAHPTTAKSGIVW</span><span class="topo-membrane">AGWGMVLAVLATF</span><span class="topo-outside">FWPGMGNFAL</span><span class="topo-membrane">ILLALLLGSVVAWWA</span><span class="topo-inside">AVRVAMTDMPQMVA</span><span class="topo-membrane">IYNGMGGGAAATIAA</span><span class="topo-outside">VELLKGAFENTGLMA</span><span class="topo-membrane">LAIL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGLIGSVAFTGSLI</span><span class="topo-inside">AFAKLQGIMKSRPILFP</span><span class="topo-membrane">GQKAVNALVLALTVVIGL</span><span class="topo-outside">SLLWNDATASIV</span><span class="topo-membrane">LFFLLALLFGVLMTL</span><span class="topo-inside">PIGGGDMPVAISF</span><span class="topo-membrane">YNAFTGMAVGFEGFAVG</span><span class="topo-outside">N</span><span class="topo-membrane">PALMVAGTLVGAA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">GT</span><span class="topo-inside">LLTVLMARAMNRSVWSVL</span><span class="topo-unknown">VGGFGVEQEAGEV</span><span class="topo-inside">KGSLKPIDVEDAAVMLAYAGKVVFVPGYGMALSQAQHKLKELADLLEARGVEVKFAIHPVAGRMPGHMNVLLAEAGVDYDKLKDLEE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450</span>
<span class="topo-line"><span class="topo-inside">INPEFPTVDVAVVIGANDVVNPAARRPGSPLYGMPILDVDKAKNVIVIKRGQGKGFAGVENELFYAENTRMLYGDAQKVLTELIQALKRL</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>19</td>
      <td>4</td>
      <td>19</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>20</td>
      <td>34</td>
      <td>20</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>47</td>
      <td>35</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>57</td>
      <td>48</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>72</td>
      <td>58</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>86</td>
      <td>73</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>101</td>
      <td>87</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>116</td>
      <td>102</td>
      <td>116</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>117</td>
      <td>134</td>
      <td>117</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>151</td>
      <td>135</td>
      <td>151</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>169</td>
      <td>152</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>170</td>
      <td>181</td>
      <td>170</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>196</td>
      <td>182</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>209</td>
      <td>197</td>
      <td>209</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>226</td>
      <td>210</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>227</td>
      <td>227</td>
      <td>227</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>242</td>
      <td>228</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>260</td>
      <td>243</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>450</td>
      <td>274</td>
      <td>450</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o9u">4O9U</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHHH</span><span class="topo-inside">MVTVAVPKERAPGERRVALVPEVVARLVKGGARVRVERGAGEGAYHPDEAYQEAGAEVVERGELLKGAHLLFTVQPPPEDLIQALEPGAIVVGFVQPHKNLELVRALQAKK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ATVIAMELIPRITRAQSMDALSSQATVAGYLAAIHAARLSPRFFPMLTTAAGTIRPAKVMVMGVGVAGLMAIATAKRLGAQVFAYDVRKAALEQALSLGAKPIELPISAEGEGGYARELT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">EEEKRIQHEALRDHVAGMDVLITTAQVPGRRAPILLTEDMVERLKPGTVVVDLAAESGGNCVLTKPGEVVEVRGVRVYGPLNLPSELSVHASEMYAKNLYNLSSLLIEKGAFAPKWEDEI</span></span>
<span class="topo-ruler">       370       380    </span>
<span class="topo-line"><span class="topo-inside">VRAALLMKEGEVLHGPTKALL</span><span class="topo-unknown">GGA</span></span>
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
      <td>10</td>
      <td>381</td>
      <td>1</td>
      <td>372</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o9u">4O9U</a> — Chain F (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MHHHHHHHH</span><span class="topo-inside">MVTVAVPKERAPGERRVALVPEVVARLVKGGARVRVERGAGEGAYHPDEAYQEAGAEVVERGELLKGAHLLFTVQPPPEDLIQALEPGAIVVGFVQPHKNLELVRALQAKK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ATVIAMELIPRITRAQSMDALSSQATVAGYLAAIHAARLSPRFFPMLTTAAGTIRPAKVMVMGVGVAGLMAIATAKRLGAQVFAYDVRKAALEQALSLGAKPIELPISAEG</span><span class="topo-unknown">EGGY</span><span class="topo-inside">ARELT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">EEEKRIQHEALRDHVAGMDVLITTAQVPGRRAPILLTEDMVERLKPGTVVVDLAAESGGNCVLTKPGEVVEVRGVRVYGPLNLPSELSVHASEMYAKNLYNLSSLLIEKGAFAPKWEDEI</span></span>
<span class="topo-ruler">       370       380    </span>
<span class="topo-line"><span class="topo-inside">VRAALLMKEGEVLHGPTKALLG</span><span class="topo-unknown">GA</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>10</td>
      <td>231</td>
      <td>1</td>
      <td>222</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>382</td>
      <td>227</td>
      <td>373</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o9t">4O9T</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100</span>
<span class="topo-line"><span class="topo-outside">MEFGFW</span><span class="topo-membrane">SALYIFVLTAFLGYEL</span><span class="topo-inside">ITRVPVILHTPLMSG</span><span class="topo-membrane">SNFIHGVVVVGAM</span><span class="topo-outside">VVLGHAETGLEKLIGF</span><span class="topo-membrane">LGVILGAANAAGGYA</span><span class="topo-inside">VTVRMLEMFERKP</span><span class="topo-unknown">GQGGGR</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>22</td>
      <td>7</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>37</td>
      <td>23</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>50</td>
      <td>38</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>66</td>
      <td>51</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>81</td>
      <td>67</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>94</td>
      <td>82</td>
      <td>94</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>100</td>
      <td>95</td>
      <td>100</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o9t">4O9T</a> — Chain B (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MDLIQ</span><span class="topo-membrane">AAYFVVAILFIVGLK</span><span class="topo-inside">RMAHPTTAKSGI</span><span class="topo-membrane">VWAGWGMVLAVLAT</span><span class="topo-outside">FFWPGMGNFALI</span><span class="topo-membrane">LLALLLGSVVAWWAA</span><span class="topo-inside">VRVAMTDMPQM</span><span class="topo-membrane">VAIYNGMGGGAAATIA</span><span class="topo-outside">AVELLKGAFENTGLMAL</span><span class="topo-membrane">AIL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGLIGSVAFTGSLIAFA</span><span class="topo-inside">KLQGIMKSRPILF</span><span class="topo-membrane">PGQKAVNALVLALTVV</span><span class="topo-outside">IGLSLLWNDATASIVLF</span><span class="topo-membrane">FLLALLFGVLMTL</span><span class="topo-inside">PIGGGDMPVAI</span><span class="topo-membrane">SFYNAFTGMAVGFEGF</span><span class="topo-outside">AVGN</span><span class="topo-membrane">PALMVAGTLVGAA</span></span>
<span class="topo-ruler">       250       260       270       280   </span>
<span class="topo-line"><span class="topo-membrane">GT</span><span class="topo-inside">LLTVLMARAMNRSVWSVLVG</span><span class="topo-unknown">GFGVEQEAGEVKGHHHHHHHH</span></span>
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
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>20</td>
      <td>6</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>21</td>
      <td>32</td>
      <td>21</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>46</td>
      <td>33</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>58</td>
      <td>47</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>73</td>
      <td>59</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>84</td>
      <td>74</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>100</td>
      <td>85</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>117</td>
      <td>101</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>137</td>
      <td>118</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>150</td>
      <td>138</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>166</td>
      <td>151</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>183</td>
      <td>167</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>196</td>
      <td>184</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>207</td>
      <td>197</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>223</td>
      <td>208</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>227</td>
      <td>224</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>242</td>
      <td>228</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>262</td>
      <td>243</td>
      <td>262</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>263</td>
      <td>283</td>
      <td>263</td>
      <td>283</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o9t">4O9T</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100</span>
<span class="topo-line"><span class="topo-outside">MEFGFW</span><span class="topo-membrane">SALYIFVLTAFLGYEL</span><span class="topo-inside">ITRVPVILHTPLMS</span><span class="topo-membrane">GSNFIHGVVVVGAM</span><span class="topo-outside">VVLGHAETGLEKLIGF</span><span class="topo-membrane">LGVILGAANAAGGYA</span><span class="topo-inside">VTVRMLEM</span><span class="topo-unknown">FERKPGQGGGR</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>22</td>
      <td>7</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>36</td>
      <td>23</td>
      <td>36</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>50</td>
      <td>37</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>66</td>
      <td>51</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>81</td>
      <td>67</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>89</td>
      <td>82</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>100</td>
      <td>90</td>
      <td>100</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4o9t">4O9T</a> — Chain D (9 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MDLIQ</span><span class="topo-membrane">AAYFVVAILFIVGLK</span><span class="topo-inside">RMAHPTTAKSGI</span><span class="topo-membrane">VWAGWGMVLAVLAT</span><span class="topo-outside">FFWPGMGNFALI</span><span class="topo-membrane">LLALLLGSVVAWWAA</span><span class="topo-inside">VRVAMTDMPQM</span><span class="topo-membrane">VAIYNGMGGGAAATIA</span><span class="topo-outside">AVELLKGAFENTGLMAL</span><span class="topo-membrane">AIL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GGLIGSVAFTGSLIAFA</span><span class="topo-inside">KLQGIMKSRPILF</span><span class="topo-membrane">PGQKAVNALVLALTVV</span><span class="topo-outside">IGLSLLWNDATASIVL</span><span class="topo-membrane">FFLLALLFGVLMTL</span><span class="topo-inside">PIGGGDMPVAI</span><span class="topo-membrane">SFYNAFTGMAVGFEGF</span><span class="topo-outside">AVGN</span><span class="topo-membrane">PALMVAGTLVGAA</span></span>
<span class="topo-ruler">       250       260       270       280   </span>
<span class="topo-line"><span class="topo-membrane">GT</span><span class="topo-inside">LLTVLMARAMNRSVWSVL</span><span class="topo-unknown">VGGFGVEQEAGEVKGHHHHHHHH</span></span>
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
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>20</td>
      <td>6</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>21</td>
      <td>32</td>
      <td>21</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>46</td>
      <td>33</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>58</td>
      <td>47</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>73</td>
      <td>59</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>84</td>
      <td>74</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>100</td>
      <td>85</td>
      <td>100</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>117</td>
      <td>101</td>
      <td>117</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>137</td>
      <td>118</td>
      <td>137</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>138</td>
      <td>150</td>
      <td>138</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>151</td>
      <td>166</td>
      <td>151</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>182</td>
      <td>167</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>196</td>
      <td>183</td>
      <td>196</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>197</td>
      <td>207</td>
      <td>197</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>208</td>
      <td>223</td>
      <td>208</td>
      <td>223</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>224</td>
      <td>227</td>
      <td>224</td>
      <td>227</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>228</td>
      <td>242</td>
      <td>228</td>
      <td>242</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>243</td>
      <td>260</td>
      <td>243</td>
      <td>260</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>283</td>
      <td>261</td>
      <td>283</td>
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

### Holo-TH asymmetric dimer with alternating dIII conformations

The 2015 Science paper (Leung et al.) revealed the 2.8 A structure of the transmembrane proton channel domain and the 6.9 A structure of the entire holo-TH enzyme. The holo-TH is a highly asymmetric dimer with the NADP(H)-binding domain (dIII) in two different orientations, suggesting a catalytic mechanism in which the two copies of dIII alternately function in proton translocation and hydride transfer — a division of labor approximately 40 A apart within the complex.

### Internal water molecules in the proton channel

The 2.2-Å structure reveals nine internal water molecules (W1-W9) within cytoplasmic and periplasmic invaginations on either side of His42α2. W2 and W3 are hydrogen bonded to asparagines that are themselves hydrogen bonded to His42α2, forming part of a hydrogen-bond network surrounding this critical residue. W1 is within the cytoplasmic chamber. In MD simulations, W2 can be observed exchanging with bulk water on the cytoplasmic side of the membrane. W4, W5, and W6 are clustered at the periplasmic entrance and hydrogen bonded to Asn227β and Glu103β. W8 and W9 are hydrogen bonded to W4 through main-chain interactions involving Pro228β and Ala229β.

### His42α2 as central protonation gate

His42α2 (chain A, TM3) is a functionally critical residue located in the middle of the membrane. It is postulated to be transiently protonated during proton translocation across the membrane. In MD simulations with His42α2 protonated, a transient water wire forms between Glu221β and His42α2 in the periplasmic region (z = -2 to 5 Å), and a second water wire persists between His42α2 and Ser208β in the cytoplasmic chamber (z = 5 to 15 Å). With His42α2 deprotonated, no water penetrates the dry region between His42α2 and the periplasmic chamber during 300-ns MD runs.

### Thr214β conformational gating

Thr214β (chain B) displays conformational changes that gate channel access. When the transient water wire forms in the dry region, the Thr214β side-chain χ1 dihedral angle transitions from -60° to +60°, rotating its Oγ atom out of the proton pathway. Mutation of Thr214β to Ala deactivated the enzyme to 3-5% of wild-type activity at pH 6.5, 7.0, and 8.0, confirming its critical role in proton translocation.

### pH-dependent conformational changes

Comparison of the dimeric dII structures solved at pH 6.5 (2.2 Å) versus pH 8.5 (2.8 Å) reveals conformational changes in helix positions. The TM helices in each protomer are slightly tilted about a vertical axis near the middle of the TM bundles. These pH-dependent changes may be related to proton translocation or enzymatic activities affected by pH.

### Hydrophobic dry region in the proton channel

The pore profile shows a narrow region (<2 Å radius) that includes both a dry region on the periplasmic side of His42α2 and the region from His42α2 on the cytoplasmic side. The dry region is composed of hydrophobic aliphatic amino acids and acts as a gated barrier between the periplasmic and cytoplasmic chambers. MD simulations show that water wire formation across this dry region is coordinated with Thr214β conformational changes.


## Cross-References

- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — LCP crystallization method used to solve the 5UNI structure
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Similar monoglyceride lipid used in LCP crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used in purification and crystallization buffers
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/">Molecular Dynamics Simulation</a> — MD simulations used to elucidate proton translocation mechanism
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Used for final purification step with Superose 6 column
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/1,4-butanediol/">1,4-Butanediol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/ammonium-formate/">Ammonium Formate</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer component in purification or crystallization
