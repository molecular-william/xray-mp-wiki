---
title: "YePEPT (Yersinia enterocolitica Peptide Transporter)"
created: 2026-06-11
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [membrane-protein, transporter, transporter, xray-crystallography]
sources: [doi/10.1186##s12915-015-0167-8, doi/10.1038##s42004-022-00636-0]
verified: regex
uniprot_id: A0A2R9TD79
---

# YePEPT (Yersinia enterocolitica Peptide Transporter)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A2R9TD79">UniProt: A0A2R9TD79</a>

<span class="expr-badge">Yersinia enterocolitica subsp. palearctica YE-P4</span>

## Overview

YePEPT is a proton-dependent oligopeptide transporter (POT) family member from
the bacterium Yersinia enterocolitica. It is a membrane protein that mediates
the cellular uptake of di- and tripeptides using energy provided by
transmembrane proton gradients. YePEPT belongs to the major facilitator
superfamily ([MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/)) of secondary active transporters. The X-ray crystal structure
of YePEPT at 3.02 A resolution revealed the molecular bases for recognition,
binding and specificity of dipeptides with a charged amino acid residue at the
N-terminal position. Lys314 in the substrate-binding pocket determines
specificity for negatively charged dipeptides (Asp-Ala, Glu-Ala) via
electrostatic interactions. Mutagenesis of Lys314 to Glu (K314E) re-tuned
specificity toward positively charged dipeptides (Lys-Ala), while the K314A
mutation abolished charged dipeptide specificity. The corresponding mutation in
human PEPT1 (Q300K) similarly introduced affinity for Asp-Ala, demonstrating
that this electrostatic recognition mechanism is conserved from bacteria to
humans.
A subsequent structure of the YePEPT K314A variant in complex with the potent
PEPT1/PEPT2 inhibitor Lys[Z(NO2)]-Val (LZNV) at 3.1 A resolution revealed the
molecular details of inhibitor binding and a previously undescribed mostly
hydrophobic pocket, the PZ pocket, that forms upon inhibitor binding. The apo
structure of YePEPT K314A at 2.93 A provided the ligand-free reference.
Comparison showed that the PZ pocket is initially absent and emerges through
conformational changes (rigid body movement of the N-terminal bundle by ~5°
and rotamer changes of F318, Y35, and Y159) upon LZNV binding. The Z(NO2)
moiety of LZNV bound to the PZ pocket acts like a wedge impeding transition
to the inward-open state, revealing the inhibition mechanism.


## Publications

### doi/10.1186##s12915-015-0167-8

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4w6v">4W6V</a></td>
      <td>3.02</td>
      <td>P2_1_2_1_2_1</td>
      <td>Full-length YePEPT with C-terminal HRV3C cleavage site and deca-His tag</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) pLysS
- **Construct**: YePEPT gene (UniProt R9G739) with C-terminal HRV3C protease cleavage site and deca-His tag, cloned into pZUDF21-rbs vector
- **Notes**: Overexpressed at 20 C for 16-20 h with 0.3 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) induction. K314A mutant purified for LZNV-bound and apo structures.

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: YePEPT with C-terminal HRV3C-decaHis tag
- **Tag info**: deca-His tag, cleaved by HRV3C protease

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
      <td>Microfluidizer (15,000 psi, 5 passages)</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl</td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Ultracentrifugation (100,000 x g, 1 h, 4 C)</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl</td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent extraction, 1 h at 4 C</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA Superflow Beads</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Washed with 10 CV of washing buffer (20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 5 mM histidine, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>). Eluted by HRV3C protease cleavage overnight.</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Concentrated to ~10 mg/mL for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>YePEPT at ~10 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M HEPES pH 7.5, 10% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400, 10% isopropanol</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>1:1</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4w6v">4W6V</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQT</span><span class="topo-outside">STNTPGGRTFFGHPY</span><span class="topo-membrane">PLSGLFLSEMWERFSFYGIRP</span><span class="topo-inside">LLILFMAATVFDGGMGLPREQAS</span><span class="topo-membrane">AIVGIFAGSMYLAALPGGLLA</span><span class="topo-outside">DNWLGQ</span><span class="topo-membrane">QRAVWYGSILIALGHLSI</span><span class="topo-inside">ALSAFFGNDLFF</span><span class="topo-membrane">I</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GLVFIVLGTGLFKTCISVMV</span><span class="topo-outside">GTLYKPGDARRDGG</span><span class="topo-membrane">FSLFYMGINMGSFIAPLL</span><span class="topo-inside">SGWLLRTHGWHWGFG</span><span class="topo-membrane">IGGIGMLVALLIFRGFAIPA</span><span class="topo-outside">MKRYDAEVGLDSSWNKPT</span><span class="topo-unknown">NQRQGV</span><span class="topo-outside">G</span><span class="topo-membrane">RWVTAIMA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">VVVVIIALIS</span><span class="topo-inside">QGVIPINP</span><span class="topo-membrane">VMIASLLVYVIAASVTLYFI</span><span class="topo-outside">YLFAFAKMSRKDRARLLVC</span><span class="topo-membrane">FILLVSAAFFWSAFEQKPTSF</span><span class="topo-inside">NLFANDYTDRMVMGFEIPTVW</span><span class="topo-membrane">FQSINALFIILLAPVFSWA</span><span class="topo-unknown">WP</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-unknown">ALAKKKIQ</span><span class="topo-outside">PSS</span><span class="topo-membrane">ITKFVIGILCAAAGFAVMM</span><span class="topo-inside">YAAQHVLSSGGAGVSPLW</span><span class="topo-membrane">LVMSILLLTLGELCLSPIGL</span><span class="topo-outside">ATMTLLAPDRMRGQV</span><span class="topo-membrane">MGLWFCASSLGNLAAGLIG</span><span class="topo-inside">GHVKADQLDMLPTL</span><span class="topo-membrane">FARC</span></span>
<span class="topo-ruler">       490       500       510         </span>
<span class="topo-line"><span class="topo-membrane">SIALVICAAVLILL</span><span class="topo-outside">IVPIRRLM</span><span class="topo-unknown">NNTQGQQTALELEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>4</td>
      <td>18</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>39</td>
      <td>19</td>
      <td>39</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>62</td>
      <td>40</td>
      <td>62</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>83</td>
      <td>63</td>
      <td>83</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>89</td>
      <td>84</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>107</td>
      <td>90</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>119</td>
      <td>108</td>
      <td>119</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>140</td>
      <td>120</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>154</td>
      <td>141</td>
      <td>154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>172</td>
      <td>155</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>187</td>
      <td>173</td>
      <td>187</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>188</td>
      <td>207</td>
      <td>188</td>
      <td>207</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>208</td>
      <td>225</td>
      <td>208</td>
      <td>225</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>232</td>
      <td>232</td>
      <td>232</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>233</td>
      <td>250</td>
      <td>233</td>
      <td>250</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>251</td>
      <td>258</td>
      <td>251</td>
      <td>258</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>278</td>
      <td>259</td>
      <td>278</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>297</td>
      <td>279</td>
      <td>297</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>298</td>
      <td>318</td>
      <td>298</td>
      <td>318</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>319</td>
      <td>339</td>
      <td>319</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>358</td>
      <td>340</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>369</td>
      <td>371</td>
      <td>369</td>
      <td>371</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>372</td>
      <td>390</td>
      <td>372</td>
      <td>390</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>391</td>
      <td>408</td>
      <td>391</td>
      <td>408</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>409</td>
      <td>428</td>
      <td>409</td>
      <td>428</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>429</td>
      <td>443</td>
      <td>429</td>
      <td>443</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>462</td>
      <td>444</td>
      <td>462</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>463</td>
      <td>476</td>
      <td>463</td>
      <td>476</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>477</td>
      <td>494</td>
      <td>477</td>
      <td>494</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>495</td>
      <td>502</td>
      <td>495</td>
      <td>502</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##s42004-022-00636-0

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7pz3">7PZ3</a></td>
      <td>3.10</td>
      <td>P2_1_2_1_2_1</td>
      <td>YePEPT K314A mutant with C-terminal HRV3C cleavage site and deca-His tag</td>
      <td>LZNV (Lys[Z(NO2)]-Val)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7pz4">7PZ4</a></td>
      <td>2.93</td>
      <td>P2_1_2_1_2_1</td>
      <td>YePEPT K314A mutant with C-terminal HRV3C cleavage site and deca-His tag</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3) pLysS
- **Construct**: YePEPT gene (UniProt R9G739) with C-terminal HRV3C protease cleavage site and deca-His tag, cloned into pZUDF21-rbs vector
- **Notes**: Overexpressed at 20 C for 16-20 h with 0.3 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) induction. K314A mutant purified for LZNV-bound and apo structures.

**Purification:**

- **Expression system**: E. coli BL21(DE3) pLysS
- **Expression construct**: YePEPT K314A with C-terminal HRV3C cleavage site and deca-His tag in pZUDF21-rbs vector
- **Tag info**: deca-His tag, cleaved by HRV3C protease

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
      <td>Sonication (60 min total ON, 5 s ON/3 s OFF)</td>
      <td>—</td>
      <td>20 mM Tris-HCl pH 8.0, 50 mM NaCl</td>
      <td>Cells thawed and sonicated using Branson 450 Digital Sonifier</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Ultracentrifugation (150,000 x g, 1 h, 4 C)</td>
      <td>—</td>
      <td>20 mM Tris-HCl pH 8.0, 500 mM NaCl</td>
      <td>Washed once with membrane wash buffer</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent extraction, 1 h at 4 C</td>
      <td>—</td>
      <td>20 mM Tris-HCl pH 8.0, 300 mM NaCl + 2% (w/v) n-undecyl-β-D-maltopyranoside (UDM)</td>
      <td></td>
    </tr>
    <tr>
      <td>Ni-NTA affinity chromatography</td>
      <td>Affinity chromatography</td>
      <td>Ni-NTA Superflow resin</td>
      <td>20 mM Tris-HCl pH 8.0, 150 mM NaCl, 0.075% (w/v) UDM</td>
      <td>Washed with 20 mM Tris-HCl pH 8.0, 300 mM NaCl, 5 mM L-histidine, 0.1% (w/v) UDM. Eluted by on-column HRV3C protease cleavage overnight.</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified YePEPT K314A in detergent-containing buffer

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>YePEPT K314A at ~10 mg/mL in 20 mM Tris-HCl pH 8.0, 150 mM NaCl, 0.075% (w/v) UDM</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M HEPES pH 7.5, 8% PEG 400, 10% isopropanol (for apo); 0.1 M HEPES pH 7.5, 8% PEG 400, 10% isopropanol, 0.5-1.0 mM LZNV (for LZNV-bound)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Apo crystals grown as previously described. LZNV-bound crystals obtained by co-crystallization with 0.5-1.0 mM LZNV. Data collected at SLS beamline X06SA. Orthorhombic P2_1_2_1_2_1 space group.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Electrostatic recognition of charged dipeptides by Lys314

Lys314 in the YePEPT substrate-binding pocket forms a salt bridge with
negatively charged N-terminal amino acid side chains of dipeptides (Asp-Ala,
Glu-Ala). This electrostatic interaction is the primary determinant of
specificity for charged substrates. In the apo structure, the positive charge
of Lys314 is stabilized by a hydrogen bond and pi-cation interaction with
Phe311. Mutation F311A severely impairs transport function, confirming the
importance of this stabilization.

### Tuning substrate specificity by charge reversal

The K314E charge reversal mutation in YePEPT switches specificity from
negatively charged dipeptides (Asp-Ala, Glu-Ala) to positively charged
dipeptides (Lys-Ala). The K314A mutation abolishes charged dipeptide
specificity entirely. This demonstrates that a single residue at position
314 controls charged dipeptide recognition via electrostatic complementarity.

### Conserved mechanism in human PEPT1

The corresponding residue in human PEPT1 is Gln300. Introduction of the
Q300K mutation into hPEPT1 conferred affinity for Asp-Ala while reducing
affinity for Lys-Ala, demonstrating that the electrostatic recognition
mechanism identified in YePEPT is transferable to the human peptide
transporter PEPT1.

### PZ pocket: a novel inhibitor-induced binding pocket in POTs

The LZNV-bound structure of YePEPT K314A reveals a previously undescribed mostly hydrophobic pocket (PZ pocket) that accommodates the Z(NO2) moiety of LZNV. The PZ pocket is comprised of 9 residues within 4.0 Å of the Z(NO2) moiety: F311, Q313, A314, F318, F386, M389, S412, I413, and L416. Most of these residues are conserved in bacterial peptide transporters as well as in human PEPT1 and PEPT2. A π-stacking interaction between F318 and the 4-nitrophenyl group of LZNV anchors the inhibitor in the PZ pocket. The PZ pocket is absent in the ligand-free (apo) state and forms only upon LZNV binding through conformational changes, suggesting its potential as a target for inhibitor design.

### Conformational changes and PZ pocket formation upon LZNV binding

Comparison of the apo and LZNV-bound structures of YePEPT K314A reveals three key conformational changes: (1) the N-terminal six-helix bundle undergoes a rigid body movement of ~5° towards the C-terminal bundle (hinge at the periplasmic region); (2) F318 adopts a new rotamer conformation to create space for the Z(NO2) moiety and form π-stacking with the 4-nitrophenyl group; (3) the hydroxyl group of Y35 (TM1) moves ~2 Å to interact with the LZNV carboxyl group, and Y159 (TM5) adopts a new rotamer with a 9.5 Å hydroxyl shift to orient E420 for ligand binding. The PZ pocket is initially absent in the apo state and forms upon inhibitor binding.

### Wedge mechanism of POT inhibition by LZNV

LZNV inhibits POTs through a unique mechanism: after the dipeptide backbone of LZNV binds to the conserved substrate-binding pocket, the Z(NO2) moiety induces formation of the initially absent PZ pocket via rotamer changes of specific amino acid side chains. The Z(NO2) moiety anchored deep in the C-terminal bundle acts like a wedge that impedes the transition from the inward-facing occluded state to the inward-open state, thereby blocking the transport cycle. This mechanism is supported by thermal shift assays, uptake competition experiments, and structural analysis of humanised YePEPT variants (K314Q-P315G) confirming relevance to human PEPT1/PEPT2.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/pot-family-substrate-specificity/">POT Family Substrate Specificity</a> — YePEPT defines the electrostatic mechanism for charged dipeptide recognition in the POT family
- <a href="/xray-mp-wiki/concepts/protein-families/mfs-transporter/">Major Facilitator Superfamily (MFS)</a> — YePEPT belongs to the MFS fold with N- and C-terminal six-helix bundles
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — YePEPT structure is in the inward-open conformation, representing one state of the alternating access cycle
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/peptide-binding-pocket/">Peptide Binding Pocket</a> — LZNV binds in the conserved substrate-binding pocket with additional PZ pocket interactions
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/pz-pocket-pot-inhibition/">PZ Pocket POT Inhibition</a> — LZNV-bound structure reveals the PZ pocket, a novel inhibitor-induced binding pocket
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer component in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
