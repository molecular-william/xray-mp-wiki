---
title: "E. coli Phosphatidylglycerophosphate Phosphatase B (ecPgpB)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1403097111]
verified: false
---

# E. coli Phosphatidylglycerophosphate Phosphatase B (ecPgpB)

## Overview

ecPgpB is an E. coli membrane-integrated type II [Phosphatidic Acid](/xray-mp-wiki/reagents/lipids/phosphatidic-acid/) phosphatase (PAP2) that catalyzes
removal of the terminal phosphate group from the lipid carrier undecaprenyl pyrophosphate. It is essential
for transport of hydrophilic small molecules across the membrane. The 3.2 A crystal structure revealed
a six-transmembrane helix topology with a V-shaped TM helix pair (TM2-TM3) forming the substrate
entrance cleft, allowing lateral movement of lipid substrates from the membrane bilayer into the active site.
The structure serves as a prototype for eukaryotic PAP2 enzymes including human -6-phosphatase.


## Publications

### doi/10.1073##pnas.1403097111

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4px7">4PX7</a></td>
      <td>3.2</td>
      <td>P2(1)2(1)2(1)</td>
      <td>ecPgpB WT and I116M/E120K mutant</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21
- **Construct**: Full-length PgpB cloned from E. coli BL21 genome
- **Notes**: Expressed as recombinant protein

**Purification:**

- **Expression system**: E. coli BL21

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
      <td>Purification</td>
      <td>Detergent solubilization and purification</td>
      <td>—</td>
      <td> + <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> ()</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified ecPgpB in detergent combination</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>I116M/E120K double mutant gave better resolution. Space group P2(1)2(1)2(1).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4px7">4PX7</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">GRSI</span><span class="topo-membrane">ARRTAVGAALLLVMPVAVWIS</span><span class="topo-outside">GWRWQPG</span><span class="topo-unknown">EQ</span><span class="topo-outside">SWLLK</span><span class="topo-membrane">AAFWVTETVTQPWGVITHLILFGWFL</span><span class="topo-inside">WCLRFRIKAA</span><span class="topo-membrane">FVLFAILAAAILVGQGVKSWIK</span><span class="topo-outside">DKVQEPRPFVIWLEKTHHMPVDK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">FYTLKRAERGNLVKEQLAE</span><span class="topo-unknown">EKNI</span><span class="topo-outside">P</span><span class="topo-unknown">QYLRSHWQKE</span><span class="topo-outside">TGFA</span><span class="topo-membrane">FPSGHTMFAASWALLAVGLLW</span><span class="topo-inside">PRRR</span><span class="topo-membrane">TLTIAILLVWATGVMGSRLL</span><span class="topo-outside">LGM</span><span class="topo-membrane">HWPRDLVVATLISWALVAVATWLA</span><span class="topo-inside">QRICGPLTPP</span></span>
<span class="topo-ruler">       250       260  </span>
<span class="topo-line"><span class="topo-unknown">A</span><span class="topo-inside">EENREIAQREQESLEHH</span><span class="topo-unknown">HHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (22 regions)</summary>
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
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>25</td>
      <td>5</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>32</td>
      <td>26</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>34</td>
      <td>33</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>39</td>
      <td>35</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>65</td>
      <td>40</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>75</td>
      <td>66</td>
      <td>75</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>76</td>
      <td>97</td>
      <td>76</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>98</td>
      <td>139</td>
      <td>98</td>
      <td>139</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>140</td>
      <td>143</td>
      <td>140</td>
      <td>143</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>144</td>
      <td>144</td>
      <td>144</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>145</td>
      <td>154</td>
      <td>145</td>
      <td>154</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>155</td>
      <td>158</td>
      <td>155</td>
      <td>158</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>179</td>
      <td>159</td>
      <td>179</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>180</td>
      <td>183</td>
      <td>180</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>203</td>
      <td>184</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>206</td>
      <td>204</td>
      <td>206</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>230</td>
      <td>207</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>240</td>
      <td>231</td>
      <td>240</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>241</td>
      <td>241</td>
      <td>241</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>242</td>
      <td>258</td>
      <td>242</td>
      <td>258</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>262</td>
      <td>259</td>
      <td>262</td>
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

### V-shaped TM helix pair substrate entrance

A V-shaped TM helix pair (TMs 2 and 3) forms a surface cleft at the membrane-solvent interface,
allowing membrane-associated lipid substrates to enter the active site. The lipid substrate inserts
its phosphate head toward the nucleophilic His207(3.08) to form the phosphate-enzyme intermediate.

### Induced-fit substrate binding

The crystal structure represents an apo-form. TM3 packs loosely, placing Lys97(1.01) ~9 A from
its active position. Substrate binding drives TM3 movement toward TM2, completing the active site.
This induced-fit mechanism restricts activity to properly bound lipid substrates.

### Conserved active site with soluble PAP2 enzymes

Despite different substrate binding mechanisms, the catalytic residues (His163, His207, Asp211)
and overall fold of TMs 4-6 are nearly identical to soluble PAP2 enzymes ebNSAP (PDB 1EOI)
and ciCPO (PDB 1VNC), confirming evolutionary relationship between soluble and TM PAP2 proteins.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/pap2-family/">Type II Phosphatidic Acid Phosphatase (PAP2) Family</a> — ecPgpB is prototypical transmembrane PAP2 enzyme
- <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> — Referenced in ecpgb text
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a> — Referenced in ecpgb text
- <a href="/xray-mp-wiki/reagents/nonyl-beta-d-glucopyranoside/">Nonyl Beta D Glucopyranoside</a> — Referenced in ecpgb text
- <a href="/xray-mp-wiki/reagents/lipids/phosphatidic-acid/">Phosphatidic Acid</a> — Referenced in ecpgb text
