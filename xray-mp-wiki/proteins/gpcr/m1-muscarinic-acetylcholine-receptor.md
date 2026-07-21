---
title: "M1 Muscarinic Acetylcholine Receptor"
created: 2026-05-27
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aax2517, doi/10.1038##nature17188, doi/10.1016##j.cell.2021.11.001]
verified: agent
uniprot_id: ['P11229', 'Q8QGR0']
---

# M1 Muscarinic Acetylcholine Receptor

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P11229">UniProt: P11229</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8QGR0">UniProt: Q8QGR0</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The M1 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) receptor (M1 mAChR) is a class A G protein-coupled receptor that mediates cholinergic neurotransmission in the central nervous system. It is highly expressed in the hippocampus and cortex, areas critical for learning and memory. The M1 receptor couples to Gq/11 proteins to activate phospholipase C-beta, leading to intracellular calcium release. It is a major therapeutic target for Alzheimer disease, as cholinergic deficits in the hippocampus and cortex are a hallmark of the disease. The M1 receptor has been crystallized in complex with multiple orthosteric agonists, revealing the molecular basis for agonist-induced activation and subtype selectivity.


## Publications

### doi/10.1126##science.aax2517

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6wjc">6WJC</a></td>
      <td>2.80</td>
      <td>Not specified</td>
      <td>Recombinantly expressed M1AChR from Sf9 insect cells; MT7 expressed in H15 insect cells; co-crystallized with atropine (orthosteric antagonist)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/atropine/">Atropine</a>, <a href="/xray-mp-wiki/reagents/ligands/mt7/">MT7</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf21 insect cells (baculovirus expression vector system)
- **Construct**: [M1-StaR-T4L](/xray-mp-wiki/proteins/gpcr/m1-star-t4l/) construct with N-terminal GP64 signal sequence, chimeric M4 N-terminus (residues 1-95 of M4 replacing residues 1-87 of M1), residues 88-438 of M1 receptor, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (residues 439-460 removed), [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) inserted into ICL3 between residues 219 and 354, and C-terminal deca-histidine tag. The StaR variant contains 12 thermostabilizing mutations: F27A, T32A, V46L, L64A, T95A, W101A, S112A, A143L, A196T, K362A, A364L, S411A.


<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6wjc">6WJC</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDDAAAQTSAPPAVSPQITVL</span><span class="topo-inside">APGKGPW</span><span class="topo-membrane">QVAFIGITTGLLSLATVTGNLLVLI</span><span class="topo-outside">SFKVNTELKTVNNY</span><span class="topo-membrane">FLLSLACADLIIGTFSMNLYTTYLL</span><span class="topo-inside">MGHWAL</span><span class="topo-membrane">GTLACDLWLALDYVASQA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">RVMNLLLISF</span><span class="topo-outside">DRYFSVTRPLSYRAKRTPRRAA</span><span class="topo-membrane">LMIGLAWLVSFVLWAPAILFWQYLV</span><span class="topo-inside">GERTVLAGQC</span><span class="topo-membrane">YIQFLSQPIITFGTAMAAFYLPVTVMCTLYWR</span><span class="topo-outside">IYRETENRNIFEMLRIDEGLR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">LKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KSRWYNQTPNRAKRVITTFRTGTWDAYFSLVKEKKAAR</span><span class="topo-membrane">TLSAILLAFILTWTPYNIMVLVSTF</span><span class="topo-inside">CKDCVPET</span><span class="topo-membrane">LWELGYWLCYVNSTINPMCYALC</span><span class="topo-outside">N</span><span class="topo-unknown">KAFRDTFRLLL</span><span class="topo-outside">LCRW</span><span class="topo-unknown">DKRRWRKIPK</span></span>
<span class="topo-ruler">       490         </span>
<span class="topo-line"><span class="topo-unknown">RPGSVHRTPSRQCHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>26</td>
      <td>32</td>
      <td>17</td>
      <td>23</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>57</td>
      <td>24</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>71</td>
      <td>49</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>96</td>
      <td>63</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>102</td>
      <td>88</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>130</td>
      <td>94</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>131</td>
      <td>152</td>
      <td>122</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>177</td>
      <td>144</td>
      <td>168</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>178</td>
      <td>187</td>
      <td>169</td>
      <td>178</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>219</td>
      <td>179</td>
      <td>210</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>220</td>
      <td>398</td>
      <td>211</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>399</td>
      <td>423</td>
      <td>366</td>
      <td>390</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>424</td>
      <td>431</td>
      <td>391</td>
      <td>398</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>432</td>
      <td>454</td>
      <td>399</td>
      <td>421</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>455</td>
      <td>455</td>
      <td>422</td>
      <td>422</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>456</td>
      <td>466</td>
      <td>423</td>
      <td>433</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>467</td>
      <td>470</td>
      <td>434</td>
      <td>437</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6wjc">6WJC</a> — Chain C (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60         </span>
<span class="topo-line"><span class="topo-inside">GPGSLTCVKSNSIWFPTSEDCPDGQNLCFKRWQYISPRMYDFTRGCAATCPKAEYRDVINCCGTDKCNK</span></span>
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
      <td>1</td>
      <td>69</td>
      <td>-3</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nature17188

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5cxv">5CXV</a></td>
      <td>2.7</td>
      <td>P 21 21 21</td>
      <td>Human M1 muscarinic receptor, N-terminal FLAG epitope tag, N-glycosylation mutants (N2Q, N12Q, unintentionally N110Q 3.37), residues 226-389 of ICL3 replaced by T4 lysozyme fusion protein, C-terminal 8x histidine tag
</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/tiotropium/">Tiotropium</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf21 insect cells (baculovirus expression vector system)
- **Construct**: [M1-StaR-T4L](/xray-mp-wiki/proteins/gpcr/m1-star-t4l/) construct with N-terminal GP64 signal sequence, chimeric M4 N-terminus (residues 1-95 of M4 replacing residues 1-87 of M1), residues 88-438 of M1 receptor, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (residues 439-460 removed), [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) inserted into ICL3 between residues 219 and 354, and C-terminal deca-histidine tag. The StaR variant contains 12 thermostabilizing mutations: F27A, T32A, V46L, L64A, T95A, W101A, S112A, A143L, A196T, K362A, A364L, S411A.


<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5cxv">5CXV</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDAAAQTSAPPAVSPQITVLAPG</span><span class="topo-inside">KGPW</span><span class="topo-membrane">QVAFIGITTGLLSLATVTGNLLVLI</span><span class="topo-outside">SFKVNTELKTVNNYF</span><span class="topo-membrane">LLSLACADLIIGTFSMNLYTTYLL</span><span class="topo-inside">MGHWALGT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">L</span><span class="topo-membrane">ACDLWLALDYVASQASVMNLLLIS</span><span class="topo-outside">FDRYFSVTRPLSYRAKRTPRRAAL</span><span class="topo-membrane">MIGLAWLVSFVLWAPAILFWQYL</span><span class="topo-inside">VGERTVLAGQC</span><span class="topo-membrane">YIQFLSQPIITFGTAMAAFYLPVTVMCTL</span><span class="topo-outside">YWRIYRET</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ENRNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">RMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYFSLVKEKKAARTL</span><span class="topo-membrane">SAILLAFILTWTPYNIMVLVSTFC</span><span class="topo-inside">KDC</span><span class="topo-membrane">VPETLWELGYWLCYVNSTINPMC</span><span class="topo-outside">YALCNKAFRDTFRL</span></span>
<span class="topo-ruler">       490       500       510     </span>
<span class="topo-line"><span class="topo-outside">LLLCRWDK</span><span class="topo-unknown">RRWRKIPKRPGSVHRTPSRQCHHHHHH</span></span>
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
      <td>44</td>
      <td>-24</td>
      <td>19</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>45</td>
      <td>48</td>
      <td>20</td>
      <td>23</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>73</td>
      <td>24</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>88</td>
      <td>49</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>112</td>
      <td>64</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>121</td>
      <td>88</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>145</td>
      <td>97</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>169</td>
      <td>121</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>192</td>
      <td>145</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>193</td>
      <td>203</td>
      <td>168</td>
      <td>178</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>204</td>
      <td>232</td>
      <td>179</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>243</td>
      <td>208</td>
      <td>218</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>244</td>
      <td>403</td>
      <td>1001</td>
      <td>1160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>404</td>
      <td>416</td>
      <td>355</td>
      <td>367</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>417</td>
      <td>440</td>
      <td>368</td>
      <td>391</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>441</td>
      <td>443</td>
      <td>392</td>
      <td>394</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>466</td>
      <td>395</td>
      <td>417</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>467</td>
      <td>488</td>
      <td>418</td>
      <td>439</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>489</td>
      <td>515</td>
      <td>440</td>
      <td>466</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1016##j.cell.2021.11.001

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zfz">6ZFZ</a></td>
      <td>2.17</td>
      <td>C 2 2 21</td>
      <td><a href="/xray-mp-wiki/proteins/gpcr/m1-star-t4l/">M1-StaR-T4L</a> (12 thermostabilizing mutations, M4 N-terminus chimera, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>, <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> in ICL3)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/77-lh-28-1/">77-LH-28-1</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zg4">6ZG4</a></td>
      <td>2.17</td>
      <td>C 2 2 21</td>
      <td><a href="/xray-mp-wiki/proteins/gpcr/m1-star-t4l/">M1-StaR-T4L</a> (12 thermostabilizing mutations, M4 N-terminus chimera, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>, <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> in ICL3)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/htl9936/">HTL9936</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6zg9">6ZG9</a></td>
      <td>2.17</td>
      <td>C 2 2 21</td>
      <td><a href="/xray-mp-wiki/proteins/gpcr/m1-star-t4l/">M1-StaR-T4L</a> (12 thermostabilizing mutations, M4 N-terminus chimera, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>, <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> in ICL3)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/gsk1034702/">GSK1034702</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf21 insect cells (baculovirus expression vector system)
- **Construct**: [M1-StaR-T4L](/xray-mp-wiki/proteins/gpcr/m1-star-t4l/) construct with N-terminal GP64 signal sequence, chimeric M4 N-terminus (residues 1-95 of M4 replacing residues 1-87 of M1), residues 88-438 of M1 receptor, C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (residues 439-460 removed), [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) inserted into ICL3 between residues 219 and 354, and C-terminal deca-histidine tag. The StaR variant contains 12 thermostabilizing mutations: F27A, T32A, V46L, L64A, T95A, W101A, S112A, A143L, A196T, K362A, A364L, S411A.


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
      <td>Cell culture and infection</td>
      <td>Sf21 cells infected with baculovirus at multiplicity of infection 2, harvested 48 hours post-infection</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Cells grown at 27 degrees Celsius with constant shaking in ESF 921 medium supplemented with 10% FBS and 1% penicillin/streptomycin</td>
    </tr>
    <tr>
      <td>Cell disruption and membrane preparation</td>
      <td>Cell disruption at 15000 psi using microfluidizer, membranes pelleted by ultracentrifugation at 200000 g for 50 min, high salt washes</td>
      <td>--</td>
      <td>PBS, 5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, protease inhibitor cocktail; wash buffer: PBS, 1 M NaCl, protease inhibitor cocktail + --</td>
      <td>Membranes resuspended in 40 mM Tris pH 7.6, 500 mM NaCl with protease inhibitors and stored at -80 degrees Celsius</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membranes incubated with ligand (40 uM <a href="/xray-mp-wiki/reagents/ligands/htl9936/">HTL9936</a> or <a href="/xray-mp-wiki/reagents/ligands/gsk1034702/">GSK1034702</a> or <a href="/xray-mp-wiki/reagents/ligands/77-lh-28-1/">77-LH-28-1</a>) for 40 min at room temperature, then solubilized with 1.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> for 1 hour at 4 degrees Celsius</td>
      <td>--</td>
      <td>40 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.6, 500 mM NaCl, protease inhibitor cocktail + 1.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Solubilized material clarified by centrifugation at 145000 g for 60 min</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Batch binding to <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)](/xray-mp-wiki/reagents/additives/nickel-nta/) Superflow resin for 3 hours, gradient wash (10 to 60 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>), elution with 245 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/)](/xray-mp-wiki/reagents/additives/nickel-nta/) Superflow resin</td>
      <td>40 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.6, 150 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (binding); 40 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.6, 500 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 70 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (wash); 40 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.6, 500 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 245 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (elution) + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Ligand (20 uM) included in all binding and wash buffers</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) on <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> column pre-equilibrated with buffer containing ligand</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>40 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.6, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 40 uM ligand + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Protein concentrated to approximately 60 mg/mL using 100 kDa cut-off membrane prior to crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified <a href="/xray-mp-wiki/proteins/gpcr/m1-star-t4l/">M1-StaR-T4L</a> at approximately 60 mg/mL in 40 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.6, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 40 uM ligand</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 degrees Celsius</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals were flash-cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Three structures were solved: <a href="/xray-mp-wiki/proteins/gpcr/m1-star-t4l/">M1-StaR-T4L</a> with <a href="/xray-mp-wiki/reagents/ligands/77-lh-28-1/">77-LH-28-1</a> (PDB 6ZFZ), <a href="/xray-mp-wiki/reagents/ligands/htl9936/">HTL9936</a> (PDB 6ZG4), and <a href="/xray-mp-wiki/reagents/ligands/gsk1034702/">GSK1034702</a> (PDB 6ZG9). All structures were solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using the turkey beta1-adrenergic receptor (PDB 2Y00) as the search model. Iterative rounds of model refinement with BUSTER were interspersed with manual model building in COOT. Two TLS groups corresponding to the receptor and <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> were defined.
</td>
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
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zfz">6ZFZ</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">METV</span><span class="topo-membrane">EMVAIATVAGLLSLATVTGNILLML</span><span class="topo-outside">SIKVNRQLQTVNNY</span><span class="topo-membrane">FAFSLACADLIIGAFSMNLYTVYII</span><span class="topo-inside">MGHWALGAL</span><span class="topo-membrane">ACDLALALDYVASNAAVMNLLLISF</span><span class="topo-outside">DRYFSVTRPLSYRAKRTP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">RRAL</span><span class="topo-membrane">LMIGLAWLVSFVLWAPAILFW</span><span class="topo-inside">QYLVGERTVLAGQC</span><span class="topo-membrane">YIQFLSQPIITFGTAMATFYLPVTVMCTLYW</span><span class="topo-outside">RIYRETENRANIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">AKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-outside">TFSLVKEKAALRT</span><span class="topo-membrane">LSAILLAFILTWTPYNIMVLVSTF</span><span class="topo-inside">CKDCVPE</span><span class="topo-membrane">TLWELGYWLCYVNATINPMCYAL</span><span class="topo-outside">CNKAFRDTFRLLLLARWDH</span><span class="topo-unknown">HHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>20</td>
      <td>23</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>29</td>
      <td>24</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>43</td>
      <td>49</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>68</td>
      <td>63</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>77</td>
      <td>88</td>
      <td>96</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>102</td>
      <td>97</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>124</td>
      <td>122</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>145</td>
      <td>144</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>159</td>
      <td>165</td>
      <td>178</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>190</td>
      <td>179</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>200</td>
      <td>210</td>
      <td>219</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>201</td>
      <td>360</td>
      <td>1002</td>
      <td>1161</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>373</td>
      <td>354</td>
      <td>366</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>397</td>
      <td>367</td>
      <td>390</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>404</td>
      <td>391</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>405</td>
      <td>427</td>
      <td>398</td>
      <td>420</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>428</td>
      <td>446</td>
      <td>421</td>
      <td>439</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>447</td>
      <td>455</td>
      <td>440</td>
      <td>448</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zg4">6ZG4</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">METVEMV</span><span class="topo-membrane">AIATVAGLLSLATVTGNILLMLSIKV</span><span class="topo-inside">NRQLQTVNN</span><span class="topo-membrane">YFAFSLACADLIIGAFSMNLYTVYI</span><span class="topo-outside">IMGHWALGAL</span><span class="topo-membrane">ACDLALALDYVASNAAVMNLLLISF</span><span class="topo-inside">DRYFSVTRPLSYRAKRTP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RRA</span><span class="topo-membrane">LLMIGLAWLVSFVLWAPAILFWQYL</span><span class="topo-outside">VGERTVLAGQCYIQFL</span><span class="topo-membrane">SQPIITFGTAMATFYLPVTVMCTLY</span><span class="topo-inside">WRIYRETENRANIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">AKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-inside">TFSLVKEKAALRT</span><span class="topo-membrane">LSAILLAFILTWTPYNIMVLVSTFC</span><span class="topo-outside">KDCVPET</span><span class="topo-membrane">LWELGYWLCYVNATINPMCYALC</span><span class="topo-inside">NKAF</span><span class="topo-unknown">RDTFRLLLLARWDHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>20</td>
      <td>26</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>33</td>
      <td>27</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>34</td>
      <td>42</td>
      <td>53</td>
      <td>61</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>67</td>
      <td>62</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>77</td>
      <td>87</td>
      <td>96</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>102</td>
      <td>97</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>123</td>
      <td>122</td>
      <td>142</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>148</td>
      <td>143</td>
      <td>167</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>164</td>
      <td>168</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>189</td>
      <td>184</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>373</td>
      <td>209</td>
      <td>366</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>374</td>
      <td>398</td>
      <td>367</td>
      <td>391</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>399</td>
      <td>405</td>
      <td>392</td>
      <td>398</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>428</td>
      <td>399</td>
      <td>421</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>429</td>
      <td>432</td>
      <td>422</td>
      <td>425</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>433</td>
      <td>446</td>
      <td>426</td>
      <td>439</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6zg9">6ZG9</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">METV</span><span class="topo-membrane">EMVAIATVAGLLSLATVTGNILLM</span><span class="topo-inside">LSIKVNRQLQTVNNYF</span><span class="topo-membrane">AFSLACADLIIGAFSMNLYTVYII</span><span class="topo-outside">MGHWAL</span><span class="topo-membrane">GALACDLALALDYVASNAAVMNLLLIS</span><span class="topo-inside">FDRYFSVTRPLSYRAKRTP</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RRALLM</span><span class="topo-membrane">IGLAWLVSFVLWAPAILFW</span><span class="topo-outside">QYLVGERTVLAGQC</span><span class="topo-membrane">YIQFLSQPIITFGTAMATFYLPVTVMCTLY</span><span class="topo-inside">WRIYRETENRANIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">AKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450     </span>
<span class="topo-line"><span class="topo-inside">TFSLVKEKAALRTL</span><span class="topo-membrane">SAILLAFILTWTPYNIMVLVSTF</span><span class="topo-outside">CKDCVPET</span><span class="topo-membrane">LWELGYWLCYVNATINPMC</span><span class="topo-inside">YALCN</span><span class="topo-unknown">KAFRDTFRLLLLARW</span><span class="topo-inside">DH</span><span class="topo-unknown">HHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>20</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>28</td>
      <td>24</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>44</td>
      <td>48</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>68</td>
      <td>64</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>74</td>
      <td>88</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>75</td>
      <td>101</td>
      <td>94</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>126</td>
      <td>121</td>
      <td>145</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>127</td>
      <td>145</td>
      <td>146</td>
      <td>164</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>159</td>
      <td>165</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>189</td>
      <td>179</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>374</td>
      <td>209</td>
      <td>367</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>375</td>
      <td>397</td>
      <td>368</td>
      <td>390</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>398</td>
      <td>405</td>
      <td>391</td>
      <td>398</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>424</td>
      <td>399</td>
      <td>417</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>425</td>
      <td>429</td>
      <td>418</td>
      <td>422</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>430</td>
      <td>444</td>
      <td>423</td>
      <td>437</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>445</td>
      <td>446</td>
      <td>438</td>
      <td>439</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### MT7 allosteric modulation mechanism and extreme subtype selectivity

The crystal structure of the M1AChR-[MT7](/xray-mp-wiki/reagents/ligands/mt7/) complex (PDB 6WJC) revealed the molecular basis for MT7's extreme subtype specificity (>5 orders of magnitude selectivity for M1 over other muscarinic subtypes). MT7 binds to the extracellular vestibule of M1AChR via its three-finger fold, with finger loop 2 acting as the primary insertion element. Unlike small-molecule allosteric modulators, MT7 engages multiple extracellular loops and TM helices simultaneously. The binding stabilizes a 3-4 A outward movement of TM6, ECL3, and TM7, which propagates to the intracellular face and traps the receptor in an inactive conformation. P33 from MT7 finger loop 2 interacts with W400^7.35 and E401^7.36, displacing W400 outward, which in turn stabilizes the outward displacement of TM6 through interactions with M384^6.54. The MT7-bound M1AChR also shows reorganization of the DRY motif at the intracellular face. The structure revealed key subtype-specific residues at the M1AChR-MT7 interface (ECL2, TM7, and TM2 regions) that explain why MT7 does not bind other muscarinic receptors. These findings established the structural basis for re-engineering MT7 to target [M2 Muscarinic Acetylcholine Receptor](/xray-mp-wiki/proteins/gpcr/m2-muscarinic-acetylcholine-receptor/), yielding the engineered toxin [Tx24](/xray-mp-wiki/reagents/ligands/tx24/).

### Agonist binding mode and activation mechanism

All three agonist-bound structures reveal that the orthosteric agonists are
primarily held in place via a charge-charge interaction between the protonated
nitrogen of the ligand and the conserved aspartate D105 (3.32) in the amine
pocket. Agonist binding causes rearrangement of the tyrosine cage (Y82, Y85,
Y104, Y378, Y381, Y404, Y408) that is characteristic of the inactive state.
The piperidine ring of [HTL9936](/xray-mp-wiki/reagents/ligands/htl9936/) makes contact with Y404 (7.39), causing a
rotation that confers a unique conformation of Y381 (6.51). The base of the
amine pocket is formed by C407 (7.42) making hydrophobic contacts to the
homopiperidine ring, and W378 (6.48) forming an edge-to-face pi-stacking
arrangement with the carbamate moiety.

### Structural basis for M1 subtype selectivity

Comparative analysis of the three agonist-bound structures revealed that
[HTL9936](/xray-mp-wiki/reagents/ligands/htl9936/) achieves M1 selectivity over M2 and M3 receptors through specific
interactions in the orthosteric pocket. The extended structure of [HTL9936](/xray-mp-wiki/reagents/ligands/htl9936/)
fills a sub-pocket defined between Tyr106 (3.33), Trp378 (6.48), Tyr381
(6.51), and Cys407 (7.42) more efficiently than the smaller agonist
[77-LH-28-1](/xray-mp-wiki/reagents/ligands/77-lh-28-1/). The tyrosine cage rearrangement induced by [HTL9936](/xray-mp-wiki/reagents/ligands/htl9936/) differs
from that seen in the M2 receptor [Iperoxo](/xray-mp-wiki/reagents/ligands/iperoxo/) agonist structure, providing a
structural basis for the reduced M2 and M3 activity of [HTL9936](/xray-mp-wiki/reagents/ligands/htl9936/) compared
to orthosteric agonists like xanomeline and [GSK1034702](/xray-mp-wiki/reagents/ligands/gsk1034702/).

### Partial agonism mechanism

Molecular dynamics simulations revealed that [HTL9936](/xray-mp-wiki/reagents/ligands/htl9936/) forms stable
water-mediated polar interaction networks in the major pocket with Y106
(3.33), T196 (5.46), Y381 (6.51), and N382 (6.52) via its carbamate
moiety, and in the minor pocket and extracellular vestibule with C178
(4.5.50) and Y404 (7.39) via its amide group. Analysis of binding site
volumes from MD simulations showed that [HTL9936](/xray-mp-wiki/reagents/ligands/htl9936/) has a more restricted
binding site volume compared to full agonists [77-LH-28-1](/xray-mp-wiki/reagents/ligands/77-lh-28-1/) and
[GSK1034702](/xray-mp-wiki/reagents/ligands/gsk1034702/), aligning more closely with the antagonist [Tiotropium](/xray-mp-wiki/reagents/ligands/tiotropium/). This
restricted binding site volume likely underlies the partial agonism of
[HTL9936](/xray-mp-wiki/reagents/ligands/htl9936/).

### StaR thermostabilization strategy

The M1-StaR construct incorporates 12 thermostabilizing mutations
distributed throughout the transmembrane domains, which collectively
enhance receptor stability without disrupting ligand binding. The W101A
(3.28) mutation was specifically designed to enable direct access of
small molecule agonists to the orthosteric binding site. The chimeric
M4 N-terminus (residues 1-95) replaced the native M1 N-terminus
(residues 1-87) to reduce toxicity associated with high expression
levels. The C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (removal of residues 439-460) and
[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) insertion in ICL3 (between residues 219 and 354) were
added to promote crystallization.

### Comparison with M2 receptor agonist structure

The M1 agonist-bound structures were compared with the M2 receptor
[Iperoxo](/xray-mp-wiki/reagents/ligands/iperoxo/) agonist structure (Fish et al., 2017). The M1 structures
revealed that agonist binding induces a different rearrangement of the
tyrosine cage compared to the M2 receptor. Specifically, the M1
receptor shows inward movement of Y104 (3.33), Y403 (6.51), and Y426
(7.39) upon agonist binding, which differs from the M2 receptor
conformation. This structural divergence provides insights into the
molecular basis for subtype-selective agonist design.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/mt7/">MT7</a> — Co-crystallized allosteric toxin modulator, PDB 6WJC
- <a href="/xray-mp-wiki/reagents/ligands/tx24/">Tx24</a> — Engineered M2-selective variant derived from MT7 using M1 structure as template
- <a href="/xray-mp-wiki/concepts/signaling-receptors/three-finger-toxin-gpcr-modulation/">Three-Finger Toxin Scaffold for GPCR Modulation</a> — M1AChR-MT7 structure is the paradigm for 3FT-GPCR interaction
- <a href="/xray-mp-wiki/reagents/ligands/atropine/">Atropine</a> — Orthosteric antagonist co-crystallized in M1AChR-MT7 complex (PDB 6WJC)
- <a href="/xray-mp-wiki/proteins/gpcr/turkey-beta1-ar-m23/">Turkey Beta1-Adrenergic Receptor M23</a> — Template structure (PDB 2Y00) used for molecular replacement in all M1 structure determinations
- <a href="/xray-mp-wiki/proteins/gpcr/m1-star-t4l/">M1-StaR-T4L</a> — Specific thermostabilized M1 receptor construct with T4L fusion used for crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">N-Dodecyl-beta-D-Maltopyranoside (DDM)</a> — Primary detergent used for membrane solubilization and throughout purification
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Crystallization method used for all three M1-StaR-T4L structures
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Final purification step for monodisperse M1-StaR-T4L sample
- <a href="/xray-mp-wiki/concepts/signaling-receptors/biased-agonism/">Biased Agonism in G Protein-Coupled Receptors</a> — HTL9936 was characterized as an unbiased agonist of the M1 receptor across multiple signaling pathways
- <a href="/xray-mp-wiki/reagents/ligands/htl9936/">HTL9936</a> — Selective M1 partial agonist co-crystallized (PDB 6ZG4)
- <a href="/xray-mp-wiki/reagents/ligands/gsk1034702/">GSK1034702</a> — Bitopic M1 agonist co-crystallized (PDB 6ZG9)
- <a href="/xray-mp-wiki/proteins/gpcr/m4-muscarinic-acetylcholine-receptor/">Human M4 Muscarinic Acetylcholine Receptor</a> — Related muscarinic receptor subtype; M1 and M4 structures solved in same study (PDB 5CXV)
- <a href="/xray-mp-wiki/reagents/ligands/pirenzepine/">Pirenzepine</a> — M1-selective antagonist used in induced fit docking studies on M1 structure (PDB 5CXV)
