---
title: "AtTPC1 - Arabidopsis thaliana Two-pore Channel 1"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein]
sources: [doi/10.1073##pnas.1616191114]
verified: agent
uniprot_id: Q94KI8
---

# AtTPC1 - Arabidopsis thaliana Two-pore Channel 1

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q94KI8">UniProt: Q94KI8</a>

<span class="expr-badge">Arabidopsis thaliana</span>

## Overview

AtTPC1 (Arabidopsis thaliana Two-pore Channel 1) is a plant vacuolar cation channel belonging to the two-pore channel (TPC) family. Each TPC subunit contains two homologous Shaker-like six-transmembrane (6-TM) domains and functions as a homodimer. AtTPC1 is permeable to various cations with a relative permeability sequence of Ca2+ > Na+ ≈ Li+ ≈ K+ > Rb+ > Cs+. It is selective for Ca2+ over Na+ (PCa/PNa ~5) but nonselective among monovalent cations. Structural studies guided the conversion of AtTPC1 to a Na+-selective channel by mimicking the selectivity filter of human TPC2, revealing key residues (Val/Asn pair in filter II) that define Na+ selectivity.

## Publications

### doi/10.1073##pnas.1616191114

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5tua">5TUA</a></td>
      <td></td>
      <td></td>
      <td>At2HsTPC2 mutant (AtTPC1 with S265A, M629V, G630N mutations in the selectivity filter to mimic HsTPC2)</td>
      <td>Na+, Rb+, or Cs+ (soaked)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293 cells
- **Construct**: Full-length AtTPC1 and mutants including AtTPC1ΔCai (D240A/D454A/E528A for Ca2+ current measurements), and At2HsTPC2 (S265A/M629V/G630N for structural studies)
- **Notes**: AtTPC1 mutants were overexpressed in HEK293 [Baculovirus Expression System](/xray-mp-wiki/methods/expression-systems/baculovirus-expression-system/) for [Solid Supported Membrane Electrophysiology](/xray-mp-wiki/methods/quality-assessment/solid-supported-membrane-electrophysiology/); At2HsTPC2 was expressed and purified for X-ray crystallography

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
      <td>purification</td>
      <td>Detailed in SI Materials and Methods</td>
      <td>—</td>
      <td></td>
      <td>purification details for At2HsTPC2 used for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Not specified in main text</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>At2HsTPC2</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals were soaked with Rb+ or Cs+ for <a href="/xray-mp-wiki/methods/structure-determination/single-wavelength-anomalous-diffraction/">SAD phasing</a> experiments</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5tua">5TUA</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDPLIGRDSLGGGGTDRVRRSEAITHGTPF</span><span class="topo-inside">QKAAALVDLAEDGIGLPVEILD</span><span class="topo-unknown">QSS</span><span class="topo-inside">FGESARYYFIFTRLDLIWSL</span><span class="topo-membrane">NYFALLFLNFFEQPLWCEK</span><span class="topo-outside">NPKPSCKDRDYYYLGEL</span><span class="topo-membrane">PYLTNAES</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IIYEVITLAILLVHT</span><span class="topo-inside">FFPISYEGSRIFWTSRLNLV</span><span class="topo-membrane">KVACVVILFVDVLVDFLY</span><span class="topo-unknown">LSPLAFDFLP</span><span class="topo-outside">F</span><span class="topo-membrane">RIAPYVRVIIFILSI</span><span class="topo-inside">RELRDTLVLLSGML</span><span class="topo-membrane">GTYLNILALWMLFLLFASWIAFVM</span><span class="topo-outside">FED</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TQQGLTVFTSYGAT</span><span class="topo-unknown">LYQMFILFTTANNP</span><span class="topo-outside">DVWIPAYKSSRW</span><span class="topo-membrane">SSVFFVLYVLIGVYFVTNLILAVV</span><span class="topo-inside">YDSFKEQLAKQVSGMDQMKRRMLEKAFGLIDSDKNGEIDKNQCIKLFEQLTNYRTL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PKISKEEFGLIFDELDDTRDFKINKDEFADLCQAIALRFQKEEVP</span><span class="topo-unknown">SLFEHFP</span><span class="topo-inside">QIYHSALSQQLRAFVRSPNFGYAISF</span><span class="topo-membrane">ILIINFIAVVVETTLDIE</span><span class="topo-outside">ESS</span><span class="topo-membrane">AQKPWQVAEFVFGWIYVL</span><span class="topo-inside">EMA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">LKIYTYGFENYWREGANRF</span><span class="topo-membrane">DFLVTWVIVIGETATFITP</span><span class="topo-unknown">DENTF</span><span class="topo-outside">F</span><span class="topo-membrane">SNGEWIRYLLLARMLRLI</span><span class="topo-inside">RLLMNVQRYRAFIATFITLIPSL</span><span class="topo-membrane">MPYLGTIFCVLCIYCSIGVQV</span><span class="topo-outside">FGGL</span><span class="topo-unknown">VNA</span><span class="topo-outside">GNKKLFE</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">TELAEDDYLLFNFND</span><span class="topo-unknown">YPNGMVTLFNLLVVNNWQ</span><span class="topo-outside">VWMESYKDLTGTWW</span><span class="topo-membrane">SITYFVSFYVITILLLLNLVVA</span><span class="topo-inside">FVLEAFFTELDLEEEEK</span><span class="topo-unknown">CQGQDSQEKRNRRRSAGSKSRSQRVDTLLHHMLG</span></span>
<span class="topo-ruler">       730         </span>
<span class="topo-line"><span class="topo-unknown">DELSKPECSTSDTSTAGLV</span></span>
<details class="topo-details"><summary>Topology coordinates (39 regions)</summary>
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
      <td>31</td>
      <td>1</td>
      <td>31</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>32</td>
      <td>53</td>
      <td>32</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>54</td>
      <td>56</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>57</td>
      <td>76</td>
      <td>57</td>
      <td>76</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>95</td>
      <td>77</td>
      <td>95</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>96</td>
      <td>112</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>113</td>
      <td>135</td>
      <td>113</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>155</td>
      <td>136</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>156</td>
      <td>173</td>
      <td>156</td>
      <td>173</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>174</td>
      <td>183</td>
      <td>174</td>
      <td>183</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>184</td>
      <td>184</td>
      <td>184</td>
      <td>184</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>199</td>
      <td>185</td>
      <td>199</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>213</td>
      <td>200</td>
      <td>213</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>214</td>
      <td>237</td>
      <td>214</td>
      <td>237</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>238</td>
      <td>254</td>
      <td>238</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>268</td>
      <td>255</td>
      <td>268</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>269</td>
      <td>280</td>
      <td>269</td>
      <td>280</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>281</td>
      <td>304</td>
      <td>281</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>305</td>
      <td>405</td>
      <td>305</td>
      <td>405</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>412</td>
      <td>406</td>
      <td>412</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>413</td>
      <td>438</td>
      <td>413</td>
      <td>438</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>439</td>
      <td>456</td>
      <td>439</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>459</td>
      <td>457</td>
      <td>459</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>460</td>
      <td>477</td>
      <td>460</td>
      <td>477</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>478</td>
      <td>499</td>
      <td>478</td>
      <td>499</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>500</td>
      <td>518</td>
      <td>500</td>
      <td>518</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>519</td>
      <td>523</td>
      <td>519</td>
      <td>523</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>524</td>
      <td>524</td>
      <td>524</td>
      <td>524</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>525</td>
      <td>542</td>
      <td>525</td>
      <td>542</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>543</td>
      <td>565</td>
      <td>543</td>
      <td>565</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>566</td>
      <td>586</td>
      <td>566</td>
      <td>586</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>587</td>
      <td>590</td>
      <td>587</td>
      <td>590</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>591</td>
      <td>593</td>
      <td>591</td>
      <td>593</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>594</td>
      <td>615</td>
      <td>594</td>
      <td>615</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>616</td>
      <td>633</td>
      <td>616</td>
      <td>633</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>634</td>
      <td>647</td>
      <td>634</td>
      <td>647</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>648</td>
      <td>669</td>
      <td>648</td>
      <td>669</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>670</td>
      <td>686</td>
      <td>670</td>
      <td>686</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>687</td>
      <td>739</td>
      <td>687</td>
      <td>739</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5tua">5TUA</a> — Chain B (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MEDPLIGRDSLGGGGTDRVRRSEAITHGTPF</span><span class="topo-inside">QKAAALVDLAEDGIGLPVEILD</span><span class="topo-unknown">QSS</span><span class="topo-inside">FGESARYYFIFTRLDLI</span><span class="topo-membrane">WSLNYFALLFLNFFEQPLW</span><span class="topo-outside">CEKNPKPSCKDRDYYYLGELPYLTNAE</span><span class="topo-membrane">S</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">IIYEVITLAILLVHTF</span><span class="topo-inside">FPISYEGSRIFWTSRLNL</span><span class="topo-membrane">VKVACVVILFVDVLVDFL</span><span class="topo-outside">Y</span><span class="topo-unknown">LSPLAFDFLP</span><span class="topo-outside">F</span><span class="topo-membrane">RIAPYVRVIIFILSI</span><span class="topo-inside">RELRDTLVLLSGMLGTY</span><span class="topo-membrane">LNILALWMLFLLFASWIAFVMFE</span><span class="topo-outside">D</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TQQGLTVFTS</span><span class="topo-unknown">YGATLYQMFILFTTANNP</span><span class="topo-outside">DVWIPAYKSSR</span><span class="topo-membrane">WSSVFFVLYVLIGVYFVTNLILA</span><span class="topo-inside">VVYDSFKEQLAKQVSGMDQMKRRMLEKAFGLIDSDKNGEIDKNQCIKLFEQLTNYRTL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PKISKEEFGLIFDELDDTRDFKINKDEFADLCQAIALRFQKEEVP</span><span class="topo-unknown">SLFEHFP</span><span class="topo-inside">QIYHSALSQQLRAFVRSPNFGY</span><span class="topo-membrane">AISFILIINFIAVVVETT</span><span class="topo-outside">LDIEESSAQKP</span><span class="topo-membrane">WQVAEFVFGWIYVLEMA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">LKI</span><span class="topo-inside">YTYGFENYWREG</span><span class="topo-membrane">ANRFDFLVTWVIVIGETATFI</span><span class="topo-outside">TP</span><span class="topo-unknown">DENTF</span><span class="topo-outside">FSNG</span><span class="topo-membrane">EWIRYLLLARMLRLIRLL</span><span class="topo-inside">MNVQRYRAFIATFITL</span><span class="topo-membrane">IPSLMPYLGTIFCVLCIYCSIGVQV</span><span class="topo-outside">FGGL</span><span class="topo-unknown">VNA</span><span class="topo-outside">GNKKLFE</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">TELAEDDYLLFNFNDY</span><span class="topo-unknown">PNGMVTLFNLLVVNNWQ</span><span class="topo-outside">VWMESYKDLTGTW</span><span class="topo-membrane">WSITYFVSFYVITILLLLNLVVAFV</span><span class="topo-inside">LEAFFTELDLEEEEK</span><span class="topo-unknown">CQGQDSQEKRNRRRSAGSKSRSQRVDTLLHHMLG</span></span>
<span class="topo-ruler">       730         </span>
<span class="topo-line"><span class="topo-unknown">DELSKPECSTSDTSTAGLV</span></span>
<details class="topo-details"><summary>Topology coordinates (41 regions)</summary>
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
      <td>31</td>
      <td>1</td>
      <td>31</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>32</td>
      <td>53</td>
      <td>32</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>56</td>
      <td>54</td>
      <td>56</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>57</td>
      <td>73</td>
      <td>57</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>92</td>
      <td>74</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>119</td>
      <td>93</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>120</td>
      <td>136</td>
      <td>120</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>154</td>
      <td>137</td>
      <td>154</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>172</td>
      <td>155</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>173</td>
      <td>173</td>
      <td>173</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>183</td>
      <td>174</td>
      <td>183</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>184</td>
      <td>184</td>
      <td>184</td>
      <td>184</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>185</td>
      <td>199</td>
      <td>185</td>
      <td>199</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>216</td>
      <td>200</td>
      <td>216</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>217</td>
      <td>239</td>
      <td>217</td>
      <td>239</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>240</td>
      <td>250</td>
      <td>240</td>
      <td>250</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>268</td>
      <td>251</td>
      <td>268</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>269</td>
      <td>279</td>
      <td>269</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>302</td>
      <td>280</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>303</td>
      <td>405</td>
      <td>303</td>
      <td>405</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>406</td>
      <td>412</td>
      <td>406</td>
      <td>412</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>413</td>
      <td>434</td>
      <td>413</td>
      <td>434</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>435</td>
      <td>452</td>
      <td>435</td>
      <td>452</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>453</td>
      <td>463</td>
      <td>453</td>
      <td>463</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>464</td>
      <td>483</td>
      <td>464</td>
      <td>483</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>484</td>
      <td>495</td>
      <td>484</td>
      <td>495</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>496</td>
      <td>516</td>
      <td>496</td>
      <td>516</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>517</td>
      <td>518</td>
      <td>517</td>
      <td>518</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>519</td>
      <td>523</td>
      <td>519</td>
      <td>523</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>524</td>
      <td>527</td>
      <td>524</td>
      <td>527</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>528</td>
      <td>545</td>
      <td>528</td>
      <td>545</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>546</td>
      <td>561</td>
      <td>546</td>
      <td>561</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>562</td>
      <td>586</td>
      <td>562</td>
      <td>586</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>587</td>
      <td>590</td>
      <td>587</td>
      <td>590</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>591</td>
      <td>593</td>
      <td>591</td>
      <td>593</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>594</td>
      <td>616</td>
      <td>594</td>
      <td>616</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>617</td>
      <td>633</td>
      <td>617</td>
      <td>633</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>634</td>
      <td>646</td>
      <td>634</td>
      <td>646</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>647</td>
      <td>671</td>
      <td>647</td>
      <td>671</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>672</td>
      <td>686</td>
      <td>672</td>
      <td>686</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>687</td>
      <td>739</td>
      <td>687</td>
      <td>739</td>
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

### Filter II Val/Asn pair defines Na+ selectivity in TPC channels

Systematic mutagenesis and [Solid Supported Membrane Electrophysiology](/xray-mp-wiki/methods/quality-assessment/solid-supported-membrane-electrophysiology/) identified that a Val/Asn pair
in filter II of TPC channels is essential for Na+ [Claudin Paracellular Ion Selectivity](/xray-mp-wiki/concepts/miscellaneous/claudin-paracellular-ion-selectivity/).
AtTPC1 residues Met629→Val and Gly630→Asn (the At2HsTPC2 mutant)
converted the nonselective [VIT1](/xray-mp-wiki/proteins/pumps-atpases/vit1/) channel to a Na+-selective channel with
PNa/PK of 41.1. The structure of At2HsTPC2 (PDB 5TUA) revealed
that Asn630 creates a constriction in the ion channel (~4.8 A) and
coordinates Na+ through its side chain carbonyl groups, while the Asn630/Asn631
pair creates steric hindrance for larger monovalent cations (Rb+, Cs+).

### Structural basis of TPC ion selectivity

Comparison of AtTPC1 and At2HsTPC2 filter structures shows that the
M629V mutation causes local rearrangements in the filter,
stabilizing a narrow conformation. The Asn630 side chain is
coordinated by [Proton Wire](/xray-mp-wiki/concepts/transport-mechanisms/proton-wire/) with backbone carbonyls of Thr264 and Ala265
from filter I. The resulting filter explains how mammalian TPCs
achieve Na+ Selectivity while [VIT1](/xray-mp-wiki/proteins/pumps-atpases/vit1/) TPC1 remains nonselective.


## Cross-References

- <a href="/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase/">Bovine F1-ATPase (azide-inhibited form)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/slc-transporters/hace2/">Human Angiotensin-Converting Enzyme 2 (hACE2)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/gpcr/ntsr1-lf/">NTSR1-LF Mutant</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/pumps-atpases/bovine-f1-atpase-stator-complex/">Bovine Mitochondrial F1-ATPase-Stator Complex (Membrane Extrinsic Region)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/other-ion-channels/glua2-ampa-receptor/">GluA2 AMPA Receptor — Structures with Antagonists, NAMs, and Allosteric Modulators</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/proteins/pumps-atpases/vit1/">Plant Vacuolar Iron Transporter 1 (VIT1)</a> — Related protein structure; referenced in text
- <a href="/xray-mp-wiki/concepts/miscellaneous/claudin-paracellular-ion-selectivity/">Claudin-Mediated Paracellular Ion Selectivity</a> — Related concept; referenced in text
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/">Membrane Mimetics and Structural Biology</a> — Related concept; referenced in text
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/proton-wire/">Proton Wire (Chain of Hydrogen Bonds)</a> — Related concept; referenced in text
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/oxygen-ladder-selectivity-filter/">Oxygen Ladder in Selectivity Filters</a> — Related concept; referenced in text
