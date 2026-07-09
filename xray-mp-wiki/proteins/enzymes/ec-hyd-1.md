---
title: "Escherichia coli Hydrogenase 1 (EcHyd-1)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2012.11.010, doi/10.1073##pnas.1119806109]
verified: regex
uniprot_id: ['P0AAM1', 'P0ACD8', 'P69739']
---

# Escherichia coli Hydrogenase 1 (EcHyd-1)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span> <span class="expr-badge expr-native-tissue">Native tissue</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0AAM1">UniProt: P0AAM1</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0ACD8">UniProt: P0ACD8</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P69739">UniProt: P69739</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

Hydrogenase 1 (EcHyd-1) is a membrane-bound, O2-tolerant [NiFe]-hydrogenase from Escherichia coli that catalyzes the reversible oxidation of molecular hydrogen (H2 ↔ 2H+ + 2e-). Unlike other E. coli hydrogenases (Hyd-2 and Hyd-3), EcHyd-1 is maximally expressed during fermentation under anaerobic conditions. It functions to protect O2-sensitive enzymes during the anaerobic-to-aerobic metabolic transition by reducing intracellular O2 to water. The enzyme forms a dimer of heterodimers with a hydrophobic membrane-anchoring small subunit C-terminal domain. The crystal structure reveals a [4Fe-3S] proximal cluster with two supernumerary Cys residues (Cys19 and Cys120) that enable O2 tolerance by providing two successive electrons to reduce O2 to H2O.


## Publications

### doi/10.1016##j.str.2012.11.010

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
      <td></td>
      <td>1.47</td>
      <td>not specified</td>
      <td>EcHyd-1 (SL)2 heterodimer</td>
      <td>NiFe active site, [Fe4S4], [Fe3S4], [Fe4S4] clusters</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli (native expression)
- **Construct**: Full-length membrane-bound EcHyd-1 (S and L subunits)

**Purification:**

- **Expression system**: Escherichia coli
- **Expression construct**: Full-length EcHyd-1

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
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>-- + 3% w/v Triton X-100</td>
      <td>Cell membrane proteins at 10 mg/ml stirred overnight at 4 C</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography</td>
      <td>Superdex 200</td>
      <td>-- + 0.02% Triton X-100</td>
      <td>Performed in anaerobic glove box; cytochrome b co-eluted in second peak</td>
    </tr>
    <tr>
      <td>Hydroxyapatite chromatography</td>
      <td>Hydroxyapatite chromatography</td>
      <td>Hydroxyapatite</td>
      <td>K2HPO4/KH2PO4 + --</td>
      <td>Protein eluted at double the concentration of K2HPO4/KH2PO4 compared to previous protocol</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>As-isolated EcHyd-1 crystal; orthorhombic; data collected at SLS (Swiss Light Source). H2-reduced structure by exposing crystal to 8 bar H2 for 10 min. Oxidized structure by soaking as-isolated crystal with 2 mM 4-OH-1,4-naphthoquinone (OH-NQ) and 10 mM K3Fe(CN)6. Focused microbeam used for data collection.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gd3">4GD3</a> — Chain S (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">LEN</span><span class="topo-outside">KPRIPVVWIHGLECTCCTESFIRSAHPLAKDVILSLISLDYDDTLMAAAGTQAEEVFEDIITQYNGKYILAVEGNPPLGEQGMFCISSGRPFIEKLKRAAAGASAIIAWGTCASWGC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">VQAARPNPTQATPIDKVITDKPIIKVPGCPPIPDVMSAIITYMVTFDRLPDVDRMGRPLMFYGQRIHDKCYRRAHFDAGEFVQSWDDDAARKGYCLYKMGCKGPTTYNACSSTRWNDGVS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330     </span>
<span class="topo-line"><span class="topo-outside">FCIQSGHGCLGCAENGFWDRGSFYSRVVDIPQMGTHST</span><span class="topo-membrane">ADTVGLTALGVVAAAVG</span><span class="topo-inside">VHAVASAVDQRR</span><span class="topo-unknown">RHNQQPTETEHQPGNEDKQARSHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>278</td>
      <td>4</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>295</td>
      <td>279</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>307</td>
      <td>296</td>
      <td>307</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>335</td>
      <td>308</td>
      <td>335</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gd3">4GD3</a> — Chain L (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">STQYETQGYTINNAGRRLVVDPITRIEGHMRCEVNINDQNVITNAVSCGTMFRGLEIILQGRDPRDAWAFVERICGVCTGVHALASVYAIEDAIGIKVPDNANIIRNIMLATLWCHDHL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">VHFYQLAGMDWIDVLDALKADPRKTSELAQSLSSWPKSSPGYFFDVQNRLKKFVEGGQLGIFRNGYWGHPQYKLPPEANLMGFAHYLEALDFQREIVKIHAVFGGKNPHPNWIVGGMPCA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">INIDESGAVGAVNMERLNLVQSIITRTADFINNVMIPDALAIGQFNKPWSEIGTGLSDKCVLSYGAFPDIANDFGEKSLLMPGGAVINGDFNNVLPVDLVDPQQVQEFVDHAWYRYPNDQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">VGRHPFDGITDPWYNPGDVKGSDTNIQQLNEQERYSWIKAPRWRGNAMEVGPLARTLIAYHKGDAATVESVDRMMSALNLPLSGIQSTLGRILCRAHEAQWAAGKLQYFFDKLMTNLKNG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580  </span>
<span class="topo-line"><span class="topo-outside">NLATASTEKWEPATWPTECRGVGFTEAPRGALGHWAAIRDGKIDLYQCVVPTTWNASPRDPKGQIGAYEAALMNTKMAIPEQPLEILRTLHSFDPCLACSTH</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>582</td>
      <td>2</td>
      <td>582</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gd3">4GD3</a> — Chain T (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">LEN</span><span class="topo-outside">KPRIPVVWIHGLECTCCTESFIRSAHPLAKDVILSLISLDYDDTLMAAAGTQAEEVFEDIITQYNGKYILAVEGNPPLGEQGMFCISSGRPFIEKLKRAAAGASAIIAWGTCASWGC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">VQAARPNPTQATPIDKVITDKPIIKVPGCPPIPDVMSAIITYMVTFDRLPDVDRMGRPLMFYGQRIHDKCYRRAHFDAGEFVQSWDDDAARKGYCLYKMGCKGPTTYNACSSTRWNDGVS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330     </span>
<span class="topo-line"><span class="topo-outside">FCIQSGHGCLGCAENGFWDRGSFYSRVVDIPQMGTHSTA</span><span class="topo-membrane">DTVGLTALGVVAAAVGVHAVA</span><span class="topo-inside">SAV</span><span class="topo-unknown">DQRRRHNQQPTETEHQPGNEDKQARSHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>279</td>
      <td>4</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>300</td>
      <td>280</td>
      <td>300</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>301</td>
      <td>303</td>
      <td>301</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>335</td>
      <td>304</td>
      <td>335</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gd3">4GD3</a> — Chain M (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">STQYETQGYTINNAGRRLVVDPITRIEGHMRCEVNINDQNVITNAVSCGTMFRGLEIILQGRDPRDAWAFVERICGVCTGVHALASVYAIEDAIGIKVPDNANIIRNIMLATLWCHDHL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">VHFYQLAGMDWIDVLDALKADPRKTSELAQSLSSWPKSSPGYFFDVQNRLKKFVEGGQLGIFRNGYWGHPQYKLPPEANLMGFAHYLEALDFQREIVKIHAVFGGKNPHPNWIVGGMPCA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">INIDESGAVGAVNMERLNLVQSIITRTADFINNVMIPDALAIGQFNKPWSEIGTGLSDKCVLSYGAFPDIANDFGEKSLLMPGGAVINGDFNNVLPVDLVDPQQVQEFVDHAWYRYPNDQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">VGRHPFDGITDPWYNPGDVKGSDTNIQQLNEQERYSWIKAPRWRGNAMEVGPLARTLIAYHKGDAATVESVDRMMSALNLPLSGIQSTLGRILCRAHEAQWAAGKLQYFFDKLMTNLKNG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580  </span>
<span class="topo-line"><span class="topo-outside">NLATASTEKWEPATWPTECRGVGFTEAPRGALGHWAAIRDGKIDLYQCVVPTTWNASPRDPKGQIGAYEAALMNTKMAIPEQPLEILRTLHSFDPCLACSTH</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>582</td>
      <td>2</td>
      <td>582</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gd3">4GD3</a> — Chain Q (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">LEN</span><span class="topo-outside">KPRIPVVWIHGLECTCCTESFIRSAHPLAKDVILSLISLDYDDTLMAAAGTQAEEVFEDIITQYNGKYILAVEGNPPLGEQGMFCISSGRPFIEKLKRAAAGASAIIAWGTCASWGC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">VQAARPNPTQATPIDKVITDKPIIKVPGCPPIPDVMSAIITYMVTFDRLPDVDRMGRPLMFYGQRIHDKCYRRAHFDAGEFVQSWDDDAARKGYCLYKMGCKGPTTYNACSSTRWNDGVS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330     </span>
<span class="topo-line"><span class="topo-outside">FCIQSGHGCLGCAENGFWDRGSFYSRVVDIPQMGTHST</span><span class="topo-membrane">ADTVGLTALGVVAAAVG</span><span class="topo-inside">VHAVASAVDQRR</span><span class="topo-unknown">RHNQQPTETEHQPGNEDKQARSHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>278</td>
      <td>4</td>
      <td>278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>295</td>
      <td>279</td>
      <td>295</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>296</td>
      <td>307</td>
      <td>296</td>
      <td>307</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>308</td>
      <td>335</td>
      <td>308</td>
      <td>335</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gd3">4GD3</a> — Chain J (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">STQYETQGYTINNAGRRLVVDPITRIEGHMRCEVNINDQNVITNAVSCGTMFRGLEIILQGRDPRDAWAFVERICGVCTGVHALASVYAIEDAIGIKVPDNANIIRNIMLATLWCHDHL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">VHFYQLAGMDWIDVLDALKADPRKTSELAQSLSSWPKSSPGYFFDVQNRLKKFVEGGQLGIFRNGYWGHPQYKLPPEANLMGFAHYLEALDFQREIVKIHAVFGGKNPHPNWIVGGMPCA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">INIDESGAVGAVNMERLNLVQSIITRTADFINNVMIPDALAIGQFNKPWSEIGTGLSDKCVLSYGAFPDIANDFGEKSLLMPGGAVINGDFNNVLPVDLVDPQQVQEFVDHAWYRYPNDQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">VGRHPFDGITDPWYNPGDVKGSDTNIQQLNEQERYSWIKAPRWRGNAMEVGPLARTLIAYHKGDAATVESVDRMMSALNLPLSGIQSTLGRILCRAHEAQWAAGKLQYFFDKLMTNLKNG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580  </span>
<span class="topo-line"><span class="topo-outside">NLATASTEKWEPATWPTECRGVGFTEAPRGALGHWAAIRDGKIDLYQCVVPTTWNASPRDPKGQIGAYEAALMNTKMAIPEQPLEILRTLHSFDPCLACSTH</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>582</td>
      <td>2</td>
      <td>582</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gd3">4GD3</a> — Chain R (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">LEN</span><span class="topo-outside">KPRIPVVWIHGLECTCCTESFIRSAHPLAKDVILSLISLDYDDTLMAAAGTQAEEVFEDIITQYNGKYILAVEGNPPLGEQGMFCISSGRPFIEKLKRAAAGASAIIAWGTCASWGC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">VQAARPNPTQATPIDKVITDKPIIKVPGCPPIPDVMSAIITYMVTFDRLPDVDRMGRPLMFYGQRIHDKCYRRAHFDAGEFVQSWDDDAARKGYCLYKMGCKGPTTYNACSSTRWNDGVS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330     </span>
<span class="topo-line"><span class="topo-outside">FCIQSGHGCLGCAENGFWDRGSFYSRVVDIPQMGTHSTA</span><span class="topo-membrane">DTVGLTALGVVAAAVGVHAVA</span><span class="topo-inside">SAV</span><span class="topo-unknown">DQRRRHNQQPTETEHQPGNEDKQARSHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>279</td>
      <td>4</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>300</td>
      <td>280</td>
      <td>300</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>301</td>
      <td>303</td>
      <td>301</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>335</td>
      <td>304</td>
      <td>335</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gd3">4GD3</a> — Chain K (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">STQYETQGYTINNAGRRLVVDPITRIEGHMRCEVNINDQNVITNAVSCGTMFRGLEIILQGRDPRDAWAFVERICGVCTGVHALASVYAIEDAIGIKVPDNANIIRNIMLATLWCHDHL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">VHFYQLAGMDWIDVLDALKADPRKTSELAQSLSSWPKSSPGYFFDVQNRLKKFVEGGQLGIFRNGYWGHPQYKLPPEANLMGFAHYLEALDFQREIVKIHAVFGGKNPHPNWIVGGMPCA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">INIDESGAVGAVNMERLNLVQSIITRTADFINNVMIPDALAIGQFNKPWSEIGTGLSDKCVLSYGAFPDIANDFGEKSLLMPGGAVINGDFNNVLPVDLVDPQQVQEFVDHAWYRYPNDQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">VGRHPFDGITDPWYNPGDVKGSDTNIQQLNEQERYSWIKAPRWRGNAMEVGPLARTLIAYHKGDAATVESVDRMMSALNLPLSGIQSTLGRILCRAHEAQWAAGKLQYFFDKLMTNLKNG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580  </span>
<span class="topo-line"><span class="topo-outside">NLATASTEKWEPATWPTECRGVGFTEAPRGALGHWAAIRDGKIDLYQCVVPTTWNASPRDPKGQIGAYEAALMNTKMAIPEQPLEILRTLHSFDPCLACSTH</span></span>
<details class="topo-details"><summary>Topology coordinates (2 regions)</summary>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>582</td>
      <td>2</td>
      <td>582</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gd3">4GD3</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQQKSDN</span><span class="topo-inside">VVSHYVFEAPV</span><span class="topo-membrane">RIWHWLTVLCMAVLMVTGY</span><span class="topo-outside">FIGKPLPSVSGEATYLFYMGYIRLI</span><span class="topo-membrane">HFSAGMVFTVVLLMRIYW</span><span class="topo-inside">AFVGNRYSR</span><span class="topo-unknown">ELFIVPVWRKSWW</span><span class="topo-inside">QGVWYEIRWYLFL</span><span class="topo-unknown">AKRPS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230     </span>
<span class="topo-line"><span class="topo-unknown">ADIGHN</span><span class="topo-inside">PIA</span><span class="topo-membrane">QAAMFGYFLMSVFMIITGFALYS</span><span class="topo-outside">EHSQYAI</span><span class="topo-unknown">FAPFRYVVEFFYWT</span><span class="topo-outside">GGNSMDIHSW</span><span class="topo-membrane">HRLGMWLIGAFVIGHVYMALR</span><span class="topo-inside">EDIMSD</span><span class="topo-unknown">DTVISTMVNGYRSHKFGKISNKERS</span></span>
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
      <td>1</td>
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>18</td>
      <td>8</td>
      <td>18</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>37</td>
      <td>19</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>62</td>
      <td>38</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>80</td>
      <td>63</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>89</td>
      <td>81</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>102</td>
      <td>90</td>
      <td>102</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>103</td>
      <td>115</td>
      <td>103</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>126</td>
      <td>116</td>
      <td>126</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>127</td>
      <td>129</td>
      <td>127</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>152</td>
      <td>130</td>
      <td>152</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>153</td>
      <td>159</td>
      <td>153</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>173</td>
      <td>160</td>
      <td>173</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>174</td>
      <td>183</td>
      <td>174</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>204</td>
      <td>184</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>210</td>
      <td>205</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>235</td>
      <td>211</td>
      <td>235</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gd3">4GD3</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQQKSDN</span><span class="topo-inside">VVSHYVFEAPV</span><span class="topo-membrane">RIWHWLTVLCMAVLMVTGY</span><span class="topo-outside">FIGKPLPSVSGEATYLFYMGYIRLI</span><span class="topo-membrane">HFSAGMVFTVVLLMRIYW</span><span class="topo-inside">AFVGNRYSR</span><span class="topo-unknown">ELFIVPVWRKSWW</span><span class="topo-inside">QGVWYEIRWYLFL</span><span class="topo-unknown">AKRPS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230     </span>
<span class="topo-line"><span class="topo-unknown">ADIGHN</span><span class="topo-inside">PIA</span><span class="topo-membrane">QAAMFGYFLMSVFMIITGFA</span><span class="topo-outside">LYSEHSQYAI</span><span class="topo-unknown">FAPFRYVVEFFYWT</span><span class="topo-outside">GGNSMDIHSW</span><span class="topo-membrane">HRLGMWLIGAFVIGHVYMALR</span><span class="topo-inside">EDIMSD</span><span class="topo-unknown">DTVISTMVNGYRSHKFGKISNKERS</span></span>
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
      <td>1</td>
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>18</td>
      <td>8</td>
      <td>18</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>37</td>
      <td>19</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>62</td>
      <td>38</td>
      <td>62</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>63</td>
      <td>80</td>
      <td>63</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>89</td>
      <td>81</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>102</td>
      <td>90</td>
      <td>102</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>103</td>
      <td>115</td>
      <td>103</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>126</td>
      <td>116</td>
      <td>126</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>127</td>
      <td>129</td>
      <td>127</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>149</td>
      <td>130</td>
      <td>149</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>159</td>
      <td>150</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>160</td>
      <td>173</td>
      <td>160</td>
      <td>173</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>174</td>
      <td>183</td>
      <td>174</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>204</td>
      <td>184</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>210</td>
      <td>205</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>235</td>
      <td>211</td>
      <td>235</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB  — Chain ? (? TMs, )**

</div>

</div>

## Biological / Functional Insights

### O2 tolerance and physiological role

EcHyd-1 is maximally expressed during fermentation when electron acceptors are scarce, in the lower part of the host's intestinal tract before excretion and the anaerobic-to-aerobic metabolic transition. The enzyme functions to keep intracellular O2 levels low by reducing O2 to water, protecting O2-sensitive enzymes (such as Hyd-3) during the transition. Under in-vivo fermenting conditions, O2 entering E. coli is reduced by EcHyd-1 using H2 generated by EcHyd-3 from formate. Hydrophobic tunnels connect the active site to the molecular surface, conveying H2 from the cytoplasmic side to the periplasmic active site.

### Structural basis of O2 tolerance via [4Fe-3S] proximal cluster

The proximal [4Fe-3S] cluster has one inorganic sulfide ligand replaced by bridging Cys19 Sγ and additional Cys120 Sγ ligand to Fe3. The cluster contains a unique [Iron](/xray-mp-wiki/reagents/additives/iron/) (Fe4) that can adopt two conformations. In the PC2 (reduced) state, Fe4 is tetrahedrally coordinated by Cys19, Cys20, and two sulfido ions. In the PC3 (oxidized) state, Fe4 binds the amide N from Cys20 and one Oε of Glu76, forming a distorted trigonal bipyramid. This structural rearrangement allows the proximal cluster to provide two successive electrons (PC2 → PC3) for complete reduction of O2 to H2O at the active site. Glu76 acts as a base to deprotonate the amide moiety of Cys20 upon [Iron](/xray-mp-wiki/reagents/additives/iron/) binding, making the second oxidation electroneutral.

### Electron transfer pathway to cytochrome b

The crystal structure reveals a viable electron-transfer pathway from the hydrogenase distal [Fe4S4] cluster to the proximal [Heme](/xray-mp-wiki/reagents/ligands/heme/) of cytochrome b. The histidine ligand of the [Fe4S4] cluster and one carboxylate group of the [Heme](/xray-mp-wiki/reagents/ligands/heme/) are separated by approximately 5 A. In the [B(SL)2]2 complex, the closest tunnel entrance virtually touches the membrane surface. The distance between the two distal [Fe4S4] clusters in the (SL)2 dimers is 12.3 A, well within the range for rapid electron transfer between H2ase S subunits.

### Dynamic water chain from O2 reduction

Comparison of as-isolated, H2-reduced, and oxidized EcHyd-1 structures shows a dynamic chain of water molecules located near the active site, resulting from O2 reduction. Four partially occupied H2O molecules close to the [NiFe] active site are likely O2-reduction products that need to be evacuated through the hydrophobic tunnel connecting the active site to the molecular surface.

### QM/CM calculations of proximal cluster redox states

Quantum mechanical/molecular mechanical (QM/MM) calculations reproduced published Mössbauer and EPR data and described the electronic and conformational changes during superoxidation of the proximal cluster. The second electron comes directly from Fe4, oxidizing from +2 to +3, causing migration of Fe4 toward the amide N of Cys20 and the carboxylate of Glu76. The best agreement to spectroscopic data was obtained for the PC3H model, which maintains electroneutrality in the PC2 → PC3 transition.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/cytochrome-b/">Cytochrome b</a> — Physiological partner; forms 2:1 complex with EcHyd-1
- <a href="/xray-mp-wiki/reagents/detergents/triton-x-100/">Triton X-100</a> — Detergent used for membrane solubilization
- <a href="/xray-mp-wiki/reagents/ligands/heme/">Heme</a> — Referenced in context related to Heme
- <a href="/xray-mp-wiki/reagents/additives/iron/">Iron</a> — Referenced in context related to Iron
