---
title: "Gdx-Clo SMR Transporter (Clostridales oral taxon 876)"
created: 2026-06-09
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-020-19820-8, doi/10.1073##pnas.2403273121]
verified: false
---

# Gdx-Clo SMR Transporter (Clostridales oral taxon 876)

## Overview

Gdx-Clo is a small multidrug resistance (SMR) family transporter from *Clostridales* oral taxon 876, belonging to the guanidinium (Gdx) subtype of SMR transporters. It is a dual-topology antiparallel homodimer with each subunit comprising 4 transmembrane helices (4-TM). Gdx-Clo functions as a Gdm⁺/H⁺ antiporter and exhibits promiscuous transport of hydrophobic substituted cations. The crystal structure of Gdx-Clo in complex with a synthetic monobody (Clo-L10) was determined at up to 2.3 Å resolution, revealing the molecular basis for substrate promiscuity. A membrane portal between the TM2 helices provides direct access for hydrophobic substrate substituents from the lipid bilayer. The two subunits adopt non-equivalent A and B conformations, with the strictly conserved substrate- and proton-binding glutamate E13ₐ and E13₆ accessible at the bottom of a large aqueous chamber open to one side of the membrane.


## Publications

### doi/10.1038##s41467-020-19820-8

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6xgq">6XGQ</a></td>
      <td>3.50</td>
      <td>C121</td>
      <td>Full-length Gdx-Clo (residues 1-108) with Clo-L10 monobody</td>
      <td>None (apo)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6xgr">6XGR</a></td>
      <td>2.30</td>
      <td>C121</td>
      <td>Full-length Gdx-Clo with Clo-L10 monobody</td>
      <td>Phenylguanidinium (phenylGdm⁺)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6xgs">6XGS</a></td>
      <td>2.30</td>
      <td>C121</td>
      <td>Full-length Gdx-Clo with Clo-L10 monobody</td>
      <td>Octylguanidinium (octylGdm⁺)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41 (DE3)
- **Construct**: C-terminal hexahistidine tag with LysC recognition site, cloned in pET-21c
- **Induction**: 0.2 mM IPTG for 3 h at 37°C

**Purification:**

- **Expression system**: E. coli C41 (DE3)
- **Expression construct**: C-terminal His6-tag with LysC site
- **Tag info**: [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag)

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
      <td>Cell culture</td>
      <td>Fermentation</td>
      <td>--</td>
      <td>LB medium + --</td>
      <td>Standard E. coli culture</td>
    </tr>
    <tr>
      <td>Induction</td>
      <td>Chemical induction</td>
      <td>--</td>
      <td>--</td>
      <td>0.2 mM IPTG, 3 h at 37°C</td>
    </tr>
    <tr>
      <td>Membrane extraction</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>100 mM NaCl, 20 mM imidazole + 2% (w/v) <a href="/xray-mp-wiki/reagents/detergents/decyl-maltoside">Decyl Maltoside (DM)</a></td>
      <td>Cell lysate extracted with DM</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Immobilized metal-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (IMAC)</td>
      <td>Cobalt affinity column</td>
      <td>100 mM NaCl, 20 mM imidazole (wash); 400 mM imidazole (elution) + 5 mM DM</td>
      <td>His6-tag purification</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Proteolytic cleavage</td>
      <td>--</td>
      <td>--</td>
      <td>LysC protease (200 ng per mg protein, 2 h at room temperature)</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>Superdex 200</td>
      <td>100 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES Buffer</a>-NaOH, pH 8.1 + 5 mM DM</td>
      <td>Final purification step</td>
    </tr>
  </tbody>
</table>
**Final sample**: 10 mg/ml in DM
**Purity**: Purified to homogeneity

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>10 mg/ml Gdx-Clo dimer mixed with Clo-L10 monobody at 2:1:1 ratio</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>200 mM CaCl₂, 0.1 M Tris-HCl pH 8.0, 32-36% PEG 600</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>0.45 µl protein + 0.3 µl reservoir</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>14 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Flash-cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Initial hits improved by adding charged detergents (LDAO, Apo12) or octylGdm⁺ to protein solution before mixing. For selenomethionine-incorporated protein: 0.1 M LiNO₃, 0.1 M ADA pH 6.8, 35% PEG 600. For phenylGdm⁺-bound: 0.1 M LiNaSO₄, 100 mM Tris pH 8.8, 34% PEG 600. For octylGdm⁺-bound: 0.1 M calcium acetate, 0.1 M HEPES pH 7.5, 33% PEG 600. Data collected at LS-CAT beamline 21-ID-D (APS).</td>
    </tr>
  </tbody>
</table>
### doi/10.1073##pnas.2403273121

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8vxu">8VXU</a></td>
      <td>2.5</td>
      <td></td>
      <td>Gdx-Clo A60T mutant in complex with cetrimonium (CTA⁺). Structure determined at ~2.5 Å resolution (SI Appendix, Table S1). The CTA⁺ quaternary ammonium headgroup binds ~2.5 Å higher and ~4 Å farther back in the pocket than guanidinyl substrates, with the alkyl tail extending through a membrane portal between helices 2A and 2B.</td>
      <td>Cetrimonium (CTA⁺)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41 (DE3)
- **Construct**: C-terminal hexahistidine tag with LysC recognition site, cloned in pET-21c
- **Induction**: 0.2 mM IPTG for 3 h at 37°C

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8vxu">8VXU</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MA</span><span class="topo-membrane">WLILIIAGIFEVVWAIALK</span><span class="topo-inside">YSNGFTRL</span><span class="topo-membrane">IPSMITLIGMLISFYLLSQA</span><span class="topo-outside">TKTLPIGT</span><span class="topo-membrane">AYT</span></span>
<span class="topo-line"><span class="topo-membrane">IWTGIGALGAVICG</span><span class="topo-inside">IIFFKEPLTAL</span><span class="topo-membrane">RIVFMILLLTGIIGLKA</span><span class="topo-outside">TS</span><span class="topo-unknown">SGGTAK</span></span>
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
      <td>3</td>
      <td>21</td>
      <td>3</td>
      <td>21</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>22</td>
      <td>29</td>
      <td>22</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>49</td>
      <td>30</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>57</td>
      <td>50</td>
      <td>57</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>74</td>
      <td>58</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>85</td>
      <td>75</td>
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
      <td>104</td>
      <td>103</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>110</td>
      <td>105</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8vxu">8VXU</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-membrane">AWLILIIAGIFEVVWAIAL</span><span class="topo-outside">KYSNGFTRLIPS</span><span class="topo-membrane">MITLIGMLISFYLLSQAT</span><span class="topo-inside">KTLPI</span><span class="topo-membrane">GTAYT</span></span>
<span class="topo-line"><span class="topo-membrane">IWTGIGALGAVIC</span><span class="topo-outside">GIIFFKEPLTAL</span><span class="topo-membrane">RIVFMILLLTGIIGLKA</span><span class="topo-inside">TS</span><span class="topo-unknown">SGGTAK</span></span>
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
      <td>2</td>
      <td>20</td>
      <td>2</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>21</td>
      <td>32</td>
      <td>21</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>50</td>
      <td>33</td>
      <td>50</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>51</td>
      <td>55</td>
      <td>51</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>73</td>
      <td>56</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>85</td>
      <td>74</td>
      <td>85</td>
      <td>Outside</td>
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
      <td>104</td>
      <td>103</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>110</td>
      <td>105</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Dual topology antiparallel homodimer architecture

Gdx-Clo forms an antiparallel homodimer where the two 4-TM subunits are arranged in opposite orientations relative to the membrane plane. This dual topology architecture is extremely rare and is a defining feature of the SMR family. The two subunits adopt non-equivalent A and B conformations. Transport involves a conformational swap between the two structurally distinct monomers, sealing the substrate binding site on one side of the membrane while opening an identical site on the opposite side. As a consequence of the antiparallel architecture, the inward-open and outward-open conformations are structurally identical, related by twofold symmetry about an axis parallel to the membrane plane.

### GxxxAxxxG packing motifs mediate conformational exchange

The conformational exchange between A and B subunits is facilitated by two GxxxAxxxG packing motifs in TM3. The first motif (G65-I66-G69 in Gdx-Clo, corresponding to G65I G in EmrE numbering) mediates tight helix packing, while the second motif (G72-A76-G79) forms a looser interface. During the conformational swap, regions that alternate in solvent accessibility include TM2, loop 2, and the first GxxxAxxxG motif of TM3 (magenta in the structure), and TM1, loop 1, and the second GxxxAxxxG motif of TM3 (dark blue).

### Minimal substrate coordination enables promiscuity

The strictly conserved E13ₐ and E13₆ form the substrate- and proton-binding site. The guanidinyl group of transported substrates coordinates with E13 via a single hydrogen bond, in contrast to the bidentate coordination observed in solution or by guanidine riboswitches. This minimal coordination explains the permissiveness of Gdx-Clo towards guanidinium ions with methyl, ethyl, or phenyl substitutions. The E13ₐ is deflected by a cross-subunit interaction with Y59₆, and displacement of Y59₆ by the guanidinyl group is proposed to initiate the transport motion.

### Membrane portal for hydrophobic substrate access

A cleft between the antiparallel TM2 helices of the two subunits provides a portal from the membrane to the substrate binding site. This portal accommodates hydrophobic substituents that partition into the lipid bilayer, as demonstrated by the octylGdm⁺-bound structure where the eight-carbon tail protrudes into the detergent micelle. The portal is lined by hydrophobic residues including M39 and F43 on TM2 that undergo rotameric rearrangements to accommodate bulky substituents. This feature provides a selectivity mechanism against physiological guanidinylated metabolites (arginine, creatine, agmatine) that have polar tail groups with high energetic penalty for membrane insertion.

### Functional promiscuity across SMR subtypes

Both the Qac subtype (exemplified by EmrE) and Gdx subtype (Gdx-Clo) of SMR transporters exhibit promiscuous transport of hydrophobic substituted cations. Solid-supported membrane (SSM) electrophysiology and radioactive exchange assays showed that Gdx-Clo transports guanidinyl compounds with hydrophobic single substitutions (methylGdm⁺, ethylGdm⁺, phenylGdm⁺), while EmrE requires additional hydrophobicity and bulk and accommodates substrates with reduced H-bonding capacity (tetramethylGdm⁺, tetramethylammonium). The broad substrate range and presence with horizontal gene transfer elements suggests that promiscuous transport functions contribute to the evolutionary success and dissemination of SMR genes.

### Engineering quaternary ammonium transport via peripheral mutations

Combinatorial mutagenesis and deep sequencing identified seven mutations (G10I, W16G, A17T, M39Y, A60T, A67I, K101N) that convert the selective Gdx-Clo into a promiscuous quaternary ammonium antiseptic exporter (Gdx-Clo-7x). The mutations cluster into three groups: cluster 1 (G10I) at the TM1-TM2 interface, cluster 2 (W16G/A17T/M39Y) near the binding site, and cluster 3 (A60T/A67I/K101N) at the membrane portal. Crucially, substrate preference changes not through modification of residues that directly interact with the substrate but through peripheral mutations that remodel the binding pocket hydrogen bond network and increase sidechain flexibility. Cluster 1 and 2 mutations are necessary and sufficient for polyspecific quaternary ammonium transport, while cluster 3 mutations enhance transport rate. The engineered Gdx-Clo-7x loses Gdm⁺ transport and acquires the substrate preference profile characteristic of EmrE and the SMR_Qac subtype, recapitulating a plausible evolutionary pathway.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/emre/">EmrE (E. coli SMR transporter)</a> — Prototypical Qac subtype SMR transporter for structural and functional comparison
- <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">Polyhistidine Tag (His6)</a> — Affinity tag for purification
- <a href="/xray-mp-wiki/reagents/detergents/decyl-maltoside/">Decyl Maltoside (DM)</a> — Detergent for solubilization and purification
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO (Lauryldimethylamine-N-Oxide)</a> — Charged detergent additive for crystallization
- <a href="/xray-mp-wiki/reagents/additives/peg-600/">PEG 600</a> — Crystallization precipitant
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a> — Crystallization buffer
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Purification and crystallization buffer
- <a href="/xray-mp-wiki/concepts/smr-family/">SMR Family (Small Multidrug Resistance Transporters)</a> — Transporter family classification
