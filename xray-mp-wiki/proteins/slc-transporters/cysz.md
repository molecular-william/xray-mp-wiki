---
title: "CysZ bacterial sulfate permease"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, channel, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.27829]
verified: agent
uniprot_id: ['A0A0X8F058', 'M4XKU7', 'Q5QUJ8']
---

# CysZ bacterial sulfate permease

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A0X8F058">UniProt: A0A0X8F058</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/M4XKU7">UniProt: M4XKU7</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q5QUJ8">UniProt: Q5QUJ8</a>

<span class="expr-badge">Pseudomonas fragi A22</span>

## Overview

CysZ is a bacterial inner-membrane sulfate (SO₄²⁻) permease/channel found exclusively
in prokaryotes. It belongs to a family of ~28-30 kDa integral membrane proteins that
mediate sulfate uptake for biosynthesis of cysteine and methionine. The CysZ family
shows no sequence or structural homology to any known transporter or channel fold.
Crystal structures from three bacterial species — Idiomarina loihiensis (IlCysZ,
PDB 3TX3, 2.3 Å), Pseudomonas fragi (PfCysZ, PDB 6D79, 3.2 Å), and Pseudomonas
denitrificans (PdCysZ, PDB 6D9Z, 3.4 Å) — reveal a novel fold consisting of two
long transmembrane (TM) helices and two hemi-penetrating helical hairpins that form
a tripod-like shape. PdCysZ assembles as a hexamer with D3 symmetry, organized as
a trimer of antiparallel dimers with inverted transmembrane topology — a highly
unusual arrangement shared with EmrE and Fluc channels. Functional studies show
CysZ mediates non-concentrative, channel-like sulfate flux that is not coupled
to proton or sodium gradients and is inhibited by sulfite (SO₃²⁻). A conserved
sulfate-binding site (GLR motif) at the loop between helices H1-H2 coordinates
sulfate via two arginine residues and backbone amides. The structure reveals a
putative pore and ion conduction pathway lined by highly conserved polar and charged
residues.


## Publications

### doi/10.7554/eLife.27829

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3tx3">3TX3</a></td>
      <td>2.3</td>
      <td>C2</td>
      <td>IlCysZ (Idiomarina loihiensis CysZ), residues 1-200</td>
      <td>SO₄²⁻ (selenate soak, refined at 2.1 Å)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6d79">6D79</a></td>
      <td>3.2</td>
      <td>C2</td>
      <td>PfCysZ (Pseudomonas fragi CysZ), residues 1-200, SeMet derivative</td>
      <td>--</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6d9z">6D9Z</a></td>
      <td>3.4</td>
      <td>P6₃</td>
      <td>PdCysZ (Pseudomonas denitrificans CysZ), hexamer, residues 1-200</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)pLysS
- **Construct**: CysZ genes cloned into pET-derived kanamycin-resistant vector with N-terminal deca-histidine tag and TEV protease cleavage site. Includes cysZ from I. loihiensis (UniProt Q5QUJ8), P. fragi (UniProt A0A0X8F058), P. denitrificans (UniProt M4XKU7)

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
      <td>Microfluidizer</td>
      <td>--</td>
      <td>20 mM Na-<a href="/xray-mp-wiki/reagents/buffers/hepes">Hepes</a> pH 7.0, 200 mM NaCl, 1 mM TCEP-HCl, 20 mM Na₂SO₄ + 1% (w/v) decyl maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>Solubilization for 1 hr at 4°C, insoluble material removed by <a href="/xray-mp-wiki/methods/purification/ultracentrifugation">ultracentrifugation</a> at 100,000 x g</td>
    </tr>
    <tr>
      <td>Affinity purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) Sepharose</td>
      <td>20 mM Na-<a href="/xray-mp-wiki/reagents/buffers/hepes">Hepes</a> pH 7.0, 200 mM NaCl, 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 40 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">imidazole</a> (wash); 250 mM imidazole (elution) + 0.2% decyl maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>Eluted protein dialyzed overnight with His-tagged <a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease at 4°C against 20 mM Na-<a href="/xray-mp-wiki/reagents/buffers/hepes">Hepes</a> pH 7.0, 200 mM NaCl, 0.2% <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>, 1 mM TCEP-HCl, 20 mM Na₂SO₄ for tag cleavage</td>
    </tr>
    <tr>
      <td>Reverse Ni-NTA</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta) Sepharose</td>
      <td>Same as dialysis buffer + 0.2% decyl maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>)</td>
      <td>Passaged over <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> to remove uncleaved CysZ, <a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease, and cleaved His₁₀ tag</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200</a> 10/300 HR</td>
      <td>20 mM Na-<a href="/xray-mp-wiki/reagents/buffers/hepes">Hepes</a> pH 7.0, 200 mM NaCl, 1 mM TCEP-HCl, 20 mM Na₂SO₄ + For IlCysZ: 0.06% <a href="/xray-mp-wiki/reagents/detergents/ldao/">LDAO</a>; for PfCysZ and PdCysZ: 1% beta-<a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> (beta-octyl glucopyranoside)</td>
      <td>Typical yield ~1.5 mg from 1 L culture</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion">Sitting-drop vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>IlCysZ at 6-8 mg/mL in LDAO; PfCysZ at 5 mg/mL in beta-OG; PdCysZ at 5-8 mg/mL in beta-OG</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>IlCysZ: 28-32% PEG400, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a>-HCl pH 8.0, 0.1 M NaCl or 0.1 M MgCl2. PfCysZ: 28% PEG400, 0.1 M MES pH 6.0. PdCysZ: 22-30% PEG550MME or PEG400, 0.1 M MES pH 6.0</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1-4 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals flash-frozen directly without additional cryo-protectant</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>IlCysZ crystals grew overnight, rhomboid/cuboid ~200 x 100 x 50 um. PfCysZ crystals cuboid, optimized with silicone oil microbatch. PdCysZ hexagonal prism crystals with multiple crystal forms (P6_3, P2_12_12_1, P4_122).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3tx3">3TX3</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">SYVMQKA</span><span class="topo-inside">AYSNSGLAYIGRGLELIRTKGLRRYVVVPIL</span><span class="topo-membrane">TNLILFSLAFTWLYGEVD</span><span class="topo-outside">YW</span><span class="topo-unknown">LNRFMSWLPDFFQWL</span><span class="topo-outside">EFILW</span><span class="topo-membrane">PLAVITIIALFSFIFSTIMHLI</span><span class="topo-inside">AAPFNGLLAEKVERYESGES</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LGDEGFLGLFKD</span><span class="topo-unknown">IPRTLKREMQKLMYYIPRALGFFLLSLV</span><span class="topo-inside">I</span><span class="topo-unknown">PVIGQVLWYIFVCWMMSIQYLDYPFDN</span><span class="topo-inside">HKLSFPRMRSELHQQRSKTLGFGFGVTVLTMIPLINLIIMPLAVCGATSLWV</span></span>
<span class="topo-ruler">         </span>
<span class="topo-line"><span class="topo-inside">DHYRRSALS</span></span>
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
      <td>7</td>
      <td>-2</td>
      <td>4</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>38</td>
      <td>5</td>
      <td>35</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>56</td>
      <td>36</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>58</td>
      <td>54</td>
      <td>55</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>73</td>
      <td>56</td>
      <td>70</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>74</td>
      <td>78</td>
      <td>71</td>
      <td>75</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>100</td>
      <td>76</td>
      <td>97</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>101</td>
      <td>132</td>
      <td>98</td>
      <td>129</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>133</td>
      <td>160</td>
      <td>130</td>
      <td>157</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>161</td>
      <td>161</td>
      <td>158</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>162</td>
      <td>188</td>
      <td>159</td>
      <td>185</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>189</td>
      <td>249</td>
      <td>186</td>
      <td>246</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6d79">6D79</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MPAPVLS</span><span class="topo-outside">GPQYLREGLKLVLSPGLRLFVLLPLLI</span><span class="topo-membrane">NLVLFVGLIYFAGHQFSLW</span><span class="topo-unknown">VDALMPSLPHWLSFLNYLLW</span><span class="topo-inside">PLFVV</span><span class="topo-membrane">LVALMVFFTFTMLANIIA</span><span class="topo-outside">APFNGFLSEKVEAVVRGVDNSPPF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">SWGELIAMVPRTLARE</span><span class="topo-membrane">MRKLGYFLPRAIALLILSFI</span><span class="topo-inside">PV</span><span class="topo-membrane">LNLVAAPLWLIFGVWMM</span><span class="topo-outside">AIQYIDYPADNHKLGWNEMLAWLREKRWQSLSFGGIVYLVLLIPVVNILMMPAAVAGATLFWVRE</span></span>
<span class="topo-ruler">       250 </span>
<span class="topo-line"><span class="topo-unknown">RGDEALARTRA</span></span>
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
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>34</td>
      <td>8</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>53</td>
      <td>35</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>73</td>
      <td>54</td>
      <td>73</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>74</td>
      <td>78</td>
      <td>74</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>96</td>
      <td>79</td>
      <td>96</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>97</td>
      <td>136</td>
      <td>97</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>137</td>
      <td>156</td>
      <td>137</td>
      <td>156</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>157</td>
      <td>158</td>
      <td>157</td>
      <td>158</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>159</td>
      <td>175</td>
      <td>159</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>240</td>
      <td>176</td>
      <td>240</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>251</td>
      <td>241</td>
      <td>251</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6d9z">6D9Z</a> — Chain F (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MS</span><span class="topo-outside">TLSGPQYLGEGLKLMMRPGLRLFVLLP</span><span class="topo-membrane">LSINLILFIGLIGFAINQF</span><span class="topo-inside">SHWVDWLMPSLPEWLSFLQFILWPLFVTLV</span><span class="topo-membrane">LLIVFFTFTLIANLIAA</span><span class="topo-outside">PFNGFLAEKVEVVVRGTDDFPAFSW</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">AELMAMVPRTI</span><span class="topo-membrane">GRELRKLGYFLPRAIALFILS</span><span class="topo-inside">LIPGL</span><span class="topo-membrane">NLIAAPLWLLFGVWMMAVQ</span><span class="topo-outside">YIDYPADNHKLGWNEMLAWLRSKRWACMGFGGITYLVLLIPLVNLVAMPAAVAGAVLFWVREGG</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-outside">DQ</span><span class="topo-unknown">ALVK</span></span>
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
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>3</td>
      <td>29</td>
      <td>3</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>48</td>
      <td>30</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>78</td>
      <td>49</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>95</td>
      <td>79</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>131</td>
      <td>96</td>
      <td>131</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>132</td>
      <td>152</td>
      <td>132</td>
      <td>152</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>153</td>
      <td>157</td>
      <td>153</td>
      <td>157</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>158</td>
      <td>176</td>
      <td>158</td>
      <td>176</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>177</td>
      <td>242</td>
      <td>177</td>
      <td>242</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>243</td>
      <td>246</td>
      <td>243</td>
      <td>246</td>
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

### Novel fold and dual-topology assembly

CysZ features a previously unknown protein fold with two long TM helices and two hemi-penetrating helical hairpins. The protein assembles with inverted transmembrane topology (antiparallel dimers), a rare arrangement shared with EmrE and Fluc fluoride channels. The PdCysZ hexamer reveals D3 symmetry organized as a trimer of antiparallel dimers.

### Non-concentrative sulfate flux

CysZ mediates sulfate translocation without coupling to ion gradients (H+ or Na+) or ATP, characteristic of a passive channel-like mechanism rather than an active transporter. Flux is non-concentrative (max ~5-fold accumulation) and is inhibited by sulfite (SO3(2-)).

### Conserved sulfate-binding GLR motif

A sulfate-binding site was identified at the loop between helices H1-H2, comprising a conserved GLR motif (G25, L26, R27, R28 in IlCysZ). Two arginine residues coordinate the sulfate ion. Mutation of these arginines (R27A/R28A) abolishes sulfate binding and uptake.

### Putative pore and conduction pathway

PoreWalker analysis identified a putative ion translocation pathway beginning at a conserved hydrophilic entrance near the E106-R110-E134-N184-H185 interaction network. The pathway widens into a large central hydrophobic cavity (~50 A across) in the hexamer. The structures captured in a closed state, suggesting conformational changes are required for ion passage.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KcsA K+ channel</a> — Different fold, but both are bacterial channel structures
- <a href="/xray-mp-wiki/proteins/other-ion-channels/bpe-fluoride-channel/">Bpe Fluc fluoride channel</a> — Shares dual-topology antiparallel dimer assembly
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating access mechanism</a> — Channel mechanism vs transporter alternating access in CysZ sulfate transport
