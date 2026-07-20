---
title: "Phosphatidylinositol-Phosphate Synthase (RsPIPS) from Renibacterium salmoninarum"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1038##ncomms9505]
verified: agent
uniprot_id: A9WSF5
---

# Phosphatidylinositol-Phosphate Synthase (RsPIPS) from Renibacterium salmoninarum

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A9WSF5">UniProt: A9WSF5</a>

<span class="expr-badge">Renibacterium salmoninarum (strain ATCC 33209 / DSM 20767 / JCM 11484 / NBRC 15589 / NCIMB 2235)</span>

## Overview

Phosphatidylinositol-phosphate (PIP) synthase catalyses the first step of [Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/phosphatidylinositol/) biosynthesis in prokaryotes, using L-myo-inositol-1-phosphate as the acceptor alcohol and CDP-[Diacylglycerol](/xray-mp-wiki/reagents/lipids/diacylglycerol/) (CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/)) as the donor substrate. The crystal structures of PIP synthase from Renibacterium salmoninarum (RsPIPS) were determined in apo form (2.5 Å, construct RsPIPS-Δ6N with N-terminal deletion) and in complex with CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) (3.6 Å, full-length RsPIPS-FL), revealing a homodimeric six-transmembrane-helix architecture characteristic of class I CDP-alcohol phosphotransferases (CDP-APs). The structures identify the inositol phosphate acceptor pocket (defined by conserved arginines R155 and R195), the nucleotide-binding pocket containing the signature CDP-AP sequence, and a hydrophobic groove between TM2 and JM1 that accommodates the acyl chains of CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/). A chimeric fusion strategy using the [AF2299 CDP-Alcohol Phosphotransferase from Archaeoglobus fulgidus](/xray-mp-wiki/proteins/enzymes/af2299/) cytidylyltransferase-like domain as a crystallization chaperone was essential for obtaining diffracting crystals. Functional characterization of the 40%-identical ortholog from Mycobacterium tuberculosis (MtPIPS, a potential anti-tuberculosis drug target) supports the proposed mechanism and reveals a sequential ordered bi-bi reaction in which CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) binds first, followed by inositol phosphate, with D93 acting as the catalytic base.

## Publications

### doi/10.1038##ncomms9505

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5d91">5D91</a></td>
      <td>2.50</td>
      <td>P 2₁ 2₁ 2</td>
      <td>RsPIPS-Δ6N: chimeric construct with N-terminal <a href="/xray-mp-wiki/proteins/enzymes/af2299/">AF2299 CDP-Alcohol Phosphotransferase from Archaeoglobus fulgidus</a> cytidylyltransferase-like domain, first six residues of RsPIPS omitted, with six interface mutations (L75, F77, etc.)</td>
      <td>Apo (SO₄²⁻ bound at the active site mimicking the phosphate of inositol phosphate)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5d91">5D91</a></td>
      <td>3.61</td>
      <td>P 2₁</td>
      <td>RsPIPS-FL: full-length RsPIPS (absent initiating methionine) with N-terminal <a href="/xray-mp-wiki/proteins/enzymes/af2299/">AF2299 CDP-Alcohol Phosphotransferase from Archaeoglobus fulgidus</a> cytidylyltransferase-like domain and six interface mutations</td>
      <td>CDP-<a href="/xray-mp-wiki/reagents/lipids/diacylglycerol/">Diacylglycerol</a> (CDP-<a href="/xray-mp-wiki/reagents/lipids/dag/">DAG</a>), Mg²⁺</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli (expression of synthetic gene; chimeric construct with N-terminal [AF2299 CDP-Alcohol Phosphotransferase from Archaeoglobus fulgidus](/xray-mp-wiki/proteins/enzymes/af2299/) cytidylyltransferase-like domain)
- **Construct**: Chimeric RsPIPS with N-terminal [AF2299 CDP-Alcohol Phosphotransferase from Archaeoglobus fulgidus](/xray-mp-wiki/proteins/enzymes/af2299/) extramembrane domain (residues 1-242) fused to RsPIPS sequence. Six interface mutations (L75F, F77Y, etc.) introduced to mimic the [AF2299 CDP-Alcohol Phosphotransferase from Archaeoglobus fulgidus](/xray-mp-wiki/proteins/enzymes/af2299/) soluble-TM domain interface. RsPIPS-Δ6N omits first 6 residues; RsPIPS-FL includes full sequence minus initiating Met.

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
      <td>1. Affinity purification</td>
      <td>Ni²⁺ <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>His-tagged chimeric protein purified by <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
    </tr>
    <tr>
      <td>2. Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td>—</td>
      <td></td>
      <td>Final polishing step in detergent-containing buffer</td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified RsPIPS chimera in detergent solution for LCP crystallization

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified RsPIPS chimera in detergent solution, reconstituted into <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 °C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>RsPIPS-Δ6N diffracted to 2.5 Å. RsPIPS-FL diffracted to 3.6 Å. Crystals grown in LCP using <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> as host lipid. Heavy-atom derivatives for SeMet SAD phasing. Data collected at APS NE-CAT beamline 24ID-C.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5d91">5D91</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MRLAYVKNHEIYGEKLLGLTLRERIEKTLQRAGFDVRFFDELSLEEAEDYLIILEPVLILERDLLLEGRKILVSDGFTVGYFFGGDFRTVFDGNLQSSIEKYLSLNNLESYEIWAIKLSN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">DNLKTAEKLLLSSLIGSRGLFAAIF</span><span class="topo-unknown">LPIARLLAD</span><span class="topo-inside">WGVSPDAVTV</span><span class="topo-membrane">VGTLGVMAGALIFYPMGQ</span><span class="topo-outside">L</span><span class="topo-membrane">FWGTVVITVFVFSD</span><span class="topo-inside">IIDGLMARLLFREGPWGAFLDSYL</span><span class="topo-membrane">DRVGDSSVFTGIVIWFFL</span><span class="topo-outside">G</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330      </span>
<span class="topo-line"><span class="topo-outside">GANP</span><span class="topo-membrane">TIAILALICLVLSSLV</span><span class="topo-inside">SYSKARAEGLGLTANVGI</span><span class="topo-membrane">AERSERLVVVLVATGLVGL</span><span class="topo-outside">GIPS</span><span class="topo-membrane">WVLLVVLIVLAIASVVT</span><span class="topo-inside">IFQRVLTVREQAKAWTA</span><span class="topo-unknown">S</span></span>
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
      <td>145</td>
      <td>-130</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>154</td>
      <td>15</td>
      <td>23</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>155</td>
      <td>164</td>
      <td>24</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>182</td>
      <td>34</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>183</td>
      <td>52</td>
      <td>52</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>197</td>
      <td>53</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>221</td>
      <td>67</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>239</td>
      <td>91</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>244</td>
      <td>109</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>260</td>
      <td>114</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>261</td>
      <td>278</td>
      <td>130</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>297</td>
      <td>148</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>301</td>
      <td>167</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>318</td>
      <td>171</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>319</td>
      <td>335</td>
      <td>188</td>
      <td>204</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5d91">5D91</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MRLAYVKNHEIYGEKLLGLTLRERIEKTLQRAGFDVRFFDELSLEEAEDYLIILEPVLILERDLLLEGRKILVSDGFTVGYFFGGDFRTVFDGNLQSSIEKYLSLNNLESYEIWAIKLSN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">DNLKTAEKLLLSSLIGSRGLFAAIF</span><span class="topo-unknown">LPIARLLAD</span><span class="topo-inside">WGVSPDAVTV</span><span class="topo-membrane">VGTLGVMAGALIFYPMGQ</span><span class="topo-outside">L</span><span class="topo-membrane">FWGTVVITVFVFSD</span><span class="topo-inside">IIDGLMARLLFREGPWGAFLDSYL</span><span class="topo-membrane">DRVGDSSVFTGIVIWFFL</span><span class="topo-outside">G</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330      </span>
<span class="topo-line"><span class="topo-outside">GANP</span><span class="topo-membrane">TIAILALICLVLSSLV</span><span class="topo-inside">SYSKARAEGLGLTANVGI</span><span class="topo-membrane">AERSERLVVVLVATGLVGL</span><span class="topo-outside">GIPS</span><span class="topo-membrane">WVLLVVLIVLAIASVVT</span><span class="topo-inside">IFQRVLTVREQAKAWTA</span><span class="topo-unknown">S</span></span>
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
      <td>145</td>
      <td>-130</td>
      <td>14</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>154</td>
      <td>15</td>
      <td>23</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>155</td>
      <td>164</td>
      <td>24</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>165</td>
      <td>182</td>
      <td>34</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>183</td>
      <td>183</td>
      <td>52</td>
      <td>52</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>197</td>
      <td>53</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>198</td>
      <td>221</td>
      <td>67</td>
      <td>90</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>222</td>
      <td>239</td>
      <td>91</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>244</td>
      <td>109</td>
      <td>113</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>245</td>
      <td>260</td>
      <td>114</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>261</td>
      <td>278</td>
      <td>130</td>
      <td>147</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>279</td>
      <td>297</td>
      <td>148</td>
      <td>166</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>301</td>
      <td>167</td>
      <td>170</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>302</td>
      <td>318</td>
      <td>171</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>319</td>
      <td>335</td>
      <td>188</td>
      <td>204</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Dimeric six-TM architecture of PIP synthase

RsPIPS adopts a homodimeric architecture with each protomer possessing six transmembrane helices surrounding a large polar cavity located at the cytosolic boundary of the membrane. This architecture is conserved among class I CDP-APs that utilize soluble acceptor substrates.

### Active site architecture with three subregions

The central polar cavity contains three distinct regions that form the active site: (1) the inositol phosphate acceptor-binding pocket defined by conserved arginines R155 and R195 that coordinate the phosphate group; (2) the nucleotide-binding pocket between TM2 and TM3 characterized by the conserved CDP-AP signature sequence D₁xxD₂G₁xxAR...G₂xxxD₃xxxD₄; and (3) a hydrophobic groove between TM2 and JM1 that accommodates the acyl chains of CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/).

### CDP-DAG binding and lipid substrate pathway

The structure of RsPIPS-FL with bound CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) reveals a hydrophobic crevice between JM1, TM2, and TM5 that is directly exposed to the bulk lipid, providing a pathway for lateral diffusion of CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) into the active site. The CDP moiety is wedged between TM2 and TM3, interacting with residues from the signature sequence. D31 and T34 (conserved P(D/N)xx(T/S) motif on TM1) form hydrogen bonds with the pyrimidine ring.

### Sequential ordered bi-bi reaction mechanism

Functional characterization of MtPIPS (40% identical to RsPIPS) demonstrates that inositol phosphate binding is strictly CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) dependent, supporting a sequential ordered bi-bi mechanism in which CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) binds first, followed by inositol phosphate. D93 (the fourth aspartate in the signature sequence 'D₄') acts as the catalytic base. Mutation D93N nearly completely abrogates activity without substantially affecting substrate binding.

### Inositol phosphate recognition by conserved arginine pair

Two conserved arginine residues, R155 and R195, coordinate the phosphate group of inositol phosphate. Mutation of either residue to alanine or glutamine severely impairs enzymatic activity. R195Q mutation increases K_M for inositol phosphate 10-fold (from 122 µM to 1,208 µM) while only mildly affecting CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/) K_M, confirming these residues are specific inositol phosphate binding determinants.

### M. tuberculosis PIP synthase as anti-tuberculosis drug target

Genetic ablation of PIP synthase in Mycobacterium smegmatis is lethal. The unique prokaryotic PI biosynthesis pathway and the absence of inositol phosphate recognition by eukaryotic CDP-APs position MtPIPS as a plausible target for novel anti-tuberculosis drugs. The inositol phosphate binding pocket, with its relatively low affinity (K_M = 122 µM), provides a potentially druggable site that could be targeted by competitive inhibitors.


## Cross-References

- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/enzymes/af2299/">AF2299 CDP-Alcohol Phosphotransferase from Archaeoglobus fulgidus</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/lipids/dag/">DAG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/lipids/diacylglycerol/">Diacylglycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylinositol/">Phosphatidylinositol</a> — Additive used in purification or crystallization buffers
