---

title: ADP/ATP Carrier (AAC)
created: 2026-04-27
updated: 2026-04-27
type: protein
tags: [transporter, pump]
sources: [doi/10.1016##j.cell.2018.11.025, doi/10.1016##J.FEBSLET.2005.09.061]

category: proteins
---
layout: default


# ADP/ATP Carrier (AAC)

## Overview

The mitochondrial ADP/ATP carrier (AAC, also known as SLC25A4-6 in humans) is the archetypal member of the mitochondrial carrier family. It transports ADP into the mitochondrial matrix for ATP synthesis and ATP out to the cytosol, recycling each ATP molecule more than a thousand times. It is estimated that every day this carrier transports body weight in ADP and ATP.

## Structure Determination

### Thermothelomyces thermophila TtAac (Cell 2018)

- **Matrix-open state (m-state)**: 3.3 Å resolution, BKA-inhibited, [nanobody](/reagents/antibodies/nanobody/)-stabilized
- **Space group**: Not specified (crystals composed of alternating carrier and nanobody layers)
- **Stability mutation**: Q302K in the cytoplasmic network (increases thermal stability)
- **Sequence identity**: 75% to *S. cerevisiae* ScAac2/ScAac3; 51% to bovine Aac1p

### Bovine Heart AAC (FEBS Lett. 2005)

- **Resolution**: 2.8 Å
- **Space group**: C222₁ (centered crystal form, salt-dependent)
- **PDB IDs**: 1OKC (P2₁2₁2, low salt), 2C3E (C222₁, low/no salt)
- **Inhibitor**: Carboxyatractyloside (CATR)
- **Construct**: Bovine heart mitochondrial AAC, residues 1–293 (residues 294–297 disordered)
- **Key finding**: Low salt (0–5 mM NaCl) during purification leads to centered crystal form with cardiolipin-mediated dimerization interfaces

## Structural Architecture

- **Transmembrane helices**: 6 helices (H1-H6)
- **Matrix helices**: h12, h34, h56 (inner helices)
- **Domains**: 3 homology domains, each with 2 transmembrane helices
- **Characteristic fold**: Three-domain structure typical of the mitochondrial carrier family
- **Substrate-binding site**: Located at the bottom of the central cavity, at the center of the membrane

## Conformational States

### Matrix-Open State (m-state) — BKA-inhibited
- Central cavity open to mitochondrial matrix side
- Matrix helices rotated outward
- Cytoplasmic side closed by cytoplasmic salt bridge network
- **Key residues closing cytoplasmic side**: D101, K104, D205, K208, D299, K302 (cytoplasmic salt bridge network)
- **Tyrosine braces**: YFxx[KR] motif on even-numbered helices, bracing the cytoplasmic network
- **Matrix helices**: glycine and small amino acid residues allow close-packing on matrix side

### Cytoplasmic-Open State (c-state) — CATR-inhibited
- Central cavity open to cytoplasmic side
- Matrix salt bridge network residues interacting, closing matrix side
- Cytoplasmic network residues far apart
- Previously solved: ScAac2 (PDB: 4C9H)

## Salt Bridge Networks

### Cytoplasmic Network (m-state)
- **Residues**: D101, K104, D205, K208, D299, K302
- **Braces**: R100-Y204 and Y298-D101 (YFxx[KR] motif)
- **Function**: Closes cytoplasmic gate in m-state; tyrosine braces provide additional stabilization beyond salt bridges
- **Mutation effects**: R100A, Y204A significantly reduce thermal stability; R100A, K104A, K208A mutations reduce transport rate

### Matrix Network (m-state)
- **Residues**: E37, K40, D142, R145, D242, R245
- **Glutamine braces**: Additional stabilization (Ruprecht et al., 2014)

## Cardiolipin-Mediated Dimerization (Bovine AAC)

The bovine AAC crystal structure (PDB: 2C3E) reveals a biologically relevant dimerization interface mediated by endogenous **[cardiolipin](/reagents/lipids/cardiolipin/)** molecules:

- **3 cardiolipins per AAC monomer** tightly bound to the protein
- Two cardiolipins (CDL801 and CDL802) are sandwiched between monomers on the matrix side
- **Intermonomer contact surface**: 446 Å² (with lipids) / 132 Å² (protein-protein only) between monomers A and B
- **Cardiolipin interactions**:
  - CDL801: interacts with I53, I54 (N-terminus of h1-2) and G272, A273, W274, S275 (junction of M3 and H6)
  - CDL802: interacts with L156, G157, N158 (h3-4) and G72, L74 (junction of M1 and H2)
  - Aromatic residues W70, Y173, F270 stack against acyl chains of cardiolipins
  - Indole nitrogens of W274 and W257 form H-bonds with cardiolipin branches
- **Crystal form dependence**: High salt (100 mM NaCl) yields primitive crystals (P2₁2₁2) with no biologically relevant dimerization; low salt (0–5 mM NaCl) yields centered crystals (C222₁) with cardiolipin-mediated dimers
- **Functional significance**: Cardiolipins are not essential for yeast growth but decrease AAC activity to 20% of wild-type when absent; they may transmit conformational changes between monomers during ADP/ATP exchange

## Transport Mechanism

**Domain rotation**: Unlike many transporters, AAC switches between states by **rotation of its three domains about a fulcrum provided by the substrate-binding site**. This is unique among known transport mechanisms.

The substrate-binding site (K30, R88, G192, I193, Y196, S238, R287) acts as a fulcrum. Substrate binding disrupts and reforms the salt bridge networks, driving the conformational transition between m-state and c-state.

## Solubilization and Purification

- **[lapao](/reagents/detergents/lapao/)** (3-laurylamido-N,N'-dimethylpropylaminoxyde, 2% w/v) — primary solubilization detergent from bovine heart mitochondria
- **Hydroxylapatite (HTP) [affinity-chromatography](/methods/purification/affinity-chromatography/)** — initial purification step
- **Gel filtration** — buffer containing 0 or 5 mM [sodium-chloride](/reagents/additives/sodium-chloride/) (salt concentration determines crystal form)
- **Bio-Beads** — detergent-to-protein ratio reduction
- **[amicon-filters](/methods/purification/amicon-filters/)** — concentration to ~5 mg/mL

## Crystallization

- **Method**: [vapor-diffusion](/methods/crystallization/vapor-diffusion/) (hanging drop)
- **Precipitant**: 28–32% [jeffamine](/reagents/additives/jeffamine/) M600 (Hampton Research)
- **Additives**: 10–20 mM NiSO₄ (or 5 mM [sodium-citrate](/reagents/additives/sodium-citrate/) + 50 mM Na arseniate)
- **Buffer**: 100 mM [hepes-buffer](/reagents/buffers/hepes-buffer/) pH 7.0 (or 100 mM [tris-buffer](/reagents/buffers/tris-buffer/) pH 8.5)
- **Temperature**: 20 °C
- **Crystal morphology**: Plate-shaped, 100 × 20 × 5 μm³

## Cross-References

- [nTMATE2-transporter](/proteins/nTMATE2-transporter.html) — Another transporter with multiple conformational states; [alternating-access](/concepts/alternating-access/) mechanism
- [lb-semisweet](/proteins/lb-semisweet.html) — Another alternating access transporter; conformational states captured
- [cardiolipin](/reagents/lipids/cardiolipin/) — Lipid that binds to AAC; stabilizes the carrier and mediates dimerization
- [bongkrekic-acid](/reagents/ligands/bongkrekic-acid/) — Inhibitor that locks the m-state
- [carboxyatractyloside](/reagents/ligands/carboxyatractyloside/) — Inhibitor that locks the c-state

## Related Transporters

- [sotb](/proteins/sotb.html) — E. coli antiporter (MFS family); nonlinear alternating access mechanism
- [nupg-nucleoside-transporter](/proteins/nupg-nucleoside-transporter.html) — MFS nucleoside transporter; alternating access
- [mfs-transporter](/concepts/mfs-transporter/) — Major facilitator superfamily