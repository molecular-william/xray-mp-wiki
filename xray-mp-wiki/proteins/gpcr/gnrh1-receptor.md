---
title: "Human Gonadotropin-Releasing Hormone Receptor (GnRH1R)"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-020-19109-w]
verified: agent
uniprot_id: P30968
---

# Human Gonadotropin-Releasing Hormone Receptor (GnRH1R)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P30968">UniProt: P30968</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The human gonadotropin-releasing hormone receptor (GnRH1R, also known as luteinizing hormone-releasing hormone receptor) is a class A [GPCR](/xray-mp-wiki/concepts/signaling-receptors/gpcr/) that serves as the central regulator of the reproductive system. Activated by the decapeptide GnRH via the G_q signaling pathway, GnRH1R initiates the reproductive hormone cascade and releases gonadotropins (FSH and LH). The crystal structure of GnRH1R bound to the FDA-approved small-molecule antagonist drug elagolix at 2.8 Å resolution reveals an enlarged orthosteric binding pocket co-occupied by elagolix and the receptor N-terminus. Uniquely among class A GPCRs, GnRH1R lacks a cytoplasmic C-terminal helix and exhibits distinct microswitch structural features including a special N^2.50-D^7.49 pair and a hydrophobic Y^6.51-Y^6.52-W^6.48-F^6.44 motif in TM6 critical for signal transmission.

## Publications

### doi/10.1038##s41467-020-19109-w

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7br3">7BR3</a></td>
      <td>2.8</td>
      <td></td>
      <td>Engineered construct: ICL3 (residues 243-256) replaced with thermostable Pyrococcus abyssi glycogen synthase (PGS) domain. Mutation: P128^3.39K for improved homogeneity.</td>
      <td>Elagolix (NBI-56418)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Baculovirus/Sf9 insect cells
- **Construct**: HA signal sequence + FLAG tag at N-terminus; 10x His tag at C-terminus. ICL3 replaced with PGS domain. Mutation: P128^3.39K.

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
      <td>Cell harvest</td>
      <td>Sf9 insect cells infected with baculovirus; harvested 48 h post-infection</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Homogenization and <a href="/xray-mp-wiki/methods/purification/ultracentrifugation/">ultracentrifugation</a></td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> with <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Nickel <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC</a> for <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His-tag</a> capture</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>/<a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/) buffer</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>Concentrated with elagolix for crystallization</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>GnRH1R-<a href="/xray-mp-wiki/reagents/protein-tags/pgs-fusion/">PGS</a>-elagolix complex</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Data collected at Shanghai Synchrotron Radiation Facility (SSRF) BL17U. Structure solved by molecular replacement using <a href="/xray-mp-wiki/reagents/protein-tags/pgs-fusion/">PGS</a> domain as search model.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7br3">7BR3</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">DYKDDDDAMANSASPEQNQNHCSAI</span><span class="topo-inside">NNSIPLMQGNLPTLTLSGKI</span><span class="topo-membrane">RVTVTFFLFLLSATFNASFLLKLQK</span><span class="topo-outside">WTQ</span><span class="topo-unknown">KKEKGKKL</span><span class="topo-outside">SRMK</span><span class="topo-membrane">LLLKHLTLANLLETLIVMPLDGMW</span><span class="topo-inside">NITVQWYAGEL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LCK</span><span class="topo-membrane">VLSYLKLFSMYAKAFMMVVISLD</span><span class="topo-outside">RSLAIT</span><span class="topo-unknown">RPLALKS</span><span class="topo-outside">NSKV</span><span class="topo-membrane">GQSMVGLAWILSSVFAGPQL</span><span class="topo-inside">YIFRMIHL</span><span class="topo-unknown">ADSSGQTK</span><span class="topo-inside">VFSQCVTHCSFSQWWH</span><span class="topo-membrane">QAFYNFFTFSCLFIIPLFIMLICNA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">KIIFTLTRVLGIDCSFWNESYLTGSRDERKKSLLSKFGMDEGVTFMFIGRFDRGQKGVDVLLKAIEILSSKKEFQEMRFIIIGKGDPELEGWARSLEEKHGNVKVITEMLSREFVRELYG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">SVDFVIIPSYFEPFGLVALEAMCLGAIPIASAVGGLRDIITNETGILVKAGDPGELANAILKALELSRSDLSKFRENCKKRAMSFSNIPRARLKTLKM</span><span class="topo-membrane">TVAFATSFTVCWTPYYVLGIWY</span></span>
<span class="topo-ruler">       490       500       510       520        </span>
<span class="topo-line"><span class="topo-membrane">WF</span><span class="topo-inside">DPEMLNRL</span><span class="topo-membrane">SDPVNHFFFLFAFLNPCFDPLIYGY</span><span class="topo-outside">FSL</span><span class="topo-unknown">HHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>25</td>
      <td>-7</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>45</td>
      <td>18</td>
      <td>37</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>70</td>
      <td>38</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>73</td>
      <td>63</td>
      <td>65</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>81</td>
      <td>66</td>
      <td>73</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>82</td>
      <td>85</td>
      <td>74</td>
      <td>77</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>109</td>
      <td>78</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>110</td>
      <td>123</td>
      <td>102</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>146</td>
      <td>116</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>147</td>
      <td>152</td>
      <td>139</td>
      <td>144</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>153</td>
      <td>159</td>
      <td>145</td>
      <td>151</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>160</td>
      <td>163</td>
      <td>152</td>
      <td>155</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>164</td>
      <td>183</td>
      <td>156</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>184</td>
      <td>191</td>
      <td>176</td>
      <td>183</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>192</td>
      <td>199</td>
      <td>184</td>
      <td>191</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>200</td>
      <td>215</td>
      <td>192</td>
      <td>207</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>216</td>
      <td>240</td>
      <td>208</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>241</td>
      <td>250</td>
      <td>233</td>
      <td>242</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>446</td>
      <td>1001</td>
      <td>1196</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>447</td>
      <td>458</td>
      <td>257</td>
      <td>268</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>459</td>
      <td>482</td>
      <td>269</td>
      <td>292</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>483</td>
      <td>490</td>
      <td>293</td>
      <td>300</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>491</td>
      <td>515</td>
      <td>301</td>
      <td>325</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>516</td>
      <td>518</td>
      <td>326</td>
      <td>328</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>519</td>
      <td>528</td>
      <td>329</td>
      <td>338</td>
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

### Unusual N-terminus co-occupancy of orthosteric pocket

The N-terminus of GnRH1R inserts into the enlarged orthosteric binding pocket and co-occupies it together with elagolix. Residues L23 and M24 of the N-terminus pack alongside the ligand. The N-terminus is not involved in agonist GnRH binding but participates in small-molecule antagonist binding. The M24A mutation caused almost complete loss of elagolix inhibition of GnRH-induced response.

### Shallow antagonist binding site

Unlike other beta-branch GPCRs where ligands extend deeply into the orthosteric pocket and contact the toggle switch W^6.48, elagolix sits close to the top of the classical pocket and contacts Y283^6.51. Y283^6.51 together with Y284^6.52 and M125^3.36 form the bottom wall of the orthosteric pocket, decreasing ligand-binding cavity depth and blocking access to the toggle switch area. This shallow binding mode was further validated by docking of relugolix and sufugolix.

### Distinct microswitch features

GnRH1R lacks the conserved D^2.50 (replaced by N^2.50) and lacks a cytoplasmic C-terminal helix. The N^2.50-D^7.49 pair forms direct polar interactions and is critical for receptor activation. The hydrophobic Y^6.51-Y^6.52-W^6.48-F^6.44 motif in TM6 is critical for signal transmission upon extracellular stimuli. The Y283^6.51, Y284^6.52, and W280^6.48 residues greatly contribute to GnRH1R activation.


## Cross-References

- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr/">GPCR</a> — GnRH1R is a class A GPCR
