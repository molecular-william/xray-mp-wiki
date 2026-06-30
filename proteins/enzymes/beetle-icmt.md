---
title: "Isoprenylcysteine Carboxyl Methyltransferase (ICMT) from Tribolium castaneum"
created: 2026-06-03
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature25439]
verified: false
---

# Isoprenylcysteine Carboxyl Methyltransferase (ICMT) from Tribolium castaneum

## Overview

ICMT (isoprenylcysteine carboxyl methyltransferase) from the beetle Tribolium castaneum is an integral membrane enzyme that catalyzes the final step of CAAX box processing — the carboxyl methylation of prenylated cysteine residues in proteins such as RAS GTPases, prelamin A, and RAB proteins. The beetle ortholog exhibited superior biochemical stability compared to other eukaryotic ICMT orthologues, making it suitable for crystallization. The structure reveals eight transmembrane alpha-helices and a unique active site architecture spanning both cytosolic and membrane-exposed regions, solving the topographical challenge of bringing two reactants with different cellular localizations together in a membrane environment.

## Publications

### doi/10.1038##nature25439

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5v7p">5V7P</a></td>
      <td>2.3 A</td>
      <td>P21 21 21</td>
      <td>Full-length beetle ICMT (UniProt D6WJ77) with C-terminal YL1/2 antibody-affinity tag (AAEGEEF), in complex with AdoHcy cofactor, <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> lipid, and MB-15 monobody inhibitor. Surface mutations G151A and E154A introduced for crystallizability.</td>
      <td><a href="/xray-mp-wiki/reagents/cofactors/s-adenosyl-l-homocysteine/">S Adenosyl L Homocysteine</a> (AdoHcy), <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> lipid, MB-15 monobody</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5v7p">5V7P</a></td>
      <td>4.0 A</td>
      <td>C2221</td>
      <td>Beetle ICMT without monobody, in detergent (<a href="/xray-mp-wiki/reagents/detergents/dmng/">Dmng</a>)</td>
      <td>AdoHcy cofactor, lipid density in cavity</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris strain SMD1168
- **Construct**: Full-length beetle ICMT (D6WJ77) with C-terminal YL1/2 antibody-affinity tag (Ala-Ala-Glu-Gly-Glu-Glu-Phe, AAEGEEF). Cloned into pPICZ-C vector (EcoRI and SalI sites). Surface mutations G151A and E154A introduced to improve crystallizability.

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
      <td>Cell lysis and solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> (pH 7.5), 150 mM KCl, 2 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a>, 2 mM CaCl2, 25 uM AdoHcy + 2 g <a href="/xray-mp-wiki/reagents/detergents/dmng/">Dmng</a> (decyl <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> neopentyl glycol) per 40 g cells, 45 min at room temperature</td>
      <td>Lysed P. pastoris cells extracted with <a href="/xray-mp-wiki/reagents/detergents/dmng/">Dmng</a> detergent</td>
    </tr>
    <tr>
      <td>Antibody-affinity chromatography</td>
      <td>Affinity chromatography</td>
      <td>YL1/2 antibody coupled to CNBr-activated sepharose beads</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> (pH 7.5), 150 mM KCl, 2 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a>, 2 mM CaCl2, 25 uM AdoHcy, 1 mM <a href="/xray-mp-wiki/reagents/detergents/dmng/">Dmng</a> + 1 mM <a href="/xray-mp-wiki/reagents/detergents/dmng/">Dmng</a></td>
      <td>YL1/2 antibody recognizes C-terminal AAEGEEF tag. Elution with 5 mM Asp-Phe peptide or Glu-Glu-Phe peptide</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>Superdex 200 Increase column (GE Healthcare)</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> (pH 7.5), 150 mM KCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP</a>, 2 mM CaCl2, 25 uM AdoHcy, 1 mM <a href="/xray-mp-wiki/reagents/detergents/dmng/">Dmng</a> + 1 mM <a href="/xray-mp-wiki/reagents/detergents/dmng/">Dmng</a></td>
      <td>ICMT-monobody complex purified at 1:3 molar ratio (ICMT:monobody)</td>
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
      <td>Protein sample</td>
      <td>Purified beetle ICMT in complex with MB-15 monobody (1:3 molar ratio)</td>
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
      <td>Crystals obtained in lipidic-cubic phase in the presence of AdoHcy cofactor and AGGC substrate analog. SeMet crystals collected for SAD phasing. Native crystals at 2.3 A (P21 21 21) and 4.0 A (C2221, ICMT without monobody in detergent).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5v7p">5V7P</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">LSPAGKISLQS</span><span class="topo-membrane">FTGSSLVFFVICMFNHY</span><span class="topo-inside">YGITNL</span><span class="topo-membrane">VVNTLIVFFYAVNVYFF</span><span class="topo-outside">LKFFYNEFAFAIAI</span><span class="topo-membrane">RAAFLGLVLVLGLYIKLVA</span><span class="topo-inside">PPNI</span><span class="topo-membrane">QIFGGYMSVMALFHYS</span><span class="topo-outside">EFLAIAIVQPKQVST</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">DSFVI</span><span class="topo-membrane">NHSPQYTIAAVSSWVEFFI</span><span class="topo-inside">ETYFFPGLKEIH</span><span class="topo-membrane">WLSNIGLCVCILGEVLR</span><span class="topo-outside">KTAILTAGSNFNHLVQCEKSSDHVLVTHGVYAWFRHPSYV</span><span class="topo-membrane">GWFYWSIGTQIILINP</span><span class="topo-inside">L</span><span class="topo-membrane">CIPAYTLASW</span></span>
<span class="topo-ruler">       250       260       270       280        </span>
<span class="topo-line"><span class="topo-membrane">MFF</span><span class="topo-outside">KERIYIEESMLLSFFGQQYCDYQQQVGTGIPFIEGYKI</span><span class="topo-unknown">AAEGEEF</span></span>
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
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>29</td>
      <td>13</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>35</td>
      <td>30</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>36</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>66</td>
      <td>53</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>85</td>
      <td>67</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>89</td>
      <td>86</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>105</td>
      <td>90</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>125</td>
      <td>106</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>144</td>
      <td>126</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>156</td>
      <td>145</td>
      <td>156</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>173</td>
      <td>157</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>213</td>
      <td>174</td>
      <td>213</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>229</td>
      <td>214</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>230</td>
      <td>230</td>
      <td>230</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>243</td>
      <td>231</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>281</td>
      <td>244</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5v7p">5V7P</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90     </span>
<span class="topo-line"><span class="topo-outside">AVSSVPTKLEVVAATPTSLLISWDAPAVTVDLYVITYGETGGNSPVQEFKVPGSKSTATISGLKPGVDYTITVYAFSSYYWPSYKGSPISINYRT</span></span>
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
      <td>95</td>
      <td>0</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5v7p">5V7P</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">LSPAGKISLQS</span><span class="topo-membrane">FTGSSLVFFVICMFNHY</span><span class="topo-inside">YGITNL</span><span class="topo-membrane">VVNTLIVFFYAVNVYFF</span><span class="topo-outside">LKFFYNEFAFAIAI</span><span class="topo-membrane">RAAFLGLVLVLGLYIKLVA</span><span class="topo-inside">PPNI</span><span class="topo-membrane">QIFGGYMSVMALFHYS</span><span class="topo-outside">EFLAIAIVQPKQVST</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">DSFVI</span><span class="topo-membrane">NHSPQYTIAAVSSWVEFFI</span><span class="topo-inside">ETYFFPGLKEIH</span><span class="topo-membrane">WLSNIGLCVCILGEVLR</span><span class="topo-outside">KTAILTAGSNFNHLVQCEKSSDHVLVTHGVYAWFRHPSYV</span><span class="topo-membrane">GWFYWSIGTQIILINP</span><span class="topo-inside">L</span><span class="topo-membrane">CIPAYTLASW</span></span>
<span class="topo-ruler">       250       260       270       280        </span>
<span class="topo-line"><span class="topo-membrane">MFF</span><span class="topo-outside">KERIYIEESMLLSFFGQQYCDYQQQVGTGIPFIEGYKI</span><span class="topo-unknown">AAEGEEF</span></span>
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
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>12</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>29</td>
      <td>13</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>35</td>
      <td>30</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>52</td>
      <td>36</td>
      <td>52</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>53</td>
      <td>66</td>
      <td>53</td>
      <td>66</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>67</td>
      <td>85</td>
      <td>67</td>
      <td>85</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>86</td>
      <td>89</td>
      <td>86</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>105</td>
      <td>90</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>125</td>
      <td>106</td>
      <td>125</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>144</td>
      <td>126</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>145</td>
      <td>156</td>
      <td>145</td>
      <td>156</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>173</td>
      <td>157</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>213</td>
      <td>174</td>
      <td>213</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>229</td>
      <td>214</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>230</td>
      <td>230</td>
      <td>230</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>243</td>
      <td>231</td>
      <td>243</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>281</td>
      <td>244</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5v7p">5V7P</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90     </span>
<span class="topo-line"><span class="topo-outside">AVSSVPTKLEVVAATPTSLLISWDAPAVTVDLYVITYGETGGNSPVQEFKVPGSKSTATISGLKPGVDYTITVYAFSSYYWPSYKGSPISINYRT</span></span>
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
      <td>95</td>
      <td>0</td>
      <td>94</td>
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

### Integral membrane architecture with eight transmembrane helices

Beetle ICMT contains eight transmembrane alpha-helices (M1-M8) and resides almost entirely within the endoplasmic reticulum membrane. The largest cytosolic region forms the binding site for AdoHcy and is composed of an extension of M8, a structurally ordered M6-M7 connector, and a short cap helix near the C terminus. The M6-M7 connector does not fully reach the luminal side but is stabilized by interactions with the M5-M6 connector.

### Active site spans cytosolic and membrane-exposed regions

The active site uniquely spans both cytosolic and membrane-exposed regions, indicating distinct entry routes for the cytosolic methyl donor AdoHcy and for prenylcysteine substrates associated with the ER membrane. The prenyl-binding cavity is approximately 22 A long and 6 A wide, extending from the cofactor pocket into the transmembrane region. Approximately two-thirds of the cavity is exposed to the cytosolic leaflet via a lateral crevice between helices M5 and M8. The cavity is lined primarily by aromatic amino acids (Tyr95, Met99, Phe102, Val124, Asn126, Tyr131, Trp215, Trp218, Tyr235, Phe242, Phe243) that markedly reduce enzyme activity when mutated.

### Substrate access through membrane crevice

The crevice between M5 and M8, accessible to the hydrophobic core of the membrane, provides a plausible route for prenyl entry by lateral diffusion. The M4-M5 connector, which is highly conserved and greatly diminishes catalytic activity when mutated, creates a hydrophilic depression within the membrane-embedded region that might induce a concomitant depression in proximal lipids of the bilayer, accommodating the upstream peptide portion of substrate proteins.

### Monobody inhibition mechanism

The MB-15 monobody binds ICMT adjacent to the active site, interacting with portions of M5, M8, and the M6-M7 loop. The monobody FG loop dips into the membrane region and presents a tryptophan residue (Trp80) that occupies part of the M5-M8 crevice. Hydrogen bonding between Ser77 of the monobody and Arg246 of ICMT contributes to inhibitory function; Arg246 is predicted to coordinate the C-terminal carboxylate of the prenylcysteine substrate. The monobody would prevent prenylated substrates from reaching the active site and/or block product release.

### Transition state stabilization mechanism

The C-terminal carboxylate of the prenylcysteine substrate forms hydrogen bonds with Arg173 and Arg246 that orient it for inline nucleophilic attack. The transition state is stabilized by additional interactions: a CH-O hydrogen bond with the side chain hydroxyl of Tyr212, a CH-O hydrogen bond with the backbone carbonyl oxygen of Asn185, and a CH-pi interaction with the aromatic face of Phe184. All proposed transition state stabilizing residues are perfectly conserved among ICMT enzymes.

### Comparison with prokaryotic MaMTase

Despite sharing only 14% sequence identity with the prokaryotic methyltransferase MaMTase, the AdoHcy binding sites are analogous. The cofactor-binding domain of ICMT (M6 through cap helix) shares a recognizable fold with MaMTase and with a prokaryotic integral membrane sterol reductase ([Masr1](/xray-mp-wiki/proteins/enzymes/masr1/)) that uses NADP+, suggesting this domain represents a structural motif for soluble cofactor binding to integral membrane enzymes. However, substrate-binding sites differ significantly in size, amino acid composition, and membrane exposure.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/sam/">SAM (S-Adenosyl-L-Methionine)</a> — Methyl donor cofactor for ICMT methylation reaction
- <a href="/xray-mp-wiki/reagents/detergents/dmng/">DMNG (Decyl Maltose Neopentyl Glycol)</a> — Detergent used for solubilization and purification of beetle ICMT
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid used in LCP crystallization and modeled in the active site cavity
- <a href="/xray-mp-wiki/reagents/additives/tcep/">TCEP (Tris(2-carboxyethyl)phosphine)</a> — Reducing agent used throughout purification and crystallization
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> — Buffer component (10 mM, pH 7.5) in purification and crystallization
- <a href="/xray-mp-wiki/reagents/additives/potassium-chloride/">Potassium Chloride (KCl)</a> — Salt component (150 mM) in purification buffers
- <a href="/xray-mp-wiki/reagents/additives/calcium-chloride/">Calcium Chloride (CaCl2)</a> — Added at 2 mM in lysis and purification buffers
- <a href="/xray-mp-wiki/proteins/enzymes/ma-icmt/">Ma-ICMT (Isoprenylcysteine Carboxyl Methyltransferase from Methanosarcina acetivorans)</a> — Prokaryotic ortholog with analogous cofactor-binding domain but different substrate access architecture
- <a href="/xray-mp-wiki/reagents/cofactors/s-adenosyl-l-homocysteine/">S Adenosyl L Homocysteine</a> — Referenced in the context of S Adenosyl L Homocysteine
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> — Referenced in the context of Tris Hcl
