---
title: "Human KDEL Receptor"
created: 2026-05-26
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2012.05.064]
verified: false
---

# Human KDEL Receptor

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


## Overview

The human KDEL receptor is a seven-pass transmembrane receptor that retrieves escaped endoplasmic reticulum (ER) resident proteins from the Golgi apparatus by recognizing the C-terminal KDEL (Lys-Asp-Glu-Leu) retrieval signal. This paper presents the first crystal structure of the human KDEL receptor in complex with a KDEL peptide, solved at 3.0 A resolution using the [lipidic cubic phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) method. The structure reveals the molecular basis for KDEL peptide recognition and provides insights into the receptor's role in retrograde transport and pH-dependent ligand binding.

## Publications

### doi/10.1016##j.jmb.2012.05.064

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3jmd">3JMD</a></td>
      <td>3.0 A</td>
      <td>P212121</td>
      <td>Human KDEL receptor (seven transmembrane domain construct with truncated N- and C-terminal extensions, expressed in Sf9 insect cells)</td>
      <td>KDEL peptide</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression system)
- **Construct**: Human KDEL receptor with truncated N- and C-terminal cytoplasmic tails, containing only the seven transmembrane domain and extracellular loops

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
      <td>Cell lysis and membrane preparation</td>
      <td>Cell lysis and membrane fractionation</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Sf9 insect cells infected with baculovirus expressing the human KDEL receptor construct were harvested and homogenized. Crude membrane fraction was isolated by differential ultracentrifugation.</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>-- + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (N-Dodecyl-beta-D-maltoside) at 1% (w/w)</td>
      <td>Membranes solubilized in buffer containing 1% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> to extract the seven-pass transmembrane KDEL receptor into detergent micelles.</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> resin</td>
      <td>Buffer containing <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> for elution + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>His-tag affinity purification of the KDEL receptor from the solubilized membrane fraction. The receptor was eluted with <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>-containing buffer while maintaining <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> to keep the protein soluble.</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> column</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> (pH 7.5), 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Final purification and buffer exchange. The KDEL receptor was concentrated to approximately 10 mg/ml for crystallization. The protein eluted as a monodisperse peak indicating proper folding and detergent micelle stability.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>KDEL receptor at 10 mg/ml in 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES Buffer</a> (pH 7.5), 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>, mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">monoolein</a> lipid at a 1:1.5 protein-to-lipid ratio</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Crystals appeared within 1-2 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals were flash-cooled in liquid nitrogen without additional cryoprotectant (LCP matrix provides inherent cryoprotection)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew as thin plates and diffracted to 3.0 A resolution. The structure was solved by molecular replacement. The acidic pH of the reservoir (pH 4.6) mimics the acidic pH of the Golgi apparatus where the KDEL receptor binds its ligand. Space group P212121, one molecule in the asymmetric unit.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Molecular basis for KDEL peptide recognition

The crystal structure reveals a deep binding pocket formed by the extracellular loops and the upper portion of the transmembrane helices of the KDEL receptor. The KDEL peptide binds in an extended conformation within this pocket, with key hydrogen bonds formed between the receptor and the conserved Asp and Glu side chains of the KDEL motif. The Lys residue at the N-terminus of the KDEL peptide makes ionic interactions with a cluster of acidic residues on the receptor surface. This binding mode explains the high specificity of the KDEL receptor for the KDEL retrieval signal and its ability to discriminate against other C-terminal tetrapeptides.

### pH-dependent ligand binding mechanism

The structure was solved at acidic pH (4.6), which corresponds to the pH of the cis-Golgi network where the KDEL receptor retrieves escaped ER proteins. The acidic environment promotes protonation of key histidine and glutamate residues in the binding pocket, strengthening the interaction with the KDEL peptide. Upon delivery of the cargo to the ER at neutral pH (approximately 7.2), deprotonation of these residues triggers ligand release, completing the retrieval cycle. This pH-dependent binding mechanism is essential for the receptor''s function in retrograde transport.

### Seven-pass transmembrane topology and comparison to other receptors

The KDEL receptor adopts a seven-pass transmembrane topology, which is distinct from the canonical seven-transmembrane G protein-coupled receptor (GPCR) fold. The transmembrane helices are arranged in a bundle with the ligand-binding pocket oriented toward the extracellular side, consistent with its role in retrieving luminal ER proteins. Despite the topological differences from class A GPCRs, the KDEL receptor shares a similar overall architecture with other seven-pass membrane proteins, suggesting convergent evolution of ligand-binding mechanisms in membrane receptors. The structure provides a structural framework for understanding the [ER retrieval mechanism](/xray-mp-wiki/concepts/signaling-receptors/er-retrieval-mechanism/) that maintains ER protein localization.


## Cross-References

- <a href="/xray-mp-wiki/concepts/signaling-receptors/er-retrieval-mechanism/">ER Retrieval Mechanism</a> — The KDEL receptor is the central receptor in the ER retrieval mechanism that maintains ER resident protein localization
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/">Membrane Mimetics and Structural Biology</a> — The KDEL receptor was solubilized and crystallized using detergent micelles and lipidic cubic phase, key membrane mimetic techniques
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM (N-Dodecyl-beta-D-maltoside)</a> — Primary solubilization detergent (1%) used for KDEL receptor membrane extraction and purification
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid used as the cubic phase matrix for LCP crystallization of the KDEL receptor
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> — Crystallization precipitant (20-30% PEG 400) used in the LCP crystallization reservoir
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Primary buffer (20 mM, pH 7.5) used in KDEL receptor purification
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA Agarose Resin</a> — Used for His-tag affinity purification of the KDEL receptor
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Crystallization method used for the KDEL receptor; LCP is particularly well-suited for seven-pass transmembrane proteins
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Used for final purification and buffer exchange of the KDEL receptor
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Ni-NTA affinity chromatography used for initial purification of the His-tagged KDEL receptor
