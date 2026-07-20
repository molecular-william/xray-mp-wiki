---
title: "KtrA (Cytosolic Regulatory Protein from Bacillus subtilis)"
created: 2026-06-03
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature12055]
verified: agent
uniprot_id: O32080
---

# KtrA (Cytosolic Regulatory Protein from Bacillus subtilis)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O32080">UniProt: O32080</a>

<span class="expr-badge">Bacillus subtilis</span>

## Overview

KtrA is a cytosolic regulatory protein from the bacterium Bacillus subtilis that forms an octameric ring and associates with the [KTRB](/xray-mp-wiki/proteins/pumps-atpases/ktrb/) membrane protein to form the KtrAB potassium transporter complex. KtrA contains RCK (Regulator of K+ conductance) domains and binds ATP and ADP with a strong preference for ATP. Ligand binding induces a ligand-dependent conformational change in the octameric ring: ATP binding produces a four-fold symmetric square conformation, while ADP binding produces a two-fold symmetric diamond conformation. In full-length KtrA, ATP binding induces unique intradimer interactions that determine the conformation of the octameric ring, contrasting with truncated KtrA where ligand binding and ring conformation are uncoupled.


## Publications

### doi/10.1038##nature12055

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4j90">4J90</a></td>
      <td>3.2</td>
      <td>Not specified</td>
      <td>Full-length KtrA octameric ring bound to ATP</td>
      <td>ATP</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4j91">4J91</a></td>
      <td>2.9</td>
      <td>Not specified</td>
      <td>Full-length KtrA octameric ring bound to ADP</td>
      <td>ADP</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21(DE3)
- **Construct**: Tag-less KtrA from Bacillus subtilis
- **Notes**: Overexpressed in LB media at 20°C for 14-16 h after [IPTG](/xray-mp-wiki/reagents/additives/iptg/) induction

**Purification:**

- **Expression system**: E. coli BL21(DE3)
- **Expression construct**: Tag-less KtrA from Bacillus subtilis

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
      <td>Cell lysis</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 50 mM KCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a></td>
      <td>Cells lysed in Buffer C</td>
    </tr>
    <tr>
      <td>Anion exchange chromatography</td>
      <td>Ion-exchange chromatography</td>
      <td>Anion exchange column</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 50 mM KCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a></td>
      <td>Cleared lysate loaded into anion exchange column</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (ADP-agarose)</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (ADP-agarose matrix)</td>
      <td>ADP-agarose resin (Innova Biosciences)</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a>, 150 mM KCl, 1 mM TCEP</td>
      <td>Incubated overnight at 4°C; eluted with 5 mM adenosine-containing nucleotide</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>Superdex-S200 column</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: ~3 mg/ml in appropriate buffer

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>KtrA-ATP octamer, concentrated to ~10 mg/ml, run on SEC in Buffer F</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM HEPES pH 7.5, 3% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 6000, 2.5% <a href="/xray-mp-wiki/reagents/additives/mpd/">MPD</a> (2-methyl-2,4-pentanediol)</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Flash-frozen in liquid nitrogen after transfer to mother liquor containing 6% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 6000 and 30% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>KtrA-ADP octamer, concentrated to ~10 mg/ml, run on SEC in Buffer F</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> pH 5.6, 14.5% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 20000</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Flash-frozen in liquid nitrogen</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### ATP-dependent octameric ring conformation

KtrA octameric rings adopt different conformations depending on the bound nucleotide. The KtrA-ATP ring adopts a four-fold symmetric square conformation, whereas the KtrA-ADP ring adopts a two-fold symmetric diamond conformation. This conformational difference is also observed in solution through controlled proteolysis. The gamma- phosphate in ATP occupies the position taken by the beta-phosphate in ADP, accomplished by a shift in G79 and repositioning of the alpha- and beta-phosphates.

### Intradimer interactions mediated by ATP

In the ATP structure, the gamma-phosphate interacts with R16 from its own binding site, while the beta-phosphate interacts with R16 from the neighbouring KtrA subunit binding site. This intradimer interaction brings the two binding sites within a KtrA dimer together through a ~16 degree change in the angle between subunits. The distances separating the conserved D36 in the two binding pockets are ~35 A in the ADP structure and ~30 A in the ATP structure. The absence of the gamma-phosphate in ADP results in lack of ligand-mediated intradimer interactions and relaxation of the ring.

### Full-length vs truncated KtrA conformational coupling

In truncated KtrA (composed of N lobe alone), ligand binding and ring conformation are uncoupled. In contrast, full-length KtrA exhibits conformational coupling: ATP binding induces a unique set of intradimer interactions that determine the conformation of the octameric ring. This suggests that the C-terminal portion of full-length KtrA is essential for transmitting the ligand-binding signal to the ring conformation.

### Asymmetric ring contraction upon ATP binding

Unlike [MTHK](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) and BK channels where RCK rings expand symmetrically upon binding of activating ligands, the KtrA ring in KtrAB contracts asymmetrically upon ATP binding. In KtrAB, the cytoplasmic loops of the [KTRB](/xray-mp-wiki/proteins/pumps-atpases/ktrb/) homodimer mediate the interaction with the KtrA (RCK) ring, and the ring undergoes asymmetric conformational changes along the diagonal defined by the lateral contacts or tip contacts. This represents a fundamentally different activation mechanism compared to covalently tethered RCK channels.

### Ligand specificity of KtrA

KtrA has a strong binding preference for ATP and ADP over other small molecules, resembling other KtrA proteins. Functional assays with 86Rb+ uptake show that ATP markedly increases flux compared to ADP or [KTRB](/xray-mp-wiki/proteins/pumps-atpases/ktrb/) alone, supporting previous cell-based results showing that ATP is an activator of KtrAB. The functional effect of ATP and ADP was evaluated in liposome reconstitution assays with excess KtrA to minimize formation of the KtrB-KtrA-[KTRB](/xray-mp-wiki/proteins/pumps-atpases/ktrb/) complex.


## Cross-References

- <a href="/xray-mp-wiki/proteins/pumps-atpases/ktrb/">KtrB (Potassium Transporter Membrane Subunit from Bacillus subtilis)</a> — KtrB forms the homodimeric membrane component that associates with KtrA octameric ring to form the functional KtrAB transporter
- <a href="/xray-mp-wiki/reagents/ligands/atp/">Adenosine Triphosphate (ATP)</a> — ATP is the primary activating ligand that binds to KtrA and induces square conformation of the octameric ring
- <a href="/xray-mp-wiki/reagents/ligands/adp/">Adenosine Diphosphate (ADP)</a> — ADP binds to KtrA and induces diamond conformation of the octameric ring, with lower activating effect
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES (4-(2-Hydroxyethyl)-1-piperazineethanesulfonic Acid)</a> — HEPES buffer (pH 7.5) used in KtrA-ATP crystallization
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer (Sodium Citrate)</a> — Citrate buffer (pH 5.6) used in KtrA-ADP crystallization
- <a href="/xray-mp-wiki/reagents/additives/tcep/">Tris-(2-carboxyethyl)phosphine (TCEP)</a> — TCEP used as reducing agent in KtrA purification buffer
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rck-domain-activation-mechanism/">RCK Domain Activation Mechanism</a> — KtrA RCK domains form an octameric gating ring with asymmetric contraction mechanism, distinct from MthK/BK symmetric expansion
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/voltage-gated-channels/mthk/">MTHK</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> — Additive used in purification or crystallization buffers
