---
title: "MexB (Pseudomonas aeruginosa multidrug exporter)"
created: 2026-05-26
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, pump, membrane-protein, xray-crystallography]
sources: [doi/10.1016##J.JMB.2009.04.001, doi/10.1038##nature12300]
verified: regex
uniprot_id: P52002
---

# MexB (Pseudomonas aeruginosa multidrug exporter)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P52002">UniProt: P52002</a>

<span class="expr-badge">Pseudomonas AERUGINOSA PA01</span>

## Overview

MexB is the inner-membrane component of the MexAB-OprM tripartite efflux pump in Pseudomonas aeruginosa, a major multidrug resistance system. It belongs to the resistance-nodulation-cell division ([RND](/xray-mp-wiki/concepts/protein-families/rnd-superfamily/)) superfamily of secondary active transporters. The crystal structure was solved at 3.0 A resolution, revealing an asymmetric [homotrimer](/xray-mp-wiki/concepts/structural-mechanisms/homotrimer/) where each subunit adopts a distinct conformation representing three snapshots of the transport cycle. A [DDM](/xray-mp-wiki/reagents/detergents/ddm/) molecule was found bound in the internal multidrug-binding cavity, supporting the model that [RND](/xray-mp-wiki/concepts/protein-families/rnd-superfamily/) transporters can transport detergent molecules as substrates. The first inhibitor-bound structure of MexB was solved with the pyridopyrimidine derivative [ABI-PP](/xray-mp-wiki/reagents/ligands/abi-pp), revealing that the inhibitor binds to a hydrophobic trap in the distal drug-binding pocket, similar to [ACRB](/xray-mp-wiki/proteins/acrB).


## Publications

### doi/10.1016##J.JMB.2009.04.001

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2v50">2V50</a></td>
      <td>3.0 A</td>
      <td>P1</td>
      <td>MexB from P. aeruginosa PAO1 (1046 amino acids); <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/">C-terminal</a> <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">hexahistidine</a> tag; two almost structurally identical trimers (chains ABC and DEF) in the asymmetric unit</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (n-dodecyl-D-maltoside) bound in the multidrug-binding cavity of subunit B</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli strain C43 (DE3) (wild-type), E. coli MG1655 ([ACRB](/xray-mp-wiki/proteins/acrB)-deficient, for F178W mutant)
- **Construct**: MexB from P. aeruginosa PAO1 with [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) [hexahistidine](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag, overproduced from plasmid pUCP20-B_His. MexB(F178W) mutant expressed from plasmid pUC118mexB F178W (pUC118 DNA, Takara Bio) in [ACRB](/xray-mp-wiki/proteins/acrB)-deficient E. coli strain MG1655. Expression induced with 0.1 mM [IPTG](/xray-mp-wiki/methods/expression-systems/iptg-induction/) for 4 h at 37 deg.C.

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
      <td>Cell lysis</td>
      <td><a href="/xray-mp-wiki/methods/cell-lysis/french-press/">French press</a></td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF</a>, <a href="/xray-mp-wiki/reagents/additives/dnase/">DNase</a> I, complete protease inhibitor cocktail + --</td>
      <td>Membranes collected by centrifugation at 100,000g for 1 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + 1% (wt/vol) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (D310LA Anagrade; Anatrace)</td>
      <td>Solubilized for 2 h at 4 deg.C; insoluble material removed by centrifugation at 100,000g for 1 h</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (<a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a>)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> affinity column (Qiagen)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (equilibration); 30 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (wash); 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (elution) + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td><a href="/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/">C-terminal</a> <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">hexahistidine</a> tag purification; column equilibrated with buffer A containing 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>Tricorn <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> column (Amersham Biosciences)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Further purification and buffer exchange for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a>-purified MexB in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 7.5, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>; concentrated prior to crystallization</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>not specified in paper text</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals belong to space group P1 with two trimers in the asymmetric unit. Structure solved at 3.0 A resolution by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">molecular replacement</a> using the asymmetric <a href="/xray-mp-wiki/proteins/acrB">ACRB</a> structure (PDB 2J8S) as search model. R-factors: R = 24.3%, R_free = 28.7%, with 2-fold noncrystallographic symmetry applied.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2v50">2V50</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MSK</span><span class="topo-inside">FFIDRPI</span><span class="topo-membrane">FAWVIALVIMLAGG</span><span class="topo-outside">LSILSLPVNQYPAIAPPAIAVQVSYPGASAETVQDTVVQVIEQQMNGIDNLRYISSESNSDGSMTITVTFEQGTDPDIAQVQVQNKLQLATPLLPQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EVQRQGIRVTKAVKNFLMVVGVVSTDGSMTKEDLSNYIVSNIQDPLSRTKGVGDFQVFGSQYSMRIWLDPAKLNSYQLTPGDVSSAIQAQNVQISSGQLGGLPAVKGQQLNATIIGKTRL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">QTAEQFENILLKVNPDGSQVRLKDVADVGLGGQDYSINAQFNGSPASGIAIKLATGANALDTAKAIRQTIANLEPFMPQGMKVVYPYDTTPVVSASIHEVVKT</span><span class="topo-membrane">LGEAILLVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFGV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDA</span><span class="topo-inside">IVVVENVERVMAEEGLSPREAARKSMGQIQGALV</span><span class="topo-membrane">GIAMVLSAVFLPM</span><span class="topo-outside">AFFGGSTGVIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">SVIVALILT</span><span class="topo-unknown">PALCATM</span><span class="topo-inside">LKP</span><span class="topo-unknown">IEKGDHGEHKGG</span><span class="topo-inside">F</span><span class="topo-unknown">FGWFNRMFLSTTHGYERGVASILKH</span><span class="topo-inside">RAPYL</span><span class="topo-membrane">LIYVVIVAGMIWM</span><span class="topo-outside">FTRIPTAFLPDEDQGVLFAQVQTPPGSSAERTQVVVDSMREYLLE</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">KESSSVSSVFTVTGFNFAGRGQSSGMAFIMLKPWEERPGGENSVFELAKRAQMHFFSFKDAMVFAFAPPSVL</span><span class="topo-unknown">ELGNA</span><span class="topo-outside">TGFDLFLQDQAGVGHEVLLQARNKFLMLAAQNPALQRVRPNGM</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">SDEPQYKLEIDDEKASALGVSLADINSTVSIAWGSSYVNDFIDRGRVKRVYLQGRPDARMNPDDLSKWYVRNDKGEMVPFNAFATGKWEYGSPKLERYNGVPAMEILGEPAPGLSSGDAM</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">AAVEEIVKQLPKGVGYSWTGLSYEERLSGSQAPAL</span><span class="topo-membrane">YALSLLVVFLCLA</span><span class="topo-inside">ALYESWSIPFSV</span><span class="topo-membrane">MLVVPLGVIGALLA</span><span class="topo-outside">TSMRGLSNDVFFQV</span><span class="topo-membrane">GLLTTIGLSAKNA</span><span class="topo-inside">ILIVEFAKELHEQGKGIVE</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050  </span>
<span class="topo-line"><span class="topo-inside">AAIEACRMRLRPI</span><span class="topo-membrane">VMTSLAFILGVVPLA</span><span class="topo-outside">ISTGAGSGSQHAIG</span><span class="topo-membrane">TGVIGGMVTATVLA</span><span class="topo-unknown">IFWVPLF</span><span class="topo-inside">YV</span><span class="topo-unknown">AVSTLFKDEASKQQASVEKGQHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (35 regions)</summary>
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
      <td>10</td>
      <td>4</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>24</td>
      <td>11</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>343</td>
      <td>25</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>382</td>
      <td>366</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>409</td>
      <td>398</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>443</td>
      <td>410</td>
      <td>443</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>444</td>
      <td>456</td>
      <td>444</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>471</td>
      <td>457</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>496</td>
      <td>490</td>
      <td>496</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>497</td>
      <td>499</td>
      <td>497</td>
      <td>499</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>500</td>
      <td>511</td>
      <td>500</td>
      <td>511</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>512</td>
      <td>512</td>
      <td>512</td>
      <td>512</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>537</td>
      <td>513</td>
      <td>537</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>538</td>
      <td>542</td>
      <td>538</td>
      <td>542</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>543</td>
      <td>555</td>
      <td>543</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>672</td>
      <td>556</td>
      <td>672</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>673</td>
      <td>677</td>
      <td>673</td>
      <td>677</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>678</td>
      <td>875</td>
      <td>678</td>
      <td>875</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>876</td>
      <td>888</td>
      <td>876</td>
      <td>888</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>889</td>
      <td>900</td>
      <td>889</td>
      <td>900</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>901</td>
      <td>914</td>
      <td>901</td>
      <td>914</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>915</td>
      <td>928</td>
      <td>915</td>
      <td>928</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>929</td>
      <td>941</td>
      <td>929</td>
      <td>941</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>942</td>
      <td>973</td>
      <td>942</td>
      <td>973</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>974</td>
      <td>988</td>
      <td>974</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1002</td>
      <td>989</td>
      <td>1002</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1003</td>
      <td>1016</td>
      <td>1003</td>
      <td>1016</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1017</td>
      <td>1023</td>
      <td>1017</td>
      <td>1023</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1024</td>
      <td>1025</td>
      <td>1024</td>
      <td>1025</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1026</td>
      <td>1052</td>
      <td>1026</td>
      <td>1052</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2v50">2V50</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MSKFFIDRPI</span><span class="topo-membrane">FAWVIALVIMLAGG</span><span class="topo-outside">LSILSLPVNQYPAIAPPAIAVQVSYPGASAETVQDTVVQVIEQQMNGIDNLRYISSESNSDGSMTITVTFEQGTDPDIAQVQVQNKLQLATPLLPQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EVQRQGIRVTKAVKNFLMVVGVVSTDGSMTKEDLSNYIVSNIQDPLSRTKGVGDFQVFGSQYSMRIWLDPAKLNSYQLTPGDVSSAIQAQNVQISSGQLGGLPAVKGQQLNATIIGKTRL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">QTAEQFENILLKVNPDGSQVRLKDVADVGLGGQDYSINAQFNGSPASGIAIKLATGANALDTAKAIRQTIANLEPFMPQGMKVVYPYDTTPVVSASIHEVVKT</span><span class="topo-membrane">LGEAILLVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGT</span><span class="topo-outside">FGVLAAFGFSINTLTMFGMV</span><span class="topo-membrane">LAIGLLVDDAIVV</span><span class="topo-inside">VENVERVMAEEGLSPREAARKSMGQIQG</span><span class="topo-membrane">ALVGIAMVLSAVFL</span><span class="topo-outside">PMAFFGGSTGVIYRQFSITI</span><span class="topo-membrane">VSAMAL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">SVIVALILT</span><span class="topo-inside">PALCATMLKPIEKGDHGEHKG</span><span class="topo-unknown">GFFGWFNRMFLSTTHGYERGVASILK</span><span class="topo-inside">HRA</span><span class="topo-membrane">PYLLIYVVIVAGMI</span><span class="topo-outside">WMFTRIPTAFLPDEDQGVLFAQVQTPPGSSAERTQVVVDSMREYLLE</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">KESSSVSSVFTVTGFNFAGRGQSSGMAFIMLKPWEERPGGENSVFELAKRAQMHFFSFKDAMVFAFAPPSVLELGNATGFDLFLQDQAGVGHEVLLQARNKFLMLAAQNPALQRVRPNGM</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">SDEPQYKLEIDDEKASALGVSLADINSTVSIAWGSSYVNDFIDRGRVKRVYLQGRPDARMNPDDLSKWYVRNDKGEMVPFNAFATGKWEYGSPKLERYNGVPAMEILGEPAPGLSSGDAM</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">AAVEEIVKQLPKGVGYSWTGLSYEERLSGSQAPALYA</span><span class="topo-membrane">LSLLVVFLCLAAL</span><span class="topo-inside">YESW</span><span class="topo-membrane">SIPFSVMLVVPLGVIGA</span><span class="topo-outside">LLATSMRGLSNDVFFQVGL</span><span class="topo-membrane">LTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKELHEQGKGIVE</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050  </span>
<span class="topo-line"><span class="topo-inside">AAIEACRMRLRP</span><span class="topo-membrane">IVMTSLAFILGVV</span><span class="topo-outside">PLAISTGAGSGSQHAIGTGV</span><span class="topo-membrane">IGGMVTATVLAIFWV</span><span class="topo-unknown">PLFYVAVST</span><span class="topo-inside">L</span><span class="topo-unknown">FKDEASKQQASVEKGQHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>24</td>
      <td>11</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>25</td>
      <td>343</td>
      <td>25</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>379</td>
      <td>366</td>
      <td>379</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>380</td>
      <td>399</td>
      <td>380</td>
      <td>399</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>400</td>
      <td>412</td>
      <td>400</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>440</td>
      <td>413</td>
      <td>440</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>454</td>
      <td>441</td>
      <td>454</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>455</td>
      <td>474</td>
      <td>455</td>
      <td>474</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>475</td>
      <td>489</td>
      <td>475</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>510</td>
      <td>490</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>511</td>
      <td>536</td>
      <td>511</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>539</td>
      <td>537</td>
      <td>539</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>540</td>
      <td>553</td>
      <td>540</td>
      <td>553</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>554</td>
      <td>877</td>
      <td>554</td>
      <td>877</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>878</td>
      <td>890</td>
      <td>878</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>894</td>
      <td>891</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>911</td>
      <td>895</td>
      <td>911</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>912</td>
      <td>930</td>
      <td>912</td>
      <td>930</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>931</td>
      <td>943</td>
      <td>931</td>
      <td>943</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>944</td>
      <td>972</td>
      <td>944</td>
      <td>972</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>973</td>
      <td>985</td>
      <td>973</td>
      <td>985</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>986</td>
      <td>1005</td>
      <td>986</td>
      <td>1005</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1006</td>
      <td>1020</td>
      <td>1006</td>
      <td>1020</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1021</td>
      <td>1029</td>
      <td>1021</td>
      <td>1029</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1030</td>
      <td>1030</td>
      <td>1030</td>
      <td>1030</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1031</td>
      <td>1052</td>
      <td>1031</td>
      <td>1052</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2v50">2V50</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MSKFFIDRPIFA</span><span class="topo-membrane">WVIALVIMLAGGL</span><span class="topo-outside">SILSLPVNQYPAIAPPAIAVQVSYPGASAETVQDTVVQVIEQQMNGIDNLRYISSESNSDGSMTITVTFEQGTDPDIAQVQVQNKLQLATPLLPQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EVQRQGIRVTKAVKNFLMVVGVVSTDGSMTKEDLSNYIVSNIQDPLSRTKGVGDFQVFGSQYSMRIWLDPAKLNSYQLTPGDVSSAIQAQNVQISSGQLGGLPAVKGQQLNATIIGKTRL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">QTAEQFENILLKVNPDGSQVRLKDVADVGLGGQDYSINAQFNGSPASGIAIKLATGANALDTAKAIRQTIANLEPFMPQGMKVVYPYDTTPVVSASIHEVVKT</span><span class="topo-membrane">LGEAILLVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NFRATL</span><span class="topo-membrane">IPTIAVPVVLLGTFGV</span><span class="topo-outside">LAAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDA</span><span class="topo-inside">IVVVENVERVMAEEGLSPREAARKSMGQIQGAL</span><span class="topo-membrane">VGIAMVLSAVFLP</span><span class="topo-outside">MAFFGGSTGVIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">SVIVA</span><span class="topo-inside">LILTPALCATMLKPIEKGDHGEHKGG</span><span class="topo-unknown">FFGWFNRMFLSTTHGYERGVASILK</span><span class="topo-inside">HRAPY</span><span class="topo-membrane">LLIYVVIVAGMIWM</span><span class="topo-outside">FTRIPTAFLPDEDQGVLFAQVQTPPGSSAERTQVVVDSMREYLLE</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">KESSSVSSVFTVTGFNFAGRGQSSGMAFIMLKPWEERPGGENSVFELAKRAQMHFFSFKDAMVFAFAPPSVLELGNATGFDLFLQDQAGVGHEVLLQARNKFLMLAAQNPALQRVRPNGM</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">SDEPQYKLEIDDEKASALGVSLADINSTVSIAWGSSYVNDFIDRGRVKRVYLQGRPDARMNPDDLSKWYVRNDKGEMVPFNAFATGKWEYGSPKLERYNGVPAMEILGEPAPGLSSGDAM</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">AAVEEIVKQLPKGVGYSWTGLSYEERLSGSQAPALY</span><span class="topo-membrane">ALSLLVVFLCLAAL</span><span class="topo-inside">YESWSIP</span><span class="topo-membrane">FSVMLVVPLGVIGALLA</span><span class="topo-outside">TSMRGLSNDVFFQVG</span><span class="topo-membrane">LLTTIGLSAKNAI</span><span class="topo-inside">LIVEFAKELHEQGKGIVE</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050  </span>
<span class="topo-line"><span class="topo-inside">AAIEACRMRLRPI</span><span class="topo-membrane">VMTSLAFILGVVPLA</span><span class="topo-outside">ISTGAGSGSQHAIG</span><span class="topo-membrane">TGVIGGMVTATVLA</span><span class="topo-unknown">IFWVPLFYVAVS</span><span class="topo-inside">TL</span><span class="topo-unknown">FKDEASKQQASVEKGQHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>12</td>
      <td>1</td>
      <td>12</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>13</td>
      <td>25</td>
      <td>13</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>343</td>
      <td>26</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>344</td>
      <td>357</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>366</td>
      <td>358</td>
      <td>366</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>382</td>
      <td>367</td>
      <td>382</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>383</td>
      <td>397</td>
      <td>383</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>409</td>
      <td>398</td>
      <td>409</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>410</td>
      <td>442</td>
      <td>410</td>
      <td>442</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>443</td>
      <td>455</td>
      <td>443</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>471</td>
      <td>456</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>485</td>
      <td>472</td>
      <td>485</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>486</td>
      <td>511</td>
      <td>486</td>
      <td>511</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>536</td>
      <td>512</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>541</td>
      <td>537</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>555</td>
      <td>542</td>
      <td>555</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>876</td>
      <td>556</td>
      <td>876</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>877</td>
      <td>890</td>
      <td>877</td>
      <td>890</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>891</td>
      <td>897</td>
      <td>891</td>
      <td>897</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>898</td>
      <td>914</td>
      <td>898</td>
      <td>914</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>915</td>
      <td>929</td>
      <td>915</td>
      <td>929</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>942</td>
      <td>930</td>
      <td>942</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>943</td>
      <td>973</td>
      <td>943</td>
      <td>973</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>974</td>
      <td>988</td>
      <td>974</td>
      <td>988</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>989</td>
      <td>1002</td>
      <td>989</td>
      <td>1002</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1003</td>
      <td>1016</td>
      <td>1003</td>
      <td>1016</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1017</td>
      <td>1028</td>
      <td>1017</td>
      <td>1028</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1029</td>
      <td>1030</td>
      <td>1029</td>
      <td>1030</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1031</td>
      <td>1052</td>
      <td>1031</td>
      <td>1052</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nature12300

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
      <td>3.15 A</td>
      <td>P1</td>
      <td>MexB from P. aeruginosa with <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/">C-terminal</a> polyhistidine tag, complexed with <a href="/xray-mp-wiki/reagents/ligands/abi-pp">ABI-PP</a> inhibitor</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/abi-pp">ABI-PP</a> (tert-butyl thiazolyl aminocarboxyl pyridopyrimidine)</td>
    </tr>
    <tr>
      <td></td>
      <td>2.70 A</td>
      <td>P1</td>
      <td>Drug-free MexB from P. aeruginosa with <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/">C-terminal</a> polyhistidine tag</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (n-dodecyl-beta-D-maltoside) bound in distal pocket</td>
    </tr>
    <tr>
      <td></td>
      <td>3.30 A</td>
      <td>P1</td>
      <td>Drug-free MexB(F178W) mutant with <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/">C-terminal</a> polyhistidine tag</td>
      <td>None (drug-free)</td>
    </tr>
    <tr>
      <td></td>
      <td>3.00 A</td>
      <td>P1</td>
      <td>MexB(F178W) mutant with <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/">C-terminal</a> polyhistidine tag, complexed with <a href="/xray-mp-wiki/reagents/ligands/abi-pp">ABI-PP</a> inhibitor</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/abi-pp">ABI-PP</a> (tert-butyl thiazolyl aminocarboxyl pyridopyrimidine)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli strain C43 (DE3) (wild-type), E. coli MG1655 ([ACRB](/xray-mp-wiki/proteins/acrB)-deficient, for F178W mutant)
- **Construct**: MexB from P. aeruginosa PAO1 with [C-terminal](/xray-mp-wiki/concepts/structural-mechanisms/c-terminus/) [hexahistidine](/xray-mp-wiki/reagents/protein-tags/his6-tag/) tag, overproduced from plasmid pUCP20-B_His. MexB(F178W) mutant expressed from plasmid pUC118mexB F178W (pUC118 DNA, Takara Bio) in [ACRB](/xray-mp-wiki/proteins/acrB)-deficient E. coli strain MG1655. Expression induced with 0.1 mM [IPTG](/xray-mp-wiki/methods/expression-systems/iptg-induction/) for 4 h at 37 deg.C.

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
      <td>Cell culture and membrane isolation</td>
      <td>High-pressure homogenizer (APV 1000, SPX) at 180 MPa, membrane fractions collected by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a> at 158,000g for 90 min</td>
      <td>--</td>
      <td>-- + --</td>
      <td>E. coli MG1655 (<a href="/xray-mp-wiki/proteins/acrB">ACRB</a>-deficient) grown to A580nm of 0.7 at 37 deg.C; MexB expression induced with 0.1 mM <a href="/xray-mp-wiki/methods/expression-systems/iptg-induction/">IPTG</a> for 4 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane solubilization</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> (pH 7.5), 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a> + 1.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (D316, Dojindo)</td>
      <td>Membrane fractions solubilized in 1.5% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>; solubilized mixture centrifuged for 1 h at 172,000g</td>
    </tr>
    <tr>
      <td>Ni-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Ni-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (Ni Sepharose Fast Flow)</td>
      <td>Ni Sepharose Fast Flow (GE Healthcare)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> (pH 7.5), 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (equilibration); 25 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (wash); 140 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (wash); 350 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> (elution) + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Column pre-equilibrated with buffer A containing 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>; washed with 25 mM and 140 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a>; MexB eluted with 350 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a></td>
    </tr>
    <tr>
      <td>Concentration and buffer exchange</td>
      <td>Concentration-dilution using Amicon stirred cell (Model 8010, Millipore)</td>
      <td>--</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> (pH 7.5), 50 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Three concentration-dilution steps; final protein concentration approximately 30 mg/mL</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">hanging-drop</a> <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>25 mg/mL MexB</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>50 mM Na <a href="/xray-mp-wiki/reagents/buffers/acetate">Acetate Buffer</a>-HCl (pH 5.5), 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 26% (v/v) polyethylene glycol 400</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>equal volumes protein to reservoir</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>25 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Crystals appeared within 5 days, collected after further 5 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Polyethylene glycol 400 concentration increased to 40% (v/v) in three steps; crystals flash frozen in liquid nitrogen or cryostream (100 K)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Drug-free MexB crystallized using <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>. P1 crystals solved at 2.70 A resolution. Electron density corresponding to entire <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> molecule evident in distal pocket. Data collected at BL44XU beamline at SPring-8 with MX225-HE CCD detector at 100 K. Crystals processed using HKL2000. Structure largely identical to 3.0 A structure in ref. 25.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">hanging-drop</a> <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>25 mg/mL MexB with <a href="/xray-mp-wiki/reagents/ligands/abi-pp">ABI-PP</a>, inhibitor:protein molar ratio 5:1</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>50 mM Na <a href="/xray-mp-wiki/reagents/buffers/acetate">Acetate Buffer</a>-HCl (pH 5.5), 300 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 26% (v/v) polyethylene glycol 400</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>equal volumes protein to reservoir</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>25 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Crystals appeared within 5 days, collected after further 5 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Polyethylene glycol 400 concentration increased to 40% (v/v) in three steps; crystals flash frozen in liquid nitrogen or cryostream (100 K)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/abi-pp">ABI-PP</a>-bound MexB crystallized using <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>. P1 crystals solved at 3.15 A resolution. Fo-Fc omit map contoured at 3.0 sigma. The hydrophobic TAP moiety of <a href="/xray-mp-wiki/reagents/ligands/abi-pp">ABI-PP</a> inserts into narrow hydrophobic trap surrounded by F136, F178, F610, F615, F628 and F573. Hydrophilic tetrazole ring interacts with D274, R620 and K151. PAEA moiety extends towards R128 in MexB (different from <a href="/xray-mp-wiki/proteins/acrB">ACRB</a> where it is bent between piperidine ring and aceto-amino ethylene ammonio-<a href="/xray-mp-wiki/reagents/buffers/acetate">Acetate Buffer</a> group).</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">hanging-drop</a> <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Drug-free MexB(F178W) mutant</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Similar conditions to wild-type MexB, except <a href="/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-thioglucoside/">n-octyl-beta-D-thioglucoside</a> used as additive</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>Similar to wild-type</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>25 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Similar to wild-type</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Polyethylene glycol 400 concentration increased to 40% (v/v) in three steps; crystals flash frozen in liquid nitrogen or cryostream (100 K)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Drug-free MexB(F178W) crystallized using <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> with <a href="/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-thioglucoside/">n-octyl-beta-D-thioglucoside</a> as additive. P1 crystals solved at 3.30 A resolution. Overall structure almost identical to wild-type MexB. Indolyl side chain of W178 does not protrude towards hydrophobic trap because space is partially occupied by bound <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> molecule.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">hanging-drop</a> <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>MexB(F178W) mutant with <a href="/xray-mp-wiki/reagents/ligands/abi-pp">ABI-PP</a>, inhibitor:protein molar ratio 5:1</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Similar conditions to wild-type MexB</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>Similar to wild-type</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>25 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Similar to wild-type</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Polyethylene glycol 400 concentration increased to 40% (v/v) in three steps; crystals flash frozen in liquid nitrogen or cryostream (100 K)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/abi-pp">ABI-PP</a>-bound MexB(F178W) crystallized using <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>. P1 crystals solved at 3.00 A resolution. <a href="/xray-mp-wiki/reagents/ligands/abi-pp">ABI-PP</a> detected in hydrophobic trap as in wild-type MexB. Indolyl ring of W178 fits into position capable of forming pi-pi interactions with pyridopyrimidine ring without large <a href="/xray-mp-wiki/concepts/structural-mechanisms/conformational-change/">conformational change</a> relative to <a href="/xray-mp-wiki/reagents/ligands/abi-pp">ABI-PP</a>-free structure.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Asymmetric homotrimer transport mechanism

MexB adopts an asymmetric [homotrimeric](/xray-mp-wiki/concepts/structural-mechanisms/homotrimer/) conformation where each subunit represents a different
state in the transport cycle. Subunit B (binding) exhibits a channel open to the [periplasm](/xray-mp-wiki/concepts/miscellaneous/periplasm/)
for substrate capture. Subunit C (extrusion) has a channel open toward the outer-membrane
factor docking site. Subunit A shows an altered conformation, likely representing a transitional
state, potentially influenced by crystal packing. The progression through conformations is
ABC rather than BAC.

### Multidrug-binding cavity with bound DDM

A large drug-binding cavity is formed by the four pore domain subdomains (PN1, PN2, PC1, PC2).
A [DDM](/xray-mp-wiki/reagents/detergents/ddm/) molecule was observed bound in subunit B, with the maltoside group interacting with
Val47, Ser48, Gln125, Val177, Gly179, Ser180, Gln273, and Arg620. The binding site corresponds
to minocycline and [Doxorubicin - Anthracycline Anticancer Drug](/xray-mp-wiki/reagents/ligands/doxorubicin) sites in [ACRB](/xray-mp-wiki/proteins/acrB), demonstrating that [RND](/xray-mp-wiki/concepts/protein-families/rnd-superfamily/) transporters can transport
detergent molecules as substrates. The cavity is rich in polar residues at the distal end and
aromatic residues at the proximal end.

### Proton translocation mechanism conserved with AcrB

The transmembrane region is highly conserved between MexB and [ACRB](/xray-mp-wiki/proteins/acrB), with key charged residues
Asp407, Asp408 (TM4) and Lys939 (TM10) forming a salt-bridge involved in proton translocation.
In subunit C, the lysine is tilted towards Thr976 (TM11), implicating a rigid-body shift of
TM5 towards TM4 and TM10, and [conformational changes](/xray-mp-wiki/concepts/structural-mechanisms/conformational-change/) in TM8. The [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) end of TM8,
connecting the transmembrane domain to the PC2 subdomain, adopts different conformations across
subunits and is believed to trigger the large [conformational changes](/xray-mp-wiki/concepts/structural-mechanisms/conformational-change/) in the pore domains.

### Structural differences in pore domain subunit A

Compared to [ACRB](/xray-mp-wiki/proteins/acrB), a shift of the PC2 subdomain results in closure of the [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) portal
in one subunit, with no access to the binding cavity observed. The portal from the membrane
bilayer leading to the channel of subunit B in MexB is more constricted than in [ACRB](/xray-mp-wiki/proteins/acrB), likely
due to a more helical conformation of the [N-terminal](/xray-mp-wiki/concepts/structural-mechanisms/n-terminus/) part of TM8. In MexB, TM8 in subunit B
is fully helical, whereas in [ACRB](/xray-mp-wiki/proteins/acrB) it varies from random-coil (subunit A) to fully helical
(subunit C).

### Electrostatic differences in binding pocket

The electrostatic surface potential of the MexB binding pocket is slightly more positive than
[ACRB](/xray-mp-wiki/proteins/acrB) due to two exposed arginine residues. Since minocycline is positively charged at the
crystallization pH of 4.5, the positive electrostatic potential may explain difficulties in
obtaining crystals of MexB-minocycline complexes. These subtle differences in binding pockets
likely underlie the altered substrate specificity between MexB and [ACRB](/xray-mp-wiki/proteins/acrB).

### Assembly of the tripartite MexAB-OprM system

The docking domains of MexB and [ACRB](/xray-mp-wiki/proteins/acrB) are very similar, each consisting of two subdomains with
a long protruding loop inserting into the neighboring subunit. Despite high structural
similarity, OprM and TolC are not interchangeable between MexAB and AcrAB systems. The high
specificity likely relies on the membrane fusion protein (MFP) rather than the outer-membrane
factor (OMF), consistent with the finding that [RND](/xray-mp-wiki/concepts/protein-families/rnd-superfamily/) transporters interact transiently with OMFs
at low affinity.

### Crystal packing influences subunit A conformation

The two trimers of MexB in the asymmetric unit pack head-to-head, substantially involving the
[periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) part with approximately 700 A^2 of surface area buried at this interface, mainly
through the PC2 subdomain of subunit A. The altered conformation of subunit A could be a result
of crystal contacts, but evidence suggests functional significance: the symmetry-related trimer
has an identical conformation, and the PC1 and PC2 domains show the smallest sequence
conservation between MexB and [ACRB](/xray-mp-wiki/proteins/acrB), suggesting this difference could be an intrinsic property
of MexB.

### ABI-PP binding to hydrophobic trap in MexB

The first inhibitor-bound structure of MexB was solved with [ABI-PP](/xray-mp-wiki/reagents/ligands/abi-pp) at 3.15 A resolution. The
[ABI-PP](/xray-mp-wiki/reagents/ligands/abi-pp) binding site in MexB is similar to that in [ACRB](/xray-mp-wiki/proteins/acrB). The hydrophobic TAP moiety inserts
into a narrow hydrophobic trap surrounded by F136, F178, F610, F615, F628 and F573. The
hydrophilic tetrazole ring interacts with D274, R620 and K151. The conformations of the [ABI-PP](/xray-mp-wiki/reagents/ligands/abi-pp)
moieties are almost the same as in [ACRB](/xray-mp-wiki/proteins/acrB). However, the PAEA moiety in MexB extends towards R128,
whereas in [ACRB](/xray-mp-wiki/proteins/acrB) it is bent between the piperidine ring and the aceto-amino ethylene ammonio-[Acetate Buffer](/xray-mp-wiki/reagents/buffers/acetate)
group. The distal pocket is separated into two parts: a relatively hydrophilic
substrate-translocation channel and a hydrophobic trap forming a deep and narrow fissure.

### DDM molecule bound in MexB distal pocket

The crystal structure of drug-free MexB at 2.70 A resolution revealed clear electron density
corresponding to an entire molecule of [DDM](/xray-mp-wiki/reagents/detergents/ddm/) in the distal pocket. The bound [DDM](/xray-mp-wiki/reagents/detergents/ddm/) partially
overlaps with the bound [ABI-PP](/xray-mp-wiki/reagents/ligands/abi-pp) in the narrow hydrophobic trap. This demonstrates that the
hydrophobic trap can accommodate both detergent molecules and small-molecule inhibitors, and
that [DDM](/xray-mp-wiki/reagents/detergents/ddm/) binding in this site may influence inhibitor accessibility.

### MexB(F178W) mutant retains ABI-PP sensitivity unlike AcrB(F178W)

Despite introducing the same F178W mutation in both [ACRB](/xray-mp-wiki/proteins/acrB) and MexB, the two mutants showed
different responses to [ABI-PP](/xray-mp-wiki/reagents/ligands/abi-pp). While [ACRB](/xray-mp-wiki/proteins/acrB)(F178W) lost sensitivity to [ABI-PP](/xray-mp-wiki/reagents/ligands/abi-pp), MexB(F178W)
remained fully inhibitable. Crystal structures revealed that the indolyl side chain of W178
in MexB(F178W) does not protrude towards the hydrophobic trap because that space is partially
occupied by a [DDM](/xray-mp-wiki/reagents/detergents/ddm/) molecule, as in wild-type MexB. In contrast, the indolyl side chain of
W178 in [ACRB](/xray-mp-wiki/proteins/acrB)(F178W) protrudes into the narrow space of the hydrophobic trap, blocking [ABI-PP](/xray-mp-wiki/reagents/ligands/abi-pp)
binding. This difference is attributed to steric hindrance with V139 in [ACRB](/xray-mp-wiki/proteins/acrB) and I138 in
MexB at corresponding positions.

### Hydrophobic trap architecture separates substrate channel from inhibitor site

The distal drug-binding pocket of MexB is separated into two parts: a relatively hydrophilic
substrate-translocation channel with sufficient space for multisite drug binding, and a
hydrophobic trap forming a deep and narrow fissure. The hydrophobic trap is rich in
phenylalanine residues that do not directly interact with exported drugs but indirectly
affect drug binding. [ABI-PP](/xray-mp-wiki/reagents/ligands/abi-pp) binds tightly to this trap and inhibits the functional rotation
mechanism of MexB monomers, potentiating the activities of all antibiotics exported by MexB.
The inhibitor specificity between MexB and [MEXY](/xray-mp-wiki/proteins/mexY) is determined by subtle differences in the
amount of space in the hydrophobic trap.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">AcrB multidrug efflux pump</a> — Close homologue (69.8% identity, 83.2% similarity); structure solved by molecular replacement using asymmetric AcrB (PDB 2J8S) as search model; shares same asymmetric transport mechanism
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Primary detergent used for solubilization (1% DDM), purification (0.03% DDM), and crystallization; also observed bound in the multidrug-binding cavity of subunit B and distal pocket, suggesting RND transporters can transport detergents as substrates
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Used at 10 mM in solubilization buffer, 25-140 mM for Ni-NTA wash, and 350 mM for elution of C-terminal hexahistidine-tagged MexB
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — 10% glycerol included in all purification buffers for protein stability
- <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF (Phenylmethylsulfonyl Fluoride)</a> — 1 mM PMSF added during cell lysis and solubilization as a serine protease inhibitor
- <a href="/xray-mp-wiki/reagents/additives/kanamycin/">Kanamycin</a> — Used for plasmid maintenance during E. coli expression
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer (Tris-HCl)</a> — 20 mM Tris-HCl pH 7.5 used as the primary buffer in cell lysis, solubilization, affinity chromatography, and SEC purification steps
- <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a> — 50 mM Na acetate-HCl (pH 5.5) used as crystallization buffer component for MexB
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">Polyethylene Glycol 400 (PEG 400)</a> — 26% (v/v) PEG 400 used as precipitant in MexB crystallization; increased to 40% for cryoprotection
- <a href="/xray-mp-wiki/reagents/ligands/abi-pp/">ABI-PP (tert-butyl thiazolyl aminocarboxyl pyridopyrimidine)</a> — Inhibitor bound in hydrophobic trap of MexB; first inhibitor-bound structure of MexB solved
- <a href="/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-thioglucoside/">n-Octyl-beta-D-thioglucoside</a> — Used as crystallization additive for MexB(F178W) mutant
- <a href="/xray-mp-wiki/proteins/abc-transporters/mexY/">MexY (Pseudomonas aeruginosa multidrug exporter)</a> — Close homologue; MexY(W177F) mutant studied in parallel to understand inhibitor specificity
