---
title: "IPCT/DIPPS from Archaeoglobus fulgidus (Bifunctional CTP:Inositol-1-Phosphate Cytidylyltransferase/CDP-Inositol:Inositol-1-Phosphate Phosphotransferase)"
created: 2026-06-05
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms5169]
verified: agent
uniprot_id: O29976
---

# IPCT/DIPPS from Archaeoglobus fulgidus (Bifunctional CTP:Inositol-1-Phosphate Cytidylyltransferase/CDP-Inositol:Inositol-1-Phosphate Phosphotransferase)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O29976">UniProt: O29976</a>

<span class="expr-badge">Archaeoglobus fulgidus</span>

## Overview

IPCT/DIPPS is a bifunctional membrane enzyme from the hyperthermophilic archaeon Archaeoglobus fulgidus that catalyses two consecutive steps of di-myo-inositol-1,3-phosphate (DIP) biosynthesis. The N-terminal IPCT domain (CTP:L-myo-inositol-1-phosphate cytidylyltransferase) activates inositol-1-phosphate to CDP-inositol, while the C-terminal DIPPS domain (CDP-L-myo-inositol:myo-inositolphosphotransferase, also called DIPP synthase) displaces CMP from CDP-inositol by a second inositol-1-phosphate to form DIPP-phosphate (DIPP). The DIPPS domain is a membrane-embedded CDP-alcohol phosphatidyltransferase with 6 transmembrane helices that dimerizes through its domains. The catalytic mechanism follows an SN2-like displacement with Mg2+ coordinated by four conserved aspartate residues (Asp357, Asp360, Asp378, Asp382) at the membrane interface.

## Publications

### doi/10.1038##ncomms5169

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4mnd">4MND</a></td>
      <td>2.65 A</td>
      <td>P2;2,2</td>
      <td>IPCT/DIPPS bifunctional enzyme from Archaeoglobus fulgidus (AF0263); N-terminal Strept tag II, C-terminal His10 tag; DIPPS domain comprises 6 transmembrane helices (TM1-TM6)</td>
      <td>Mg2+ (1 ion), 4 lipid fragments, CTP, inositol-1-phosphate, CDP-inositol, DIPP</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43 DE3
- **Construct**: A. fulgidus AF0263 gene cloned into PET52b(+) expression vector (Novagen) with N-terminal Strept tag II and C-terminal His10 tag; induced with 0.5 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at OD600=1.0, grown at 30 C for 6 h

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
      <td>Cell growth and lysis</td>
      <td>Fermentation and cell disruption</td>
      <td>--</td>
      <td>terrific broth medium; lysis buffer: 50 mM sodium <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate</a>, 200 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 100 mM <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 0.5 mM PMSF, 2 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a>, SIGMAFAST protease inhibitor cocktail; pH 7.5 + --</td>
      <td>Cells cultivated at 37 C in 30 L fermentor, pH 7.4; induced with 0.5 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> at OD600=1.0; temperature lowered to 30 C; harvested 6 h post-induction; disrupted by constant flow cell disrutor; membranes isolated by ultracentrifugation at 200,000 g for 2 h</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>2% Triton X-100, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1 M NaCl, 50 mM phosphate buffer, 50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 100 mM <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a>, 2 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a>, 1 mM MgCl2; final pH 7.4 at 277 K + 2% Triton X-100</td>
      <td>Solubilized for 2 h at 277 K; insoluble fraction removed by centrifugation at 100,000 g for 1 h</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>HisTrap HP column (GE Healthcare)</td>
      <td>Wash buffer A: 0.1% Triton X-100, 50 mM phosphate buffer, 5 mM MgCl2, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.1 M NaCl, pH 7.5; Elution buffer B: 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 0.1% Triton X-100</td>
      <td>Loaded supernatant washed with buffer A, eluted with buffer B containing 500 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hilide-crystallization/">HiLiDe Crystallization</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified IPCT/DIPPS in detergent</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td><a href="/xray-mp-wiki/reagents/additives/peg200/">PEG200</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized using HiLiDe method in detergent conditions</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified IPCT/DIPPS</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystallized in meso using <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> method</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>lcp</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4mnd">4MND</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MASWSHPQFEKGALEVLFQGPGMINVDGEYLKIFAGRIK</span><span class="topo-inside">LMKAVILAAGLG</span><span class="topo-unknown">TRL</span><span class="topo-inside">GGVPKPLVRVGGCEIILRTMKLLSPHVSEFIIVASRYADDIDAFLKDKGFNYKIVRHDRPEKGNGY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">SLLVAKNHVEDRFILTMGDHVYSQQFIEKAVRGEGVIADREPRFVDIGEATKIRVEDGRVAKIGKDLREFDCVDTGFFVLDDSIFEHAEKLRDREEIPLSEIVKLARLPVTYVDGELWMD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">VDTKEDVRRANRALVSAAV</span><span class="topo-unknown">KGS</span><span class="topo-inside">GDGFISRKI</span><span class="topo-unknown">NRKISTRISAAI</span><span class="topo-inside">VNKVNPNQMT</span><span class="topo-membrane">LISFLVGAFSALASF</span><span class="topo-outside">FSI</span><span class="topo-membrane">PLAGLLYQFSSILD</span><span class="topo-inside">GCDGEIARASLKMSKKGGYVD</span><span class="topo-membrane">SILDRFVDFLFLAI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470         </span>
<span class="topo-line"><span class="topo-membrane">IAL</span><span class="topo-outside">LYPKTA</span><span class="topo-membrane">TVAMFAIFGSVMVSYT</span><span class="topo-inside">SEKYKAEFGESI</span><span class="topo-unknown">FGKF</span><span class="topo-inside">RVLNY</span><span class="topo-membrane">IPGKRDERIFLIMIFCLL</span><span class="topo-outside">SAISLQWI</span><span class="topo-membrane">FWMFLFVAAISLTRVVVTLL</span><span class="topo-inside">AVLVS</span><span class="topo-unknown">KELALVPRGSSAHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>39</td>
      <td>33</td>
      <td>71</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>40</td>
      <td>51</td>
      <td>72</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>54</td>
      <td>84</td>
      <td>86</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>259</td>
      <td>87</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>262</td>
      <td>292</td>
      <td>294</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>263</td>
      <td>271</td>
      <td>295</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>283</td>
      <td>304</td>
      <td>315</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>284</td>
      <td>293</td>
      <td>316</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>308</td>
      <td>326</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>309</td>
      <td>311</td>
      <td>341</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>325</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>326</td>
      <td>346</td>
      <td>358</td>
      <td>378</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>363</td>
      <td>379</td>
      <td>395</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>369</td>
      <td>396</td>
      <td>401</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>370</td>
      <td>385</td>
      <td>402</td>
      <td>417</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>386</td>
      <td>397</td>
      <td>418</td>
      <td>429</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>401</td>
      <td>430</td>
      <td>433</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>402</td>
      <td>406</td>
      <td>434</td>
      <td>438</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>424</td>
      <td>439</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>425</td>
      <td>432</td>
      <td>457</td>
      <td>464</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>433</td>
      <td>452</td>
      <td>465</td>
      <td>484</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>453</td>
      <td>457</td>
      <td>485</td>
      <td>489</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>479</td>
      <td>490</td>
      <td>511</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4mnd">4MND</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MASWSHPQFEKGALEVLFQGPGMINVDGEYLKIFAGRIK</span><span class="topo-inside">LMKAVILAAGLG</span><span class="topo-unknown">TRL</span><span class="topo-inside">GGVPKPLVRVGGCEIILRTMKLLSPHVSEFIIVASRYADDIDAFLKDKGFNYKIVRHDRPEKGNGY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">SLLVAKNHVEDRFILTMGDHVYSQQFIEKAVRGEGVIADREPRFVDIGEATKIRVEDGRVAKIGKDLREFDCVDTGFFVLDDSIFEHAEKLRDREEIPLSEIVKLARLPVTYVDGELWMD</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">VDTKEDVRRANRALVSAAV</span><span class="topo-unknown">KGS</span><span class="topo-inside">GDGFISRKI</span><span class="topo-unknown">NRKISTRISAAI</span><span class="topo-inside">VNKVNPNQMT</span><span class="topo-membrane">LISFLVGAFSALASF</span><span class="topo-outside">FSI</span><span class="topo-membrane">PLAGLLYQFSSILD</span><span class="topo-inside">GCDGEIARASLKMSKKGGYVD</span><span class="topo-membrane">SILDRFVDFLFLAI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470         </span>
<span class="topo-line"><span class="topo-membrane">IAL</span><span class="topo-outside">LYPKTA</span><span class="topo-membrane">TVAMFAIFGSVMVSYT</span><span class="topo-inside">SEKYKAEFGESI</span><span class="topo-unknown">FGKF</span><span class="topo-inside">RVLNY</span><span class="topo-membrane">IPGKRDERIFLIMIFCLL</span><span class="topo-outside">SAISLQWI</span><span class="topo-membrane">FWMFLFVAAISLTRVVVTLL</span><span class="topo-inside">AVLVS</span><span class="topo-unknown">KELALVPRGSSAHHHHHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>39</td>
      <td>33</td>
      <td>71</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>40</td>
      <td>51</td>
      <td>72</td>
      <td>83</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>54</td>
      <td>84</td>
      <td>86</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>259</td>
      <td>87</td>
      <td>291</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>260</td>
      <td>262</td>
      <td>292</td>
      <td>294</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>263</td>
      <td>271</td>
      <td>295</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>272</td>
      <td>283</td>
      <td>304</td>
      <td>315</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>284</td>
      <td>293</td>
      <td>316</td>
      <td>325</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>308</td>
      <td>326</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>309</td>
      <td>311</td>
      <td>341</td>
      <td>343</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>325</td>
      <td>344</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>326</td>
      <td>346</td>
      <td>358</td>
      <td>378</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>347</td>
      <td>363</td>
      <td>379</td>
      <td>395</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>364</td>
      <td>369</td>
      <td>396</td>
      <td>401</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>370</td>
      <td>385</td>
      <td>402</td>
      <td>417</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>386</td>
      <td>397</td>
      <td>418</td>
      <td>429</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>401</td>
      <td>430</td>
      <td>433</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>402</td>
      <td>406</td>
      <td>434</td>
      <td>438</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>407</td>
      <td>424</td>
      <td>439</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>425</td>
      <td>432</td>
      <td>457</td>
      <td>464</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>433</td>
      <td>452</td>
      <td>465</td>
      <td>484</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>453</td>
      <td>457</td>
      <td>485</td>
      <td>489</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>458</td>
      <td>479</td>
      <td>490</td>
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

### Bifunctional enzyme architecture with cytoplasmic and membrane domains

IPCT/DIPPS is a single polypeptide comprising two distinct domains. The N-terminal IPCT domain is cytoplasmic and catalyses the activation of inositol-1-phosphate to CDP-inositol using CTP as a cofactor. The C-terminal DIPPS domain is a membrane-embedded protein with 6 transmembrane helices (TM1-TM6) that catalyses the phosphotransfer reaction. The two domains dimerize through the DIPPS domains, with each monomer contributing 6 transmembrane helices. The interface between IPCT and DIPPS domains is relatively weak (479 A^2 interface area, -7.3 kcal/mol solvation free energy). The entries to the active sites of the two domains are oriented in different directions, suggesting no direct cross-talk between domains.

### Magnesium-dependent catalytic mechanism at the membrane interface

The DIPPS active site cavity is hydrophilic, widely open to the cytoplasm, and located at the membrane interface. A magnesium ion is coordinated by three conserved aspartate residues (Asp357, Asp360, Asp378) from helices TM2 and TM3, with a fourth conserved aspartate (Asp382) nearby. Mg2+ is expected to decrease the pKa of surrounding aspartate residues, enabling them to function as base catalysts. The catalytic mechanism is proposed to be a single displacement SN2-like reaction where Asp357/Asp382 promote direct nucleophilic attack of the hydroxyl group (C3) of inositol-1-phosphate on the beta-phosphoryl of CDP-inositol, forming DIPP and CMP. Magnesium is essential for enzymatic activity.

### Substrate binding pockets and conserved sequence motif

Three substrate binding pockets were identified by HOLLOW analysis. Pocket 1 (cytidine binding) is flanked by the TM2-TM3 loop and lined by conserved residues Gly361, Ala364, Gly374 from the family consensus motif DG(x)2AR(x)7,8G(x)3D(x)3D. Pocket 2 (inositol-1-phosphate binding) is at the bottom of the hydrophilic cavity formed by Asn304, Arg305, Ser308, Ser354, Asp357, Arg443. Pocket 3 is non-conserved and unlikely to bind substrate. The conserved sequence pattern was proposed to be extended to D(x)2DG(x)2AR(x)7-12G(x)3D(x)3D to include the additional Asp357 (D1) residue.

### Structure-based mutagenesis validation

Site-directed mutagenesis validated functional importance of conserved residues. Mutations S308A and S308M (pocket 2) reduced or abolished activity by disrupting inositol-1-phosphate binding. Mutation S371P in the TM2-TM3 loop reduced activity by constraining loop flexibility. Mutations A364M and R365M (pocket 1) likely obstruct active site access or substrate capture. R443A abolished activity completely. These results confirm the proposed substrate binding model and catalytic mechanism, and agree with equivalent mutation studies in yeast CPT1, E. coli phosphatidylglycerophosphate synthase, and Sinorhizobium meliloti CPT.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/triton-x-100/">Triton X-100</a> — Nonionic detergent used for membrane solubilization of IPCT/DIPPS at 2%
- <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate Buffer</a> — Buffer component in lysis buffer (50 mM) and solubilization buffer (50 mM)
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer</a> — Buffer component in lysis buffer (50 mM sodium citrate)
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Stabilizer in lysis buffer (5%) and solubilization buffer (20%)
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride (NaCl)</a> — Salt in lysis buffer (200 mM) and solubilization buffer (1 M)
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Chelator in lysis buffer (1 mM)
- <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> — Osmoprotectant in lysis buffer (100 mM) and solubilization buffer (100 mM)
- <a href="/xray-mp-wiki/reagents/additives/peg200/">PEG200</a> — Crystallization precipitant in HiLiDe method
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride (MgCl2)</a> — Essential catalytic cofactor; present in solubilization buffer (1 mM) and purification wash buffer (5 mM)
- <a href="/xray-mp-wiki/reagents/additives/ptg/">Imidazole</a> — Component of solubilization buffer (50 mM) and elution buffer (500 mM) for His-tag purification
- <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">Beta-Mercaptoethanol</a> — Reducing agent in lysis buffer (2 mM) and solubilization buffer (2 mM)
- <a href="/xray-mp-wiki/reagents/additives/pmsf/">Phenylmethanesulfonylfluoride (PMSF)</a> — Protease inhibitor in lysis buffer (0.5 mM)
- <a href="/xray-mp-wiki/reagents/additives/isopropyl-beta-d-thiogalactoside/">Isopropyl beta-D-1-Thiogalactopyranoside (IPTG)</a> — Inducer for protein expression (0.5 mM)
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — HisTrap HP Ni-affinity column used for His-tagged IPCT/DIPPS purification
- <a href="/xray-mp-wiki/methods/crystallization/hilide-crystallization/">HiLiDe Crystallization</a> — Crystallization method used for IPCT/DIPPS in detergent conditions
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — In meso crystallization method used for IPCT/DIPPS
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement (MR)</a> — Structure determination method used for 4MND
- <a href="/xray-mp-wiki/concepts/protein-families/cdp-alcohol-phosphotransferase-family/">CDP-Alcohol Phosphotransferase Family</a> — IPCT/DIPPS DIPPS domain belongs to the CDP-alcohol phosphatidyltransferase family (CDP-OH_P_trans)
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/sn2-like-displacement-mechanism/">SN2-Like Displacement Mechanism</a> — Proposed catalytic mechanism for DIPPS domain of IPCT/DIPPS
