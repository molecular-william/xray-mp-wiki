---
title: "Saccharomyces cerevisiae Niemann-Pick Type C-Related Protein 1 (NCR1)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2019.08.038]
verified: regex
uniprot_id: Q12200
---

# Saccharomyces cerevisiae Niemann-Pick Type C-Related Protein 1 (NCR1)

<div class="expr-badges"><span class="expr-badge expr-s-cerevisiae">S. cerevisiae</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q12200">UniProt: Q12200</a>

<span class="expr-badge">Saccharomyces cerevisiae</span>

## Overview

NCR1 (Niemann-Pick type C-Related protein 1) from Saccharomyces cerevisiae is a member of the Resistance-Nodulation-Division (RND) superfamily and the functional yeast homolog of human [NPC1](/xray-mp-wiki/proteins/structural-adhesion/human-niemann-pick-c1/). It is a membrane protein essential for sterol homeostasis, mediating the integration of sterols into the vacuolar membrane after receiving sterols from the soluble carrier NPC2. NCR1 consists of 13 transmembrane helices, an N-terminal domain (NTD) that accepts sterols from NPC2, a Middle Luminal Domain (MLD), a C-terminal Domain (CTD), and a Sterol Sensing Domain (SSD). A key feature of NCR1 is a tunnel through the MLD/CTD core that connects the NTD to the SSD and the membrane leaflet, allowing sterols to bypass the ~60 A thick glycocalyx layer. The transmembrane domain contains a conserved proton-relay network (Asp631/Glu1068/His1072) that drives sterol transport through pincer-like movements of the MLD and CTD, analogous to the mechanism in the bacterial RND exporter [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/).


## Publications

### doi/10.1016##j.cell.2019.08.038

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6r4l">6R4L</a></td>
      <td>3.5</td>
      <td>Not specified</td>
      <td>Saccharomyces cerevisiae NCR1 residues 21-1159 with C-terminal deca-histidine tag; expressed in S. cerevisiae DSY-5</td>
      <td>Ergosterol (observed in MLD/CTD tunnel at 0.87 occupancy)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6r4m">6R4M</a></td>
      <td>2.8</td>
      <td>P6_1</td>
      <td>Saccharomyces cerevisiae NPC2 residues 24-195 with C-terminal deca-histidine tag; expressed in S. cerevisiae DSY-5; sterol-free form</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6r4n">6R4N</a></td>
      <td>2.9</td>
      <td>P6_1</td>
      <td>Saccharomyces cerevisiae NPC2 residues 24-195 with C-terminal deca-histidine tag; expressed in S. cerevisiae DSY-5; sterol-bound form</td>
      <td>Ergosterol</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Saccharomyces cerevisiae DSY-5
- **Construct**: NCR1 with C-terminal thrombin cleavage site and deca-histidine tag in p423_GAL1 vector

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
      <td>Membrane preparation and solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>500 mM NaCl, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.6% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Solubilized for 30 min at 4 C with 1.5 mg/mL <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a></td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (His-tag)</td>
      <td>HisTrap HP 5mL</td>
      <td>500 mM NaCl, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 70 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 0.017% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>On-column thrombin cleavage and Endo-H deglycosylation overnight</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>Superdex200 10/300 GL Increase</td>
      <td>200 mM NaCl, 20 mM MES pH 6.5, 0.01% DM-NG (decyl <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> neopentyl glycol)</td>
      <td>Followed by PNGase F treatment at 4 C overnight and second SEC step</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography (second)</td>
      <td>Size-exclusion chromatography</td>
      <td>Superdex200 10/300 GL Increase</td>
      <td>200 mM NaCl, 20 mM MES pH 6.5, 0.01% DM-NG</td>
      <td>Final sample concentrated to ~10 mg/mL for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified NCR1 at ~10 mg/mL in 0.01% DM-NG</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryocooled to 100 K</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>NCR1 crystal structure (6R4L); 3.5 A resolution; Rfree 30.1%; residues 21-1159 modeled; single molecule in asymmetric unit; four N-linked glycosylations; fourteen disulfide bridges</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6r4l">6R4L</a> — Chain A (13 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MNVLWIIALVGQLMRLVQGT</span><span class="topo-outside">ATCAMYGNCGKKSVFGNELPCPVPRSFEPPVLSDETSKLLVEVCGEEWKEVRYACCTKDQVVALRDNLQKAQPLISSCPACLKNFNNLFCHFTCAADQGR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FVNITKVEKSKEDKDIVAELDVFMNSSWASEFYDSCKNIKFSATNGYAMDLIGGGAKNYSQFLKFLGDAKPMLGGSPFQINYKYDLANEEKEWQEFNDEVYACDDAQYKCACSDCQESCP</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">HLKPLKDGVCKVGPLPCF</span><span class="topo-membrane">SLSVLIFYTICALFAFMWYYL</span><span class="topo-unknown">CKRKKNGAMIVDDDIVPESGSLDESETNVFESFNNE</span><span class="topo-inside">TNFFNGKLANLFTKVGQFSVENPY</span><span class="topo-membrane">KILITTVFSIFVFSFIIF</span><span class="topo-outside">QYA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">TLETDPINLWVSKNSEKFKEKEYFDDNFGPFYRTEQIFVVNETGPVLSYETLHWWFDVENFITEELQSSENIGYQDLCFRPTEDSTCVIESFTQYFQGALPNKDSWKRELQECGKFPVNC</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">LPTFQQPLKTNLLFSDDDILNAHAFVVTLLLTNHTQSANRWEERLEEYLLDLKVPEGLRISFNTEISLEKELNNNNDIS</span><span class="topo-membrane">TVAISYLMMFLYATWA</span><span class="topo-inside">LRRKDGKTRL</span><span class="topo-membrane">LLGISGLLIVLASIV</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-membrane">CAAGFLTLF</span><span class="topo-outside">GLKSTLII</span><span class="topo-membrane">AEVIPFLILAIGIDNIFL</span><span class="topo-inside">ITHEYDRNCEQKPEYSIDQKIISAIGRMSPS</span><span class="topo-membrane">ILMSLLCQTGCFLIAAF</span><span class="topo-outside">VTMPAVH</span><span class="topo-membrane">NFAIYSTVSVIFNGVLQLTAY</span><span class="topo-inside">VSILSLYEK</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">RSNYKQIT</span><span class="topo-unknown">GNEETKE</span><span class="topo-inside">SFLKTFYFKMLTQKR</span><span class="topo-membrane">LIIIIFSAWFFTSLVFL</span><span class="topo-outside">PEIQFGLDQTLAVPQDSYLVDYFKDVYSFLNVGPPVYMVVKNLDLTKRQNQQKICGKFTTCERDSLANVLEQE</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">RHRSTITEPLANWLDDYFMFLNPQNDQCCRLKKGTDEVCPPSFPSRRCETCFQQGSWNYNMSGFPEGKDFMEYLSIWINAPSDPCPLGGRAPYSTALVYNETSVSASVFRTAHHPLRSQK</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050      1060      1070      1080</span>
<span class="topo-line"><span class="topo-outside">DFIQAYSDGVRISSSFPELDMFAYSPFYIFFVQYQTLGPL</span><span class="topo-membrane">TLKLIGSAIILIFFISSVF</span><span class="topo-inside">LQNI</span><span class="topo-membrane">RSSFLLALVVTMIIVDIGALMALL</span><span class="topo-outside">GISLNAVS</span><span class="topo-membrane">LVNLIICVGLGVEFCVHIV</span><span class="topo-inside">RSFTVV</span></span>
<span class="topo-ruler">      1090      1100      1110      1120      1130      1140      1150      1160      1170      1180      1190        </span>
<span class="topo-line"><span class="topo-inside">PSETKKDANSRVLYSLNTIGES</span><span class="topo-membrane">VIKGITLTKFIGVCVLA</span><span class="topo-outside">FAQSKIFDVFY</span><span class="topo-membrane">FRMWFTLIIVAALHALLFLPAL</span><span class="topo-inside">LSLFGGE</span><span class="topo-unknown">SYRDDSIEAEDLVPRGSGGGGSGGGGSGGHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (32 regions)</summary>
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
      <td>20</td>
      <td>1</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>21</td>
      <td>258</td>
      <td>21</td>
      <td>258</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>279</td>
      <td>259</td>
      <td>279</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>280</td>
      <td>315</td>
      <td>280</td>
      <td>315</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>316</td>
      <td>339</td>
      <td>316</td>
      <td>339</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>340</td>
      <td>357</td>
      <td>340</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>559</td>
      <td>358</td>
      <td>559</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>560</td>
      <td>575</td>
      <td>560</td>
      <td>575</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>576</td>
      <td>585</td>
      <td>576</td>
      <td>585</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>586</td>
      <td>609</td>
      <td>586</td>
      <td>609</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>610</td>
      <td>617</td>
      <td>610</td>
      <td>617</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>618</td>
      <td>635</td>
      <td>618</td>
      <td>635</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>636</td>
      <td>666</td>
      <td>636</td>
      <td>666</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>667</td>
      <td>683</td>
      <td>667</td>
      <td>683</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>684</td>
      <td>690</td>
      <td>684</td>
      <td>690</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>691</td>
      <td>711</td>
      <td>691</td>
      <td>711</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>712</td>
      <td>728</td>
      <td>712</td>
      <td>728</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>729</td>
      <td>735</td>
      <td>729</td>
      <td>735</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>736</td>
      <td>750</td>
      <td>736</td>
      <td>750</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>751</td>
      <td>767</td>
      <td>751</td>
      <td>767</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>768</td>
      <td>1000</td>
      <td>768</td>
      <td>1000</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1001</td>
      <td>1019</td>
      <td>1001</td>
      <td>1019</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1020</td>
      <td>1023</td>
      <td>1020</td>
      <td>1023</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1024</td>
      <td>1047</td>
      <td>1024</td>
      <td>1047</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1048</td>
      <td>1055</td>
      <td>1048</td>
      <td>1055</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1056</td>
      <td>1074</td>
      <td>1056</td>
      <td>1074</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1075</td>
      <td>1102</td>
      <td>1075</td>
      <td>1102</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1103</td>
      <td>1119</td>
      <td>1103</td>
      <td>1119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1120</td>
      <td>1130</td>
      <td>1120</td>
      <td>1130</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1131</td>
      <td>1152</td>
      <td>1131</td>
      <td>1152</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1153</td>
      <td>1159</td>
      <td>1153</td>
      <td>1159</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1160</td>
      <td>1198</td>
      <td>1160</td>
      <td>1198</td>
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

### MLD/CTD tunnel enables sterol bypass of the glycocalyx

The NCR1 crystal structure reveals a tunnel through the pseudo two-fold symmetry point of the MLD and CTD domains, extending from the membrane leaflet and SSD shelf to the NTD loop-helix gate. An ergosterol molecule (0.87 occupancy) is observed inside this tunnel, positioned 24 A from the start of the membrane with its hydroxyl group pointing toward the NTD. The tunnel provides a pathway for sterols to bypass the ~60 A thick glycocalyx layer coating the vacuolar membrane. This tunnel-based mechanism is distinct from previous models involving NTD decoupling and direct membrane insertion. Analogous tunnels exist in hNPC1 structures and the related Patched protein family, suggesting a conserved transport mechanism within the RND superfamily.

### Proton-relay network drives sterol transport

The transmembrane domain contains a fully conserved cluster of charged residues: Asp631(M5), Glu1068(M11), and His1072(M11) at the pseudo two-fold symmetry axis. Mutagenesis of H1072A and D631N reduces sterol transfer from NPC2 to NCR1 by approximately 50%, despite being ~80 A from the NTD, demonstrating allosteric coupling from the proton-relay site to the sterol loading region. This network is analogous to the Asp407/Lys940 proton-relay pair in [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/), where proton translocation drives pincer-like movements of the coupling helices and Porter domain. The coupling loops connecting MLD/CTD to the transmembrane acidic cluster are proposed to transduce proton-driven conformational changes.

### NTD conformational flexibility enables sterol loading

The NTD of NCR1 adopts a distinct rotated conformation compared to the [Cryo-Electron Microscopy](/xray-mp-wiki/methods/structure-determination/cryo-em/) structure of hNPC1, with the sterol binding pocket rotated ~20 degrees and tilted ~40 degrees toward the MLD/CTD two-fold point. A loop-helix motif (residues 157-172) moves ~14 A toward the CTD, forming an interaction surface mediated by Ser162(NDT)-Asn865(CTD). Mutation of Asn865 (N865A) or deletion/mutation of the [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) hinge (residues 173-175) strongly reduces sterol transfer from NPC2, confirming that NTD conformational shifts are essential for sterol loading and unloading.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/rnd-efflux-pumps/">RND Efflux Pumps</a> — NCR1 belongs to the RND superfamily; the sterol transport tunnel mechanism is analogous to the AcrB Porter domain transport pathway
- <a href="/xray-mp-wiki/proteins/secretion-translocon/secyeg/">Thermus thermophilus SecYEG Translocon Complex</a> — SecDF, another RND superfamily member, uses a similar remote coupling mechanism linking transmembrane proton transport to extracytoplasmic domain movements
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Primary detergent used for membrane solubilization of NCR1
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Crystallization method used for NCR1 structure determination
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo-Electron Microscopy</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">ACRB</a> — Related protein structure
- <a href="/xray-mp-wiki/proteins/structural-adhesion/human-niemann-pick-c1/">NPC1</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
