---
title: "Escherichia coli Site-2 Protease Homolog RseP (EcRseP)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1126##sciadv.abp9011]
verified: regex
---

# Escherichia coli Site-2 Protease Homolog RseP (EcRseP)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


## Overview

EcRseP is the E. coli homolog of [Site-2 Protease (mjS2P) from Methanocaldococcus jannaschii](/xray-mp-wiki/proteins/enzymes/mjs2p/) (S2P), a conserved zinc metalloprotease family that performs [Intramembrane Proteolysis](/xray-mp-wiki/concepts/membrane-mimetics/intramembrane-proteolysis/) of transmembrane substrates. EcRseP catalyzes the second step of the extracytoplasmic stress response by cleaving the anti-sigma factor RseA after its periplasmic region has been removed by DegS. It contains a conserved catalytic core with a zinc-binding HEXXH motif, an MRE beta-sheet, two tandem periplasmic PDZ domains that serve as a size exclusion filter, and a PCT (PDZ C-terminal) region with two helices (H1 and H2). The crystal structure of EcRseP in complex with the peptide-mimetic inhibitor  revealed the architecture of a group I S2P family member with extracytoplasmic PDZ domains.


## Publications

### doi/10.1126##sciadv.abp9011

**Expression:**

- **Expression system**: E. coli C43(DE3)
- **Construct**: Full-length EcRseP with C-terminal TEV-His8-Myc-PA tag
- **Induction**: 0.1 mM  at 30°C for 4 hours
- **Media**: LB medium with 50 ug/ml 

**Purification:**

- **Expression system**: E. coli C43(DE3)
- **Expression construct**: Full-length EcRseP with C-terminal TEV consensus sequence, His8 tag, Myc epitope, and PA tag
- **Tag info**: C-terminal TEV-His8-Myc-PA, TEV cleaved for crystallization

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
      <td>Sonication</td>
      <td>—</td>
      <td>10 mM  Hcl]] pH 7.4, 150 mM NaCl</td>
      <td>Lysed cells centrifuged at 40,000g for 45 min, supernatant ultracentrifuged at 200,000g for 90 min</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>40 mM  Hcl]] pH 8.5, 150 mM NaCl + 1%  monododecanoate (SM)</td>
      <td>Equal volume of solubilization buffer added to membrane suspension</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA</td>
      <td>Ni-NTA agarose</td>
      <td>20 mM  Hcl]] pH 8.0, 300 mM NaCl, 10%  + 0.03% , 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td>Wash with 50 mM , elute with 300 mM ; His8 tag cleaved with <a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease (Tobacco Etch Virus Protease)</a> overnight at 20°C</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>SEC</td>
      <td>Superdex 200 10/300 GL</td>
      <td>20 mM  Hcl]] pH 8.0, 300 mM NaCl, 10%  + 0.03% , 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a></td>
      <td> added to SEC buffer for co-crystallization</td>
    </tr>
    <tr>
      <td>Reverse Ni-NTA</td>
      <td>Ni-NTA (flow-through)</td>
      <td>—</td>
      <td></td>
      <td>Tag-cleaved protein collected in unbound fraction after TEV cleavage</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>EcRseP- complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified in extracted text</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals obtained in space group P1, diffracted to 3.20 A resolution; data collected at SPring-8 BL32XU</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Gating mechanism for substrate entry

The PDZ tandem, PCT-H2, and TM4 form a gate that regulates substrate access to the active center. In the gate-closed conformation, the active center is covered and inaccessible. Upon substrate binding, the PDZ tandem separates from the PCT region, and PCT-H2 with TM4 move away, exposing the substrate-binding site.

### Substrate unwinding and clamping

The substrate TM segment is unwound by strand addition to the MRE beta-sheet and clamped at the active center by conserved residue N394, which forms a hydrogen bond with the substrate backbone. This mechanism appears conserved across S2P family members and other intramembrane protease families.

### Three-step substrate accommodation model

EcRseP regulates substrate cleavage through three processes: (1) size exclusion by the PDZ tandem restricting bulky intact substrates, (2) gating by PDZ tandem/PCT-H2/TM4 rearrangement, and (3) unwinding of the substrate TM helix by the MRE beta-sheet edge strand.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/kkrsep/">Kangiella koreensis RseP (KkRseP)</a> — Orthologous S2P used for comparative structural analysis
- <a href="/xray-mp-wiki/reagents/ligands/batimastat/">Batimastat</a> — Peptide-mimetic inhibitor bound in crystal structure
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/intramembrane-proteolysis/">Intramembrane Proteolysis</a> — EcRseP is a member of the S2P family of intramembrane proteases
- <a href="/xray-mp-wiki/concepts/protein-families/site-2-protease-family-mechanism/">Site-2 Protease Family Mechanism</a> — EcRseP is the defining bacterial group I S2P member
- <a href="/xray-mp-wiki/proteins/enzymes/glpg/">GlpG Rhomboid Intramembrane Protease</a> — Another intramembrane protease family with analogous gating mechanism
- <a href="/xray-mp-wiki/reagents/ligands/batimastat/">Batimastat</a> — Referenced in ecrsep text
- <a href="/xray-mp-wiki/reagents/additives/iptg/">Iptg</a> — Referenced in ecrsep text
- <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a> — Referenced in ecrsep text
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Referenced in ecrsep text
- <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> — Referenced in ecrsep text
