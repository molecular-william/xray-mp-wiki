---
title: "GluA2 AMPA Receptor — Structures with Antagonists, NAMs, and Allosteric Modulators"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature08624, doi/10.1111##bph.15254, doi/10.1111##febs.15455, doi/10.1126##science.1256508, doi/10.1126##science.1258409, doi/10.1016##j.cell.2014.07.023]
verified: agent
uniprot_id: P19491
---

# GluA2 AMPA Receptor — Structures with Antagonists, NAMs, and Allosteric Modulators

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span> <span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P19491">UniProt: P19491</a>

<span class="expr-badge">Rattus norvegicus</span>

## Overview

GluA2 (also known as GluR2) is an AMPA-subtype ionotropic glutamate receptor (iGluR) subunit that forms tetrameric cation channels mediating fast excitatory neurotransmission in the central nervous system. The first X-ray crystal structure of a full-length rat GluA2 receptor was determined at 3.6 A resolution in 2009 (Sobolevsky et al., Nature 2009), revealing the Y-shaped tetrameric architecture with amino-terminal domain (ATD), ligand-binding domain (LBD), and transmembrane domain (TMD). AMPA receptors are validated targets for antiepileptic drugs (AEDs). Multiple subsequent crystal structures of the full-length rat GluA2 receptor have been determined in complex with various ligands, revealing distinct inhibition mechanisms. A 4.25 A structure with trans-4-butylcyclohexane carboxylic acid (4-BCCA), a medium-chain fatty acid AED candidate, showed 4-BCCA binding at TMD side portals distinct from the perampanel site (Yelshanskaya et al., 2020, Br J Pharmacol). A 4.65 A structure with the competitive antagonist ZK200775 and the negative allosteric modulator (NAM) GYKI53655 demonstrated that four molecules of each antagonist can bind simultaneously, with the two mechanisms of antagonism operating independently (Krintel et al., 2020, FEBS J). The EM analysis showed that AMPA induces a mix of compact and bulgy conformations regardless of GYKI53655 presence, indicating the NAM primarily affects the TMD gate without altering extracellular domain conformations. A structure of GluA2 bound to the partial agonist (S)-5-nitrowillardine (NOW) at 3.6-4.0 A resolution revealed ~11 degrees of LBD clamshell closure compared to the antagonist-bound state, providing insights into iGluR gating (Yelshanskaya et al., 2014, Science). Multiple X-ray structures of GluA2 in complex with the Conus striatus cone snail toxin con-ikot-ikot, a positive allosteric modulator, and orthosteric agonists at 3.8-4.1 A resolution showed how the toxin restrains the LBD gating ring, transducing agonist-induced clamshell closure into iris-like expansion of the gating ring (Chen et al., 2014, Science).


## Publications

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##nature08624 (1 structure, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3kg2">3KG2</a></td>
      <td>3.6</td>
      <td>P1</td>
      <td>GluA2cryst — modified rat GluA2i (flip isoform) with C-terminal deletions, ATD-LBD linker deletions (6 residues), glycosylation knockout mutations (N235E, N385D, N392Q), loop L1 alanine substitutions, R586Q, and C589A</td>
      <td>None (apo-like, antagonist-bound)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293 GnTI- cells (BacMam system) or Sf9 insect cells (baculovirus)
- **Construct**: Rat GluA2i (flip) with native signal peptide. Variants include GluA2cryst (C-terminal deletions, ATD-LBD linker deletions, glycosylation knockout mutations), GluA2Del (36-residue C-terminal deletion), GluA2_cryst1, and GluA2_cryst2
- **Notes**: Multiple constructs used across studies for crystallization. C-terminal GFP-His tag or C-terminal thrombin cleavage site with eGFP and [Strep-Tag](/xray-mp-wiki/reagents/protein-tags/strep-tag/) used for purification.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kg2">3KG2</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKANHAALAGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAY</span><span class="topo-membrane">EIWMCIVFAYIGVSVVLFLV</span><span class="topo-unknown">SRFSPYEWHTEEFEDGRETQSSES</span><span class="topo-inside">TNEFGIFNS</span><span class="topo-unknown">LWFSLGAFMQQGADIS</span><span class="topo-inside">PR</span><span class="topo-membrane">SLSGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIISSY</span><span class="topo-outside">TANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820   </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGLLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNV</span><span class="topo-membrane">AGVFYILVGGLGLAMLVALI</span><span class="topo-inside">EFCYK</span><span class="topo-unknown">SRAEAKRMKGLVPRG</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>514</td>
      <td>10</td>
      <td>523</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>515</td>
      <td>534</td>
      <td>524</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>558</td>
      <td>545</td>
      <td>567</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>559</td>
      <td>567</td>
      <td>568</td>
      <td>576</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>568</td>
      <td>577</td>
      <td>577</td>
      <td>586</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>578</td>
      <td>583</td>
      <td>587</td>
      <td>592</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>584</td>
      <td>585</td>
      <td>593</td>
      <td>594</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>607</td>
      <td>595</td>
      <td>616</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>608</td>
      <td>783</td>
      <td>617</td>
      <td>792</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>784</td>
      <td>803</td>
      <td>793</td>
      <td>812</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>804</td>
      <td>808</td>
      <td>813</td>
      <td>817</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>809</td>
      <td>823</td>
      <td>818</td>
      <td>832</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kg2">3KG2</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKANHAALAGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAY</span><span class="topo-membrane">EIWMCIVFAYIGVSVVLFLV</span><span class="topo-unknown">SRFSPYEWHTEEFEDGRETQSSES</span><span class="topo-inside">TNEFGIFN</span><span class="topo-unknown">SLWFSLGAFMQQGADISP</span><span class="topo-membrane">RSLSGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIIS</span><span class="topo-outside">SYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820   </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGLLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNV</span><span class="topo-membrane">AGVFYILVGGLGLAMLVAL</span><span class="topo-inside">IEFCYK</span><span class="topo-unknown">SRAEAKRMKGLVPRG</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>514</td>
      <td>10</td>
      <td>523</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>515</td>
      <td>534</td>
      <td>524</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>558</td>
      <td>545</td>
      <td>567</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>559</td>
      <td>566</td>
      <td>568</td>
      <td>575</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>567</td>
      <td>577</td>
      <td>576</td>
      <td>586</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>578</td>
      <td>583</td>
      <td>587</td>
      <td>592</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>585</td>
      <td>605</td>
      <td>594</td>
      <td>614</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>606</td>
      <td>783</td>
      <td>615</td>
      <td>792</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>784</td>
      <td>802</td>
      <td>793</td>
      <td>811</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>808</td>
      <td>812</td>
      <td>817</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>809</td>
      <td>823</td>
      <td>818</td>
      <td>832</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kg2">3KG2</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKANHAALAGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYEI</span><span class="topo-membrane">WMCIVFAYIGVSVVLFLVS</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSES</span><span class="topo-inside">TNEFG</span><span class="topo-unknown">IFNSLWFSLGAFMQQGADISP</span><span class="topo-membrane">RSLSGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIIS</span><span class="topo-outside">SYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820   </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGLLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNV</span><span class="topo-membrane">AGVFYILVGGLGLAMLVALIE</span><span class="topo-inside">FCYK</span><span class="topo-unknown">SRAEAKRMKGLVPRG</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>516</td>
      <td>10</td>
      <td>525</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>535</td>
      <td>526</td>
      <td>544</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>558</td>
      <td>545</td>
      <td>567</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>559</td>
      <td>563</td>
      <td>568</td>
      <td>572</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>564</td>
      <td>577</td>
      <td>573</td>
      <td>586</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>578</td>
      <td>583</td>
      <td>587</td>
      <td>592</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>585</td>
      <td>605</td>
      <td>594</td>
      <td>614</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>606</td>
      <td>783</td>
      <td>615</td>
      <td>792</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>784</td>
      <td>804</td>
      <td>793</td>
      <td>813</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>805</td>
      <td>808</td>
      <td>814</td>
      <td>817</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>809</td>
      <td>823</td>
      <td>818</td>
      <td>832</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kg2">3KG2</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKANHAALAGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYEI</span><span class="topo-membrane">WMCIVFAYIGVSVVLFLV</span><span class="topo-unknown">SRFSPYEWHTEEFEDGRETQSSES</span><span class="topo-inside">TNEFG</span><span class="topo-unknown">IFNSLWFSLGAFMQQGADIS</span><span class="topo-inside">PR</span><span class="topo-membrane">SLSGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIIS</span><span class="topo-outside">SYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820   </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGLLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNVAGV</span><span class="topo-membrane">FYILVGGLGLAMLVALIEFC</span><span class="topo-inside">YK</span><span class="topo-unknown">SRAEAKRMKGLVPRG</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>516</td>
      <td>10</td>
      <td>525</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>534</td>
      <td>526</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>558</td>
      <td>545</td>
      <td>567</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>559</td>
      <td>563</td>
      <td>568</td>
      <td>572</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>564</td>
      <td>577</td>
      <td>573</td>
      <td>586</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>578</td>
      <td>583</td>
      <td>587</td>
      <td>592</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>584</td>
      <td>585</td>
      <td>593</td>
      <td>594</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>605</td>
      <td>595</td>
      <td>614</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>606</td>
      <td>786</td>
      <td>615</td>
      <td>795</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>787</td>
      <td>806</td>
      <td>796</td>
      <td>815</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>807</td>
      <td>808</td>
      <td>816</td>
      <td>817</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>809</td>
      <td>823</td>
      <td>818</td>
      <td>832</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1111##bph.15254 (1 structure, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6xsr">6XSR</a></td>
      <td>4.25</td>
      <td>P 21 21 21</td>
      <td>GluA2Del (modified rat GluA2i flip isoform) — 36-residue C-terminal deletion, ATD-LBD linker deletions, N235E/N385D/N392Q (glycosylation knockouts), M1-M2 linker replaced with DTD linker, R586Q, C589A</td>
      <td>4-BCCA (trans-4-butylcyclohexane carboxylic acid)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293 GnTI- cells (BacMam system) or Sf9 insect cells (baculovirus)
- **Construct**: Rat GluA2i (flip) with native signal peptide. Variants include GluA2cryst (C-terminal deletions, ATD-LBD linker deletions, glycosylation knockout mutations), GluA2Del (36-residue C-terminal deletion), GluA2_cryst1, and GluA2_cryst2
- **Notes**: Multiple constructs used across studies for crystallization. C-terminal GFP-His tag or C-terminal thrombin cleavage site with eGFP and [Strep-Tag](/xray-mp-wiki/reagents/protein-tags/strep-tag/) used for purification.

**Purification:**

- **Expression system**: HEK293 GnTI- cells (BacMam)
- **Expression construct**: Rat GluA2i (flip) with native signal peptide in [Peg](/xray-mp-wiki/reagents/additives/peg/) BacMam vector. C-terminal thrombin cleavage site, eGFP, Strep-tag. Deletions: 36 residues from C-terminus, 6 residues from ATD-LBD linker. Mutations: N235E, N385D, N392Q, R586Q, C589A.
- **Tag info**: C-terminal eGFP-Strep-tag, thrombin removable

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
      <td>Cell culture and expression</td>
      <td><a href="/xray-mp-wiki/methods/expression/bacmam/">BacMam</a> P2 virus transduction of HEK293 GnTI- cells</td>
      <td>—</td>
      <td>DMEM culture medium</td>
      <td>Cells harvested 60-96 h after virus addition</td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Sonication</td>
      <td>—</td>
      <td>150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>(/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 0.8 uM aprotinin, 2 ug/mL leupeptin, 2 uM pepstatin A, 1 mM PMSF</td>
      <td>18 x 15 s at power level 7. Homogenate clarified at 8000 rpm for 15 min. Crude membranes collected by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">Ultracentrifugation</a> at 40000 rpm for 1 h (Ti45 rotor)</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td><a href="/xray-mp-wiki/methods/purification/detergent-solubilization/">Detergent Solubilization</a></td>
      <td>—</td>
      <td>150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>(/xray-mp-wiki/reagents/buffers/tris/) pH 8.0 + 20 mM C12M (n-dodecyl-beta-D-maltopyranoside, <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>) at 0.25 g/g membranes</td>
      <td>Solubilization for 2 h at 4 C. Insoluble material removed by ultracentrifugation at 40000 rpm for 40 min (Ti45 rotor)</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/reagents/additives/strep-tactin/">Strep-Tactin</a> resin batch binding</td>
      <td>Strep-Tactin</td>
      <td>150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>(/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 1 mM C12M</td>
      <td>0.5-1.0 mL resin per L culture. Binding for 3-18 h. Elution with 2.5 mM <a href="/xray-mp-wiki/reagents/ligands/desthiobiotin/">Desthiobiotin</a></td>
    </tr>
    <tr>
      <td>Deglycosylation and tag removal</td>
      <td><a href="/xray-mp-wiki/reagents/additives/endoh/">Endoh</a> + thrombin digestion</td>
      <td>—</td>
      <td>150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>(/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 1 mM C12M</td>
      <td><a href="/xray-mp-wiki/reagents/additives/endoh/">Endoh</a> at 1:1 mass ratio for 24 h at 4 C, then thrombin at 1:200 mass ratio for 1 h at 22 C</td>
    </tr>
    <tr>
      <td>Size exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> - <a href="/xray-mp-wiki/reagents/additives/superose-6/">Superose 6</a> column</td>
      <td>—</td>
      <td>150 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>(/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 1 mM n-undecyl-beta-D-thiomaltopyranoside (C11Thio), 0.01 mg/mL <a href="/xray-mp-wiki/reagents/lipids/popc/">POPC</a>:<a href="/xray-mp-wiki/reagents/lipids/pope/">POPE</a>:<a href="/xray-mp-wiki/reagents/lipids/popg/">POPG</a> (3:1:1)</td>
      <td>Pooled peak fractions concentrated to ~2 mg/mL for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion</a>, hanging drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>GluA2Del at ~2 mg/mL with 2 mM 4-BCCA</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Condition 1: 8-11% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 8000, 0.2 M magnesium <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate</a>, 0.1 M sodium <a href="/xray-mp-wiki/reagents/buffers/cacodylate/">Cacodylate</a> pH 6.3-6.7; Condition 2: 11-14% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 6000, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/ammonium-phosphate/">Ammonium Phosphate</a>, 0.1 M TRIS pH 7.9-8.0</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>2:1 (protein:reservoir)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>5-7 days (crystals appeared), 30-60 days (max size ~100x100x300 um)</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Serial <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> to 20% (v/v)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Protein subjected to ultracentrifugation at 40000 rpm for 40 min at 4 C prior to crystallization</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6xsr">6XSR</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYEI</span><span class="topo-membrane">WMCIVFAYIGVSVVLFLV</span><span class="topo-inside">S</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSESTNEFG</span><span class="topo-inside">IFNSL</span><span class="topo-unknown">WFSLGAFMQQGCDISPRSL</span><span class="topo-inside">S</span><span class="topo-membrane">GRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIIS</span><span class="topo-outside">SYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800        </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNV</span><span class="topo-membrane">AGVFYILVGGLGLAMLVAL</span><span class="topo-inside">IEFCY</span><span class="topo-unknown">K</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>516</td>
      <td>10</td>
      <td>525</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>534</td>
      <td>526</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>535</td>
      <td>535</td>
      <td>544</td>
      <td>544</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>564</td>
      <td>568</td>
      <td>573</td>
      <td>577</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>569</td>
      <td>578</td>
      <td>578</td>
      <td>587</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>588</td>
      <td>588</td>
      <td>597</td>
      <td>597</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>589</td>
      <td>605</td>
      <td>598</td>
      <td>614</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>606</td>
      <td>783</td>
      <td>615</td>
      <td>792</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>784</td>
      <td>802</td>
      <td>793</td>
      <td>811</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>807</td>
      <td>812</td>
      <td>816</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6xsr">6XSR</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPG</span><span class="topo-unknown">VFSFLD</span><span class="topo-outside">PLAYE</span><span class="topo-membrane">IWMCIVFAYIGVSVVLFL</span><span class="topo-inside">VS</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSESTNEFG</span><span class="topo-inside">IFNSL</span><span class="topo-unknown">WFSLGAFMQQGCDISPR</span><span class="topo-inside">SL</span><span class="topo-membrane">SGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIISSY</span><span class="topo-outside">TANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800        </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNVA</span><span class="topo-membrane">GVFYILVGGLGLAMLVAL</span><span class="topo-inside">IEFCY</span><span class="topo-unknown">K</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>504</td>
      <td>10</td>
      <td>513</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>505</td>
      <td>510</td>
      <td>514</td>
      <td>519</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>511</td>
      <td>515</td>
      <td>520</td>
      <td>524</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>533</td>
      <td>525</td>
      <td>542</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>534</td>
      <td>535</td>
      <td>543</td>
      <td>544</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>564</td>
      <td>568</td>
      <td>573</td>
      <td>577</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>569</td>
      <td>578</td>
      <td>578</td>
      <td>587</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>586</td>
      <td>587</td>
      <td>595</td>
      <td>596</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>588</td>
      <td>607</td>
      <td>597</td>
      <td>616</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>608</td>
      <td>784</td>
      <td>617</td>
      <td>793</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>785</td>
      <td>802</td>
      <td>794</td>
      <td>811</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>807</td>
      <td>812</td>
      <td>816</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6xsr">6XSR</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYE</span><span class="topo-membrane">IWMCIVFAYIGVSVVLFLV</span><span class="topo-inside">S</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSESTNEFG</span><span class="topo-inside">IFNS</span><span class="topo-unknown">LWFSLGAFMQQGCDISP</span><span class="topo-inside">RSL</span><span class="topo-membrane">SGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIISSY</span><span class="topo-outside">TANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800        </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNV</span><span class="topo-membrane">AGVFYILVGGLGLAMLVAL</span><span class="topo-inside">IEFCYK</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>515</td>
      <td>10</td>
      <td>524</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>534</td>
      <td>525</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>535</td>
      <td>535</td>
      <td>544</td>
      <td>544</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>564</td>
      <td>567</td>
      <td>573</td>
      <td>576</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>568</td>
      <td>578</td>
      <td>577</td>
      <td>587</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>585</td>
      <td>587</td>
      <td>594</td>
      <td>596</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>588</td>
      <td>607</td>
      <td>597</td>
      <td>616</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>608</td>
      <td>783</td>
      <td>617</td>
      <td>792</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>784</td>
      <td>802</td>
      <td>793</td>
      <td>811</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>808</td>
      <td>812</td>
      <td>817</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6xsr">6XSR</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYE</span><span class="topo-membrane">IWMCIVFAYIGVSVVLFLV</span><span class="topo-inside">S</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSESTNEFG</span><span class="topo-inside">IFNS</span><span class="topo-unknown">LWFSLGAFMQQGCDISPR</span><span class="topo-inside">SL</span><span class="topo-membrane">SGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIIS</span><span class="topo-outside">SYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800        </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNV</span><span class="topo-membrane">AGVFYILVGGLGLAMLV</span><span class="topo-inside">ALIEFCY</span><span class="topo-unknown">K</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>515</td>
      <td>10</td>
      <td>524</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>534</td>
      <td>525</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>535</td>
      <td>535</td>
      <td>544</td>
      <td>544</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>564</td>
      <td>567</td>
      <td>573</td>
      <td>576</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>568</td>
      <td>578</td>
      <td>577</td>
      <td>587</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>586</td>
      <td>587</td>
      <td>595</td>
      <td>596</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>588</td>
      <td>605</td>
      <td>597</td>
      <td>614</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>606</td>
      <td>783</td>
      <td>615</td>
      <td>792</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>784</td>
      <td>800</td>
      <td>793</td>
      <td>809</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>801</td>
      <td>807</td>
      <td>810</td>
      <td>816</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1111##febs.15455 (1 structure, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ruq">6RUQ</a></td>
      <td>4.65</td>
      <td>P 1 21 1</td>
      <td>GluA2cryst (modified rat GluA2 without CTD) — expressed in Sf9 insect cells</td>
      <td>ZK200775 (competitive antagonist), GYKI53655 (NAM)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293 GnTI- cells (BacMam system) or Sf9 insect cells (baculovirus)
- **Construct**: Rat GluA2i (flip) with native signal peptide. Variants include GluA2cryst (C-terminal deletions, ATD-LBD linker deletions, glycosylation knockout mutations), GluA2Del (36-residue C-terminal deletion), GluA2_cryst1, and GluA2_cryst2
- **Notes**: Multiple constructs used across studies for crystallization. C-terminal GFP-His tag or C-terminal thrombin cleavage site with eGFP and [Strep-Tag](/xray-mp-wiki/reagents/protein-tags/strep-tag/) used for purification.

**Purification:**

- **Expression system**: Sf9 insect cells (baculovirus) and HEK293F mammalian cells (BacMam)
- **Expression construct**: GluA2cryst construct with C-terminal GFP-His tag
- **Tag info**: C-terminal GFP-His tag, thrombin removable

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
      <td>Cell culture and expression (Sf9)</td>
      <td>Baculovirus expression in Sf9 insect cells</td>
      <td>—</td>
      <td></td>
      <td>Baculovirus particles generated using standard methods</td>
    </tr>
    <tr>
      <td>Cell culture and expression (HEK293F)</td>
      <td>BacMam transduction of HEK293F cells</td>
      <td>—</td>
      <td>FreeStyle 293 expression medium, 8% CO2, 37 C, 150 RPM</td>
      <td>20 mL BacMam virus for 200 mL HEK293F at 1x10^6 cells/mL. 5 mM <a href="/xray-mp-wiki/reagents/additives/sodium-butyrate/">Sodium Butyrate</a> added 6-24 h post-transduction, temperature lowered to 30 C. Cells harvested after 72 h</td>
    </tr>
    <tr>
      <td>Cell lysis and membrane preparation</td>
      <td>Sonication and ultracentrifugation</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 150 mM NaCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">Pmsf</a>, cOmplete Protease Inhibitor</td>
      <td>Cells resuspended and sonicated. Lysate spun at 41000 RPM (70Ti rotor) for 20 min</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> solubilization</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 150 mM NaCl, cOmplete Protease Inhibitor + 20 mg/mL <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (n-dodecyl-beta-D-maltopyranoside) Sol-Grade (Anatrace)</td>
      <td>Pellet resuspended using dounce homogenizer. Solubilized membranes spun at 41000 RPM (70Ti rotor)</td>
    </tr>
    <tr>
      <td>Affinity purification and tag removal</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> Metal Affinity + thrombin digest</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> Superflow Metal Affinity Resin</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 150 mM NaCl, <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Eluted with 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>. Overnight digestion with thrombin to remove GFP-His tag</td>
    </tr>
    <tr>
      <td>Size exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> - Superose 6 10/300 GL</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 150 mM NaCl, 0.5 mg/mL <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> Anagrade, low alpha isomer (Anatrace)</td>
      <td>Tag-free GluA2cryst purified. Pooled peak fractions used for EM and crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/microbatch-crystallization-under-oil/">Microbatch Under Oil</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>GluA2cryst at 2 mg/mL in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, 150 mM NaCl, 0.5 mg/mL <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> with 0.67 mM GYKI53655 and 0.31 mM ZK200775</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.0, 12% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 20000</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>279</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Appeared within 24 h, grew for 3-4 days before flash-cooling</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Flash-cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected at ESRF ID29 using helical scan. Processed with XIA2/MOSFLM. Resolution cut at 4.65 A</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ruq">6RUQ</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKANHAALAGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPG</span><span class="topo-membrane">VFSFLDPLAYEIWMCIVFAYIGVSVVLFLVS</span><span class="topo-inside">RFS</span><span class="topo-unknown">PYEWHTEEFEDGRETQSSESTNEF</span><span class="topo-inside">AI</span><span class="topo-unknown">FQSAWFSLGAFMQQGADIS</span><span class="topo-inside">PRS</span><span class="topo-membrane">LSGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIISSYTA</span><span class="topo-outside">NLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820   </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGLLDKLKNKWWYDKGECGAKDSGSKEKTSALS</span><span class="topo-membrane">LSNVAGVFYILVGGLGLAMLVALI</span><span class="topo-inside">EFCYK</span><span class="topo-unknown">SRAEAKRMKGLVPRG</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>504</td>
      <td>10</td>
      <td>513</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>505</td>
      <td>535</td>
      <td>514</td>
      <td>544</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>538</td>
      <td>545</td>
      <td>547</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>539</td>
      <td>562</td>
      <td>548</td>
      <td>571</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>563</td>
      <td>564</td>
      <td>572</td>
      <td>573</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>565</td>
      <td>583</td>
      <td>574</td>
      <td>592</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>584</td>
      <td>586</td>
      <td>593</td>
      <td>595</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>587</td>
      <td>609</td>
      <td>596</td>
      <td>618</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>610</td>
      <td>779</td>
      <td>619</td>
      <td>788</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>780</td>
      <td>803</td>
      <td>789</td>
      <td>812</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>804</td>
      <td>808</td>
      <td>813</td>
      <td>817</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>809</td>
      <td>823</td>
      <td>818</td>
      <td>832</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ruq">6RUQ</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKANHAALAGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSF</span><span class="topo-membrane">LDPLAYEIWMCIVFAYIGVSVVLFLV</span><span class="topo-inside">SR</span><span class="topo-unknown">FSPYEWHTEEFEDGRETQSSESTNEF</span><span class="topo-inside">AIFQS</span><span class="topo-unknown">AWFSLGAFMQQGADI</span><span class="topo-inside">SPRS</span><span class="topo-membrane">LSGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIISSYTANL</span><span class="topo-outside">AAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820   </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGLLDKLKNKWWYDKGECGAKDSGSKEKTSALSL</span><span class="topo-membrane">SNVAGVFYILVGGLGLAMLVALI</span><span class="topo-inside">EFCY</span><span class="topo-unknown">KSRAEAKRMKGLVPRG</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>508</td>
      <td>10</td>
      <td>517</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>509</td>
      <td>534</td>
      <td>518</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>535</td>
      <td>536</td>
      <td>544</td>
      <td>545</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>537</td>
      <td>562</td>
      <td>546</td>
      <td>571</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>563</td>
      <td>567</td>
      <td>572</td>
      <td>576</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>568</td>
      <td>582</td>
      <td>577</td>
      <td>591</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>583</td>
      <td>586</td>
      <td>592</td>
      <td>595</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>587</td>
      <td>611</td>
      <td>596</td>
      <td>620</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>612</td>
      <td>780</td>
      <td>621</td>
      <td>789</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>781</td>
      <td>803</td>
      <td>790</td>
      <td>812</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>804</td>
      <td>807</td>
      <td>813</td>
      <td>816</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>808</td>
      <td>823</td>
      <td>817</td>
      <td>832</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ruq">6RUQ</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKANHAALAGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPG</span><span class="topo-membrane">VFSFLDPLAYEIWMCIVFAYIGVSVVLFLV</span><span class="topo-inside">SRFSPYE</span><span class="topo-unknown">WHTEEFEDGRETQSSES</span><span class="topo-inside">TNEFAIFQS</span><span class="topo-unknown">AWFSLGAFMQQGADI</span><span class="topo-inside">SPRS</span><span class="topo-membrane">LSGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIISSYTANL</span><span class="topo-outside">AAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820   </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGLLDKLKNKWWYDKGECGAKDSGSKEKTSAL</span><span class="topo-membrane">SLSNVAGVFYILVGGLGLAMLVAL</span><span class="topo-inside">IEFCYKSRAEA</span><span class="topo-unknown">KRMKGLVPRG</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>504</td>
      <td>10</td>
      <td>513</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>505</td>
      <td>534</td>
      <td>514</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>535</td>
      <td>541</td>
      <td>544</td>
      <td>550</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>558</td>
      <td>551</td>
      <td>567</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>559</td>
      <td>567</td>
      <td>568</td>
      <td>576</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>568</td>
      <td>582</td>
      <td>577</td>
      <td>591</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>583</td>
      <td>586</td>
      <td>592</td>
      <td>595</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>587</td>
      <td>611</td>
      <td>596</td>
      <td>620</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>612</td>
      <td>778</td>
      <td>621</td>
      <td>787</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>779</td>
      <td>802</td>
      <td>788</td>
      <td>811</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>813</td>
      <td>812</td>
      <td>822</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>814</td>
      <td>823</td>
      <td>823</td>
      <td>832</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ruq">6RUQ</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKANHAALAGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSFL</span><span class="topo-membrane">DPLAYEIWMCIVFAYIGVSVVLFLV</span><span class="topo-inside">SRFSP</span><span class="topo-unknown">YEWHTEEFEDGRETQSSESTNEF</span><span class="topo-inside">AIFQSA</span><span class="topo-unknown">WFSLGAFMQQGADI</span><span class="topo-inside">SPRSL</span><span class="topo-membrane">SGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIISSYTANL</span><span class="topo-outside">AAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820   </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGLLDKLKNKWWYDKGECGAKDSGSKEKTSALSL</span><span class="topo-membrane">SNVAGVFYILVGGLGLAMLVAL</span><span class="topo-inside">IEFCYKS</span><span class="topo-unknown">RAEAKRMKGLVPRG</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>509</td>
      <td>10</td>
      <td>518</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>534</td>
      <td>519</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>535</td>
      <td>539</td>
      <td>544</td>
      <td>548</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>540</td>
      <td>562</td>
      <td>549</td>
      <td>571</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>563</td>
      <td>568</td>
      <td>572</td>
      <td>577</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>569</td>
      <td>582</td>
      <td>578</td>
      <td>591</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>583</td>
      <td>587</td>
      <td>592</td>
      <td>596</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>588</td>
      <td>611</td>
      <td>597</td>
      <td>620</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>612</td>
      <td>780</td>
      <td>621</td>
      <td>789</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>781</td>
      <td>802</td>
      <td>790</td>
      <td>811</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>809</td>
      <td>812</td>
      <td>818</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>810</td>
      <td>823</td>
      <td>819</td>
      <td>832</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1126##science.1256508 (1 structure, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u4g">4U4G</a></td>
      <td>3.6-4.0</td>
      <td>N/A</td>
      <td>Homotetrameric rat GluA2 (GluA2*) — modified for crystallization</td>
      <td>(S)-5-nitrowillardine (NOW, partial agonist)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293 GnTI- cells (BacMam system) or Sf9 insect cells (baculovirus)
- **Construct**: Rat GluA2i (flip) with native signal peptide. Variants include GluA2cryst (C-terminal deletions, ATD-LBD linker deletions, glycosylation knockout mutations), GluA2Del (36-residue C-terminal deletion), GluA2_cryst1, and GluA2_cryst2
- **Notes**: Multiple constructs used across studies for crystallization. C-terminal GFP-His tag or C-terminal thrombin cleavage site with eGFP and [Strep-Tag](/xray-mp-wiki/reagents/protein-tags/strep-tag/) used for purification.

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>GluA2* with (S)-5-nitrowillardine (<a href="/xray-mp-wiki/reagents/ligands/s-5-nitrowillardine/">NOW</a>)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown from GluA2* in complex with partial agonist (S)-5-nitrowillardine. Comparison with GluA2_ZK (ZK 200775-bound) closed-state structure</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u4g">4U4G</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSFLDP</span><span class="topo-membrane">LAYEIWMCIVFAYIGVSVVLFLV</span><span class="topo-unknown">SRFSPYEWHTEEFEDGRETQSSES</span><span class="topo-inside">TNEFGIFNS</span><span class="topo-unknown">LWFSLGAFMQQGCDISP</span><span class="topo-membrane">RSLSGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIISSYTA</span><span class="topo-outside">NLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820  </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGEC</span><span class="topo-unknown">GAKDSGSKEKT</span><span class="topo-outside">SALSL</span><span class="topo-membrane">SNVAGVFYILVGGLGLAMLVAL</span><span class="topo-inside">IEFCYK</span><span class="topo-unknown">SRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>511</td>
      <td>10</td>
      <td>520</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>534</td>
      <td>521</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>558</td>
      <td>545</td>
      <td>567</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>559</td>
      <td>567</td>
      <td>568</td>
      <td>576</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>568</td>
      <td>577</td>
      <td>577</td>
      <td>586</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>578</td>
      <td>583</td>
      <td>587</td>
      <td>592</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>585</td>
      <td>609</td>
      <td>594</td>
      <td>618</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>610</td>
      <td>764</td>
      <td>619</td>
      <td>773</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>765</td>
      <td>775</td>
      <td>774</td>
      <td>784</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>776</td>
      <td>780</td>
      <td>785</td>
      <td>789</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>781</td>
      <td>802</td>
      <td>790</td>
      <td>811</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>808</td>
      <td>812</td>
      <td>817</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>809</td>
      <td>822</td>
      <td>818</td>
      <td>831</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u4g">4U4G</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSFLDP</span><span class="topo-membrane">LAYEIWMCIVFAYIGVSVVLFLV</span><span class="topo-unknown">SRFSPYEWHTEEFEDGRETQSSES</span><span class="topo-inside">TNEFGIFN</span><span class="topo-unknown">SLWFSLGAFMQQGCDISP</span><span class="topo-membrane">RSLSGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIISSYTA</span><span class="topo-outside">NLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820  </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGEC</span><span class="topo-unknown">GAKDSGSKEKT</span><span class="topo-outside">SALSL</span><span class="topo-membrane">SNVAGVFYILVGGLGLAMLVA</span><span class="topo-inside">LIEFCYK</span><span class="topo-unknown">SRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>511</td>
      <td>10</td>
      <td>520</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>534</td>
      <td>521</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>558</td>
      <td>545</td>
      <td>567</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>559</td>
      <td>566</td>
      <td>568</td>
      <td>575</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>567</td>
      <td>577</td>
      <td>576</td>
      <td>586</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>578</td>
      <td>583</td>
      <td>587</td>
      <td>592</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>585</td>
      <td>609</td>
      <td>594</td>
      <td>618</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>610</td>
      <td>764</td>
      <td>619</td>
      <td>773</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>765</td>
      <td>775</td>
      <td>774</td>
      <td>784</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>776</td>
      <td>780</td>
      <td>785</td>
      <td>789</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>781</td>
      <td>801</td>
      <td>790</td>
      <td>810</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>802</td>
      <td>808</td>
      <td>811</td>
      <td>817</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>809</td>
      <td>822</td>
      <td>818</td>
      <td>831</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u4g">4U4G</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSFLDPL</span><span class="topo-membrane">AYEIWMCIVFAYIGVSVVLFLVS</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSES</span><span class="topo-inside">TNEFG</span><span class="topo-unknown">IFNSLWFSLGAFMQQGCDISP</span><span class="topo-membrane">RSLSGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIISSYT</span><span class="topo-outside">ANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820  </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGEC</span><span class="topo-unknown">GAKDSGSKEKT</span><span class="topo-outside">SALSLSN</span><span class="topo-membrane">VAGVFYILVGGLGLAMLVALIE</span><span class="topo-inside">FCYK</span><span class="topo-unknown">SRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>512</td>
      <td>10</td>
      <td>521</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>535</td>
      <td>522</td>
      <td>544</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>558</td>
      <td>545</td>
      <td>567</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>559</td>
      <td>563</td>
      <td>568</td>
      <td>572</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>564</td>
      <td>577</td>
      <td>573</td>
      <td>586</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>578</td>
      <td>583</td>
      <td>587</td>
      <td>592</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>585</td>
      <td>608</td>
      <td>594</td>
      <td>617</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>609</td>
      <td>764</td>
      <td>618</td>
      <td>773</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>765</td>
      <td>775</td>
      <td>774</td>
      <td>784</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>776</td>
      <td>782</td>
      <td>785</td>
      <td>791</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>783</td>
      <td>804</td>
      <td>792</td>
      <td>813</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>805</td>
      <td>808</td>
      <td>814</td>
      <td>817</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>809</td>
      <td>822</td>
      <td>818</td>
      <td>831</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u4g">4U4G</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSFLDPL</span><span class="topo-membrane">AYEIWMCIVFAYIGVSVVLFLV</span><span class="topo-unknown">SRFSPYEWHTEEFEDGRETQSSES</span><span class="topo-inside">TNEFGI</span><span class="topo-unknown">FNSLWFSLGAFMQQGCDIS</span><span class="topo-inside">PR</span><span class="topo-membrane">SLSGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIISSYT</span><span class="topo-outside">ANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820  </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGEC</span><span class="topo-unknown">GAKDSGSKEKT</span><span class="topo-outside">SALSLSNV</span><span class="topo-membrane">AGVFYILVGGLGLAMLVALIE</span><span class="topo-inside">FCYK</span><span class="topo-unknown">SRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>512</td>
      <td>10</td>
      <td>521</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>534</td>
      <td>522</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>558</td>
      <td>545</td>
      <td>567</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>559</td>
      <td>564</td>
      <td>568</td>
      <td>573</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>565</td>
      <td>577</td>
      <td>574</td>
      <td>586</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>578</td>
      <td>583</td>
      <td>587</td>
      <td>592</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>584</td>
      <td>585</td>
      <td>593</td>
      <td>594</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>608</td>
      <td>595</td>
      <td>617</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>609</td>
      <td>764</td>
      <td>618</td>
      <td>773</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>765</td>
      <td>775</td>
      <td>774</td>
      <td>784</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>776</td>
      <td>783</td>
      <td>785</td>
      <td>792</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>784</td>
      <td>804</td>
      <td>793</td>
      <td>813</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>805</td>
      <td>808</td>
      <td>814</td>
      <td>817</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>809</td>
      <td>822</td>
      <td>818</td>
      <td>831</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1126##science.1258409 (1 structure, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3kg2">3KG2</a></td>
      <td>3.8-4.1</td>
      <td>N/A</td>
      <td>GluA2_cryst1 and GluA2_cryst2 constructs with Lurcher-like mutants (A622T, T625G)</td>
      <td>con-ikot-ikot toxin, (R,R)-2b (positive allosteric modulator), kainate or fluorowillardiine (FW)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293 GnTI- cells (BacMam system) or Sf9 insect cells (baculovirus)
- **Construct**: Rat GluA2i (flip) with native signal peptide. Variants include GluA2cryst (C-terminal deletions, ATD-LBD linker deletions, glycosylation knockout mutations), GluA2Del (36-residue C-terminal deletion), GluA2_cryst1, and GluA2_cryst2
- **Notes**: Multiple constructs used across studies for crystallization. C-terminal GFP-His tag or C-terminal thrombin cleavage site with eGFP and [Strep-Tag](/xray-mp-wiki/reagents/protein-tags/strep-tag/) used for purification.

**Purification:**

- **Expression system**: HEK293 GnTI- cells (BacMam)
- **Expression construct**: Rat GluA2_cryst1 and GluA2_cryst2 constructs, with A622T and T625G Lurcher-like mutants
- **Tag info**: C-terminal GFP-His tag

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
      <td>Cell culture and expression</td>
      <td>BacMam transduction of HEK293 GnTI- cells</td>
      <td>—</td>
      <td></td>
      <td>Similar expression protocol to other GluA2 constructs</td>
    </tr>
    <tr>
      <td>Purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> and <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>Similar to GluA2_cryst1 protocols</td>
      <td><a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8.0, NaCl + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Detailed purification similar to GluA2_cryst1 construct. Protein concentrated for crystallization with toxin and ligands</td>
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
      <td>GluA2_cryst1 or GluA2_cryst2 with con-ikot-ikot toxin, (R,R)-2b, and <a href="/xray-mp-wiki/reagents/ligands/kainate/">KA</a> or fluorowillardiine</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Flash-cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Multiple structures determined at 3.8-4.1 A resolution. Modulator (R,R)-2b included to improve diffraction quality. Complexes with <a href="/xray-mp-wiki/reagents/ligands/kainate/">KA</a> or <a href="/xray-mp-wiki/reagents/ligands/fluorowilliardiine/">FW</a> as partial agonists. Lurcher-like mutants A622T and T625G used to favor open state. Structures represent toxin-bound preopen states</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kg2">3KG2</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKANHAALAGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAY</span><span class="topo-membrane">EIWMCIVFAYIGVSVVLFLV</span><span class="topo-unknown">SRFSPYEWHTEEFEDGRETQSSES</span><span class="topo-inside">TNEFGIFNS</span><span class="topo-unknown">LWFSLGAFMQQGADIS</span><span class="topo-inside">PR</span><span class="topo-membrane">SLSGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIISSY</span><span class="topo-outside">TANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820   </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGLLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNV</span><span class="topo-membrane">AGVFYILVGGLGLAMLVALI</span><span class="topo-inside">EFCYK</span><span class="topo-unknown">SRAEAKRMKGLVPRG</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>514</td>
      <td>10</td>
      <td>523</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>515</td>
      <td>534</td>
      <td>524</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>558</td>
      <td>545</td>
      <td>567</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>559</td>
      <td>567</td>
      <td>568</td>
      <td>576</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>568</td>
      <td>577</td>
      <td>577</td>
      <td>586</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>578</td>
      <td>583</td>
      <td>587</td>
      <td>592</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>584</td>
      <td>585</td>
      <td>593</td>
      <td>594</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>607</td>
      <td>595</td>
      <td>616</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>608</td>
      <td>783</td>
      <td>617</td>
      <td>792</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>784</td>
      <td>803</td>
      <td>793</td>
      <td>812</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>804</td>
      <td>808</td>
      <td>813</td>
      <td>817</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>809</td>
      <td>823</td>
      <td>818</td>
      <td>832</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kg2">3KG2</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKANHAALAGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAY</span><span class="topo-membrane">EIWMCIVFAYIGVSVVLFLV</span><span class="topo-unknown">SRFSPYEWHTEEFEDGRETQSSES</span><span class="topo-inside">TNEFGIFN</span><span class="topo-unknown">SLWFSLGAFMQQGADISP</span><span class="topo-membrane">RSLSGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIIS</span><span class="topo-outside">SYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820   </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGLLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNV</span><span class="topo-membrane">AGVFYILVGGLGLAMLVAL</span><span class="topo-inside">IEFCYK</span><span class="topo-unknown">SRAEAKRMKGLVPRG</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>514</td>
      <td>10</td>
      <td>523</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>515</td>
      <td>534</td>
      <td>524</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>558</td>
      <td>545</td>
      <td>567</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>559</td>
      <td>566</td>
      <td>568</td>
      <td>575</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>567</td>
      <td>577</td>
      <td>576</td>
      <td>586</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>578</td>
      <td>583</td>
      <td>587</td>
      <td>592</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>585</td>
      <td>605</td>
      <td>594</td>
      <td>614</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>606</td>
      <td>783</td>
      <td>615</td>
      <td>792</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>784</td>
      <td>802</td>
      <td>793</td>
      <td>811</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>808</td>
      <td>812</td>
      <td>817</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>809</td>
      <td>823</td>
      <td>818</td>
      <td>832</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kg2">3KG2</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKANHAALAGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYEI</span><span class="topo-membrane">WMCIVFAYIGVSVVLFLVS</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSES</span><span class="topo-inside">TNEFG</span><span class="topo-unknown">IFNSLWFSLGAFMQQGADISP</span><span class="topo-membrane">RSLSGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIIS</span><span class="topo-outside">SYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820   </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGLLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNV</span><span class="topo-membrane">AGVFYILVGGLGLAMLVALIE</span><span class="topo-inside">FCYK</span><span class="topo-unknown">SRAEAKRMKGLVPRG</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>516</td>
      <td>10</td>
      <td>525</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>535</td>
      <td>526</td>
      <td>544</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>558</td>
      <td>545</td>
      <td>567</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>559</td>
      <td>563</td>
      <td>568</td>
      <td>572</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>564</td>
      <td>577</td>
      <td>573</td>
      <td>586</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>578</td>
      <td>583</td>
      <td>587</td>
      <td>592</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>585</td>
      <td>605</td>
      <td>594</td>
      <td>614</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>606</td>
      <td>783</td>
      <td>615</td>
      <td>792</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>784</td>
      <td>804</td>
      <td>793</td>
      <td>813</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>805</td>
      <td>808</td>
      <td>814</td>
      <td>817</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>809</td>
      <td>823</td>
      <td>818</td>
      <td>832</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3kg2">3KG2</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVLTEDDTSGLEQKTVVVTTILESPYVMMKANHAALAGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREEVI</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYEI</span><span class="topo-membrane">WMCIVFAYIGVSVVLFLV</span><span class="topo-unknown">SRFSPYEWHTEEFEDGRETQSSES</span><span class="topo-inside">TNEFG</span><span class="topo-unknown">IFNSLWFSLGAFMQQGADIS</span><span class="topo-inside">PR</span><span class="topo-membrane">SLSGRIVGGVWWFFT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">LIIIS</span><span class="topo-outside">SYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820   </span>
<span class="topo-line"><span class="topo-outside">KGYGIATPKGSSLGTPVNLAVLKLSEQGLLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNVAGV</span><span class="topo-membrane">FYILVGGLGLAMLVALIEFC</span><span class="topo-inside">YK</span><span class="topo-unknown">SRAEAKRMKGLVPRG</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>516</td>
      <td>10</td>
      <td>525</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>534</td>
      <td>526</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>558</td>
      <td>545</td>
      <td>567</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>559</td>
      <td>563</td>
      <td>568</td>
      <td>572</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>564</td>
      <td>577</td>
      <td>573</td>
      <td>586</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>578</td>
      <td>583</td>
      <td>587</td>
      <td>592</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>584</td>
      <td>585</td>
      <td>593</td>
      <td>594</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>605</td>
      <td>595</td>
      <td>614</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>606</td>
      <td>786</td>
      <td>615</td>
      <td>795</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>787</td>
      <td>806</td>
      <td>796</td>
      <td>815</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>807</td>
      <td>808</td>
      <td>816</td>
      <td>817</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>809</td>
      <td>823</td>
      <td>818</td>
      <td>832</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1016##j.cell.2014.07.023 (6 structures, 22 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u2p">4U2P</a></td>
      <td>3.71</td>
      <td>P2(1)2(1)2(1)</td>
      <td>5M (thermostabilized rat GluA2 construct with 5 thermostabilizing mutations)</td>
      <td>None (apo resting/closed state)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u1w">4U1W</a></td>
      <td>3.61</td>
      <td>P2(1)2(1)2(1)</td>
      <td>5M construct</td>
      <td>Kainate (partial agonist), (R,R)-2b (positive allosteric modulator)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u1x">4U1X</a></td>
      <td>3.82</td>
      <td>P2(1)2(1)2(1)</td>
      <td>10M construct (10 thermostabilizing mutations)</td>
      <td>Kainate (partial agonist), (R,R)-2b (positive allosteric modulator)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u1y">4U1Y</a></td>
      <td>4.27</td>
      <td>P2(1)2(1)2(1)</td>
      <td>10Mdel construct (10 thermostabilizing mutations + M1-M2 loop deletion)</td>
      <td>Fluorowilliardiine (partial agonist), (R,R)-2b (positive allosteric modulator)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u2q">4U2Q</a></td>
      <td>4.05</td>
      <td>P2(1)2(1)2(1)</td>
      <td>5M construct</td>
      <td>Kainate (partial agonist, no modulator)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4u2p">4U2P</a></td>
      <td>7.94</td>
      <td>P2(1)</td>
      <td>5M construct</td>
      <td>Fluorowilliardiine (partial agonist, desensitizing conditions)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293 GnTI- cells (BacMam system) or Sf9 insect cells (baculovirus)
- **Construct**: Rat GluA2i (flip) with native signal peptide. Variants include GluA2cryst (C-terminal deletions, ATD-LBD linker deletions, glycosylation knockout mutations), GluA2Del (36-residue C-terminal deletion), GluA2_cryst1, and GluA2_cryst2
- **Notes**: Multiple constructs used across studies for crystallization. C-terminal GFP-His tag or C-terminal thrombin cleavage site with eGFP and [Strep-Tag](/xray-mp-wiki/reagents/protein-tags/strep-tag/) used for purification.

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u2p">4U2P</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">NS</span><span class="topo-outside">IQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVVTLTEDDTSGLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VIDFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYEIW</span><span class="topo-membrane">MAIVFAYIGVSVVL</span><span class="topo-inside">FLVSR</span><span class="topo-unknown">FSPYEWHTEEFEDGRETQSSESTNEFGIFNSLWFSLGAFFQQGADIS</span><span class="topo-inside">PRSL</span><span class="topo-membrane">SARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIII</span><span class="topo-outside">SSYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-outside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNVAGV</span><span class="topo-membrane">FYILVGGLGLAML</span><span class="topo-inside">VAL</span><span class="topo-unknown">IEFAYKSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>519</td>
      <td>10</td>
      <td>526</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>520</td>
      <td>533</td>
      <td>527</td>
      <td>540</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>534</td>
      <td>538</td>
      <td>541</td>
      <td>545</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>589</td>
      <td>593</td>
      <td>596</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>590</td>
      <td>606</td>
      <td>597</td>
      <td>613</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>607</td>
      <td>788</td>
      <td>614</td>
      <td>795</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>789</td>
      <td>801</td>
      <td>796</td>
      <td>808</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>802</td>
      <td>804</td>
      <td>809</td>
      <td>811</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u2p">4U2P</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVVTLTEDDTSGLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VIDFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYEIWM</span><span class="topo-membrane">AIVFAYIGVSVVLF</span><span class="topo-inside">LVS</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSESTNEFGIFNSLWFSLGAFFQQGADIS</span><span class="topo-inside">PRSL</span><span class="topo-membrane">SARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIII</span><span class="topo-outside">SSYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-outside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNVAGV</span><span class="topo-membrane">FYILVGGLGLAMLV</span><span class="topo-inside">ALIEFAY</span><span class="topo-unknown">KSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>520</td>
      <td>8</td>
      <td>527</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>521</td>
      <td>534</td>
      <td>528</td>
      <td>541</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>535</td>
      <td>537</td>
      <td>542</td>
      <td>544</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>589</td>
      <td>593</td>
      <td>596</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>590</td>
      <td>606</td>
      <td>597</td>
      <td>613</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>607</td>
      <td>788</td>
      <td>614</td>
      <td>795</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>789</td>
      <td>802</td>
      <td>796</td>
      <td>809</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>809</td>
      <td>810</td>
      <td>816</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u2p">4U2P</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVVTLTEDDTSGLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VIDFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYEIW</span><span class="topo-membrane">MAIVFAYIGVSVVL</span><span class="topo-inside">FL</span><span class="topo-unknown">VSRFSPYEWHTEEFEDGRETQSSESTNEFGIFNSLWFSLGAFFQQGADISPRS</span><span class="topo-inside">LS</span><span class="topo-membrane">ARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIII</span><span class="topo-outside">SSYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-outside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNVAGV</span><span class="topo-membrane">FYILVGGLGLAMLV</span><span class="topo-inside">AL</span><span class="topo-unknown">IEFAYKSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>519</td>
      <td>8</td>
      <td>526</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>520</td>
      <td>533</td>
      <td>527</td>
      <td>540</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>534</td>
      <td>535</td>
      <td>541</td>
      <td>542</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>589</td>
      <td>590</td>
      <td>596</td>
      <td>597</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>591</td>
      <td>606</td>
      <td>598</td>
      <td>613</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>607</td>
      <td>788</td>
      <td>614</td>
      <td>795</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>789</td>
      <td>802</td>
      <td>796</td>
      <td>809</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>804</td>
      <td>810</td>
      <td>811</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u2p">4U2P</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVVTLTEDD</span><span class="topo-unknown">TSGL</span><span class="topo-outside">EQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VIDFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYEIWM</span><span class="topo-membrane">AIVFAYIGVSVVL</span><span class="topo-inside">FLV</span><span class="topo-unknown">SRFSPYEWHTEEFEDGRETQSSESTNEFGIFNSLWFSLGAFFQQGADISP</span><span class="topo-inside">RSLS</span><span class="topo-membrane">ARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIII</span><span class="topo-outside">SSYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-outside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNVAGVF</span><span class="topo-membrane">YILVGGLGLAMLV</span><span class="topo-inside">ALIEFAY</span><span class="topo-unknown">KSRAEAKRMKGLVPR</span></span>
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
      <td>379</td>
      <td>8</td>
      <td>386</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>520</td>
      <td>391</td>
      <td>527</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>521</td>
      <td>533</td>
      <td>528</td>
      <td>540</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>534</td>
      <td>536</td>
      <td>541</td>
      <td>543</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>587</td>
      <td>590</td>
      <td>594</td>
      <td>597</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>591</td>
      <td>606</td>
      <td>598</td>
      <td>613</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>607</td>
      <td>789</td>
      <td>614</td>
      <td>796</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>790</td>
      <td>802</td>
      <td>797</td>
      <td>809</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>809</td>
      <td>810</td>
      <td>816</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u1w">4U1W</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGN</span><span class="topo-unknown">INNDKKDETYRSLFQDLELK</span><span class="topo-outside">KERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVVTLTED</span><span class="topo-unknown">DTSGL</span><span class="topo-outside">EQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VIDFSKPFMSLGISIMIKKPQKSKPGVFSFL</span><span class="topo-membrane">DPLAYEIWMAIVFAYIGVSVVLF</span><span class="topo-inside">LVS</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSESTNEFGIFNSLWFSLGAFFQQGADISPR</span><span class="topo-inside">SL</span><span class="topo-membrane">SARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIIISSYTANLA</span><span class="topo-outside">AFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-outside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKDSGSKEKTSAL</span><span class="topo-membrane">SLSNVAGVFYILVGGLGLAMLVAL</span><span class="topo-inside">IE</span><span class="topo-unknown">FAYKSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>158</td>
      <td>8</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>178</td>
      <td>166</td>
      <td>185</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>179</td>
      <td>378</td>
      <td>186</td>
      <td>385</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>379</td>
      <td>383</td>
      <td>386</td>
      <td>390</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>384</td>
      <td>511</td>
      <td>391</td>
      <td>518</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>534</td>
      <td>519</td>
      <td>541</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>535</td>
      <td>537</td>
      <td>542</td>
      <td>544</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>538</td>
      <td>587</td>
      <td>545</td>
      <td>594</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>588</td>
      <td>589</td>
      <td>595</td>
      <td>596</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>590</td>
      <td>614</td>
      <td>597</td>
      <td>621</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>615</td>
      <td>780</td>
      <td>622</td>
      <td>787</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>781</td>
      <td>804</td>
      <td>788</td>
      <td>811</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>805</td>
      <td>806</td>
      <td>812</td>
      <td>813</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>807</td>
      <td>824</td>
      <td>814</td>
      <td>831</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u1w">4U1W</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">N</span><span class="topo-outside">SIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVVTLT</span><span class="topo-unknown">EDDTSGL</span><span class="topo-outside">EQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VIDFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLA</span><span class="topo-unknown">YE</span><span class="topo-outside">I</span><span class="topo-membrane">WMAIVFAYIGVSVVLFLV</span><span class="topo-inside">S</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSESTNEFGIFNSLWFSLGAFFQQGADIS</span><span class="topo-inside">PRS</span><span class="topo-membrane">LSARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIIISSYTANLA</span><span class="topo-outside">AFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-outside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKDSGSKEKTSA</span><span class="topo-membrane">LSLSNVAGVFYILVGGLGLAMLV</span><span class="topo-inside">ALIEFAYK</span><span class="topo-unknown">SRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>8</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>376</td>
      <td>9</td>
      <td>383</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>383</td>
      <td>384</td>
      <td>390</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>384</td>
      <td>515</td>
      <td>391</td>
      <td>522</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>517</td>
      <td>523</td>
      <td>524</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>518</td>
      <td>518</td>
      <td>525</td>
      <td>525</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>519</td>
      <td>536</td>
      <td>526</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>537</td>
      <td>537</td>
      <td>544</td>
      <td>544</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>538</td>
      <td>585</td>
      <td>545</td>
      <td>592</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>586</td>
      <td>588</td>
      <td>593</td>
      <td>595</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>589</td>
      <td>614</td>
      <td>596</td>
      <td>621</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>615</td>
      <td>779</td>
      <td>622</td>
      <td>786</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>780</td>
      <td>802</td>
      <td>787</td>
      <td>809</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>810</td>
      <td>810</td>
      <td>817</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>811</td>
      <td>824</td>
      <td>818</td>
      <td>831</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u1x">4U1X</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVVTLTEDDTSGLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VIDFSKPFMSLGISIMIKKPQK</span><span class="topo-unknown">SKPGV</span><span class="topo-outside">F</span><span class="topo-membrane">SFLDPLAYEIWMAIVFAYILVSVVLFL</span><span class="topo-inside">VS</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSESTNEFGIFNSFWFALKLFFQQGADIS</span><span class="topo-inside">PRSL</span><span class="topo-membrane">SARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIIISSYTANLA</span><span class="topo-outside">AFLTVERM</span><span class="topo-unknown">V</span><span class="topo-outside">SPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-outside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAK</span><span class="topo-unknown">DSGSKEKT</span><span class="topo-outside">SAL</span><span class="topo-membrane">SLSNVAGVFYILVGGLGLAMLVA</span><span class="topo-inside">LI</span><span class="topo-unknown">EFAYKSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>502</td>
      <td>8</td>
      <td>509</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>508</td>
      <td>508</td>
      <td>515</td>
      <td>515</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>509</td>
      <td>535</td>
      <td>516</td>
      <td>542</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>537</td>
      <td>543</td>
      <td>544</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>589</td>
      <td>593</td>
      <td>596</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>590</td>
      <td>614</td>
      <td>597</td>
      <td>621</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>615</td>
      <td>622</td>
      <td>622</td>
      <td>629</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>624</td>
      <td>769</td>
      <td>631</td>
      <td>776</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>778</td>
      <td>780</td>
      <td>785</td>
      <td>787</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>781</td>
      <td>803</td>
      <td>788</td>
      <td>810</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>804</td>
      <td>805</td>
      <td>811</td>
      <td>812</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u1x">4U1X</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVVTLTEDD</span><span class="topo-unknown">TSG</span><span class="topo-outside">LEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VIDFSKPFMSLGISIMIKKPQKSKPGV</span><span class="topo-unknown">FSFLD</span><span class="topo-outside">P</span><span class="topo-membrane">LAYEIWMAIVFAYILVSVVL</span><span class="topo-inside">FLV</span><span class="topo-unknown">SRFSPYEWHTEEFEDGRETQSSESTNEFGIFNSFWFALKLFFQQGADISPRSLS</span><span class="topo-inside">A</span><span class="topo-membrane">RIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIIISSYTANLA</span><span class="topo-outside">AFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-outside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAK</span><span class="topo-unknown">DSGSKEKTS</span><span class="topo-outside">AL</span><span class="topo-membrane">SLSNVAGVFYILVGGLGLAMLV</span><span class="topo-inside">ALIEFAY</span><span class="topo-unknown">KSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>379</td>
      <td>8</td>
      <td>386</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>507</td>
      <td>390</td>
      <td>514</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>513</td>
      <td>513</td>
      <td>520</td>
      <td>520</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>514</td>
      <td>533</td>
      <td>521</td>
      <td>540</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>534</td>
      <td>536</td>
      <td>541</td>
      <td>543</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>591</td>
      <td>591</td>
      <td>598</td>
      <td>598</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>592</td>
      <td>614</td>
      <td>599</td>
      <td>621</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>615</td>
      <td>769</td>
      <td>622</td>
      <td>776</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>779</td>
      <td>780</td>
      <td>786</td>
      <td>787</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>781</td>
      <td>802</td>
      <td>788</td>
      <td>809</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>809</td>
      <td>810</td>
      <td>816</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u1x">4U1X</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">N</span><span class="topo-outside">SIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVVTLTE</span><span class="topo-unknown">DDTSG</span><span class="topo-outside">LEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VIDFSKPFMSLGISIMIKKPQKSKPGVFSFL</span><span class="topo-membrane">DPLAYEIWMAIVFAYILVSVVLFL</span><span class="topo-inside">VSRF</span><span class="topo-unknown">SPYEWHTEEFEDGRETQSSESTNEFGIFNSFWFALKLFFQQGADIS</span><span class="topo-inside">PRSL</span><span class="topo-membrane">SARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIIISSYTANLA</span><span class="topo-outside">AFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-outside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKDSGSKEKTSA</span><span class="topo-membrane">LSLSNVAGVFYILVGGLGLAMLV</span><span class="topo-inside">ALIEF</span><span class="topo-unknown">AYKSRAEAKRMKGLVPR</span></span>
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
      <td>2</td>
      <td>377</td>
      <td>9</td>
      <td>384</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>511</td>
      <td>390</td>
      <td>518</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>535</td>
      <td>519</td>
      <td>542</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>539</td>
      <td>543</td>
      <td>546</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>589</td>
      <td>593</td>
      <td>596</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>590</td>
      <td>614</td>
      <td>597</td>
      <td>621</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>615</td>
      <td>779</td>
      <td>622</td>
      <td>786</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>780</td>
      <td>802</td>
      <td>787</td>
      <td>809</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>807</td>
      <td>810</td>
      <td>814</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u1x">4U1X</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">NS</span><span class="topo-outside">IQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVVTLTE</span><span class="topo-unknown">DDTSG</span><span class="topo-outside">LEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VIDFSKPFMSLGISIMIKKPQKSKPGVFSFL</span><span class="topo-membrane">DPLAYEIWMAIVFAYILVSVVLFL</span><span class="topo-inside">VS</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSESTNEFGIFNSFWFALKLFFQQGADIS</span><span class="topo-inside">PRSL</span><span class="topo-membrane">SARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIIISSYTANLA</span><span class="topo-outside">AFLTV</span><span class="topo-unknown">ER</span><span class="topo-outside">MVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-outside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECG</span><span class="topo-unknown">AKDSGSK</span><span class="topo-outside">EKTSAL</span><span class="topo-membrane">SLSNVAGVFYILVGGLGLAMLVA</span><span class="topo-inside">LIEFA</span><span class="topo-unknown">YKSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>377</td>
      <td>10</td>
      <td>384</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>511</td>
      <td>390</td>
      <td>518</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>512</td>
      <td>535</td>
      <td>519</td>
      <td>542</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>537</td>
      <td>543</td>
      <td>544</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>589</td>
      <td>593</td>
      <td>596</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>590</td>
      <td>614</td>
      <td>597</td>
      <td>621</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>615</td>
      <td>619</td>
      <td>622</td>
      <td>626</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>622</td>
      <td>767</td>
      <td>629</td>
      <td>774</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>775</td>
      <td>780</td>
      <td>782</td>
      <td>787</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>781</td>
      <td>803</td>
      <td>788</td>
      <td>810</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>804</td>
      <td>808</td>
      <td>811</td>
      <td>815</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u1y">4U1Y</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINV</span><span class="topo-unknown">GNINNDKKDETYRSLFQDLELK</span><span class="topo-inside">KERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">KIGYWSEVDKMVVTLTED</span><span class="topo-unknown">DTSGL</span><span class="topo-inside">EQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">VIDFSKPFMSLGISIMIKKPQK</span><span class="topo-unknown">SKPG</span><span class="topo-inside">VFSFLDPLAY</span><span class="topo-membrane">EIWMAIVFAYILVSVVLFLV</span><span class="topo-outside">S</span><span class="topo-unknown">RFSPYEWHTEEFEDGEESTNEFGIFNSFWFALKLFFQQGADISP</span><span class="topo-outside">R</span><span class="topo-membrane">SLSARIVAGVWWFFTLII</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">ISSYT</span><span class="topo-inside">ANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDSKGY</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810         </span>
<span class="topo-line"><span class="topo-inside">GIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKD</span><span class="topo-unknown">SGSKEKT</span><span class="topo-inside">SALSLSN</span><span class="topo-membrane">VAGVFYILVGGLGLAMLVA</span><span class="topo-outside">LIEF</span><span class="topo-unknown">AYKSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>156</td>
      <td>8</td>
      <td>163</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>179</td>
      <td>378</td>
      <td>186</td>
      <td>385</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>502</td>
      <td>391</td>
      <td>509</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>507</td>
      <td>516</td>
      <td>514</td>
      <td>523</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>536</td>
      <td>524</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>537</td>
      <td>537</td>
      <td>544</td>
      <td>544</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>582</td>
      <td>582</td>
      <td>594</td>
      <td>594</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>583</td>
      <td>605</td>
      <td>595</td>
      <td>617</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>606</td>
      <td>765</td>
      <td>618</td>
      <td>777</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>773</td>
      <td>779</td>
      <td>785</td>
      <td>791</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>780</td>
      <td>798</td>
      <td>792</td>
      <td>810</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>799</td>
      <td>802</td>
      <td>811</td>
      <td>814</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u1y">4U1Y</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">NS</span><span class="topo-inside">IQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISR</span><span class="topo-unknown">RGNAGD</span><span class="topo-inside">CLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">KIGYWSEVDKMVVTLTEDDTSGLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">VIDFSKPFMSLGISIMIKKPQK</span><span class="topo-unknown">SKPGVFS</span><span class="topo-inside">FLDPLAYEI</span><span class="topo-membrane">WMAIVFAYILVSVVLFLVSRF</span><span class="topo-unknown">SPYEWHTEEFEDGEESTNEFGIFNSFWFALKLFFQQGADISP</span><span class="topo-outside">R</span><span class="topo-membrane">SLSARIVAGVWWFFTLII</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">IS</span><span class="topo-inside">SYTANLAAFLTVERM</span><span class="topo-unknown">VSP</span><span class="topo-inside">IESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDSKGY</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810         </span>
<span class="topo-line"><span class="topo-inside">GIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECG</span><span class="topo-unknown">AKDSGSKEKTSAL</span><span class="topo-inside">SLSNV</span><span class="topo-membrane">AGVFYILVGGLGLAMLVALI</span><span class="topo-outside">EFAY</span><span class="topo-unknown">KSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>299</td>
      <td>10</td>
      <td>306</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>502</td>
      <td>313</td>
      <td>509</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>518</td>
      <td>517</td>
      <td>525</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>519</td>
      <td>539</td>
      <td>526</td>
      <td>546</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>582</td>
      <td>582</td>
      <td>594</td>
      <td>594</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>583</td>
      <td>602</td>
      <td>595</td>
      <td>614</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>603</td>
      <td>617</td>
      <td>615</td>
      <td>629</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>621</td>
      <td>762</td>
      <td>633</td>
      <td>774</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>776</td>
      <td>780</td>
      <td>788</td>
      <td>792</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>781</td>
      <td>800</td>
      <td>793</td>
      <td>812</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>801</td>
      <td>804</td>
      <td>813</td>
      <td>816</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u1y">4U1Y</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">NSI</span><span class="topo-inside">QIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNI</span><span class="topo-unknown">NNDKK</span><span class="topo-inside">DETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">KIGYWSEVDKMVVTLTE</span><span class="topo-unknown">DDTSGLE</span><span class="topo-inside">QKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">VIDFSKPFMSLGISIMIKKP</span><span class="topo-unknown">QKSKPGVFS</span><span class="topo-inside">FLDPLAYEI</span><span class="topo-membrane">WMAIVFAYILVSVVLFLVS</span><span class="topo-unknown">RFSPYEWHTEEFEDGEESTNEFGIFNSFWFALKLFFQQGADIS</span><span class="topo-outside">PRSL</span><span class="topo-membrane">SARIVAGVWWFFTLII</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">ISS</span><span class="topo-inside">YTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDSKGY</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810         </span>
<span class="topo-line"><span class="topo-inside">GIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGEC</span><span class="topo-unknown">GAKDS</span><span class="topo-inside">GSKEKTSALSLSNV</span><span class="topo-membrane">AGVFYILVGGLGLAMLVALI</span><span class="topo-outside">EF</span><span class="topo-unknown">AYKSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>4</td>
      <td>159</td>
      <td>11</td>
      <td>166</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>377</td>
      <td>172</td>
      <td>384</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>385</td>
      <td>500</td>
      <td>392</td>
      <td>507</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>518</td>
      <td>517</td>
      <td>525</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>519</td>
      <td>537</td>
      <td>526</td>
      <td>544</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>581</td>
      <td>584</td>
      <td>593</td>
      <td>596</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>585</td>
      <td>603</td>
      <td>597</td>
      <td>615</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>604</td>
      <td>761</td>
      <td>616</td>
      <td>773</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>767</td>
      <td>780</td>
      <td>779</td>
      <td>792</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>781</td>
      <td>800</td>
      <td>793</td>
      <td>812</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>801</td>
      <td>802</td>
      <td>813</td>
      <td>814</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u1y">4U1Y</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">NSI</span><span class="topo-inside">QIGGLFPRGADQEYSAFRVGMVQF</span><span class="topo-unknown">STSEFRL</span><span class="topo-inside">TPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">KIGYWSEVDKMVVT</span><span class="topo-unknown">LTEDDTSGLE</span><span class="topo-inside">QKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">VIDFSKPFMSLGISIMIKKPQKS</span><span class="topo-unknown">KP</span><span class="topo-inside">GVFSFLDPLAY</span><span class="topo-membrane">EIWMAIVFAYILVSVVLFL</span><span class="topo-outside">V</span><span class="topo-unknown">SRFSPYEWHTEEFEDGEESTNEFGIFNSFWFALKLFFQQGADISPRS</span><span class="topo-outside">L</span><span class="topo-membrane">SARIVAGVWWFFTLII</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">ISSYT</span><span class="topo-inside">ANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNLDSKGY</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810         </span>
<span class="topo-line"><span class="topo-inside">GIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGA</span><span class="topo-unknown">KDSGSKEKT</span><span class="topo-inside">SALSLSNV</span><span class="topo-membrane">AGVFYILVGGLGLAMLVALI</span><span class="topo-outside">EFAYK</span><span class="topo-unknown">SRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (12 regions)</summary>
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
      <td>4</td>
      <td>27</td>
      <td>11</td>
      <td>34</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>374</td>
      <td>42</td>
      <td>381</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>385</td>
      <td>503</td>
      <td>392</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>506</td>
      <td>516</td>
      <td>513</td>
      <td>523</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>517</td>
      <td>535</td>
      <td>524</td>
      <td>542</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>536</td>
      <td>536</td>
      <td>543</td>
      <td>543</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>584</td>
      <td>584</td>
      <td>596</td>
      <td>596</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>585</td>
      <td>605</td>
      <td>597</td>
      <td>617</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>606</td>
      <td>763</td>
      <td>618</td>
      <td>775</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>773</td>
      <td>780</td>
      <td>785</td>
      <td>792</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>781</td>
      <td>800</td>
      <td>793</td>
      <td>812</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>801</td>
      <td>805</td>
      <td>813</td>
      <td>817</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u2q">4U2Q</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVG</span><span class="topo-unknown">NINNDKKDETYRSLFQDLEL</span><span class="topo-inside">KKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">KIGYWSEVDKMVVTLTED</span><span class="topo-unknown">DTSG</span><span class="topo-inside">LEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">VIDFSKPFMSLGISIMIKK</span><span class="topo-unknown">PQK</span><span class="topo-inside">S</span><span class="topo-unknown">K</span><span class="topo-inside">PGVFSFLDPLAYEI</span><span class="topo-membrane">WMAIVFAYIGVSVVLFLV</span><span class="topo-outside">S</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSESTNEFGIFNSLWFSLGAFFQQGADIS</span><span class="topo-outside">P</span><span class="topo-membrane">RSLSARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIII</span><span class="topo-inside">SSYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-inside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGEC</span><span class="topo-unknown">GAKDSGSKEKT</span><span class="topo-inside">SALSLSNVAGV</span><span class="topo-membrane">FYILVGGLGLAMLVALIE</span><span class="topo-outside">FA</span><span class="topo-unknown">YKSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>157</td>
      <td>8</td>
      <td>164</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>178</td>
      <td>378</td>
      <td>185</td>
      <td>385</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>499</td>
      <td>390</td>
      <td>506</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>503</td>
      <td>503</td>
      <td>510</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>505</td>
      <td>518</td>
      <td>512</td>
      <td>525</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>519</td>
      <td>536</td>
      <td>526</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>537</td>
      <td>537</td>
      <td>544</td>
      <td>544</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>586</td>
      <td>593</td>
      <td>593</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>587</td>
      <td>606</td>
      <td>594</td>
      <td>613</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>607</td>
      <td>766</td>
      <td>614</td>
      <td>773</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>778</td>
      <td>788</td>
      <td>785</td>
      <td>795</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>789</td>
      <td>806</td>
      <td>796</td>
      <td>813</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>807</td>
      <td>808</td>
      <td>814</td>
      <td>815</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u2q">4U2Q</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">N</span><span class="topo-inside">SIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">KIGYWSEVDKMVVTL</span><span class="topo-unknown">TEDDTSG</span><span class="topo-inside">LEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">VIDFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYEI</span><span class="topo-membrane">WMAIVFAYIGVSVVLFLV</span><span class="topo-outside">S</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSESTNEFGIFNSLWFSLGAFFQQGADIS</span><span class="topo-outside">PR</span><span class="topo-membrane">SLSARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIII</span><span class="topo-inside">SSYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-inside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAK</span><span class="topo-unknown">DSGSKE</span><span class="topo-inside">KTSALSLSNVAGV</span><span class="topo-membrane">FYILVGGLGLAMLVALI</span><span class="topo-outside">EFA</span><span class="topo-unknown">YKSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
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
      <td>375</td>
      <td>9</td>
      <td>382</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>383</td>
      <td>518</td>
      <td>390</td>
      <td>525</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>519</td>
      <td>536</td>
      <td>526</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>537</td>
      <td>537</td>
      <td>544</td>
      <td>544</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>587</td>
      <td>593</td>
      <td>594</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>588</td>
      <td>606</td>
      <td>595</td>
      <td>613</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>607</td>
      <td>769</td>
      <td>614</td>
      <td>776</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>776</td>
      <td>788</td>
      <td>783</td>
      <td>795</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>789</td>
      <td>805</td>
      <td>796</td>
      <td>812</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>806</td>
      <td>808</td>
      <td>813</td>
      <td>815</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u2q">4U2Q</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">KIGYWSEVDKMVVTLTEDD</span><span class="topo-unknown">TS</span><span class="topo-inside">GLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">VIDFSKPFMSLGISIMIKKPQKS</span><span class="topo-unknown">KP</span><span class="topo-inside">G</span><span class="topo-unknown">VFSFLD</span><span class="topo-inside">PLAYE</span><span class="topo-membrane">IWMAIVFAYIGVSVVLFLV</span><span class="topo-outside">S</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSESTNEFGIFNSLWFSLGAFFQQGADISPRS</span><span class="topo-outside">L</span><span class="topo-membrane">SARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIIIS</span><span class="topo-inside">SYTANLAAFLTVERMVS</span><span class="topo-unknown">PI</span><span class="topo-inside">ESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-inside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGA</span><span class="topo-unknown">KDSGSKE</span><span class="topo-inside">KTSALSLSNVA</span><span class="topo-membrane">GVFYILVGGLGLAMLVALI</span><span class="topo-outside">EFA</span><span class="topo-unknown">YKSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>379</td>
      <td>8</td>
      <td>386</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>503</td>
      <td>389</td>
      <td>510</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>506</td>
      <td>506</td>
      <td>513</td>
      <td>513</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>507</td>
      <td>512</td>
      <td>514</td>
      <td>519</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>513</td>
      <td>517</td>
      <td>520</td>
      <td>524</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>518</td>
      <td>536</td>
      <td>525</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>537</td>
      <td>537</td>
      <td>544</td>
      <td>544</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>589</td>
      <td>589</td>
      <td>596</td>
      <td>596</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>590</td>
      <td>607</td>
      <td>597</td>
      <td>614</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>608</td>
      <td>624</td>
      <td>615</td>
      <td>631</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>627</td>
      <td>768</td>
      <td>634</td>
      <td>775</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>776</td>
      <td>786</td>
      <td>783</td>
      <td>793</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>787</td>
      <td>805</td>
      <td>794</td>
      <td>812</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>806</td>
      <td>808</td>
      <td>813</td>
      <td>815</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u2q">4U2Q</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">KIGYWSEVDKMVVTLTEDDTS</span><span class="topo-unknown">GLE</span><span class="topo-inside">QKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">VIDFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYEI</span><span class="topo-membrane">WMAIVFAYIGVSVVLFLV</span><span class="topo-outside">S</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSESTNEFGIFNSLWFSLGAFFQQGADIS</span><span class="topo-outside">PR</span><span class="topo-membrane">SLSARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIIIS</span><span class="topo-inside">SYTANLAAFLTVERM</span><span class="topo-unknown">VSP</span><span class="topo-inside">IESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-inside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKD</span><span class="topo-unknown">SGSK</span><span class="topo-inside">EKTSALSLSNV</span><span class="topo-membrane">AGVFYILVGGLGLAMLVALI</span><span class="topo-outside">EF</span><span class="topo-unknown">AYKSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>381</td>
      <td>8</td>
      <td>388</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>385</td>
      <td>518</td>
      <td>392</td>
      <td>525</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>519</td>
      <td>536</td>
      <td>526</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>537</td>
      <td>537</td>
      <td>544</td>
      <td>544</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>587</td>
      <td>593</td>
      <td>594</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>588</td>
      <td>607</td>
      <td>595</td>
      <td>614</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>608</td>
      <td>622</td>
      <td>615</td>
      <td>629</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>626</td>
      <td>770</td>
      <td>633</td>
      <td>777</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>775</td>
      <td>785</td>
      <td>782</td>
      <td>792</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>786</td>
      <td>805</td>
      <td>793</td>
      <td>812</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>806</td>
      <td>807</td>
      <td>813</td>
      <td>814</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u2p">4U2P</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">NS</span><span class="topo-outside">IQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVVTLTEDDTSGLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VIDFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYEIW</span><span class="topo-membrane">MAIVFAYIGVSVVL</span><span class="topo-inside">FLVSR</span><span class="topo-unknown">FSPYEWHTEEFEDGRETQSSESTNEFGIFNSLWFSLGAFFQQGADIS</span><span class="topo-inside">PRSL</span><span class="topo-membrane">SARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIII</span><span class="topo-outside">SSYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-outside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNVAGV</span><span class="topo-membrane">FYILVGGLGLAML</span><span class="topo-inside">VAL</span><span class="topo-unknown">IEFAYKSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>519</td>
      <td>10</td>
      <td>526</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>520</td>
      <td>533</td>
      <td>527</td>
      <td>540</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>534</td>
      <td>538</td>
      <td>541</td>
      <td>545</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>589</td>
      <td>593</td>
      <td>596</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>590</td>
      <td>606</td>
      <td>597</td>
      <td>613</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>607</td>
      <td>788</td>
      <td>614</td>
      <td>795</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>789</td>
      <td>801</td>
      <td>796</td>
      <td>808</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>802</td>
      <td>804</td>
      <td>809</td>
      <td>811</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u2p">4U2P</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVVTLTEDDTSGLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VIDFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYEIWM</span><span class="topo-membrane">AIVFAYIGVSVVLF</span><span class="topo-inside">LVS</span><span class="topo-unknown">RFSPYEWHTEEFEDGRETQSSESTNEFGIFNSLWFSLGAFFQQGADIS</span><span class="topo-inside">PRSL</span><span class="topo-membrane">SARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIII</span><span class="topo-outside">SSYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-outside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNVAGV</span><span class="topo-membrane">FYILVGGLGLAMLV</span><span class="topo-inside">ALIEFAY</span><span class="topo-unknown">KSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>520</td>
      <td>8</td>
      <td>527</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>521</td>
      <td>534</td>
      <td>528</td>
      <td>541</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>535</td>
      <td>537</td>
      <td>542</td>
      <td>544</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>589</td>
      <td>593</td>
      <td>596</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>590</td>
      <td>606</td>
      <td>597</td>
      <td>613</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>607</td>
      <td>788</td>
      <td>614</td>
      <td>795</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>789</td>
      <td>802</td>
      <td>796</td>
      <td>809</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>809</td>
      <td>810</td>
      <td>816</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u2p">4U2P</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVVTLTEDDTSGLEQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VIDFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYEIW</span><span class="topo-membrane">MAIVFAYIGVSVVL</span><span class="topo-inside">FL</span><span class="topo-unknown">VSRFSPYEWHTEEFEDGRETQSSESTNEFGIFNSLWFSLGAFFQQGADISPRS</span><span class="topo-inside">LS</span><span class="topo-membrane">ARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIII</span><span class="topo-outside">SSYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-outside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNVAGV</span><span class="topo-membrane">FYILVGGLGLAMLV</span><span class="topo-inside">AL</span><span class="topo-unknown">IEFAYKSRAEAKRMKGLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
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
      <td>519</td>
      <td>8</td>
      <td>526</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>520</td>
      <td>533</td>
      <td>527</td>
      <td>540</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>534</td>
      <td>535</td>
      <td>541</td>
      <td>542</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>589</td>
      <td>590</td>
      <td>596</td>
      <td>597</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>591</td>
      <td>606</td>
      <td>598</td>
      <td>613</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>607</td>
      <td>788</td>
      <td>614</td>
      <td>795</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>789</td>
      <td>802</td>
      <td>796</td>
      <td>809</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>804</td>
      <td>810</td>
      <td>811</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4u2p">4U2P</a> — Chain C (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NSIQIGGLFPRGADQEYSAFRVGMVQFSTSEFRLTPHIDNLEVANSFAVTNAFCSQFSRGVYAIFGFYDKKSVNTITSFCGTLHVSFITPSFPTDGTHPFVIQMRPDLKGALLSLIEYYQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">WDKFAYLYDSDRGLSTLQAVLDSAAEKKWQVTAINVGNINNDKKDETYRSLFQDLELKKERRVILDCERDKVNDIVDQVITIGKHVKGYHYIIANLGFTDGDLLKIQFGGAEVSGFQIVD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">YDDSLVSKFIERWSTLEEKEYPGAHTATIKYTSALTYDAVQVMTEAFRNLRKQRIEISRRGNAGDCLANPAVPWGQGVEIERALKQVQVEGLSGNIKFDQNGKRINYTINIMELKTNGPR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KIGYWSEVDKMVVTLTEDD</span><span class="topo-unknown">TSGL</span><span class="topo-outside">EQKTVVVTTILESPYVMMKKNHEMLEGNERYEGYCVDLAAEIAKHCGFKYKLTIVGDGKYGARDADTKIWNGMVGELVYGKADIAIAPLTITLVREE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">VIDFSKPFMSLGISIMIKKPQKSKPGVFSFLDPLAYEIWM</span><span class="topo-membrane">AIVFAYIGVSVVL</span><span class="topo-inside">FLV</span><span class="topo-unknown">SRFSPYEWHTEEFEDGRETQSSESTNEFGIFNSLWFSLGAFFQQGADISP</span><span class="topo-inside">RSLS</span><span class="topo-membrane">ARIVAGVWWF</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">FTLIII</span><span class="topo-outside">SSYTANLAAFLTVERMVSPIESAEDLSKQTEIAYGTLDSGSTKEFFRRSKIAVFDKMWTYMRSAEPSVFVRTTAEGVARVRKSKGKYAYLLESTMNEYIEQRKPCDTMKVGGNL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820    </span>
<span class="topo-line"><span class="topo-outside">DSKGYGIATPKGSSLGTPVNLAVLKLSEQGVLDKLKNKWWYDKGECGAKDSGSKEKTSALSLSNVAGVF</span><span class="topo-membrane">YILVGGLGLAMLV</span><span class="topo-inside">ALIEFAY</span><span class="topo-unknown">KSRAEAKRMKGLVPR</span></span>
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
      <td>379</td>
      <td>8</td>
      <td>386</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>384</td>
      <td>520</td>
      <td>391</td>
      <td>527</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>521</td>
      <td>533</td>
      <td>528</td>
      <td>540</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>534</td>
      <td>536</td>
      <td>541</td>
      <td>543</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>587</td>
      <td>590</td>
      <td>594</td>
      <td>597</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>591</td>
      <td>606</td>
      <td>598</td>
      <td>613</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>607</td>
      <td>789</td>
      <td>614</td>
      <td>796</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>790</td>
      <td>802</td>
      <td>797</td>
      <td>809</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>803</td>
      <td>809</td>
      <td>810</td>
      <td>816</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>


## Biological / Functional Insights

### First full-length iGluR structure reveals Y-shaped tetrameric architecture

The 3.6 A crystal structure of the full-length rat GluA2cryst receptor (Sobolevsky et al., 2009) was the first X-ray structure of any intact ionotropic glutamate receptor. It revealed a Y-shaped tetramer composed of three distinct layers: the amino-terminal domain (ATD), the ligand-binding domain (LBD), and the transmembrane domain (TMD). The ATD and LBD form dimer-of-dimers assemblies with 2-fold symmetry, while the TMD adopts a 4-fold symmetric ion channel pore. The ATD dimers are arranged in a swapped configuration, with two pairs of ATD-LBD subunit arrangements (A/C and B/D) that are structurally distinct.

### Agonist-bound GluA2 structure reveals LBD clamshell closure in intact receptor

The structure of GluA2 in complex with partial agonist (S)-5-nitrowillardine (NOW) (Yelshanskaya et al., 2014, Science) provides structural evidence of clamshell motion in the context of an intact, multidomain iGluR. The LBD clamshells are ~11 degrees more closed in the NOW-bound state compared to the ZK 200775 antagonist-bound state. This conformational change is smaller than in agonist-bound structures of isolated LBDs (up to ~14 degrees). The tension from altered LBD dimer conformation pulls ATD dimers down, tilting them ~1.2 degrees, and pulls the ion channel up, making the structure ~2 A shorter. The interface between the two LBD dimers becomes tighter and covers a surface area three times larger than in the antagonist-bound state.

### Agonist-induced LBD dimer interface tightening and gating

Disulfide cross-linking experiments with GluA2-I664C demonstrated that agonist-induced tightening of the LBD dimer-dimer interface occurs during gating. In nonreducing conditions, recovery from desensitization was incomplete, consistent with agonist-induced interface tightening. Cross-linking at the D1-D1 interface (P494C, S497C) promoted channel opening, while cross-linking at D2 lobes produced negative effects on iGluR activation. These findings support two possible gating models where LBDs are highly mobile and agonist binding causes clamshell closure.

### Cone snail toxin stabilizes LBD gating ring in expanded conformation

The con-ikot-ikot toxin from Conus striatus acts like a straightjacket on the LBD gating ring (Chen et al., 2014, Science). The toxin spans the tetrameric LBD gating ring, participating in extensive interactions with all four subunits, simultaneously fortifying intradimer interfaces and spanning the interdimer cleft. The electrostatic surface of the toxin shows extensive negative patches complementary to positively charged residues on the receptor surface. Toxin binding requires agonist-induced clamshell closure, as it binds to both D1 and D2 lobes of LBD A/C pair subunits.

### Iris-like expansion of the LBD gating ring

The toxin complex structures reveal that the LBD gating ring adopts an expanded conformation. The interaxis angle between LBD dimers is smaller in the toxin complex than in the antagonist-bound ZK structure. The S640 C-alpha marker atoms show an 8.4 A increase in separation between D2 lobes upon transition from the ZK antagonist state to the FW agonist-bound structure. The toxin stabilizes the D1-D1 interface in a nondesensitized conformation with S741 C-alpha distances of 19.3-19.7 A. The expansion is asymmetric, with the A/C pair showing 3.4 A additional separation and the B/D pair showing 12.4 A separation, consistent with symmetry nonequivalence.

### I633 coupling mechanism in M3-LBD linkers

The I633 residue from the B/D subunits couples agonist binding to ion channel gating. In non-M3-mutant structures, I633 from B/D subunits adopts an uncoupled conformation pulled out of the hydrophobic D2 pocket. In Lurcher-like mutant structures (A622T, T625G), I633 from B/D subunits binds within a hydrophobic pocket formed by V732, I504, L639, and I645 on the D2 lobe, adopting a coupled conformation. The I633A and I633E mutants show severely diminished currents, confirming I633's essential role. The coupling is asymmetric, with B/D subunits showing larger conformational changes than A/C subunits.

### 4-BCCA binds at TMD side portals distinct from known modulators

4-BCCA binds at the lateral portals formed by transmembrane segments M1-M4 at the intersubunit interfaces. These sites are distinct from the perampanel binding site (extracellular collar) and polyamine/ion channel blocker sites. The binding pocket is formed by mostly hydrophobic residues from M1 (L521, W526, I529), M2 (F584, M585), and M3 (T609, I612, I613, Y616, T617) of one subunit and M3 (F607, L610, I611, S614) of the neighboring subunit.

### Simultaneous binding of competitive antagonist and NAM

The X-ray structure of GluA2cryst with ZK200775 (competitive antagonist) and GYKI53655 (NAM) at 4.65 A demonstrates that four molecules of each antagonist can bind simultaneously without mutual interference. ZK200775 occupies all four LBD binding sites with the same domain-opening as in the ZK200775-only structure (3KG2). GYKI53655 occupies all four NAM pockets near the TMD-LBD linker. The two binding events are structurally independent.

### Full-length GluA2 structures in apo resting, pre-open, and desensitized states

Dürr et al. (2014, Cell) determined X-ray crystal structures of the intact homotetrameric GluA2 AMPA receptor in three functionally distinct states: (1) an apo resting/closed state (PDB 4U2P, 3.71 A), (2) agonist-bound pre-open/activated states stabilized by the positive allosteric modulator (R,R)-2b in complex with partial agonists kainate (KA) or fluorowilliardiine (FW) (PDBs 4U1W, 4U1X, 4U1Y, 3.6-4.3 A), and (3) an FW-bound desensitized state (~8 A, solved by molecular replacement with cryo-EM validation). These structures, combined with DEER spectroscopy and cryo-EM, provide a near-comprehensive view of AMPA receptor gating transitions. The structures revealed that the LBD layer undergoes large conformational rearrangements, with the LBD gating ring expanding upon activation and contracting upon desensitization.

### LBD gating ring expansion upon activation

Comparison of the apo and pre-open structures (KA+(R,R)-2b and FW+(R,R)-2b) reveals that agonist binding modulates the conformation of the LBD layer. The D2-D2 separation increases by 6-7 A in both diagonal pairs (AC and BD), reflecting an enhanced mechanical pulling force exerted by bound partial agonists. The angle between LBD dimer local 2-fold axes (roll angle) increases from 34.6 degrees in apo to 52.2-55.6 degrees in modulator-bound states. Despite these movements, the ion channel pore remains closed, suggesting these represent a pre-open state. DEER spectroscopy confirmed the D2-D2 distance increases. The (R,R)-2b modulator binds at the D1-D1 interface, stabilizing it in a nondesensitized conformation.

### Large conformational rearrangements upon desensitization

The low-resolution (8 A) X-ray structure of GluA2 in complex with FW alone (desensitizing conditions) reveals dramatic conformational changes. One ATD dimer (AB) is tilted downward by ~89 degrees, approaching the side of the other ATD dimer (CD). The D1-D1 interfaces are disrupted in both LBD dimers. In the AD pair, the LBD monomers become more separated than in the S729C disulfide-trapped structure, with the LBD of chain D rotated outward by ~105 degrees. Cryo-EM studies confirm the conformational heterogeneity of the desensitized state, with particles showing a range of compact and bulgy conformations compared to the more uniform Y-shaped pre-open state. This domain-swapped architecture explains why disruption of the LBD dimer interface destabilizes the Y-shaped resting state.


## Cross-References

- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/non-competitive-inhibition/">Non-competitive Inhibition</a> — 4-BCCA and GYKI53655 are non-competitive inhibitors of AMPA receptors binding at distinct TMD sites from the orthosteric glutamate site
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/">C-type Inactivation</a> — AMPA receptor gating and desensitization involve TMD conformational changes modulated by antagonist and NAM binding
- <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> — Referenced in glua2-ampa-receptor text
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Referenced in glua2-ampa-receptor text
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Referenced in glua2-ampa-receptor text
- <a href="/xray-mp-wiki/reagents/ligands/desthiobiotin/">Desthiobiotin</a> — Referenced in glua2-ampa-receptor text
- <a href="/xray-mp-wiki/reagents/additives/endoh/">Endoh</a> — Referenced in glua2-ampa-receptor text
- <a href="/xray-mp-wiki/reagents/additives/pmsf/">Pmsf</a> — Referenced in glua2-ampa-receptor text
- <a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> — Referenced in glua2-ampa-receptor text
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Referenced in glua2-ampa-receptor text
