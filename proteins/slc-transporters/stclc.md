---
title: "StClC CIC Chloride Channel"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##415287a]
verified: false
---

# StClC CIC Chloride Channel

## Overview

StClC is a prokaryotic CIC chloride channel from Salmonella enterica serovar typhimurium whose X-ray crystal structure at 3.0 Å resolution, together with the related EcClC channel from Escherichia coli at 3.5 Å, revealed the molecular basis of anion selectivity in CIC chloride channels. The structure showed that CIC channels form homodimers with two independent pores, each pore formed by a separate subunit with an antiparallel transmembrane architecture. Each subunit is composed of two roughly repeated halves that span the membrane with opposite orientations, and the Cl- selectivity filter is defined by electrostatic interactions with alpha-helix dipoles and chemical coordination with main-chain amide nitrogen atoms and side-chain hydroxyl groups from Ser 107 and Tyr 445. The pore features a narrow selectivity filter near the membrane center with wider vestibules on both sides. A conserved glutamate residue (Glu 148) projects into the pore above the Cl- binding site and is proposed to act as a gate that must be displaced for Cl- conduction to occur. This landmark study established the physical and chemical principles underlying anion selectivity in the CIC channel family.


## Publications

### doi/10.1038##415287a

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1kpl">1KPL</a></td>
      <td>3.0 A</td>
      <td>P2(1)</td>
      <td>Full-length StClC from Salmonella enterica serovar typhimurium with C-terminal His tag</td>
      <td>Cl- ion bound in selectivity filter</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21 DE3
- **Construct**: StClC cloned into pET28b+ vector using NcoI and XhoI restriction sites with C-terminal His tag

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
      <td>Protein expression</td>
      <td>E. coli expression</td>
      <td>--</td>
      <td>-- + --</td>
      <td>StClC expressed in E. coli BL21 DE3 with C-terminal His tag</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion / heavy atom derivatization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified StClC in detergent</td>
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
      <td>Native data collected at BNL X25 beamline. Initial phases estimated from platinum derivatives. Four-fold <a href="/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/">NCS</a> averaging and phase extension to 3.0 Å using RAVE and DM. Solvent-flattened, averaged electron density maps used for model building. Crystal form: P2(1) space group.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1kpl">1KPL</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTDTSTFLAQQIVRLRRRDQIRRLLQRDK</span><span class="topo-outside">TPL</span><span class="topo-membrane">AILFMAAVVGTLTGLVGVAFEKAVSWVQ</span><span class="topo-inside">NMRIGALVQVADHAFLLWP</span><span class="topo-membrane">LAFILSALLAMVGYFLVRKFAP</span><span class="topo-outside">EAGGSGIPEIEGALEELR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">PVRW</span><span class="topo-membrane">WRVLPVKFIGGMGTLGAG</span><span class="topo-inside">M</span><span class="topo-membrane">VLGREGPTVQIGGNLG</span><span class="topo-outside">RMVLDVFRMRSAEARHTLLAT</span><span class="topo-unknown">GAAAGLSAAFNAPLAGILFII</span><span class="topo-outside">EEMRPQFRYNLIS</span><span class="topo-membrane">IKAVFTGVIMSSIVFRIFN</span><span class="topo-inside">GEAPIIE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">VGKLSDAPVNT</span><span class="topo-membrane">LWLYLILGIIFGVVGPVFNSLVLRTQDMFQ</span><span class="topo-outside">RFHGGEI</span><span class="topo-membrane">KKWVLMGGAIGGLCGILG</span><span class="topo-inside">LIEPAAAGGGFNLIPIAAAGNFSVGLLL</span><span class="topo-membrane">FIFITRVVTTLLCFSSG</span><span class="topo-outside">A</span><span class="topo-membrane">PGGIFAPM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470   </span>
<span class="topo-line"><span class="topo-membrane">LALGTLLG</span><span class="topo-inside">TAFGMAAAVLFPQYHLEAGTFAI</span><span class="topo-unknown">AGMGALMAASVRAPLTGIVLVLEMT</span><span class="topo-inside">DNYQL</span><span class="topo-membrane">ILPMIITCLGATLLAQFLGGK</span><span class="topo-outside">PLYSTILARTLAKQDAEQ</span><span class="topo-unknown">AEKNQNAPADENT</span></span>
<details class="topo-details"><summary>Topology coordinates (27 regions)</summary>
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
      <td>30</td>
      <td>1</td>
      <td>30</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>31</td>
      <td>33</td>
      <td>31</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>61</td>
      <td>34</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>80</td>
      <td>62</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>102</td>
      <td>81</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>124</td>
      <td>103</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>142</td>
      <td>125</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>159</td>
      <td>144</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>180</td>
      <td>160</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>201</td>
      <td>181</td>
      <td>201</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>202</td>
      <td>214</td>
      <td>202</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>233</td>
      <td>215</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>251</td>
      <td>234</td>
      <td>251</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>252</td>
      <td>281</td>
      <td>252</td>
      <td>281</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>282</td>
      <td>288</td>
      <td>282</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>306</td>
      <td>289</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>334</td>
      <td>307</td>
      <td>334</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>351</td>
      <td>335</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>352</td>
      <td>352</td>
      <td>352</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>368</td>
      <td>353</td>
      <td>368</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>369</td>
      <td>391</td>
      <td>369</td>
      <td>391</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>392</td>
      <td>416</td>
      <td>392</td>
      <td>416</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>442</td>
      <td>422</td>
      <td>442</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>443</td>
      <td>460</td>
      <td>443</td>
      <td>460</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>461</td>
      <td>473</td>
      <td>461</td>
      <td>473</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1kpl">1KPL</a> — Chain B (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MKTDTSTFLAQ</span><span class="topo-outside">QIVRLRRRDQIRRLLQRDKTPLAI</span><span class="topo-membrane">LFMAAVVGTLTGLVGVAFEKAVSWVQ</span><span class="topo-inside">NMRIGALVQVADHAFLLWP</span><span class="topo-membrane">LAFILSALLAMVGYFLVRKFAP</span><span class="topo-outside">EAGGSGIPEIEGALEELR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">PVRW</span><span class="topo-membrane">WRVLPVKFIGGMGTLGAG</span><span class="topo-inside">M</span><span class="topo-membrane">VLGREGPTVQIGGNLG</span><span class="topo-outside">RMVLDVFRMRSAEARHTLLAT</span><span class="topo-unknown">GAAAGLSAAFNAPLAGILFII</span><span class="topo-outside">EEMRPQFRYNLIS</span><span class="topo-membrane">IKAVFTGVIMSSIVFRIFN</span><span class="topo-inside">GEAPIIE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">VGKLSDAPV</span><span class="topo-membrane">NTLWLYLILGIIFGVVGPVFNSLVLRTQ</span><span class="topo-unknown">DMFQRFH</span><span class="topo-outside">GGEI</span><span class="topo-membrane">KKWVLMGGAIGGLCGILG</span><span class="topo-inside">LIEPAAAGGGFNLIPIAAAGNFSVGLLL</span><span class="topo-membrane">FIFITRVVTTLLCFSSG</span><span class="topo-outside">A</span><span class="topo-membrane">PGGIFAPM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470   </span>
<span class="topo-line"><span class="topo-membrane">LALGTLLG</span><span class="topo-unknown">TAFGMAAAVLF</span><span class="topo-inside">PQYHLEAGTFAI</span><span class="topo-unknown">AGMGALMAASVRAPLTGIVLVLEMT</span><span class="topo-inside">DNYQL</span><span class="topo-membrane">ILPMIITCLGATLLAQFLGGK</span><span class="topo-outside">PLYSTILARTLAKQDAEQAE</span><span class="topo-unknown">KNQNAPADENT</span></span>
<details class="topo-details"><summary>Topology coordinates (29 regions)</summary>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>12</td>
      <td>35</td>
      <td>12</td>
      <td>35</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>61</td>
      <td>36</td>
      <td>61</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>62</td>
      <td>80</td>
      <td>62</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>102</td>
      <td>81</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>124</td>
      <td>103</td>
      <td>124</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>142</td>
      <td>125</td>
      <td>142</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>143</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>144</td>
      <td>159</td>
      <td>144</td>
      <td>159</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>160</td>
      <td>180</td>
      <td>160</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>201</td>
      <td>181</td>
      <td>201</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>202</td>
      <td>214</td>
      <td>202</td>
      <td>214</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>233</td>
      <td>215</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>249</td>
      <td>234</td>
      <td>249</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>250</td>
      <td>277</td>
      <td>250</td>
      <td>277</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>278</td>
      <td>284</td>
      <td>278</td>
      <td>284</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>285</td>
      <td>288</td>
      <td>285</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>306</td>
      <td>289</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>334</td>
      <td>307</td>
      <td>334</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>351</td>
      <td>335</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>352</td>
      <td>352</td>
      <td>352</td>
      <td>352</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>353</td>
      <td>368</td>
      <td>353</td>
      <td>368</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>369</td>
      <td>379</td>
      <td>369</td>
      <td>379</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>380</td>
      <td>391</td>
      <td>380</td>
      <td>391</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>392</td>
      <td>416</td>
      <td>392</td>
      <td>416</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>417</td>
      <td>421</td>
      <td>417</td>
      <td>421</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>422</td>
      <td>442</td>
      <td>422</td>
      <td>442</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>443</td>
      <td>462</td>
      <td>443</td>
      <td>462</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>463</td>
      <td>473</td>
      <td>463</td>
      <td>473</td>
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

### Antiparallel architecture defines the CIC channel fold

Each CIC subunit is composed of two roughly repeated halves (helices A-I and J-R) that span the membrane with opposite orientations. This antiparallel architecture brings the N-termini of alpha-helices D, F, and N together near the membrane center to form an electrostatically favorable environment for anion binding. This architecture is distinct from the parallel barrel-stave architecture of K+ channels and represents a novel membrane protein fold that satisfies the constraints of placing helix dipoles at the selectivity filter while burying the opposite ends in the membrane.

### Cl- selectivity filter uses partial charges, not full charges

The Cl- ion is coordinated by main-chain amide nitrogen atoms from Ile 356 and Phe 357, and side-chain oxygen atoms from Ser 107 and Tyr 445. The favorable electrostatic environment arises from partial positive charges contributed by helix dipole interactions and contacts with main-chain and side-chain nitrogen and oxygen atoms. Unlike cation channels that use full positive charges, CIC channels use partial charges to stabilize Cl- while still permitting rapid ionic diffusion rates. A full positive charge would create too deep an energy well.

### Glutamate gate mechanism for Cl- conduction

A conserved glutamate residue (Glu 148) projects into the pore above the Cl- binding site, sandwiched between the positive ends of alpha-helices F and N. The selectivity filter effectively contains two anions: a Cl- ion at the inner site (closer to the intracellular vestibule) and a carboxylate anion (Glu 148) at the outer site (closer to the extracellular vestibule). For Cl- conduction to occur, the glutamate side chain must swing out of the way, allowing a Cl- ion to enter in its place. This provides a structural basis for the Cl- activation and gating properties observed in CIC channels.

### Double-barreled channel architecture

The CIC channel forms a homodimer with two identical pores, each formed by a separate subunit. The contact surface between subunits is extensive (~2,300 Å² within the membrane), consistent with CIC channels existing and functioning only as dimers. The two pores are separated by a large distance and by an electronegative (Cl--repulsive) region on the extracellular surface, consistent with the functional independence of the two pores observed in ClC-0 channels by single-channel analysis.

### Electrostatic funneling of Cl- ions

The vestibules leading to the selectivity filter on both sides of the membrane contain basic (positively charged) amino acids (e.g., Arg 147, Arg 451). The distribution of charges on the entire channel surface creates an electrostatic potential that funnels Cl- ions into the pore entryways. Poisson-Boltzmann calculations in 150 mM electrolyte confirm that the electrostatic surface potential around the pore openings attracts anions.


## Cross-References

- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/kcsa/">KcsA Potassium Channel</a> — Comparison of antiparallel (CIC) vs barrel-stave (KcsA) ion channel architectures
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/non-crystallographic-symmetry/">NCS</a> — Related biological concept
