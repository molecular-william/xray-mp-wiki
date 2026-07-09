---
title: "AdeB Multidrug Efflux Transporter"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-021-27146-2]
verified: regex
uniprot_id: B0V4F5
---

# AdeB Multidrug Efflux Transporter

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/B0V4F5">UniProt: B0V4F5</a>

<span class="expr-badge">Acinetobacter baumannii (strain AYE)</span>

## Overview

AdeB is a multidrug efflux transporter from the Gram-negative pathogen Acinetobacter baumannii, belonging to the Resistance-Nodulation-Division (RND) superfamily. It forms the inner membrane pump component of the AdeABC tripartite efflux complex, together with the periplasmic adaptor AdeA and the outer membrane channel AdeC. AdeB functions as a homotrimer, with each protomer cycling through different conformational states. Single-particle cryo-electron microscopy revealed the AdeB trimer predominantly adopts a symmetric OOO resting state (3.54-3.84 A) with all protomers in a conformation devoid of transport channels or antibiotic binding sites. A second conformation, L*OO (3.84 A), was observed in approximately 10% of protomers, where three transport channels (CH1-CH3) lead to the closed deep binding pocket (DBP). The L* conformation represents a novel state not described for the homologous E. coli [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) transporter. Mutagenesis studies comparing AdeB and [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) substrate binding in the DBP using co-structures with doxycycline (2.1 A), fusidic acid (2.3 A), and levofloxacin (2.7 A) reveal distinct drug binding mechanisms between the two homologous RND pumps.

## Publications

### doi/10.1038##s41467-021-27146-2

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7b8q">7B8Q</a></td>
      <td>3.84</td>
      <td>--</td>
      <td>AdeB from A. baumannii, full-length, in L*OO conformation</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7b8r">7B8R</a></td>
      <td>3.54</td>
      <td>--</td>
      <td>AdeB from A. baumannii, full-length, in OOO conformation (C3-symmetric)</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: A. baumannii AdeB with C-terminal His10-tag, expressed in E. coli C43(DE3) Delta acrAB

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
      <td>Cell culture</td>
      <td>Fermentation</td>
      <td>--</td>
      <td>TB medium (12 g/L tryptone, 24 g/L yeast extract, 5 g/L <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 2.31 g/L KH2PO4, 12.54 g/L K2HPO4) + --</td>
      <td>E. coli C43(DE3) Delta acrAB harboring p7XC3H_<a href="/xray-mp-wiki/proteins/adeb/">adeB</a></td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td><a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">Ultracentrifugation</a></td>
      <td>--</td>
      <td>Resuspension buffer + --</td>
      <td>Membrane fraction collected by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 7.5, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Membranes solubilized in 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> with 12 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td>HisPur <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> (Thermo Scientific)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> pH 7.5, 300 mM NaCl, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Washed with 20 mM and 80 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, eluted with 400 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-exclusion chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>Superose 6 increase 10/300 GL</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.5, 150 mM NaCl, 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Trimeric protein fractions collected at ~13 mL elution volume</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> (single-particle)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified AdeB in 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> pH 7.5, 150 mM NaCl</td>
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
      <td><a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> data collected on Titan Krios, processed with Relion 3.0. Final maps at 3.54 A (OOO) and 3.84 A (L*OO). Initial model generated with Phyre2 using PDB 4DX5 as template. Model refined with Phenix real-space refinement and Coot, validated with Molprobity.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7b8q">7B8Q</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MS</span><span class="topo-outside">M</span><span class="topo-unknown">SQFFIR</span><span class="topo-outside">RPV</span><span class="topo-membrane">FAWVIAIFIIIFGLL</span><span class="topo-inside">SIPKLPIARFPSVAPPQVNISATYPGATAKTINDSVVTLIERELSGVKNLLYYSATTDTSGTAEITATFKPGTDVEMAQVDVQNKIKAVEARL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PQVVRQQGLQVEASSSGFLMLVGINSPNNQYSEVDLSDYLVRNVVEELKRVEGVGKVQSFGAEKAMRIWVDPNKLVSYGLSISDVNNAIRENNVEIAPGRLGDLPAEKGQLITIPLSAQG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">QLSSLEQFKNISLK</span><span class="topo-unknown">SKTNG</span><span class="topo-inside">SVIKLSDVANVEIGSQAYNFAILENGKPATAAAIQLSPGANAVKTAEGVRAKIEELKLNLPEGMEFSIPYDTAPFVKISIEKVIH</span><span class="topo-membrane">TLLEAMVLVFIVMYL</span><span class="topo-outside">F</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">LHNVRYT</span><span class="topo-membrane">LIPAIVAPIALLGTFTV</span><span class="topo-inside">MLLAGFSINVLTMFG</span><span class="topo-membrane">MVLAIGIIVDDAIV</span><span class="topo-outside">VVENVERIMATEGLS</span><span class="topo-unknown">PKDATSKAMKEI</span><span class="topo-outside">TSP</span><span class="topo-membrane">IIGITLVLAAVFLPM</span><span class="topo-inside">AFASGSVGVIYKQFT</span><span class="topo-membrane">LTMSVSI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">LFSALLALILT</span><span class="topo-outside">PALCATILKPIDGH</span><span class="topo-unknown">HQKKGFF</span><span class="topo-outside">AW</span><span class="topo-unknown">FDRSFDKVTKKYELMLLKII</span><span class="topo-outside">KHTVP</span><span class="topo-membrane">MMVIFLVITGITFAGM</span><span class="topo-inside">KYWPTAFMPEEDQGWFMTSFQLPSDATAERTRNVVNQFENNLKDN</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">PDVKSNTAILGWGFSGAGQNVAVAFTTLKDFKERTSSASKMTSDVNSSMANSTEGETMAVLPPAIDELGTFSGFSLRLQDRANLGMPALLAAQDELMAMAAKNKKFYMVWNEGLPQGDNI</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">SLKIDREKLSALGVKFSDVSDIISTSMGSMYINDFPNQGRMQQVIVQVEAKSRMQLKDILNLKVMGSSGQLVSLSEVVTPQWNKAPQQYNRYNGRPSLSIAGIPNFDTSSGEAMREMEQL</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-inside">IAKLPKGIGYEWTGISLQEKQSESQMAF</span><span class="topo-membrane">LLGLSMLVVFLVLAAL</span><span class="topo-outside">YESWAIP</span><span class="topo-membrane">LSVMLVVPLGIFGAIIAIMS</span><span class="topo-inside">RGLMNDVFFKI</span><span class="topo-membrane">GLITIIGLSAKNAI</span><span class="topo-outside">LIVEFAKMLKEEGMSLIEATVAAA</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050      </span>
<span class="topo-line"><span class="topo-outside">KLRLRPI</span><span class="topo-membrane">LMTSLAFTCGVIPLVI</span><span class="topo-inside">ATGASSETQHALG</span><span class="topo-membrane">TGVFGGMISATILAI</span><span class="topo-unknown">FFVPVFFIFILG</span><span class="topo-outside">AV</span><span class="topo-unknown">EKLFSSKKKISSALEVLFQGPHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (34 regions)</summary>
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
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>9</td>
      <td>2</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>12</td>
      <td>8</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>27</td>
      <td>11</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>254</td>
      <td>26</td>
      <td>252</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>344</td>
      <td>258</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>359</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>367</td>
      <td>358</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>384</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>385</td>
      <td>399</td>
      <td>383</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>413</td>
      <td>398</td>
      <td>411</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>414</td>
      <td>428</td>
      <td>412</td>
      <td>426</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>429</td>
      <td>440</td>
      <td>427</td>
      <td>438</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>441</td>
      <td>443</td>
      <td>439</td>
      <td>441</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>458</td>
      <td>442</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>473</td>
      <td>457</td>
      <td>471</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>474</td>
      <td>491</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>492</td>
      <td>505</td>
      <td>490</td>
      <td>503</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>514</td>
      <td>511</td>
      <td>512</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>515</td>
      <td>534</td>
      <td>513</td>
      <td>532</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>535</td>
      <td>539</td>
      <td>533</td>
      <td>537</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>540</td>
      <td>555</td>
      <td>538</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>868</td>
      <td>554</td>
      <td>866</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>869</td>
      <td>884</td>
      <td>867</td>
      <td>882</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>885</td>
      <td>891</td>
      <td>883</td>
      <td>889</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>892</td>
      <td>911</td>
      <td>890</td>
      <td>909</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>912</td>
      <td>922</td>
      <td>910</td>
      <td>920</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>923</td>
      <td>936</td>
      <td>921</td>
      <td>934</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>937</td>
      <td>967</td>
      <td>935</td>
      <td>965</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>968</td>
      <td>983</td>
      <td>966</td>
      <td>981</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>984</td>
      <td>996</td>
      <td>982</td>
      <td>994</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>997</td>
      <td>1011</td>
      <td>995</td>
      <td>1009</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1012</td>
      <td>1023</td>
      <td>1010</td>
      <td>1021</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1024</td>
      <td>1025</td>
      <td>1022</td>
      <td>1023</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7b8q">7B8Q</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MS</span><span class="topo-outside">MSQFFIRRPVF</span><span class="topo-membrane">AWVIAIFIIIFGLLS</span><span class="topo-inside">IPKLPIARFPSVAPPQVNISATYPGATAKTINDSVVTLIERELSGVKNLLYYSATTDTSGTAEITATFKPGTDVEMAQVDVQNKIKAVEARL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PQVVRQQGLQVEASSSGFLMLVGINSPNNQYSEVDLSDYLVRNVVEELKRVEGVGKVQSFGAEKAMRIWVDPNKLVSYGLSISDVNNAIRENNVEIAPGRLGDLPAEKGQLITIPLSAQG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">QLSSLEQFKNISLKSKTNGSVIKLSDVANVEIGSQAYNFAILENGKPATAAAIQLSPGANAVKTAEGVRAKIEELKLNLPEGMEFSIPYDTAPFVKISIEKVIH</span><span class="topo-membrane">TLLEAMVLVFIVMYL</span><span class="topo-outside">F</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">LHNVRYT</span><span class="topo-membrane">LIPAIVAPIALLGTFTVM</span><span class="topo-inside">LLAGFSINVLTMFG</span><span class="topo-membrane">MVLAIGIIVDDAI</span><span class="topo-outside">VVVENVERIMATEGLSPKDATSKAMKEITSPI</span><span class="topo-membrane">IGITLVLAAVFLPM</span><span class="topo-inside">AFASGSVGVIYKQF</span><span class="topo-membrane">TLTMSVSI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">LFSALLALIL</span><span class="topo-outside">TPALCATILKPIDG</span><span class="topo-unknown">HHQKKGFF</span><span class="topo-outside">AW</span><span class="topo-unknown">FDRSFDKVTKKYELMLLKIIK</span><span class="topo-outside">HTVP</span><span class="topo-membrane">MMVIFLVITGITFAGM</span><span class="topo-inside">KYWPTAFMPEEDQGWFMTSFQLPSDATAERTRNVVNQFENNLKDN</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">PDVKSNTAILGWGFSGAGQNVAVAFTTLKDFKERTSSASKMTSDVNSSMANSTEGETMAVLPPAIDELGTFSGFSLRLQDRANLGMPALLAAQDELMAMAAKNKKFYMVWNEGLPQGDNI</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">SLKIDREKLSALGVKFSDVSDIISTSMGSMYINDFPNQGRMQQVIVQVEAKSRMQLKDILNLKVMGSSGQLVSLSEVVTPQWNKAPQQYNRYNGRPSLSIAGIPNFDTSSGEAMREMEQL</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-inside">IAKLPKGIGYEWTGISLQEKQSESQMAF</span><span class="topo-membrane">LLGLSMLVVFLVLAAL</span><span class="topo-outside">YESWAIP</span><span class="topo-membrane">LSVMLVVPLGIFGAIIAI</span><span class="topo-inside">MSRGLMNDVFFKI</span><span class="topo-membrane">GLITIIGLSAKNAI</span><span class="topo-outside">LIVEFAKMLKEEGMSLIEATVAAA</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050      </span>
<span class="topo-line"><span class="topo-outside">KLRLRPI</span><span class="topo-membrane">LMTSLAFTCGVIPLVI</span><span class="topo-inside">ATGASSETQHALG</span><span class="topo-membrane">TGVFGGMISATILAI</span><span class="topo-outside">F</span><span class="topo-unknown">FVPVFFIFILG</span><span class="topo-outside">AV</span><span class="topo-unknown">EKLFSSKKKISSALEVLFQGPHHHHHHHHHH</span></span>
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
      <td>3</td>
      <td>13</td>
      <td>1</td>
      <td>11</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>28</td>
      <td>12</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>344</td>
      <td>27</td>
      <td>342</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>345</td>
      <td>359</td>
      <td>343</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>360</td>
      <td>367</td>
      <td>358</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>385</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>386</td>
      <td>399</td>
      <td>384</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>412</td>
      <td>398</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>444</td>
      <td>411</td>
      <td>442</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>458</td>
      <td>443</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>472</td>
      <td>457</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>473</td>
      <td>490</td>
      <td>471</td>
      <td>488</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>491</td>
      <td>504</td>
      <td>489</td>
      <td>502</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>514</td>
      <td>511</td>
      <td>512</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>515</td>
      <td>535</td>
      <td>513</td>
      <td>533</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>536</td>
      <td>539</td>
      <td>534</td>
      <td>537</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>540</td>
      <td>555</td>
      <td>538</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>868</td>
      <td>554</td>
      <td>866</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>869</td>
      <td>884</td>
      <td>867</td>
      <td>882</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>885</td>
      <td>891</td>
      <td>883</td>
      <td>889</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>892</td>
      <td>909</td>
      <td>890</td>
      <td>907</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>910</td>
      <td>922</td>
      <td>908</td>
      <td>920</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>923</td>
      <td>936</td>
      <td>921</td>
      <td>934</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>937</td>
      <td>967</td>
      <td>935</td>
      <td>965</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>968</td>
      <td>983</td>
      <td>966</td>
      <td>981</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>984</td>
      <td>996</td>
      <td>982</td>
      <td>994</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>997</td>
      <td>1011</td>
      <td>995</td>
      <td>1009</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1012</td>
      <td>1012</td>
      <td>1010</td>
      <td>1010</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1013</td>
      <td>1023</td>
      <td>1011</td>
      <td>1021</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1024</td>
      <td>1025</td>
      <td>1022</td>
      <td>1023</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7b8q">7B8Q</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MS</span><span class="topo-outside">MSQFFIRRPV</span><span class="topo-membrane">FAWVIAIFIIIFGLL</span><span class="topo-inside">SIPKLPIARFPSVAPPQVNISATYPGATAKTINDSVVTLIERELSGVKNLLYYSATTDTSGTAEITATFKPGTDVEMAQVDVQNKIKAVEARL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">PQVVRQQGLQVEASSSGFLMLVGINSPNNQYSEVDLSDYLVRNVVEELKRVEGVGKVQSFGAEKAMRIWVDPNKLVSYGLSISDVNNAIRENNVEIAPGRLGDLPAEKGQLITIPLSAQG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">QLSSLEQFKNISLKSKTNGSVIKLSDVANVEIGSQAYNFAILENGKPATAAAIQLSPGANAVKTAEGVRAKIEELKLNLPEGMEFSIPYDTAPFVKISIEKVIHT</span><span class="topo-membrane">LLEAMVLVFIVMYLF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">LHNVRYT</span><span class="topo-membrane">LIPAIVAPIALLGTFTV</span><span class="topo-inside">MLLAGFSINVLTMFG</span><span class="topo-membrane">MVLAIGIIVDDAI</span><span class="topo-outside">VVVENVERIMATEGLSPKDATSKAMKEITSPI</span><span class="topo-membrane">IGITLVLAAVFLPM</span><span class="topo-inside">AFASGSVGVIYKQF</span><span class="topo-membrane">TLTMSVSI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">LFSALLALILT</span><span class="topo-outside">PALCATILKPIDG</span><span class="topo-unknown">HHQKKGFF</span><span class="topo-outside">AW</span><span class="topo-unknown">FDRSFDKVTKKYELMLLKIIK</span><span class="topo-outside">HTVPM</span><span class="topo-membrane">MVIFLVITGITFAGM</span><span class="topo-inside">KYWPTAFMPEEDQGWFMTSFQLPSDATAERTRNVVNQFENNLKDN</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">PDVKSNTAILGWGFSGAGQNVAVAFTTLKDFKERTSSASKMTSDVNSSMANSTEGETMAVLPPAIDELGTFSGFSLRLQDRANLGMPALLAAQDELMAMAAKNKKFYMVWNEGLPQGDNI</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">SLKIDREKLSALGVKFSDVSDIISTSMGSMYINDFPNQGRMQQVIVQVEAKSRMQLKDILNLKVMGSSGQLVSLSEVVTPQWNKAPQQYNRYNGRPSLSIAGIPNFDTSSGEAMREMEQL</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-inside">IAKLPKGIGYEWTGISLQEKQSESQMAF</span><span class="topo-membrane">LLGLSMLVVFLVLAAL</span><span class="topo-outside">YESWAIP</span><span class="topo-membrane">LSVMLVVPLGIFGAIIAI</span><span class="topo-inside">MSRGLMNDVFFKI</span><span class="topo-membrane">GLITIIGLSAKNAI</span><span class="topo-outside">LIVEFAKMLKEEGMSLIEATVAAA</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050      </span>
<span class="topo-line"><span class="topo-outside">KLRLRPI</span><span class="topo-membrane">LMTSLAFTCGVIPLVI</span><span class="topo-inside">ATGASSETQHALG</span><span class="topo-membrane">TGVFGGMISATILAI</span><span class="topo-outside">F</span><span class="topo-unknown">FVPVFFIFILG</span><span class="topo-outside">AV</span><span class="topo-unknown">EKLFSSKKKISSALEVLFQGPHHHHHHHHHH</span></span>
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
      <td>3</td>
      <td>12</td>
      <td>1</td>
      <td>10</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>27</td>
      <td>11</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>28</td>
      <td>345</td>
      <td>26</td>
      <td>343</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>346</td>
      <td>360</td>
      <td>344</td>
      <td>358</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>361</td>
      <td>367</td>
      <td>359</td>
      <td>365</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>368</td>
      <td>384</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>385</td>
      <td>399</td>
      <td>383</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>412</td>
      <td>398</td>
      <td>410</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>444</td>
      <td>411</td>
      <td>442</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>445</td>
      <td>458</td>
      <td>443</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>459</td>
      <td>472</td>
      <td>457</td>
      <td>470</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>473</td>
      <td>491</td>
      <td>471</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>492</td>
      <td>504</td>
      <td>490</td>
      <td>502</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>514</td>
      <td>511</td>
      <td>512</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>515</td>
      <td>535</td>
      <td>513</td>
      <td>533</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>536</td>
      <td>540</td>
      <td>534</td>
      <td>538</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>541</td>
      <td>555</td>
      <td>539</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>868</td>
      <td>554</td>
      <td>866</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>869</td>
      <td>884</td>
      <td>867</td>
      <td>882</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>885</td>
      <td>891</td>
      <td>883</td>
      <td>889</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>892</td>
      <td>909</td>
      <td>890</td>
      <td>907</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>910</td>
      <td>922</td>
      <td>908</td>
      <td>920</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>923</td>
      <td>936</td>
      <td>921</td>
      <td>934</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>937</td>
      <td>967</td>
      <td>935</td>
      <td>965</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>968</td>
      <td>983</td>
      <td>966</td>
      <td>981</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>984</td>
      <td>996</td>
      <td>982</td>
      <td>994</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>997</td>
      <td>1011</td>
      <td>995</td>
      <td>1009</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1012</td>
      <td>1012</td>
      <td>1010</td>
      <td>1010</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1013</td>
      <td>1023</td>
      <td>1011</td>
      <td>1021</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1024</td>
      <td>1025</td>
      <td>1022</td>
      <td>1023</td>
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

### OOO resting state predominates in AdeB

The AdeB trimer adopts predominantly a symmetric OOO conformation (all protomers in the O/extrusion state), in contrast to the asymmetric LTO states of [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/). This conformation lacks drug entry channels and binding sites, suggesting tight regulation of AdeB activity. The high prevalence of the OOO state is not an artifact, as similar symmetric conformations have been observed in C. jejuni [Campylobacter jejuni CmeB Multidrug Efflux Pump](/xray-mp-wiki/proteins/abc-transporters/cmeb/) and another AdeB [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) study.

### L*OO - a novel pre-binding conformation

Approximately 10% of AdeB protomers adopt the L* conformation, a previously undiscovered state. L* reveals three entry tunnels (CH1-CH3) leading to the closed DBP, analogous to [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) channels. The L* protomer most closely resembles the [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) T conformation (RMSD 0.68 A over C-alpha), but PN2 and PC1 subdomains differ significantly from both L and T states. The L* conformation may be the first state in the AdeB transport cycle, allowing initial substrate entry in the absence of drugs.

### Different drug binding mechanisms between AdeB and AcrB

Mutagenesis of 20 AdeB DBP variants and comparison with [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) reveals distinct substrate preferences. AdeB confers higher resistance to polyaromatic compounds, while [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) shows higher resistance to non-polyaromatic antibiotics. For AdeB, drug binding may proceed via induced fit (drug binds to AP first, inducing DBP opening), whereas [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/) appears to use conformational selection. Removal of bulky Phe/Tyr residues in the AdeB DBP generally widens the binding pocket, affecting substrate specificity differently than equivalent substitutions in [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/).


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">AcrB Multidrug Efflux Transporter</a> — Homologous RND efflux transporter from E. coli; detailed structural and functional comparison in this study
- <a href="/xray-mp-wiki/proteins/abc-transporters/mexb/">MexB Multidrug Efflux Transporter</a> — Homologous RND transporter from P. aeruginosa with similar tripartite efflux pump architecture
- <a href="/xray-mp-wiki/concepts/multidrug-resistance/">Multidrug Resistance Mechanisms</a> — AdeB is a key RND efflux pump contributing to multidrug resistance in A. baumannii
- <a href="/xray-mp-wiki/methods/structure-determination/single-particle-cryo-em/">Single-Particle Cryo-Electron Microscopy</a> — AdeB structures determined by single-particle cryo-EM
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Method used in the study
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — Method used in the study
- <a href="/xray-mp-wiki/proteins/rhodopsins/gr/">GR (Halobacterium sp. GR Bacteriorhodopsin)</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/proteins/abc-transporters/mexB/">MexB (Pseudomonas aeruginosa multidrug exporter)</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">AcrB multidrug efflux pump</a> — Related protein mentioned in the study
- <a href="/xray-mp-wiki/proteins/abc-transporters/cmeb/">Campylobacter jejuni CmeB Multidrug Efflux Pump</a> — Related protein mentioned in the study
