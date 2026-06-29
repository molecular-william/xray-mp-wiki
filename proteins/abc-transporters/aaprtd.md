---
title: "Aquifex aeolicus PrtD (AaPrtD) Type-1 Secretion System ABC Transporter"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2017.01.010]
verified: false
---

# Aquifex aeolicus PrtD (AaPrtD) Type-1 Secretion System ABC Transporter

## Overview

[AaPrtD](/xray-mp-wiki/proteins/aaprtd/) is the ABC transporter component of the Type-1 secretion system (T1SS) from the hyperthermophilic bacterium Aquifex aeolicus. T1SSs are widespread among Gram-negative bacteria and are responsible for the secretion of virulence factors including proteases, lipases, and scavenging molecules. The crystal structure at 3.15 A resolution reveals a homodimeric ABC exporter fold with each subunit containing six N-terminal transmembrane helices and a C-terminal nucleotide-binding domain (NBD). The structure is in an [ADP](/xray-mp-wiki/reagents/ligands/adp/)-bound occluded conformation. Distinctive features include highly kinked TM3 and TM6 helices that create a narrow interior channel and a highly basic concave surface formed by TM1, TM3, and TM6, which is likely involved in substrate recruitment. The structure supports a polypeptide transport mechanism distinct from alternating access.

## Publications

### doi/10.1016##j.str.2017.01.010

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5l22">5L22</a></td>
      <td>3.15 A</td>
      <td>C1 2 1</td>
      <td>Full-length AaPrtD from Aquifex aeolicus, residues 11-315 and 326-559, C-terminally His-tagged, <a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a>-bound, occluded conformation</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Full-length AaPrtD from Aquifex aeolicus with C-terminal [His-tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/)

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
      <td>Affinity purification</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta">Ni-NTA</a></td>
      <td>Not specified + dodecyl-beta-D-maltoside (<a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a>)</td>
      <td>AaPrtD expressed in E. coli and purified in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> via metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">affinity chromatography</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Gel-filtration chromatography</a></td>
      <td>Not specified</td>
      <td>Not specified + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Final polishing step after <a href="/xray-mp-wiki/methods/purification/affinity-chromatography">IMAC</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified AaPrtD in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, <a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a>-bound</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals optimized in the presence of <a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a>. Structure determined by <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction">SAD</a> phasing using samarium <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate Buffer (Sodium Acetate)</a>-soaked crystals and <a href="/xray-mp-wiki/reagents/additives/mercury/">Mercury (HgCl2) - Aquaporin Inhibitor</a> chloride-soaked single-Cys mutants, and Se-Met-derivatized protein. Initial phases from <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction">SAD</a> in ShelX. Model built in Coot and refined in Phenix. Native data to 3.15 A resolution. Unit cell: 118.6, 97.9, 179.8 A, beta=100.5 deg.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l22">5L22</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MATKENTEN</span><span class="topo-inside">VLRSYLAKYK</span><span class="topo-membrane">KTLIIVGLFSLFINILFLLPSIY</span><span class="topo-outside">MLAVYDIVVPSTSVPTLL</span></span>
<span class="topo-line"><span class="topo-outside">VIT</span><span class="topo-membrane">ALAVVLYFALGLLQSVRAKVMQII</span><span class="topo-inside">SLKLDSELNKEVFTSSFEYAIRNPSKASAQPIN</span></span>
<span class="topo-line"><span class="topo-inside">DLYQLKQ</span><span class="topo-membrane">FLTSPVLFAIFDLPWVPIYFGVLF</span><span class="topo-outside">VFHVYY</span><span class="topo-membrane">GVMAILSMAVIVALAILNEYITK</span></span>
<span class="topo-line"><span class="topo-inside">KKLKESNELLVRSTNFLNRALLNAEVVEALGMRNNLYKKWMNFYSKHLSAFEE</span><span class="topo-membrane">ATDRNNF</span></span>
<span class="topo-line"><span class="topo-membrane">LSNLTRIFRIMAQSLM</span><span class="topo-outside">LGLGGYLAIKHEITTGMIVA</span><span class="topo-membrane">GSILLGRILGPIDTIVNGWRQIG</span><span class="topo-inside">N</span></span>
<span class="topo-line"><span class="topo-inside">TKVAYTRLNEFLKFL</span><span class="topo-unknown">RFKREVSVKL</span><span class="topo-inside">PEPKGEIELSNVVVVPPEGKTPVLRNINMRILPGE</span></span>
<span class="topo-line"><span class="topo-inside">FVAIIGPSGSGKSSLVRTILGIWLPVHGTVEIDGADLKQWDRDYFGKFVGYLPQDIELFE</span></span>
<span class="topo-line"><span class="topo-inside">GTVAENIARFGELDSEKIIEAAKLSGAHDVIIKLPDGYDTYIGPGGITLSGGQRQRIALA</span></span>
<span class="topo-line"><span class="topo-inside">RALYGNPRIVILDEPDSNLDEQGEQALYNALIELKKRKVTTIIVSHRIRLLNLVDKIAIM</span></span>
<span class="topo-line"><span class="topo-inside">QDGTLKAFGKADIIIQKLL</span><span class="topo-unknown">RKNVNLEHHHHHH</span></span>
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
      <td>10</td>
      <td>19</td>
      <td>10</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>42</td>
      <td>20</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>63</td>
      <td>43</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>87</td>
      <td>64</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>127</td>
      <td>88</td>
      <td>127</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>151</td>
      <td>128</td>
      <td>151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>157</td>
      <td>152</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>180</td>
      <td>158</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>233</td>
      <td>181</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>256</td>
      <td>234</td>
      <td>256</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>257</td>
      <td>276</td>
      <td>257</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>299</td>
      <td>277</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>315</td>
      <td>300</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>559</td>
      <td>326</td>
      <td>559</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5l22">5L22</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MATKENTENV</span><span class="topo-inside">LRSYLAKYK</span><span class="topo-membrane">KTLIIVGLFSLFINILFLLPSIY</span><span class="topo-outside">MLAVYDIVVPSTSVPTLL</span></span>
<span class="topo-line"><span class="topo-outside">VITA</span><span class="topo-membrane">LAVVLYFALGLLQSVRAKVMQII</span><span class="topo-inside">SLKLDSELNKEVFTSSFEYAIRNPSKASAQPIN</span></span>
<span class="topo-line"><span class="topo-inside">DLYQLKQ</span><span class="topo-membrane">FLTSPVLFAIFDLPWVPIYFGVLF</span><span class="topo-outside">VFHVYY</span><span class="topo-membrane">GVMAILSMAVIVALAILNEYITK</span></span>
<span class="topo-line"><span class="topo-inside">KKLKESNELLVRSTNFLNRALLNAEVVEALGMRNNLYKKWMNFYSKHLSAFEE</span><span class="topo-membrane">ATDRNNF</span></span>
<span class="topo-line"><span class="topo-membrane">LSNLTRIFRIMAQSLM</span><span class="topo-outside">LGLGGYLAIKHEITTGMIVA</span><span class="topo-membrane">GSILLGRILGPIDTIVNGWRQIG</span><span class="topo-inside">N</span></span>
<span class="topo-line"><span class="topo-inside">TKVAYTRLNEFLKFL</span><span class="topo-unknown">RFKREVSVKL</span><span class="topo-inside">PEPKGEIELSNVVVVPPEGKTPVLRNINMRILPGE</span></span>
<span class="topo-line"><span class="topo-inside">FVAIIGPSGSGKSSLVRTILGIWLPVHGTVEIDGADLKQWDRDYFGKFVGYLPQDIELFE</span></span>
<span class="topo-line"><span class="topo-inside">GTVAENIARFGELDSEKIIEAAKLSGAHDVIIKLPDGYDTYIGPGGITLSGGQRQRIALA</span></span>
<span class="topo-line"><span class="topo-inside">RALYGNPRIVILDEPDSNLDEQGEQALYNALIELKKRKVTTIIVSHRIRLLNLVDKIAIM</span></span>
<span class="topo-line"><span class="topo-inside">QDGTLKAFGKADIIIQKLL</span><span class="topo-unknown">RKNVNLEHHHHHH</span></span>
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
      <td>11</td>
      <td>19</td>
      <td>11</td>
      <td>19</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>20</td>
      <td>42</td>
      <td>20</td>
      <td>42</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>43</td>
      <td>64</td>
      <td>43</td>
      <td>64</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>65</td>
      <td>87</td>
      <td>65</td>
      <td>87</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>127</td>
      <td>88</td>
      <td>127</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>151</td>
      <td>128</td>
      <td>151</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>152</td>
      <td>157</td>
      <td>152</td>
      <td>157</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>180</td>
      <td>158</td>
      <td>180</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>181</td>
      <td>233</td>
      <td>181</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>234</td>
      <td>256</td>
      <td>234</td>
      <td>256</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>257</td>
      <td>276</td>
      <td>257</td>
      <td>276</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>277</td>
      <td>299</td>
      <td>277</td>
      <td>299</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>300</td>
      <td>315</td>
      <td>300</td>
      <td>315</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>326</td>
      <td>559</td>
      <td>326</td>
      <td>559</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Distinct T1SS ABC transporter architecture

[AaPrtD](/xray-mp-wiki/proteins/aaprtd/) reveals a distinct transmembrane architecture with highly kinked TM3 and TM6 helices near the cytosolic solvent-lipid interface. These kinks, which point toward the dimer interface, create a highly basic concave bowl on the PrtD surface formed by TM1, TM3, and TM6. The TM3 kink is stabilized by a conserved FxT motif (F128, T130) that interacts with TM6 of both the same and opposite subunit, tethering the protomers together.

### Narrow interior channel

The TM helices frame a narrow channel not observed in canonical peptide ABC transporters. The narrow pore and the highly basic concave surface likely engage acidic T1SS substrates via electrostatic interactions. The structure suggests a substrate entry window just above the NBDs where TM4 separates from TM6, which would need to be flexible to accommodate passage of polypeptide stretches.

### ATP hydrolysis required for secretion

In vivo secretion assays using the homologous DdPrtDEF system from Dickeya dadantii demonstrated that [ATP](/xray-mp-wiki/reagents/ligands/atp/) hydrolysis by PrtD is essential for substrate (PrtG) secretion. The catalytically inactive E492Q mutant retained [ATP](/xray-mp-wiki/reagents/ligands/atp/) binding but showed no secretion. Additionally, the entire T1SS complex (PrtD, PrtE, and PrtF) is required for transport across the inner membrane - neither PrtD alone nor PrtD-PrtE complex sufficed.

### Distinct from alternating access

The [AaPrtD](/xray-mp-wiki/proteins/aaprtd/) structure supports a polypeptide transport mechanism distinct from the alternating access mechanism of classical ABC exporters. The broken TM3 and TM6 helices are reminiscent of translocating ATPases such as ClpX or SecA, which interact with unfolded polypeptides at broken helix regions. This suggests that T1SS ABC transporters may use a channel-like mechanism to thread unfolded polypeptide substrates across the membrane.


## Cross-References

- <a href="/xray-mp-wiki/concepts/abc-transporter-mechanism/">ABC Transporter Mechanism</a> — AaPrtD is a bacterial ABC exporter with a distinct transport mechanism
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — AaPrtD structure supports a T1SS-specific mechanism distinct from alternating access
- <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">Single-Wavelength Anomalous Diffraction (SAD)</a> — Structure determined by SAD phasing using samarium, mercury, and selenium derivatives
- <a href="/xray-mp-wiki/concepts/type-1-secretion-system/">Type-1 Secretion System</a> — AaPrtD is the ABC transporter component of the T1SS machinery
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">N-Dodecyl-beta-D-maltopyranoside (beta-DDM)</a> — Detergent used for purification and crystallization of AaPrtD
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Final purification step after IMAC
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — IMAC used for initial purification
- <a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion-crystallization/">Vapor Diffusion Crystallization</a> — Crystallization method used for AaPrtD
- <a href="/xray-mp-wiki/methods/structure-determination/xray-crystallography/">X-ray Crystallography</a> — Method used in the study
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in the study
