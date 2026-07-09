---
title: "E. coli Lipoprotein Diacylglyceryl Transferase (Lgt)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms10198]
verified: regex
uniprot_id: P60955
---

# E. coli Lipoprotein Diacylglyceryl Transferase (Lgt)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P60955">UniProt: P60955</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

Lgt (phosphatidylglycerol:prolipoprotein diacylglyceryl transferase) is an integral membrane enzyme from Escherichia coli that catalyses the first step of bacterial lipoprotein biogenesis: the transfer of a diacylglyceryl group from [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) (PG) to the thiol group of the conserved cysteine residue in the lipobox motif of prolipoproteins. The crystal structures of E. coli Lgt were determined at 1.6 and 1.9 A resolution, revealing a novel 7-transmembrane helix fold with a periplasmic head domain, two amphipathic arms, and a central cavity containing two PG-binding sites. The catalytic centre involves a conserved hydrogen bond network centred on R143 and R239. Lgt is an essential enzyme in Gram-negative bacteria and a potential target for broad-spectrum antibiotics.


## Publications

### doi/10.1038##ncomms10198

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5azc">5AZC</a></td>
      <td>1.6</td>
      <td>P2_12_12_1</td>
      <td>wild-type E. coli Lgt (residues 3-286)</td>
      <td>palmitic acid, <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>, PG</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5azc">5AZC</a></td>
      <td>1.9</td>
      <td>P2_12_12_1</td>
      <td>wild-type E. coli Lgt (residues 3-286)</td>
      <td>PG, diacylglycerol (<a href="/xray-mp-wiki/reagents/lipids/dag/">DAG</a>)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43(DE3) with pET28a vector; [Iptg](/xray-mp-wiki/reagents/additives/iptg/) induction at 16 C for 20 h
- **Construct**: full-length E. coli Lgt (291 aa) with N-terminal [His6 Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (not explicitly specified as hanging/sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified Lgt in 20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> pH 7.5, 100 mM NaCl, 0.6% <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a>; concentrated to ~20 mg/mL</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not explicitly specified in the raw text</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Two crystal forms obtained: form-1 (1.6 A, with palmitic acid/OG) and form-2 (1.9 A, with PG/DAG). Phased using Se-Met SAD.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5azc">5AZC</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVT</span><span class="topo-outside">SSYLHFPEFDPVIFSIGPVAL</span><span class="topo-membrane">HWYGLMYLVGFIFAMWLATRRA</span><span class="topo-inside">NRPGSGWTK</span><span class="topo-membrane">NEVENLLYAGFLGVFLGGRIGYVLF</span><span class="topo-outside">YN</span><span class="topo-unknown">FPQFMA</span><span class="topo-outside">DPLYLFRVWDGG</span><span class="topo-membrane">MSFHGGLIGVIVVMIIFARR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TKRS</span><span class="topo-membrane">FFQVSDFIAPLIPFGLGAGRLGN</span><span class="topo-outside">FINGELWGRVDPNFPFAMLFPGSRTEDILLLQTNPQWQSIFDTYGVLPRHPS</span><span class="topo-membrane">QLYELLLEGVVLFIILNLYIR</span><span class="topo-inside">KPRPMG</span><span class="topo-membrane">AVSGLFLIGYGAFR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300</span>
<span class="topo-line"><span class="topo-membrane">IIVEF</span><span class="topo-outside">FRQPDAQFTGA</span><span class="topo-membrane">WVQYISMGQILSIPMIVAGVIMMVWA</span><span class="topo-inside">YRRSP</span><span class="topo-unknown">QQHVSLEHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>4</td>
      <td>24</td>
      <td>3</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>46</td>
      <td>24</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>55</td>
      <td>46</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>80</td>
      <td>55</td>
      <td>79</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>82</td>
      <td>80</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>88</td>
      <td>82</td>
      <td>87</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>89</td>
      <td>100</td>
      <td>88</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>120</td>
      <td>100</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>124</td>
      <td>120</td>
      <td>123</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>147</td>
      <td>124</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>199</td>
      <td>147</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>220</td>
      <td>199</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>226</td>
      <td>220</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>245</td>
      <td>226</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>246</td>
      <td>256</td>
      <td>245</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>282</td>
      <td>256</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>283</td>
      <td>287</td>
      <td>282</td>
      <td>286</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5azc">5AZC</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MVT</span><span class="topo-outside">SSYLHFPEFDPVIFSIGPVAL</span><span class="topo-membrane">HWYGLMYLVGFIFAMWLATRRA</span><span class="topo-inside">NRPGSGWTK</span><span class="topo-membrane">NEVENLLYAGFLGVFLGGRIGYVLF</span><span class="topo-outside">YN</span><span class="topo-unknown">FPQFMA</span><span class="topo-outside">DPLYLFRVWDGG</span><span class="topo-membrane">MSFHGGLIGVIVVMIIFARR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">TKRS</span><span class="topo-membrane">FFQVSDFIAPLIPFGLGAGRLGN</span><span class="topo-outside">FINGELWGRVDPNFPFAMLFPGSRTEDILLLQTNPQWQSIFDTYGVLPRHPS</span><span class="topo-membrane">QLYELLLEGVVLFIILNLYIR</span><span class="topo-inside">KPRPMG</span><span class="topo-membrane">AVSGLFLIGYGAFR</span></span>
<span class="topo-ruler">       250       260       270       280       290       300</span>
<span class="topo-line"><span class="topo-membrane">IIVEF</span><span class="topo-outside">FRQPDAQFTGA</span><span class="topo-membrane">WVQYISMGQILSIPMIVAGVIMMVWA</span><span class="topo-inside">YRRSP</span><span class="topo-unknown">QQHVSLEHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>4</td>
      <td>24</td>
      <td>3</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>25</td>
      <td>46</td>
      <td>24</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>55</td>
      <td>46</td>
      <td>54</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>80</td>
      <td>55</td>
      <td>79</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>82</td>
      <td>80</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>83</td>
      <td>88</td>
      <td>82</td>
      <td>87</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>89</td>
      <td>100</td>
      <td>88</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>120</td>
      <td>100</td>
      <td>119</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>124</td>
      <td>120</td>
      <td>123</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>147</td>
      <td>124</td>
      <td>146</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>148</td>
      <td>199</td>
      <td>147</td>
      <td>198</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>220</td>
      <td>199</td>
      <td>219</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>221</td>
      <td>226</td>
      <td>220</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>227</td>
      <td>245</td>
      <td>226</td>
      <td>244</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>246</td>
      <td>256</td>
      <td>245</td>
      <td>255</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>282</td>
      <td>256</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>283</td>
      <td>287</td>
      <td>282</td>
      <td>286</td>
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

### Novel 7-TM fold with central cavity and two substrate-binding sites

Lgt adopts a novel folding topology with seven transmembrane helices (TMs 1-7) organized into a major and minor TM domain, a periplasmic head domain, and two amphipathic arms. The central cavity between the major and minor TM domains contains two distinct PG-binding sites separated by W256. The first PG-binding site (site I) involves E151, and the second (site II) involves the catalytically essential R143. Two clefts (front and side) connect the cavity to the lipid bilayer, providing lateral access for substrates.

### Catalytic mechanism and key residues

The catalytically essential residues include R143, R239, and H103 (from the conserved HGGL motif). R143 directly binds the donor substrate PG at the second binding site, while R239 is part of the buried H-bond network. H103 in the HGGL motif at the N-terminal end of TM3 is critical for activity and likely interacts with the lipobox-containing peptide substrate. The cytoplasmic side is highly positively charged (positive-inside rule). The proposed mechanism involves SN2-like attack of the lipobox cysteine thiol on the diacylglyceryl group of PG.

### Inhibitor binding and substrate specificity

Palmitic acid binds to the active site and acts as a competitive inhibitor of Lgt. The enzyme shows specificity for negatively charged phospholipids as diacylglyceryl donors: DPPG > DPPS > DPPA, while neutral lipids (DPPE, DPPC, [DAG](/xray-mp-wiki/reagents/lipids/dag/)) are not substrates. Saturated alkyl chains stabilize Lgt more effectively than unsaturated chains. A GFP-based in vitro assay (lipoGFP substrate) was developed to monitor Lgt activity. Lyso-PG can serve as a substrate but is less effective than full PG.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/og/">OG</a> — Referenced in context related to OG
- <a href="/xray-mp-wiki/reagents/lipids/dag/">DAG</a> — Referenced in context related to DAG
- <a href="/xray-mp-wiki/reagents/additives/iptg/">Iptg</a> — Referenced in context related to Iptg
- <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His6 Tag</a> — Referenced in context related to His6 Tag
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Hcl</a> — Referenced in context related to Tris Hcl
- <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> — Referenced in context related to DM
- <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> — Referenced in context related to DM
- <a href="/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/">Phosphatidylglycerol</a> — Referenced in context related to Phosphatidylglycerol
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in context related to Glycerol
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Referenced in context related to Imidazole
