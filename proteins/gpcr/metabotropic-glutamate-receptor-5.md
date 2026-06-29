---
title: "Metabotropic Glutamate Receptor 5 (mGlu5)"
created: 2026-05-29
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature13396, doi/10.1021##acs.jmedchem.7b01722]
verified: false
---

# Metabotropic Glutamate Receptor 5 (mGlu5)

## Overview

Metabotropic glutamate receptor 5 (mGlu5) is a Class C G protein-coupled receptor that plays a key role in regulating NMDA receptor activity in the central nervous system. mGlu5 couples via the Gq/11 family of G proteins and is implicated in numerous neurological disorders including fragile X syndrome, Parkinson's disease, anxiety, and chronic pain. The transmembrane domain (TMD) of mGlu5 contains a well-characterized allosteric binding site (the [MPEP](/xray-mp-wiki/reagents/ligands/mpep/) site) where negative allosteric modulators (NAMs) bind in a deep pocket within the transmembrane helix bundle. Multiple high-resolution crystal structures have been determined using a thermostabilized StaR construct fused with [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) in intracellular loop 2. The first TMD structure (PDB 4OO9) established the architecture of class C GPCR transmembrane domains and revealed the conserved ionic lock network.


## Publications

### doi/10.1038##nature13396

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4oo9">4OO9</a></td>
      <td>2.6 A</td>
      <td>C 1 2 1</td>
      <td>mGlu5-StaR TMD (residues 569-836) with N-terminal GP64 signal sequence, C-terminal decahistidine tag, <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> inserted into ICL2 between Lys678 and Lys679, ECD and C-terminus <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>, six thermostabilizing mutations (E579A, N667Y, I669A, G675M, T742A, S753A). Complexed with <a href="/xray-mp-wiki/reagents/ligands/mavoglurant/">AFQ056</a>.
</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/mavoglurant/">AFQ056</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf21 insect cells (baculovirus expression vector system)
- **Construct**: mGlu5-StaR TMD construct with N-terminal GP64 signal sequence, residues 569-836 of mGlu5 receptor (TMD only), C-terminal decahistidine tag. The StaR variant contains six thermostabilizing mutations (E579A, N667Y, I669A, G675M, T742A, S753A) located away from the allosteric ligand binding site. The N-terminal extracellular domain (residues 2-568) and unstructured C-terminus (residues 837-1153) were excised. [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) was inserted into intracellular loop 2 between Lys678 and Lys679.


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
      <td>Cell culture and infection</td>
      <td>Sf21 cells infected with baculovirus at multiplicity of infection ~1, harvested 48 hours post-infection</td>
      <td>--</td>
      <td>-- + --</td>
      <td>Cells grown at 27 degrees Celsius in ESF921 medium supplemented with 10% FBS and 1% penicillin/streptomycin</td>
    </tr>
    <tr>
      <td>Cell disruption and membrane preparation</td>
      <td>Cells resuspended in PBS with protease inhibitors and <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, disrupted by microfluidizer at 14 kPSI, membranes isolated by ultracentrifugation at 204700g for 1 hour</td>
      <td>--</td>
      <td>PBS, protease inhibitor cocktail, 5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>; wash buffer: PBS, 500 mM NaCl, protease inhibitor cocktail + --</td>
      <td>Washed membranes resuspended in 40 mM HEPES pH 7.5, 250 mM NaCl and stored at -80 degrees Celsius</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membranes supplemented with 40 uM <a href="/xray-mp-wiki/reagents/ligands/mavoglurant/">AFQ056</a> and 8 mM <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a>, incubated on roller, then solubilized with <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> for 1 hour at 4 degrees Celsius</td>
      <td>--</td>
      <td>40 mM HEPES pH 7.5, 250 mM NaCl + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Insoluble material removed by ultracentrifugation</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Batch binding to <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) beads, wash with <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, elution with histidine</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) beads</td>
      <td>40 mM HEPES pH 7.5, 250 mM NaCl, 0.025% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> (binding); 40 mM HEPES pH 7.5, 250 mM NaCl, 0.025% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 100 mM histidine (elution) + 0.025% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/mavoglurant/">AFQ056</a> included in all buffers to maintain receptor-ligand complex</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/)) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>mGlu5-StaR-<a href="/xray-mp-wiki/reagents/ligands/mavoglurant/">AFQ056</a> complex mixed with <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> supplemented with 10% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a> using twin-syringe method
</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> with 10% <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a></td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>40:60 (w/w)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20.0 degrees Celsius</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals harvested and flash-frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Diffraction data from 5 crystals grown in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">[LCP</a>](/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/), collected at Diamond Light Source beamline I24. Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> and an ensemble of 8 GPCR TMD structures as search models. Rwork/Rfree = 23.9/27.4%.
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4oo9">4OO9</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">AA</span><span class="topo-outside">SPVQYLRWGDP</span><span class="topo-membrane">APIAAVVFACLGLLATLFVTVVFII</span><span class="topo-inside">YRDTPVVKSSSR</span><span class="topo-membrane">ELCYIILAGI</span></span>
<span class="topo-line"><span class="topo-membrane">CLGYLCTFCLIA</span><span class="topo-outside">KPKQI</span><span class="topo-membrane">YCYLQRIGIGLSPAMSYSALVTKTY</span><span class="topo-inside">RAARILAMSKKNIFEMLR</span></span>
<span class="topo-line"><span class="topo-inside">IDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFN</span></span>
<span class="topo-line"><span class="topo-inside">QDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDE</span></span>
<span class="topo-line"><span class="topo-inside">AAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYK</span><span class="topo-unknown">ICTKKPRFM</span><span class="topo-inside">SAC</span><span class="topo-membrane">AQLVIAFILICIQL</span></span>
<span class="topo-line"><span class="topo-membrane">GIIVALFIME</span><span class="topo-outside">PPDIM</span><span class="topo-unknown">HDYPSIRE</span><span class="topo-outside">VYLICNT</span><span class="topo-membrane">TNLGVVAPLGYNGLLILACTFYAF</span><span class="topo-inside">KTRNVP</span></span>
<span class="topo-line"><span class="topo-inside">ANFNEA</span><span class="topo-membrane">KYIAFTMYTTCIIWLAFVPIYFGS</span><span class="topo-outside">NYK</span><span class="topo-membrane">IITMCFSVSLSATVALGCMFVPKVY</span><span class="topo-inside">II</span></span>
<span class="topo-line"><span class="topo-inside">LAKPERN</span><span class="topo-unknown">VRSAAAAHHHHHHHHHH</span></span>
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
      <td>2</td>
      <td>566</td>
      <td>567</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>13</td>
      <td>568</td>
      <td>578</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>38</td>
      <td>579</td>
      <td>603</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>50</td>
      <td>604</td>
      <td>615</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>72</td>
      <td>616</td>
      <td>637</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>77</td>
      <td>638</td>
      <td>642</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>102</td>
      <td>643</td>
      <td>667</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>113</td>
      <td>668</td>
      <td>678</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>274</td>
      <td>1002</td>
      <td>1162</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>283</td>
      <td>681</td>
      <td>688</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>284</td>
      <td>286</td>
      <td>689</td>
      <td>691</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>310</td>
      <td>692</td>
      <td>715</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>315</td>
      <td>716</td>
      <td>720</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>323</td>
      <td>721</td>
      <td>728</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>324</td>
      <td>330</td>
      <td>729</td>
      <td>735</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>354</td>
      <td>736</td>
      <td>759</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>355</td>
      <td>366</td>
      <td>760</td>
      <td>771</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>390</td>
      <td>772</td>
      <td>795</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>391</td>
      <td>393</td>
      <td>796</td>
      <td>798</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>418</td>
      <td>799</td>
      <td>823</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>419</td>
      <td>427</td>
      <td>824</td>
      <td>832</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>444</td>
      <td>833</td>
      <td>849</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1021##acs.jmedchem.7b01722

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ffi">6FFI</a></td>
      <td>2.2 A</td>
      <td>C 1 2 1</td>
      <td>mGlu5-StaR TMD (residues 569-832) with N-terminal GP64 signal sequence, C-terminal decahistidine tag, <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> inserted into ICL2 between Lys678 and Lys679, ECD and C-terminus <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>, six thermostabilizing mutations. Complexed with <a href="/xray-mp-wiki/reagents/ligands/m-mpep/">M-MPEP</a>.
</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/m-mpep/">M-MPEP</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6ffh">6FFH</a></td>
      <td>2.65 A</td>
      <td>C 1 2 1</td>
      <td>mGlu5-StaR TMD (residues 569-832) with N-terminal GP64 signal sequence, C-terminal decahistidine tag, <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> inserted into ICL2 between Lys678 and Lys679, ECD and C-terminus <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>, six thermostabilizing mutations. Complexed with <a href="/xray-mp-wiki/reagents/ligands/fenobam/">Fenobam</a>.
</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf21 insect cells (baculovirus expression vector system)
- **Construct**: mGlu5-StaR TMD construct with N-terminal GP64 signal sequence, residues 569-836 of mGlu5 receptor (TMD only), C-terminal decahistidine tag. The StaR variant contains six thermostabilizing mutations (E579A, N667Y, I669A, G675M, T742A, S753A) located away from the allosteric ligand binding site. The N-terminal extracellular domain (residues 2-568) and unstructured C-terminus (residues 837-1153) were excised. [T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) was inserted into intracellular loop 2 between Lys678 and Lys679.


<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ffi">6FFI</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">AA</span><span class="topo-outside">SPVQYLRWGDPA</span><span class="topo-membrane">PIAAVVFACLGLLATLFVTVVFII</span><span class="topo-inside">YRDTPVVKSSSR</span><span class="topo-membrane">ELCYIILAGI</span></span>
<span class="topo-line"><span class="topo-membrane">CLGYLCTFCLIA</span><span class="topo-outside">KPKQI</span><span class="topo-membrane">YCYLQRIGIGLSPAMSYSALVTKTY</span><span class="topo-inside">RAARILAMSKKNIFEMLR</span></span>
<span class="topo-line"><span class="topo-inside">IDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFN</span></span>
<span class="topo-line"><span class="topo-inside">QDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDE</span></span>
<span class="topo-line"><span class="topo-inside">AAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYKI</span><span class="topo-unknown">CTKKPRFM</span><span class="topo-inside">SACA</span><span class="topo-membrane">QLVIAFILICIQL</span></span>
<span class="topo-line"><span class="topo-membrane">GIIVALFIMEPP</span><span class="topo-outside">DIM</span><span class="topo-unknown">HDYPSIR</span><span class="topo-outside">EVYLICNT</span><span class="topo-membrane">TNLGVVAPLGYNGLLILACTFYAFK</span><span class="topo-inside">TRNVP</span></span>
<span class="topo-line"><span class="topo-inside">ANFNEA</span><span class="topo-membrane">KYIAFTMYTTCIIWLAFVPIYFGS</span><span class="topo-outside">NYK</span><span class="topo-membrane">IITMCFSVSLSATVALGCMFVPKVY</span><span class="topo-inside">II</span></span>
<span class="topo-line"><span class="topo-inside">LAKPERN</span><span class="topo-unknown">VRSAAAAHHHHHHHHHH</span></span>
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
      <td>2</td>
      <td>566</td>
      <td>567</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>14</td>
      <td>568</td>
      <td>579</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>15</td>
      <td>38</td>
      <td>580</td>
      <td>603</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>50</td>
      <td>604</td>
      <td>615</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>51</td>
      <td>72</td>
      <td>616</td>
      <td>637</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>77</td>
      <td>638</td>
      <td>642</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>102</td>
      <td>643</td>
      <td>667</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>275</td>
      <td>668</td>
      <td>840</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>283</td>
      <td>841</td>
      <td>848</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>284</td>
      <td>287</td>
      <td>849</td>
      <td>852</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>312</td>
      <td>853</td>
      <td>877</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>315</td>
      <td>878</td>
      <td>880</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>322</td>
      <td>881</td>
      <td>887</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>323</td>
      <td>330</td>
      <td>888</td>
      <td>895</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>355</td>
      <td>896</td>
      <td>920</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>356</td>
      <td>366</td>
      <td>921</td>
      <td>931</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>390</td>
      <td>932</td>
      <td>955</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>391</td>
      <td>393</td>
      <td>956</td>
      <td>958</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>418</td>
      <td>959</td>
      <td>983</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>419</td>
      <td>427</td>
      <td>984</td>
      <td>992</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>444</td>
      <td>993</td>
      <td>1009</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6ffh">6FFH</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">AA</span><span class="topo-outside">SPVQYLRWGDP</span><span class="topo-membrane">APIAAVVFACLGLLATLFVTVVFII</span><span class="topo-inside">YRDTPVVKSSS</span><span class="topo-membrane">RELCYIILAGI</span></span>
<span class="topo-line"><span class="topo-membrane">CLGYLCTFCLIA</span><span class="topo-outside">KPKQI</span><span class="topo-membrane">YCYLQRIGIGLSPAMSYSALVTKTY</span><span class="topo-inside">RAARILAMSKKNIFEMLR</span></span>
<span class="topo-line"><span class="topo-inside">IDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFN</span></span>
<span class="topo-line"><span class="topo-inside">QDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDE</span></span>
<span class="topo-line"><span class="topo-inside">AAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYKI</span><span class="topo-unknown">CTKKPRFM</span><span class="topo-inside">SAC</span><span class="topo-membrane">AQLVIAFILICIQL</span></span>
<span class="topo-line"><span class="topo-membrane">GIIVALFIMEPP</span><span class="topo-outside">DIMHDYP</span><span class="topo-unknown">SIR</span><span class="topo-outside">EVYLICNT</span><span class="topo-membrane">TNLGVVAPLGYNGLLILACTFYAFK</span><span class="topo-inside">TRNVP</span></span>
<span class="topo-line"><span class="topo-inside">ANFNEA</span><span class="topo-membrane">KYIAFTMYTTCIIWLAFVPIYFGS</span><span class="topo-outside">NYK</span><span class="topo-membrane">IITMCFSVSLSATVALGCMFVPKVY</span><span class="topo-inside">II</span></span>
<span class="topo-line"><span class="topo-inside">LAKPERN</span><span class="topo-unknown">VRSAAAAHHHHHHHHHH</span></span>
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
      <td>2</td>
      <td>566</td>
      <td>567</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>13</td>
      <td>568</td>
      <td>578</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>38</td>
      <td>579</td>
      <td>603</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>49</td>
      <td>604</td>
      <td>614</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>72</td>
      <td>615</td>
      <td>637</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>77</td>
      <td>638</td>
      <td>642</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>102</td>
      <td>643</td>
      <td>667</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>113</td>
      <td>668</td>
      <td>678</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>273</td>
      <td>1002</td>
      <td>1161</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>275</td>
      <td>1679</td>
      <td>1680</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>276</td>
      <td>283</td>
      <td>1681</td>
      <td>1688</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>284</td>
      <td>286</td>
      <td>1689</td>
      <td>1691</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>312</td>
      <td>1692</td>
      <td>1717</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>319</td>
      <td>1718</td>
      <td>1724</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>320</td>
      <td>322</td>
      <td>1725</td>
      <td>1727</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>323</td>
      <td>330</td>
      <td>1728</td>
      <td>1735</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>355</td>
      <td>1736</td>
      <td>1760</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>356</td>
      <td>366</td>
      <td>1761</td>
      <td>1771</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>367</td>
      <td>390</td>
      <td>1772</td>
      <td>1795</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>391</td>
      <td>393</td>
      <td>1796</td>
      <td>1798</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>394</td>
      <td>418</td>
      <td>1799</td>
      <td>1823</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>419</td>
      <td>427</td>
      <td>1824</td>
      <td>1832</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>428</td>
      <td>444</td>
      <td>1833</td>
      <td>1849</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Ionic lock network in class C GPCRs

The mGlu5 structure reveals a conserved ionic lock network in the
transmembrane domain that regulates receptor signaling. Lys665^3.50 in
TM3 forms a salt bridge with Glu770^6.35 in TM6 (2.7 A distance),
analogous to the Arg135^3.50-Glu247^6.30 salt bridge in rhodopsin.
Additionally, Arg668^3.53 is within hydrogen bonding distance of
Ser614 in ICL1 (3.1 A), forming a secondary lock that tethers TM6
to TM3 via ICL1. Disruption of this network through mutation of
Ser613, Glu770^6.35, or Lys665^3.50 to alanine significantly increases
constitutive activity, providing functional evidence for the role of
this network in maintaining the inactive state. The network is highly
conserved across class C GPCRs including mGlu, GABA_A, CaS, and TAS1
receptors.

### Allosteric binding site architecture

The [AFQ056](/xray-mp-wiki/reagents/ligands/mavoglurant/) binding pocket is located approximately 8 A from the
receptor surface, spanning ligand positions observed for class A and B
GPCRs. The ligand is oriented with an approximate 30 degree tilt
relative to the TM bundle axis. The 3-methylphenyl ring sits in a
pocket between Ala810^7.40 and Pro655^3.40, bordered by Ile625^2.46,
Gly628^2.49, Ser654^3.39, Ser658^3.43, and Tyr659^3.44. The alkyne
linker traverses a narrow channel between Tyr659^3.44, Ser809^7.39,
Val806^7.36, and Pro655^3.40. The saturated bicyclic ring system sits
within a mainly hydrophobic pocket defined by Val806^7.36, Met802^7.32,
Phe788^6.53, Trp785^6.50, Leu744^5.44, Ile651^3.36, Pro655^3.40, and
Asn747^5.47.

### Class C GPCR transmembrane architecture

Comparison with rhodopsin (PDB 1F88, class A) and [CRF1R](/xray-mp-wiki/proteins/gpcr/crf1r-star-t4l/) (PDB 4K5Y,
class B) reveals distinct features of class C GPCR TMD architecture.
TM5 in mGlu5 is positioned approximately 6 A further inward compared
to both rhodopsin and [CRF1R](/xray-mp-wiki/proteins/gpcr/crf1r-star-t4l/), contributing to a narrow entrance to the
allosteric cavity. TM2 in mGlu5 is straighter than class A receptors
but shifted ~2.5 A closer to the central axis due to packing of
highly conserved Tyr629^2.50 against Gly590^1.50. These structural
features provide a model for all class C G-protein-coupled receptors.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/mavoglurant/">Mavoglurant (AFQ056)</a> — First NAM co-crystal structure with mGlu5 TMD (PDB 4OO9)
- <a href="/xray-mp-wiki/reagents/ligands/m-mpep/">M-MPEP</a> — High-affinity NAM; structure 6FFI
- <a href="/xray-mp-wiki/reagents/ligands/fenobam/">Fenobam</a> — Urea-linked NAM; structure 6FFH
- <a href="/xray-mp-wiki/reagents/ligands/htl14242/">HTL14242</a> — Pyrimidine-linked NAM; structure 5GCD
- <a href="/xray-mp-wiki/reagents/ligands/mpep/">MPEP</a> — Reference NAM; defines MPEP allosteric site
- <a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4 Lysozyme (T4L)</a> — Fusion partner inserted into ICL2 for crystallization
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase Crystallization</a> — Crystallization method for all mGlu5 structures
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-inactive-conformation/">GPCR Inactive Conformation</a> — Ionic lock network maintains inactive state of mGlu5
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
