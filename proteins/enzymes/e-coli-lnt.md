---
title: "Escherichia coli Apolipoprotein N-Acyl Transferase (Lnt)"
created: 2026-06-03
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms15948, doi/10.1038##ncomms15952, doi/10.1126##sciadv.adf5799]
verified: false
---

# Escherichia coli Apolipoprotein N-Acyl Transferase (Lnt)

## Overview

Apolipoprotein N-acyl transferase (Lnt) from Escherichia coli is a 512-residue integral membrane enzyme (57 kDa) that catalyses the third and final step of lipoprotein biogenesis in Gram-negative bacteria. Lnt transfers an acyl chain from the sn-1 position of a phospholipid donor (e.g. [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol)) to the alpha-amine group of the N-terminal cysteine residue of an apolipoprotein, completing the formation of a mature triacylated lipoprotein. Lnt belongs to the ninth branch of the nitrilase superfamily and contains a catalytic triad of E267-K335-C387. The enzyme consists of an eight-helix transmembrane (TM) domain fused to a periplasmic nitrilase (Nit) catalytic domain. A lid loop from the Nit domain interacts with the lipid bilayer, forming an interfacial entrance from the membrane to the catalytic centre.


## Publications

### doi/10.1038##ncomms15948

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5xhq">5XHQ</a></td>
      <td>2.6</td>
      <td>P212121</td>
      <td>Full-length E. coli Lnt (512 residues)</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43(DE3) / C41(DE3)
- **Construct**: Full-length lnt gene (GenBank ID: 946201 for E. coli; synthetic gene for P. aeruginosa) cloned into pET28a vector. N-terminal thrombin-cleavable His-tag for purification.

- **Induction**: 0.5 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg), 20 h at 20 C post-induction

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
      <td>Cell lysis</td>
      <td>High-pressure homogenization</td>
      <td>--</td>
      <td>50 mM HEPES pH 7.5, 100 mM NaCl, 10% glycerol, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>, 1 mM PMSF + --</td>
      <td>Cells centrifuged at 18,000g for 20 min to remove debris</td>
    </tr>
    <tr>
      <td>Membrane fraction collection</td>
      <td>Ultracentrifugation</td>
      <td>--</td>
      <td>Lysis buffer + --</td>
      <td>Supernatant centrifuged at 100,000g for 1 h; membrane pellet collected</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>Lysis buffer + 2% <a href="/xray-mp-wiki/reagents/detergents/dm">n-decyl-beta-D-maltopyranoside</a></td>
      <td>Membrane pellet dissolved in buffer with 2% <a href="/xray-mp-wiki/reagents/detergents/dm">n-decyl-beta-D-maltopyranoside</a> at 4 C for 1 h</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td>Ni-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a></td>
      <td>Lysis buffer with 2% <a href="/xray-mp-wiki/reagents/detergents/dm">n-decyl-beta-D-maltopyranoside</a> + 2% <a href="/xray-mp-wiki/reagents/detergents/dm">n-decyl-beta-D-maltopyranoside</a></td>
      <td>Tagged proteins in supernatant purified by Ni-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>12 mg/ml E. coli Lnt in 50 mM HEPES pH 7.5, 100 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>, 2% <a href="/xray-mp-wiki/reagents/detergents/dm">n-decyl-beta-D-maltopyranoside</a>
</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>30% PEG 400, 0.2 M sodium <a href="/xray-mp-wiki/reagents/buffers/acetate">Acetate Buffer (Sodium Acetate)</a> pH 4.6
</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified in paper</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals cryoprotected and flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Native data collected at BL17U at SSRF (wavelength 0.9793 A). Se-Met <a href="/xray-mp-wiki/methods/phasing/single-anomalous-dispersion">SAD</a> data collected at BL1A at KEK (wavelength 0.9791 A). Space group P212121. Resolution 50-2.59 A. R_work/R_free: 23.2/28.9%.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5xhq">5XHQ</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MAFASLIE</span><span class="topo-inside">RQR</span><span class="topo-membrane">IRLLLALLFGACGT</span><span class="topo-outside">LAFSPYDVWP</span><span class="topo-membrane">AAIISLMGLQALT</span><span class="topo-inside">FNRRPL</span><span class="topo-membrane">QSAAIG</span></span>
<span class="topo-line"><span class="topo-membrane">FGWGFGLFGS</span><span class="topo-outside">GINWVYVSIATFGGMPG</span><span class="topo-unknown">PVNIFLVV</span><span class="topo-membrane">LLAAYLSLYTGLFAGVLS</span><span class="topo-inside">RLWPKTT</span></span>
<span class="topo-line"><span class="topo-inside">W</span><span class="topo-membrane">LRVAIAAPALWQVTEFLR</span><span class="topo-outside">GWVLTGFPWLQFGYSQIDGPLK</span><span class="topo-unknown">GLAPIM</span><span class="topo-outside">GVE</span><span class="topo-membrane">AINFLLMMVS</span></span>
<span class="topo-line"><span class="topo-membrane">GLLALAL</span><span class="topo-inside">VKRNW</span><span class="topo-membrane">RPLVVAVVLFALPF</span><span class="topo-outside">PLRYIQWFTPQPEKTIQVSMVQGDIPQSLKWDEG</span></span>
<span class="topo-line"><span class="topo-outside">QLLNTLKIYYNATAPLMGKSSLIIWPESAITDLEINQQPFLKVLDGELRDKGSSLVTGIV</span></span>
<span class="topo-line"><span class="topo-outside">DARL</span><span class="topo-unknown">NKQNR</span><span class="topo-outside">YDTYNTIITLGKGAPYSYESADRYNKNHLVPFGEFVPLESILRPLAPF</span><span class="topo-unknown">FDL</span></span>
<span class="topo-line"><span class="topo-outside">PMSSFSRGPYIQPPLSVNGIELTAAICYEIILGEQVRDNFRPDTDYLLTISNDAWFGKSI</span></span>
<span class="topo-line"><span class="topo-outside">GPWQHFQMARMRALELARPLLRSTNNGITAVIGPQGEIQAMIPQFTREVLTTNVTPTTGL</span></span>
<span class="topo-line"><span class="topo-outside">TPYARTGNW</span><span class="topo-membrane">PLWVLTALFGFAAV</span><span class="topo-inside">L</span><span class="topo-unknown">MSLRGSSGSSGG</span></span>
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
      <td>11</td>
      <td>9</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>25</td>
      <td>12</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>35</td>
      <td>26</td>
      <td>35</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>48</td>
      <td>36</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>54</td>
      <td>49</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>70</td>
      <td>55</td>
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
      <td>113</td>
      <td>96</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>121</td>
      <td>114</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>139</td>
      <td>122</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>161</td>
      <td>140</td>
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
      <td>206</td>
      <td>193</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>304</td>
      <td>207</td>
      <td>304</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>310</td>
      <td>357</td>
      <td>310</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>361</td>
      <td>489</td>
      <td>361</td>
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
      <td>504</td>
      <td>504</td>
      <td>504</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1038##ncomms15952

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5n6h">5N6H</a></td>
      <td>2.9</td>
      <td>P212121</td>
      <td>Full-length E. coli Lnt (512 residues), N-terminal thrombin-cleavable His-tag</td>
      <td>none (apo)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5n6l">5N6L</a></td>
      <td>2.9</td>
      <td>P212121</td>
      <td>Full-length E. coli Lnt C387A mutant (512 residues), N-terminal thrombin-cleavable His-tag</td>
      <td>monoolein (structured lipids in active site portal)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5n6m">5N6M</a></td>
      <td>3.1</td>
      <td>C2</td>
      <td>Full-length P. aeruginosa Lnt (514 residues), N-terminal thrombin-cleavable His-tag</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43(DE3) / C41(DE3)
- **Construct**: Full-length lnt gene (GenBank ID: 946201 for E. coli; synthetic gene for P. aeruginosa) cloned into pET28a vector. N-terminal thrombin-cleavable His-tag for purification.

- **Induction**: 0.5 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg), 20 h at 20 C post-induction

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
      <td>Cell lysis</td>
      <td>High-pressure homogenization (Emulsiflex-CS)</td>
      <td>--</td>
      <td>20 mM Tris-HCl pH 8.0, 50 mM NaCl, 0.5 mM EDTA, 1 mM PMSF + --</td>
      <td>Cells lysed at 1000-1750 bar at 4 C</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Ultracentrifugation</td>
      <td>--</td>
      <td>20 mM Tris-HCl pH 8.0, 50 mM NaCl, 0.5 mM EDTA, 1 mM PMSF + --</td>
      <td>Membranes pelleted at 120,000g for 2 h at 4 C</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization (dodecyl-beta-D-maltoside, <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>)</td>
      <td>--</td>
      <td>20 mM Tris-HCl pH 8.0, 50 mM NaCl, 0.5 mM EDTA, 1 mM PMSF + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm">n-dodecyl-beta-D-maltopyranoside</a> (<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>)</td>
      <td>membranes solubilized by stirring for 2 h at 4 C; insoluble material removed by centrifugation at 120,000g</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a> affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA agarose</a></td>
      <td>20 mM Tris-HCl pH 8.0, 300 mM NaCl, 20 mM imidazole, 0.5 mM EDTA, 0.3% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> + 0.3% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Protein eluted with 300 mM imidazole in same buffer</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/resins/superdex-200">Superdex 200</a> 10/300 GL</td>
      <td>20 mM Tris-HCl pH 8.0, 50 mM NaCl, 0.5 mM EDTA, 0.3% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> + 0.3% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Peak fractions concentrated to 5-10 mg/ml for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic Cubic Phase</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Lnt in 20 mM Tris-HCl pH 8.0, 50 mM NaCl, 0.5 mM EDTA, 0.3% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, reconstituted into monoolein (9.9 MAG) cubic mesophase (2:3 v/v protein:lipid)
</td>
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
      <td>Cryoprotection</td>
      <td>Crystals harvested from LCP and snap-cooled in liquid nitrogen without added cryoprotectant</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected at Swiss Light Source (X06SA-PXI, X10SA-PXII). SeMet <a href="/xray-mp-wiki/methods/phasing/single-anomalous-dispersion">SAD</a> at 0.9792 A for phasing. LntEco and LntEcoC387A in P212121; LntPae in C2.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5n6h">5N6H</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMAFAS</span><span class="topo-inside">LIERQR</span><span class="topo-membrane">IRLLLALLFGACGTLAF</span><span class="topo-outside">SPY</span><span class="topo-membrane">DVWPAAIIS</span></span>
<span class="topo-line"><span class="topo-membrane">LMGLQALTF</span><span class="topo-inside">NRRP</span><span class="topo-membrane">LQSAAIGFCWGFGLFGSGIN</span><span class="topo-outside">WVYVSIATFGGMPGP</span><span class="topo-membrane">VNIFLVVLLAAY</span></span>
<span class="topo-line"><span class="topo-membrane">LSLYTGLFAGVLS</span><span class="topo-inside">RLWPKTTW</span><span class="topo-membrane">LRVAIAAPALWQVTEFLRGWVLTGF</span><span class="topo-outside">PWLQFGYSQIDGPL</span></span>
<span class="topo-line"><span class="topo-unknown">KGLAPI</span><span class="topo-membrane">MGVEAINFLLMMVSGLLALALV</span><span class="topo-inside">KRNW</span><span class="topo-membrane">RPLVVAVVLFALPFPL</span><span class="topo-outside">RYIQWFTPQPEK</span></span>
<span class="topo-line"><span class="topo-outside">TIQVSMVQGDIPQSLKWDEGQLLNTLKIYYNATAPLMGKSSLIIWPESAITDLEINQQPF</span></span>
<span class="topo-line"><span class="topo-outside">LKALDGELRDKGSSLVTGIVDARLNKQNRYDTYNTIITLGKGAPYSYESADRYNKNHLVP</span></span>
<span class="topo-line"><span class="topo-outside">FGEFVPLESILRPLAPFFDLPMSSFSRGPYIQPPLSANGIELTAAICYEIILGEQVRDNF</span></span>
<span class="topo-line"><span class="topo-outside">RPDTDYLLTISNDAWFGKSI</span><span class="topo-unknown">GPWQHFQMARMRALEL</span><span class="topo-outside">ARPLLRSTNNGITAVIGPQGEIQA</span></span>
<span class="topo-line"><span class="topo-outside">MIPQFTREVLTTNVTPTTGLTPYART</span><span class="topo-membrane">GNWPLWVLTALFGFAAVL</span><span class="topo-inside">MSLR</span><span class="topo-unknown">QRRK</span></span>
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
      <td>31</td>
      <td>6</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>48</td>
      <td>12</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>51</td>
      <td>29</td>
      <td>31</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>69</td>
      <td>32</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>73</td>
      <td>50</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>93</td>
      <td>54</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>108</td>
      <td>74</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>109</td>
      <td>133</td>
      <td>89</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>141</td>
      <td>114</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>166</td>
      <td>122</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>167</td>
      <td>180</td>
      <td>147</td>
      <td>160</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>186</td>
      <td>161</td>
      <td>166</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>187</td>
      <td>208</td>
      <td>167</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>212</td>
      <td>189</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>228</td>
      <td>193</td>
      <td>208</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>229</td>
      <td>440</td>
      <td>209</td>
      <td>420</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>456</td>
      <td>421</td>
      <td>436</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>457</td>
      <td>506</td>
      <td>437</td>
      <td>486</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>507</td>
      <td>524</td>
      <td>487</td>
      <td>504</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>525</td>
      <td>528</td>
      <td>505</td>
      <td>508</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5n6l">5N6L</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMA</span><span class="topo-inside">FASLIERQ</span><span class="topo-membrane">RIRLLLALLFGACGTLA</span><span class="topo-outside">FSPYDVW</span><span class="topo-membrane">PAAIIS</span></span>
<span class="topo-line"><span class="topo-membrane">LMGLQALTF</span><span class="topo-inside">NRRP</span><span class="topo-membrane">LQSAAIGFCWGFGLFGS</span><span class="topo-outside">GINWVYVSIATFGGMP</span><span class="topo-unknown">GPVNIFLVV</span><span class="topo-membrane">LLAAY</span></span>
<span class="topo-line"><span class="topo-membrane">LSLYTGLFAGVLS</span><span class="topo-inside">RLWPKTTW</span><span class="topo-membrane">LRVAIAAPALWQVTEFLRGWV</span><span class="topo-outside">LTGFPWLQFGYSQIDGPL</span></span>
<span class="topo-line"><span class="topo-outside">K</span><span class="topo-unknown">GLAPIM</span><span class="topo-outside">GVE</span><span class="topo-membrane">AINFLLMMVSGLLALALV</span><span class="topo-inside">KRNW</span><span class="topo-membrane">RPLVVAVVLFALPFP</span><span class="topo-outside">LRYIQWFTPQPEK</span></span>
<span class="topo-line"><span class="topo-outside">TIQVSMVQGDIPQSLKWDEGQLLNTLKIYYNATAPLMGKSSLIIWPESAITDLEINQQPF</span></span>
<span class="topo-line"><span class="topo-outside">LKALDGELRDKGSSLVTGIVDARLNKQNRYDTYNTIITLGKGAPYSYESADRYNKNHLVP</span></span>
<span class="topo-line"><span class="topo-outside">FGEFVPLESILRPLAPFFDLPMSSFSRGPYIQPPLSANGIELTAAIAYEIILGEQVRDNF</span></span>
<span class="topo-line"><span class="topo-outside">RPDTDYLLTISNDAWFGKSIGPWQHFQMARMRALELARPLLRSTNNGITAVIGPQGEIQA</span></span>
<span class="topo-line"><span class="topo-outside">MIPQFTREVLTTNVTPTTGLTPYARTGN</span><span class="topo-membrane">WPLWVLTALFGFAAV</span><span class="topo-inside">LMSLR</span><span class="topo-unknown">QRRK</span></span>
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
      <td>23</td>
      <td>30</td>
      <td>3</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>47</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>54</td>
      <td>28</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>69</td>
      <td>35</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>73</td>
      <td>50</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>90</td>
      <td>54</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>106</td>
      <td>71</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>107</td>
      <td>115</td>
      <td>87</td>
      <td>95</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>116</td>
      <td>133</td>
      <td>96</td>
      <td>113</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>141</td>
      <td>114</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>162</td>
      <td>122</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>181</td>
      <td>143</td>
      <td>161</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>187</td>
      <td>162</td>
      <td>167</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>188</td>
      <td>190</td>
      <td>168</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>208</td>
      <td>171</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>212</td>
      <td>189</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>227</td>
      <td>193</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>508</td>
      <td>208</td>
      <td>488</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>509</td>
      <td>523</td>
      <td>489</td>
      <td>503</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>524</td>
      <td>528</td>
      <td>504</td>
      <td>508</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5n6m">5N6M</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMR</span><span class="topo-inside">WISRPG</span><span class="topo-membrane">WPGHLLALAAGALT</span><span class="topo-outside">PLALAPFDYW</span><span class="topo-membrane">PLAILSIA</span></span>
<span class="topo-line"><span class="topo-membrane">LLYLGLR</span><span class="topo-inside">GLPG</span><span class="topo-membrane">KSALWRGWWYGFGAFGA</span><span class="topo-outside">GTSWIYVSIHDYGAAS</span><span class="topo-unknown">VPLASLLML</span><span class="topo-membrane">GFTAGVA</span></span>
<span class="topo-line"><span class="topo-membrane">FFFALPAWLWARCL</span><span class="topo-inside">RRDNAP</span><span class="topo-membrane">LGDALAFAALWLALELFR</span><span class="topo-outside">SWFLTGFPWLYAGYSQLQGPL</span><span class="topo-unknown">A</span></span>
<span class="topo-line"><span class="topo-unknown">GLVPVG</span><span class="topo-outside">GVW</span><span class="topo-membrane">LSSFVIALSAALLVNLP</span><span class="topo-inside">RLFPHGASL</span><span class="topo-membrane">LLGLVLLLGPWAAG</span><span class="topo-outside">LYLKGHAWTHS</span></span>
<span class="topo-line"><span class="topo-outside">AGEPLRVVAIQGNIAQE</span><span class="topo-unknown">LKWD</span><span class="topo-outside">PNQVRAQLDLYRDLSLPQQDVDLIVWPETAVPILQDMAS</span></span>
<span class="topo-line"><span class="topo-outside">GYLGAMGQVADEKNAALITGVPVRERLADGKSRYFNGITVVGEGAGTYLKQKLVPFGEYV</span></span>
<span class="topo-line"><span class="topo-outside">PLQDLLRGLIA</span><span class="topo-unknown">FFDLPM</span><span class="topo-outside">SDFARGPADQPLLKAKGYQIAPYICYEVVYPEFAAALAAQSQV</span></span>
<span class="topo-line"><span class="topo-outside">LLTVSNDTWFGTSIGPLQHLQMAQMRALESGRWMIRATNNGVTGLIDPYGRIVRQIPQFQ</span></span>
<span class="topo-line"><span class="topo-outside">QGILRGEVIPMQGLTPYLQYRV</span><span class="topo-membrane">WPLAGLAGVLLLWAL</span><span class="topo-inside">LGRQLR</span><span class="topo-unknown">PQERRLFG</span></span>
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
      <td>23</td>
      <td>28</td>
      <td>3</td>
      <td>8</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>42</td>
      <td>9</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>52</td>
      <td>23</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>67</td>
      <td>33</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>71</td>
      <td>48</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>88</td>
      <td>52</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>89</td>
      <td>104</td>
      <td>69</td>
      <td>84</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>113</td>
      <td>85</td>
      <td>93</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>114</td>
      <td>134</td>
      <td>94</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>140</td>
      <td>115</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>158</td>
      <td>121</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>159</td>
      <td>179</td>
      <td>139</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>186</td>
      <td>160</td>
      <td>166</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>187</td>
      <td>189</td>
      <td>167</td>
      <td>169</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>206</td>
      <td>170</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>215</td>
      <td>187</td>
      <td>195</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>229</td>
      <td>196</td>
      <td>209</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>257</td>
      <td>210</td>
      <td>237</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>262</td>
      <td>371</td>
      <td>242</td>
      <td>351</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>378</td>
      <td>502</td>
      <td>358</td>
      <td>482</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>503</td>
      <td>517</td>
      <td>483</td>
      <td>497</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>518</td>
      <td>523</td>
      <td>498</td>
      <td>503</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1126##sciadv.adf5799

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8b0k">8B0K</a></td>
      <td>3.0</td>
      <td>—</td>
      <td>Full-length E. coli Lnt WT, HA-treated (deacylated)</td>
      <td>none (apo)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8aq3">8AQ3</a></td>
      <td>2.4</td>
      <td>Not specified</td>
      <td>Full-length E. coli Lnt C387A mutant</td>
      <td>PE (phosphatidylethanolamine)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8b0m">8B0M</a></td>
      <td>3.0</td>
      <td>—</td>
      <td>Full-length E. coli Lnt C387S mutant</td>
      <td>PE</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8b0l">8B0L</a></td>
      <td>3.1</td>
      <td>—</td>
      <td>Full-length E. coli Lnt C387A mutant</td>
      <td>PE</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8b0n">8B0N</a></td>
      <td>2.7</td>
      <td>—</td>
      <td>Full-length E. coli Lnt WT (acyl-Lnt)</td>
      <td>S-acyl chain (palmitate at C387), lyso-PE</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8aq4">8AQ4</a></td>
      <td>2.6</td>
      <td>—</td>
      <td>Full-length E. coli Lnt with TITC modification</td>
      <td>TITC, lyso-PE</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8aq2">8AQ2</a></td>
      <td>2.7</td>
      <td>—</td>
      <td>Full-length P. aeruginosa Lnt with TITC modification</td>
      <td>TITC, monoolein (2 molecules)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8b0p">8B0P</a></td>
      <td>2.9</td>
      <td>—</td>
      <td>Full-length E. coli Lnt C387A mutant</td>
      <td>Pam3CSK4</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8b0o">8B0O</a></td>
      <td>3.0</td>
      <td>—</td>
      <td>Full-length E. coli Lnt C387S mutant</td>
      <td>FP3 (TA-BLPtide product)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43(DE3) / C41(DE3)
- **Construct**: Full-length lnt gene (GenBank ID: 946201 for E. coli; synthetic gene for P. aeruginosa) cloned into pET28a vector. N-terminal thrombin-cleavable His-tag for purification.

- **Induction**: 0.5 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg), 20 h at 20 C post-induction

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8b0k">8B0K</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSH</span><span class="topo-outside">MAFASLIERQR</span><span class="topo-membrane">IRLLLALLFGACGTLA</span><span class="topo-inside">FSPYDV</span><span class="topo-membrane">WPAAIIS</span></span>
<span class="topo-line"><span class="topo-membrane">LMGLQALTF</span><span class="topo-outside">NRRP</span><span class="topo-membrane">LQSAAIGFCWGFGLFGSG</span><span class="topo-inside">INWVYVSIATFGGMPGPVNI</span><span class="topo-membrane">FLVVLLAAY</span></span>
<span class="topo-line"><span class="topo-membrane">LSLYTGLFAGVLSRLW</span><span class="topo-outside">PKTTW</span><span class="topo-membrane">LRVAIAAPALWQVTEFLRGWV</span><span class="topo-inside">LTGFPWLQFGYSQIDGPL</span></span>
<span class="topo-line"><span class="topo-inside">KGLAPIMGVE</span><span class="topo-membrane">AINFLLMMVSGLLALAL</span><span class="topo-outside">VKRNW</span><span class="topo-membrane">RPLVVAVVLFALPF</span><span class="topo-inside">PLRYIQWFTPQPEK</span></span>
<span class="topo-line"><span class="topo-inside">TIQVSMVQGDIPQSLKWDEGQLLNTLKIYYNATAPLMGKSSLIIWPESAITDLEINQQPF</span></span>
<span class="topo-line"><span class="topo-inside">LKALDGELRDKGSSLVTGIVDARLNKQNRYDTYNTIITLGKGAPYSYESADRYNKNHLVP</span></span>
<span class="topo-line"><span class="topo-inside">FGEFVPL</span><span class="topo-unknown">ESILRPLAPFFDLPMS</span><span class="topo-inside">SFSRGPYIQPPLSANGIELTAAICYEIILGEQVRDNF</span></span>
<span class="topo-line"><span class="topo-inside">RPDTDYLLTISNDAWFGKSIGPWQHFQMARMRALELARPLLRSTNNGITAVIGPQGEIQA</span></span>
<span class="topo-line"><span class="topo-inside">MIPQFTREVLTTNVTPTTGLTPYARTGNWP</span><span class="topo-membrane">LWVLTALFGFAAVLM</span><span class="topo-outside">SLR</span><span class="topo-unknown">QRRK</span></span>
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
      <td>20</td>
      <td>-19</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>21</td>
      <td>31</td>
      <td>1</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>47</td>
      <td>12</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>53</td>
      <td>28</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>69</td>
      <td>34</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>73</td>
      <td>50</td>
      <td>53</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>91</td>
      <td>54</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>111</td>
      <td>72</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>112</td>
      <td>136</td>
      <td>92</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>141</td>
      <td>117</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>162</td>
      <td>122</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>190</td>
      <td>143</td>
      <td>170</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>207</td>
      <td>171</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>212</td>
      <td>188</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>226</td>
      <td>193</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>227</td>
      <td>367</td>
      <td>207</td>
      <td>347</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>383</td>
      <td>348</td>
      <td>363</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>384</td>
      <td>510</td>
      <td>364</td>
      <td>490</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>525</td>
      <td>491</td>
      <td>505</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>526</td>
      <td>528</td>
      <td>506</td>
      <td>508</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>529</td>
      <td>532</td>
      <td>509</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8aq3">8AQ3</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSH</span><span class="topo-inside">MAFASLIERQ</span><span class="topo-membrane">RIRLLLALLFGACGTLA</span><span class="topo-outside">FSPYDV</span><span class="topo-membrane">WPAAIIS</span></span>
<span class="topo-line"><span class="topo-membrane">LMGLQALTF</span><span class="topo-inside">NRRP</span><span class="topo-membrane">LQSAAIGFCWGFGLFGS</span><span class="topo-outside">GINWVYVSIATFGGMPGPVNIFLVV</span><span class="topo-membrane">LLAAY</span></span>
<span class="topo-line"><span class="topo-membrane">LSLYTGLFAGVLSRLW</span><span class="topo-inside">PKTTW</span><span class="topo-membrane">LRVAIAAPALWQVTEFLR</span><span class="topo-outside">GWVLTGFPWLQFGYSQIDGPL</span></span>
<span class="topo-line"><span class="topo-outside">KGLAPIMGVE</span><span class="topo-membrane">AINFLLMMVSGLLALAL</span><span class="topo-inside">VKRNW</span><span class="topo-membrane">RPLVVAVVLFALPFP</span><span class="topo-outside">LRYIQWFTPQPEK</span></span>
<span class="topo-line"><span class="topo-outside">TIQVSMVQGDIPQSLKWDEGQLLNTLKIYYNATAPLMGKSSLIIWPESAITDLEINQQPF</span></span>
<span class="topo-line"><span class="topo-outside">LKALDGELRDKGSSLVTGIVDARLNKQNRYDTYNTIITLGKGAPYSYESADRYNKNHLVP</span></span>
<span class="topo-line"><span class="topo-outside">FGEFVPLESILRPLAPFFDLPMSSFSRGPYIQPPLSANGIELTAAIAYEIILGEQVRDNF</span></span>
<span class="topo-line"><span class="topo-outside">RPDTDYLLTISNDAWFGKSIGPWQHFQMARMRALELARPLLRSTNNGITAVIGPQGEIQA</span></span>
<span class="topo-line"><span class="topo-outside">MIPQFTREVLTTNVTPTTGLTPYARTGNW</span><span class="topo-membrane">PLWVLTALFGFAAVL</span><span class="topo-inside">MSLR</span><span class="topo-unknown">QRRK</span></span>
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
      <td>20</td>
      <td>-19</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>21</td>
      <td>30</td>
      <td>1</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>47</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>53</td>
      <td>28</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>69</td>
      <td>34</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>73</td>
      <td>50</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>90</td>
      <td>54</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>115</td>
      <td>71</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>136</td>
      <td>96</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>141</td>
      <td>117</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>159</td>
      <td>122</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>190</td>
      <td>140</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>207</td>
      <td>171</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>212</td>
      <td>188</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>227</td>
      <td>193</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>509</td>
      <td>208</td>
      <td>489</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>524</td>
      <td>490</td>
      <td>504</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>525</td>
      <td>528</td>
      <td>505</td>
      <td>508</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>529</td>
      <td>532</td>
      <td>509</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8b0m">8B0M</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHM</span><span class="topo-outside">AFASLIERQ</span><span class="topo-membrane">RIRLLLALLFGACGTLA</span><span class="topo-inside">FSPYDVW</span><span class="topo-membrane">PAAIIS</span></span>
<span class="topo-line"><span class="topo-membrane">LMGLQALTF</span><span class="topo-outside">NRRP</span><span class="topo-membrane">LQSAAIGFCWGFGLFGS</span><span class="topo-inside">GINWVYVSIATFGGMPGPVNIFLVV</span><span class="topo-membrane">LLAAY</span></span>
<span class="topo-line"><span class="topo-membrane">LSLYTGLFAGVLSRL</span><span class="topo-outside">WPKTTW</span><span class="topo-membrane">LRVAIAAPALWQVTEFLRGWV</span><span class="topo-inside">LTGFPWLQFGYSQIDGPL</span></span>
<span class="topo-line"><span class="topo-inside">KGLAPIMGVE</span><span class="topo-membrane">AINFLLMMVSGLLALALV</span><span class="topo-outside">KRNW</span><span class="topo-membrane">RPLVVAVVLFALPFP</span><span class="topo-inside">LRYIQWFTPQPEK</span></span>
<span class="topo-line"><span class="topo-inside">TIQVSMVQGDIPQSLKWDEGQLLNTLKIYYNATAPLMGKSSLIIWPESAITDLEINQQPF</span></span>
<span class="topo-line"><span class="topo-inside">LKALDGELRDKGSSLVTGIVDARLNKQNRYDTYNTIITLGKGAPYSYESADRYNKNHLVP</span></span>
<span class="topo-line"><span class="topo-inside">FGEFVPLESILRPLAPFFDLPMSSFSRGPYIQPPLSANGIELTAAISYEIILGEQVRDNF</span></span>
<span class="topo-line"><span class="topo-inside">RPDTDYLLTISNDAWFGKSIGPWQHFQMARMRALELARPLLRSTNNGITAVIGPQGEIQA</span></span>
<span class="topo-line"><span class="topo-inside">MIPQFTREVLTTNVTPTTGLTPYARTGN</span><span class="topo-membrane">WPLWVLTALFGFAAV</span><span class="topo-outside">LMSLRQ</span><span class="topo-unknown">RRK</span></span>
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
      <td>21</td>
      <td>-19</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>22</td>
      <td>30</td>
      <td>2</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>47</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>54</td>
      <td>28</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>69</td>
      <td>35</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>73</td>
      <td>50</td>
      <td>53</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>90</td>
      <td>54</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>115</td>
      <td>71</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>135</td>
      <td>96</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>141</td>
      <td>116</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>162</td>
      <td>122</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>190</td>
      <td>143</td>
      <td>170</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>208</td>
      <td>171</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>212</td>
      <td>189</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>227</td>
      <td>193</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>508</td>
      <td>208</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>509</td>
      <td>523</td>
      <td>489</td>
      <td>503</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>524</td>
      <td>529</td>
      <td>504</td>
      <td>509</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>530</td>
      <td>532</td>
      <td>510</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8b0l">8B0L</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSH</span><span class="topo-outside">MAFASLIERQ</span><span class="topo-membrane">RIRLLLALLFGACGTLA</span><span class="topo-inside">FSPYDV</span><span class="topo-membrane">WPAAIIS</span></span>
<span class="topo-line"><span class="topo-membrane">LMGLQALTF</span><span class="topo-outside">NRRP</span><span class="topo-membrane">LQSAAIGFCWGFGLFGS</span><span class="topo-inside">GINWVYVSIATFGGMPGPVNIFLVV</span><span class="topo-membrane">LLAAY</span></span>
<span class="topo-line"><span class="topo-membrane">LSLYTGLFAGVLSRLW</span><span class="topo-outside">PKTTW</span><span class="topo-membrane">LRVAIAAPALWQVTEFLR</span><span class="topo-inside">GWVLTGFPWLQFGYSQIDGPL</span></span>
<span class="topo-line"><span class="topo-inside">KGLAPIMGVE</span><span class="topo-membrane">AINFLLMMVSGLLALALV</span><span class="topo-outside">KRNW</span><span class="topo-membrane">RPLVVAVVLFALPFP</span><span class="topo-inside">LRYIQWFTPQPEK</span></span>
<span class="topo-line"><span class="topo-inside">TIQVSMVQGDIPQSLKWDEGQLLNTLKIYYNATAPLMGKSSLIIWPESAITDLEINQQPF</span></span>
<span class="topo-line"><span class="topo-inside">LKALDGELRDKGSSLVTGIVDARLNKQNRYDTYNTIITLGKGAPYSYESADRYNKNHLVP</span></span>
<span class="topo-line"><span class="topo-inside">FGEFVPLESILRPLAPFFDLPMSSFSRGPYIQPPLSANGIELTAAIAYEIILGEQVRDNF</span></span>
<span class="topo-line"><span class="topo-inside">RPDTDYLLTISNDAWFGKSIGPWQHFQMARMRALELARPLLRSTNNGITAVIGPQGEIQA</span></span>
<span class="topo-line"><span class="topo-inside">MIPQFTREVLTTNVTPTTGLTPYARTGNW</span><span class="topo-membrane">PLWVLTALFGFAAVL</span><span class="topo-outside">MSLRQR</span><span class="topo-unknown">RK</span></span>
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
      <td>20</td>
      <td>-19</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>21</td>
      <td>30</td>
      <td>1</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>47</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>53</td>
      <td>28</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>69</td>
      <td>34</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>73</td>
      <td>50</td>
      <td>53</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>90</td>
      <td>54</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>115</td>
      <td>71</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>136</td>
      <td>96</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>141</td>
      <td>117</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>159</td>
      <td>122</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>190</td>
      <td>140</td>
      <td>170</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>208</td>
      <td>171</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>212</td>
      <td>189</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>227</td>
      <td>193</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>509</td>
      <td>208</td>
      <td>489</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>524</td>
      <td>490</td>
      <td>504</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>525</td>
      <td>530</td>
      <td>505</td>
      <td>510</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>531</td>
      <td>532</td>
      <td>511</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8b0n">8B0N</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSH</span><span class="topo-outside">MAFASLIERQRIR</span><span class="topo-membrane">LLLALLFGACGTLAF</span><span class="topo-inside">SPYDV</span><span class="topo-membrane">WPAAIIS</span></span>
<span class="topo-line"><span class="topo-membrane">LMGLQALT</span><span class="topo-outside">FNRRPLQS</span><span class="topo-membrane">AAIGFCWGFGLFGSGIN</span><span class="topo-inside">WVYVSIATFGGMPG</span><span class="topo-membrane">PVNIFLVVLLAAY</span></span>
<span class="topo-line"><span class="topo-membrane">LSLYTGLFAGVLSRLW</span><span class="topo-outside">PKTTW</span><span class="topo-membrane">LRVAIAAPALWQVTEFLRGWVL</span><span class="topo-inside">TGFPWLQFGYSQIDGPL</span></span>
<span class="topo-line"><span class="topo-inside">KGLAPIMGVE</span><span class="topo-membrane">AINFLLMMVSGLLALAL</span><span class="topo-outside">VKRNW</span><span class="topo-membrane">RPLVVAVVLFALPF</span><span class="topo-inside">PLRYIQWFTPQPEK</span></span>
<span class="topo-line"><span class="topo-inside">TIQVSMVQGDIPQSLKWDEGQLLNTLKIYYNATAPLMGKSSLIIWPESAITDLEINQQPF</span></span>
<span class="topo-line"><span class="topo-inside">LKALDGELRDKGSSLVTGIVDARLNKQNRYDTYNTIITLGKGAPYSYESADRYNKNHLVP</span></span>
<span class="topo-line"><span class="topo-inside">FGEFVPLESILRPLAPFFDLPMSSFSRGPYIQPPLSANGIELTAAICYEIILGEQVRDNF</span></span>
<span class="topo-line"><span class="topo-inside">RPDTDYLLTISNDAWFGKSIGPWQHFQMARMRALELARPLLRSTNNGITAVIGPQGEIQA</span></span>
<span class="topo-line"><span class="topo-inside">MIPQFTREVLTTNVTPTTGLTPYARTGNWP</span><span class="topo-membrane">LWVLTALFGFAAVLMS</span><span class="topo-outside">LRQR</span><span class="topo-unknown">RK</span></span>
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
      <td>20</td>
      <td>-19</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>21</td>
      <td>33</td>
      <td>1</td>
      <td>13</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>48</td>
      <td>14</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>53</td>
      <td>29</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>68</td>
      <td>34</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>76</td>
      <td>49</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>93</td>
      <td>57</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>107</td>
      <td>74</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>108</td>
      <td>136</td>
      <td>88</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>141</td>
      <td>117</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>163</td>
      <td>122</td>
      <td>143</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>164</td>
      <td>190</td>
      <td>144</td>
      <td>170</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>207</td>
      <td>171</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>212</td>
      <td>188</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>226</td>
      <td>193</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>227</td>
      <td>510</td>
      <td>207</td>
      <td>490</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>526</td>
      <td>491</td>
      <td>506</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>527</td>
      <td>530</td>
      <td>507</td>
      <td>510</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>531</td>
      <td>532</td>
      <td>511</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8aq4">8AQ4</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSH</span><span class="topo-inside">MAFASLIERQ</span><span class="topo-membrane">RIRLLLALLFGACGTLA</span><span class="topo-outside">FSPYDV</span><span class="topo-membrane">WPAAIIS</span></span>
<span class="topo-line"><span class="topo-membrane">LMGLQALTF</span><span class="topo-inside">NRRP</span><span class="topo-membrane">LQSAAIGFCWGFGLFGS</span><span class="topo-outside">GINWVYVSIATFGGMPGPVNIFLVV</span><span class="topo-membrane">LLAAY</span></span>
<span class="topo-line"><span class="topo-membrane">LSLYTGLFAGVLSRLW</span><span class="topo-inside">PKTTW</span><span class="topo-membrane">LRVAIAAPALWQVTEFLRGWV</span><span class="topo-outside">LTGFPWLQFGYSQIDGPL</span></span>
<span class="topo-line"><span class="topo-outside">KGLAPIMGVE</span><span class="topo-membrane">AINFLLMMVSGLLALALV</span><span class="topo-inside">KRNW</span><span class="topo-membrane">RPLVVAVVLFALPF</span><span class="topo-outside">PLRYIQWFTPQPEK</span></span>
<span class="topo-line"><span class="topo-outside">TIQVSMVQGDIPQSLKWDEGQLLNTLKIYYNATAPLMGKSSLIIWPESAITDLEINQQPF</span></span>
<span class="topo-line"><span class="topo-outside">LKALDGELRDKGSSLVTGIVDARLNKQNRYDTYNTIITLGKGAPYSYESADRYNKNHLVP</span></span>
<span class="topo-line"><span class="topo-outside">FGEFVPLESILRPLAPFFDLPMSSFSRGPYIQPPLSANGIELTAAICYEIILGEQVRDNF</span></span>
<span class="topo-line"><span class="topo-outside">RPDTDYLLTISNDAWFGKSIGPWQHFQMARMRALELARPLLRSTNNGITAVIGPQGEIQA</span></span>
<span class="topo-line"><span class="topo-outside">MIPQFTREVLTTNVTPTTGLTPYARTGNW</span><span class="topo-membrane">PLWVLTALFGFAAVL</span><span class="topo-inside">MSLRQ</span><span class="topo-unknown">RRK</span></span>
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
      <td>20</td>
      <td>-19</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>21</td>
      <td>30</td>
      <td>1</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>47</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>53</td>
      <td>28</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>69</td>
      <td>34</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>73</td>
      <td>50</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>90</td>
      <td>54</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>115</td>
      <td>71</td>
      <td>95</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>136</td>
      <td>96</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>141</td>
      <td>117</td>
      <td>121</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>162</td>
      <td>122</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>190</td>
      <td>143</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>208</td>
      <td>171</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>212</td>
      <td>189</td>
      <td>192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>226</td>
      <td>193</td>
      <td>206</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>227</td>
      <td>509</td>
      <td>207</td>
      <td>489</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>524</td>
      <td>490</td>
      <td>504</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>525</td>
      <td>529</td>
      <td>505</td>
      <td>509</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>530</td>
      <td>532</td>
      <td>510</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8aq2">8AQ2</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSSHHHHH</span><span class="topo-outside">HSSGLVPRGSHMRWISRPGW</span><span class="topo-membrane">PGHLLALAAGALTPLAL</span><span class="topo-inside">APF</span><span class="topo-membrane">DYWPLAILSIA</span></span>
<span class="topo-line"><span class="topo-membrane">LLYLGLR</span><span class="topo-outside">GLPG</span><span class="topo-membrane">KSALWRGWWYGFGAFGAGTS</span><span class="topo-inside">WIYVSIHDYGAASVPLAS</span><span class="topo-membrane">LLMLGFTAGVA</span></span>
<span class="topo-line"><span class="topo-membrane">FFFALPAWLWARCLR</span><span class="topo-outside">RDNAP</span><span class="topo-membrane">LGDALAFAALWLALELFRSWFL</span><span class="topo-inside">TGFPWLYAGYSQLQGPLA</span></span>
<span class="topo-line"><span class="topo-inside">GLVPV</span><span class="topo-membrane">GGVWLSSFVIALSAALLVNLP</span><span class="topo-outside">RLFPHGA</span><span class="topo-membrane">SLLLGLVLLLGPWAAGLYL</span><span class="topo-inside">KGHAWTHS</span></span>
<span class="topo-line"><span class="topo-inside">AGEPLRVVAIQGNIAQELKWDPNQVRAQLDLYRDLSLPQQDVDLIVWPETAVPILQDMAS</span></span>
<span class="topo-line"><span class="topo-inside">GYLGAMGQVADEKNAALITGVPVRERLADGKSRYFNGITVVGEGAGTYLKQKLVPFGEYV</span></span>
<span class="topo-line"><span class="topo-inside">PLQDLLRGLIAFFDLPMSDFARGPADQPLLKAKGYQIAPYICYEVVYPEFAAALAAQSQV</span></span>
<span class="topo-line"><span class="topo-inside">LLTVSNDTWFGTSIGPLQHLQMAQMRALESGRWMIRATNNGVTGLIDPYGRIVRQIPQFQ</span></span>
<span class="topo-line"><span class="topo-inside">QGILRGEVIPMQGLTPYLQYRV</span><span class="topo-membrane">WPLAGLAGVLLLWALL</span><span class="topo-outside">GRQLRPQERRL</span><span class="topo-unknown">FG</span></span>
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
      <td>-19</td>
      <td>-11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>29</td>
      <td>-10</td>
      <td>9</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>10</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>49</td>
      <td>27</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>67</td>
      <td>30</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>71</td>
      <td>48</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>91</td>
      <td>52</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>109</td>
      <td>72</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>135</td>
      <td>90</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>140</td>
      <td>116</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>162</td>
      <td>121</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>185</td>
      <td>143</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>206</td>
      <td>166</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>213</td>
      <td>187</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>232</td>
      <td>194</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>502</td>
      <td>213</td>
      <td>482</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>503</td>
      <td>518</td>
      <td>483</td>
      <td>498</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>519</td>
      <td>529</td>
      <td>499</td>
      <td>509</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>530</td>
      <td>531</td>
      <td>510</td>
      <td>511</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8b0p">8B0P</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMAF</span><span class="topo-outside">ASLIERQ</span><span class="topo-membrane">RIRLLLALLFGACGTLA</span><span class="topo-inside">FSPYDVW</span><span class="topo-membrane">PAAIIS</span></span>
<span class="topo-line"><span class="topo-membrane">LMGLQALTF</span><span class="topo-outside">NRRP</span><span class="topo-membrane">LQSAAIGFCWGFGLFGS</span><span class="topo-inside">GINWVYVSIATFGGMPGPVNIFLVV</span><span class="topo-membrane">LLAAY</span></span>
<span class="topo-line"><span class="topo-membrane">LSLYTGLFAGVLSRL</span><span class="topo-outside">WPKTTW</span><span class="topo-membrane">LRVAIAAPALWQVTEFLRGWV</span><span class="topo-inside">LTGFPWLQFGYSQIDGPL</span></span>
<span class="topo-line"><span class="topo-inside">KGLAPIMGVE</span><span class="topo-membrane">AINFLLMMVSGLLALALV</span><span class="topo-outside">KRNW</span><span class="topo-membrane">RPLVVAVVLFALPFP</span><span class="topo-inside">LRYIQWFTPQPEK</span></span>
<span class="topo-line"><span class="topo-inside">TIQVSMVQGDIPQSLKWDEGQLLNTLKIYYNATAPLMGKSSLIIWPESAITDLEINQQPF</span></span>
<span class="topo-line"><span class="topo-inside">LKALDGELRDKGSSLVTGIVDARLNKQNRYDTYNTIITLGKGAPYSYESADRYNKNHLVP</span></span>
<span class="topo-line"><span class="topo-inside">FGEFVPLESILRPLAPFFDLPMSSFSRGPYIQPPLSANGIELTAAIAYEIILGEQVRDNF</span></span>
<span class="topo-line"><span class="topo-inside">RPDTDYLLTISNDAWFGKSIGPWQHFQMARMRALELARPLLRSTNNGITAVIGPQGEIQA</span></span>
<span class="topo-line"><span class="topo-inside">MIPQFTREVLTTNVTPTTGLTPYARTGN</span><span class="topo-membrane">WPLWVLTALFGFAAV</span><span class="topo-outside">LMSLR</span><span class="topo-unknown">QRRK</span></span>
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
      <td>23</td>
      <td>-19</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>30</td>
      <td>4</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>47</td>
      <td>11</td>
      <td>27</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>54</td>
      <td>28</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>69</td>
      <td>35</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>73</td>
      <td>50</td>
      <td>53</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>90</td>
      <td>54</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>115</td>
      <td>71</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>135</td>
      <td>96</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>141</td>
      <td>116</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>162</td>
      <td>122</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>190</td>
      <td>143</td>
      <td>170</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>208</td>
      <td>171</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>212</td>
      <td>189</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>227</td>
      <td>193</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>508</td>
      <td>208</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>509</td>
      <td>523</td>
      <td>489</td>
      <td>503</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>524</td>
      <td>528</td>
      <td>504</td>
      <td>508</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>529</td>
      <td>532</td>
      <td>509</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8b0o">8B0O</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MGSSHHHHHHSSGLVPRGSHMA</span><span class="topo-outside">FASLIERQ</span><span class="topo-membrane">RIRLLLALLFGACGTL</span><span class="topo-inside">AFSPYDVW</span><span class="topo-membrane">PAAIIS</span></span>
<span class="topo-line"><span class="topo-membrane">LMGLQALTF</span><span class="topo-outside">NRRP</span><span class="topo-membrane">LQSAAIGFCWGFGLFGS</span><span class="topo-inside">GINWVYVSIATFGGMPGPVNIFLVV</span><span class="topo-membrane">LLAAY</span></span>
<span class="topo-line"><span class="topo-membrane">LSLYTGLFAGVLSRL</span><span class="topo-outside">WPKTTW</span><span class="topo-membrane">LRVAIAAPALWQVTEFLRGWV</span><span class="topo-inside">LTGFPWLQFGYSQIDGPL</span></span>
<span class="topo-line"><span class="topo-inside">KGLAPIMGVE</span><span class="topo-membrane">AINFLLMMVSGLLALALV</span><span class="topo-outside">KRNW</span><span class="topo-membrane">RPLVVAVVLFALPFP</span><span class="topo-inside">LRYIQWFTPQPEK</span></span>
<span class="topo-line"><span class="topo-inside">TIQVSMVQGDIPQSLKWDEGQLLNTLKIYYNATAPLMGKSSLIIWPESAITDLEINQQPF</span></span>
<span class="topo-line"><span class="topo-inside">LKALDGELRDKGSSLVTGIVDARLNKQNRYDTYNTIITLGKGAPYSYESADRYNKNHLVP</span></span>
<span class="topo-line"><span class="topo-inside">FGEFVPLESILRPLAPFFDLPMSSFSRGPYIQPPLSANGIELTAAISYEIILGEQVRDNF</span></span>
<span class="topo-line"><span class="topo-inside">RPDTDYLLTISNDAWFGKSIGPWQHFQMARMRALELARPLLRSTNNGITAVIGPQGEIQA</span></span>
<span class="topo-line"><span class="topo-inside">MIPQFTREVLTTNVTPTTGLTPYARTGN</span><span class="topo-membrane">WPLWVLTALFGFAAV</span><span class="topo-outside">LMSLR</span><span class="topo-unknown">QRRK</span></span>
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
      <td>22</td>
      <td>-19</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>23</td>
      <td>30</td>
      <td>3</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>46</td>
      <td>11</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>54</td>
      <td>27</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>55</td>
      <td>69</td>
      <td>35</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>73</td>
      <td>50</td>
      <td>53</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>90</td>
      <td>54</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>115</td>
      <td>71</td>
      <td>95</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>135</td>
      <td>96</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>141</td>
      <td>116</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>162</td>
      <td>122</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>190</td>
      <td>143</td>
      <td>170</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>191</td>
      <td>208</td>
      <td>171</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>209</td>
      <td>212</td>
      <td>189</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>213</td>
      <td>227</td>
      <td>193</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>228</td>
      <td>508</td>
      <td>208</td>
      <td>488</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>509</td>
      <td>523</td>
      <td>489</td>
      <td>503</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>524</td>
      <td>528</td>
      <td>504</td>
      <td>508</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>529</td>
      <td>532</td>
      <td>509</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Structural architecture of Lnt

E. coli Lnt contains an eight-helix transmembrane (TM) domain that forms a
membrane-embedded cavity with a lateral opening and a periplasmic exit. The
nitrilase (Nit) catalytic domain is located on the periplasmic side of the
membrane, with its catalytic cavity connected to the periplasmic exit of the
TM domain. The Nit domain contains the characteristic alpha-beta-alpha folding
topology of the nitrilase superfamily and a conserved Glu-Lys-Cys catalytic
triad (E267-K335-C387).

### Amphipathic lid loop mediates membrane interaction

An amphipathic lid loop (residues F357-D359) from the Nit domain interacts
with the periplasmic lipid leaflet, forming an interfacial entrance from the
lipid bilayer to the catalytic centre. The lid loop anchors the Nit domain
to the outer leaflet through multiple interactions: aromatic residues F357
and F358 interact with lipid molecules, the acidic sidechain of D359
interacts with the head-group of a [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol) molecule, and the
basic sidechain of R352 interacts with the phosphate-group of a lipid
molecule. The lid loop protects the catalytic site from exposure to the
solvent phase.

### Ping-pong catalytic mechanism

Lnt uses a two-step ping-pong mechanism. In the first step, the lipid donor
substrate enters the catalytic cavity through the interfacial opening, and
an acyl-enzyme thioester intermediate is formed with C387. The leaving group
(sn-2-lyso-glycerolphosphate) is released to the lipid bilayer. In the
second step, the lipid-acceptor substrate (apolipoprotein) enters the
reaction cavity and its N-terminal amine group attacks the reaction-centre
carbon atom, resulting in cleavage of the C-S bond and formation of the
mature triacylated lipoprotein.

### Functional residues identified by mutagenesis

Mutagenesis studies identified several functionally important residues. P147
at the TM-Nit domain interface is important for full Lnt activity. The double
mutant F357A/F358A in the lid loop is inactive. Residues S78 (in TM3),
V339 (lid loop), Y388 (near catalytic Cys), and E389 (alpha3') were shown
to maintain the ability to form the acyl-enzyme intermediate, suggesting
they are involved in the second step of the reaction (substrate recognition
and binding of the apolipoprotein substrate).

### Substrate portal defined by structured lipids

In the LntEco-C387A mutant structure, structured monoolein lipid molecules line up in single file along a hydrophobic pocket connecting the bulk membrane to the active site. This portal is formed by periplasmic extensions of TM3 and TM4 (Arm 1), L1 between H5 and H6 (Arm 2), and loops in the Nit domain (Arm 3). Lipids enter this region from the bulk membrane via the H4-H5 cleft, defining the route for phospholipid substrates to access the active site.

### Conserved nitrilase superfamily fold

Lnt is a member of the nitrilase superfamily with a four-layer alphabeta betaalpha sandwich fold in the Nit domain. The catalytic Cys387 resides in a nucleophilic elbow (beta-strand-turn-helix motif) characteristic of nitrilases. The oxyanion hole is formed by backbone amides of I390, I391, and L392 in alpha3'. Structure-based pKa calculations support the proposed catalytic roles of Glu267 (proton abstraction) and Lys335 (oxyanion stabilization).

### Complete structural snapshots of the ping-pong reaction cycle (2023)

A comprehensive structural study (Smithers et al., Sci. Adv. 2023) used MX and cryo-EM to capture nine structures representing all six states of the Lnt N-acylation ping-pong reaction: Apo (8B0K), M1 (8AQ3/8B0M/8B0L), P1 (8B0N/8AQ4), M2 mimic (8AQ2), and P2 (8B0P/8B0O). The study identified a single active site that binds GPL and BLP substrates sequentially. Three distinct acyl chain binding sites were defined. Arm 3 (residues 348-363) was shown to be flexible in apo and becomes ordered upon substrate binding. The structures validate the ping-pong mechanism, explain substrate promiscuity, and should facilitate antibiotic design.

### Apo state captured by cryo-EM after hydroxylamine treatment

Hydroxylamine (HA) treatment was implemented to remove thioacylation and adventitious phospholipids from Lnt. Cryo-EM analysis provided a 3.0 A reconstruction of the apo state with an active site free of thioacylation, lipids, and substrates. The HA-treated protein was enzymatically active only with added GPLs. Arm 3 was partly disordered in the apo state (16 residues without density: Glu348-Ser363), suggesting it is flexible and involved in substrate binding.

### M1 state reveals PE binding and arm 3 ordering

The M1 (first Michaelis complex) structures show PE bound with its glyceryl phosphoethanolamine headgroup positioned in front of the catalytic triad and acyl chains extending into the hydrophobic groove. The sn-1 ester is positioned next to C387 for reaction. Arm 3 becomes stably folded over the PE molecule. The MX structure (8AQ3, 2.4 A) is the highest resolution Lnt structure to date.

### P1 and acyl-enzyme intermediate states

The P1 (first product complex) structures capture the acyl-enzyme intermediate with a palmitoyl thioester at C387 and lyso-PE bound adjacent. Interactions between enzyme and lyso-PE are fewer than for PE in M1, consistent with lyso-PE release. The S-acyl chain at C387 and lyso-PE occupy distinct volumes in the binding pocket. Native MS confirmed palmitate modification of Lnt.

### P2 state reveals TA-BLP product binding and arm rearrangements

The P2 (second product complex) structures show the triacylated BLP product (Pam3CSK4 or FP3) bound in the pocket. The acyl amide linkage is positioned within a few angstroms of the catalytic site. The diacylated glyceryl moiety extends away from the catalytic center with acyl chains running parallel. The peptide part extends through an opening at the top of the binding pocket created by conformational changes in arm 3 and arm 7. Comparison of P1 and P2 states shows the biggest changes in arms 1, 3, and 9.


## Cross-References

- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/">Phosphatidylglycerol (PG)</a> — Primary acyl-donor lipid substrate for Lnt
- <a href="/xray-mp-wiki/reagents/detergents/dm/">N-Decyl-beta-D-maltopyranoside</a> — Detergent used for membrane solubilization
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Buffer used in lysis, purification, and crystallization
- <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a> — Crystallization method used for structure determination (ncomms15948)
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase">Lipidic Cubic Phase (LCP)</a> — Crystallization method used for structure determination (ncomms15952)
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a> — Purification method used in protein preparation
- <a href="/xray-mp-wiki/reagents/additives/iptg">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/acetate">Acetate</a> — Buffer component in purification and crystallization
- <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA Agarose Resin</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/proteins/enzymes/pseudomonas-aeruginosa-lnt/">Pseudomonas aeruginosa Apolipoprotein N-Acyl Transferase (LntPae)</a> — Orthologous Lnt from P. aeruginosa with 39% sequence identity
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/ping-pong-mechanism/">Ping-Pong Catalytic Mechanism</a> — Lnt N-acylation cycle provides definitive structural evidence for ping-pong mechanism; 9 structures capturing all reaction states
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — Six of nine structures determined by cryo-EM showing all states of the Lnt reaction cycle
