---
title: "Heliorhodopsin 48C12 from actinobacterial fosmid (Lake Kinneret)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.1915888117]
verified: agent
---

# Heliorhodopsin 48C12 from actinobacterial fosmid (Lake Kinneret)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


## Overview

HeR-48C12 is a bacterial heliorhodopsin (HeR) discovered in an actinobacterial fosmid from freshwater Lake Kinneret and is the founding member of heliorhodopsin subfamily 1. Like other HeRs, it exhibits reverse membrane topology with the N terminus facing the cytoplasm and shares less than 15% sequence identity with type-1 microbial rhodopsins. Two crystal structures were solved at 1.5 A resolution, a violet form at pH 8.8 and a blue form at pH 4.3. The structures reveal a remarkably different organization from all known rhodopsins, with a completely hydrophobic extracellular interior and a large hydrophilic Schiff base cavity (SBC) in the cytoplasmic part containing a cluster of six water molecules that likely serves as the primary proton acceptor from the retinal Schiff base. At acidic pH, a planar triangular molecule (acetate from the crystallization buffer) occupies the SBC. HeR-48C12 does not function as a proton pump or ion channel; the photocycle involves a water cluster as the proton acceptor rather than a specific amino acid side chain. The structure enabled identification of 10 HeR subfamilies through structure-based bioinformatic analysis.


## Publications

### doi/10.1073##pnas.1915888117

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6su3">6SU3</a></td>
      <td>1.5 A</td>
      <td>P2_1</td>
      <td>Full-length HeR-48C12 with C-terminal 6x His tag, expressed in E. coli</td>
      <td>all-trans retinal (covalently bound via Schiff base to Lys238)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6su3">6SU3</a></td>
      <td>1.5 A</td>
      <td>P2_1</td>
      <td>Full-length HeR-48C12 with C-terminal 6x His tag</td>
      <td>all-trans retinal, acetate ion</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: HeR-48C12 with C-terminal 6x His tag
- **Induction**: 0.1 mM IPTG at 26 C overnight; additional 150 ug/mL ampicillin maintained every 2 h
- **Media**: LB medium supplemented with 20 uM all-trans retinal and 150 ug/mL ampicillin

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
      <td>Cell disruption</td>
      <td>Microfluidizer homogenization</td>
      <td>—</td>
      <td>30 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> pH 8.0, 0.3 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.04% Triton X-100</td>
      <td>Cells disrupted at 20,000 psi with M-110P homogenizer. DNase I and protease inhibitors added.</td>
    </tr>
    <tr>
      <td>Membrane isolation</td>
      <td>Ultracentrifugation</td>
      <td>—</td>
      <td>30 mM Tris-HCl pH 8.0, 0.3 M NaCl</td>
      <td>Total lysate centrifuged at 120,000 rcf. Membranes isolated and dispensed in buffer with 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">[DDM</a>](/xray-mp-wiki/reagents/detergents/n-dodecyl-beta-d-maltoside/) and 5 mM all-trans <a href="/xray-mp-wiki/reagents/ligands/retinal/">Retinal</a>.</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>30 mM Tris-HCl pH 8.0, 0.3 M NaCl, 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Membranes stirred overnight at 4 C. Insoluble fraction removed by ultracentrifugation at 120,000 rcf for 1 h.</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta/) agarose (Cube Biotech)</td>
      <td>30 mM Tris-HCl pH 8.0, 0.3 M NaCl, 0.05% Triton, 0.2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Washed with 3 CV WB1 (10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>), then WB2 (50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>). Eluted with 250 mM L-histidine in buffer pH 7.8.</td>
    </tr>
    <tr>
      <td>Size exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td>Superdex200 Increase 10/300 GL (GE Healthcare)</td>
      <td>30 mM Tris-HCl, 50 mM NaPi pH 7.8, 300 mM NaCl, 0.5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 2 mM 6-aminohexanoic acid, 0.075% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.075% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Fractions with peak ratio ~1.25 collected and concentrated to 20 mg/mL</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> crystallization (in meso)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified 48C12 at 20 mg/mL in DDM solution, reconstituted into monoolein-based <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a></td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293 K (20 C)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2 weeks</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Rhombic crystals reached 150 um in length and width, maximum thickness 20 um. Crystals grown at both pH 8.8 (violet form) and pH 4.3 (blue form). Crystal packing same for both, with one 48C12 dimer in asymmetric unit. P2_1 symmetry.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Reverse membrane topology and unique overall architecture

HeR-48C12 has the N terminus facing the cytoplasm, opposite to all known type-1 and type-2 rhodopsins. The N-terminal cytoplasmic orientation is a hallmark of the heliorhodopsin family. The AB loop (residues 34-64) forms a ~40 A long beta-sheet extending toward the second protomer of the dimer, covering the extracellular surface of the neighboring molecule.

### Schiff base cavity (SBC) and water cluster as proton acceptor

A large hydrophilic cavity (SBC) is present near the retinal Schiff base, between residues Glu107 and Arg104, filled with six water molecules at pH 8.8. The SBC is surrounded by highly conserved charged residues (His23, His80, Arg104, Glu107, Glu230) and polar residues (Asn16, Tyr92, Asn101, Tyr108, Ser237) interconnected by an extensive hydrogen bonding network. Mutational analysis showed that none of the charged amino acids surrounding the SBC act as the primary proton acceptor. The water cluster itself is proposed to serve as the proton reservoir after RSB deprotonation during the photocycle.

### Hydrophobic extracellular interior prevents proton transfer

The extracellular part of HeR-48C12 is completely hydrophobic, with no charged or polar amino acids in the internal region. This explains the absence of proton/ion pumping activity. The hydrophobic barrier makes transfer of the RSB proton to the extracellular side energetically unfavorable, supporting the model where the proton remains in the cytoplasmic SBC during the photocycle.

### Acetate binding at acidic pH

At pH 4.3, a planar triangular acetate molecule from the crystallization buffer binds in the SBC, hydrogen bonded to the neutralized Glu107 side chain and two water molecules. The acetate does not interact directly with the RSB, explaining only small shifts in absorption wavelength. The anion binding is only possible when Glu107 is protonated at low pH, consistent with spectroscopy showing no acetate effects at neutral pH.

### Structure-based classification into 10 HeR subfamilies

Using the 48C12 structure, 10 subfamilies of heliorhodopsins were identified from 479 unique HeR sequences. Subfamily 1 (48C12 group) is the largest with 195 proteins, mostly from Actinobacteria, Chloroflexi, Firmicutes, Proteobacteria, and PVC group. Key conserved regions include the RSB-stabilizing residues (Ser237, Glu107, Ser111, Ser76), SBC residues, and the hydrophobic extracellular organization.

### Dimer interface organization

48C12 forms a dimer via helices D and E with a broad hydrophobic interface in the middle part and polar interactions (Asp127-Tyr179 and Tyr151-Asp158) at the extracellular and cytoplasmic sides respectively. The AB loop is stabilized by hydrogen bonds mediated by water molecules on the extracellular surface.


## Cross-References

- <a href="/xray-mp-wiki/proteins/rhodopsins/heliorhodopsin-taher/">Heliorhodopsin (TaHeR)</a> — Archaeal heliorhodopsin homolog; structures compared with 48C12 (RMSD 0.66 A)
- <a href="/xray-mp-wiki/proteins/rhodopsins/bacteriorhodopsin/">Bacteriorhodopsin</a> — Prototypical type-1 rhodopsin; structural comparison reveals key differences in HeR organization
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/heliorhodopsin-schiff-base-cavity/">Heliorhodopsin Schiff Base Cavity</a> — The SBC is a defining structural and functional feature of HeR-48C12
- <a href="/xray-mp-wiki/concepts/rhodopsin-mechanisms/rhodopsin-photocycle/">Rhodopsin Photocycle</a> — 48C12 exhibits a photocycle with K, M, and O intermediates; water cluster serves as proton acceptor
- <a href="/xray-mp-wiki/reagents/ligands/retinal/">All-trans Retinal</a> — Covalently bound chromophore via Schiff base to Lys238
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid used in LCP crystallization matrix
