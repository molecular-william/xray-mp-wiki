---
title: "Turkey Beta1-Adrenergic Receptor M23"
created: 2026-05-26
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.jmb.2012.01.032, doi/10.1038##NATURE09746]
verified: regex
uniprot_id: P07550
---

# Turkey Beta1-Adrenergic Receptor M23

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P07550">UniProt: P07550</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The turkey beta1-adrenergic receptor (beta1AR) is a class A G protein-coupled receptor that mediates sympathetic nervous system responses including increased heart rate and contractility. The thermostabilized mutant beta1AR-M23, incorporating a 25-60 helix insertion, 292-303 deletion, point mutations, and a [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) fusion on the third intracellular loop, was crystallized using the [lipidic cubic phase](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/) method. Crystal structures of both the apo form at 2.9 A (PDB: 4LDE) and a complex with the antagonist [carvedilol](/xray-mp-wiki/reagents/ligands/carvedilol/) at 3.0 A (PDB: 4LDF) were solved, representing the first GPCR structures without a bound G-protein or Fab fragment.

## Publications

### doi/10.1016##j.jmb.2012.01.032

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4lde">4LDE</a></td>
      <td>2.9</td>
      <td>P 21 21 21</td>
      <td>Turkey beta1AR-M23 with BRIL fusion on ICL3</td>
      <td>None (apo form)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ldf">4LDF</a></td>
      <td>3.0</td>
      <td>P 21 21 21</td>
      <td>Turkey beta1AR-M23 with BRIL fusion on ICL3</td>
      <td>Carvedilol</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression vector system)
- **Construct**: Turkey beta1AR-M23 thermostabilized mutant with His6-tag for purification. The construct includes a 25-60 helix insertion, 292-303 deletion, point mutations (F88A, T89A, T90A, F92A, F194A, F198A), and a BRIL fusion on the third intracellular loop.

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
      <td>Cell culture and membrane preparation</td>
      <td>Sf9 cells were infected with baculovirus expressing beta1AR-M23 and harvested 48 hours post-infection. Cell membranes were prepared by homogenization and ultracentrifugation.</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Membranes were solubilized in 50 mM Tris-HCl pH 7.5, 150 mM NaCl, 10 mM MgCl2, 1 mM EDTA, 10% glycerol, and 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-dodecyl-beta-D-maltopyranoside (DDM)</a> for 1 hour at 4 degrees Celsius.</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a> using <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a> agarose](/xray-mp-wiki/reagents/additives/nickel-nta/) resin</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> agarose</td>
      <td>50 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Column was washed with buffer containing 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> and eluted with 250 mM imidazole.</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a> on a <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> column</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>20 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluted fractions containing monodisperse protein were pooled and concentrated.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified beta1AR-M23 at approximately 20 mg/mL in 20 mM Tris-HCl pH 7.5, 150 mM NaCl, 0.05% DDM. For the <a href="/xray-mp-wiki/reagents/ligands/carvedilol/">Carvedilol</a> complex, the receptor was incubated with 100 microM <a href="/xray-mp-wiki/reagents/ligands/carvedilol/">Carvedilol</a> for 30 minutes prior to mixing with the lipid matrix.</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 degrees Celsius</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Crystals appeared within 1-2 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals were flash-cooled in liquid nitrogen directly from the reservoir solution (no additional cryoprotectant was needed).</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Both apo and <a href="/xray-mp-wiki/reagents/ligands/carvedilol/">Carvedilol</a>-bound structures were obtained under identical crystallization conditions. The <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> lipid matrix was mixed with protein sample at a 1:1 ratio before dispensing into reservoir drops via the LCP robot. X-ray diffraction data were collected at beamline 23-ID-B at APS. The apo structure (4LDE) was solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> at 2.9 A resolution. The <a href="/xray-mp-wiki/reagents/ligands/carvedilol/">Carvedilol</a>-bound structure (4LDF) was solved at 3.0 A resolution by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using the apo structure as a search model.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4lde">4LDE</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDD</span><span class="topo-inside">DAENLYFQGNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">GETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYAADEV</span><span class="topo-membrane">WVVGMGIVMSLIVLAIVFGNVLVITA</span><span class="topo-outside">IAKFERLQTVTNY</span><span class="topo-membrane">FITSLACADLVMGLAVVPFGA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-membrane">AHIL</span><span class="topo-inside">TKTWTFGNF</span><span class="topo-membrane">WCEFWTSIDVLCVTASIETLCVIAV</span><span class="topo-outside">DRYFAITSPFKYQSLLTKNKA</span><span class="topo-membrane">RVIILMVWIVSGLTSFLPIQMHWYR</span><span class="topo-inside">ATH</span><span class="topo-unknown">QEAINCYA</span><span class="topo-inside">EETCCD</span><span class="topo-membrane">FFTNQAYAIASSIVSFYVP</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460         </span>
<span class="topo-line"><span class="topo-membrane">LVIMVFVYS</span><span class="topo-outside">RVFQEAKRQLQ</span><span class="topo-unknown">KID</span><span class="topo-outside">KFALKEHKALK</span><span class="topo-membrane">TLGIIMGTFTLCWLPFFIVNIVHVIQ</span><span class="topo-inside">DNL</span><span class="topo-membrane">IRKEVYILLNWIGYVNSGFNPLIYC</span><span class="topo-outside">RS</span><span class="topo-unknown">PDFRIAFQELL</span><span class="topo-outside">CL</span><span class="topo-unknown">RRSSLK</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>6</td>
      <td>852</td>
      <td>857</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>180</td>
      <td>858</td>
      <td>1031</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>206</td>
      <td>1032</td>
      <td>1057</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>219</td>
      <td>1058</td>
      <td>1070</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>244</td>
      <td>1071</td>
      <td>1095</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>253</td>
      <td>1096</td>
      <td>1104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>254</td>
      <td>278</td>
      <td>1105</td>
      <td>1129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>279</td>
      <td>299</td>
      <td>1130</td>
      <td>1150</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>324</td>
      <td>1151</td>
      <td>1175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>327</td>
      <td>1176</td>
      <td>1178</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>328</td>
      <td>335</td>
      <td>1179</td>
      <td>1186</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>336</td>
      <td>341</td>
      <td>1187</td>
      <td>1192</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>342</td>
      <td>369</td>
      <td>1193</td>
      <td>1220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>370</td>
      <td>380</td>
      <td>1221</td>
      <td>1231</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>381</td>
      <td>383</td>
      <td>1232</td>
      <td>1234</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>384</td>
      <td>394</td>
      <td>1263</td>
      <td>1273</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>395</td>
      <td>420</td>
      <td>1274</td>
      <td>1299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>423</td>
      <td>1300</td>
      <td>1302</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>424</td>
      <td>448</td>
      <td>1303</td>
      <td>1327</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>449</td>
      <td>450</td>
      <td>1328</td>
      <td>1329</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>451</td>
      <td>461</td>
      <td>1330</td>
      <td>1340</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>462</td>
      <td>463</td>
      <td>1341</td>
      <td>1342</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>464</td>
      <td>469</td>
      <td>1343</td>
      <td>1348</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##NATURE09746

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/iso327">ISO327</a></td>
      <td>2.85</td>
      <td>P21</td>
      <td>Turkey beta1AR-M23 with carmoterol</td>
      <td>Isoprenaline</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/car7">CAR7</a></td>
      <td>2.6</td>
      <td>P21</td>
      <td>Turkey beta1AR-M23 with carmoterol</td>
      <td>Carmoterol</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/dob92">DOB92</a></td>
      <td>2.5</td>
      <td>P21</td>
      <td>Turkey beta1AR-M23 with dobutamine</td>
      <td>Dobutamine (R-isomer)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/dob102">DOB102</a></td>
      <td>2.6</td>
      <td>P21</td>
      <td>Turkey beta1AR-M23 with dobutamine</td>
      <td>Dobutamine (R-isomer)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/sal109">SAL109</a></td>
      <td>3.05</td>
      <td>P21</td>
      <td>Turkey beta1AR-M23 with salbutamol</td>
      <td>Salbutamol (R-isomer)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (baculovirus expression vector system)
- **Construct**: Turkey beta1AR-M23 thermostabilized mutant with His6-tag for purification. The construct includes a 25-60 helix insertion, 292-303 deletion, point mutations (F88A, T89A, T90A, F92A, F194A, F198A), and a BRIL fusion on the third intracellular loop.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified turkey beta1AR-M23 at 14.5-16.0 mg/ml in varying buffer conditions. CHS added from a 10 mg/ml stock in 2% HEGA-10 immediately prior to crystallization.</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Varied by ligand: <a href="/xray-mp-wiki/reagents/ligands/salbutamol/">Salbutamol</a> (sal109) - 28% PEG 400 in <a href="/xray-mp-wiki/reagents/buffers/bicine/">Bicine</a> pH 9.0; <a href="/xray-mp-wiki/reagents/ligands/isoprenaline/">Isoprenaline</a> (iso327) - 28% PEG 600 in <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>-HCl pH 8.5; <a href="/xray-mp-wiki/reagents/ligands/carmoterol/">Carmoterol</a> (car7) - 26% PEG 600 in <a href="/xray-mp-wiki/reagents/buffers/bicine/">Bicine</a> pH 9.0; <a href="/xray-mp-wiki/reagents/ligands/dobutamine/">Dobutamine</a> (dob92) - 25% PEG 600 in <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>-HCl pH 8.5; <a href="/xray-mp-wiki/reagents/ligands/dobutamine/">Dobutamine</a> (dob102) - 25% PEG 600 in <a href="/xray-mp-wiki/reagents/buffers/bicine/">Bicine</a> pH 9.0</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>PEG 600 at 55% used as cryoprotectant</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>All structures crystallized in space group P21 with two monomers per asymmetric unit. The two monomers make similar crystal contacts, but crystal contacts at the top of helix 7 differ between monomers A and B. This causes different orientations of the methylphenoxy group in <a href="/xray-mp-wiki/reagents/ligands/carmoterol/">Carmoterol</a> and the methylhydroxyl substituent in <a href="/xray-mp-wiki/reagents/ligands/salbutamol/">Salbutamol</a> between the two monomers. CHS concentrations ranged from 0.45 to 1.9 mg/ml depending on the ligand.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified turkey beta1AR-M23 at 16.5 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>28% PEG 400, <a href="/xray-mp-wiki/reagents/buffers/bicine/">Bicine</a> pH 9.0</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>60% PEG 400</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallization of beta1AR-M23 with <a href="/xray-mp-wiki/reagents/ligands/salbutamol/">Salbutamol</a> (sal109). Racemic (R,S)-<a href="/xray-mp-wiki/reagents/ligands/salbutamol/">Salbutamol</a> was used in crystallization, but the (R)-isomer was found in the resulting structure. Wilson B factor: 70.6 A^2. Resolution range: 38.6-3.05 A. Rmerge: 0.119 (0.509).</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Antagonist binding pocket architecture

The structure of beta1AR-M23 in complex with carvedilol reveals the molecular details of antagonist binding in a beta1-adrenergic receptor. Carvedilol binds deep within the transmembrane bundle, with its carbazole moiety making hydrophobic contacts with transmembrane helices 3, 5, 6, and 7, while the cyclohexyl group interacts with helix 3. The hydroxyl groups of carvedilol form hydrogen bonds with Ser193(5.42) and Ser197(5.46) in transmembrane helix 5, a conserved feature of catecholamine binding in beta-adrenergic receptors.

### Thermostabilization mechanism

The beta1AR-M23 mutant shows dramatically improved thermal stability compared to wild-type turkey beta1AR. The melting temperature increases from approximately 40 degrees Celsius for wild-type to over 55 degrees Celsius for the M23 mutant. The stabilizing mutations are distributed throughout the receptor, with the 25-60 helix filling a cavity in the intracellular region and the BRIL fusion providing additional structural rigidity to the intracellular loops.

### GPCR conformational state

The apo structure of beta1AR-M23 reveals a receptor conformation that is intermediate between the inactive and active states. The intracellular surface shows partial rearrangement of the ionic lock (Arg3.50-Glu6.30 interaction), suggesting that the thermostabilization mutations may bias the receptor toward a specific conformational ensemble. This intermediate state may explain why beta1AR-M23 can crystallize without a bound G-protein or Fab fragment.

### BRIL fusion strategy

The [BRIL](/xray-mp-wiki/reagents/protein-tags/bril/) (brucellae lysozyme) fusion protein was found to be an effective strategy for GPCR crystallization. BRIL is a small, thermostable protein that fuses to the ICL3 without disrupting the receptor's structural integrity or ligand binding. The BRIL fusion replaces flexible ICL3 loops with a rigid alpha-helical domain, reducing conformational heterogeneity and promoting crystal contacts.

### Comparison with other GPCR structures

The turkey beta1AR-M23 structure shares the canonical seven-transmembrane helix architecture with other class A GPCR structures, including bovine rhodopsin, the human adenosine A2A receptor, and the human beta2-adrenergic receptor. The carvedilol binding mode is consistent with the conserved catecholamine-binding pharmacophore observed in other beta-adrenergic receptor structures.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/">Human Adenosine A2A Receptor (A2AR)</a> — Another class A GPCR crystallized using the LCP method by the same group (RCSB)
- <a href="/xray-mp-wiki/proteins/gpcr/a2a-psb1-bril/">A2A-PSB1-bRIL</a> — Related thermostabilized GPCR construct using the BRIL fusion strategy
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid used as the matrix for LCP crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">N-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Detergent used for solubilization and all purification steps
- <a href="/xray-mp-wiki/reagents/ligands/carvedilol/">Carvedilol</a> — Antagonist ligand co-crystallized with beta1AR-M23 in structure 4LDF
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Crystallization method used for both apo and ligand-bound structures
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Final purification step to obtain monodisperse protein sample
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Ni-NTA affinity chromatography used for initial purification of His6-tagged receptor
