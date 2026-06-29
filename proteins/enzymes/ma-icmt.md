---
title: "Isoprenylcysteine Carboxyl Methyltransferase (ICMT) from Methanosarcina acetivorans"
created: 2026-05-26
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.molcel.2011.10.020]
verified: false
---

# Isoprenylcysteine Carboxyl Methyltransferase (ICMT) from Methanosarcina acetivorans

## Overview

ICMT (isoprenylcysteine carboxyl methyltransferase) is an integral membrane methyltransferase that catalyzes the final step of CAAX processing — the carboxyl methylation of prenylated cysteine residues in proteins such as Ras and Rho GTPases. The crystal structure of a prokaryotic ortholog from Methanosarcina acetivorans (Ma-ICMT) reveals a unique architecture with five transmembrane helices and a cytosolic cofactor-binding pocket, with a substrate access tunnel linking the catalytic site to the inner membrane. This structure explains how an integral membrane methyltransferase achieves recognition of both a hydrophilic cofactor ([SAM](/xray-mp-wiki/reagents/cofactors/sam/)) and a lipophilic prenyl substrate within the lipid bilayer.

## Publications

### doi/10.1016##j.molcel.2011.10.020

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4a2n">4A2N</a></td>
      <td>3.4 A</td>
      <td>P6222</td>
      <td>Ma-ICMT (MA2698 from Methanosarcina acetivorans) in complex with SAH cofactor</td>
      <td>SAH (<a href="/xray-mp-wiki/reagents/cofactors/s-adenosyl-l-homocysteine/">S-Adenosyl-L-Homocysteine (AdoHcy)</a>), endogenous C9 alkyl chain lipid</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli strain C41(DE3)
- **Construct**: Ma-ICMT (MA2698) fused with TEV-cleavable C-terminal GFP-His7 tag. Cloned into pTriEX-based plasmid (pOPIN-GFP).

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
      <td>Protein expression in E. coli</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Ma-ICMT-GFP-His7 expressed in E. coli strain C41(DE3) at 20 degrees C overnight</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin (His-tag affinity)</td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Ma-ICMT-GFP-His7 purified with <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> using the C-terminal His7 tag</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion-Exchange Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion-Exchange Chromatography</a></td>
      <td>Ion exchange resin</td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Ion exchange purification step to further purify Ma-ICMT</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>Size-exclusion resin</td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Final polishing step using size-exclusion chromatography</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>8 mg/ml Ma-ICMT in buffer (20 mM <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> [pH 6.5], 200 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a>, 10% [v/v] <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, and 0.024% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>5 mM SAH (<a href="/xray-mp-wiki/reagents/cofactors/s-adenosyl-l-homocysteine/">S-Adenosyl-L-Homocysteine (AdoHcy)</a>) and 0.5 mg/ml <a href="/xray-mp-wiki/reagents/lipids/e-coli-polar-lipids/">E. coli Polar Lipids</a> (Avanti Polar Lipids)</td>
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
      <td>Crystals were obtained in complex with SAH (Sigma) but not in its absence, suggesting that cofactor influences the protein conformation and is required for conformational homogeneity necessary for crystallization. Two derivatives were collected: EMTS (ethylmercurithiosalicylate) at DLS beam line I02, and gold derivative (KAu(CN)2) at DLS beam line I03. Structure determined from SAD phases obtained from EMTS and gold derivatives and multicrystal averaging.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4a2n">4A2N</a> — Chain B (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-inside">MNEN</span><span class="topo-membrane">LWKICFIVMFIIWVFVRK</span><span class="topo-outside">VYGTRAMKNKSKKKVRPNFEKS</span><span class="topo-membrane">LVFLNFIGMVFLPLTA</span></span>
<span class="topo-line"><span class="topo-membrane">VFSSYL</span><span class="topo-inside">DSFNINLPDS</span><span class="topo-membrane">IRLFALIVTFLNIGLFT</span><span class="topo-outside">KIHKDLGNNWSAILEIKDGHKLVKEGI</span></span>
<span class="topo-line"><span class="topo-outside">YKNIRHPM</span><span class="topo-membrane">YAHLWLWVITQGIILSN</span><span class="topo-inside">W</span><span class="topo-membrane">VVLIFGIVAWAILYFI</span><span class="topo-outside">RVPKEEELLIEEFGDEYI</span></span>
<span class="topo-line"><span class="topo-outside">EYMGKTGRLFPK</span><span class="topo-unknown">VV</span></span>
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
      <td>1</td>
      <td>4</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>22</td>
      <td>5</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>44</td>
      <td>23</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>66</td>
      <td>45</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>76</td>
      <td>67</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>93</td>
      <td>77</td>
      <td>93</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>94</td>
      <td>128</td>
      <td>94</td>
      <td>128</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>129</td>
      <td>145</td>
      <td>129</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>146</td>
      <td>146</td>
      <td>146</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>147</td>
      <td>162</td>
      <td>147</td>
      <td>162</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>192</td>
      <td>163</td>
      <td>192</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>193</td>
      <td>194</td>
      <td>193</td>
      <td>194</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Unique integral membrane methyltransferase architecture

Unlike all known aqueous methyltransferases, ICMT is an integral membrane protein with five transmembrane helices (H1 to H5) and a short C-terminal cytosolic alpha helix (H6). The cofactor-binding pocket is completely enclosed within a highly conserved C-terminal catalytic subdomain of approximately 90 amino acids, and a substrate access tunnel connects the catalytic site to the inner membrane. The tunnel features a hydrophobic upper region within the membrane (for prenyl lipid access) and a hydrophilic lower region in the cytosol (for the polar protein substrate C terminus).

### Substrate access tunnel architecture and lipid binding

A substrate access tunnel located between helices H1 and H2 provides the only access to the [SAM](/xray-mp-wiki/reagents/cofactors/sam/) cofactor, specifically the catalytic methyl group. Strong and continuous rod-like electron density was interpreted as a C9 alkyl chain derived from endogenous lipid bound within Ma-ICMT, suggesting it might mimic a substrate prenyl lipid. The hydrophobic upper tunnel region is positioned within the inner membrane, whereas the hydrophilic lower regions open into the cytosol.

### Catalytic mechanism and substrate positioning

The guanidinium side chain of Arg163 (invariant residue of the M2 motif) is positioned at the inner entrance of the tunnel to form electrostatic interactions with the substrate carboxylate group, aligning it for direct in-line nucleophilic attack onto the reactive methyl group of [SAM](/xray-mp-wiki/reagents/cofactors/sam/). Mutation of Arg163 abolished carboxyl methyltransferase activity. Arg163 is absent from [Phosphatidylethanolamine](/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/) methyltransferase, an enzyme that methylates a positively charged amine group rather than a carboxylate.

### Conserved cofactor-binding residues and catalytic mechanism

The cofactor-binding cavity (volume of 1291 A^3) is generated from the L3 loop and cytosolic segments of H5 and H6. Conserved residues His126 and Glu167 (charge-neutralizing residues from M1 and M2 motifs) are essential for cofactor binding — their mutation completely eliminated methylation activity. Residues interacting with the adenine ring (His113) or indirectly contacting cofactor (Tyr129) impaired catalytic activity by approximately 75%. The cofactor adopts a closed conformation most similar to class IV methyltransferases.

### Substrate specificity toward prenyl lipids

Ma-ICMT displayed robust catalytic activity toward the AFC analog S-farnesylthioacetic acid (FTA), at a 6-fold lower rate than AFC-catalyzed methylation by yeast ICMT, and some substantially weaker activity toward AFC. No activity was detected toward a farnesylated peptide substrate or the straight-chain fatty acid palmitic acid, suggesting the enzyme may not recognize straight-chain alkyl lipids. This mirrors the much lower affinity of rat ICMT toward S-alkyl peptide derivatives compared with S-prenyl peptides.

### ICMT as an anticancer therapeutic target

ICMT is essential for proper subcellular localization of CAAX proteins including Ras and Rho GTPases, which regulate diverse cellular processes. Carboxyl methylation augments the hydrophobicity of the prenyl membrane anchor, and pharmacological inhibition of ICMT disrupts Rho-mediated cell migration and adhesion. ICMT inhibition negatively regulates Ras and Rho signaling, implicating ICMT as an anticancer therapeutic target. Existing substrate-competitive ICMT inhibitors are lipophilic and compromise bioavailability; the Ma-ICMT structure provides a framework for rational design of [SAM](/xray-mp-wiki/reagents/cofactors/sam/) antagonists as an alternative approach.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/sam/">SAM (S-Adenosyl-L-Methionine)</a> — Essential cofactor for ICMT methyltransferase activity, binds in the enclosed cofactor-binding pocket
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM (N-Dodecyl-beta-D-maltoside)</a> — Detergent used for solubilization and purification of Ma-ICMT
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Included in purification and crystallization buffer (10% v/v)
- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES (2-(N-morpholino)ethanesulfonic acid)</a> — Buffer used in crystallization (20 mM MES, pH 6.5)
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride (NaCl)</a> — Salt component in crystallization buffer (200 mM NaCl)
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Agarose Resin</a> — Used for His-tag affinity purification of Ma-ICMT-GFP-His7
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200 Increase SEC Resin</a> — Size-exclusion chromatography resin used for final purification step
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/ion-exchange-chromatography/">Ion-Exchange Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/cofactors/s-adenosyl-l-homocysteine/">S-Adenosyl-L-Homocysteine (AdoHcy)</a> — Related ligand or cofactor
