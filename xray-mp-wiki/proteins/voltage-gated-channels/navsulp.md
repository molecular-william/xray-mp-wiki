---
title: "NavSulP (Sulfitobacter pontiacus Voltage-Gated Sodium Channel)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms1797]
verified: agent
uniprot_id: A9VEV6
---

# NavSulP (Sulfitobacter pontiacus Voltage-Gated Sodium Channel)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A9VEV6">UniProt: A9VEV6</a>

<span class="expr-badge">Bacillus weihenstephanensis</span>

## Overview

NavSulP is a prokaryotic voltage-gated sodium channel (NavBac) cloned from
Sulfitobacter pontiacus. As a homotetrameric channel, each subunit contains six
transmembrane alpha-helices (S1-S6), with S5 and S6 forming the pore domain and
S1-S4 forming voltage sensors. NavSulP exhibits a typical inward sodium current
with half-maximum potentials for activation at -31.2 mV and inactivation at
-62.1 mV. The C-terminal region of NavSulP forms a four-helix bundle (4HB)
that plays critical roles in stabilizing the channel tetramer and accelerating
the channel inactivation rate. The 4HB was visualized by grafting the NavSulP
C-terminal region into the C-terminus of the NaK channel and determining the
crystal structure at 3.2 A resolution. The 4HB connects directly to the inner
helix of the pore domain and promotes the conformational change of the inner
helix required for inactivation.

## Publications

### doi/10.1038##ncomms1797

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3vou">3VOU</a></td>
      <td>3.2</td>
      <td>P3121</td>
      <td>NaK-NavSulP C239 chimera channel (NavSulP C-terminal region grafted into NaK channel)</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli KRX strain (Promega)
- **Construct**: Full-length NavSulP with C-terminal His-tag

**Purification:**

- **Expression system**: E. coli KRX (Promega)
- **Expression construct**: Full-length NavSulP with C-terminal His-tag
- **Tag info**: C-terminal His-tag

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
      <td>Protein expression</td>
      <td>E. coli expression</td>
      <td>—</td>
      <td></td>
      <td>Cells grown at 37 C to OD600 of 0.8, induced with 0.1% rhamnose, grown for 16 h at 18 C</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>French Press</td>
      <td>—</td>
      <td>TBS (20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl)</td>
      <td>Cells suspended in TBS buffer and lysed at 12,000 psi</td>
    </tr>
    <tr>
      <td>Membrane collection</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td>TBS</td>
      <td>Membranes collected by centrifugation at 100,000g for 1 h at 4 C</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>TBS with 40 mM <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a> (Anatrace) + 40 mM <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Cobalt <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>HIS-Select cobalt affinity gel (Sigma)</td>
      <td>TBS + 3 mM <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a> + 0.1 mg/ml <a href="/xray-mp-wiki/reagents/lipids/e-coli-polar-lipids/">E. coli Polar Lipids</a> + 3 mM <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a></td>
      <td>Washed with 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>150 mM NaCl, 20 mM HEPES-NaOH pH 8.0 + 3 mM <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a> + 0.1 mg/ml <a href="/xray-mp-wiki/reagents/lipids/e-coli-polar-lipids/">E. coli Polar Lipids</a> + 3 mM <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a></td>
      <td>Final purification step in gel filtration buffer</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Protein sample</td>
      <td>NaK-NavSulP C239 chimera channel</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal structure of the NaK-NavSulP C239 chimera at 3.2 A resolution. Space group P3121. Data collected at BL38B1 in SPring-8 with approval of JASRI (Proposal numbers 2009B1211, 2010A1270, 2010A1803, 2010B1232). Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using NaK structure (PDB 2AHY) as search model.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3vou">3VOU</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGS</span><span class="topo-outside">M</span><span class="topo-unknown">LSFILTLKRMLKACLRAW</span><span class="topo-outside">KDKEFQ</span><span class="topo-membrane">VLFVLTFLTLTSGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">LDALYFSVVTLTTVGDG</span><span class="topo-inside">NFSPQTD</span><span class="topo-membrane">FGKVFTILYIFIGIGLVFGFI</span><span class="topo-outside">HKLAVNVQLPSILSNRKKETDA</span></span>
<span class="topo-ruler">       130       140        </span>
<span class="topo-line"><span class="topo-outside">YRLEVMEKLEAIEKKLAEHSRQ</span><span class="topo-unknown">GSLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>-2</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>22</td>
      <td>2</td>
      <td>19</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>28</td>
      <td>20</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>53</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>70</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>71</td>
      <td>77</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>98</td>
      <td>75</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>142</td>
      <td>96</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>148</td>
      <td>140</td>
      <td>145</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3vou">3VOU</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGS</span><span class="topo-outside">M</span><span class="topo-unknown">LSFILTLKRMLKACLRA</span><span class="topo-outside">WKDKEFQ</span><span class="topo-membrane">VLFVLTFLTLTSGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">LDALYFSVVTLTTVGDG</span><span class="topo-inside">NFSPQTDF</span><span class="topo-membrane">GKVFTILYIFIGIGLVFGFI</span><span class="topo-outside">HKLAV</span><span class="topo-unknown">NVQ</span><span class="topo-outside">LPSILSNRKKETDA</span></span>
<span class="topo-ruler">       130       140        </span>
<span class="topo-line"><span class="topo-outside">YRLEVMEKLEAIEKKLAEHSRQ</span><span class="topo-unknown">GSLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>-2</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>21</td>
      <td>2</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>28</td>
      <td>19</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>53</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>70</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>71</td>
      <td>78</td>
      <td>68</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>98</td>
      <td>76</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>103</td>
      <td>96</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>106</td>
      <td>101</td>
      <td>103</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>107</td>
      <td>142</td>
      <td>104</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>148</td>
      <td>140</td>
      <td>145</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3vou">3VOU</a> — Chain C (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGS</span><span class="topo-outside">M</span><span class="topo-unknown">LSFILTLKRMLKACLRAW</span><span class="topo-outside">KDKEFQ</span><span class="topo-membrane">VLFVLTFLTLTSGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">LDALYFSVVTLTTVGDG</span><span class="topo-inside">NFSPQTD</span><span class="topo-membrane">FGKVFTILYIFIGIGLVFGFI</span><span class="topo-outside">HKLAVNVQLPSILSNRKKETDA</span></span>
<span class="topo-ruler">       130       140        </span>
<span class="topo-line"><span class="topo-outside">YRLEVMEKLEAIEKKLAEHSRQ</span><span class="topo-unknown">GSLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>-2</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>22</td>
      <td>2</td>
      <td>19</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>28</td>
      <td>20</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>53</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>70</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>71</td>
      <td>77</td>
      <td>68</td>
      <td>74</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>98</td>
      <td>75</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>142</td>
      <td>96</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>148</td>
      <td>140</td>
      <td>145</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3vou">3VOU</a> — Chain D (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGS</span><span class="topo-outside">M</span><span class="topo-unknown">LSFILTLKRMLKACLRA</span><span class="topo-outside">WKDKEFQ</span><span class="topo-membrane">VLFVLTFLTLTSGTIFYSTV</span><span class="topo-inside">EGLRP</span><span class="topo-unknown">LDALYFSVVTLTTVGDG</span><span class="topo-inside">NFSPQTDF</span><span class="topo-membrane">GKVFTILYIFIGIGLVFGFI</span><span class="topo-outside">HKLAV</span><span class="topo-unknown">NVQ</span><span class="topo-outside">LPSILSNRKKETDA</span></span>
<span class="topo-ruler">       130       140        </span>
<span class="topo-line"><span class="topo-outside">YRLEVMEKLEAIEKKLAEHSRQ</span><span class="topo-unknown">GSLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>-2</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>21</td>
      <td>2</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>28</td>
      <td>19</td>
      <td>25</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>48</td>
      <td>26</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>53</td>
      <td>46</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>70</td>
      <td>51</td>
      <td>67</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>71</td>
      <td>78</td>
      <td>68</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>98</td>
      <td>76</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>103</td>
      <td>96</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>106</td>
      <td>101</td>
      <td>103</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>107</td>
      <td>142</td>
      <td>104</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>143</td>
      <td>148</td>
      <td>140</td>
      <td>145</td>
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

### C-terminal four-helix bundle stabilizes the channel tetramer

The C-terminal region of NavSulP (residues 239-260) forms a four-helix bundle (4HB) that stabilizes the tetrameric channel. The 4HB is composed of hydrophobic residues forming a hydrophobic core. Mutations of interface residues (V246R, L250R, I253R, L257R) destabilized the tetramer and reduced the inactivation rate. The NavSulP DeltaC239 deletion mutant migrated predominantly as monomers in size-exclusion chromatography and crosslinking analysis, confirming that the C-terminal region is essential for tetramer stability.

### Four-helix bundle accelerates channel inactivation

Deletion of the C-terminal region (NavSulP DeltaC239) dramatically reduced the inactivation rate by approximately 40-fold (tau_inact = 1,701 ms vs 40.6 ms for wild-type at 0 mV). Point mutations in the 4HB hydrophobic core similarly reduced inactivation rates. The 4HB is directly connected to the inner helix (S6) of the pore domain via a conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residue (G221). The G221A mutation, which increases inner helix rigidity, also severely reduced inactivation (tau_inact = 1,850 ms), suggesting the 4HB promotes inactivation by facilitating conformational changes in the inner helix.

### Distinct inactivation mechanism from potassium channels

Unlike [KCSA](/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/), where the C-terminal bundle reduces inactivation, the NavSulP 4HB accelerates inactivation. This suggests that the inactivation mechanism of prokaryotic sodium channels (NavBacs) differs from the C-type inactivation of potassium channels. The 4HB generates a counter force on the inner helix that promotes conformational changes leading to pore inactivation. The selectivity filter of NavSulP, which features an elaborate intersubunit hydrogen-bond network (as seen in [NAVAB](/xray-mp-wiki/proteins/voltage-gated-channels/navab/)), may collapse during inactivation promoted by the 4HB through inner helix conformational changes.

### Role of Lys249 in intersubunit interactions

The 4HB involves specific intersubunit interactions, including a salt bridge of Lys249 with Glu251 and Glu254 of adjacent subunits. Mutation K249E reduced the inactivation rate to a level similar to the C-terminal deletion mutant, while E251K and E254K mutations alone did not significantly reduce inactivation. This suggests Lys249 interacts with other residues in addition to Glu251 and Glu254 for accelerating channel inactivation.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/navab/">NavAb Bacterial Voltage-Gated Sodium Channel</a> — Prokaryotic voltage-gated sodium channel homolog from Arcobacter butzleri, used for structural comparison (PDB 3RVZ)
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KCSA</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/lipids/e-coli-polar-lipids/">E. coli Polar Lipids</a> — Additive used in purification or crystallization buffers
