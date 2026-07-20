---
title: "E. coli Diacylglycerol Kinase (DgkA)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##NATURE12179, doi/10.1038##NCOMMS10140]
verified: agent
uniprot_id: P0ABN1
---

# E. coli Diacylglycerol Kinase (DgkA)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0ABN1">UniProt: P0ABN1</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

Diacylglycerol kinase (DgkA) from Escherichia coli is a 121-residue integral membrane enzyme that catalyses the ATP-dependent phosphorylation of diacylglycerol ([DAG](/xray-mp-wiki/reagents/lipids/dag/)) to phosphatidic acid. For half a century, DgkA has served as a model for investigating membrane protein enzymology, folding, assembly, and stability. The crystal structure reveals a homo-trimeric enzyme with three transmembrane helices (H1-H3) and an N-terminal amphiphilic surface helix per monomer. The three active sites are of the composite, shared-site type, formed between adjacent subunits. The structure was determined by the [LCP](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) (in meso) method using 7.8 [MAG](/xray-mp-wiki/reagents/lipids/mag/) as host lipid, with phases obtained by Se-Met [SAD](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/).

## Publications

### doi/10.1038##NATURE12179

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3ze4">3ZE4</a></td>
      <td>2.05</td>
      <td></td>
      <td>DgkA Delta7 (Ala41Cys Cys46Ala Ile53Val Ile70Leu Met96Leu Val107Asp Cys113Ala) with 7.8 <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a></td>
      <td><a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a> (monoacylglycerol)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli B893(DE3) methionine auxotroph pTrcHisB vector
- **Construct**: Wild-type dgkA Delta4 (Ile53Cys Ile70Leu Met96Leu Val107Asp) and Delta7 mutants cloned into pTrcHisB using NcoI and EcoRI sites

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
      <td>Protein production</td>
      <td>Auto-induction or <a href="/xray-mp-wiki/reagents/additives/iptg/">Iptg</a> induction in E. coli</td>
      <td>--</td>
      <td>-- + --</td>
      <td>DgkA proteins expressed and purified as described with an additional <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) step; Se-Met labelling performed using methionine auxotroph B893(DE3) in M9 minimal media</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (in meso) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>DgkA (Delta7 Delta4 or wild-type) at 12 mg/ml reconstituted into 7.8 <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a> cubic mesophase</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Direct snap-cooling in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown in glass sandwich plates; initial trials with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (9.9 <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a>) at 20 C yielded minute crystals; optimization with shorter-chain <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a> (7.8 <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a>) at 4 C gave quality crystals; 50 nl protein-lipid mesophase + 800 nl precipitant</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ze4">3ZE4</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GHHHHHHELANNTTG</span><span class="topo-inside">F</span><span class="topo-unknown">TRIIKAAGYSWKGLRAAWIN</span><span class="topo-inside">EAAFRQ</span><span class="topo-membrane">EGVAVLLAVVIACWL</span><span class="topo-outside">DVDA</span><span class="topo-membrane">ITRVLLISSVMLVMIV</span><span class="topo-inside">EILNSAIEAVVDRIGSEYHELSGRAKDMGSAAVL</span><span class="topo-membrane">IAIIVAVIT</span></span>
<span class="topo-ruler">       130</span>
<span class="topo-line"><span class="topo-membrane">WCILL</span><span class="topo-outside">WSHF</span><span class="topo-unknown">G</span></span>
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
      <td>15</td>
      <td>-8</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>16</td>
      <td>16</td>
      <td>7</td>
      <td>7</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>36</td>
      <td>8</td>
      <td>27</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>37</td>
      <td>42</td>
      <td>28</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>57</td>
      <td>34</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>61</td>
      <td>49</td>
      <td>52</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>77</td>
      <td>53</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>111</td>
      <td>69</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>125</td>
      <td>103</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>126</td>
      <td>129</td>
      <td>117</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>130</td>
      <td>121</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ze4">3ZE4</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GHHHHHHELANNTT</span><span class="topo-inside">GF</span><span class="topo-unknown">TRIIKAAGYSWKGLRAAWI</span><span class="topo-inside">NEAAFRQ</span><span class="topo-membrane">EGVAVLLAVVIACWL</span><span class="topo-outside">DVDA</span><span class="topo-membrane">ITRVLLISSVMLVMI</span><span class="topo-inside">VEILNSAIEAVVDRIGSEYHELSGRAKDMGSAAVL</span><span class="topo-membrane">IAIIVAVIT</span></span>
<span class="topo-ruler">       130</span>
<span class="topo-line"><span class="topo-membrane">WCILLW</span><span class="topo-outside">SHF</span><span class="topo-unknown">G</span></span>
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
      <td>14</td>
      <td>-8</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>16</td>
      <td>6</td>
      <td>7</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>35</td>
      <td>8</td>
      <td>26</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>42</td>
      <td>27</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>57</td>
      <td>34</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>61</td>
      <td>49</td>
      <td>52</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>76</td>
      <td>53</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>111</td>
      <td>68</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>126</td>
      <td>103</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>129</td>
      <td>118</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>130</td>
      <td>121</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3ze4">3ZE4</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GHHHHHHELANNTTGFTRIIKAAGYSWKGLRAAWIN</span><span class="topo-inside">EAAFRQ</span><span class="topo-membrane">EGVAVLLAVVIACWL</span><span class="topo-outside">DVDA</span><span class="topo-membrane">ITRVLLISSVMLVMI</span><span class="topo-inside">VEILNSAIEAVVDRIGSEYHELSGRAKDMGSAAVL</span><span class="topo-membrane">IAIIVAVIT</span></span>
<span class="topo-ruler">       130</span>
<span class="topo-line"><span class="topo-membrane">WCILLW</span><span class="topo-outside">SH</span><span class="topo-unknown">FG</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>36</td>
      <td>-8</td>
      <td>27</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>37</td>
      <td>42</td>
      <td>28</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>57</td>
      <td>34</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>61</td>
      <td>49</td>
      <td>52</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>76</td>
      <td>53</td>
      <td>67</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>111</td>
      <td>68</td>
      <td>102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>126</td>
      <td>103</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>128</td>
      <td>118</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>130</td>
      <td>120</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##NCOMMS10140

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4uxx">4UXX</a></td>
      <td>2.7</td>
      <td>P3321</td>
      <td>DgkA Delta4 construct (I53C I70L M96L V107D) co-crystallized with 9.9 <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a> and soaked with zinc-ACP; ternary complex with ACP (non-hydrolysable <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> analogue) and lipid substrate bound in active site asBC</td>
      <td>Zinc-ACP (adenylylmethylenediphosphonate), <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a> (monoacylglycerol lipid substrate)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli B893(DE3) methionine auxotroph pTrcHisB vector
- **Construct**: Wild-type dgkA Delta4 (Ile53Cys Ile70Leu Met96Leu Val107Asp) and Delta7 mutants cloned into pTrcHisB using NcoI and EcoRI sites

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
      <td>Protein expression and purification</td>
      <td>Auto-induction in E. coli</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Delta4-DgkA expressed and purified as previously described (Nature 2012); co-crystallized with 9.9 <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a> host lipid in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/); zinc-ACP soaked into crystals</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> (in meso) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Delta4-DgkA reconstituted into 9.9 <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a> cubic mesophase at 4 degrees C</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Direct snap-cooling in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Co-crystallized with 9.9 <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a> host lipid; soaked with zinc-ACP to obtain ternary complex; also obtained room-temperature SFX structure using XFEL (Delta7 construct with 7.9 <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a>)</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Homo-trimeric architecture with shared active sites

DgkA forms a homo-trimer with approximate three-fold symmetry. Each subunit has a bundle of three transmembrane helices (H1-H3) arranged as an isosceles triangle when viewed from the cytosol. The trimer core consists of H2 from each subunit forming a parallel three-helix bundle. The active sites are composite and shared between subunits: active site AB is formed by the surface helix of subunit A and H1-H3 of subunit B. This matches the biochemical evidence from subunit mixing experiments showing that DgkA has three active sites per trimer with moderate heteroallostery.

### Active site architecture

The putative active site is located at the interface between the N-terminal surface helix of one subunit and the transmembrane helices of an adjacent subunit. Bound [MAG](/xray-mp-wiki/reagents/lipids/mag/) (monoacylglycerol) density in the Delta7 structure identifies the lipid substrate binding region. [ATP](/xray-mp-wiki/reagents/ligands/atp/) was docked with the adenyl moiety interacting with the cytosolic loop and the triphosphate extending toward the lipid-binding pocket. Divalent cations (Zn2+ found coordinated by Glu28 and Glu76) are required for full activation.

### Comparison with solution NMR model

The crystal structure differs significantly from the published solution NMR model of DgkA, particularly in that domain swapping is absent in the crystal structure. In the NMR model, H3 from one subunit contacts H1 and H2 from an adjacent subunit, whereas in the crystal structure, H2 from each subunit forms the trimer core with H1 and H3 extending outward. This results in different active site architecture between the two models.

### Osmotic stress sensor hypothesis

DgkA is probably activated in vivo under hypo-osmotic conditions to enhance production of the osmoregulant membrane-derived oligosaccharide. The N-terminal amphiphilic surface helix connected to H1 by a short hinge may act as a sensor of osmotic stress by responding to bilayer thickness and lateral pressure, adjusting active site architecture and enhancing kinase activity.

### Ternary complex structure and catalytic mechanism

The DgkA ternary complex with ACP (non-hydrolysable [ATP](/xray-mp-wiki/reagents/ligands/atp/) analogue) and lipid substrate reveals a direct in-line phosphoryl transfer mechanism. The gamma-phosphate of [ATP](/xray-mp-wiki/reagents/ligands/atp/) is positioned ~4 A from the 1-OH of the lipid substrate. Glu69 acts as the catalytic base, abstracting a proton from the lipid 1-OH to create a reactive alkoxide that attacks the gamma-phosphorus. The pentavalent transition intermediate is stabilized by Asn72 and/or Arg9.

### Active site comparison with protein kinase A

Striking resemblance exists between DgkA and cAMP-dependent protein kinase A (PKA): Glu69 (DgkA) vs Asp166 (PKA) as catalytic base; Lys94 vs Lys72 for alpha-phosphate coordination; Asp80 vs Glu91 stabilizing the catalytic lysine; Glu76 vs Asp184 chelating metal ions; Asn72 vs Asn171 stabilizing the transition state. This suggests convergent evolution of the kinase active site architecture.

### Zinc coordination in the active site

Two zinc ions (Zn1, Zn2) are bound to ACP, coordinated by Glu28, Glu76, and the triphosphate moiety. Zinc serves the same role as magnesium in other kinases - electrostatic binding to the gamma-phosphate renders the phosphorus more susceptible to nucleophilic attack. Zn1 coordinates alpha- and beta-phosphates while Zn2 coordinates beta- and gamma-phosphates.

### Room-temperature SFX validation

Serial femtosecond crystallography (SFX) at an X-ray free-electron laser (XFEL) confirmed the ternary complex structure at room temperature, ruling out radiation damage artefacts. Alternative conformers for Glu34, Glu69, and Glu76 were observed at RT, suggesting functionally relevant conformational states involved in the catalytic cycle and product release.


## Cross-References

- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein (9.9 MAG)</a> — Host lipid for initial in meso crystallization trials
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (In Meso) Crystallization</a> — Crystallization method used to obtain DgkA structures
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> — Used for Se-Met [SAD](/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/) phasing
- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside (DM)</a> — Detergent in enzyme assay mixture
- <a href="/xray-mp-wiki/reagents/lipids/dag/">DAG</a> — Referenced in context related to DAG
- <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a> — Referenced in context related to MAG
- <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> — Referenced in context related to ATP
- <a href="/xray-mp-wiki/reagents/additives/iptg/">Iptg</a> — Referenced in context related to Iptg
- <a href="/xray-mp-wiki/reagents/additives/mpd/">MPD</a> — Referenced in context related to MPD
- <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate</a> — Referenced in context related to Acetate
- <a href="/xray-mp-wiki/reagents/lipids/cardiolipin/">Cardiolipin</a> — Component of enzyme assay buffer
- <a href="/xray-mp-wiki/reagents/buffers/pipes/">PIPES Buffer</a> — Buffer used in kinase and ADP assays
- <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">Single-Wavelength Anomalous Diffraction (SAD)</a> — Phasing method for Delta7 structure
- <a href="/xray-mp-wiki/proteins/enzymes/dgka/">Dgka</a> — Referenced in context related to Dgka
