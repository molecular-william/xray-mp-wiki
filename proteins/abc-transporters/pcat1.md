---
title: "PCAT1 (Peptidase-Containing ABC Transporter from Clostridium thermocellum)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature14623]
verified: false
---

# PCAT1 (Peptidase-Containing ABC Transporter from Clostridium thermocellum)

## Overview

PCAT1 is a peptidase-containing ATP-binding cassette (ABC) transporter from Clostridium thermocellum that functions as both a maturation protease and exporter for bacteriocin-like polypeptides. PCAT1 represents a dual-function ABC transporter that processes and secretes small proteins. It contains two N-terminal peptidase domains (family C39 cysteine protease), two transmembrane domains (TMDs) forming a large alpha-helical barrel translocation pathway, and two nucleotide-binding domains (NBDs) that hydrolyze ATP. The crystal structures reveal an inward-facing ATP-free conformation with a large transmembrane tunnel sufficient to accommodate small folded proteins, and an ATP-bound occluded conformation where the peptidase domains dissociate. ATP binding alternates access to the transmembrane pathway and regulates protease activity, thereby coupling substrate processing to translocation.


## Publications

### doi/10.1038##nature14623

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ry2">4RY2</a></td>
      <td>3.6 A</td>
      <td>P2(1)2(1)2(1)</td>
      <td>Full-length PCAT1 from Clostridium thermocellum (residues 1-727), expressed in E. coli BL21(DE3) codon plus (RIL) cells, N-terminal GST tag removed by TEV protease</td>
      <td>None (ATP-free form)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ry2">4RY2</a></td>
      <td>4.1 A</td>
      <td>C222(1)</td>
      <td>Full-length PCAT1 from Clostridium thermocellum (residues 1-727), expressed in E. coli BL21(DE3) codon plus (RIL) cells, N-terminal GST tag removed by TEV protease</td>
      <td>None (ATP-free form, alternative crystal form)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ry2">4RY2</a></td>
      <td>5.5 A</td>
      <td>P4(2)2(1)2</td>
      <td>Full-length PCAT1 E648Q mutant from Clostridium thermocellum (residues 1-727), expressed in E. coli BL21(DE3) codon plus (RIL) cells, N-terminal GST tag removed by TEV protease</td>
      <td>ATPγS (bound, hydrolysis-deficient mutant)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3) codon plus (RIL) cells
- **Construct**: Full-length PCAT1 (residues 1-727) from Clostridium thermocellum, N-terminal GST tag with TEV protease cleavage site; also isolated peptidase domain (residues 1-148) as GST fusion

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
      <td>Cell growth and induction</td>
      <td>E. coli expression in Terrific Broth</td>
      <td>--</td>
      <td>Terrific Broth (Novagen) supplemented with ampicillin + --</td>
      <td>Induced with 100 μM IPTG at 16 C for 24 h</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>High-pressure homogenization and ultracentrifugation</td>
      <td>--</td>
      <td>50 mM Tris-HCl pH 7.0, 500 mM NaCl, 10% glycerol + --</td>
      <td>Cells lysed by two passes through Emulsiflex-C3 homogenizer, membranes pelleted at 80,000g for 40 min</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>50 mM Tris-HCl pH 7.0, 500 mM NaCl, 10% glycerol, 5 mM DTT + <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a> (n-dodecyl-beta-D-maltopyranoside) at 1%</td>
      <td>Solubilized at 4 C for 2 h, insoluble material removed at 70,000g for 20 min</td>
    </tr>
    <tr>
      <td>GST affinity purification</td>
      <td>Glutathione Sepharose <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Glutathione Sepharose 4B (GE Healthcare)</td>
      <td>50 mM Tris-HCl pH 7.0, 500 mM NaCl, 10% glycerol, 5 mM DTT, 2 mM <a href="/xray-mp-wiki/reagents/detergents/udm">UDM</a> (n-undecyl-beta-D-maltopyranoside) + <a href="/xray-mp-wiki/reagents/detergents/udm">UDM</a></td>
      <td>On-column TEV protease cleavage overnight at 4 C to remove GST tag</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC on Superdex 200</td>
      <td>Superdex 200 16/60 (GE Healthcare)</td>
      <td>20 mM Tris-HCl pH 7.0, 150 mM NaCl, 2 mM <a href="/xray-mp-wiki/reagents/detergents/udm">UDM</a>, 5 mM DTT + <a href="/xray-mp-wiki/reagents/detergents/udm">UDM</a></td>
      <td>Final purification step</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic bicelle method</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PCAT1 at undetermined concentration in <a href="/xray-mp-wiki/reagents/detergents/udm">UDM</a>, reconstituted into DMPC/CHAPSO bicelles (35% bicelle stock, 2.8:1 DMPC:CHAPSO)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not explicitly reported</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not reported</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryocooled</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal form 1, space group P2(1)2(1)2(1), unit cell a=87.6, b=89.7, c=296.6 A. Resolution 3.6 A. R_work/R_free not explicitly reported. Two monomers per asymmetric unit forming a dimer.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic bicelle method</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PCAT1 at undetermined concentration in <a href="/xray-mp-wiki/reagents/detergents/udm">UDM</a>, reconstituted into DMPC/CHAPSO bicelles</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not explicitly reported</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not reported</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryocooled</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystal form 2, space group C222(1), unit cell a=138.4, b=178.4, c=90.2 A. Resolution 4.1 A. One monomer per asymmetric unit.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic bicelle method</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>PCAT1 E648Q mutant at undetermined concentration, reconstituted into DMPC/CHAPSO bicelles</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not explicitly reported</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Not reported</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryocooled</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>E648Q mutant in complex with ATPγS. Space group P4(2)2(1)2, unit cell a=b=230.0, c=89.4 A. Resolution 5.5 A. R_work=30%, R_free=31%. Peptidase domains disordered (no electron density observed).</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ry2">4RY2</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">SNAMLRRLFKKKYV</span><span class="topo-outside">CVRQYDLTDCGAACLSSIAQYYGLKMSLAKIREMTGTDTQGTNAYG</span></span>
<span class="topo-line"><span class="topo-outside">LIHAAKQLGFSAKGVKASKEDLLKDFRLPAIANVIVDNRLAHFVVIYSIKNRIITVADPG</span></span>
<span class="topo-line"><span class="topo-outside">KGIVRYSMDDFCSIWTGGLVLLEPGEAFQKGDYTQN</span><span class="topo-unknown">MMVKFAGFLK</span><span class="topo-outside">PL</span><span class="topo-membrane">KKTVLCIFLASL</span></span>
<span class="topo-line"><span class="topo-membrane">LYTALGIAGSF</span><span class="topo-inside">YIKFLFDDLIKFEKLNDLHIISA</span><span class="topo-membrane">GFAVIFLLQIFLNYYRSILVTKLG</span><span class="topo-outside">MS</span></span>
<span class="topo-line"><span class="topo-outside">IDKSIMMEYYSHVLKLPMNFFNSRKVGEIISRFMDASKIRQA</span><span class="topo-membrane">ISGATLTIMIDTIMAVIG</span></span>
<span class="topo-line"><span class="topo-membrane">GILLY</span><span class="topo-inside">IQNSSL</span><span class="topo-membrane">FFISFIIILLYGIIVTVFNKPI</span><span class="topo-outside">QNANRQIMEDNAKLTSALVESVKGIET</span></span>
<span class="topo-line"><span class="topo-outside">IKSFGAEEQTEKSTRDKIETVMKSSFKE</span><span class="topo-membrane">GMLYINLSSLTGIVAGLGGIVI</span><span class="topo-inside">LWAGAYNVIK</span></span>
<span class="topo-line"><span class="topo-inside">GNMSGGQLLAF</span><span class="topo-membrane">NALLAYFLTPVKNLIDLQPLI</span><span class="topo-outside">QTAVVASNRLGEILELATEKEL</span><span class="topo-unknown">REDSDD</span></span>
<span class="topo-line"><span class="topo-unknown">FVISLK</span><span class="topo-outside">GDIEFRNVDFRYGLRKPVLKNINLTIPKGKTVAIVGESGSGKTTLAKLLMNFYS</span></span>
<span class="topo-line"><span class="topo-outside">PEKGDILINGHSIKNISLELIRKKIAFVSQDVFIFSGTVKENLCLGNENVDMDEIIKAAK</span></span>
<span class="topo-line"><span class="topo-outside">MANAHDFIEKLPLKYDTFLNESGANLSEGQKQRLAIARALLKKPDILILDEATSNLDSIT</span></span>
<span class="topo-line"><span class="topo-outside">ENHIKDAIYGLEDDVTVIIIAHRLSTIVNCDKIYLLKDGEIVESGSHTELIALKGCYFKM</span></span>
<span class="topo-line"><span class="topo-outside">WKQTENT</span><span class="topo-unknown">LAS</span></span>
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
      <td>15</td>
      <td>156</td>
      <td>12</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>166</td>
      <td>154</td>
      <td>163</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>167</td>
      <td>168</td>
      <td>164</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>169</td>
      <td>191</td>
      <td>166</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>214</td>
      <td>189</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>238</td>
      <td>212</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>282</td>
      <td>236</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>305</td>
      <td>280</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>311</td>
      <td>303</td>
      <td>308</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>333</td>
      <td>309</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>388</td>
      <td>331</td>
      <td>385</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>410</td>
      <td>386</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>431</td>
      <td>408</td>
      <td>428</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>432</td>
      <td>452</td>
      <td>429</td>
      <td>449</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>453</td>
      <td>474</td>
      <td>450</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>487</td>
      <td>727</td>
      <td>484</td>
      <td>724</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ry2">4RY2</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">SNAMLRRLFKKKYV</span><span class="topo-outside">CVRQYDLTDCGAACLSSIAQYYGLKMSLAKIREMTGTDTQGTNAYG</span></span>
<span class="topo-line"><span class="topo-outside">LIHAAKQLGFSAKGVKASKEDLLKDFRLPAIANVIVDNRLAHFVVIYSIKNRIITVADPG</span></span>
<span class="topo-line"><span class="topo-outside">KGIVRYSMDDFCSIWTGGLVLLEPGEAFQKGDYTQN</span><span class="topo-unknown">MMVKFAG</span><span class="topo-outside">FL</span><span class="topo-membrane">KPLKKTVLCIFLASL</span></span>
<span class="topo-line"><span class="topo-membrane">LYTALGIAGS</span><span class="topo-inside">FYIKFLFDDLIKFEKLNDLHIISA</span><span class="topo-membrane">GFAVIFLLQIFLNYYRSILVTKLG</span><span class="topo-outside">MS</span></span>
<span class="topo-line"><span class="topo-outside">IDKSIMMEYYSHVLKLPMNFFNSRKVGEIISRFMDASKIRQA</span><span class="topo-membrane">ISGATLTIMIDTIMAVIG</span></span>
<span class="topo-line"><span class="topo-membrane">GILLY</span><span class="topo-inside">IQNSSL</span><span class="topo-membrane">FFISFIIILLYGIIVTVFNKPI</span><span class="topo-outside">QNANRQIMEDNAKLTSALVESVKGIET</span></span>
<span class="topo-line"><span class="topo-outside">IKSFGAEEQTEKSTRDKIETVMKSSFKE</span><span class="topo-membrane">GMLYINLSSLTGIVAGLGGIVI</span><span class="topo-inside">LWAGAYNVIK</span></span>
<span class="topo-line"><span class="topo-inside">GNMSGGQLLAF</span><span class="topo-membrane">NALLAYFLTPVKNLIDLQPLIQ</span><span class="topo-outside">TAVVASNRLGEILELATEKEL</span><span class="topo-unknown">REDSDD</span></span>
<span class="topo-line"><span class="topo-unknown">FVISLK</span><span class="topo-outside">GDIEFRNVDFRYGLRKPVLKNINLTIPKGKTVAIVGESGSGKTTLAKLLMNFYS</span></span>
<span class="topo-line"><span class="topo-outside">PEKGDILINGHSIKNISLELIRKKIAFVSQDVFIFSGTVKENLCLGNENVDMDEIIKAAK</span></span>
<span class="topo-line"><span class="topo-outside">MANAHDFIEKLPLKYDTFLNESGANLSEGQKQRLAIARALLKKPDILILDEATSNLDSIT</span></span>
<span class="topo-line"><span class="topo-outside">ENHIKDAIYGLEDDVTVIIIAHRLSTIVNCDKIYLLKDGEIVESGSHTELIALKGCYFKM</span></span>
<span class="topo-line"><span class="topo-outside">WKQTE</span><span class="topo-unknown">NTLAS</span></span>
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
      <td>15</td>
      <td>156</td>
      <td>12</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>163</td>
      <td>154</td>
      <td>160</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>164</td>
      <td>165</td>
      <td>161</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>190</td>
      <td>163</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>214</td>
      <td>188</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>238</td>
      <td>212</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>282</td>
      <td>236</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>305</td>
      <td>280</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>311</td>
      <td>303</td>
      <td>308</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>333</td>
      <td>309</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>388</td>
      <td>331</td>
      <td>385</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>410</td>
      <td>386</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>431</td>
      <td>408</td>
      <td>428</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>432</td>
      <td>453</td>
      <td>429</td>
      <td>450</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>451</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>487</td>
      <td>725</td>
      <td>484</td>
      <td>722</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ry2">4RY2</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">SNAMLRRLFKKKYV</span><span class="topo-outside">CVRQYDLTDCGAACLSSIAQYYGLKMSLAKIREMTGTDTQGTNAYG</span></span>
<span class="topo-line"><span class="topo-outside">LIHAAKQLGFSAKGVKASKEDLLKDFRLPAIANVIVDNRLAHFVVIYSIKNRIITVADPG</span></span>
<span class="topo-line"><span class="topo-outside">KGIVRYSMDDFCSIWTGGLVLLEPGEAFQKGDYTQN</span><span class="topo-unknown">MMVKFAGFLK</span><span class="topo-outside">PL</span><span class="topo-membrane">KKTVLCIFLASL</span></span>
<span class="topo-line"><span class="topo-membrane">LYTALGIAGSF</span><span class="topo-inside">YIKFLFDDLIKFEKLNDLHIISA</span><span class="topo-membrane">GFAVIFLLQIFLNYYRSILVTKLG</span><span class="topo-outside">MS</span></span>
<span class="topo-line"><span class="topo-outside">IDKSIMMEYYSHVLKLPMNFFNSRKVGEIISRFMDASKIRQA</span><span class="topo-membrane">ISGATLTIMIDTIMAVIG</span></span>
<span class="topo-line"><span class="topo-membrane">GILLY</span><span class="topo-inside">IQNSSL</span><span class="topo-membrane">FFISFIIILLYGIIVTVFNKPI</span><span class="topo-outside">QNANRQIMEDNAKLTSALVESVKGIET</span></span>
<span class="topo-line"><span class="topo-outside">IKSFGAEEQTEKSTRDKIETVMKSSFKE</span><span class="topo-membrane">GMLYINLSSLTGIVAGLGGIVI</span><span class="topo-inside">LWAGAYNVIK</span></span>
<span class="topo-line"><span class="topo-inside">GNMSGGQLLAF</span><span class="topo-membrane">NALLAYFLTPVKNLIDLQPLI</span><span class="topo-outside">QTAVVASNRLGEILELATEKEL</span><span class="topo-unknown">REDSDD</span></span>
<span class="topo-line"><span class="topo-unknown">FVISLK</span><span class="topo-outside">GDIEFRNVDFRYGLRKPVLKNINLTIPKGKTVAIVGESGSGKTTLAKLLMNFYS</span></span>
<span class="topo-line"><span class="topo-outside">PEKGDILINGHSIKNISLELIRKKIAFVSQDVFIFSGTVKENLCLGNENVDMDEIIKAAK</span></span>
<span class="topo-line"><span class="topo-outside">MANAHDFIEKLPLKYDTFLNESGANLSEGQKQRLAIARALLKKPDILILDEATSNLDSIT</span></span>
<span class="topo-line"><span class="topo-outside">ENHIKDAIYGLEDDVTVIIIAHRLSTIVNCDKIYLLKDGEIVESGSHTELIALKGCYFKM</span></span>
<span class="topo-line"><span class="topo-outside">WKQTENT</span><span class="topo-unknown">LAS</span></span>
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
      <td>15</td>
      <td>156</td>
      <td>12</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>166</td>
      <td>154</td>
      <td>163</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>167</td>
      <td>168</td>
      <td>164</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>169</td>
      <td>191</td>
      <td>166</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>214</td>
      <td>189</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>238</td>
      <td>212</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>282</td>
      <td>236</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>305</td>
      <td>280</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>311</td>
      <td>303</td>
      <td>308</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>333</td>
      <td>309</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>388</td>
      <td>331</td>
      <td>385</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>410</td>
      <td>386</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>431</td>
      <td>408</td>
      <td>428</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>432</td>
      <td>452</td>
      <td>429</td>
      <td>449</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>453</td>
      <td>474</td>
      <td>450</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>487</td>
      <td>727</td>
      <td>484</td>
      <td>724</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ry2">4RY2</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">SNAMLRRLFKKKYV</span><span class="topo-outside">CVRQYDLTDCGAACLSSIAQYYGLKMSLAKIREMTGTDTQGTNAYG</span></span>
<span class="topo-line"><span class="topo-outside">LIHAAKQLGFSAKGVKASKEDLLKDFRLPAIANVIVDNRLAHFVVIYSIKNRIITVADPG</span></span>
<span class="topo-line"><span class="topo-outside">KGIVRYSMDDFCSIWTGGLVLLEPGEAFQKGDYTQN</span><span class="topo-unknown">MMVKFAG</span><span class="topo-outside">FL</span><span class="topo-membrane">KPLKKTVLCIFLASL</span></span>
<span class="topo-line"><span class="topo-membrane">LYTALGIAGS</span><span class="topo-inside">FYIKFLFDDLIKFEKLNDLHIISA</span><span class="topo-membrane">GFAVIFLLQIFLNYYRSILVTKLG</span><span class="topo-outside">MS</span></span>
<span class="topo-line"><span class="topo-outside">IDKSIMMEYYSHVLKLPMNFFNSRKVGEIISRFMDASKIRQA</span><span class="topo-membrane">ISGATLTIMIDTIMAVIG</span></span>
<span class="topo-line"><span class="topo-membrane">GILLY</span><span class="topo-inside">IQNSSL</span><span class="topo-membrane">FFISFIIILLYGIIVTVFNKPI</span><span class="topo-outside">QNANRQIMEDNAKLTSALVESVKGIET</span></span>
<span class="topo-line"><span class="topo-outside">IKSFGAEEQTEKSTRDKIETVMKSSFKE</span><span class="topo-membrane">GMLYINLSSLTGIVAGLGGIVI</span><span class="topo-inside">LWAGAYNVIK</span></span>
<span class="topo-line"><span class="topo-inside">GNMSGGQLLAF</span><span class="topo-membrane">NALLAYFLTPVKNLIDLQPLIQ</span><span class="topo-outside">TAVVASNRLGEILELATEKEL</span><span class="topo-unknown">REDSDD</span></span>
<span class="topo-line"><span class="topo-unknown">FVISLK</span><span class="topo-outside">GDIEFRNVDFRYGLRKPVLKNINLTIPKGKTVAIVGESGSGKTTLAKLLMNFYS</span></span>
<span class="topo-line"><span class="topo-outside">PEKGDILINGHSIKNISLELIRKKIAFVSQDVFIFSGTVKENLCLGNENVDMDEIIKAAK</span></span>
<span class="topo-line"><span class="topo-outside">MANAHDFIEKLPLKYDTFLNESGANLSEGQKQRLAIARALLKKPDILILDEATSNLDSIT</span></span>
<span class="topo-line"><span class="topo-outside">ENHIKDAIYGLEDDVTVIIIAHRLSTIVNCDKIYLLKDGEIVESGSHTELIALKGCYFKM</span></span>
<span class="topo-line"><span class="topo-outside">WKQTE</span><span class="topo-unknown">NTLAS</span></span>
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
      <td>15</td>
      <td>156</td>
      <td>12</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>163</td>
      <td>154</td>
      <td>160</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>164</td>
      <td>165</td>
      <td>161</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>190</td>
      <td>163</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>214</td>
      <td>188</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>238</td>
      <td>212</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>282</td>
      <td>236</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>305</td>
      <td>280</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>311</td>
      <td>303</td>
      <td>308</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>333</td>
      <td>309</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>388</td>
      <td>331</td>
      <td>385</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>410</td>
      <td>386</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>431</td>
      <td>408</td>
      <td>428</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>432</td>
      <td>453</td>
      <td>429</td>
      <td>450</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>451</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>487</td>
      <td>725</td>
      <td>484</td>
      <td>722</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ry2">4RY2</a> — Chain A (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">SNAMLRRLFKKKYV</span><span class="topo-outside">CVRQYDLTDCGAACLSSIAQYYGLKMSLAKIREMTGTDTQGTNAYG</span></span>
<span class="topo-line"><span class="topo-outside">LIHAAKQLGFSAKGVKASKEDLLKDFRLPAIANVIVDNRLAHFVVIYSIKNRIITVADPG</span></span>
<span class="topo-line"><span class="topo-outside">KGIVRYSMDDFCSIWTGGLVLLEPGEAFQKGDYTQN</span><span class="topo-unknown">MMVKFAGFLK</span><span class="topo-outside">PL</span><span class="topo-membrane">KKTVLCIFLASL</span></span>
<span class="topo-line"><span class="topo-membrane">LYTALGIAGSF</span><span class="topo-inside">YIKFLFDDLIKFEKLNDLHIISA</span><span class="topo-membrane">GFAVIFLLQIFLNYYRSILVTKLG</span><span class="topo-outside">MS</span></span>
<span class="topo-line"><span class="topo-outside">IDKSIMMEYYSHVLKLPMNFFNSRKVGEIISRFMDASKIRQA</span><span class="topo-membrane">ISGATLTIMIDTIMAVIG</span></span>
<span class="topo-line"><span class="topo-membrane">GILLY</span><span class="topo-inside">IQNSSL</span><span class="topo-membrane">FFISFIIILLYGIIVTVFNKPI</span><span class="topo-outside">QNANRQIMEDNAKLTSALVESVKGIET</span></span>
<span class="topo-line"><span class="topo-outside">IKSFGAEEQTEKSTRDKIETVMKSSFKE</span><span class="topo-membrane">GMLYINLSSLTGIVAGLGGIVI</span><span class="topo-inside">LWAGAYNVIK</span></span>
<span class="topo-line"><span class="topo-inside">GNMSGGQLLAF</span><span class="topo-membrane">NALLAYFLTPVKNLIDLQPLI</span><span class="topo-outside">QTAVVASNRLGEILELATEKEL</span><span class="topo-unknown">REDSDD</span></span>
<span class="topo-line"><span class="topo-unknown">FVISLK</span><span class="topo-outside">GDIEFRNVDFRYGLRKPVLKNINLTIPKGKTVAIVGESGSGKTTLAKLLMNFYS</span></span>
<span class="topo-line"><span class="topo-outside">PEKGDILINGHSIKNISLELIRKKIAFVSQDVFIFSGTVKENLCLGNENVDMDEIIKAAK</span></span>
<span class="topo-line"><span class="topo-outside">MANAHDFIEKLPLKYDTFLNESGANLSEGQKQRLAIARALLKKPDILILDEATSNLDSIT</span></span>
<span class="topo-line"><span class="topo-outside">ENHIKDAIYGLEDDVTVIIIAHRLSTIVNCDKIYLLKDGEIVESGSHTELIALKGCYFKM</span></span>
<span class="topo-line"><span class="topo-outside">WKQTENT</span><span class="topo-unknown">LAS</span></span>
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
      <td>15</td>
      <td>156</td>
      <td>12</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>166</td>
      <td>154</td>
      <td>163</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>167</td>
      <td>168</td>
      <td>164</td>
      <td>165</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>169</td>
      <td>191</td>
      <td>166</td>
      <td>188</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>192</td>
      <td>214</td>
      <td>189</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>238</td>
      <td>212</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>282</td>
      <td>236</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>305</td>
      <td>280</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>311</td>
      <td>303</td>
      <td>308</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>333</td>
      <td>309</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>388</td>
      <td>331</td>
      <td>385</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>410</td>
      <td>386</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>431</td>
      <td>408</td>
      <td>428</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>432</td>
      <td>452</td>
      <td>429</td>
      <td>449</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>453</td>
      <td>474</td>
      <td>450</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>487</td>
      <td>727</td>
      <td>484</td>
      <td>724</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ry2">4RY2</a> — Chain B (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">SNAMLRRLFKKKYV</span><span class="topo-outside">CVRQYDLTDCGAACLSSIAQYYGLKMSLAKIREMTGTDTQGTNAYG</span></span>
<span class="topo-line"><span class="topo-outside">LIHAAKQLGFSAKGVKASKEDLLKDFRLPAIANVIVDNRLAHFVVIYSIKNRIITVADPG</span></span>
<span class="topo-line"><span class="topo-outside">KGIVRYSMDDFCSIWTGGLVLLEPGEAFQKGDYTQN</span><span class="topo-unknown">MMVKFAG</span><span class="topo-outside">FL</span><span class="topo-membrane">KPLKKTVLCIFLASL</span></span>
<span class="topo-line"><span class="topo-membrane">LYTALGIAGS</span><span class="topo-inside">FYIKFLFDDLIKFEKLNDLHIISA</span><span class="topo-membrane">GFAVIFLLQIFLNYYRSILVTKLG</span><span class="topo-outside">MS</span></span>
<span class="topo-line"><span class="topo-outside">IDKSIMMEYYSHVLKLPMNFFNSRKVGEIISRFMDASKIRQA</span><span class="topo-membrane">ISGATLTIMIDTIMAVIG</span></span>
<span class="topo-line"><span class="topo-membrane">GILLY</span><span class="topo-inside">IQNSSL</span><span class="topo-membrane">FFISFIIILLYGIIVTVFNKPI</span><span class="topo-outside">QNANRQIMEDNAKLTSALVESVKGIET</span></span>
<span class="topo-line"><span class="topo-outside">IKSFGAEEQTEKSTRDKIETVMKSSFKE</span><span class="topo-membrane">GMLYINLSSLTGIVAGLGGIVI</span><span class="topo-inside">LWAGAYNVIK</span></span>
<span class="topo-line"><span class="topo-inside">GNMSGGQLLAF</span><span class="topo-membrane">NALLAYFLTPVKNLIDLQPLIQ</span><span class="topo-outside">TAVVASNRLGEILELATEKEL</span><span class="topo-unknown">REDSDD</span></span>
<span class="topo-line"><span class="topo-unknown">FVISLK</span><span class="topo-outside">GDIEFRNVDFRYGLRKPVLKNINLTIPKGKTVAIVGESGSGKTTLAKLLMNFYS</span></span>
<span class="topo-line"><span class="topo-outside">PEKGDILINGHSIKNISLELIRKKIAFVSQDVFIFSGTVKENLCLGNENVDMDEIIKAAK</span></span>
<span class="topo-line"><span class="topo-outside">MANAHDFIEKLPLKYDTFLNESGANLSEGQKQRLAIARALLKKPDILILDEATSNLDSIT</span></span>
<span class="topo-line"><span class="topo-outside">ENHIKDAIYGLEDDVTVIIIAHRLSTIVNCDKIYLLKDGEIVESGSHTELIALKGCYFKM</span></span>
<span class="topo-line"><span class="topo-outside">WKQTE</span><span class="topo-unknown">NTLAS</span></span>
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
      <td>15</td>
      <td>156</td>
      <td>12</td>
      <td>153</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>157</td>
      <td>163</td>
      <td>154</td>
      <td>160</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>164</td>
      <td>165</td>
      <td>161</td>
      <td>162</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>166</td>
      <td>190</td>
      <td>163</td>
      <td>187</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>191</td>
      <td>214</td>
      <td>188</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>238</td>
      <td>212</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>239</td>
      <td>282</td>
      <td>236</td>
      <td>279</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>305</td>
      <td>280</td>
      <td>302</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>311</td>
      <td>303</td>
      <td>308</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>333</td>
      <td>309</td>
      <td>330</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>388</td>
      <td>331</td>
      <td>385</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>389</td>
      <td>410</td>
      <td>386</td>
      <td>407</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>411</td>
      <td>431</td>
      <td>408</td>
      <td>428</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>432</td>
      <td>453</td>
      <td>429</td>
      <td>450</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>454</td>
      <td>474</td>
      <td>451</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>487</td>
      <td>725</td>
      <td>484</td>
      <td>722</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Dual-function ABC transporter architecture

PCAT1 is a dual-function ABC transporter containing both a protease domain for substrate processing and a translocation channel for secretion. The full-length transporter is a homodimer with each subunit containing an N-terminal peptidase domain (family C39 cysteine protease), six transmembrane helices, and a C-terminal nucleotide-binding domain. The overall architecture resembles other ABC exporters with the TMDs and NBDs forming the core transporter, while the peptidase domains dock onto the cytoplasmic openings of the TM tunnel.

### Large alpha-helical barrel translocation pathway

The translocation pathway is a large alpha-helical barrel traversing nearly the entire lipid bilayer. The cross-section is rhomboidal with an area of approximately 440 A^2 in the membrane-spanning region, sufficient to accommodate small folded proteins (e.g., BPTI). The interior surface is lined with charged residues, providing a hydrophilic environment for the cargo. Near the extracellular surface, hydrophobic residues I190, F194, and L426 form a closed gate.

### Peptidase domain docking and substrate processing

The peptidase domains dock onto the lateral cytoplasmic openings of the TM tunnel, with the catalytic site (Cys21, His100, Asp106) facing the gateway. This positions the domains perfectly to process the leader peptide by enzymatic cleavage while recruiting the substrate into the translocation pathway. The buried surface area at the interface is small (~980 A^2), suggesting weak association.

### ATP binding regulates access and protease activity

ATP binding (ATPγS to E648Q mutant) induces a major conformational change: the NBDs rotate inward to form a closed dimer, TM helices 3-6 shift toward the molecular center, narrowing the TM pathway and closing the lateral openings. The extracellular gate remains closed, resulting in an occluded cavity. In this conformation, the peptidase domains dissociate from the transporter, explaining the reduced protease activity upon ATP binding.

### Primed NBD dimer

In the ATP-free form, the NBD dimer resembles the pre-translocation state of the maltose transporter (MalK), a substrate-induced conformation primed for ATP hydrolysis. Key features include the Walker A serine and switch histidine at the dimer interface making contact with the D-loop of the opposite NBD. This pre-arranged configuration explains why substrate does not stimulate ATP hydrolysis in PCAT1.

### Alternating-access model for protein translocation

Based on the two conformations, the paper proposes an alternating-access model: (1) In the absence of ATP, the substrate is recruited through the peptidase domain and inserted into the translocation pathway. Proteolytic cleavage removes the leader peptide. (2) ATP binding alters the access of the translocation pathway and disengages the peptidase domains. (3) ATP hydrolysis resets the transporter to the inward-facing conformation for the next cycle.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/tm287-288/">TM287/288 (ABC exporter from Thermotoga maritima)</a> — Homologous ABC exporter used as molecular replacement search model for TMD and NBD
- <a href="/xray-mp-wiki/concepts/abc-transporters/">ABC Transporters</a> — PCAT1 is a member of the ABC transporter family with dual peptidase/transporter function
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — Lipidic bicelle method used for crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Used for membrane solubilization
