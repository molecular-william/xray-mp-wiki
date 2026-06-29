---
title: "Human Niemann-Pick C1 (NPC1)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1711716114, doi/10.1107##s2053230x23000705]
verified: false
---

# Human Niemann-Pick C1 (NPC1)

## Overview

Human NPC1 (Niemann-Pick C1) is a large multi-domain membrane protein essential for the export of LDL-derived [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) from late endosomes. It consists of 1,278 amino acid residues, including three luminal domains [N-terminal domain (NTD), middle luminal domain (MLD), and C-terminal domain (CTD/cysteine-rich domain)] and 13 transmembrane helices. NPC1, together with the soluble NPC2 protein, mediates [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) transport across the ~8 nm glycocalyx of the endosomal lumen. Mutations in NPC1 cause Niemann-Pick type C disease, a fatal lysosomal storage disorder. NPC1 also functions as a receptor for Ebola virus in late endosomes.


## Publications

### doi/10.1073##pnas.1711716114

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5u73">5U73</a></td>
      <td>3.3 A</td>
      <td>not specified</td>
      <td>NPC1* (residues 314-1,278), including TM2-13, MLD, and CTD</td>
      <td>none detected (itraconazole used during purification but not observed in density)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293 cells (mammalian expression, as previously published)
- **Construct**: NPC1* (residues 314-1,278)

**Purification:**

- **Expression system**: HEK293 cells
- **Expression construct**: NPC1* (residues 314-1,278)

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
      <td>Cell disruption</td>
      <td>Sonication</td>
      <td>--</td>
      <td>20 mM Hepes pH 7.0, 150 mM NaCl, 1 mM PMSF, 5 ug/mL leupeptin and aprotinin + --</td>
      <td>Cells resuspended in buffer A</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>--</td>
      <td>20 mM Hepes pH 7.0, 150 mM NaCl, 100 uM itraconazole + 1% (w/v) n-Dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Incubated 2 h at 4 C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA</td>
      <td>Ni-NTA affinity column (Qiagen)</td>
      <td>20 mM Hepes pH 7.0, 150 mM NaCl, 50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Washed twice with 50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography</td>
      <td>Superose 6 or similar</td>
      <td>20 mM Hepes pH 7.0, 150 mM NaCl + 0.02% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>All buffers supplemented with 10 uM itraconazole</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>NPC1* at 10 mg/mL, incubated with 100 uM itraconazole on ice for 1 h</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew in 3 d. Data collected at NECAT beamlines (APS), processed with XDS. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using previous NPC1* structure (5I31) as search model. Refined with PHENIX to Rfree 30.5% and Rwork 25.3%.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5u73">5U73</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MTARGLALGLLLLLLCPAQVFSQSCVWYGECGIAYGDKRYNCEYSGPPKPLPKDGYDLVQ</span></span>
<span class="topo-line"><span class="topo-unknown">ELCPGFFFGNVSLCCDVRQLQTLKDNLQLPLQFLSRCPSCFYNLLNLFCELTCSPRQSQF</span></span>
<span class="topo-line"><span class="topo-unknown">LNVTATEDYVDPVTNQTKTNVKELQYYVGQSFANAMYNACRDVEAPSSNDKALGLLCGKD</span></span>
<span class="topo-line"><span class="topo-unknown">ADACNATNWIEYMFNKDNGQAPFTITPVFSDFPVHGMEPMNNATKGCDESVDEVTAPCSC</span></span>
<span class="topo-line"><span class="topo-unknown">QDCSIVCGPKPQPPPPPAPWTILGLDAMYVIMWITYMAFLLVFFGAFFAVWCYRKRYFVS</span></span>
<span class="topo-line"><span class="topo-unknown">EYTPIDSNIAFSVNASDKGEASCCDPVSAAFEG</span><span class="topo-inside">CLRRLFTRWGSFCVRNPGCVI</span><span class="topo-membrane">FFSLVF</span></span>
<span class="topo-line"><span class="topo-membrane">ITACSSGLVF</span><span class="topo-outside">VRVTTNPVDLWSAPSSQARLEKEYFDQHFGPFFRTEQLIIRAPLTDKHIY</span></span>
<span class="topo-line"><span class="topo-outside">QPYPSGADVPFGPPLDIQILHQVLDLQIAIENITASYDNETVTLQDICLAPLSPYNTNCT</span></span>
<span class="topo-line"><span class="topo-outside">ILSVLNYFQNSHSVLDHKKGDDFFVYADYHTHFLYCVRAPASLNDTSLLHDPCLGTFGGP</span></span>
<span class="topo-line"><span class="topo-outside">VFPWLVLGGYDDQNYNNATALVITFPVNNYYNDTEKLQRAQAWEKEFINFVKNYKNPNLT</span></span>
<span class="topo-line"><span class="topo-outside">ISFTAERSIEDELNRESDSDV</span><span class="topo-membrane">FTVVISYAIMFLYISLA</span><span class="topo-inside">LG</span><span class="topo-unknown">HIKSCRRLL</span><span class="topo-inside">VDSKV</span><span class="topo-membrane">SLGIAG</span></span>
<span class="topo-line"><span class="topo-membrane">ILIVLSSVACSLGVFSYI</span><span class="topo-outside">GLPLTLIV</span><span class="topo-membrane">IEVIPFLVLAVGVDNIF</span><span class="topo-inside">ILVQAYQRDERLQGETL</span></span>
<span class="topo-line"><span class="topo-inside">DQQLGRVLGEVAPSM</span><span class="topo-membrane">FLSSFSETVAFFLGAL</span><span class="topo-outside">SVMPAV</span><span class="topo-membrane">HTFSLFAGLAVFIDFLLQITCF</span><span class="topo-inside">V</span></span>
<span class="topo-line"><span class="topo-inside">SLLGLDIKRQEKNRLDIFC</span><span class="topo-unknown">CVRGAEDGTSVQAS</span><span class="topo-inside">ESCLFRFFKNSYSPLLLKDWMRP</span><span class="topo-membrane">IVIA</span></span>
<span class="topo-line"><span class="topo-membrane">IFVGVLSFSIAVL</span><span class="topo-outside">NKVDIGLDQSLSMPDDSYMVDYFKSISQYLHAGPPVYFVLEEGHDYT</span></span>
<span class="topo-line"><span class="topo-outside">SSKGQNMVCGGMGCNNDSLVQQIFNAAQLDNYTRIGFAPSSWIDDYFDWVKPQSSCCRVD</span></span>
<span class="topo-line"><span class="topo-outside">NITDQFCNASVVDPACVRCRPLTPEGKQRPQGGDFMRFLPMFLSDNPNPKCGKGGHAAYS</span></span>
<span class="topo-line"><span class="topo-outside">SAVNILLGHGTRVGATYFMTYHTVLQTSADFIDALKKARLIASNVTETMGINGSAYRVFP</span></span>
<span class="topo-line"><span class="topo-outside">YSVFYVFYEQYLTIIDDT</span><span class="topo-membrane">IFNLGVSLGAIFLVTMVL</span><span class="topo-inside">LGC</span><span class="topo-membrane">ELWSAVIMCATIAMVLVNMFG</span></span>
<span class="topo-line"><span class="topo-membrane">VMWLW</span><span class="topo-outside">GISLNAVS</span><span class="topo-membrane">LVNLVMSCGISVEFCSHIT</span><span class="topo-inside">RAFTVSMKGSRVERAEEALAHMGSSV</span><span class="topo-membrane">FS</span></span>
<span class="topo-line"><span class="topo-membrane">GITLTKFGGIVVLAFA</span><span class="topo-outside">KSQIFQIF</span><span class="topo-membrane">YFRMYLAMVLLGATHGLIFL</span><span class="topo-inside">PVLLSYIGPS</span><span class="topo-unknown">VNKAKS</span></span>
<span class="topo-line"><span class="topo-unknown">CATEERYKGTERERLLNF</span></span>
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
      <td>333</td>
      <td>1</td>
      <td>333</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>334</td>
      <td>354</td>
      <td>334</td>
      <td>354</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>355</td>
      <td>370</td>
      <td>355</td>
      <td>370</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>371</td>
      <td>621</td>
      <td>371</td>
      <td>621</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>622</td>
      <td>638</td>
      <td>622</td>
      <td>638</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>639</td>
      <td>640</td>
      <td>639</td>
      <td>640</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>641</td>
      <td>649</td>
      <td>641</td>
      <td>649</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>650</td>
      <td>654</td>
      <td>650</td>
      <td>654</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>655</td>
      <td>678</td>
      <td>655</td>
      <td>678</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>679</td>
      <td>686</td>
      <td>679</td>
      <td>686</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>687</td>
      <td>703</td>
      <td>687</td>
      <td>703</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>704</td>
      <td>735</td>
      <td>704</td>
      <td>735</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>736</td>
      <td>751</td>
      <td>736</td>
      <td>751</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>752</td>
      <td>757</td>
      <td>752</td>
      <td>757</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>758</td>
      <td>779</td>
      <td>758</td>
      <td>779</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>780</td>
      <td>799</td>
      <td>780</td>
      <td>799</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>800</td>
      <td>813</td>
      <td>800</td>
      <td>813</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>814</td>
      <td>836</td>
      <td>814</td>
      <td>836</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>837</td>
      <td>853</td>
      <td>837</td>
      <td>853</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>854</td>
      <td>1098</td>
      <td>854</td>
      <td>1098</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1099</td>
      <td>1116</td>
      <td>1099</td>
      <td>1116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1117</td>
      <td>1119</td>
      <td>1117</td>
      <td>1119</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1120</td>
      <td>1145</td>
      <td>1120</td>
      <td>1145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1146</td>
      <td>1153</td>
      <td>1146</td>
      <td>1153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1154</td>
      <td>1172</td>
      <td>1154</td>
      <td>1172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1173</td>
      <td>1198</td>
      <td>1173</td>
      <td>1198</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1199</td>
      <td>1216</td>
      <td>1199</td>
      <td>1216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1217</td>
      <td>1224</td>
      <td>1217</td>
      <td>1224</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1225</td>
      <td>1244</td>
      <td>1225</td>
      <td>1244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1245</td>
      <td>1254</td>
      <td>1245</td>
      <td>1254</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1255</td>
      <td>1278</td>
      <td>1255</td>
      <td>1278</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1107##s2053230x23000705

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8eus">8EUS</a></td>
      <td>2.3 A</td>
      <td>P2_1</td>
      <td>Human NPC1-C (residues 371-621) with C-terminal His8 tag, nonglycosylated, expressed in E. coli</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293 cells (mammalian expression, as previously published)
- **Construct**: NPC1* (residues 314-1,278)


## Biological / Functional Insights

### Complete CTD structure revealed

At 3.3 A resolution, the entire C-terminal luminal domain (CTD,
residues 861-1,083) is fully resolved with unambiguous sequence
assignment. The CTD consists of three beta strands surrounded by
five alpha-helices. All eight cysteines form four disulfide bonds,
stabilizing the loop structures on the tip of this domain. This
contrasts with the MLD, which only contains two disulfide bonds
despite sharing a similar fold.

### Omega loop and CTD-NTD interaction

A disulfide bond between Cys909 and Cys914 creates a unique loop
(residues 909-917, termed the Omega loop) that breaks one long
alpha-helix into two shorter helices (alpha2a and alpha2b). The
Omega loop interacts with a Psi loop (residues 230-234) on the NTD,
forming a CTD-NTD interface. Mutagenesis showed that deleting the
Omega loop (NPC1-Delta-Omega-A) completely blocks [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/)
transport, while deleting the Psi loop (NPC1-Delta-Psi) results in
50% loss of activity, confirming the physiological importance of
this interaction.

### Mapping of disease-causing mutations

The improved resolution allows precise mapping of all NPC
disease-causing mutations across the NPC1 structure. The most
frequent mutation, I1061T (15-20% of disease alleles), is located
in the alpha5 helix of the CTD. Analysis suggests that I1061T
would not disrupt the alpha5-alpha2b interaction, explaining why
overexpression of NPC1-I1061T can still partially rescue the
NPC1-deficient phenotype. The P691S mutation (which abolishes
ligand binding to the SSD) is located in TM5, facing the SSD
ligand-binding pocket.

### Hydrophobic hand-off cholesterol transfer model

The structural data support a "hydrophobic hand-off" model for
[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) transfer. [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) binds NPC2 in the endosomal
lumen, inducing conformational changes that facilitate NPC2-MLD
interaction. The Omega loop-Psi loop interaction keeps the NTD in
the proper orientation to receive [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) from NPC2. After
[Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) transfer from NPC2 to NPC1-NTD, the Omega loop-Psi
loop interaction may weaken to allow the NTD to reach across the
glycocalyx and deliver [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) to the SSD pocket in the
membrane. Two possible mechanisms are proposed: (1) intramolecular
transfer where TM1 movement docks NTD to SSD, or (2) intermolecular
transfer where NTD from one NPC1 docks to an SSD of a neighboring
molecule.


## Cross-References

- <a href="/xray-mp-wiki/proteins/structural-adhesion/ncr1/">Saccharomyces cerevisiae Niemann-Pick Type C-Related Protein 1 (NCR1)</a> — Yeast homolog of human NPC1
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltoside (DDM)</a> — Used for NPC1 solubilization and purification
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (HEPES-KOH Buffer)</a> — Used in all purification and crystallization buffers
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> — Additive used in purification or crystallization buffers
