---
title: "Pseudomonas aeruginosa Apolipoprotein N-Acyl Transferase (LntPae)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.adf5799]
verified: agent
uniprot_id: Q9ZI86
---

# Pseudomonas aeruginosa Apolipoprotein N-Acyl Transferase (LntPae)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9ZI86">UniProt: Q9ZI86</a>

<span class="expr-badge">Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1)</span>

## Overview

Pseudomonas aeruginosa apolipoprotein N-acyltransferase (LntPae) is a 57 kDa integral membrane enzyme that catalyzes the final step of lipoprotein maturation in Gram-negative bacteria, transferring an acyl chain from a glycerophospholipid (GPL) donor to the N-terminal cysteine of diacylated lipoproteins. LntPae shares 39% sequence identity with E. coli [LNT](/xray-mp-wiki/proteins/enzymes/lnt/). The structure was determined by x-ray crystallography (PDB 8AQ2) as a TITC-modified variant in complex with [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/), capturing a mimic of the second Michaelis complex (M2 state) in the ping-pong reaction mechanism.

## Publications

### doi/10.1126##sciadv.adf5799

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/8aq2">8AQ2</a></td>
      <td>Not specified (~2.7 A range)</td>
      <td>Not specified</td>
      <td>Full-length P. aeruginosa <a href="/xray-mp-wiki/proteins/enzymes/lnt/">LNT</a> with TITC modification at catalytic Cys</td>
      <td>TITC (tetradecyl-1-isothiocyanate), <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43(DE3)
- **Construct**: Full-length P. aeruginosa [LNT](/xray-mp-wiki/proteins/enzymes/lnt/) (514 residues) with N-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/)

**Purification:**

- **Expression system**: E. coli C43(DE3)
- **Expression construct**: Full-length P. aeruginosa [LNT](/xray-mp-wiki/proteins/enzymes/lnt/) with N-terminal [Polyhistidine Tag (His6)](/xray-mp-wiki/reagents/protein-tags/his6-tag/)

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
      <td>High-pressure homogenization</td>
      <td>—</td>
      <td></td>
      <td>Membranes isolated by centrifugation at 120,000g for 45 min</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>Lauryl <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> neopentyl glycol (<a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>) or n-dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Solubilized for 45 min at room temperature</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> Superflow</td>
      <td></td>
      <td>Washed with buffer containing 40 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; eluted with 400 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>HiLoad 16/60 <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td></td>
      <td>Purified in buffer containing 0.05% (w/v) <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> or 0.02% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (in meso)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>TITC-modified LntPae in detergent</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Varies</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized by in meso method. Data collected at Swiss Light Source.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/8aq2">8AQ2</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGSSHHHHH</span><span class="topo-outside">HSSGLVPRGSHMRWISRPGW</span><span class="topo-membrane">PGHLLALAAGALTPLAL</span><span class="topo-inside">APF</span><span class="topo-membrane">DYWPLAILSIALLYLGLR</span><span class="topo-outside">GLPG</span><span class="topo-membrane">KSALWRGWWYGFGAFGAGTS</span><span class="topo-inside">WIYVSIHDYGAASVPLAS</span><span class="topo-membrane">LLMLGFTAGVA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">FFFALPAWLWARCLR</span><span class="topo-outside">RDNAP</span><span class="topo-membrane">LGDALAFAALWLALELFRSWFL</span><span class="topo-inside">TGFPWLYAGYSQLQGPLAGLVPV</span><span class="topo-membrane">GGVWLSSFVIALSAALLVNLP</span><span class="topo-outside">RLFPHGA</span><span class="topo-membrane">SLLLGLVLLLGPWAAGLYL</span><span class="topo-inside">KGHAWTHS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">AGEPLRVVAIQGNIAQELKWDPNQVRAQLDLYRDLSLPQQDVDLIVWPETAVPILQDMASGYLGAMGQVADEKNAALITGVPVRERLADGKSRYFNGITVVGEGAGTYLKQKLVPFGEYV</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PLQDLLRGLIAFFDLPMSDFARGPADQPLLKAKGYQIAPYICYEVVYPEFAAALAAQSQVLLTVSNDTWFGTSIGPLQHLQMAQMRALESGRWMIRATNNGVTGLIDPYGRIVRQIPQFQ</span></span>
<span class="topo-ruler">       490       500       510       520       530 </span>
<span class="topo-line"><span class="topo-inside">QGILRGEVIPMQGLTPYLQYRV</span><span class="topo-membrane">WPLAGLAGVLLLWALL</span><span class="topo-outside">GRQLRPQERRL</span><span class="topo-unknown">FG</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>9</td>
      <td>-19</td>
      <td>-11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>29</td>
      <td>-10</td>
      <td>9</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>10</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>49</td>
      <td>27</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>67</td>
      <td>30</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>71</td>
      <td>48</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>72</td>
      <td>91</td>
      <td>52</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>109</td>
      <td>72</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>110</td>
      <td>135</td>
      <td>90</td>
      <td>115</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>140</td>
      <td>116</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>141</td>
      <td>162</td>
      <td>121</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>163</td>
      <td>185</td>
      <td>143</td>
      <td>165</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>186</td>
      <td>206</td>
      <td>166</td>
      <td>186</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>207</td>
      <td>213</td>
      <td>187</td>
      <td>193</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>232</td>
      <td>194</td>
      <td>212</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>502</td>
      <td>213</td>
      <td>482</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>503</td>
      <td>518</td>
      <td>483</td>
      <td>498</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>519</td>
      <td>529</td>
      <td>499</td>
      <td>509</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>530</td>
      <td>531</td>
      <td>510</td>
      <td>511</td>
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

### M2 state mimic reveals acyl chain binding sites

The TITC-modified LntPae structure with two [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) molecules (PDB 8AQ2) represents a mimic of the second Michaelis complex (M2 state). The TITC alkyl chain aligns with the amide-linked acyl chain of the final product, while the two [Monoolein](/xray-mp-wiki/reagents/lipids/monoolein/) molecules align with the sn-1 and sn-2 chains of the diacylglyceryl moiety in the TA-BLP product. This structure, together with the other eight structures solved in the study, defines three distinct acyl chain binding sites in [LNT](/xray-mp-wiki/proteins/enzymes/lnt/) that are occupied to varying degrees throughout the N-acylation reaction.

### Structural conservation across Lnt orthologs

Despite only 39% sequence identity, LntPae and LntEco share highly similar overall architecture with the same nitrilase-like domain (ND) and membrane domain (MD) organization. The active site catalytic triad (Glu267-Lys335-Cys387 in E. coli numbering) is conserved. The structures solved at multiple states along the reaction coordinate validate the ping-pong mechanism and explain substrate promiscuity.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/e-coli-lnt/">Escherichia coli Apolipoprotein N-Acyl Transferase (Lnt)</a> — Orthologous Lnt from E. coli with 39% sequence identity; both characterized in the same structural study
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/ping-pong-mechanism/">Ping-Pong Catalytic Mechanism</a> — Lnt uses ping-pong mechanism for N-acyl transfer; structural snapshots of all states
- <a href="/xray-mp-wiki/concepts/protein-families/nitrilase-superfamily/">Nitrilase Superfamily</a> — Lnt belongs to the nitrilase superfamily (ninth branch)
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/enzymes/lnt/">LNT</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/maltose/">Maltose</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> — Detergent used in purification or crystallization
