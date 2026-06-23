---
title: GluA2 AMPA Receptor — Structures with Antagonists, NAMs, and Allosteric Modulators
created: 2026-06-08
updated: 2026-06-16
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aad3873, doi/10.1038##nature08624, doi/10.1111##bph.15254, doi/10.1111##febs.15455, doi/10.1126##science.1256508, doi/10.1126##science.1258409, doi/10.1016##j.cell.2014.07.023]
verified: false
---

# GluA2 AMPA Receptor — Structures with Antagonists, NAMs, and Allosteric Modulators

## Overview

GluA2 (also known as GluR2) is an AMPA-subtype ionotropic glutamate receptor (iGluR) subunit that forms tetrameric cation channels mediating fast excitatory neurotransmission in the central nervous system. The first X-ray crystal structure of a full-length rat GluA2 receptor was determined at 3.6 A resolution in 2009 (Sobolevsky et al., Nature 2009), revealing the Y-shaped tetrameric architecture with amino-terminal domain (ATD), ligand-binding domain (LBD), and transmembrane domain (TMD). AMPA receptors are validated targets for antiepileptic drugs (AEDs). Multiple subsequent crystal structures of the full-length rat GluA2 receptor have been determined in complex with various ligands, revealing distinct inhibition mechanisms. A 4.25 A structure with trans-4-butylcyclohexane carboxylic acid (4-BCCA), a medium-chain fatty acid AED candidate, showed 4-BCCA binding at TMD side portals distinct from the perampanel site (Yelshanskaya et al., 2020, Br J Pharmacol). A 4.65 A structure with the competitive antagonist ZK200775 and the negative allosteric modulator (NAM) GYKI53655 demonstrated that four molecules of each antagonist can bind simultaneously, with the two mechanisms of antagonism operating independently (Krintel et al., 2020, FEBS J). The EM analysis showed that AMPA induces a mix of compact and bulgy conformations regardless of GYKI53655 presence, indicating the NAM primarily affects the TMD gate without altering extracellular domain conformations. A structure of GluA2 bound to the partial agonist (S)-5-nitrowillardine (NOW) at 3.6-4.0 A resolution revealed ~11 degrees of LBD clamshell closure compared to the antagonist-bound state, providing insights into iGluR gating (Yelshanskaya et al., 2014, Science). Multiple X-ray structures of GluA2 in complex with the Conus striatus cone snail toxin con-ikot-ikot, a positive allosteric modulator, and orthosteric agonists at 3.8-4.1 A resolution showed how the toxin restrains the LBD gating ring, transducing agonist-induced clamshell closure into iris-like expansion of the gating ring (Chen et al., 2014, Science).


## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1038##nature08624 | N/A (not deposited) | 3.6 | P1 | GluA2cryst — modified rat GluA2i (flip isoform) with C-terminal deletions, ATD-LBD linker deletions (6 residues), glycosylation knockout mutations (N235E, N385D, N392Q), loop L1 alanine substitutions, R586Q, and C589A | None (apo-like, antagonist-bound) |
| doi/10.1111##bph.15254 | 6XSR | 4.25 | P 21 21 21 | GluA2Del (modified rat GluA2i flip isoform) — 36-residue C-terminal deletion, ATD-LBD linker deletions, N235E/N385D/N392Q (glycosylation knockouts), M1-M2 linker replaced with DTD linker, R586Q, C589A | 4-BCCA (trans-4-butylcyclohexane carboxylic acid) |
| doi/10.1111##febs.15455 | 6RUQ | 4.65 | P 1 21 1 | GluA2cryst (modified rat GluA2 without CTD) — expressed in Sf9 insect cells | ZK200775 (competitive antagonist), GYKI53655 (NAM) |
| doi/10.1126##science.1256508 | N/A (not explicitly deposited) | 3.6-4.0 | N/A | Homotetrameric rat GluA2 (GluA2*) — modified for crystallization | (S)-5-nitrowillardine (NOW, partial agonist) |
| doi/10.1126##science.1258409 | 3KG2 (reference structure) | 3.8-4.1 | N/A | GluA2_cryst1 and GluA2_cryst2 constructs with Lurcher-like mutants (A622T, T625G) | con-ikot-ikot toxin, (R,R)-2b (positive allosteric modulator), kainate or fluorowillardiine (FW) |
| doi/10.1016##j.cell.2014.07.023 | 4U2P | 3.71 | P2(1)2(1)2(1) | 5M (thermostabilized rat GluA2 construct with 5 thermostabilizing mutations) | None (apo resting/closed state) |
| doi/10.1016##j.cell.2014.07.023 | 4U1W | 3.61 | P2(1)2(1)2(1) | 5M construct | Kainate (partial agonist), (R,R)-2b (positive allosteric modulator) |
| doi/10.1016##j.cell.2014.07.023 | 4U1X | 3.82 | P2(1)2(1)2(1) | 10M construct (10 thermostabilizing mutations) | Kainate (partial agonist), (R,R)-2b (positive allosteric modulator) |
| doi/10.1016##j.cell.2014.07.023 | 4U1Y | 4.27 | P2(1)2(1)2(1) | 10Mdel construct (10 thermostabilizing mutations + M1-M2 loop deletion) | Fluorowilliardiine (partial agonist), (R,R)-2b (positive allosteric modulator) |
| doi/10.1016##j.cell.2014.07.023 | 4U2Q | 4.05 | P2(1)2(1)2(1) | 5M construct | Kainate (partial agonist, no modulator) |
| doi/10.1016##j.cell.2014.07.023 | Not deposited | 7.94 | P2(1) | 5M construct | Fluorowilliardiine (partial agonist, desensitizing conditions) |

## Expression and Purification

- **Expression system**: HEK293 GnTI- cells (BacMam system) or Sf9 insect cells (baculovirus)
- **Construct**: Rat GluA2i (flip) with native signal peptide. Variants include GluA2cryst (C-terminal deletions, ATD-LBD linker deletions, glycosylation knockout mutations), GluA2Del (36-residue C-terminal deletion), GluA2_cryst1, and GluA2_cryst2
- **Notes**: Multiple constructs used across studies for crystallization. C-terminal GFP-His tag or C-terminal thrombin cleavage site with eGFP and Strep-tag used for purification.

### Purification Workflow

*Source: doi/10.1111##bph.15254*

- **Expression system**: HEK293 GnTI- cells (BacMam)
- **Expression construct**: Rat GluA2i (flip) with native signal peptide in [Peg](/xray-mp-wiki/reagents/additives/peg/) BacMam vector. C-terminal thrombin cleavage site, eGFP, Strep-tag. Deletions: 36 residues from C-terminus, 6 residues from ATD-LBD linker. Mutations: N235E, N385D, N392Q, R586Q, C589A.
- **Tag info**: C-terminal eGFP-Strep-tag, thrombin removable

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and expression | BacMam P2 virus transduction of HEK293 GnTI- cells | — | DMEM culture medium | Cells harvested 60-96 h after virus addition |
| Cell lysis | Sonication | — | 150 mM NaCl, 20 mM [[Tris](/xray-mp-wiki/reagents/buffers/tris/) Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 0.8 uM aprotinin, 2 ug/mL leupeptin, 2 uM pepstatin A, 1 mM PMSF | 18 x 15 s at power level 7. Homogenate clarified at 8000 rpm for 15 min. Crude membranes collected by ultracentrifugation at 40000 rpm for 1 h (Ti45 rotor) |
| Solubilization | Detergent solubilization | — | 150 mM NaCl, 20 mM [[Tris](/xray-mp-wiki/reagents/buffers/tris/) Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0 + 20 mM C12M (n-dodecyl-beta-D-maltopyranoside, [DDM](/xray-mp-wiki/reagents/detergents/ddm/)) at 0.25 g/g membranes | Solubilization for 2 h at 4 C. Insoluble material removed by ultracentrifugation at 40000 rpm for 40 min (Ti45 rotor) |
| Affinity purification | Strep-Tactin resin batch binding | Strep-Tactin | 150 mM NaCl, 20 mM [[Tris](/xray-mp-wiki/reagents/buffers/tris/) Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 1 mM C12M | 0.5-1.0 mL resin per L culture. Binding for 3-18 h. Elution with 2.5 mM [Desthiobiotin](/xray-mp-wiki/reagents/ligands/desthiobiotin/) |
| Deglycosylation and tag removal | [Endoh](/xray-mp-wiki/reagents/additives/endoh/) + thrombin digestion | — | 150 mM NaCl, 20 mM [[Tris](/xray-mp-wiki/reagents/buffers/tris/) Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 1 mM C12M | [Endoh](/xray-mp-wiki/reagents/additives/endoh/) at 1:1 mass ratio for 24 h at 4 C, then thrombin at 1:200 mass ratio for 1 h at 22 C |
| Size exclusion chromatography | SEC - Superose 6 column | — | 150 mM NaCl, 20 mM [[Tris](/xray-mp-wiki/reagents/buffers/tris/) Hcl](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 1 mM n-undecyl-beta-D-thiomaltopyranoside (C11Thio), 0.01 mg/mL POPC:POPE:POPG (3:1:1) | Pooled peak fractions concentrated to ~2 mg/mL for crystallization |

### Purification Workflow

*Source: doi/10.1111##febs.15455*

- **Expression system**: Sf9 insect cells (baculovirus) and HEK293F mammalian cells (BacMam)
- **Expression construct**: GluA2cryst construct with C-terminal GFP-His tag
- **Tag info**: C-terminal GFP-His tag, thrombin removable

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and expression (Sf9) | Baculovirus expression in Sf9 insect cells | — |  | Baculovirus particles generated using standard methods |
| Cell culture and expression (HEK293F) | BacMam transduction of HEK293F cells | — | FreeStyle 293 expression medium, 8% CO2, 37 C, 150 RPM | 20 mL BacMam virus for 200 mL HEK293F at 1x10^6 cells/mL. 5 mM sodium butyrate added 6-24 h post-transduction, temperature lowered to 30 C. Cells harvested after 72 h |
| Cell lysis and membrane preparation | Sonication and ultracentrifugation | — | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 1 mM [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/), cOmplete Protease Inhibitor | Cells resuspended and sonicated. Lysate spun at 41000 RPM (70Ti rotor) for 20 min |
| Solubilization | [DDM](/xray-mp-wiki/reagents/detergents/ddm/) solubilization | — | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, cOmplete Protease Inhibitor + 20 mg/mL [DDM](/xray-mp-wiki/reagents/detergents/ddm/) (n-dodecyl-beta-D-maltopyranoside) Sol-Grade (Anatrace) | Pellet resuspended using dounce homogenizer. Solubilized membranes spun at 41000 RPM (70Ti rotor) |
| Affinity purification and tag removal | [Talon](/xray-mp-wiki/reagents/additives/talon/) Metal Affinity + thrombin digest | [Talon](/xray-mp-wiki/reagents/additives/talon/) Superflow Metal Affinity Resin | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, DDM | Eluted with 250 mM [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/). Overnight digestion with thrombin to remove GFP-His tag |
| Size exclusion chromatography | SEC - Superose 6 10/300 GL | — | 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.5 mg/mL DDM Anagrade, low alpha isomer (Anatrace) | Tag-free GluA2cryst purified. Pooled peak fractions used for EM and crystallization |

### Purification Workflow

*Source: doi/10.1126##science.1258409*

- **Expression system**: HEK293 GnTI- cells (BacMam)
- **Expression construct**: Rat GluA2_cryst1 and GluA2_cryst2 constructs, with A622T and T625G Lurcher-like mutants
- **Tag info**: C-terminal GFP-His tag

#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell culture and expression | BacMam transduction of HEK293 GnTI- cells | — |  | Similar expression protocol to other GluA2 constructs |
| Purification | Affinity chromatography and SEC | Similar to GluA2_cryst1 protocols | [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, NaCl + [DDM](/xray-mp-wiki/reagents/detergents/ddm/) | Detailed purification similar to GluA2_cryst1 construct. Protein concentrated for crystallization with toxin and ligands |


## Crystallization

### doi/10.1111##bph.15254

| Parameter | Value |
|---|---|
| Method | Vapor diffusion, hanging drop |
| Protein sample | GluA2Del at ~2 mg/mL with 2 mM 4-BCCA |
| Reservoir | Condition 1: 8-11% [Peg](/xray-mp-wiki/reagents/additives/peg/) 8000, 0.2 M magnesium [Acetate](/xray-mp-wiki/reagents/buffers/acetate/), 0.1 M sodium [Cacodylate](/xray-mp-wiki/reagents/cacodylate/) pH 6.3-6.7; Condition 2: 11-14% PEG 6000, 0.1 M ammonium phosphate, 0.1 M TRIS pH 7.9-8.0 |
| Mixing ratio | 2:1 (protein:reservoir) |
| Temperature | 4 |
| Growth time | 5-7 days (crystals appeared), 30-60 days (max size ~100x100x300 um) |
| Cryoprotection | Serial [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) to 20% (v/v) |
| Notes | Protein subjected to ultracentrifugation at 40000 rpm for 40 min at 4 C prior to crystallization |

### doi/10.1111##febs.15455

| Parameter | Value |
|---|---|
| Method | Microbatch under oil |
| Protein sample | GluA2cryst at 2 mg/mL in 20 mM [Tris](/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 150 mM NaCl, 0.5 mg/mL DDM with 0.67 mM GYKI53655 and 0.31 mM ZK200775 |
| Reservoir | 0.1 M [MES](/xray-mp-wiki/reagents/buffers/mes/) pH 6.0, 12% [Peg](/xray-mp-wiki/reagents/additives/peg/) 20000 |
| Temperature | 279 |
| Growth time | Appeared within 24 h, grew for 3-4 days before flash-cooling |
| Cryoprotection | Flash-cooled in liquid nitrogen |
| Notes | Data collected at ESRF ID29 using helical scan. Processed with XIA2/MOSFLM. Resolution cut at 4.65 A |

### doi/10.1126##science.1256508

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | GluA2* with (S)-5-nitrowillardine (NOW) |
| Temperature | 4 |
| Notes | Crystals grown from GluA2* in complex with partial agonist (S)-5-nitrowillardine. Comparison with GluA2_ZK (ZK 200775-bound) closed-state structure |

### doi/10.1126##science.1258409

| Parameter | Value |
|---|---|
| Method | Vapor diffusion |
| Protein sample | GluA2_cryst1 or GluA2_cryst2 with con-ikot-ikot toxin, (R,R)-2b, and kainate or fluorowillardiine |
| Temperature | 4 |
| Cryoprotection | Flash-cooled in liquid nitrogen |
| Notes | Multiple structures determined at 3.8-4.1 A resolution. Modulator (R,R)-2b included to improve diffraction quality. Complexes with KA or FW as partial agonists. Lurcher-like mutants A622T and T625G used to favor open state. Structures represent toxin-bound preopen states |


## Biological / Functional Insights

### First full-length iGluR structure reveals Y-shaped tetrameric architecture

The 3.6 A crystal structure of the full-length rat GluA2cryst receptor (Sobolevsky et al., 2009) was the first X-ray structure of any intact ionotropic glutamate receptor. It revealed a Y-shaped tetramer composed of three distinct layers: the amino-terminal domain (ATD), the ligand-binding domain (LBD), and the transmembrane domain (TMD). The ATD and LBD form dimer-of-dimers assemblies with 2-fold symmetry, while the TMD adopts a 4-fold symmetric ion channel pore. The ATD dimers are arranged in a swapped configuration, with two pairs of ATD-LBD subunit arrangements (A/C and B/D) that are structurally distinct.

### Agonist-bound GluA2 structure reveals LBD clamshell closure in intact receptor

The structure of GluA2 in complex with partial agonist (S)-5-nitrowillardine (NOW) (Yelshanskaya et al., 2014, Science) provides structural evidence of clamshell motion in the context of an intact, multidomain iGluR. The LBD clamshells are ~11 degrees more closed in the NOW-bound state compared to the ZK 200775 antagonist-bound state. This conformational change is smaller than in agonist-bound structures of isolated LBDs (up to ~14 degrees). The tension from altered LBD dimer conformation pulls ATD dimers down, tilting them ~1.2 degrees, and pulls the ion channel up, making the structure ~2 A shorter. The interface between the two LBD dimers becomes tighter and covers a surface area three times larger than in the antagonist-bound state.

### Agonist-induced LBD dimer interface tightening and gating

Disulfide cross-linking experiments with GluA2-I664C demonstrated that agonist-induced tightening of the LBD dimer-dimer interface occurs during gating. In nonreducing conditions, recovery from desensitization was incomplete, consistent with agonist-induced interface tightening. Cross-linking at the D1-D1 interface (P494C, S497C) promoted channel opening, while cross-linking at D2 lobes produced negative effects on iGluR activation. These findings support two possible gating models where LBDs are highly mobile and agonist binding causes clamshell closure.

### Cone snail toxin stabilizes LBD gating ring in expanded conformation

The con-ikot-ikot toxin from Conus striatus acts like a straightjacket on the LBD gating ring (Chen et al., 2014, Science). The toxin spans the tetrameric LBD gating ring, participating in extensive interactions with all four subunits, simultaneously fortifying intradimer interfaces and spanning the interdimer cleft. The electrostatic surface of the toxin shows extensive negative patches complementary to positively charged residues on the receptor surface. Toxin binding requires agonist-induced clamshell closure, as it binds to both D1 and D2 lobes of LBD A/C pair subunits.

### Iris-like expansion of the LBD gating ring

The toxin complex structures reveal that the LBD gating ring adopts an expanded conformation. The interaxis angle between LBD dimers is smaller in the toxin complex than in the antagonist-bound ZK structure. The S640 C-alpha marker atoms show an 8.4 A increase in separation between D2 lobes upon transition from the ZK antagonist state to the FW agonist-bound structure. The toxin stabilizes the D1-D1 interface in a nondesensitized conformation with S741 C-alpha distances of 19.3-19.7 A. The expansion is asymmetric, with the A/C pair showing 3.4 A additional separation and the B/D pair showing 12.4 A separation, consistent with symmetry nonequivalence.

### I633 coupling mechanism in M3-LBD linkers

The I633 residue from the B/D subunits couples agonist binding to ion channel gating. In non-M3-mutant structures, I633 from B/D subunits adopts an uncoupled conformation pulled out of the hydrophobic D2 pocket. In Lurcher-like mutant structures (A622T, T625G), I633 from B/D subunits binds within a hydrophobic pocket formed by V732, I504, L639, and I645 on the D2 lobe, adopting a coupled conformation. The I633A and I633E mutants show severely diminished currents, confirming I633's essential role. The coupling is asymmetric, with B/D subunits showing larger conformational changes than A/C subunits.

### 4-BCCA binds at TMD side portals distinct from known modulators

4-BCCA binds at the lateral portals formed by transmembrane segments M1-M4 at the intersubunit interfaces. These sites are distinct from the perampanel binding site (extracellular collar) and polyamine/ion channel blocker sites. The binding pocket is formed by mostly hydrophobic residues from M1 (L521, W526, I529), M2 (F584, M585), and M3 (T609, I612, I613, Y616, T617) of one subunit and M3 (F607, L610, I611, S614) of the neighboring subunit.

### Simultaneous binding of competitive antagonist and NAM

The X-ray structure of GluA2cryst with ZK200775 (competitive antagonist) and GYKI53655 (NAM) at 4.65 A demonstrates that four molecules of each antagonist can bind simultaneously without mutual interference. ZK200775 occupies all four LBD binding sites with the same domain-opening as in the ZK200775-only structure (3KG2). GYKI53655 occupies all four NAM pockets near the TMD-LBD linker. The two binding events are structurally independent.

### Full-length GluA2 structures in apo resting, pre-open, and desensitized states

Dürr et al. (2014, Cell) determined X-ray crystal structures of the intact homotetrameric GluA2 AMPA receptor in three functionally distinct states: (1) an apo resting/closed state (PDB 4U2P, 3.71 A), (2) agonist-bound pre-open/activated states stabilized by the positive allosteric modulator (R,R)-2b in complex with partial agonists kainate (KA) or fluorowilliardiine (FW) (PDBs 4U1W, 4U1X, 4U1Y, 3.6-4.3 A), and (3) an FW-bound desensitized state (~8 A, solved by molecular replacement with cryo-EM validation). These structures, combined with DEER spectroscopy and cryo-EM, provide a near-comprehensive view of AMPA receptor gating transitions. The structures revealed that the LBD layer undergoes large conformational rearrangements, with the LBD gating ring expanding upon activation and contracting upon desensitization.

### LBD gating ring expansion upon activation

Comparison of the apo and pre-open structures (KA+(R,R)-2b and FW+(R,R)-2b) reveals that agonist binding modulates the conformation of the LBD layer. The D2-D2 separation increases by 6-7 A in both diagonal pairs (AC and BD), reflecting an enhanced mechanical pulling force exerted by bound partial agonists. The angle between LBD dimer local 2-fold axes (roll angle) increases from 34.6 degrees in apo to 52.2-55.6 degrees in modulator-bound states. Despite these movements, the ion channel pore remains closed, suggesting these represent a pre-open state. DEER spectroscopy confirmed the D2-D2 distance increases. The (R,R)-2b modulator binds at the D1-D1 interface, stabilizing it in a nondesensitized conformation.

### Large conformational rearrangements upon desensitization

The low-resolution (8 A) X-ray structure of GluA2 in complex with FW alone (desensitizing conditions) reveals dramatic conformational changes. One ATD dimer (AB) is tilted downward by ~89 degrees, approaching the side of the other ATD dimer (CD). The D1-D1 interfaces are disrupted in both LBD dimers. In the AD pair, the LBD monomers become more separated than in the S729C disulfide-trapped structure, with the LBD of chain D rotated outward by ~105 degrees. Cryo-EM studies confirm the conformational heterogeneity of the desensitized state, with particles showing a range of compact and bulgy conformations compared to the more uniform Y-shaped pre-open state. This domain-swapped architecture explains why disruption of the LBD dimer interface destabilizes the Y-shaped resting state.


## Cross-References

- [Non-competitive Inhibition](/xray-mp-wiki/concepts/enzyme-mechanisms/non-competitive-inhibition/) — 4-BCCA and GYKI53655 are non-competitive inhibitors of AMPA receptors binding at distinct TMD sites from the orthosteric glutamate site
- [C-type Inactivation](/xray-mp-wiki/concepts/structural-mechanisms/c-type-inactivation/) — AMPA receptor gating and desensitization involve TMD conformational changes modulated by antagonist and NAM binding
- [Peg](/xray-mp-wiki/reagents/additives/peg/) — Referenced in glua2-ampa-receptor text
- [Tris](/xray-mp-wiki/reagents/buffers/tris/) — Referenced in glua2-ampa-receptor text
- [DDM](/xray-mp-wiki/reagents/detergents/ddm/) — Referenced in glua2-ampa-receptor text
- [Desthiobiotin](/xray-mp-wiki/reagents/ligands/desthiobiotin/) — Referenced in glua2-ampa-receptor text
- [Endoh](/xray-mp-wiki/reagents/additives/endoh/) — Referenced in glua2-ampa-receptor text
- [Pmsf](/xray-mp-wiki/reagents/additives/pmsf/) — Referenced in glua2-ampa-receptor text
- [Talon](/xray-mp-wiki/reagents/additives/talon/) — Referenced in glua2-ampa-receptor text
- [Imidazole](/xray-mp-wiki/reagents/additives/imidazole/) — Referenced in glua2-ampa-receptor text
