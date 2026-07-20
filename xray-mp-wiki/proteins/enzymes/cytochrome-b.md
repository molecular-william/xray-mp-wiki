---
title: "Cytochrome b (EcHyd-1 Partner)"
created: 2026-05-28
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2012.11.010]
verified: agent
uniprot_id: ['P0AAM1', 'P0ACD8', 'P69739']
---

# Cytochrome b (EcHyd-1 Partner)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0AAM1">UniProt: P0AAM1</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P0ACD8">UniProt: P0ACD8</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P69739">UniProt: P69739</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

Cytochrome b is the physiological partner of Escherichia coli Hydrogenase 1 (EcHyd-1). It serves primarily as a membrane anchor for the hydrogenase complex and participates in the electron-transfer pathway. The structure of the EcHyd-1-cytochrome b complex was solved at 3.3 A resolution, revealing approximately 6,800 A2 of buried surface area between the two proteins. The proximal [HEME](/xray-mp-wiki/reagents/ligands/heme) of cytochrome b is connected to the distal [Fe4S4] cluster of the hydrogenase S subunit via a 5 A pathway.


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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4gd3">4GD3</a></td>
      <td>3.3</td>
      <td>P212121</td>
      <td>Cytochrome b subunit in complex with EcHyd-1 (SL)2 dimer</td>
      <td>Proximal heme (single Fe atom per cytochrome b)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Native cytochrome b (B subunit) associated with EcHyd-1

**Purification:**

- **Expression system**: Escherichia coli

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
      <td>Co-purification with EcHyd-1</td>
      <td>Detergent solubilization and <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>0.02% Triton X-100 + 0.02% Triton X-100</td>
      <td>Cytochrome b co-eluted with EcHyd-1 in the second peak; homogenizer treatment dissociates cytochrome b from EcHyd-1</td>
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

</div>

## Biological / Functional Insights

### Membrane anchoring role

The main role of cytochrome b in the EcHyd-1 complex is to anchor the
hydrogenase to the membrane rather than sending electrons to the respiratory
chain. The mainly hydrophobic interaction between one S subunit C-terminal
alpha helix and the cytochrome is very similar to the one observed in
formate dehydrogenase-N (EcFDH-N).

### Electron transfer to proximal heme

The histidine ligand of the distal [Fe4S4] cluster and one of the
carboxylate groups of the proximal heme are separated by about 5 A.
It is possible to partially reduce the cytochrome with H2, which implies
a viable electron-transfer pathway from the H2ase distal [Fe4S4] cluster
to the proximal heme. The cytochrome becomes oxidized under air and can
be partially reduced again by H2.

### Extensive interaction surface

About 6,800 A2 of the cytochrome b surface is buried in the [B(SL)2]2
complex. This value is much higher than those obtained for a symmetrical
(BSL)2 structure, explaining the stability of the crystallized complex.
The interface between the two proteins contains numerous conserved residues
and shows extensive charge and shape complementarity.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/ec-hyd-1/">Escherichia coli Hydrogenase 1 (EcHyd-1)</a> — Forms 2:1 complex; cytochrome b is the physiological partner
- <a href="/xray-mp-wiki/proteins/enzymes/cytochrome-b5/">Cytochrome b5</a> — Related cytochrome with similar heme-containing electron transfer function
- <a href="/xray-mp-wiki/reagents/detergents/triton-x-100/">Triton X-100</a> — Detergent used for co-purification of the complex
- <a href="/xray-mp-wiki/reagents/ligands/heme/">Heme</a> — Proximal heme cofactor in cytochrome b
