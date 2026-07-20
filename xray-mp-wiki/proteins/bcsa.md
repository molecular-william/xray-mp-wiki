---
title: "BcsA from Rhodobacter sphaeroides (Cellulose Synthase Catalytic Subunit)"
created: 2026-06-03
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11744]
verified: agent
uniprot_id: ['Q3J125', 'Q3J126']
---

# BcsA from Rhodobacter sphaeroides (Cellulose Synthase Catalytic Subunit)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q3J125">UniProt: Q3J125</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q3J126">UniProt: Q3J126</a>

<span class="expr-badge">Rhodobacter sphaeroides</span>

## Overview

BcsA is the catalytically active subunit of the bacterial cellulose synthase complex from Rhodobacter sphaeroides. It is a membrane-embedded glycosyltransferase that uses UDP-activated glucose (UDP-Glc) as donor substrate to synthesize beta-1,4-linked cellulose polymers. BcsA contains a GT-A fold glycosyltransferase domain between transmembrane helices 4 and 5, a PilZ domain at the C-terminus that binds the bacterial secondary messenger [CYCLIC-DI-GMP](/xray-mp-wiki/reagents/ligands/cyclic-di-gmp) for activation, and eight transmembrane helices that form a narrow polysaccharide-conducting channel. The structure of the BcsA-BcsB translocation intermediate reveals how cellulose synthesis is coupled to membrane translocation, with the nascent glucan extended by one glucose molecule at a time.

## Publications

### doi/10.1038##nature11744

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4hg6">4HG6</a></td>
      <td>4.5 A</td>
      <td></td>
      <td>BcsA-<a href="/xray-mp-wiki/proteins/bcsb">BCSB</a> complex from Rhodobacter sphaeroides; BcsA residues 1-788 with C-terminal dodeca-histidine tag; BcsB residues 21-725 with N-terminal PelB signal sequence</td>
      <td>UDP, translocating glucan (18 <a href="/xray-mp-wiki/reagents/additives/glucose">GLUCOSE</a> units)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli Rosetta 2 cells
- **Construct**: BcsA with C-terminal His12 tag; [BCSB](/xray-mp-wiki/proteins/bcsb) residues 21-725 with N-terminal PelB signal sequence

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
      <td>Cell growth and membrane preparation</td>
      <td>Auto-induction culture</td>
      <td>--</td>
      <td>ZYP-5052 auto-induction medium + --</td>
      <td>Cells grown in ZYP-5052 auto-induction medium at 37 C; crude membranes collected by centrifugation at 120,000g</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM sodium phosphate pH 7.2, 0.3 M NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/cellobiose">CELLOBIOSE</a>, 5 mM MgCl2, 40 mM imidazole, 10% glycerol + 2% <a href="/xray-mp-wiki/reagents/detergents/triton-x-100">Triton X-100</a></td>
      <td>Solubilized for 60 min at 4 C; insoluble material cleared by centrifugation</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">IMAC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) agarose (Qiagen)</td>
      <td>RB2 buffer (20 mM sodium phosphate pH 7.2, 0.3 M NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/cellobiose">CELLOBIOSE</a>, 5 mM MgCl2, 40 mM imidazole, 10% glycerol) + 2% <a href="/xray-mp-wiki/reagents/detergents/triton-x-100">Triton X-100</a></td>
      <td>Batch incubation with 10 ml <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) agarose for 45 min at 4 C</td>
    </tr>
    <tr>
      <td>Column washing</td>
      <td>Gravity flow chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) agarose</td>
      <td>WB1-buffer (RB2-buffer with 60 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">IMIDAZOLE</a>) + 2% <a href="/xray-mp-wiki/reagents/detergents/triton-x-100">Triton X-100</a></td>
      <td>Washed with 75 ml WB1-buffer containing 5 mM <a href="/xray-mp-wiki/reagents/detergents/ldao">LDAO</a></td>
    </tr>
    <tr>
      <td>Elution</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) affinity elution</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) agarose</td>
      <td>RB2 buffer with 1 M NaCl and increasing <a href="/xray-mp-wiki/reagents/additives/imidazole">IMIDAZOLE</a> + 2% <a href="/xray-mp-wiki/reagents/detergents/triton-x-100">Triton X-100</a></td>
      <td>Eluted with high <a href="/xray-mp-wiki/reagents/additives/imidazole">IMIDAZOLE</a> concentration</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified BcsA-<a href="/xray-mp-wiki/proteins/bcsb">BCSB</a> complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>30% <a href="/xray-mp-wiki/reagents/additives/peg200">PEG200</a>, 0.1 M MES pH 6.5, 50 mM NaCl</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>approximately 7 days for initial crystals</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Initial crystals observed after approximately 7 days; final size about 50 x 50 x 10 micrometers</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hg6">4HG6</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTVRAKARSPLRV</span><span class="topo-membrane">VPVLLFLLWVALLVPFGLLAA</span><span class="topo-outside">APVAPSAQ</span><span class="topo-membrane">GLIALSAVVLVALLKPFA</span><span class="topo-inside">DKM</span><span class="topo-membrane">VPRFLLLSAASMLVMRYWFWRLF</span><span class="topo-outside">ETLPPPAL</span><span class="topo-membrane">DASFLFALLLFAVETFSISIFFLNGF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LSADPTDRPFPRPLQPEELPTVDILVPSYNEPADMLSVTLAAAKNMIYPARLRTVVLCDDGGTDQRCMSPDPELAQKAQERRRELQQLCRELGVVYSTRERNEHAKAGNMSAALERLKGE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">LVVVFDADHVPSRDFLARTVGYFVEDPDLFLVQTPHFFINPDPIQRNLALGDRCPPENEMFYGKIHRGLDRWGGAFFCGSAAVLRRRALDEAGGFAGETITEDAETALEIHSRGWKSLYI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">DRAMIAGLQPETFASFIQQRGRWATGMMQMLLLKNPLFRRGLGIAQRLCYLNSMSFWF</span><span class="topo-membrane">FPLVRMMFLVAPLIYLFFGIE</span><span class="topo-outside">IFVATFEEV</span><span class="topo-membrane">LAYMPGYLAVSFLVQNA</span><span class="topo-inside">LFARQRWPLVSEVYE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">VAQAPYLARAIVTTLLRPRSARFAVTAKDETLSENYISPIYRPLL</span><span class="topo-membrane">FTFLLCLSGVLATLVRWV</span><span class="topo-outside">AFPGDRSV</span><span class="topo-membrane">LLVVGGWAVLNVLLVG</span><span class="topo-inside">FALRAVAEKQQRRAAPRVQMEVPAEAQIPAFGN</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">RSLTATVLDASTSGVRLLVRLPGVGDPHPALEAGGLIQFQPKFPDAPQLERMVRGRIRSARREGGTVMVGVIFEAGQPIAVRETVAYLIFGESAHWRTMREATMRPIGLLHGMARILWMA</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800  </span>
<span class="topo-line"><span class="topo-inside">AASLPKTARDFMDEPARRRRRHEEPKEKQAHLLAFGTDF</span><span class="topo-unknown">STEPDWAGELLDPTAQVSARPNTVAWGSNHHHHHHKLHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>34</td>
      <td>14</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>42</td>
      <td>35</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>63</td>
      <td>61</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>86</td>
      <td>64</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>94</td>
      <td>87</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>120</td>
      <td>95</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>418</td>
      <td>121</td>
      <td>418</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>439</td>
      <td>419</td>
      <td>439</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>440</td>
      <td>448</td>
      <td>440</td>
      <td>448</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>465</td>
      <td>449</td>
      <td>465</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>466</td>
      <td>525</td>
      <td>466</td>
      <td>525</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>526</td>
      <td>543</td>
      <td>526</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>544</td>
      <td>551</td>
      <td>544</td>
      <td>551</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>567</td>
      <td>552</td>
      <td>567</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>568</td>
      <td>759</td>
      <td>568</td>
      <td>759</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>760</td>
      <td>802</td>
      <td>760</td>
      <td>802</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hg6">4HG6</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGQDAPMIVIEGLTSEEPQASPDAVAEAVPAAEVA</span><span class="topo-outside">PWIIPLRPLAETAQVGPLFRLQGQQARAAFRLFLPTEAVGGTLTLAQRSSIDILPESSQIIVRMNDQEIGRFTPRQFGALGAVTM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">PLGEAVRAGDNLVTIEAQHRHRIYCGADAEFDLWTEVDLSQSGVALPAAAIGTEPTSFIAALTAQAESGRPVEIRTPTPPDEATLRTLAQALGRPLPDEALPLALSKPWSAETGPTYARI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TLLPSDADRVSIRRGGDGAVVLVLEHPPEGSPNASLVADLLGATPTLPPPTLPQIPPGRVVTLADMGVDTILTDNRYFNRDIDFQLPDDWLLLASQKAQIGIDYGFAGGLPEGALLLVKV</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">NGTTVRMLPLDRDAAPVKPRLDIRFPARLLHPGPNRLSFESVIPGNPPDQPCPASAGDLMQVLSSTDLEVPPSPRMQMADMARDLAQVTPASVHPATPDGLARTLPFMAAFREVPDAAPV</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DLTVAGLHDIATVPLNEEGLTPRLLALTLLPST</span><span class="topo-unknown">VSRLVERPATPA</span><span class="topo-outside">GPPANALAPLGAAPGEGVMPPLVESNWSDRAQTFVQATLQPVIQTVRRMLRPGDGNLAEWLATRKGTAMLLAPEP</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       </span>
<span class="topo-line"><span class="topo-outside">GKLWVILGPEAEPARVAEALAMAPRSPGGPRGQVAVLGSDGRWSSWSKPGLLPELREPVSLDNVRSVVGNVASARPPLL</span><span class="topo-membrane">LGGMLGLAWISAAIAVGFV</span><span class="topo-inside">LRTR</span><span class="topo-unknown">RKGLK</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
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
      <td>35</td>
      <td>19</td>
      <td>53</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>513</td>
      <td>54</td>
      <td>531</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>514</td>
      <td>525</td>
      <td>532</td>
      <td>543</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>526</td>
      <td>679</td>
      <td>544</td>
      <td>697</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>680</td>
      <td>698</td>
      <td>698</td>
      <td>716</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>699</td>
      <td>702</td>
      <td>717</td>
      <td>720</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>703</td>
      <td>707</td>
      <td>721</td>
      <td>725</td>
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

### Architecture of the BcsA-[BCSB](/xray-mp-wiki/proteins/bcsb) translocation complex

BcsA and [BCSB](/xray-mp-wiki/proteins/bcsb) form an elongated complex with large cytosolic and periplasmic domains. The transmembrane helices of BcsA (TM1-TM8) form a narrow channel approximately 8 A wide and 33 A long. BcsB anchors to the membrane via a single C-terminal transmembrane helix and contributes two amphipathic interface helices (IF4 and IF5) at the water-lipid interface. The complex accommodates a translocating glucan chain that extends from the intracellular catalytic site to the periplasmic solvent.

### Glycosyltransferase A fold and catalytic mechanism

The GT domain of BcsA adopts a [GT-A Fold](/xray-mp-wiki/concepts/gt-a-fold) fold (GT-A) consisting of a mixed seven-stranded beta-sheet surrounded by seven alpha-helices. The conserved signature D,D,D,Q(Q/R)XRW motif contains three variably spaced aspartic acids (Asp 179, Asp 246, Asp 343) and a pentapeptide (Gln 379-Arg 380-Arg 382-Trp 383). The first two aspartic acids coordinate UDP, while the third (Asp 343) represents the catalytic base. The Q(Q/R)XRW sequence and an FFCGS pentapeptide form a binding site for the terminal disaccharide of the glucan acceptor. The structure superimposes with the inverting glycosyltransferase SpA from Bacillus subtilis with 2.15 A RMSD.

### Polysaccharide-conducting transmembrane channel

TM3-TM8 of BcsA form a narrow channel that accommodates ten [GLUCOSE](/xray-mp-wiki/reagents/additives/glucose) units of the translocating glucan. The glucan enters through the cytoplasmic opening formed by IF1-3 and the N-terminal half of TM5, crosses the membrane parallel to TM5 and TM6, and exits on the periplasmic side between BcsA's 5/6 and 7/8 loops at the BcsA-BcsB interface. All transmembrane helices of BcsA except TM1 and TM2 directly contact the glucan. The periplasmic exit is maintained by the tips of TM6 and TM8 side chains, separated by about 9 A and 15 A at the periplasmic and cytoplasmic sides respectively.

### Activation by [CYCLIC-DI-GMP](/xray-mp-wiki/reagents/ligands/cyclic-di-gmp) via PilZ domain

BcsA activity is stimulated by [CYCLIC-DI-GMP](/xray-mp-wiki/reagents/ligands/cyclic-di-gmp) through a PilZ domain localized within BcsA's C-terminus, right next to the GT domain. The C-terminus extends from TM8 via a short beta-strand forming a two-stranded beta-sheet with the IF3-TM7 loop, before folding into a six-stranded beta-barrel (amino acids 585-675). The beta-barrel points away from the GT domain at approximately 90 degrees. The PilZ domain is the cyclic-di-GMP-responsive sensor that controls cellulose synthase activity.

### Periplasmic domain architecture of [BCSB](/xray-mp-wiki/proteins/bcsb)

The periplasmic region of the cellulose synthase is primarily formed by [BCSB](/xray-mp-wiki/proteins/bcsb) and consists of two carbohydrate binding domains (CBD1 and CBD2) connected by a disulphide bond between conserved Cys 163 and Cys 430, and two flavodoxin-like domains (FD1: amino acids 192-303; FD2: amino acids 457-529 and 598-666). CBD1 contains a cluster of conserved hydrophobic residues (His 159, Arg 160, Ile 161, Leu 171, Trp 172) at its tip that likely interact with the translocating glucan. The repeating structural motif of BcsB contains a CBD linked to an FD domain.

### Model for cellulose synthesis and translocation coupling

The structure suggests a model in which the nascent glucan is extended by one [GLUCOSE](/xray-mp-wiki/reagents/additives/glucose) molecule at a time. After glycosyl transfer, the newly attached terminal glucose rotates around the acetal linkage to align with the glucan in the channel. Steric interactions dictate the rotation direction, leading to the beta-1,4 glucan characteristic 180 degree rotation between individual glucose units. The model represents a cellulose synthase-cellulose translocation intermediate captured after glycosyl transfer and before replacing UDP with UDP-Glc.


## Cross-References

- <a href="/xray-mp-wiki/reagents/substrates/udp-glucose/">UDP-Glucose (UDP-Glc)</a> — Sugar nucleotide donor substrate for [Cellulose Synthase](/xray-mp-wiki/concepts/cellulose-synthase)
- <a href="/xray-mp-wiki/reagents/ligands/cyclic-di-gmp/">Cyclic-di-GMP</a> — Bacterial secondary messenger that activates BcsA via PilZ domain
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">Lauryldimethylamine N-oxide (LDAO)</a> — Zwitterionic detergent used in BcsA-[BcsB from Rhodobacter sphaeroides (Cellulose Synthase Periplasmic Subunit)](/xray-mp-wiki/proteins/bcsb) purification wash buffer
- <a href="/xray-mp-wiki/reagents/detergents/triton-x-100/">Triton X-100</a> — Nonionic detergent used for membrane solubilization of BcsA-[BcsB from Rhodobacter sphaeroides (Cellulose Synthase Periplasmic Subunit)](/xray-mp-wiki/proteins/bcsb) complex
- <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate Buffer</a> — Buffer component in purification and solubilization buffers
- <a href="/xray-mp-wiki/reagents/buffers/mes/">2-(N-Morpholino)ethanesulfonic Acid (MES)</a> — Crystallization buffer at pH 6.5
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> — Used for [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine) derivatization for SAD phasing
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/gt-a-fold/">GT-A Fold (Glycosyltransferase A Fold)</a> — Structural domain of BcsA glycosyltransferase catalytic domain
- <a href="/xray-mp-wiki/reagents/additives/cellobiose">Cellobiose</a> — Additive used in purification or crystallization buffers
