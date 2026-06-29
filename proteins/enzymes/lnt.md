---
title: "Apolipoprotein N-acyltransferase (Lnt) from Escherichia coli"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##s41598-020-57419-7]
verified: false
---

# Apolipoprotein N-acyltransferase (Lnt) from Escherichia coli

## Overview

Apolipoprotein N-acyltransferase (Lnt) is an integral membrane enzyme that catalyzes the final step of lipoprotein maturation in Gram-negative bacteria — the N-acylation of the N-terminal cysteine of apolipoproteins. Lnt belongs to the [Nitrilase Superfamily](/xray-mp-wiki/concepts/protein-families/nitrilase-superfamily/) and employs a Glu-Lys-Cys catalytic triad (E267-K335-C387 in E. coli) to perform a two-step ping-pong mechanism. The first step involves acyl transfer from a phospholipid substrate to the active site cysteine, forming a thioester acyl-intermediate. The second step transfers the acyl chain from this cysteine to the N-terminal cysteine of the incoming apolipoprotein. This work reports two crystal forms of E. coli Lnt that capture the thioester acyl-intermediate and reveal conformational dynamics of a flexible arm (residues 345-365) that may regulate active site access.


## Publications

### doi/10.1038##s41598-020-57419-7

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6nwr">6NWR</a></td>
      <td>3.5</td>
      <td>P2_12_12_1</td>
      <td>Full-length with C-terminal 15-aa tail including <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">Polyhistidine Tag (His6)</a> (Lnt-C1)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6q3a">6Q3A</a></td>
      <td>3.01</td>
      <td>P6_422</td>
      <td>Full-length with N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">Polyhistidine Tag (His6)</a> removed by TEV cleavage (Lnt-C2)</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli (DH5α genomic DNA)
- **Construct**: Full-length Lnt with C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (Lnt-C1) or N-terminal TEV-cleavable [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (Lnt-C2)

**Purification:**

- **Expression system**: E. coli K12 DH5α
- **Expression construct**: Full-length Lnt with C-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (Lnt-C1) or N-terminal TEV-cleavable [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (Lnt-C2)
- **Tag info**: [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/) (C-terminal for Lnt-C1; N-terminal TEV-cleavable for Lnt-C2)

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
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA</td>
      <td>—</td>
      <td></td>
      <td>Purification via <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">Polyhistidine Tag (His6)</a></td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td>TEV protease cleavage</td>
      <td>—</td>
      <td></td>
      <td>Lnt-C2 only — TEV cleavage removed N-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">Polyhistidine Tag (His6)</a></td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified Lnt in crystallization buffer

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Lnt-C1 with C-terminal <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">Polyhistidine Tag (His6)</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>~2 weeks</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew in P2_12_12_1 space group with 2 molecules in asymmetric unit. Loop-harvested and snap-cooled in liquid nitrogen without additional cryoprotectant.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Lnt-C2 (TEV-cleaved, 15 mg/mL)</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (9.9 <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a>)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>18</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>~6 weeks</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Initial trials at 18°C, optimized at 10°C for 3 weeks then 4°C for 3 weeks. Crystals in P6_422 space group. Loop-harvested and snap-frozen without cryoprotectant.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6nwr">6NWR</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MAFASLI</span><span class="topo-inside">ERQRI</span><span class="topo-membrane">RLLLALLFGACGT</span><span class="topo-outside">LAFSPYDVW</span><span class="topo-membrane">PAAIISLMGLQALT</span><span class="topo-inside">FNRRPLQS</span><span class="topo-membrane">AAIG</span></span>
<span class="topo-line"><span class="topo-membrane">FCWGFGLFGS</span><span class="topo-outside">GINWVYVSIATFGGMPG</span><span class="topo-unknown">PVNIFLVV</span><span class="topo-membrane">LLAAYLSLYTGLFAGVL</span><span class="topo-inside">SRLWPKTT</span></span>
<span class="topo-line"><span class="topo-inside">W</span><span class="topo-membrane">LRVAIAAPALWQVTEFLRGWVL</span><span class="topo-outside">TGFPWLQFGYSQIDGPLK</span><span class="topo-unknown">GLAPIM</span><span class="topo-outside">GVE</span><span class="topo-membrane">AINFLLMMVS</span></span>
<span class="topo-line"><span class="topo-membrane">GLLALAL</span><span class="topo-inside">VKRNW</span><span class="topo-membrane">RPLVVAVVLFALP</span><span class="topo-outside">FPLRYIQWFTPQPEKTIQVSMVQGDIPQSLKWDEG</span></span>
<span class="topo-line"><span class="topo-outside">QLLNTLKIYYNATAPLMGKSSLIIWPESAITDLEINQQPFLKALDGELRDKGSSLVTGIV</span></span>
<span class="topo-line"><span class="topo-outside">DARLNKQNRYDTYNTIITLGKGAPYSYESADRYNKNHLVPFGEFVPLESIL</span><span class="topo-unknown">RPLAPFFDL</span></span>
<span class="topo-line"><span class="topo-unknown">PM</span><span class="topo-outside">SSFSRGPYIQPPLSANGIELTAAICYEIILGEQVRDNFRPDTDYLLTISNDAWFGKSI</span></span>
<span class="topo-line"><span class="topo-outside">GPWQHFQMARMRALELARPLLRSTNNGITAVIGPQGEIQAMIPQFTREVLTTNVTPTTGL</span></span>
<span class="topo-line"><span class="topo-outside">TPYARTGNW</span><span class="topo-membrane">PLWVLTALFGFAAV</span><span class="topo-inside">LMS</span><span class="topo-unknown">LRQRRKEFRVPGSHHHHHHHH</span></span>
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
      <td>8</td>
      <td>12</td>
      <td>8</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>25</td>
      <td>13</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>34</td>
      <td>26</td>
      <td>34</td>
      <td>Outside</td>
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
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>70</td>
      <td>57</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>87</td>
      <td>71</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>95</td>
      <td>88</td>
      <td>95</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>96</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>121</td>
      <td>113</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>143</td>
      <td>122</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>161</td>
      <td>144</td>
      <td>161</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>167</td>
      <td>162</td>
      <td>167</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>168</td>
      <td>170</td>
      <td>168</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>171</td>
      <td>187</td>
      <td>171</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>188</td>
      <td>192</td>
      <td>188</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>205</td>
      <td>193</td>
      <td>205</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>351</td>
      <td>206</td>
      <td>351</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>363</td>
      <td>489</td>
      <td>363</td>
      <td>489</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>490</td>
      <td>503</td>
      <td>490</td>
      <td>503</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>504</td>
      <td>506</td>
      <td>504</td>
      <td>506</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6q3a">6Q3A</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">GHMAFASL</span><span class="topo-inside">IERQR</span><span class="topo-membrane">IRLLLALLFGACGTLAF</span><span class="topo-outside">SPY</span><span class="topo-membrane">DVWPAAIISLMGLQALT</span><span class="topo-inside">FNRRPL</span><span class="topo-membrane">QSAA</span></span>
<span class="topo-line"><span class="topo-membrane">IGFCWGFGLFGSGIN</span><span class="topo-outside">WVYVSIATFGGMPG</span><span class="topo-membrane">PVNIFLVVLLAAYLSLYTGLFAGVLS</span><span class="topo-inside">RLWPK</span></span>
<span class="topo-line"><span class="topo-inside">TTW</span><span class="topo-membrane">LRVAIAAPALWQVTEFLRGWVLTGF</span><span class="topo-outside">PWLQFGYSQIDGPLKGLAPI</span><span class="topo-membrane">MGVEAINFLLMM</span></span>
<span class="topo-line"><span class="topo-membrane">VSGLLALAL</span><span class="topo-inside">VKRNW</span><span class="topo-membrane">RPLVVAVVLFALPFPL</span><span class="topo-outside">RYIQWFTPQPEKTIQVSMVQGDIPQSLKWD</span></span>
<span class="topo-line"><span class="topo-outside">EGQLLNTLKIYYNATAPLMGKSSLIIWPESAITDLEINQQPFLKALDGELRDKGSSLVTG</span></span>
<span class="topo-line"><span class="topo-outside">IVDARLNKQNRYDTYNTIITLGKGAPYSYESADRYNKNHLVPFGEFVPLESIL</span><span class="topo-unknown">RPLAPFF</span></span>
<span class="topo-line"><span class="topo-unknown">DLPM</span><span class="topo-outside">SSFSRGPYIQPPLSANGIELTAAICYEIILGEQVRDNFRPDTDYLLTISNDAWFGK</span></span>
<span class="topo-line"><span class="topo-outside">SI</span><span class="topo-unknown">GPWQHFQMARMRALEL</span><span class="topo-outside">ARPLLRSTNNGITAVIGPQGEIQAMIPQFTREVLTTNVTPTT</span></span>
<span class="topo-line"><span class="topo-outside">GLTPYARTGN</span><span class="topo-membrane">WPLWVLTALFGFAAVL</span><span class="topo-inside">MSLRQ</span><span class="topo-unknown">RRK</span></span>
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
      <td>9</td>
      <td>13</td>
      <td>7</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>30</td>
      <td>12</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>33</td>
      <td>29</td>
      <td>31</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>50</td>
      <td>32</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>56</td>
      <td>49</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>75</td>
      <td>55</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>89</td>
      <td>74</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>115</td>
      <td>88</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>123</td>
      <td>114</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>148</td>
      <td>122</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>149</td>
      <td>168</td>
      <td>147</td>
      <td>166</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>169</td>
      <td>189</td>
      <td>167</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>190</td>
      <td>194</td>
      <td>188</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>210</td>
      <td>193</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>211</td>
      <td>353</td>
      <td>209</td>
      <td>351</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>365</td>
      <td>422</td>
      <td>363</td>
      <td>420</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>423</td>
      <td>438</td>
      <td>421</td>
      <td>436</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>439</td>
      <td>490</td>
      <td>437</td>
      <td>488</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>491</td>
      <td>506</td>
      <td>489</td>
      <td>504</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>507</td>
      <td>511</td>
      <td>505</td>
      <td>509</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Thioester acyl-intermediate captured in Lnt-C1 chain B

Extra electron density extending off the active site C387 in chain B of Lnt-C1 is consistent with a palmitoyl thioester acyl-intermediate, confirmed by mass spectrometry. The acyl tail curves upward above the predicted membrane interface and fits into a hydrophobic binding groove. No large-scale active site rearrangements are required to accommodate the modification.

### Conformational dynamics of the flexible 345-365 arm

The long 345-365 arm displays remarkable flexibility. In Lnt-C1 chain B it extends at a ~60° upward angle above the membrane, likely acting as a protective lid over the active site during the reactive thioester state. In chain A and Lnt-C2, the arm lies parallel to the membrane, creating an open, accessible active site cavity. This arm may regulate access to the active site and protect the thioester intermediate from unwanted hydrolysis.

### W237 movement mediates substrate binding

W237, located at the entry of the large substrate-binding cavity, adopts two alternate conformations across available Lnt structures: an upward position coordinated with T271 (pointing away from the portal), and a downward position pointing into the portal where it can interact with substrates. This movement (~8.5 Å) appears to be triggered by substrate binding and may help stabilize incoming apolipoproteins for the second catalytic step.

### Proposed window mechanism for substrate selectivity

When the 345-365 arm is above the membrane and W237 is in the downward position, a restricted window is formed at the narrowest part of the cavity involving E343, W415, W237, and P346. This may selectively allow only the N-terminus of apolipoproteins to access the reactive thioester state, providing substrate selectivity at the second catalytic step.


## Cross-References

- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Used in LCP crystallization reservoir at 100 mM pH 7.2
- <a href="/xray-mp-wiki/reagents/additives/peg200/">PEG200</a> — Used as precipitant in LCP crystallization at 36%
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid used for LCP crystallization of Lnt-C2
- <a href="/xray-mp-wiki/reagents/buffers/ammonium-phosphate/">Ammonium Phosphate</a> — Used at 400 mM in LCP crystallization reservoir
- <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His6-tag</a> — Used for affinity purification of both Lnt constructs
- <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> — Used to remove N-terminal His6-tag from Lnt-C2
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase</a> — Crystallization method used for Lnt-C2
- <a href="/xray-mp-wiki/concepts/protein-families/nitrilase-superfamily/">Nitrilase Superfamily</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/lipids/mag/">MAG</a> — Additive used in purification or crystallization buffers
