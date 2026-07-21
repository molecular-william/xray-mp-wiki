---
title: "Kangiella koreensis Site-2 Protease Homolog (KkRseP)"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1126##sciadv.abp9011]
verified: agent
---

# Kangiella koreensis Site-2 Protease Homolog (KkRseP)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


## Overview

KkRseP is an ortholog of E. coli RseP from the marine bacterium Kangiella koreensis (strain DSM 16069). It is a group I site-2 protease (S2P) family member that performs [Intramembrane Proteolysis](/xray-mp-wiki/concepts/membrane-mimetics/intramembrane-proteolysis/). KkRseP restored the growth deficiency of E. coli rseP mutant cells and cleaved substrates containing TM segments from E. coli RseA, confirming functional conservation. Crystal structures were determined in two crystal forms in complex with [Batimastat](/xray-mp-wiki/reagents/ligands/batimastat/), revealing a PDZ-open conformation distinct from the PDZ-closed conformation of [ECRSEP](/xray-mp-wiki/proteins/enzymes/ecrsep/), suggesting domain rearrangements may occur during substrate accommodation.


## Publications

### doi/10.1126##sciadv.abp9011

**Expression:**

- **Expression system**: E. coli C43(DE3) with pRARE2
- **Construct**: Full-length KkRseP with C-terminal TEV-His8 tag
- **Induction**: 0.1 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) at 16°C for 18 hours
- **Media**: LB medium (native) or M9 medium (SeMet) with 50 ug/ml [Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) and 34 ug/ml [Chloramphenicol](/xray-mp-wiki/reagents/antibiotics/chloramphenicol/)

**Purification:**

- **Expression system**: E. coli C43(DE3) + pRARE2
- **Tag info**: C-terminal TEV-His8, cleaved with TEV for crystallization

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
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.4, 150 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a></td>
      <td>Lysed cells centrifuged at 20,000g for 30 min, supernatant ultracentrifuged at 200,000g for 60 min</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>40 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Incubation at 4°C for 1 hour</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) agarose</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Wash with 50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, elute with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td><a href="/xray-mp-wiki/reagents/additives/tev-protease/">TEV Protease</a> cleavage</td>
      <td>—</td>
      <td></td>
      <td>His8 tag cleaved by <a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease overnight at 20°C; dialyzed against 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> buffer</td>
    </tr>
    <tr>
      <td>Reverse Ni-NTA</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> (flow-through)</td>
      <td>—</td>
      <td></td>
      <td>Tag-cleaved KkRseP collected in unbound fraction</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 10/300 GL</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/batimastat/">Batimastat</a> added to <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> buffer</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion</a> (sitting drop)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>KkRseP-<a href="/xray-mp-wiki/reagents/ligands/batimastat/">Batimastat</a> complex</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20°C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Two crystal forms obtained: space group P1 (3.10 A) and P2_1 (3.15 A); SeMet-substituted protein used for phasing; data collected at SPring-8 BL32XU</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
    <tr>
      <td>Variant</td>
      <td>sitting-drop</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### PDZ-open conformation

The KkRseP structures revealed a PDZ-open conformation where the PDZ tandem is positioned further from the PCT region compared to [ECRSEP](/xray-mp-wiki/proteins/enzymes/ecrsep/). The C-terminal part of PCT (PCT-loop and H2) is disordered, and TM4 moves away to interact with the cleft between TM1 and TM3-N of a crystal packing neighbor, potentially mimicking substrate binding.

### Functional conservation across species

KkRseP cleaves E. coli RseA substrate and restores rseP mutant growth, demonstrating functional conservation despite ~1.34 A RMSD in domain arrangement compared to [ECRSEP](/xray-mp-wiki/proteins/enzymes/ecrsep/).


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/ecrsep/">Escherichia coli RseP (EcRseP)</a> — Orthologous S2P used for comparative structural analysis; both determined in same study
- <a href="/xray-mp-wiki/reagents/ligands/batimastat/">Batimastat</a> — Peptide-mimetic inhibitor bound in crystal structure
- <a href="/xray-mp-wiki/concepts/membrane-mimetics/intramembrane-proteolysis/">Intramembrane Proteolysis</a> — KkRseP is a member of the S2P family of intramembrane proteases
- <a href="/xray-mp-wiki/concepts/protein-families/site-2-protease-family-mechanism/">Site-2 Protease Family Mechanism</a> — Structural comparison provided insights into group I S2P mechanism
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
