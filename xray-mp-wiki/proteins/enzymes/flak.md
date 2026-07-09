---
title: "FlaK (Preflagellin Peptidase from Methanococcus maripaludis)"
created: 2026-06-02
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature10218]
verified: regex
uniprot_id: A9A677
---

# FlaK (Preflagellin Peptidase from Methanococcus maripaludis)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A9A677">UniProt: A9A677</a>

<span class="expr-badge">Methanococcus maripaludis</span>

## Overview

FlaK is a preflagellin peptidase (PFP) from the archaeon Methanococcus maripaludis. It belongs to the GXGD family of polytopic membrane proteases that cleave type-II (N_in-C_out) membrane protein substrates using a pair of essential aspartyl residues. FlaK processes preflagellin leader peptides before flagellin incorporation into the archaeal flagellum. The crystal structure reveals six transmembrane helices with the GXGD motif positioned at the center of the transmembrane bundle.


## Publications

### doi/10.1038##nature10218

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3s0x">3S0X</a></td>
      <td>3.6 A</td>
      <td>Not specified</td>
      <td>Full-length FlaK (MmarC6_0338) from M. maripaludis strain C6</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli Rosetta 2 (DE3) cells
- **Construct**: MmarC6_0338 encoding FlaK with N-terminal His6-tag and Gly-Ser-Gly-Ser linker between thrombin site and FlaK sequence, cloned into pET-28a
- **Notes**: Se-Met substituted version expressed in M9 minimum media supplemented with Se-Met, induced by 1 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg) at A600 of 0.6, grown at 20 deg.C for 16 h

**Purification:**

- **Expression system**: E. coli Rosetta 2 (DE3)
- **Expression construct**: His6-tagged FlaK with Gly-Ser-Gly-Ser linker for thrombin cleavage
- **Tag info**: [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag), removed by thrombin cleavage overnight at 22 deg.C

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
      <td>Spheroplast method</td>
      <td>--</td>
      <td>50 mM sodium phosphate pH 7.2, 500 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">beta-Mercaptoethanol</a>, complete protease inhibitor cocktail (Roche, without <a href="/xray-mp-wiki/reagents/additives/edta">EDTA</a>) + --</td>
      <td>Cytoplasmic membranes prepared from M. maripaludis strain C6 genomic DNA expression</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM sodium phosphate pH 7.2, 500 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">beta-Mercaptoethanol</a> + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/foscholine-12">Foscholine-12</a> (Anatrace)</td>
      <td>Membrane suspension solubilized by adding <a href="/xray-mp-wiki/reagents/detergents/foscholine-12">Foscholine-12</a> powder</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> metal-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> (Clontech)</td>
      <td>50 mM sodium phosphate pH 7.2, 500 mM NaCl, 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">beta-Mercaptoethanol</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/foscholine-12">Foscholine-12</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/foscholine-12">Foscholine-12</a></td>
      <td>His-tagged protein eluted from <a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> column</td>
    </tr>
    <tr>
      <td>Desalting</td>
      <td>Desalting column</td>
      <td>Sephadex G-25</td>
      <td>-- + --</td>
      <td>Sample passed through Sephadex G-25 desalting column before thrombin cleavage</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Proteolytic cleavage</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Thrombin cleavage overnight at 22 deg.C to remove N-terminal His tag</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200 Increase SEC Resin</a> (GE Healthcare)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.3, 100 mM NaCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/foscholine-12">Foscholine-12</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/foscholine-12">Foscholine-12</a></td>
      <td>Final purification step</td>
    </tr>
  </tbody>
</table>
**Final sample**: Concentrated to approximately 10 mg/ml for crystallization

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Se-Met substituted FlaK at 4 mg/ml (lower concentration due to precipitation during dialysis)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>30% <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a> 300, 50 mM <a href="/xray-mp-wiki/reagents/buffers/glycine">Glycine</a> pH 9.5, 100 mM NaCl</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1 (1 ul protein + 1 ul well solution)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>22 deg.C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Needle-shaped crystals appeared in 2 days, full size in 1 week</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Dehydrated by equilibrating 24 h against well solution with 40% <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a> 300, then flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected at NSLS (X25, X29) and APS (24-ID-C, E). Structure determined by Se-Met SAD phasing.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3s0x">3S0X</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSHG</span><span class="topo-inside">SGS</span><span class="topo-membrane">MIEYIIGALGLIIASVQ</span><span class="topo-outside">D</span><span class="topo-unknown">FRSR</span><span class="topo-outside">EI</span><span class="topo-membrane">EDYIWIFLAVFGVLFAIYS</span><span class="topo-inside">SITLLDYSIL</span><span class="topo-membrane">INSISGFVICFILGYMMFLSG</span><span class="topo-outside">I</span><span class="topo-membrane">GGGDGKMLIGLGALVPKF</span><span class="topo-inside">QMPIYT</span><span class="topo-unknown">SLGTLL</span><span class="topo-inside">NLNYV</span><span class="topo-membrane">PTF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       </span>
<span class="topo-line"><span class="topo-membrane">PIMVFINGIFFMVFLPFVILFR</span><span class="topo-outside">NILNGARPKTGKEFILMFFGEKMKVNVAKEQKRLIMGQNDKINFFPA</span><span class="topo-unknown">AD</span><span class="topo-outside">DEDFSKYSNNEEIWVTPQI</span><span class="topo-membrane">PLIIPITLSYLVTPIIGD</span><span class="topo-inside">RILDFLI</span><span class="topo-unknown">PF</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>494</td>
      <td>497</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>7</td>
      <td>498</td>
      <td>500</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>24</td>
      <td>501</td>
      <td>517</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>25</td>
      <td>518</td>
      <td>518</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>26</td>
      <td>29</td>
      <td>519</td>
      <td>522</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>31</td>
      <td>523</td>
      <td>524</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>50</td>
      <td>525</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>60</td>
      <td>544</td>
      <td>553</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>81</td>
      <td>554</td>
      <td>574</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>82</td>
      <td>575</td>
      <td>575</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>100</td>
      <td>576</td>
      <td>593</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>106</td>
      <td>594</td>
      <td>599</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>107</td>
      <td>112</td>
      <td>600</td>
      <td>605</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>113</td>
      <td>117</td>
      <td>606</td>
      <td>610</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>142</td>
      <td>611</td>
      <td>635</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>189</td>
      <td>636</td>
      <td>682</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>191</td>
      <td>683</td>
      <td>684</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>192</td>
      <td>210</td>
      <td>685</td>
      <td>703</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>228</td>
      <td>704</td>
      <td>721</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>235</td>
      <td>722</td>
      <td>728</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>237</td>
      <td>729</td>
      <td>730</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3s0x">3S0X</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GSHG</span><span class="topo-inside">SGSM</span><span class="topo-membrane">IEYIIGALGLIIASVQDFR</span><span class="topo-outside">SREI</span><span class="topo-membrane">EDYIWIFLAVFGVLFAIY</span><span class="topo-inside">SSITLLDYSILINS</span><span class="topo-membrane">ISGFVICFILGYMMFLSGIGG</span><span class="topo-outside">G</span><span class="topo-membrane">DGKMLIGLGALVP</span><span class="topo-inside">KFQMPIYTSLGTLLNLNYVP</span><span class="topo-membrane">TF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       </span>
<span class="topo-line"><span class="topo-membrane">PIMVFINGIFFMVFLPFVILFR</span><span class="topo-outside">NILNGARPK</span><span class="topo-unknown">TGKEF</span><span class="topo-outside">ILMFFGEKM</span><span class="topo-unknown">KVNVAKEQKRLIMGQNDKINFFPAADDEDFSKYSNNEEIW</span><span class="topo-outside">VTPQ</span><span class="topo-membrane">IPLIIPITLSYLVTP</span><span class="topo-inside">IIGD</span><span class="topo-unknown">RILDFL</span><span class="topo-inside">I</span><span class="topo-unknown">PF</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>494</td>
      <td>497</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>5</td>
      <td>8</td>
      <td>498</td>
      <td>501</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>27</td>
      <td>502</td>
      <td>520</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>31</td>
      <td>521</td>
      <td>524</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>49</td>
      <td>525</td>
      <td>542</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>63</td>
      <td>543</td>
      <td>556</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>84</td>
      <td>557</td>
      <td>577</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>85</td>
      <td>85</td>
      <td>578</td>
      <td>578</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>98</td>
      <td>579</td>
      <td>591</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>99</td>
      <td>118</td>
      <td>592</td>
      <td>611</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>142</td>
      <td>612</td>
      <td>635</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>151</td>
      <td>636</td>
      <td>644</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>152</td>
      <td>156</td>
      <td>645</td>
      <td>649</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>157</td>
      <td>165</td>
      <td>650</td>
      <td>658</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>205</td>
      <td>659</td>
      <td>698</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>206</td>
      <td>209</td>
      <td>699</td>
      <td>702</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>210</td>
      <td>224</td>
      <td>703</td>
      <td>717</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>225</td>
      <td>228</td>
      <td>718</td>
      <td>721</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>229</td>
      <td>234</td>
      <td>722</td>
      <td>727</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>235</td>
      <td>235</td>
      <td>728</td>
      <td>728</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>236</td>
      <td>237</td>
      <td>729</td>
      <td>730</td>
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

### GXGD protease active site architecture

The two aspartyl residues essential for catalysis (Asp 18 and Asp 79) are located at the ends of TM helices alpha1 and alpha4, respectively. The GXGD motif (containing Asp 79) and helix 4 are positioned at the center of the transmembrane bundle, surrounded by other TM helices. The conserved asparagine on alpha5 (Asn 120) forms a hydrogen bond with the carbonyl oxygen of Gly 220 from the extended segment between alpha6 and alpha6a, which would be unfavorably exposed to lipid if the carboxy-terminus were positioned elsewhere.

### Conformational switching mechanism

The 12 A gap between Asp 18 and Asp 79 in the crystal structure suggests FlaK can adopt an inactive conformation where the two catalytic aspartyl residues are structurally uncoupled. Crosslinking experiments with [M2M](/xray-mp-wiki/reagents/additives/m2m) between Cys 25 (alpha2) and Cys 206 (alpha6) bridged this gap and maintained activity, while crosslinking that prevented movement of Asp 18 and Asp 79 toward each other completely eliminated activity. This conformational switching behavior parallels that of presenilin, where the two catalytic aspartates also do not closely oppose each other in all conformations.

### Membrane tilting and constriction

The tilted arrangement of TM helices accommodates unusual peripheral structures (alpha4a and alpha6a) and prevents charged groups (Asp 26, Asp 49, Asp 225) from entering the hydrophobic membrane region. Tyrosine and tryptophan residues cluster at the water-lipid interface, marking the membrane boundaries. The tilted model requires the membrane to constrict around the protease, a feature previously thought unique to intramembrane proteases.

### Evolutionary relationship to presenilin

Comparison of FlaK with presenilin models reveals that TM1, TM4, and TM6 of FlaK are equivalent to presenilin TM6, TM7, and TM9, respectively. Both proteases house their active sites in open hydrophilic cavities surrounded by TM segments carrying catalytic aspartates and a C-terminal TM segment with conserved motifs. This structural similarity reinforces the evolutionary relationship between prokaryotic GXGD proteases and the human presenilin-gamma-secretase complex.


## Cross-References

- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/gxgd-proteases/">GXGD Proteases</a> — FlaK is the prototypic GXGD family member whose structure was solved
- <a href="/xray-mp-wiki/proteins/enzymes/sppa-ec/">Signal Peptide Peptidase A from Escherichia coli</a> — Related signal peptidase family member
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> — Se-Met SAD phasing used for structure determination
- <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">Single-Wavelength Anomalous Diffraction</a> — SAD phasing method used for structure solution
- <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a> — Crystallization method used for FlaK
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — SEC on Superdex-200 used for final purification
- <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/talon">TALON</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/detergents/foscholine-12">Foscholine-12</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/m2m">M2M</a> — Entity mentioned in text
