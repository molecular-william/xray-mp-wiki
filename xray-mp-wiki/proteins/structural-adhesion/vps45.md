---
title: "Vps45 (Cryptococcus thermophilum SM Protein)"
created: 2026-05-26
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.60724]
verified: regex
uniprot_id: G0S539
---

# Vps45 (Cryptococcus thermophilum SM Protein)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/G0S539">UniProt: G0S539</a>

<span class="expr-badge">Chaetomium thermophilum</span>

## Overview

Vps45 is a Sec1/Munc18-family (SM) protein from the filamentous fungus Cryptococcus thermophilum that functions as a SNARE chaperone in membrane trafficking from the endosome to the trans-Golgi network. The crystal structures of Vps45 alone and in complex with the Qa-SNARE [TLG2](/xray-mp-wiki/proteins/tlg2) reveal that Vps45 holds [TLG2](/xray-mp-wiki/proteins/tlg2) in an open conformation with its SNARE motif disengaged from its Habc domain, in contrast to the closed (clamped) conformation observed for Munc18-1 with syntaxin-1. Vps45 rescues [TLG2](/xray-mp-wiki/proteins/tlg2) from homo-tetrameric oligomers into stoichiometric 1:1 complexes and its unfurled domain 3a helical hairpin exposes the presumptive R-SNARE binding site for template complex assembly.

## Publications

### doi/10.7554##eLife.60724

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6xjl">6XJL</a></td>
      <td>2.00 A</td>
      <td>P212121</td>
      <td>C. thermophilum Vps45 (XP_006692860.1 homolog) alone, full-length cytoplasmic domain</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6xmd">6XMD</a></td>
      <td>3.88 A</td>
      <td>P21221</td>
      <td>C. thermophilum Vps45 in complex with Qa-SNARE Tlg2 (residues 1-310) cytoplasmic domain</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6xm1">6XM1</a></td>
      <td>2.80 A</td>
      <td>P212121</td>
      <td>C. thermophilum Vps45 in complex with full-length Qa-SNARE Tlg2 (residues 1-327) cytoplasmic domain</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21 Rosetta (Novagen) for Vps45 alone; E. coli BL21-Codon Plus (Agilent) for [TLG2](/xray-mp-wiki/proteins/tlg2) and Vps45-[TLG2](/xray-mp-wiki/proteins/tlg2) co-expression
- **Construct**: Vps45 with N-terminal His7 tag for individual expression, or C-terminal His7 tag for co-expression with Tlg2. All constructs cloned into pQLink bacterial expression plasmids. Tlg2 constructs carried N-terminal His7 and MBP tags followed by TEV protease cleavage site. Mutations (V306D, F335R, L258M, I272M) introduced using QuikChange mutagenesis (Agilent). Vps45 overproduced at 25 C for 18 hr; Tlg2 and Vps45-Tlg2 co-expression at 16 C.

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
      <td>Cell lysis</td>
      <td>Pressure homogenization (Emulsiflex-C5, Avestin)</td>
      <td>--</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">beta-Mercaptoethanol</a> + --</td>
      <td>Cell pellets resuspended in lysis buffer supplemented with 1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf">PMSF</a> and 10 ug/mL DNase. Clarified by centrifugation at 30,000 g.</td>
    </tr>
    <tr>
      <td>Ni-affinity chromatography</td>
      <td>Ni-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>His60 Ni Superflow Resin (ClonTech)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 100 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">beta-Mercaptoethanol</a> (wash); 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> in wash buffer (elution) + --</td>
      <td>Resin washed with wash buffer, eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>. Performed on ice or at 4 C.</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>Superdex 200 HR 16/60 (GE Healthcare)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris-hcl">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 5 mM dithiothreitol (<a href="/xray-mp-wiki/reagents/additives/dtt">DTT</a>) + --</td>
      <td>Gel filtration buffer. Final purification step.</td>
    </tr>
    <tr>
      <td>Tag cleavage (<a href="/xray-mp-wiki/proteins/tlg2">TLG2</a> constructs)</td>
      <td>Protease digestion (TEV protease)</td>
      <td>His60 Ni Superflow (cleaved His7-MBP tags removed)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>, 50 mM NaCl + --</td>
      <td>TEV protease cleavage site present between tags and protein for tag removal.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion with streak seeding</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Vps45-<a href="/xray-mp-wiki/proteins/tlg2">TLG2</a>(1-327) complex at 4 mg/ml in 25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 8.0, 50 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M potassium <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a>, 14% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a> 3350, 5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>~3 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>1:1 mixture of well buffer supplemented with 30% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, then frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Diamond-shaped crystals in P212121 space group with two complexes in the asymmetric unit. Improved by streak seeding with Vps45-<a href="/xray-mp-wiki/proteins/tlg2">TLG2</a> crystals. Data collected at NSLSII FMX beamline.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Vps45-<a href="/xray-mp-wiki/proteins/tlg2">TLG2</a>(1-310) complex at 4 mg/ml in 25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 8.0, 50 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M potassium <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a>, 14% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a> 3350, 5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>~3 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>1:1 mixture of well buffer supplemented with 30% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, then frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>P21221 crystal form with single complex in the asymmetric unit. Streak seeded with Vps45-<a href="/xray-mp-wiki/proteins/tlg2">TLG2</a> crystals.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Vps45-V306D,F335R-<a href="/xray-mp-wiki/proteins/tlg2">TLG2</a> complex at 4 mg/ml</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M potassium <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a>, 14% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a> 3350, 5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a></td>
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
      <td>1:1 mixture of well buffer supplemented with 30% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, then frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Mutant Vps45-V306D,F335R in complex with <a href="/xray-mp-wiki/proteins/tlg2">TLG2</a>. P21 crystal form.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SeMet-labeled Vps45-<a href="/xray-mp-wiki/proteins/tlg2">TLG2</a>(L258M,I272M) complex at 5 mg/ml in 0.1 M <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 0.2 M NaCl, 10% 2-propanol, 5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 0.2 M NaCl, 10% (v/v) 2-propanol, 5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>~3 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>1:1 mixture of well buffer supplemented with 30% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> plus 10% (v/v) 2-propanol, then frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>SeMet-labeled for SAD phasing. L258M and I272M mutations confirmed sequence register in SNARE helix. P212121 crystal form.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>X-ray crystallography</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Native Vps45 at ~4 mg/ml</td>
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
      <td>Vps45 alone crystallized in P212121 space group. Data collected at CHESS F1 beamline (0.9782 A wavelength). Resolution 2.00 A.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Vps45 holds Qa-SNARE Tlg2 in an open conformation

Unlike Munc18-1 which clamps syntaxin-1 in a closed conformation where the Habc domain folds back onto the SNARE motif, Vps45 holds [TLG2](/xray-mp-wiki/proteins/tlg2) in an open conformation. The Habc domain makes only a limited contact with the SNARE motif at approximately 45 degrees, and the linker between Habc and SNARE motif is disordered/unfolded. The N-peptide of [TLG2](/xray-mp-wiki/proteins/tlg2) (residues 1-14) binds to the outside of Vps45 domain 1 burying 870 A^2 of surface area, while layers 0 to +4 of the SNARE motif interact with the cleft-facing side of Vps45 domain 1 burying about 930 A^2. The Habc domain interacts with the cleft side of Vps45 domain 1 burying 680 A^2. This demonstrates that Qa-SNARE clamping is a specialized property of Munc18 rather than a general property shared among SM proteins.

### Vps45 prevents Tlg2 homo-oligomerization by rescuing tetramers

[TLG2](/xray-mp-wiki/proteins/tlg2) has a pronounced tendency to form homo-tetramers driven by SNARE motif bundling, as shown by size-exclusion chromatography and sedimentation velocity analytical ultracentrifugation (experimental MW 33.8 kDa vs expected 33.6 kDa for tetramer). The Habc domain alone ([TLG2](/xray-mp-wiki/proteins/tlg2) residues 79-200) sediments as a monomer. Vps45 can rescue [TLG2](/xray-mp-wiki/proteins/tlg2) tetramers into stoichiometric 1:1 complexes, presumably by trapping transiently dissociated monomers. The [TLG2](/xray-mp-wiki/proteins/tlg2) N-peptide is required for this rescue, as N-terminally truncated [TLG2](/xray-mp-wiki/proteins/tlg2) constructs form oligomers that neither bind to nor are rescued by Vps45. Vps45 protects [TLG2](/xray-mp-wiki/proteins/tlg2) from oligomerization by binding to layers 0 to +4 of the SNARE motif.

### Vps45 domain 3a helical hairpin is unfurled and primed for R-SNARE binding

The domain 3a helical hairpin of Vps45 adopts an unfurled, extended conformation in the [TLG2](/xray-mp-wiki/proteins/tlg2)-bound state, exposing the presumptive R-SNARE binding site. This contrasts with the Munc18-Stx1 complex where the hairpin is furled and the R-SNARE binding site is concealed. The unfurled conformation is also seen in Vps33 bound to SNARE motifs, suggesting it may be a well-defined active conformation for SM proteins. The Vps45-[TLG2](/xray-mp-wiki/proteins/tlg2) complex appears primed to bind an R-SNARE (such as Snc2) and catalyze SNARE complex assembly via a template mechanism.

### SM proteins use at least two distinct modes to engage Qa-SNAREs

The Vps45-[TLG2](/xray-mp-wiki/proteins/tlg2) structure establishes that SM proteins can engage the N-peptide, Habc domain, and SNARE motif of a cognate Qa-SNARE without simultaneously clamping that SNARE in a closed conformation. This reveals a second mode of SM-Qa-SNARE interaction beyond the Munc18-Stx1 closed clamp. It is possible that the open mode is the rule and the Munc18 clamp mode is the exception. Munc13-1, which mediates Stx opening in neurons, may function by converting the Munc18-Stx complex into a Vps45-[TLG2](/xray-mp-wiki/proteins/tlg2)-like conformation.


## Cross-References

- <a href="/xray-mp-wiki/proteins/structural-adhesion/tlg2/">Tlg2 (Cryptococcus thermophilum Qa-SNARE Protein)</a> — Cognate Qa-SNARE partner co-crystallized with Vps45 in PDB entries 6XMD and 6XM1; forms 1:1 complexes with Vps45
- <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">beta-Mercaptoethanol</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/pmsf">PMSF</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/dtt">DTT</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> — Entity mentioned in text
