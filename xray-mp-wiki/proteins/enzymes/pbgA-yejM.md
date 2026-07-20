---
title: "PbgA (YejM) Inner Membrane LPS Sensor"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##srep30815, doi/10.1038##s41586-020-2597-x, doi/10.1128##mBio.03277-19]
verified: agent
uniprot_id: ['P0AD27', 'P40709']
---

# PbgA (YejM) Inner Membrane LPS Sensor

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0AD27">UniProt: P0AD27</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P40709">UniProt: P40709</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

[PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) (also known as YejM) is an essential inner membrane protein in Gram-negative bacteria that functions as a sensor of lipopolysaccharide (LPS) levels on the periplasmic leaflet of the inner membrane, coordinating LPS biogenesis by regulating the stability of LpxC, the committed enzyme in [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) biosynthesis. [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) contains five N-terminal transmembrane helices upon which a C-terminal periplasmic globular domain (residues 191-586) sits, connected by a three-helix bundle interfacial domain (IFD). Earlier crystal structures of the isolated periplasmic domain from Salmonella typhimurium and Escherichia coli (Lu et al., 2016, Sci Rep) revealed a fold resembling arylsulfatases and lipoteichoic acid synthases, but lacking their enzymatic activities, and were interpreted as supporting a [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) transport function. However, the full-length crystal structure of [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) determined at 2.0 A resolution (Clairfeuille et al., 2020, Nature) — together with physiological, proteomic, and pharmacological studies — definitively refuted the cardiolipin-transporter model. The full-length structure shows that the periplasmic domain remains anchored onto the TMD (total interdomain contacts ~2,550 A2) and protrudes only ~60 A above the inner membrane, inconsistent with a domain that shuttles across the ~200 A periplasm. Crucially, the structure revealed a lipid A-binding (LAB) motif along the periplasmic leaflet of the inner membrane, formed by the IFD and TMD. [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) binds LPS with remarkable selectivity — recognizing a single phospho-GlcNAc unit of [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) through a backbone-mediated coordination scheme — and does not require divalent cations or basic residues, distinguishing it from known LPS receptors. [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) constitutively associates with LapB, and together they antagonize FtsH-mediated degradation of LpxC when LPS demand is high; when periplasmic LPS accumulates, LPS binding to [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) alters the PbgA-LapB complex and promotes FtsH-dependent LpxC degradation, forming a rheostat that controls LPS synthesis. Synthetic peptides derived from the [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) LAB motif (LAB peptides) selectively bind LPS and exhibit broad-spectrum Gram-negative antibacterial activity, including against polymyxin-resistant strains. [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) is essential for E. coli pathogenesis, outer membrane integrity, and growth.


## Publications

### doi/10.1038##srep30815

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5i5h">5I5H</a></td>
      <td>1.64</td>
      <td>P 21</td>
      <td>StPbgA245-586 (S. typhimurium <a href="/xray-mp-wiki/proteins/enzymes/pbgA-yejM/">PbgA (YejM) Cardiolipin Transport Protein</a> periplasmic domain, residues 245-586)</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21-Gold(DE3)
- **Construct**: Full-length [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) (residues 1-586) with C-terminal TEV-2xFlag-hexahistidine tag

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
      <td>E. coli BL21(DE3) expression</td>
      <td>—</td>
      <td>LB medium with 50 ug/mL <a href="/xray-mp-wiki/reagents/additives/kanamycin/">Kanamycin</a> + --</td>
      <td>Induced with 0.1 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> for 12 h at 20 C.</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Cell disruption at 30,000 psi</td>
      <td>—</td>
      <td>20 mM Tris-Cl pH 7.8, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, cOmplete protease inhibitor, 1 mM DNase, 1 mM PMSF + --</td>
      <td>Debris removed by centrifugation at 120,000 g for 25 min at 4 C.</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td>20 mM Tris-Cl pH 7.8, 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + --</td>
      <td>Eluted with 20 mM Tris-Cl pH 7.8, 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>. Buffer exchanged for further processing.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, sitting drop</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>PbgA245-586 from S. typhimurium and E. coli crystallized by <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a>. StPbgA191-586 showed degradation and crystallized from the degradation product.</td>
    </tr>
  </tbody>
</table>
### doi/10.1038##s41586-020-2597-x

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6xlp">6XLP</a></td>
      <td>4.6</td>
      <td>P 31</td>
      <td>Full-length E. coli <a href="/xray-mp-wiki/proteins/enzymes/pbgA-yejM/">PbgA (YejM) Cardiolipin Transport Protein</a> (residues 1-586) with C-terminal TEV-2xFlag-hexahistidine tag</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21-Gold(DE3)
- **Construct**: Full-length [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) (residues 1-586) with C-terminal TEV-2xFlag-hexahistidine tag

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
      <td>E. coli BL21-Gold(DE3) expression</td>
      <td>—</td>
      <td>TB autoinduction medium + --</td>
      <td>Expression for 48 h at 17 C in autoinduction medium.</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Sonication</td>
      <td>—</td>
      <td>50 mM Tris pH 8, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 1 ug/mL benzonase, 1 mM PMSF, Roche protease inhibitor tablets + --</td>
      <td>50 g cell pellet resuspended in 250 mL buffer.</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>50 mM Tris pH 8, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> or 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Solubilization for 2 h at 4 C under gentle agitation. Insoluble debris pelleted at 18,000 rpm for 1 h.</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td>M2-agarose <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> resin batch binding</td>
      <td>—</td>
      <td>50 mM Tris pH 8, 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + 0.01% (w/v) <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> or 0.1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Batch binding to 20 mL M2-agarose <a href="/xray-mp-wiki/reagents/protein-tags/flag-tag/">FLAG</a> resin for 2 h at 4 C. Unbound washed with 10 CV of purification buffer.</td>
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
      <td>Full-length <a href="/xray-mp-wiki/proteins/enzymes/pbgA-yejM/">PbgA (YejM) Cardiolipin Transport Protein</a> crystallized in LCP using <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> as the host lipid. <a href="/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/">Phosphatidylethanolamine</a> was added to allow high-resolution diffraction. Two crystal forms: C2 at 2.0 A (synchrotron) and P31 at 4.6 A (XFEL, with 7.9 <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a> as viscosity enhancer for injection).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6xlp">6XLP</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGS</span><span class="topo-outside">MVTHRQRYREKVSQM</span><span class="topo-membrane">VSWGHWFALFNILLSLVIGS</span><span class="topo-inside">RYLFIADWPTTLAGRIYSY</span><span class="topo-membrane">VSIIGHFSFLVFATYLLILFPLTFIV</span><span class="topo-outside">GSQR</span><span class="topo-membrane">LMRFLSVILATAGMTLLLI</span><span class="topo-inside">DSEVFTRFHLHLN</span><span class="topo-unknown">P</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">IVWQLV</span><span class="topo-inside">INPDENEMARDW</span><span class="topo-membrane">QLMFISVPVILLLELVFATWSW</span><span class="topo-outside">QK</span><span class="topo-unknown">LRSLTR</span><span class="topo-outside">R</span><span class="topo-membrane">RRFARPLAAFLFIAFIASHV</span><span class="topo-inside">VYIWADANFY</span><span class="topo-unknown">RPITMQ</span><span class="topo-inside">RANLPLSYPMTA</span><span class="topo-unknown">RRFLEK</span><span class="topo-inside">HGLLDAQEYQRRLIEQG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">NPDAVSVQYPLSELRYRDMGTGQNVLLITVDGLNYSRFEKQMPALAGFAEQNISFTRHMSSGNTTDNGIFGLFYGISPSYMDGILSTRTPAALITALNQQGYQLGLFSSDGFTSPLYRQA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">LLSDFSMPSVRTQSDEQTATQWINWLGRYAQEDNRWFSWVSFNGTNIDDSNQQAFARKYSRAAGNVDDQINRVLNALRDSGKLDNTVVIITAGRGIPLSEEEETFDWSHGHLQVPLVIHW</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590      </span>
<span class="topo-line"><span class="topo-inside">PGTPAQRINALTDHTDLMTTLMQRLLHVSTPASEYSQGQDLFNPQRRHYWVTAADNDTLAITTPKKTLVLNNNGKYRTYNLRGERVKDEKPQLSLLLQVLTDEKRFIAN</span><span class="topo-unknown">GENLYFQ</span></span>
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
      <td>4</td>
      <td>18</td>
      <td>1</td>
      <td>15</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>38</td>
      <td>16</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>57</td>
      <td>36</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>83</td>
      <td>55</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>87</td>
      <td>81</td>
      <td>84</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>106</td>
      <td>85</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>107</td>
      <td>119</td>
      <td>104</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>126</td>
      <td>117</td>
      <td>123</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>127</td>
      <td>138</td>
      <td>124</td>
      <td>135</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>160</td>
      <td>136</td>
      <td>157</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>161</td>
      <td>162</td>
      <td>158</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>168</td>
      <td>160</td>
      <td>165</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>169</td>
      <td>169</td>
      <td>166</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>189</td>
      <td>167</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>199</td>
      <td>187</td>
      <td>196</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>205</td>
      <td>197</td>
      <td>202</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>206</td>
      <td>217</td>
      <td>203</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>218</td>
      <td>223</td>
      <td>215</td>
      <td>220</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>224</td>
      <td>589</td>
      <td>221</td>
      <td>586</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1128##mBio.03277-19

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6v8q">6V8Q</a></td>
      <td>2.7</td>
      <td>P2<sub>1</sub></td>
      <td>Full-length PbgA (residues 1-586) from S. Typhimurium 14028s, cloned into pBAD24 with C-terminal His6 tag, expressed in E. coli DH5alpha, crystallized with <a href="/xray-mp-wiki/reagents/lipids/cardiolipin/">Cardiolipin</a></td>
      <td><a href="/xray-mp-wiki/reagents/lipids/cardiolipin/">Cardiolipin</a> (CL1 in TM domain, CL2 at membrane-periplasm interface)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21-Gold(DE3)
- **Construct**: Full-length [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) (residues 1-586) with C-terminal TEV-2xFlag-hexahistidine tag

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6v8q">6V8Q</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVTHRQ</span><span class="topo-inside">RYREKVSQMV</span><span class="topo-membrane">SWGHWFALFNILLATLLGS</span><span class="topo-outside">RYLFVADWPTTLAGRIYSY</span><span class="topo-membrane">LSIVGHFSFLVFATYLLILFPLTFIV</span><span class="topo-inside">MSQRL</span><span class="topo-membrane">MRFLSAILATAGMTLLL</span><span class="topo-outside">IDSEVFTRFHLHLN</span><span class="topo-unknown">PIVW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">ELVIN</span><span class="topo-outside">P</span><span class="topo-unknown">DQNEM</span><span class="topo-outside">ARDWQLM</span><span class="topo-membrane">FISVPVILLIEMLFATWS</span><span class="topo-inside">WQKLRSL</span><span class="topo-unknown">TRRR</span><span class="topo-inside">H</span><span class="topo-membrane">FARPLAAFFFVSFIASHL</span><span class="topo-outside">IYIWADANFY</span><span class="topo-unknown">RPITMQ</span><span class="topo-outside">RANLPLSYPMTA</span><span class="topo-unknown">RRFLEK</span><span class="topo-outside">HGLLDAQEYQRRLVEQGNPE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">AVSVQYPLSNLHYRDMGTGQNVLLITVDGLNYSRFEKQMPELVTFAEQNIDFTRHMSSGNTTDNGIFGLFYGISPGYMDGVLSTRTPAALITALNQQGYQLGLFSSDGFASPLYRQALLS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">DFSMPAAQTQSDAQTASQWIDWLGRYAQEDNRWFSWISFNGTNID</span><span class="topo-unknown">D</span><span class="topo-outside">SNQKNFVKRYASAASDVDAQINRVLNALREAGKFDNTVVIITAGRGIPLTPEENRFDWSQGHLQVPLVIHWPGT</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590  </span>
<span class="topo-line"><span class="topo-outside">PAQRINVLTDHTDVMTTLMQRLLHVSTPANEYSQGQDIFTVPRRHNWVTAADGSTLAITTPQMTLVLNNNGHYQTYDLHGEKIKDQ</span><span class="topo-unknown">K</span><span class="topo-outside">PQLSLLLQVLTEEKRFIAN</span><span class="topo-unknown">HHHHHH</span></span>
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
      <td>7</td>
      <td>16</td>
      <td>7</td>
      <td>16</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>17</td>
      <td>35</td>
      <td>17</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>54</td>
      <td>36</td>
      <td>54</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>80</td>
      <td>55</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>85</td>
      <td>81</td>
      <td>85</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>102</td>
      <td>86</td>
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
      <td>125</td>
      <td>117</td>
      <td>125</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>126</td>
      <td>126</td>
      <td>126</td>
      <td>126</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>138</td>
      <td>132</td>
      <td>138</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>156</td>
      <td>139</td>
      <td>156</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>157</td>
      <td>163</td>
      <td>157</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>168</td>
      <td>168</td>
      <td>168</td>
      <td>168</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>169</td>
      <td>186</td>
      <td>169</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>187</td>
      <td>196</td>
      <td>187</td>
      <td>196</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>197</td>
      <td>202</td>
      <td>197</td>
      <td>202</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>203</td>
      <td>214</td>
      <td>203</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>220</td>
      <td>215</td>
      <td>220</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>221</td>
      <td>405</td>
      <td>221</td>
      <td>405</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>566</td>
      <td>407</td>
      <td>566</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>568</td>
      <td>586</td>
      <td>568</td>
      <td>586</td>
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

### PbgA is an LPS sensor, not a cardiolipin transporter

The full-length [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) structure at 2.0 A definitively refutes the earlier model that [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) functions as a [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) transporter. The periplasmic domain remains firmly anchored onto the TMD (~2,550 A2 interdomain contacts) and protrudes only ~60 A above the inner membrane — far short of the ~200 A periplasmic width. The IFD is a compact three-helix bundle, not a simple linker. [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) shows no structural homology to any known transporter. No [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) density was observed in the structure; instead, LPS ([Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/)) was bound.

### Lipid A-binding (LAB) motif on the periplasmic leaflet

[PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) binds LPS selectively through a backbone-mediated coordination scheme at the periplasmic leaflet of the inner membrane. A single phospho-GlcNAc unit of [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) is recognized, distinguishing [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) from other LPS receptors that bind the [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) disaccharide. The binding does not require divalent cations or basic residues. Key residues include R215 which stabilizes the IFD-TMD interface.

### PbgA-LapB complex regulates LpxC stability via FtsH

[PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) constitutively associates with LapB at its TMD. Together they antagonize FtsH-mediated degradation of LpxC when LPS demand is high (e.g., during cell growth). When periplasmic LPS accumulates, LPS binds to [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/), altering the PbgA-LapB interaction and promoting FtsH-dependent degradation of LpxC. This rheostat mechanism coordinates LPS synthesis with demand, maintaining outer membrane integrity. Deletion of [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) leads to growth inhibition, loss of cell shape, membrane bursting, and attenuation of virulence.

### PbgA-derived LAB peptides as broad-spectrum antibiotics

Synthetic peptides derived from the [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) lipid A-binding motif (LAB peptides) selectively bind LPS over phospholipids. Structure-guided optimization produced LABv2.1 with MICs of 12.5-200 uM against clinically relevant Gram-negative pathogens including E. coli, K. pneumoniae, A. baumannii, and P. aeruginosa, including polymyxin-resistant strains. These peptides represent a novel class of LPS-targeting antibiotics.

### PbgA structure resembles hydrolase superfamily

The [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) periplasmic domain is structurally related to a superfamily of cell envelope-modifying enzymes including LtaS (S. aureus lipoteichoic acid synthase) and EptA/MCR-1 (phosphoethanolamine transferases). [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) retains the fold but lacks catalytic residues (pseudo-hydrolase). The IFD aligns with the EptA linker but is reoriented ~180 degrees.

### PbgA co-purifies with LPS but not cardiolipin

Purified full-length [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/) specifically co-purifies with various [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) species (tetra-, hexa-acylated, and arabinose-modified forms) as shown by MALDI-TOF mass spectrometry and limulus amebocyte lysate assays. No [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) was detected bound to [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA-yejM/). In contrast, [LNT](/xray-mp-wiki/proteins/enzymes/lnt/) (a control inner membrane protein) did not co-purify with LPS. PbgA-LPS binding was observed in two crystal forms and supported by molecular dynamics simulations.


## Cross-References

- <a href="/xray-mp-wiki/concepts/membrane-mimetics/selective-lipid-binding/">Selective Lipid Binding</a> — PbgA selectively binds lipid A (LPS) through a backbone-mediated scheme recognizing a single phospho-GlcNAc unit
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/">Membrane Mimetics</a> — PbgA structure was determined in LCP (lipidic cubic phase), a membrane-mimetic system
- <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/">Serial Femtosecond Crystallography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/enzymes/lnt/">LNT</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/enzymes/pbgA-yejM/">PbgA (YejM) Cardiolipin Transport Protein</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/ligands/ethidium/">Ethidium - Fluorescent Intercalating Dye</a> — Related ligand or cofactor
- <a href="/xray-mp-wiki/reagents/ligands/l-methionine/">L-Methionine</a> — Related ligand or cofactor
