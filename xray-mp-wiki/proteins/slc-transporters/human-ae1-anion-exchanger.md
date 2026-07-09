---
title: "Human AE1 Anion Exchanger (Band 3) - C-Terminal Membrane Domain"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aaa4335]
verified: regex
uniprot_id: P02730
---

# Human AE1 Anion Exchanger (Band 3) - C-Terminal Membrane Domain

<div class="expr-badges"><span class="expr-badge expr-native-tissue">Native tissue</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P02730">UniProt: P02730</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

Human AE1 (anion exchanger 1, also known as Band 3) is the most abundant membrane protein in erythrocytes, where it catalyzes the electroneutral exchange of bicarbonate and chloride ions across the plasma membrane. This exchange is essential for CO2 transport from tissues to lungs. AE1 is a 110-kD glycoprotein built from a cytosolic N-terminal domain (residues 1-360) and a C-terminal integral membrane domain (AE1_CTD, residues 361-911) that performs anion exchange. The crystal structure of AE1_CTD was determined at 3.5 Å resolution in an outward-facing open conformation, locked by the covalent inhibitor [H2DIDS (4,4-Diisothiocyanatodihydro-stilbene-2,2-disulfonic acid)](/xray-mp-wiki/reagents/additives/h2dids/) and in complex with a monoclonal antibody Fab fragment. The structure reveals 14 transmembrane segments arranged in two inverted repeats of seven TMs, forming core and gate domains. AE1_CTD is a physiological homodimer with the dimer interface formed exclusively through gate domain residues (TMs 5, 6, 7).


## Publications

### doi/10.1126##science.aaa4335

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4yzf">4YZF</a></td>
      <td>3.5</td>
      <td>—</td>
      <td>AE1_CTD (residues 381-887), N-terminally cleaved by <a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/h2dids/">H2DIDS (4,4-Diisothiocyanatodihydro-stilbene-2,2-disulfonic acid)</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Native human erythrocytes
- **Construct**: AE1_CTD (residues 381-887) - C-terminal membrane domain cleaved by [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/) from full-length AE1 purified from erythrocyte ghost membranes
- **Notes**: Protein purified directly from human erythrocyte white ghost membranes, not recombinantly expressed

**Purification:**

- **Expression system**: Native (human erythrocytes)
- **Expression construct**: Full-length AE1, C-terminal domain cleaved by [Trypsin](/xray-mp-wiki/reagents/additives/trypsin/)
- **Tag info**: No affinity tag used (native purification)

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
      <td>Ghost membrane preparation</td>
      <td>Hypotonic lysis and membrane isolation</td>
      <td>—</td>
      <td>— + —</td>
      <td>White ghost membranes prepared from human erythrocytes</td>
    </tr>
    <tr>
      <td>Proteolytic cleavage</td>
      <td><a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> digestion</td>
      <td>—</td>
      <td>— + —</td>
      <td>N-terminus of AE1_CTD cleaved by <a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> to release the C-terminal membrane domain</td>
    </tr>
    <tr>
      <td>Inhibitor treatment</td>
      <td>Chemical modification</td>
      <td>—</td>
      <td>— + —</td>
      <td>Treated with <a href="/xray-mp-wiki/reagents/additives/h2dids/">H2DIDS (4,4-Diisothiocyanatodihydro-stilbene-2,2-disulfonic acid)</a> (4,4-diisothiocyanatodihydro-stilbene-2,2-disulfonic acid) to irreversibly lock the outward-facing conformation</td>
    </tr>
    <tr>
      <td>Deglycosylation</td>
      <td>Enzymatic deglycosylation</td>
      <td>—</td>
      <td>— + —</td>
      <td>Deglycosylated with N-glycosidase F to obtain well-diffracting crystals</td>
    </tr>
  </tbody>
</table>
**Final sample**: Deglycosylated AE1_CTD-[H2DIDS (4,4-Diisothiocyanatodihydro-stilbene-2,2-disulfonic acid)](/xray-mp-wiki/reagents/additives/h2dids/) complex
**Yield**: —
**Purity**: —

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Co-crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>AE1_CTD-<a href="/xray-mp-wiki/reagents/additives/h2dids/">H2DIDS (4,4-Diisothiocyanatodihydro-stilbene-2,2-disulfonic acid)</a> complex with monoclonal antibody Fab fragment</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Co-crystallized with a monoclonal antibody Fab fragment that binds tightly to a conformational epitope of AE1_CTD. The antibody was selected from a panel raised by inoculation of mice with AE1_CTD-displaying baculovirus. Two steps were required for crystallization: (1) deglycosylation with N-glycosidase F, (2) co-crystallization with Fab fragment.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yzf">4YZF</a> — Chain A (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEELQDDYEDMMEENLEQEEYEDPDIPESQMEEPAAHDTEATATDYHTTSHPGTHKVYVELQELVMDEKNQELRWMEAARWVQLEENLGENGAWGRPHLSHLTFWSLLELRRVFTKGTVL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">LDLQETSLAGVANQLLDRFIFEDQIRPQDREELLRALLLKHSHAGELEALGGVKPAVLTRSGDPSQPLLPQHSSLETQLFCEQGDGGTEGHSPSGILEKIPPDSEATLVLVGRADFLEQP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">VLGFVRLQEAAELEAVELPVPIRFLFVLLGPEAPHIDYTQLGRAAATLMSERVFRIDAYMAQSRGELLHSLEGFLDCSLVLPPTDAPSEQALLSLVPVQRELLRRRYQSSPAKPDSSFYK</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-unknown">GLDLNGGPDDPLQQTGQLFG</span><span class="topo-inside">GLVRDIRRRYPYYLSDITDA</span><span class="topo-membrane">FSPQVLAAVIFIYFAALSPA</span><span class="topo-outside">ITFGGLLGEKTRNQMGVSEL</span><span class="topo-membrane">LISTAVQGILFALLG</span><span class="topo-inside">AQ</span><span class="topo-membrane">PLLVVGFSGPLLVFE</span><span class="topo-outside">EAFFSFCE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">TNGLEYIVGR</span><span class="topo-membrane">VWIGFWLILLVVLVV</span><span class="topo-inside">AFEGSFLVRFISRYTQEI</span><span class="topo-membrane">FSFLISLIFIYETFSKL</span><span class="topo-outside">IKIFQDHPLQKTY</span><span class="topo-unknown">NYNVLMVPKPQGP</span><span class="topo-outside">LPNTALLSL</span><span class="topo-membrane">VLMAGTFFFAMMLRKF</span><span class="topo-inside">KNSSYFPGK</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">LRRV</span><span class="topo-membrane">IGDFGVPISILIMVLV</span><span class="topo-outside">DFFIQDTYTQKLSVPDGFKV</span><span class="topo-unknown">SNSSARGW</span><span class="topo-outside">VIHPLGLRSEFPIWMM</span><span class="topo-membrane">FASALPALLVFILIFLESQITT</span><span class="topo-inside">LIVSKPERKMVKGSGFHL</span><span class="topo-membrane">DLLLVVGMGGVAALF</span><span class="topo-outside">G</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-membrane">PWLSATTVRSVTHANAL</span><span class="topo-inside">TVM</span><span class="topo-unknown">GKASTPGAAAQ</span><span class="topo-inside">IQEVKEQ</span><span class="topo-membrane">RISGLLVAVLVGLS</span><span class="topo-outside">ILMEPILSRIPLA</span><span class="topo-membrane">VLFGIFLYMGVTSLS</span><span class="topo-inside">GIQLFDRILLLFKPPKYHPDVPYVKRVKTWRMHLFTGIQ</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910 </span>
<span class="topo-line"><span class="topo-membrane">IICLAVLWVVKSTP</span><span class="topo-outside">A</span><span class="topo-membrane">SLALPFVLILT</span><span class="topo-inside">VPLRRVLLPLIFRNVELQCLD</span><span class="topo-unknown">ADDAKATFDEEEGRDEYDEVAMPV</span></span>
<details class="topo-details"><summary>Topology coordinates (37 regions)</summary>
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
      <td>380</td>
      <td>1</td>
      <td>380</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>381</td>
      <td>400</td>
      <td>381</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>401</td>
      <td>420</td>
      <td>401</td>
      <td>420</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>440</td>
      <td>421</td>
      <td>440</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>455</td>
      <td>441</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>457</td>
      <td>456</td>
      <td>457</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>472</td>
      <td>458</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>490</td>
      <td>473</td>
      <td>490</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>491</td>
      <td>505</td>
      <td>491</td>
      <td>505</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>506</td>
      <td>523</td>
      <td>506</td>
      <td>523</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>524</td>
      <td>540</td>
      <td>524</td>
      <td>540</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>541</td>
      <td>553</td>
      <td>541</td>
      <td>553</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>554</td>
      <td>566</td>
      <td>554</td>
      <td>566</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>567</td>
      <td>575</td>
      <td>567</td>
      <td>575</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>576</td>
      <td>591</td>
      <td>576</td>
      <td>591</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>592</td>
      <td>604</td>
      <td>592</td>
      <td>604</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>605</td>
      <td>620</td>
      <td>605</td>
      <td>620</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>621</td>
      <td>640</td>
      <td>621</td>
      <td>640</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>641</td>
      <td>648</td>
      <td>641</td>
      <td>648</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>649</td>
      <td>664</td>
      <td>649</td>
      <td>664</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>665</td>
      <td>686</td>
      <td>665</td>
      <td>686</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>687</td>
      <td>704</td>
      <td>687</td>
      <td>704</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>705</td>
      <td>719</td>
      <td>705</td>
      <td>719</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>720</td>
      <td>721</td>
      <td>720</td>
      <td>721</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>722</td>
      <td>738</td>
      <td>722</td>
      <td>738</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>739</td>
      <td>741</td>
      <td>739</td>
      <td>741</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>742</td>
      <td>752</td>
      <td>742</td>
      <td>752</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>753</td>
      <td>759</td>
      <td>753</td>
      <td>759</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>760</td>
      <td>773</td>
      <td>760</td>
      <td>773</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>774</td>
      <td>786</td>
      <td>774</td>
      <td>786</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>787</td>
      <td>801</td>
      <td>787</td>
      <td>801</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>802</td>
      <td>840</td>
      <td>802</td>
      <td>840</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>841</td>
      <td>854</td>
      <td>841</td>
      <td>854</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>855</td>
      <td>855</td>
      <td>855</td>
      <td>855</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>856</td>
      <td>866</td>
      <td>856</td>
      <td>866</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>867</td>
      <td>887</td>
      <td>867</td>
      <td>887</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>888</td>
      <td>911</td>
      <td>888</td>
      <td>911</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4yzf">4YZF</a> — Chain B (14 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEELQDDYEDMMEENLEQEEYEDPDIPESQMEEPAAHDTEATATDYHTTSHPGTHKVYVELQELVMDEKNQELRWMEAARWVQLEENLGENGAWGRPHLSHLTFWSLLELRRVFTKGTVL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-unknown">LDLQETSLAGVANQLLDRFIFEDQIRPQDREELLRALLLKHSHAGELEALGGVKPAVLTRSGDPSQPLLPQHSSLETQLFCEQGDGGTEGHSPSGILEKIPPDSEATLVLVGRADFLEQP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">VLGFVRLQEAAELEAVELPVPIRFLFVLLGPEAPHIDYTQLGRAAATLMSERVFRIDAYMAQSRGELLHSLEGFLDCSLVLPPTDAPSEQALLSLVPVQRELLRRRYQSSPAKPDSSFYK</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-unknown">GLDLNGGPDDPLQQTGQLFG</span><span class="topo-inside">GLVRDIRRRYPYYLSDITDAFSP</span><span class="topo-membrane">QVLAAVIFIYFAALSPA</span><span class="topo-outside">ITFGGLLGEKTRNQMGVSEL</span><span class="topo-membrane">LISTAVQGILFALLG</span><span class="topo-inside">AQ</span><span class="topo-membrane">PLLVVGFSGPLLVFE</span><span class="topo-outside">EAFFSFCE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">TNGLEYIVGR</span><span class="topo-membrane">VWIGFWLILLVVLVV</span><span class="topo-inside">AFEGSFLVRFISRYTQEI</span><span class="topo-membrane">FSFLISLIFIYETFSKL</span><span class="topo-outside">IKIFQDHPLQKTY</span><span class="topo-unknown">NYNVLMVPKPQGP</span><span class="topo-outside">LPNTALLSL</span><span class="topo-membrane">VLMAGTFFFAMMLRKF</span><span class="topo-inside">KNSSYFPGK</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">LRRV</span><span class="topo-membrane">IGDFGVPISILIMVLV</span><span class="topo-outside">DFFIQDTYTQKLSVPDGFKV</span><span class="topo-unknown">SNSSARGW</span><span class="topo-outside">VIHPLGLRSEFPIWMM</span><span class="topo-membrane">FASALPALLVFILIFLESQITT</span><span class="topo-inside">LIVSKPERKMVKGSGFHL</span><span class="topo-membrane">DLLLVVGMGGVAALF</span><span class="topo-outside">G</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">M</span><span class="topo-membrane">PWLSATTVRSVTHANAL</span><span class="topo-inside">TVM</span><span class="topo-unknown">GKASTPGAAAQ</span><span class="topo-inside">IQEVKEQ</span><span class="topo-membrane">RISGLLVAVLVGLS</span><span class="topo-outside">ILMEPILSRIPL</span><span class="topo-membrane">AVLFGIFLYMGVTSL</span><span class="topo-inside">SGIQLFDRILLLFKPPKYHPDVPYVKRVKTWRMHLFTGIQ</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910 </span>
<span class="topo-line"><span class="topo-membrane">IICLAVLWVVKSTP</span><span class="topo-outside">A</span><span class="topo-membrane">SLALPFVLILT</span><span class="topo-inside">VPLRRVLLPLIFRNVELQCLD</span><span class="topo-unknown">ADDAKATFDEEEGRDEYDEVAMPV</span></span>
<details class="topo-details"><summary>Topology coordinates (37 regions)</summary>
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
      <td>380</td>
      <td>1</td>
      <td>380</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>381</td>
      <td>403</td>
      <td>381</td>
      <td>403</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>404</td>
      <td>420</td>
      <td>404</td>
      <td>420</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>421</td>
      <td>440</td>
      <td>421</td>
      <td>440</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>455</td>
      <td>441</td>
      <td>455</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>456</td>
      <td>457</td>
      <td>456</td>
      <td>457</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>472</td>
      <td>458</td>
      <td>472</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>473</td>
      <td>490</td>
      <td>473</td>
      <td>490</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>491</td>
      <td>505</td>
      <td>491</td>
      <td>505</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>506</td>
      <td>523</td>
      <td>506</td>
      <td>523</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>524</td>
      <td>540</td>
      <td>524</td>
      <td>540</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>541</td>
      <td>553</td>
      <td>541</td>
      <td>553</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>554</td>
      <td>566</td>
      <td>554</td>
      <td>566</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>567</td>
      <td>575</td>
      <td>567</td>
      <td>575</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>576</td>
      <td>591</td>
      <td>576</td>
      <td>591</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>592</td>
      <td>604</td>
      <td>592</td>
      <td>604</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>605</td>
      <td>620</td>
      <td>605</td>
      <td>620</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>621</td>
      <td>640</td>
      <td>621</td>
      <td>640</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>641</td>
      <td>648</td>
      <td>641</td>
      <td>648</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>649</td>
      <td>664</td>
      <td>649</td>
      <td>664</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>665</td>
      <td>686</td>
      <td>665</td>
      <td>686</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>687</td>
      <td>704</td>
      <td>687</td>
      <td>704</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>705</td>
      <td>719</td>
      <td>705</td>
      <td>719</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>720</td>
      <td>721</td>
      <td>720</td>
      <td>721</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>722</td>
      <td>738</td>
      <td>722</td>
      <td>738</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>739</td>
      <td>741</td>
      <td>739</td>
      <td>741</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>742</td>
      <td>752</td>
      <td>742</td>
      <td>752</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>753</td>
      <td>759</td>
      <td>753</td>
      <td>759</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>760</td>
      <td>773</td>
      <td>760</td>
      <td>773</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>774</td>
      <td>785</td>
      <td>774</td>
      <td>785</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>786</td>
      <td>800</td>
      <td>786</td>
      <td>800</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>801</td>
      <td>840</td>
      <td>801</td>
      <td>840</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>841</td>
      <td>854</td>
      <td>841</td>
      <td>854</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>855</td>
      <td>855</td>
      <td>855</td>
      <td>855</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>856</td>
      <td>866</td>
      <td>856</td>
      <td>866</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>867</td>
      <td>887</td>
      <td>867</td>
      <td>887</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>888</td>
      <td>911</td>
      <td>888</td>
      <td>911</td>
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

### Inverted Repeat Architecture and Structural Homology to UraA

AE1_CTD comprises 14 transmembrane segments built from two inverted repeats of seven TMs (TMs 1-7 and TMs 8-14). The repeat is difficult to superpose as a unit but can be treated as a two-component module: TMs 1-4 superpose on TMs 8-11 (RMSD 2.1 Å for 62/103 Cα atoms) and TMs 5-7 onto TMs 12-14 (RMSD 2.1 Å for 53/100 Cα atoms). Despite only 12% sequence identity, AE1_CTD shares the same overall fold as the [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) transporter [Uracil:Proton Symporter UraA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/uraA/), with core domain RMSD of 1.8 Å for 145/268 Cα atoms.

### Core-Gate Domain Architecture

The inverted repeat units intertwine to form two structural domains: the core (TMs 1-4 and 8-11) and the gate (TMs 5-7 and 12-14), following the convention of [Uracil:Proton Symporter UraA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/uraA/). Within the core domain, the N-termini of two half-helices (TMs 3 and 10) face each other at ~10 Å, creating the appearance of a continuous helix. The gate domains are directly involved in substrate binding, and structural variation between AE1 and [Uracil:Proton Symporter UraA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/uraA/) gate domains reflects their different substrates.

### Outward-Facing Conformation and Alternating Access Mechanism

The AE1_CTD structure is in an outward-facing open conformation. Comparison with the inward-facing [Uracil:Proton Symporter UraA from Escherichia coli](/xray-mp-wiki/proteins/slc-transporters/uraA/) structure suggests a transport mechanism where the core domain rotates against the gate domain to alternate between outward- and inward-facing states. This movement is similar to that observed in [LEUT](/xray-mp-wiki/proteins/enzymes/leut/) family transporters. Starting from the outward-facing open conformation, chloride at high plasma concentration binds to the anion-binding site, causing local conformational changes that enable the core domain to rotate relative to the gate domain to form the inward-facing structure. Chloride then diffuses out and is replaced by bicarbonate to reverse the process.

### Disease-Associated Mutations

Specific mutations in AE1_CTD are related to red cell diseases including spherocytosis, stomatocytosis, and Southeast Asian ovalocytosis (SAO). Mutations causing spherocytosis often lead to misfolding, while others exhibit abnormal transport kinetics. A cation leak phenotype caused by AE1 mutations is observed in dominantly inherited hemolytic anemia. Key mutations include Arg730Cys (putative bicarbonate-binding residue), Ser731Pro, His734Arg on half-helix TM10, and deletion of residues 400-408 (SAO) at the TM1 N terminus.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating Access Mechanism</a> — AE1 structure in outward-facing conformation provides a structural basis for the alternating access mechanism of anion exchange
- <a href="/xray-mp-wiki/proteins/enzymes/leut/">LEUT</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/slc-transporters/uraA/">Uracil:Proton Symporter UraA from Escherichia coli</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/h2dids/">H2DIDS (4,4-Diisothiocyanatodihydro-stilbene-2,2-disulfonic acid)</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/trypsin/">Trypsin</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/ligands/uracil/">URACIL</a> — Related ligand or cofactor
