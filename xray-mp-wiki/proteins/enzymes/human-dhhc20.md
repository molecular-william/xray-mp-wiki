---
title: "Human DHHC20 Palmitoyltransferase"
created: 2026-06-10
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aao6326]
verified: regex
uniprot_id: Q5W0Z9
---

# Human DHHC20 Palmitoyltransferase

<div class="expr-badges"><span class="expr-badge expr-p-pastoris">P. pastoris</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q5W0Z9">UniProt: Q5W0Z9</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Human DHHC20 (hDHHC20) is an integral membrane S-acyltransferase of the DHHC
family that catalyzes protein palmitoylation — the attachment of a palmitoyl
group to cysteine residues via a thioester linkage. It is a Golgi-resident
enzyme with four transmembrane helices adopting a tepee-like organization.
The active site, containing the signature Asp-His-His-Cys (DHHC) motif,
resides at the membrane-cytosol interface, explaining why membrane-proximal
cysteines are preferred substrates. The 2.44 A crystal structure of hDHHC20
and a 2.54 A structure of the zfDHHS15 mutant revealed the acyl-chain binding
cavity formed by the transmembrane domain, providing insights into acyl-CoA
recognition and chain-length selectivity. DHHC20 overexpression causes
cellular transformation and has been proposed as a therapeutic target for
cancers resistant to EGFR-targeted therapy.


## Publications

### doi/10.1126##science.aao6326

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6bml">6BML</a></td>
      <td>2.44</td>
      <td>—</td>
      <td>hDHHC20 (residues 5-299), reductively methylated, hexagonal P63 form</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6bml">6BML</a></td>
      <td>2.44</td>
      <td>—</td>
      <td>hDHHC20 C263A mutant with 2-bromopalmitate (2-BP) covalent inhibitor</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (yeast)
- **Construct**: N-terminal His10-GFP-PreScission-tagged hDHHC20
- **Notes**: Codon-optimized hDHHC20 cloned into pPICZ-C vector; expressed in Pichia pastoris SDM1163 cells

**Purification:**

- **Expression system**: Pichia pastoris
- **Expression construct**: N-terminal His10-GFP tag with PreScission cleavage site
- **Tag info**: His10-GFP, removed by [PreScission Protease](/xray-mp-wiki/reagents/additives/pre-scission-protease/)

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
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> resin (cobalt affinity)</td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 150 mM NaCl, 2 mM beta-ME, 2 mM TCEP + 1 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Wash with 25 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, elute with 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; gravity flow at ambient temperature</td>
    </tr>
    <tr>
      <td>SEC / Tag removal</td>
      <td>PreScission cleavage overnight at 4C, then <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase SEC</td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 150 mM NaCl, 2 mM TCEP + 0.5 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>GFP tag and <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> removed by SEC; fractions pooled and concentrated using 50 kDa MWCO Amicon</td>
    </tr>
    <tr>
      <td>Reductive methylation (for crystallization)</td>
      <td>Formaldehyde and DMAB complex treatment</td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 250 mM NaCl, 2 mM TCEP, 0.5 mM <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Methylation quenched with Tris HCl pH 8.0 and <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>; then SEC on <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase</td>
    </tr>
  </tbody>
</table>
**Final sample**: Concentrated in SEC buffer containing 0.05 mg/mL [POPC](/xray-mp-wiki/reagents/lipids/popc/):[POPG](/xray-mp-wiki/reagents/lipids/popg/):POPA (3:1:1) lipids and 0.5 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>1:1 (v/v)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3.5 months</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Directly frozen in liquid N2</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Hexagonal crystals; data collected at APS NE-CAT 24ID-C; microbatch format with 100 nl LCP bolus and ~3.6 ul crystallization solution</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>1:1 (v/v)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1.5 months</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>2-BP modified C263A hDHHC20 crystals; data collected at APS GM/CA-CAT 23ID-D</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>zfDHHS15 (zebrafish DHHC15 C153S mutant)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>50 mM MES pH 6.5, 50 mM NaH2PO4, 30.3% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 300, 50 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a>, 2.5% 2,5-Hexanediol</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3 months</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>P21 crystal form; data collected at APS GM/CA-CAT 23ID-B</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bml">6BML</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">TLWRCCQRVVGWV</span><span class="topo-membrane">PVLFITFVVVWSYYAYVVELCVFTIF</span><span class="topo-outside">GNEEN</span><span class="topo-membrane">GKTVVYLVAFHLFFVMFVWSYW</span><span class="topo-inside">MTIFTSPASPSKEFYLSNSEKERYEKEFSQERQQEILRRAARALPIYTTSASKT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IRYCEKCQLIKPDRAHHCSACDSCILKMDHHCPWVNNCVGFSNYKFFLL</span><span class="topo-membrane">FLLYSLLYCLFVAATVLEYFIKFWT</span><span class="topo-outside">NELTD</span><span class="topo-membrane">TRAKFHVLFLFFVSAMFFISVLS</span><span class="topo-inside">LFSYHCWLVGKNRTTIES</span></span>
<span class="topo-ruler">       250       260       270       280       290     </span>
<span class="topo-line"><span class="topo-inside">FRAPTFSYGPDGNGFSLGASKNWRQVFGDEKKYWLLPIFSSLGDGCSFPTRL</span><span class="topo-unknown">VGM</span></span>
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
      <td>13</td>
      <td>5</td>
      <td>17</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>39</td>
      <td>18</td>
      <td>43</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>44</td>
      <td>44</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>66</td>
      <td>49</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>169</td>
      <td>71</td>
      <td>173</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>194</td>
      <td>174</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>199</td>
      <td>199</td>
      <td>203</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>222</td>
      <td>204</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>292</td>
      <td>227</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6bml">6BML</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">TLWRCCQRVVGWV</span><span class="topo-membrane">PVLFITFVVVWSYYAYVVELCVFTIF</span><span class="topo-outside">GNEEN</span><span class="topo-membrane">GKTVVYLVAFHLFFVMFVWSYW</span><span class="topo-inside">MTIFTSPASPSKEFYLSNSEKERYEKEFSQERQQEILRRAARALPIYTTSASKT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">IRYCEKCQLIKPDRAHHCSACDSCILKMDHHCPWVNNCVGFSNYKFFLL</span><span class="topo-membrane">FLLYSLLYCLFVAATVLEYFIKFWT</span><span class="topo-outside">NELTD</span><span class="topo-membrane">TRAKFHVLFLFFVSAMFFISVLS</span><span class="topo-inside">LFSYHCWLVGKNRTTIES</span></span>
<span class="topo-ruler">       250       260       270       280       290     </span>
<span class="topo-line"><span class="topo-inside">FRAPTFSYGPDGNGFSLGASKNWRQVFGDEKKYWLLPIFSSLGDGCSFPTRL</span><span class="topo-unknown">VGM</span></span>
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
      <td>13</td>
      <td>5</td>
      <td>17</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>39</td>
      <td>18</td>
      <td>43</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>40</td>
      <td>44</td>
      <td>44</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>66</td>
      <td>49</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>169</td>
      <td>71</td>
      <td>173</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>170</td>
      <td>194</td>
      <td>174</td>
      <td>198</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>199</td>
      <td>199</td>
      <td>203</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>222</td>
      <td>204</td>
      <td>226</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>223</td>
      <td>292</td>
      <td>227</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Active site at membrane-cytosol interface enables thioester-exchange chemistry

The DHHC active site is positioned at the membrane-aqueous interface, with
the catalytic cysteine (Cys156) protruding toward the membrane. The aspartic
acid (Asp154) and the first histidine (His154) of the DHHC motif form a
catalytic triad-like arrangement that activates the nucleophilic cysteine for
attack on the acyl-CoA thioester. The second histidine (His155) coordinates
a Zn2+ ion and positions the catalytic cysteine. This organization explains
why substrate cysteines must be membrane-proximal for palmitoylation.

### Acyl chain binding cavity and chain-length selectivity

The transmembrane domain forms a hydrophobic cavity where the acyl chain of
acyl-CoA inserts. Residues from all four TM helices line the cavity, with
Trp28, Trp158, Phe171, Phe174, and Leu227 making critical contacts. Mutation
of Tyr181 to alanine shifts preference from C16 (palmitoyl) toward C18
(stearoyl)-CoA, while S29F mutation increases short-chain preference. The
Tyr181-Ser29 pair closes off the cavity; breaking this interaction allows
longer acyl chains. This enabled engineering of mutants with altered
acyl-CoA selectivity.

### C-terminal domain with amphipathic helix and hydrophobic loop

The C-terminal domain contains a conserved amphipathic helix (alpha'2)
that contacts TM3 and TM4, providing local stability. A conserved TTXE
motif (Thr240, Thr241, Glu243) forms critical interactions with the active
site. The PaCCT motif, with highly conserved Phe259 and Asn266, forms a
packing core. A hydrophobic loop inserts into the lipid bilayer and forms
contacts with TM3 and TM2. Deletion of Trp267 (homologous to a residue
causing depilation in mice when deleted in DHHC21) results in negligible
catalytic activity.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/dhhc-palmitoyltransferase-family/">DHHC Palmitoyltransferase Family</a> — hDHHC20 is a member of the DHHC family of S-acyltransferases
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltoside (DDM)</a> — Used for purification and stabilization of hDHHC20 (1 mM in affinity, 0.5 mM in SEC)
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Used as LCP host lipid for crystallization of hDHHC20
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-Drop Vapor Diffusion</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/pre-scission-protease/">PreScission Protease</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
