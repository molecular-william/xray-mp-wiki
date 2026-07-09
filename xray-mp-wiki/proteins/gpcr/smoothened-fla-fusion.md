---
title: "SMO-FLA Fusion Construct (SMO-Flavodoxin)"
created: 2026-06-03
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##ncomms15383]
verified: regex
uniprot_id: P00323
---

# SMO-FLA Fusion Construct (SMO-Flavodoxin)

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P00323">UniProt: P00323</a>

## Overview

The SMO-FLA fusion construct is an engineered human [SMO](/xray-mp-wiki/proteins/gpcr/smoothened/) ([SMO](/xray-mp-wiki/proteins/gpcr/smoothened/)) receptor with Flavodoxin (FLA, 16 kDa) fused to the intracellular loop 3 (ICL3) between residues P434 and S443. This construct was designed to enhance crystallizability by providing a stable, well-folded crystallization chaperone in the intracellular region. The construct includes N- and C-terminal truncations and a single point mutation E194M in the hinge domain.


## Publications

### doi/10.1038##ncomms15383

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5v56">5V56</a></td>
      <td>2.90</td>
      <td>P21</td>
      <td>SMO-FLA fusion (residues 53-558 with E194M mutation, FLA fused to ICL3 at P434-S443, N-term HA-FLAG-10xHis-TEV, C-term 10xHis)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/tc114/">TC114 (SMO Ligand)</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5v57">5V57</a></td>
      <td>3.00</td>
      <td>P21</td>
      <td>SMO-FLA fusion (residues 53-558, FLA fused to ICL3 at P434-S443, N-term HA-FLAG-10xHis-TEV, C-term 10xHis, N-term further truncated by 5 residues for synchrotron)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/tc114/">TC114 (SMO Ligand)</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293F cells (human embryonic kidney 293F, suspended culture)
- **Construct**: SMO-FLA fusion: N-terminus residues 1-52 truncated, C-terminus residues 559-747 truncated, E194M point mutation in hinge domain. N-terminal fusion: HA signal sequence, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10xHis tag, TEV protease recognition site. Flavodoxin (FLA, 16 kDa) fused to ICL3 between P434 and S443 via overlapping PCR. C-terminal 10xHis tag.


**Purification:**

- **Expression system**: HEK293F cells
- **Expression construct**: SMO-FLA fusion (residues 53-558, E194M, FLA fused to ICL3)
- **Tag info**: HA signal, [FLAG Tag](/xray-mp-wiki/reagents/protein-tags/flag-tag/), 10xHis tag at N-terminus (cleaved by TEV), 10xHis tag at C-terminus

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
      <td>Cell culture and transfection</td>
      <td>Transient transfection</td>
      <td>—</td>
      <td></td>
      <td>HEK293F cells transfected with PEI:DNA at 2:1 ratio, cultured at 37 C, collected 48 h post-transfection. 5 uM <a href="/xray-mp-wiki/reagents/ligands/vismodegib/">GDC-0449</a> present during expression.</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>Cell lysis and membrane fractionation</td>
      <td>—</td>
      <td>10 mM HEPES pH 7.5, 10 mM MgCl2, 20 mM KCl, EDTA-free protease inhibitor cocktail</td>
      <td>Hypotonic buffer wash; repeated centrifugation (3x) in high salt buffer (1.0 M NaCl)</td>
    </tr>
    <tr>
      <td>Ligand incubation</td>
      <td>Ligand binding</td>
      <td>—</td>
      <td>30 uM <a href="/xray-mp-wiki/reagents/ligands/tc114/">TC114 (SMO Ligand)</a>, 2 mg/ml <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a></td>
      <td>Membranes incubated with <a href="/xray-mp-wiki/reagents/ligands/tc114/">TC114 (SMO Ligand)</a> and <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> on <a href="/xray-mp-wiki/proteins/miscellaneous/rocker/">ROCKER</a> at 4 C for 1 h</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Solubilization</td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 200 mM NaCl + 1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.2% (w/v) <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>2.5 h at 4 C</td>
    </tr>
    <tr>
      <td>IMAC (first capture)</td>
      <td>Immobilized metal ion <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> IMAC resin (Clontech)</td>
      <td>50 mM HEPES pH 7.5, 200 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 1.0 M NaCl + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Overnight binding at 4 C</td>
    </tr>
    <tr>
      <td>Wash and detergent exchange</td>
      <td>Immobilized metal ion <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td>50 mM HEPES pH 7.5, 800 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.5% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.1% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 10 mM MgCl2, 6 mM ATP, 30 uM <a href="/xray-mp-wiki/reagents/ligands/tc114/">TC114 (SMO Ligand)</a> + <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Wash I buffer; 2 h <a href="/xray-mp-wiki/proteins/miscellaneous/rocker/">ROCKER</a> incubation for complete detergent exchange</td>
    </tr>
    <tr>
      <td>Wash II</td>
      <td>Immobilized metal ion <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td>25 mM HEPES pH 7.5, 500 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 40 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 50 uM <a href="/xray-mp-wiki/reagents/ligands/tc114/">TC114 (SMO Ligand)</a> + <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Six-column volume wash</td>
    </tr>
    <tr>
      <td>Elution and TEV cleavage</td>
      <td>Immobilized metal ion <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>—</td>
      <td>25 mM HEPES pH 7.5, 500 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a>, 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 50 uM <a href="/xray-mp-wiki/reagents/ligands/tc114/">TC114 (SMO Ligand)</a></td>
      <td>Eluted with high <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>; <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> cleavage of N-terminal tags</td>
    </tr>
  </tbody>
</table>
**Final sample**: 25 mM HEPES pH 7.5, 500 mM NaCl, 0.03% [LMNG](/xray-mp-wiki/reagents/detergents/lmng/), 0.006% [CHS](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/), 50 uM [TC114 (SMO Ligand)](/xray-mp-wiki/reagents/ligands/tc114/)

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/">Serial Femtosecond Crystallography</a> (XFEL)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SMO-FLA-<a href="/xray-mp-wiki/reagents/ligands/tc114/">TC114 (SMO Ligand)</a> complex</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>XFEL data collection at LCLS (Linac Coherent Light Source, SLAC). Room temperature (20 C). Space group P21. Cell dimensions: a=40.6, b=349.5, c=61.8, beta=101.1 deg. 13,583,207 reflections measured, 37,101 unique. Rsplit=13.3 (280 in outer shell). CC*=0.9986. Cryoprotection: not applicable (XFEL at room temperature).
</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Synchrotron X-ray crystallography</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SMO-FLA-<a href="/xray-mp-wiki/reagents/ligands/tc114/">TC114 (SMO Ligand)</a> complex</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>-196</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Synchrotron data collection at BL41XU, SPring-8. Cryo-cooled (-196 C). Space group P21. Cell dimensions: a=40.1, b=356.4, c=59.1, beta=102.8 deg. 109,498 reflections measured, 29,571 unique. Rmerge=11.7 (39.3 in outer shell).
</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5v56">5V56</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">AVTGPP</span><span class="topo-inside">PPLSHCGRAAPCEPLRYNVCLGSVLPYGATSTLLAGDSDSQEEAHGKLVLWSGLRNAPRCWAVIQPLLCAVYMPKCENDRVELPSRTLCQATRGPCAIVERERGWPDFLRCTPD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">RFPEGCTNEVQNIKFNSSGQCMVPLVRTDNPKSWYEDVEGCGIQCQNPLFTEAEHQDMH</span><span class="topo-membrane">SYIAAFGAVTGLCTLFTLATFVADW</span><span class="topo-outside">RNSNRY</span><span class="topo-membrane">PAVILFYVNACFFVGSIGWLAQFMD</span><span class="topo-inside">GARRE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">IVCRADGTMRLGEPTSNETL</span><span class="topo-membrane">SCVIIFVIVYYALMAGVVWFVVLTYAWHTSF</span><span class="topo-outside">KALGTTYQPLSG</span><span class="topo-membrane">KTSYFHLLTWSLPFVLTVAILA</span><span class="topo-inside">VAQVDGDSVSGICFVGYKNYRYR</span><span class="topo-membrane">AGFVLAPIGLVL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">IVGGYFLIRGVMTLFS</span><span class="topo-outside">IKSNHAKALIVYGSTTGNTEYTAETIARELADAGYEVDSRDAASVEAGGLFEGFDLVLLGCSTWGDDSIELQDDFIPLFDSLEETGAQGRKVACFGCGDSSWEY</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">FCGAVDAIEEKLKNLGAEIVQDGLRIDGDPRAARDDIVGWAHDVRGAIKINETM</span><span class="topo-membrane">LRLGIFGFLAFGFVLITFSCHF</span><span class="topo-inside">YDFFNQAEWERSFRDYVLCQANVTIGLPTKQPIPDCEIKNRPSL</span></span>
<span class="topo-ruler">       610       620       630       640       650   </span>
<span class="topo-line"><span class="topo-inside">LV</span><span class="topo-membrane">EKINLFAMFGTGIAMSTWVWTK</span><span class="topo-outside">ATLLIWRRTWCRLT</span><span class="topo-unknown">GQSDDHHHHHHHHHH</span></span>
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
      <td>6</td>
      <td>53</td>
      <td>58</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>179</td>
      <td>59</td>
      <td>231</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>204</td>
      <td>232</td>
      <td>256</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>210</td>
      <td>257</td>
      <td>262</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>235</td>
      <td>263</td>
      <td>287</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>236</td>
      <td>260</td>
      <td>288</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>261</td>
      <td>291</td>
      <td>313</td>
      <td>343</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>303</td>
      <td>344</td>
      <td>355</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>304</td>
      <td>325</td>
      <td>356</td>
      <td>377</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>326</td>
      <td>348</td>
      <td>378</td>
      <td>400</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>349</td>
      <td>376</td>
      <td>401</td>
      <td>428</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>377</td>
      <td>381</td>
      <td>429</td>
      <td>433</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>382</td>
      <td>528</td>
      <td>1002</td>
      <td>1148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>529</td>
      <td>534</td>
      <td>444</td>
      <td>449</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>535</td>
      <td>556</td>
      <td>450</td>
      <td>471</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>602</td>
      <td>472</td>
      <td>517</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>603</td>
      <td>624</td>
      <td>518</td>
      <td>539</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>625</td>
      <td>638</td>
      <td>540</td>
      <td>553</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>639</td>
      <td>653</td>
      <td>554</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5v57">5V57</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">PPPLSHCGRAAPCEPLRYNVCLGSVLPYGATSTLLAGDSDSQEEAHGKLVLWSGLRNAPRCWAVIQPLLCAVYMPKCENDRVELPSRTLCQATRGPCAIVERERGWPDFLRCTPDRFPEG</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">CTNEVQNIKFNSSGQCEVPLVRTDNPKSWYEDVEGCGIQCQNPLFTEAEHQDMHSY</span><span class="topo-membrane">IAAFGAVTGLCTLFTLATFVADW</span><span class="topo-outside">RNSNRYP</span><span class="topo-membrane">AVILFYVNACFFVGSIGWLAQFM</span><span class="topo-inside">DG</span><span class="topo-unknown">ARREIV</span><span class="topo-inside">CRA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">DGTMRLGEPTSNETL</span><span class="topo-membrane">SCVIIFVIVYYALMAGVVWFVVLTYAWH</span><span class="topo-outside">TSFKALGTTYQPLSGKT</span><span class="topo-membrane">SYFHLLTWSLPFVLTVAILAVAQV</span><span class="topo-inside">DGDSVSGICFVGYKNY</span><span class="topo-membrane">RYRAGFVLAPIGLVLIVGGY</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-membrane">FLIRGVM</span><span class="topo-outside">TLFSIKSNHAKALIVYGSTTGNTEYTAETIARELADAGYEVDSRDAASVEAGGLFEGFDLVLLGCSTWGDDSIELQDDFIPLFDSLEETGAQGRKVACFGCGDSSWEYFCGAV</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DAIEEKLKNLGAEIVQDGLRIDGDPRAAR</span><span class="topo-unknown">DDIVGWAHDVRG</span><span class="topo-outside">AIKINETML</span><span class="topo-membrane">RLGIFGFLAFGFVLITFSCHFYDFF</span><span class="topo-inside">NQAEWERSFRDYVLCQANVTIGLPTKQPIPDCEIKNRPSLL</span><span class="topo-membrane">VEKI</span></span>
<span class="topo-ruler">       610       620       630       640        </span>
<span class="topo-line"><span class="topo-membrane">NLFAMFGTGIAMSTWVWTKATL</span><span class="topo-unknown">LIWRRTWCRLT</span><span class="topo-outside">GQSDDHHHHHHH</span><span class="topo-unknown">HHH</span></span>
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
      <td>176</td>
      <td>58</td>
      <td>233</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>177</td>
      <td>199</td>
      <td>234</td>
      <td>256</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>200</td>
      <td>206</td>
      <td>257</td>
      <td>263</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>207</td>
      <td>229</td>
      <td>264</td>
      <td>286</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>231</td>
      <td>287</td>
      <td>288</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>232</td>
      <td>237</td>
      <td>289</td>
      <td>294</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>238</td>
      <td>255</td>
      <td>295</td>
      <td>312</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>256</td>
      <td>283</td>
      <td>313</td>
      <td>340</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>284</td>
      <td>300</td>
      <td>341</td>
      <td>357</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>301</td>
      <td>324</td>
      <td>358</td>
      <td>381</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>325</td>
      <td>340</td>
      <td>382</td>
      <td>397</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>367</td>
      <td>398</td>
      <td>424</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>368</td>
      <td>376</td>
      <td>425</td>
      <td>433</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>377</td>
      <td>509</td>
      <td>1002</td>
      <td>1134</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>521</td>
      <td>1135</td>
      <td>1146</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>522</td>
      <td>523</td>
      <td>1147</td>
      <td>1148</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>524</td>
      <td>530</td>
      <td>444</td>
      <td>450</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>531</td>
      <td>555</td>
      <td>451</td>
      <td>475</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>556</td>
      <td>596</td>
      <td>476</td>
      <td>516</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>597</td>
      <td>622</td>
      <td>517</td>
      <td>542</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>623</td>
      <td>633</td>
      <td>543</td>
      <td>553</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>634</td>
      <td>645</td>
      <td>554</td>
      <td>565</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Flavodoxin Fusion for GPCR Crystallization

Flavodoxin (FLA, 16 kDa) was fused to the intracellular loop 3 (ICL3) of the human [SMO](/xray-mp-wiki/proteins/gpcr/smoothened/) receptor between residues P434 and S443. This fusion strategy provides a stable, well-folded protein domain on the intracellular side of the receptor, which enhances crystallizability by reducing conformational flexibility in the intracellular region. The SMO-FLA construct enabled the first XFEL structure determination of a multi-domain [SMO](/xray-mp-wiki/proteins/gpcr/smoothened/) receptor.

### Multi-domain Architecture of SMO

The SMO-FLA structure reveals the complete three-domain architecture of [SMO](/xray-mp-wiki/proteins/gpcr/smoothened/): a seven-transmembrane helices domain (TMD), a hinge domain (HD), and an intact extracellular cysteine-rich domain (CRD). This multi-domain arrangement enables allosteric interactions between the CRD and TMD that are critical for ligand recognition and receptor activation. The structure demonstrates that the CRD adopts a 'closed' conformation regardless of sterol binding when in the context of the full-length receptor.

### Activation Mechanism of Multi-domain GPCRs

The SMO-FLA structure combined with HDX analysis and MD simulations reveals a unique GPCR activation mechanism distinct from other multi-domain GPCRs. Transmembrane helix VI, extracellular loop 3 (ECL3), and the hinge domain (HD) play a central role in signal transmission. Agonist binding to the CRD triggers a small tilt of the CRD, which pushes helix VI and ECL3 outward, leading to amplified conformational changes and downward movement of the HD, transmitting the signal to the TMD.


## Cross-References

- <a href="/xray-mp-wiki/proteins/gpcr/smoothened/">Human Smoothened Receptor (SMO)</a> — Parent receptor protein for the SMO-FLA fusion construct
- <a href="/xray-mp-wiki/reagents/ligands/tc114/">TC114</a> — Stabilizing ligand used for SMO-FLA crystallization
- <a href="/xray-mp-wiki/methods/structure-determination/serial-femtosecond-crystallography/">Serial Femtosecond Crystallography</a> — XFEL method used for SMO-FLA structure determination (PDB 5V56)
- <a href="/xray-mp-wiki/reagents/detergents/lmng/">LMNG</a> — Detergent used in SMO-FLA purification and sample preparation
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Detergent used in initial SMO-FLA membrane solubilization
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/miscellaneous/rocker/">ROCKER</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
