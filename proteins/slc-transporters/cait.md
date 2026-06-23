---
title: CaiT Carnitine Antiporter from Escherichia coli
created: 2026-06-05
updated: 2026-06-08
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsmb.1788, doi/10.1038##NATURE09310, doi/10.1073##pnas.1309071110]
verified: false
---

# CaiT Carnitine Antiporter from Escherichia coli

## Overview

CaiT is an [L-Carnitine](/xray-mp-wiki/reagents/ligands/l-carnitine/)/[Gamma-Butyrobetaine (4-Trimethylaminobutyrate)](/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/) antiporter from Escherichia coli that belongs to the betaine/[Choline](/xray-mp-wiki/reagents/substrates/choline/)/carnitine transporter (BCCT) family. Unlike other BCCT family members which are Na+/H+-dependent symporters, CaiT functions as a precursor/product antiporter independently of the ion gradient. The crystal structure at 3.15 A resolution reveals a homotrimeric complex with each protomer containing 12 transmembrane helices and 4 [L-Carnitine](/xray-mp-wiki/reagents/ligands/l-carnitine/) molecules outlining the transport pathway across the membrane. High-resolution structures of CaiT from Proteus mirabilis (PmCaiT, 2.3 A) and E. coli (EcCaiT, 3.5 A) revealed the fully open inward-facing conformation and demonstrated a Na+-independent mechanism in which a methionine sulphur (Met331) coordinates the substrate in place of a sodium ion. Mutagenesis studies identified a primary binding site at the center of the protein and a secondary substrate-binding site at the bottom of the intracellular vestibule, providing mechanistic insights into the antiport process. The structures also revealed a regulatory extracellular substrate-binding site that mediates cooperative substrate binding with Hill coefficients up to 1.7.


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nsmb.1788 | 3HFX | 3.15 A | P6(3) | CaiT from E. coli, residues 12-504, C-terminal GFP-His10 tag with TEV cleavage site, Met353 mutated to Leu; homotrimer | [L-Carnitine](/xray-mp-wiki/reagents/ligands/l-carnitine/) (4 molecules per protomer) |
| doi/10.1038##NATURE09310 | unknown | 2.3 A | not specified | PmCaiT from Proteus mirabilis, full-length; [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/)-substituted; inward-open fully open conformation | none (transport site occupied by Trp323 side chain) |
| doi/10.1038##NATURE09310 | unknown | 3.5 A | not specified | EcCaiT from E. coli, full-length; inward-open conformation with bound [Gamma-Butyrobetaine (4-Trimethylaminobutyrate)](/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/) substrate | [Gamma-Butyrobetaine (4-Trimethylaminobutyrate)](/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/) (central transport site + extracellular binding pocket) |
| doi/10.1073##pnas.1309071110 | unknown | 3.29 A | not specified | PmCaiT R262E mutant from Proteus mirabilis; inward-open substrate-bound conformation; solved by molecular replacement using PDB 2WSW | [Gamma-Butyrobetaine (4-Trimethylaminobutyrate)](/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/) (rotated orientation with carboxyl group contacting unwound TM1') |

## Expression and Purification

- **Expression system**: Escherichia coli C41
- **Construct**: CaiT from E. coli cloned into pET28-derivative vector with C-terminal GFP-His10 tag and TEV protease cleavage site; Met353 mutated to Leu by sequencing; cultured in Terrific broth, induced with 0.3 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) at 18 C for 20 h

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell membrane isolation | Cell lysis and membrane fractionation | not applicable | not specified + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Cells cultured in Terrific broth, induced with 0.3 mM [IPTG (Isopropyl-beta-D-thiogalactopyranoside)](/xray-mp-wiki/reagents/additives/iptg/) at 18 C for 20 h; membranes isolated from disrupted C41 cells |
| Membrane solubilization | Detergent solubilization | not applicable | not specified + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (1% w/v) | Membranes solubilized with 1% (w/v) n-dodecyl beta-D-maltoside (DDM) |
| Metal affinity chromatography (first pass) | Ni-NTA metal ion affinity chromatography | Ni-NTA | 20 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 300 mM NaCl, 200 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/), 0.05% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | GFP-CaiT eluted from Ni-NTA column; contains C-terminal GFP-His10 tag |
| TEV protease cleavage | Protease digestion | not applicable | not specified + not specified | TEV protease cleavage site between GFP-His10 and CaiT; removes GFP-His10 tag |
| Metal affinity chromatography (second pass) | Ni-NTA metal ion affinity chromatography | Ni-NTA | not specified + not specified | Second Ni-column separates CaiT from TEV-His and GFP-His; CaiT flows through |
| Size exclusion chromatography | Size exclusion chromatography | Superdex 200 10/300 GL column (GE Healthcare) | 50 mM [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/)-NaOH pH 7.5, 150 mM NaCl, 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Final SEC purification; concentrated to 10 mg/ml using 100-kDa Amicon Ultra-4 tube at 4 C |


## Crystallization

### doi/10.1038##nsmb.1788

| Parameter | Value |
|---|---|
| Method | Hanging-drop vapor diffusion |
| Protein sample | CaiT at 10 mg/ml in 0.03% [DDM](/xray-mp-wiki/reagents/detergents/ddm/) |
| Reservoir | 0.1 M [HEPES Buffer](/xray-mp-wiki/reagents/buffers/hepes/)-NaOH pH 7.5, 20-26% (v/v) [Polyethylene Glycol 400 (PEG 400)](/xray-mp-wiki/reagents/peg-400/), 0.1 M NaCl, 18 mM N-octyl-beta-D-glucopyranoside, 5 mM [L-Carnitine](/xray-mp-wiki/reagents/ligands/l-carnitine/) |
| Temperature | 20 C |
| Growth time | not specified |
| Notes | Crystals grown by hanging-drop vapor diffusion at 20 C. Heavy atom derivatives obtained by soaking crystals in mother liquor containing 5 mM ethylmercurithiosalicylic acid and sodium salt. Cryoprotected with reservoir solution containing 30% [Polyethylene Glycol 400 (PEG 400)](/xray-mp-wiki/reagents/peg-400/), 0.020% [DDM](/xray-mp-wiki/reagents/detergents/ddm/), and 10 mM N-octyl-beta-D-glucopyranoside. Space group P6(3), cell dimensions a=b=134.2 A, c=85.1 A, alpha=beta=90 deg, gamma=120 deg. Phased by SIRAS using [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) peak-wavelength (1.0039 A) dataset. Model contains residues 12-504, nine [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury/) atoms, and four [L-Carnitine](/xray-mp-wiki/reagents/ligands/l-carnitine/) molecules. Rwork/Rfree = 0.262/0.281. |


## Biological / Functional Insights

### BCCT family antiporter with unique Na+-independent mechanism

CaiT belongs to the betaine/[Choline](/xray-mp-wiki/reagents/substrates/choline/)/carnitine transporter (BCCT) family but functions as a precursor/product antiporter independently of the ion gradient, unlike all other BCCT members which are Na+ or H+ dependent symporters. The conserved Na+-binding motif (Gly-X-Gly in TM3) is altered to Cys-Thr-Ser in CaiT, and key Na+-coordinating residues from [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/) are mutated (Ser468 to Leu422 in TM10, Met310 to Ser263 in TM7), disrupting the Na+-binding site.

### Four L-carnitine binding sites outline transport pathway

The crystal structure reveals four [L-Carnitine](/xray-mp-wiki/reagents/ligands/l-carnitine/) molecules per protomer: LC-I (primary binding site, center of protein), LC-II (secondary cytoplasmic site at bottom of intracellular vestibule), LC-III (extracellular surface cavity), and LC-IV (entrance of intracellular vestibule). LC-I forms hydrogen bonds with Gly253, Gly254, Gly257, Ser310, Ser313, and Trp316, and cation-pi interactions with Trp316 and Tyr319. LC-II interacts with Tyr327 and Gln330. LC-III interacts with Gly310, Trp316, and Tyr114. LC-IV contacts Glu85 and Arg337.

### Mutagenesis reveals functional binding sites

Mutagenesis of LC-II-interacting residues Y327L and Q330L markedly reduced carnitine uptake, supporting the existence of a cytoplasmic secondary substrate-binding site (Sin1). W316L (Trp316L) reduced transport rate by approximately 70%, while Y114L had minor effect, indicating the importance of aromatic residues at the periplasmic barrier top in transport activity.

### Cytoplasmic gate conformational rearrangement

Structural comparison with [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/) (occluded state) reveals that Tyr327 and Gln330 in CaiT (corresponding to Trp377 and Phe380 in BetP) coordinate with LC-II and deviate to allow inward or outward permeation, suggesting LC-II binding is associated with conformational rearrangements favoring opening of the cytoplasmic gate. Intracellular portions of TM3, TM4, TM8, and TM10 in CaiT deviate by approximately 2 Angstroms from corresponding [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/) portions.

### Homotrimeric architecture with 12 TM helices

CaiT crystallizes as a homotrimer with a threefold axis perpendicular to the membrane plane. Each protomer contains 12 transmembrane helices (TM1-TM12) with both N and C termini exposed to the cytoplasm. The monomer resembles a cylinder with maximum height of 52 Angstroms and maximum diameter of 45 Angstroms. TM3-TM12 form a structural core similar to the Na+-coupled symporter [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/) and cores of unrelated transporters [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/), [V. parahaemolyticus Sodium-Galactose Transporter (vSGLT)](/xray-mp-wiki/proteins/slc-transporters/vsglt/), and [Mhp1 Benzyl-Hydantoin Transporter from Microbacterium liquefaciens](/xray-mp-wiki/proteins/slc-transporters/mhp1/).

### Na+-independent transport mechanism via methionine coordination

The 2.3 A structure of PmCaiT reveals a Na+-independent transport mechanism unique among BCCT family members. In Na+-dependent transporters like [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/) and [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/), a sodium ion (Na1) coordinates the substrate carboxyl group. In CaiT, Met331 in TM8 positions its sulphur atom to coordinate the [Gamma-Butyrobetaine (4-Trimethylaminobutyrate)](/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/) carboxyl group, substituting for the missing Na1 ion. This explains CaiT's ability to function without sodium or proton gradients. A single Met331 to valine mutation reduces Kd by ~4-fold and Vmax by ~10-fold but does not restore Na+-dependence, confirming that a single side-chain substitution is insufficient to recreate a Na+-binding site.

### Fully open inward-facing conformation completes alternating access mechanism

Both CaiT structures (PmCaiT at 2.3 A, EcCaiT at 3.5 A) show the fully open inward-facing conformation, with a cytoplasmic funnel approximately 25 A deep and 15 A wide. Access from the cytoplasm is unhindered by obstructing side chains. Together with the outward-open and occluded states observed in other BCCT and [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/)-fold transporters, these structures complete the set of functional states describing the alternating access mechanism. EcCaiT contains two bound [Gamma-Butyrobetaine (4-Trimethylaminobutyrate)](/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/) molecules - one in the central transport site and one in an extracellular binding pocket.

### Cooperative substrate binding via regulatory extracellular site

Substrate-binding curves for CaiT reconstituted into proteoliposomes are sigmoidal,
indicating positive cooperativity with Hill coefficients of 1.4-1.7. The extracellular
substrate-binding site (the second site observed in EcCaiT, coordinated by Tyr114 and
Trp316 via cation-pi interactions) functions as a regulatory site. When occupied by
substrate, it displaces two water molecules, causing small shifts that propagate via
Glu111 to the central transport site, increasing binding affinity. Trp316Ala mutation
reduces Kd, Km, and Vmax by ~5-, 3.5-, and 2.5-fold respectively, confirming the profound
effect of the regulatory site on transport activity. In PmCaiT, access to this second
site is blocked by a crystal contact, and the regulatory site is empty, explaining why
the central transport site is also empty in that structure.

### Arginine 262 replaces Na2 site sodium in CaiT

In CaiT, the positively charged sidechain of R262 in TM5' occupies the position corresponding to the Na2 site found in Na+-dependent [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/)-type transporters ([LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/), [V. parahaemolyticus Sodium-Galactose Transporter (vSGLT)](/xray-mp-wiki/proteins/slc-transporters/vsglt/), [Mhp1 Benzyl-Hydantoin Transporter from Microbacterium liquefaciens](/xray-mp-wiki/proteins/slc-transporters/mhp1/), BetP). Mutagenesis of R262 to alanine or glutamate renders CaiT Na+-dependent, with transport activity restored 30-40% by a membrane potential in the presence of Na+, indicating substrate/Na+ co-transport (electrogenic). The apparent Km(Na+) was 0.45 mM for R262E and 0.70 mM for R262A. Unlike the protonatable K158 in [ApcT Amino Acid Transporter from Methanocaldococcus jannaschii](/xray-mp-wiki/proteins/slc-transporters/apct/), R262 does not undergo protonation/deprotonation cycles, as CaiT is maximally active at pH 7.

### R262 oscillation mechanism mimics sodium binding/unbinding

Homology modeling of CaiT on [BetP (Na+/Betaine Symporter from Corynebacterium glutamicum)](/xray-mp-wiki/proteins/slc-transporters/betp/) structures in outward-open and closed conformations reveals that R262 occupies different positions in each state, stabilized by distinct hydrogen bond networks. In the inward-open conformation, R262 interacts with T100 (TM1'), S259 (TM5'), and T421 (TM8'). In the modeled closed state, it interacts with S266 (TM5') and T100 (TM1'). In the outward-open conformation, R262 interacts with S101 (TM1') and S266 (TM5'). This oscillatory movement of the R262 sidechain between different hydrogen bond partners mimics Na+ binding and unbinding in Na+-dependent transporters, triggering alternating access conformational changes.

### R262E mutant structure reveals rotated substrate orientation

The crystal structure of PmCaiT R262E at 3.29 A resolution reveals a 90-degree rotation of bound [Gamma-Butyrobetaine (4-Trimethylaminobutyrate)](/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/) compared to the wild-type EcCaiT structure. In this orientation, the carboxyl group forms polar contacts with the unwound part of TM1' (backbone carbonyl of S98, sidechain of S101). The trimethyl ammonium head group fits into the tryptophan box (W323, W324, W147). The W323 sidechain rotates 90 degrees to accommodate this orientation. Substrate binding affinity is reduced ~10-fold in R262 mutants (Kd 38-40 mM vs 3.6 mM wild-type).


## Cross-References

- [Betaine/Choline/Carnitine Transporter (BCCT) Family](/xray-mp-wiki/concepts/transport-mechanisms/bcct-family/) — CaiT belongs to the BCCT family; unique Na+-independent antiport mechanism distinguishes it from other BCCT members
- [BetP Betaine Transporter from Bacillus subtilis](/xray-mp-wiki/proteins/slc-transporters/betp/) — Structural comparison with BetP (occluded state) provides insights into cytoplasmic gate mechanism
- [LeuT Amino Acid Transporter from Aquifex aeolicus](/xray-mp-wiki/proteins/enzymes/leut/) — Core architecture comparison; LC-II reciprocal position of LeuT second binding site; outward-facing conformational state speculation
- [Alternating-Access Mechanism](/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/) — CaiT operates via alternating-access mechanism between inward-facing and outward-facing conformations
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Primary detergent for CaiT solubilization, purification, and cryoprotection
- [n-Octyl-beta-D-glucopyranoside (OG)](/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-glucopyranoside/) — Detergent used in crystallization and cryoprotection
- [HEPES (4-(2-hydroxyethyl)-1-piperazineethanesulfonic acid)](/xray-mp-wiki/reagents/buffers/hepes/) — Buffer used in SEC and crystallization (HEPES-NaOH pH 7.5)
- [TEV Protease (Tobacco Etch Virus Protease)](/xray-mp-wiki/reagents/protein-tags/tevp-protease/) — TEV protease used for cleavage of C-terminal GFP-His10 tag during purification
- [Mercury (HgCl2)](/xray-mp-wiki/reagents/additives/mercury/) — Mercury compound (ethylmercurithiosalicylate) used for SIRAS phasing in crystal structure determination
- [L-Carnitine](/xray-mp-wiki/reagents/ligands/l-carnitine/) — Endogenous substrate and ligand of CaiT; four molecules observed per protomer in crystal structure
- [Gamma-Butyrobetaine](/xray-mp-wiki/reagents/ligands/gamma-butyrobetaine/) — Endogenous substrate of CaiT antiport exchange with L-carnitine
- [Arginine Oscillation Mechanism in LeuT-Type Transporters](/xray-mp-wiki/concepts/transport-mechanisms/arginine-oscillation-mechanism/) — This paper establishes the arginine oscillation model where R262 mimics Na+ binding/unbinding in CaiT
