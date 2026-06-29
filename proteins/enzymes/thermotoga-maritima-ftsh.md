---
title: "Thermotoga maritima FtsH (Apo-FtsH AAA Protease)"
created: 2026-06-16
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [membrane-protein, enzyme, xray-crystallography]
sources: [doi/10.1073##pnas.0910708106]
verified: false
---

# Thermotoga maritima FtsH (Apo-FtsH AAA Protease)

## Overview

FtsH is a universally conserved membrane-anchored ATP-dependent zinc metalloprotease found in eubacteria, mitochondria, and chloroplasts. It belongs to the [AAA](/xray-mp-wiki/reagents/ligands/aaa/)+ (ATPases associated with various cellular activities) family and functions as a homo-hexameric complex where each polypeptide chain contains an N-terminal [AAA](/xray-mp-wiki/reagents/ligands/aaa/) domain and a C-terminal proteolytic domain. The crystal structure of the cytosolic region of apo-FtsH from Thermotoga maritima (Delta-tmFtsH K207A mutant, residues 147-610) was determined at 2.6 A resolution. In contrast to the ADP-bound state which shows a C2-symmetric [AAA](/xray-mp-wiki/reagents/ligands/aaa/) ring, the apo-state reveals a perfect 6-fold symmetric [AAA](/xray-mp-wiki/reagents/ligands/aaa/) ring with the crucial pore residues (Phe-234 of the FGV pore motif) lining an open circular entrance. Comparison of the apo- and ADP-bound structures reveals an inward movement of the aromatic pore residues of more than 45 A, generating a model of substrate translocation by [AAA](/xray-mp-wiki/reagents/ligands/aaa/)+ proteases. A substrate-binding edge beta strand (active-site switch, residues 450-460) appears within the proteolytic domain upon the conformational change. The G404L mutation in the linker region between [AAA](/xray-mp-wiki/reagents/ligands/aaa/) and protease domains inactivates FtsH by disrupting hexamerization.

## Publications

### doi/10.1073##pnas.0910708106

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3kds">3KDS</a></td>
      <td>2.6</td>
      <td>P622</td>
      <td>Delta-tmFtsH K207A (apo-state, nucleotide-free); residues 147-610 with K410L-K415A surface mutations</td>
      <td>none (apo-form)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: Delta-tmFtsH (amino acids 147-610 of FtsH from T. maritima with K410L-K415A surface mutations); K207A Walker A mutation to prevent nucleotide binding
- **Notes**: Point mutations introduced by modified overlap-extension protocol. Selenomethionine-incorporated protein produced by methionine biosynthesis inhibition method.


## Biological / Functional Insights

### C6-symmetric AAA ring in the apo-state

The apo-FtsH structure reveals a perfect 6-fold symmetry in both the [AAA](/xray-mp-wiki/reagents/ligands/aaa/) and protease rings, in contrast to the C2-symmetric [AAA](/xray-mp-wiki/reagents/ligands/aaa/) ring observed in the ADP-bound state. This transition from C2 to C6 symmetry involves changes in the inter-domain angle between protease and [AAA](/xray-mp-wiki/reagents/ligands/aaa/) moieties by some 40-60 degrees. The rearrangements of the [AAA](/xray-mp-wiki/reagents/ligands/aaa/) domains are largely of rigid body nature, with a smaller intradomain movement where the angle between the N-terminal wedge subdomain and the C-terminal helical subdomain increases by about 20 degrees due to nucleotide loss.

### Pore residue movement and substrate translocation model

The transition from ADP to apo-form causes movements of the conserved pore residue Phe-234 (part of the FGV pore motif) of more than 45 A. In the apo-state, the pore residues line an open circular entrance; in the ADP state, 4 of the 6 phenylalanines move inward in a staggered arrangement. This provides the first high-resolution image of the power stroke in [AAA](/xray-mp-wiki/reagents/ligands/aaa/)+ proteases and supports a model where ATP hydrolysis generates a mechanical force of approximately 150 pN through a 50 A movement, pulling the substrate polypeptide through the central pore.

### Active-site switch beta-strand formation

An active-site switch is formed by residues 450-460 in the proteolytic domain. In the ADP-bound state, this region adopts a helical conformation, while in the apo-state it forms a beta-strand that serves as a substrate-binding edge strand. This edge strand is proposed to fix the substrate polypeptide chain in an extended conformation around the scissile peptide bond, functioning similarly to edge strands in other zincin metalloproteases with HEXXH motifs.

### G404L mutation disrupts hexamerization and activity

The conserved [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) residue Gly-404 (Gly-399 in T. thermophilus) in the linker between [AAA](/xray-mp-wiki/reagents/ligands/aaa/) and protease domains is essential for FtsH function. The G404L mutation in T. maritima FtsH causes the protein to elute exclusively as a monomer from gel filtration, in contrast to the wild-type hexamer. This mutant is inactive in ATPase assays and possesses only very low proteolytic activity, demonstrating that the [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) provides necessary flexibility for interdomain communication and proper oligomeric assembly.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/aquifex-aeolicus-ftsh/">FtsH from Aquifex aeolicus</a> — Homologous FtsH protein with ADP-bound structure showing different AAA ring arrangement
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/aaa-protease-mechanism/">AAA Protease Mechanism</a> — FtsH is the founding member of the AAA+ protease family; this structure provides key mechanistic insights
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/glycine/">Glycine</a> — Buffer component used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/ligands/aaa/">AAA</a> — Related ligand or cofactor
