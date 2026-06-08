---
title: Archaeoglobus fulgidus AglB (AfAglB)
created: 2026-05-29
updated: 2026-05-29
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1021##acs.biochem.6b01089, doi/10.1073##pnas.1314195110]
verified: false
---

# Archaeoglobus fulgidus AglB (AfAglB)

## Overview

Archaeoglobus fulgidus AglB (AfAglB) is the catalytic subunit of the archaeal oligosaccharyltransferase (OST), a single-subunit membrane enzyme that transfers an oligosaccharide chain to Asn residues in the Asn-X-Ser/Thr sequon of substrate proteins. AfAglB comprises 13 transmembrane helices in the N-terminal region and a C-terminal globular domain. Despite low sequence identity (<20%) to eubacterial PglB homologs, AfAglB shares a highly conserved catalytic architecture including the carboxylate dyad (Asp47 and Glu360 with a metal ion) that activates the acceptor Asn side chain for nucleophilic attack on the lipid-linked oligosaccharide donor.

## Structure Determination

| Source | PDB ID | Resolution | Space Group | Construct | Ligand/Co-factor |
|---|---|---|---|---|---|
| doi/10.1021##acs.biochem.6b01089 | 5GMY | 3.5 A | Not specified in paper | AfAglB G617C mutant cross-linked with acceptor peptide Ac-RYNVTAC-NH2 via engineered disulfide bond at position 617 | Acceptor peptide (Ac-RYNVTAC-NH2) containing N-glycosylation sequon Asn-Val-Thr |
| doi/10.1073##pnas.1314195110 | 3WAK | Not specified in paper | Not specified in paper | Apo AfAglB (wild-type, full-length) | None |

## Expression and Purification

- **Expression system**: E. coli C43 (DE3) cells
- **Construct**: AfAglB G617C mutant (cysteine introduced at position 617 for peptide tethering); native AfAglB lacks cysteine residues

### Purification Workflow


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Cell disruption | Sonication of E. coli C43 (DE3) membrane fractions | -- | TS buffer (50 mM Tris-HCl, pH 8.0, 100 mM NaCl) + -- | Cells grown at 310 K in Terrific Broth with 100 mg/L ampicillin; induced with 0.5 mM IPTG at 298 K |
| Membrane isolation | Ultracentrifugation at 100,000 x g for 2 h | -- | TS buffer (50 mM Tris-HCl, pH 8.0, 100 mM NaCl) + -- | Pellets containing membrane fractions collected |
| Solubilization | Detergent solubilization of membrane pellets | -- | TS buffer (50 mM Tris-HCl, pH 8.0, 100 mM NaCl) + 1% (w/v) DDM (n-dodecyl-beta-D-maltopyranoside) | DDM-solubilized protein recovered after ultracentrifugation at 100,000 x g for 1 h |
| Affinity chromatography | Nickel Sepharose High Performance resin | Nickel Sepharose High Performance (GE Healthcare) | TS buffer (50 mM Tris-HCl, pH 8.0, 100 mM NaCl) containing 0.1% (w/v) DDM + 0.1% (w/v) DDM | His-tagged recombinant protein purified by affinity chromatography |


#### Steps

| Step | Method | Resin / Column | Buffer + Detergent | Notes |
|---|---|---|---|---|
| Gel filtration chromatography | Gel filtration in LDAO | Not specified | Not specified in paper + 0.06% (w/v) LDAO | Performed for crystallization; G617C mutant purified by gel filtration |


## Crystallization

### doi/10.1021##acs.biochem.6b01089

| Parameter | Value |
|---|---|
| Method | Hanging drop vapor diffusion |
| Protein sample | AfAglB G617C mutant cross-linked with acceptor peptide Ac-RYNVTAC-NH2, concentrated to 15 mg/ml, dialyzed against 10 mM Tris-HCl, pH 7.5, 0.1 M NaCl, 0.06% (w/v) LDAO |
| Reservoir | 0.01 M MgCl2, 0.1 M Bis-Tris, pH 6.5, 22% (w/v) PEG 550MME, 5% (v/v) Jeffamine M-600, pH 7.0 |
| Temperature | 293 K |
| Growth time | Not specified |
| Cryoprotection | 0.01 M MgCl2, 0.1 M Bis-Tris, pH 6.5, 30% (v/v) PEG 550MME, 0.06% (w/v) LDAO; cryocooled in liquid nitrogen |
| Notes | Initial screening with MemGold I, MemGold II, and MemStart+MemSys Kits (Molecular Dimensions). X-ray data collected at SPring-8 BL44XU to 3.50 A resolution. Solved by molecular replacement using apo AfAglB (3WAK) as search model. R_work/R_free = 20.7%/27.8%. Calculated solvent content 63.2% (Vm = 3.35 A^3/Da). |


## Biological / Functional Insights

### Conserved sequon recognition mechanism between archaeal and eubacterial OSTs

The crystal structure of the cross-linked AfAglB-sequon complex reveals that the N-glycosylation sequon binds in the same manner as in the C. lari PglB-peptide complex. The acceptor peptide adopts an extended conformation with the Asn-Val-Thr sequon positioned at the boundary between the N-terminal transmembrane region and the C-terminal globular domain. Two conserved interactions are observed: (1) the Asn side-chain carboxamide group interacts with Asp47 and Glu360 (carboxylate dyad) and a bound metal ion, and (2) the Thr residue at the +2 position is recognized by the Ser/Thr-binding pocket formed by the W550-W551-D552 motif and K618. This demonstrates evolutionary conservation of sequon recognition between archaeal and eubacterial OSTs despite low sequence identity (<20%).

### Carboxylate dyad catalytic mechanism

The carboxylate dyad consists of Asp47 (in the GND motif of external loop 1) and Glu360 (in the TIAE motif of external loop 5), which together coordinate a divalent metal ion. Their side-chain carboxylate groups contact the carboxamide group of the acceptor Asn side chain, twisting the planar carboxamide geometry to enable nucleophilic attack on the C1 carbon of the lipid-linked oligosaccharide donor. Single alanine mutations (D47A, E360A) retained reduced but significant activity in the cross-linked state, whereas the double mutation (D47A/E360A) completely abolished catalysis. In contrast, without tethering, both single mutants showed complete loss of activity.

### EL5 loop conformational dynamics

The EL5 loop exhibits dynamic behavior upon acceptor peptide binding. In the apo state (3WAK), the EL5 loop is fully ordered and Glu360 is not involved in metal-ion coordination. Upon acceptor peptide binding, the N-terminal half of EL5 (Ser335-Gln350) becomes disordered while the C-terminal half (Pro351-Thr373) remains ordered. This partially ordered state is an intrinsic property observed in both AfAglB and C. lari PglB complexes. The conformational change positions Glu360 to participate in the carboxylate dyad interactions with the acceptor Asn side chain and metal ion.

### Relaxed sequon consensus requirements in cross-linked state

In the cross-linked complex, the stringent N-glycosylation consensus requirements are greatly relaxed: (1) A Gln residue at the Asn position functions as an acceptor (QVT sequon), with MS analysis confirming heptasaccharide attachment, (2) The hydroxy group at the +2 position is not required (NVA sequon accepted, though slower than NVT), (3) Amino acid preferences at the X position disappear except for Pro rejection. This contrasts with free-peptide assays where strong X-position preferences (Glu/Gln favored, Arg/Lys/Trp disfavored) are observed. The cross-linked state mimics co-translational oligosaccharyl transfer coupled with membrane protein permeation.


## Cross-References

- [N-Glycosylation Sequon](/xray-mp-wiki/concepts/n-glycosylation-sequon/) — AfAglB recognizes and catalyzes glycosylation of the Asn-X-Ser/Thr sequon
- [Carboxylate Dyad](/xray-mp-wiki/concepts/carboxylate-dyad/) — Catalytic mechanism of AfAglB involves the Asp47-Glu360 carboxylate dyad
- [n-Dodecyl-beta-D-maltopyranoside (DDM)](/xray-mp-wiki/reagents/detergents/ddm/) — Detergent used for solubilization and purification of AfAglB
- [Lauryldimethylamine N-oxide (LDAO)](/xray-mp-wiki/reagents/detergents/lDAO/) — Detergent used for gel filtration and crystallization of AfAglB
- [Tris (Tris-HCl Buffer)](/xray-mp-wiki/reagents/buffers/tris/) — Buffer used throughout AfAglB expression, purification, and assays
