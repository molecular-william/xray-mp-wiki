---
title: "Human Beta-2 Adrenergic Receptor (β2AR)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aaw8981, doi/10.1107##S2052252519013137]
verified: false
---

# Human Beta-2 Adrenergic Receptor (β2AR)

## Overview

The human beta-2 adrenergic receptor (β2AR) is a prototypic class A G-protein-coupled receptor that plays essential roles in cardiovascular and respiratory physiology, and is the therapeutic target of beta-blockers and beta-agonists. Multiple crystal structures have been determined using both synchrotron and X-ray free-electron laser (XFEL) sources. The active-state β2AR in complex with orthosteric agonist [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/), [Nanobody](/xray-mp-wiki/reagents/protein-tags/nanobody/) 6B9 (Nb6B9), and positive allosteric modulator Compound-6FA was determined at 3.2 A resolution (Liu et al., Science 2019, PDB 6N48). Using [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) (SFX) with lipidic sponge phase ([LSP](/xray-mp-wiki/concepts/membrane-mimetics/lipidic-sponge-phase/)) crystallization, eight room-temperature co-crystal structures with six different ligands were determined at 2.8-4.0 A resolution (Ishchenko et al., IUCrJ 2019), including previously unreported structures with [Carvedilol](/xray-mp-wiki/reagents/ligands/carvedilol/) and propranolol. The LSP-SFX approach enabled rapid determination of multiple GPCR co-crystal structures from submilligram quantities of protein.

## Publications

### doi/10.1126##science.aaw8981

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6n48">6N48</a></td>
      <td>3.2</td>
      <td>P212121</td>
      <td>T4L-β2AR fusion (N-terminal T4 lysozyme fused to human β2AR) expressed in insect cells; complex formed with orthosteric agonist <a href="/xray-mp-wiki/reagents/ligands/bi-167107/">BI-167107</a>, <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> 6B9 (Nb6G9), and positive allosteric modulator Cmpd-6FA; <a href="/xray-mp-wiki/reagents/ligands/bi-167107/">BI-167107</a> occupancy ensures active-state stabilization</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/bi-167107/">BI-167107</a> (orthosteric agonist), Cmpd-6FA (positive allosteric modulator), Nb6B9 (<a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nanobody</a> G-protein mimetic)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Insect cell expression system (Sf9, baculovirus)
- **Construct**: T4L-β2AR fusion protein; N-terminal T4 lysozyme fused to β2AR for crystallogenesis

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
      <td>Protein expression and purification</td>
      <td>Expression in insect cells; <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a>-β2AR purified in presence of agonist <a href="/xray-mp-wiki/reagents/ligands/bi-167107/">BI-167107</a></td>
      <td>--</td>
      <td>-- + --</td>
      <td>Expression and purification details are described in previous references (Rosenbaum et al., Nature 2011; Rasmussen et al., Nature 2011; Ring et al., Nature 2013). The <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a>-β2AR fusion maintains Cmpd-6 PAM activity.</td>
    </tr>
    <tr>
      <td>Complex formation</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a>-β2AR bound to <a href="/xray-mp-wiki/reagents/ligands/bi-167107/">BI-167107</a>, <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nb6B9</a>; Cmpd-6FA (3 mM) included in crystallization solution</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Cmpd-6FA (acetic acid derivative of Cmpd-6) was used at 3 mM (solubility limit) in crystallization condition. Cmpd-6FA has ~6-fold higher solubility than the parent Cmpd-6 and recapitulates its pharmacological properties.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion crystallization</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a>-β2AR-BI-167107-<a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nb6B9</a> complex with 3 mM Cmpd-6FA</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals were obtained of the active <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a>-β2AR bound to <a href="/xray-mp-wiki/reagents/ligands/bi-167107/">BI-167107</a> and <a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nb6B9</a> in a crystallization condition saturated with 3 mM of Cmpd-6FA. The structure was resolved to 3.2 A by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using the <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a>-β2AR-<a href="/xray-mp-wiki/reagents/protein-tags/nanobody/">Nb6B9</a> structure (PDB 4LDO) as the search model.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6n48">6N48</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">DYKDDD</span><span class="topo-inside">DAENLYFQGNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSEL</span></span>
<span class="topo-line"><span class="topo-inside">DKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQM</span></span>
<span class="topo-line"><span class="topo-inside">GETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYAADEV</span></span>
<span class="topo-line"><span class="topo-membrane">WVVGMGIVMSLIVLAIVFGNVLVIT</span><span class="topo-outside">AIAKFERLQTVTNYFI</span><span class="topo-membrane">TSLACADLVMGLAVVPFGA</span></span>
<span class="topo-line"><span class="topo-membrane">AHIL</span><span class="topo-inside">TKTWTFGNF</span><span class="topo-membrane">WCEFWTSIDVLCVTASIETLCV</span><span class="topo-outside">IAVDRYFAITSPFKYQSLLTKNKAR</span></span>
<span class="topo-line"><span class="topo-outside">VII</span><span class="topo-membrane">LMVWIVSGLTSFLPIQMHWYRA</span><span class="topo-inside">TH</span><span class="topo-unknown">QEAINCYA</span><span class="topo-inside">EETCCD</span><span class="topo-membrane">FFTNQAYAIASSIVSFYVP</span></span>
<span class="topo-line"><span class="topo-membrane">LVIMVF</span><span class="topo-outside">VYSRVFQEAKRQLQ</span><span class="topo-unknown">KID</span><span class="topo-outside">KFALKEHKALKTLG</span><span class="topo-membrane">IIMGTFTLCWLPFFIVNIVHVIQ</span></span>
<span class="topo-line"><span class="topo-inside">DNL</span><span class="topo-membrane">IRKEVYILLNWIGYVNSGFNPLI</span><span class="topo-outside">YCRS</span><span class="topo-unknown">PDFRIAFQEL</span><span class="topo-outside">LCL</span><span class="topo-unknown">RRSSLK</span></span>
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
      <td>180</td>
      <td>858</td>
      <td>1031</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>205</td>
      <td>1032</td>
      <td>1056</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>206</td>
      <td>221</td>
      <td>1057</td>
      <td>1072</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>244</td>
      <td>1073</td>
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
      <td>275</td>
      <td>1105</td>
      <td>1126</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>276</td>
      <td>303</td>
      <td>1127</td>
      <td>1154</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>325</td>
      <td>1155</td>
      <td>1176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>326</td>
      <td>327</td>
      <td>1177</td>
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
      <td>366</td>
      <td>1193</td>
      <td>1217</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>367</td>
      <td>380</td>
      <td>1218</td>
      <td>1231</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>1263</td>
      <td>1276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>420</td>
      <td>1277</td>
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
      <td>446</td>
      <td>1303</td>
      <td>1325</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>447</td>
      <td>450</td>
      <td>1326</td>
      <td>1329</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>451</td>
      <td>460</td>
      <td>1330</td>
      <td>1339</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>461</td>
      <td>463</td>
      <td>1340</td>
      <td>1342</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1107##S2052252519013137

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6prz">6PRZ</a></td>
      <td>2.9</td>
      <td>--</td>
      <td>T4L-β2AR fusion protein expressed in Sf9 insect cells; purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/CHS; crystallized in lipidic sponge phase (<a href="/xray-mp-wiki/concepts/membrane-mimetics/lipidic-sponge-phase/">LSP</a>) with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>/cholesterol/PEG 400; SFX data collection at SACLA; room temperature structure</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/bi-167107/">BI-167107</a> (high-affinity agonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ps0">6PS0</a></td>
      <td>3.2</td>
      <td>--</td>
      <td>T4L-β2AR as above; crystallized in <a href="/xray-mp-wiki/concepts/membrane-mimetics/lipidic-sponge-phase/">LSP</a> with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>/cholesterol/PEG 400; SFX data collection at SACLA</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/carazolol/">Carazolol</a> (inverse agonist, β-blocker)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ps1">6PS1</a></td>
      <td>3.4</td>
      <td>--</td>
      <td>T4L-β2AR as above; LSP-SFX</td>
      <td>Timolol (non-selective β-blocker antagonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ps2">6PS2</a></td>
      <td>3.2</td>
      <td>--</td>
      <td>T4L-β2AR as above; LSP-SFX</td>
      <td>ICI-118,551 (selective β2AR inverse agonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ps3">6PS3</a></td>
      <td>3.7</td>
      <td>--</td>
      <td>T4L-β2AR as above; LSP-SFX</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/carvedilol/">Carvedilol</a> (biased β-blocker, β-arrestin-biased agonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ps4">6PS4</a></td>
      <td>4.0</td>
      <td>--</td>
      <td>T4L-β2AR as above; LSP-SFX</td>
      <td>Propranolol (non-selective β-blocker antagonist)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ps5">6PS5</a></td>
      <td>2.8</td>
      <td>--</td>
      <td>T4L-β2AR as above; LSP-SFX; crystallized with <a href="/xray-mp-wiki/reagents/ligands/bi-167107/">BI-167107</a> and <a href="/xray-mp-wiki/reagents/ligands/carazolol/">Carazolol</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/bi-167107/">BI-167107</a> (competition with <a href="/xray-mp-wiki/reagents/ligands/carazolol/">Carazolol</a>)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ps6">6PS6</a></td>
      <td>2.8</td>
      <td>--</td>
      <td>T4L-β2AR as above; LSP-SFX</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/bi-167107/">BI-167107</a> (high resolution dataset)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Insect cell expression system (Sf9, baculovirus)
- **Construct**: T4L-β2AR fusion protein; N-terminal T4 lysozyme fused to β2AR for crystallogenesis

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
      <td>Expression in Sf9 insect cells</td>
      <td><a href="/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/">Baculovirus expression system</a></td>
      <td>--</td>
      <td>-- + --</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a>-β2AR fusion expressed in <a href="/xray-mp-wiki/methods/expression-systems/sf9-expression-system/">Sf9</a> cells; harvested 48 h post-infection</td>
    </tr>
    <tr>
      <td>Membrane preparation and solubilization</td>
      <td>Differential centrifugation; solubilization in 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Purified in presence of <a href="/xray-mp-wiki/reagents/ligands/alprenolol/">Alprenolol</a> to stabilize receptor</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> followed by alprenolol-Sepharose <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a>, alprenolol-Sepharose</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Final protein concentrated to ~30 mg/ml with 10 μM <a href="/xray-mp-wiki/reagents/ligands/alprenolol/">Alprenolol</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic sponge phase (<a href="/xray-mp-wiki/concepts/membrane-mimetics/lipidic-sponge-phase/">LSP</a>) crystallization for <a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/">SFX</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a>-β2AR at ~30 mg/ml in 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-4 days</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/concepts/membrane-mimetics/lipidic-sponge-phase/">LSP</a> prepared by mixing <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a>/<a href="/xray-mp-wiki/reagents/lipids/cholesterol/">cholesterol</a> with buffer containing <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 400 and sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a>. Protein solution mixed with lipid mixture using syringe mixer. Crystallization in 96-well glass sandwich plates. For each ligand, microcrystals grew within 2-4 days. <a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/">SFX</a> data collected at SACLA BL2, 10 keV, 10 μm beam, 50 mm detector distance. Data indexed with CrystFEL; structures solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using β2AR-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> (PDB 4LDO) as search model.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6prz">6PRZ</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDAMGQPGNGSAFLLAPNRSHAPDHDVTQQRDE</span><span class="topo-outside">VWVV</span><span class="topo-membrane">GM</span></span>
<span class="topo-line"><span class="topo-membrane">GIVMSLIVLAIVFGNVLVITAIA</span><span class="topo-inside">KFERLQTVTNY</span><span class="topo-membrane">FITSLACADLVMGLAVVPFGA</span><span class="topo-outside">AHILM</span></span>
<span class="topo-line"><span class="topo-outside">KMWTFGNFWCEF</span><span class="topo-membrane">WTSIDVLCVTASIWTLCVIAV</span><span class="topo-inside">DRYFAITSPFKYQSLLTKNKA</span><span class="topo-membrane">RVIILM</span></span>
<span class="topo-line"><span class="topo-membrane">VWIVSGLTSFLPIQ</span><span class="topo-outside">MHWYRATHQEAINCYAEETCCDFFTNQA</span><span class="topo-membrane">YAIASSIVSFYVPLVIMV</span></span>
<span class="topo-line"><span class="topo-membrane">FVYS</span><span class="topo-inside">RVFQEAKRQLNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELD</span></span>
<span class="topo-line"><span class="topo-inside">KAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMG</span></span>
<span class="topo-line"><span class="topo-inside">ETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYKFCLKE</span></span>
<span class="topo-line"><span class="topo-inside">HKALKTL</span><span class="topo-membrane">GIIMGTFTLCWLPFFIVNIVHVI</span><span class="topo-outside">QDNLIRKEV</span><span class="topo-membrane">YILLNWIGYVNSGFNPLIYC</span><span class="topo-inside">R</span></span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-unknown">PDFRIAFQEL</span><span class="topo-inside">LCL</span><span class="topo-unknown">RRSSLKHHHHHH</span></span>
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
      <td>55</td>
      <td>58</td>
      <td>31</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>83</td>
      <td>35</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>94</td>
      <td>60</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>115</td>
      <td>71</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>132</td>
      <td>92</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>153</td>
      <td>109</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>130</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>194</td>
      <td>151</td>
      <td>170</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>195</td>
      <td>222</td>
      <td>171</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>244</td>
      <td>199</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>427</td>
      <td>221</td>
      <td>275</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>450</td>
      <td>276</td>
      <td>298</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>451</td>
      <td>459</td>
      <td>299</td>
      <td>307</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>460</td>
      <td>479</td>
      <td>308</td>
      <td>327</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>480</td>
      <td>481</td>
      <td>328</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>482</td>
      <td>491</td>
      <td>330</td>
      <td>339</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>492</td>
      <td>494</td>
      <td>340</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ps0">6PS0</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDAMGQPGNGSAFLLAPNRSHAPDHDVTQQRDE</span><span class="topo-outside">VWVVG</span><span class="topo-membrane">M</span></span>
<span class="topo-line"><span class="topo-membrane">GIVMSLIVLAIVFGNVLVITAIA</span><span class="topo-inside">KFERLQTVTNY</span><span class="topo-membrane">FITSLACADLVMGLAVVPFGA</span><span class="topo-outside">AHILM</span></span>
<span class="topo-line"><span class="topo-outside">KMWTFGNFWCEF</span><span class="topo-membrane">WTSIDVLCVTASIWTLCVIAV</span><span class="topo-inside">DRYFAITSPFKYQSLLTKNKA</span><span class="topo-membrane">RVIILM</span></span>
<span class="topo-line"><span class="topo-membrane">VWIVSGLTSFLPI</span><span class="topo-outside">QMHWYRATHQEAINCYAEETCCDFFTNQA</span><span class="topo-membrane">YAIASSIVSFYVPLVIMV</span></span>
<span class="topo-line"><span class="topo-membrane">FVY</span><span class="topo-inside">SRVFQEAKRQLNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELD</span></span>
<span class="topo-line"><span class="topo-inside">KAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMG</span></span>
<span class="topo-line"><span class="topo-inside">ETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYKFCLKE</span></span>
<span class="topo-line"><span class="topo-inside">HKALKTL</span><span class="topo-membrane">GIIMGTFTLCWLPFFIVNIVHV</span><span class="topo-outside">IQDNLIRKEV</span><span class="topo-membrane">YILLNWIGYVNSGFNPLIYC</span><span class="topo-inside">R</span></span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-unknown">PDFRIAFQEL</span><span class="topo-inside">LCL</span><span class="topo-unknown">RRSSLKHHHHHH</span></span>
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
      <td>55</td>
      <td>59</td>
      <td>31</td>
      <td>35</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>83</td>
      <td>36</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>94</td>
      <td>60</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>115</td>
      <td>71</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>116</td>
      <td>132</td>
      <td>92</td>
      <td>108</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>153</td>
      <td>109</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>130</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>193</td>
      <td>151</td>
      <td>169</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>194</td>
      <td>222</td>
      <td>170</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>223</td>
      <td>243</td>
      <td>199</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>427</td>
      <td>220</td>
      <td>275</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>449</td>
      <td>276</td>
      <td>297</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>450</td>
      <td>459</td>
      <td>298</td>
      <td>307</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>460</td>
      <td>479</td>
      <td>308</td>
      <td>327</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>480</td>
      <td>481</td>
      <td>328</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>482</td>
      <td>491</td>
      <td>330</td>
      <td>339</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>492</td>
      <td>494</td>
      <td>340</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ps1">6PS1</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDAMGQPGNGSAFLLAPNRSHAPDHDVTQQR</span><span class="topo-outside">DEV</span><span class="topo-membrane">WVVGM</span></span>
<span class="topo-line"><span class="topo-membrane">GIVMSLIVLAIVFGNVLVITAIA</span><span class="topo-inside">KFERLQTVTNY</span><span class="topo-membrane">FITSLACADLVMGLAVVPFGAAHIL</span><span class="topo-outside">M</span></span>
<span class="topo-line"><span class="topo-outside">KMWTFGNFW</span><span class="topo-membrane">CEFWTSIDVLCVTASIWTLCVIAV</span><span class="topo-inside">DRYFAITSPFKYQSLLTKNKA</span><span class="topo-membrane">RVIILM</span></span>
<span class="topo-line"><span class="topo-membrane">VWIVSGLTSFLPIQMHWY</span><span class="topo-outside">RATH</span><span class="topo-unknown">QEAINCYA</span><span class="topo-outside">EETCCDFFTNQ</span><span class="topo-membrane">AYAIASSIVSFYVPLVIMV</span></span>
<span class="topo-line"><span class="topo-membrane">FVY</span><span class="topo-inside">SRVFQEAKRQLNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELD</span></span>
<span class="topo-line"><span class="topo-inside">KAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMG</span></span>
<span class="topo-line"><span class="topo-inside">ETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYKFCLKE</span></span>
<span class="topo-line"><span class="topo-inside">HKALKTL</span><span class="topo-membrane">GIIMGTFTLCWLPFFIVNIVHVIQ</span><span class="topo-outside">DNLIRKE</span><span class="topo-membrane">VYILLNWIGYVNSGFNPLIY</span><span class="topo-inside">CR</span></span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-unknown">PDFRIAFQELL</span><span class="topo-inside">CL</span><span class="topo-unknown">RRSSLKHHHHHH</span></span>
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
      <td>53</td>
      <td>55</td>
      <td>29</td>
      <td>31</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>83</td>
      <td>32</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>94</td>
      <td>60</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>119</td>
      <td>71</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>129</td>
      <td>96</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>153</td>
      <td>106</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>130</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>198</td>
      <td>151</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>202</td>
      <td>175</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>210</td>
      <td>179</td>
      <td>186</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>211</td>
      <td>221</td>
      <td>187</td>
      <td>197</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>243</td>
      <td>198</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>427</td>
      <td>220</td>
      <td>275</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>451</td>
      <td>276</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>452</td>
      <td>458</td>
      <td>300</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>459</td>
      <td>478</td>
      <td>307</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>479</td>
      <td>481</td>
      <td>327</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>482</td>
      <td>492</td>
      <td>330</td>
      <td>340</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>493</td>
      <td>494</td>
      <td>341</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ps2">6PS2</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDAMGQPGNGSAFLLAPNRSHAPDHDVTQQ</span><span class="topo-outside">RDEVW</span><span class="topo-membrane">VVGM</span></span>
<span class="topo-line"><span class="topo-membrane">GIVMSLIVLAIVFGNVLVITA</span><span class="topo-inside">IAKFERLQTVTNY</span><span class="topo-membrane">FITSLACADLVMGLAVVPFGAA</span><span class="topo-outside">HILM</span></span>
<span class="topo-line"><span class="topo-outside">KMWTFGNFWCE</span><span class="topo-membrane">FWTSIDVLCVTASIWTLCVIAV</span><span class="topo-inside">DRYFAITSPFKYQSLLTKNKA</span><span class="topo-membrane">RVIILM</span></span>
<span class="topo-line"><span class="topo-membrane">VWIVSGLTSFLPIQM</span><span class="topo-outside">HWYRATHQEAINCYAEETCCDFFTNQ</span><span class="topo-membrane">AYAIASSIVSFYVPLVIMV</span></span>
<span class="topo-line"><span class="topo-membrane">FVY</span><span class="topo-inside">SRVFQEAKRQLNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELD</span></span>
<span class="topo-line"><span class="topo-inside">KAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMG</span></span>
<span class="topo-line"><span class="topo-inside">ETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYKFCLKE</span></span>
<span class="topo-line"><span class="topo-inside">HKALKTL</span><span class="topo-membrane">GIIMGTFTLCWLPFFIVNIVHVIQ</span><span class="topo-outside">DNLIRKE</span><span class="topo-membrane">VYILLNWIGYVNSGFNPLIY</span><span class="topo-inside">CR</span></span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-unknown">PDFRIAFQEL</span><span class="topo-inside">LCL</span><span class="topo-unknown">RRSSLKHHHHHH</span></span>
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
      <td>52</td>
      <td>56</td>
      <td>28</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>81</td>
      <td>33</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>94</td>
      <td>58</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>116</td>
      <td>71</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>131</td>
      <td>93</td>
      <td>107</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>153</td>
      <td>108</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>130</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>195</td>
      <td>151</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>221</td>
      <td>172</td>
      <td>197</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>243</td>
      <td>198</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>427</td>
      <td>220</td>
      <td>275</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>451</td>
      <td>276</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>452</td>
      <td>458</td>
      <td>300</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>459</td>
      <td>478</td>
      <td>307</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>479</td>
      <td>481</td>
      <td>327</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>482</td>
      <td>491</td>
      <td>330</td>
      <td>339</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>492</td>
      <td>494</td>
      <td>340</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ps3">6PS3</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDAMGQPGNGSAFLLAPNRSHAPDHDVTQQR</span><span class="topo-outside">DEV</span><span class="topo-membrane">WVVGM</span></span>
<span class="topo-line"><span class="topo-membrane">GIVMSLIVLAIVFGNVLVITA</span><span class="topo-inside">IAKFERLQTVTNY</span><span class="topo-membrane">FITSLACADLVMGLAVVPFGAAHIL</span><span class="topo-outside">M</span></span>
<span class="topo-line"><span class="topo-outside">KMWTFGNFW</span><span class="topo-membrane">CEFWTSIDVLCVTASIWTLCVIAV</span><span class="topo-inside">DRYFAITSPFKYQSLLTKNKA</span><span class="topo-membrane">RVIILM</span></span>
<span class="topo-line"><span class="topo-membrane">VWIVSGLTSFLPIQM</span><span class="topo-outside">HWYRATH</span><span class="topo-unknown">QEAINCYA</span><span class="topo-outside">EETCCDFFTNQ</span><span class="topo-membrane">AYAIASSIVSFYVPLVIMV</span></span>
<span class="topo-line"><span class="topo-membrane">FVY</span><span class="topo-inside">SRVFQEAKRQLNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELD</span></span>
<span class="topo-line"><span class="topo-inside">KAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMG</span></span>
<span class="topo-line"><span class="topo-inside">ETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYKFCLKE</span></span>
<span class="topo-line"><span class="topo-inside">HKALKTL</span><span class="topo-membrane">GIIMGTFTLCWLPFFIVNIVHVIQ</span><span class="topo-outside">DNL</span><span class="topo-membrane">IRKEVYILLNWIGYVNSGFNPLIY</span><span class="topo-inside">CR</span></span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-unknown">PDFRIAFQEL</span><span class="topo-inside">LCL</span><span class="topo-unknown">RRSSLKHHHHHH</span></span>
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
      <td>53</td>
      <td>55</td>
      <td>29</td>
      <td>31</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>81</td>
      <td>32</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>94</td>
      <td>58</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>119</td>
      <td>71</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>129</td>
      <td>96</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>153</td>
      <td>106</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>130</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>195</td>
      <td>151</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>202</td>
      <td>172</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>210</td>
      <td>179</td>
      <td>186</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>211</td>
      <td>221</td>
      <td>187</td>
      <td>197</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>243</td>
      <td>198</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>427</td>
      <td>220</td>
      <td>275</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>451</td>
      <td>276</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>452</td>
      <td>454</td>
      <td>300</td>
      <td>302</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>478</td>
      <td>303</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>479</td>
      <td>481</td>
      <td>327</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>482</td>
      <td>491</td>
      <td>330</td>
      <td>339</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>492</td>
      <td>494</td>
      <td>340</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ps4">6PS4</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDAMGQPGNGSAFLLAPNRSHAPDHDVTQQR</span><span class="topo-outside">DEV</span><span class="topo-membrane">WVVGM</span></span>
<span class="topo-line"><span class="topo-membrane">GIVMSLIVLAIVFGNVLVITA</span><span class="topo-inside">IAKFERLQTVTNY</span><span class="topo-membrane">FITSLACADLVMGLAVVPFGAAHIL</span><span class="topo-outside">M</span></span>
<span class="topo-line"><span class="topo-outside">KMWTFGNFW</span><span class="topo-membrane">CEFWTSIDVLCVTASIWTLCVIAV</span><span class="topo-inside">DRYFAITSPFKYQSLLTKNKA</span><span class="topo-membrane">RVIILM</span></span>
<span class="topo-line"><span class="topo-membrane">VWIVSGLTSFLPIQM</span><span class="topo-outside">HWYRATH</span><span class="topo-unknown">QEAINCYA</span><span class="topo-outside">EETCCDFFTNQ</span><span class="topo-membrane">AYAIASSIVSFYVPLVIMV</span></span>
<span class="topo-line"><span class="topo-membrane">FVY</span><span class="topo-inside">SRVFQEAKRQLNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELD</span></span>
<span class="topo-line"><span class="topo-inside">KAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMG</span></span>
<span class="topo-line"><span class="topo-inside">ETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYKFCLKE</span></span>
<span class="topo-line"><span class="topo-inside">HKALKTL</span><span class="topo-membrane">GIIMGTFTLCWLPFFIVNIVHVIQ</span><span class="topo-outside">DNLIRKE</span><span class="topo-membrane">VYILLNWIGYVNSGFNPLIY</span><span class="topo-inside">CR</span></span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-unknown">PDFRIAFQEL</span><span class="topo-inside">LCL</span><span class="topo-unknown">RRSSLKHHHHHH</span></span>
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
      <td>53</td>
      <td>55</td>
      <td>29</td>
      <td>31</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>81</td>
      <td>32</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>94</td>
      <td>58</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>119</td>
      <td>71</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>129</td>
      <td>96</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>153</td>
      <td>106</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>130</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>195</td>
      <td>151</td>
      <td>171</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>196</td>
      <td>202</td>
      <td>172</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>210</td>
      <td>179</td>
      <td>186</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>211</td>
      <td>221</td>
      <td>187</td>
      <td>197</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>243</td>
      <td>198</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>427</td>
      <td>220</td>
      <td>275</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>451</td>
      <td>276</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>452</td>
      <td>458</td>
      <td>300</td>
      <td>306</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>459</td>
      <td>478</td>
      <td>307</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>479</td>
      <td>481</td>
      <td>327</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>482</td>
      <td>491</td>
      <td>330</td>
      <td>339</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>492</td>
      <td>494</td>
      <td>340</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ps5">6PS5</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDAMGQPGNGSAFLLAPNRSHAPDHDVTQQR</span><span class="topo-outside">DEV</span><span class="topo-membrane">WVVGM</span></span>
<span class="topo-line"><span class="topo-membrane">GIVMSLIVLAIVFGNVLVITAIA</span><span class="topo-inside">KFERLQTVTNY</span><span class="topo-membrane">FITSLACADLVMGLAVVPFGAAHIL</span><span class="topo-outside">M</span></span>
<span class="topo-line"><span class="topo-outside">KMWTFGNFW</span><span class="topo-membrane">CEFWTSIDVLCVTASIWTLCVIAV</span><span class="topo-inside">DRYFAITSPFKYQSLLTKNKA</span><span class="topo-membrane">RVIILM</span></span>
<span class="topo-line"><span class="topo-membrane">VWIVSGLTSFLPIQMHWY</span><span class="topo-outside">RATH</span><span class="topo-unknown">QEAINCYA</span><span class="topo-outside">EETCCDFFT</span><span class="topo-membrane">NQAYAIASSIVSFYVPLVIMV</span></span>
<span class="topo-line"><span class="topo-membrane">FVY</span><span class="topo-inside">SRVFQEAKRQLNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELD</span></span>
<span class="topo-line"><span class="topo-inside">KAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMG</span></span>
<span class="topo-line"><span class="topo-inside">ETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYKFCLKE</span></span>
<span class="topo-line"><span class="topo-inside">HKALKTL</span><span class="topo-membrane">GIIMGTFTLCWLPFFIVNIVHVIQ</span><span class="topo-outside">DNL</span><span class="topo-membrane">IRKEVYILLNWIGYVNSGFNPLIY</span><span class="topo-inside">CR</span></span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-unknown">PDFRIAFQEL</span><span class="topo-inside">LCL</span><span class="topo-unknown">RRSSLKHHHHHH</span></span>
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
      <td>53</td>
      <td>55</td>
      <td>29</td>
      <td>31</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>83</td>
      <td>32</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>94</td>
      <td>60</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>119</td>
      <td>71</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>129</td>
      <td>96</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>153</td>
      <td>106</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>174</td>
      <td>130</td>
      <td>150</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>175</td>
      <td>198</td>
      <td>151</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>202</td>
      <td>175</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>210</td>
      <td>179</td>
      <td>186</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>211</td>
      <td>219</td>
      <td>187</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>243</td>
      <td>196</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>244</td>
      <td>427</td>
      <td>220</td>
      <td>275</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>451</td>
      <td>276</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>452</td>
      <td>454</td>
      <td>300</td>
      <td>302</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>478</td>
      <td>303</td>
      <td>326</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>479</td>
      <td>481</td>
      <td>327</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>482</td>
      <td>491</td>
      <td>330</td>
      <td>339</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>492</td>
      <td>494</td>
      <td>340</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ps6">6PS6</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MKTIIALSYIFCLVFADYKDDDDAMGQPGNGSAFLLAPNRSHAPDHDVTQQ</span><span class="topo-outside">RDEV</span><span class="topo-membrane">WVVGM</span></span>
<span class="topo-line"><span class="topo-membrane">GIVMSLIVLAIVFGNVLVITAIA</span><span class="topo-inside">KFERLQTVTN</span><span class="topo-membrane">YFITSLACADLVMGLAVVPFGAAHIL</span><span class="topo-outside">M</span></span>
<span class="topo-line"><span class="topo-outside">KMWTFGNFW</span><span class="topo-membrane">CEFWTSIDVLCVTASIWTLCVIAV</span><span class="topo-inside">DRYFAITSPFKYQSLLTKNK</span><span class="topo-membrane">ARVIILM</span></span>
<span class="topo-line"><span class="topo-membrane">VWIVSGLTSFLPIQMHWY</span><span class="topo-outside">RATH</span><span class="topo-unknown">QEAINCYA</span><span class="topo-outside">EETCCDFFT</span><span class="topo-membrane">NQAYAIASSIVSFYVPLVIMV</span></span>
<span class="topo-line"><span class="topo-membrane">FVYS</span><span class="topo-inside">RVFQEAKRQLNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELD</span></span>
<span class="topo-line"><span class="topo-inside">KAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMG</span></span>
<span class="topo-line"><span class="topo-inside">ETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYKFCLKE</span></span>
<span class="topo-line"><span class="topo-inside">HKALKTL</span><span class="topo-membrane">GIIMGTFTLCWLPFFIVNIVHVIQ</span><span class="topo-outside">DNL</span><span class="topo-membrane">IRKEVYILLNWIGYVNSGFNPLIYC</span><span class="topo-inside">R</span></span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-unknown">PDFRIAFQELL</span><span class="topo-inside">CL</span><span class="topo-unknown">RRSSLKHHHHHH</span></span>
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
      <td>52</td>
      <td>55</td>
      <td>28</td>
      <td>31</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>83</td>
      <td>32</td>
      <td>59</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>84</td>
      <td>93</td>
      <td>60</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>119</td>
      <td>70</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>120</td>
      <td>129</td>
      <td>96</td>
      <td>105</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>153</td>
      <td>106</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>154</td>
      <td>173</td>
      <td>130</td>
      <td>149</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>198</td>
      <td>150</td>
      <td>174</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>199</td>
      <td>202</td>
      <td>175</td>
      <td>178</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>203</td>
      <td>210</td>
      <td>179</td>
      <td>186</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>211</td>
      <td>219</td>
      <td>187</td>
      <td>195</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>220</td>
      <td>244</td>
      <td>196</td>
      <td>220</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>245</td>
      <td>427</td>
      <td>221</td>
      <td>275</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>451</td>
      <td>276</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>452</td>
      <td>454</td>
      <td>300</td>
      <td>302</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>455</td>
      <td>479</td>
      <td>303</td>
      <td>327</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>480</td>
      <td>481</td>
      <td>328</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>482</td>
      <td>492</td>
      <td>330</td>
      <td>340</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>493</td>
      <td>494</td>
      <td>341</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Novel intracellular allosteric binding pocket on β2AR

Cmpd-6FA binds in a previously unpredicted allosteric pocket at the interface between the cytoplasm and membrane, formed by transmembrane helices 2, 3, 4, and intracellular loop 2 (ICL2). The pocket was not identified in prior fragment-based molecular dynamics druggability scans (Ivetac & McCammon, 2010), demonstrating that known receptor crystal structures may still harbor unidentified allosteric sites. The binding site is subdivided into three surface regions: membrane-embedded, membrane-proximal, and cytoplasmic surfaces.

### ICL2 alpha-helix stabilization mechanism of PAM activity

Cmpd-6FA stabilizes the active-state conformation of ICL2 as a two-turn alpha-helix, which is required for G-protein engagement. In the inactive-state, ICL2 exists as a random coil. The formation of the ICL2 alpha-helix requires inward displacement of Pro138(ICL2), resulting in ~3 A inward movement of TM3, which dictates outward movement of TM5 and TM6 — a hallmark of GPCR activation. This explains the positive allosteric effect: Cmpd-6FA increases the population of receptors adopting active conformations with higher affinity for agonists.

### Mechanism distinct from M2 muscarinic PAM

Unlike the M2 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) receptor PAM [LY2119620](/xray-mp-wiki/reagents/ligands/ly2119620/), which binds within the extracellular vestibule to directly prevent agonist dissociation, Cmpd-6FA acts through a distinct mechanism — stabilizing the active-state of the receptor with a closed hormone-binding site, thereby retarding agonist dissociation (agonist trapping effect). This mechanism does not involve direct steric occlusion of the orthosteric site.

### Subtype selectivity determinants between β2AR and β1AR

Only 7 of 14 residues forming the Cmpd-6FA allosteric site are conserved between β2AR and β1AR. Cmpd-6 enhances agonist binding 31-fold for β2AR but only 2.8-fold for β1AR. Mutagenesis studies identified residues at positions 3.52 (Phe133 in β2AR vs Leu158 in β1AR) and 4.41 (Lys149 in β2AR vs Arg174 in β1AR) as the major determinants of subtype selectivity. The double mutant β1AR(L158F/R174K) conferred a 20-fold increase in agonist affinity with Cmpd-6.

### LSP-SFX enables rapid multi-ligand GPCR structure determination

Using [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/) (SFX) with lipidic sponge phase ([LSP](/xray-mp-wiki/concepts/membrane-mimetics/lipidic-sponge-phase/)) crystallization, eight room-temperature co-crystal structures of β2AR-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) were determined with six different ligands at 2.8-4.0 A resolution (Ishchenko et al., IUCrJ 2019). The [LSP](/xray-mp-wiki/concepts/membrane-mimetics/lipidic-sponge-phase/) yields thousands of uniformly sized isomorphous microcrystals per microliter of protein solution, requiring only submilligram quantities of protein. This approach enabled the first crystal structures of β2AR with [Carvedilol](/xray-mp-wiki/reagents/ligands/carvedilol/) and propranolol, and demonstrated the feasibility of rapid multi-ligand SBDD for GPCRs using XFEL sources.

### Carvedilol binding mode reveals biased agonism mechanism

The β2AR-[Carvedilol](/xray-mp-wiki/reagents/ligands/carvedilol/) structure (PDB 6PS3, 3.7 A) reveals a unique binding mode where the carbazole group extends deep into the orthosteric pocket while the ethanolamine moiety interacts with D113(3.32) and N312(7.39). [Carvedilol](/xray-mp-wiki/reagents/ligands/carvedilol/) makes an additional hydrogen bond with Y316(7.43), which may contribute to its biased signaling profile as a β-arrestin-biased agonist that inhibits Gs signaling while promoting β-arrestin recruitment.

### Diverse orthosteric binding pocket conformations

The six ligands in the β2AR LSP-SFX study produce distinct conformations of the orthosteric binding pocket. Inverse agonists ([Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/), ICI-118,551) stabilize the inactive conformation with the ionic lock between R131(3.50) and E268(6.30) intact. The agonist [BI-167107](/xray-mp-wiki/reagents/ligands/bi-167107/) shifts the pocket toward an active-like conformation. Propranolol adopts a binding mode similar to [Carazolol](/xray-mp-wiki/reagents/ligands/carazolol/). Timolol occupies the pocket with different interactions than the other β-blockers, reflecting its distinct pharmacological profile.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/human-adenosine-a2a-receptor-a2ar/">Human Adenosine A2A Receptor (A2AR)</a> — Method generality demonstrated with A2AR LSP-SFX structures (caffeine, ZM241385)
- <a href="/xray-mp-wiki/concepts/signaling-receptors/biased-agonism/">Biased Agonism</a> — Carvedilol binding mode reveals structural basis of β-arrestin-biased agonism
- <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4 Lysozyme (T4L)</a> — T4L fusion used for all β2AR structures in this study
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Standard detergent for GPCR purification and stabilization
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/lipidic-sponge-phase/">LSP</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/">Serial Femtosecond Crystallography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
