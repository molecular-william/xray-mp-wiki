---


title: Solubilization
created: 2026-04-27
updated: 2026-04-27
type: method
tags: [solubilization-detergent, membrane-protein, sample-preparation]
sources: [doi/10.1016##j.jmb.2009.08.029, doi/10.1016##j.cell.2017.01.042, doi/10.1016##j.cell.2017.03.010, doi/10.1016##j.bbrc.2019.12.091, doi/10.1016##j.str.2018.10.027, doi/10.1016##j.jmb.2018.02.026, doi/10.1073##PNAS.1105687108, doi/10.1016##j.cell.2018.11.025, doi/10.1016##j.str.2020.11.014, doi/10.1038##s41586-018-0039-9, doi/10.7554##eLife.84006, doi/10.1074##jbc.RA120.014118]


category: methods
---
layout: default



# Solubilization

## Overview

Solubilization is the first critical step in membrane protein purification workflows. It involves extracting membrane proteins from their native lipid bilayer environment into an aqueous-compatible form using detergents or other amphipathic molecules. Successful solubilization must preserve protein structure, function, and oligomeric state while removing the bulk of membrane lipids and insoluble cellular debris.

The solubilization process consists of three main stages: (1) cell lysis and membrane preparation, (2) detergent-mediated extraction, and (3) clarification of the solubilized material.

## Cell Lysis Methods

Multiple lysis methods are used depending on the expression system and protein type:

- **French pressure cell / high-pressure homogenizer**: Used for bacterial membranes (e.g., *E. coli*). Cells are forced through a narrow orifice at high pressure (e.g., 20,000 psi). Example: CusA from *E. coli* membranes were disrupted with a French pressure cell, yielding membranes washed with 2 M KCl to remove periplasmic contaminants [10.1016##j.jmb.2009.08.029].
- **Sonication**: Cell suspensions are subjected to ultrasonic waves to disrupt membranes. Used for bacterial and some eukaryotic systems. Example: LbSemiSWEET membranes were lysed by sonication before DDM solubilization [10.1016##j.cell.2017.03.010].
- **Dounce / Potter-Elvehjem homogenizer**: Used for mammalian cell membranes and tissue homogenates. Example: Ton complex from rat brain was homogenized with a Dounce homogenizer [10.1038##nature19757].
- **Freeze-thaw cycles**: Repeated freezing in liquid nitrogen and thawing at room temperature, often used in combination with other methods.
- **Lytic enzymes**: Lysozyme treatment for bacterial cell walls, often followed by mechanical disruption.

## Membrane Isolation

After lysis, membranes are separated from cytosolic content by centrifugation:

- **Low-speed spin**: 10,000-25,000 g for 15-30 min at 4°C to remove unbroken cells and large debris
- **Ultracentrifugation**: 100,000-370,000 g for 30-120 min at 4°C to pellet membranes
- **Washing**: Membrane pellets are often resuspended and washed 1-3 times with buffer (sometimes containing high salt, e.g., 0.5-2 M NaCl or 2 M KCl, to remove peripheral membrane proteins and contaminants)
- **Storage**: Pelleted membranes are typically snap-frozen in liquid nitrogen and stored at -80°C

Example protocols:
- *E. coli* membranes: 300,000 g for 90 min [10.1016##j.jmb.2009.08.029]
- Sf9 insect cell membranes: 180,000 g for 1 h [10.1016##j.bbrc.2019.12.091]
- Mammalian tissue: 25,000 g for 30 min at 4°C, then ultracentrifugation [10.1038##s41594-018-0067-z]

## Detergent Selection

The choice of detergent is the most critical parameter in solubilization. Key considerations include detergent mildness, CMC, and compatibility with downstream steps.

### Default: DDM (n-Dodecyl-β-D-Maltopyranoside)

DDM is the universal first-choice detergent for solubilization across all membrane protein classes:

| Protein class | Typical DDM concentration | Notes |
|---|---|---|
| Bacterial transporters | 1-2% (w/v) | Standard for *E. coli* membranes |
| GPCRs (bacterial/insect) | 1% (w/v) | Often combined with CHS |
| GPCRs (mammalian) | 1-1.5% (w/v) | May require CHS stabilization |
| Photosynthetic complexes | 1-2% (β-DDM) | Thylakoid membrane solubilization |
| Mitochondrial proteins | 1-2% (w/v) | Often with CHS |

Examples from the wiki:
- [nTMATE2-transporter](/proteins/nTMATE2-transporter/) — 2% DDM from *Pichia pastoris* membranes
- [acrB](/proteins/acrB/) — 2% DDM from *E. coli* membranes
- [etb-receptor](/proteins/etb-receptor/) — 1% DDM from Sf9 insect cell membranes (4°C, 1 hr)
- [angiotensin-ii-type-1-receptor](/proteins/angiotensin-ii-type-1-receptor/) — 1% DDM + 0.2% CHS from Sf9 membranes
- [psi-lhci-supercomplex](/proteins/psi-lhci-supercomplex/) — β-DDM for thylakoid membrane solubilization

### GPCR-specific: DDM + CHS

For GPCR solubilization, DDM is almost always combined with cholesterol hydrogen succinate (CHS):

- **Typical ratio**: 1% DDM + 0.1-0.2% CHS (w/v each)
- **Purpose**: CHS stabilizes GPCR tertiary structure during extraction, compensating for loss of native cholesterol
- **Examples**:
  - [etb-receptor](/proteins/etb-receptor/) — 1% DDM + 0.2% CHS for solubilization; 0.01% LMNG + 0.01% CHS in purification
  - [angiotensin-ii-type-1-receptor](/proteins/angiotensin-ii-type-1-receptor/) — 1% DDM + 0.2% CHS for solubilization
  - CCR2A — 1.0% DDM + 0.1% CHS for 2 hours at 4°C [10.1016##j.str.2018.10.027]

### Detergent Exchange for Downstream Steps

After initial solubilization with DDM, a detergent exchange is often performed for specific downstream applications:

| From | To | Purpose |
|---|---|---|
| DDM | LMNG/MNG | GPCR purification — milder, better stability |
| DDM | GDN | Cryo-EM sample preparation — extremely mild |
| DDM | OG | Crystallization — shorter chain, easier removal |
| DDM | DM | Moderate exchange for specific proteins |
| DDM | 10-MNG | Mitochondrial protein purification |

Example: KirBac membranes were solubilized in 1% DDM, then detergent was exchanged to 0.05% LMNG for purification [10.1016##j.cell.2010.05.003].

## Solubilization Protocol

### Standard Conditions

The most common solubilization conditions across the literature:

- **Temperature**: 4°C (almost universally)
- **Duration**: 1-2 hours with gentle rotation, or overnight for difficult proteins
- **Detergent concentration**: 10-50× CMC (typically 0.1-2% w/v depending on detergent)
- **Buffer**: 20-50 mM Tris-HCl or HEPES-NaOH, pH 7.0-8.0
- **Salt**: 150-500 mM NaCl
- **Additives**: 5-10% [glycerol](/reagents/additives/glycerol/), protease inhibitor tablets, DNase I for viscous lysates

### Typical Workflow

1. **Resuspend** membrane pellet in solubilization buffer (e.g., 20 mM Tris-HCl pH 7.5, 200-300 mM NaCl, 5-10% glycerol)
2. **Add detergent** to final concentration (e.g., 1% DDM, or 1% DDM + 0.2% CHS for GPCRs)
3. **Incubate** at 4°C with gentle rotation for 1-2 hours (or overnight)
4. **Clarify** by ultracentrifugation (100,000-370,000 g for 30-60 min at 4°C)
5. **Collect supernatant** containing solubilized membrane protein
6. **Proceed** to affinity chromatography or detergent exchange

### Concentration Guidelines by Detergent

| Detergent | Solubilization concentration | CMC (mM) | Notes |
|---|---|---|---|
| DDM | 1-2% | ~0.17 | Standard for all classes |
| LMNG | 0.1-0.5% | ~0.013 | Milder than DDM |
| OG | 1-2% | ~25 | Short-chain, mild, short-term |
| Digitonin | 1-3% | Variable | Steroidal, preserves complexes |
| GDN | 0.01-0.05% | Very low | Extremely mild, cryo-EM |
| DM | 0.5-1% | ~0.17 | Moderate strength |
| LDAO | 0.5-1% | ~0.5 | Zwitterionic, stronger |

## Stabilizer Addition

Several additives are commonly included in solubilization buffers to enhance protein stability:

- **Cholesterol hydrogen succinate (CHS)**: 0.1-0.2% for GPCRs; stabilizes tertiary structure
- **Glycerol**: 5-10% (v/v) as a general stabilizer
- **Structural phospholipids**: 0.1-0.5% for some transporters
- **Protease inhibitor cocktails**: Essential for all solubilization steps
- **DNase I**: 5 units/mL to reduce viscosity of bacterial lysates
- **Iodoacetamide**: 1-2 mg/mL to alkylate free cysteines and prevent aggregation
- **Benzamidine**: 100-200 μg/mL as a serine protease inhibitor
- **Leupeptin**: 0.2 μg/mL as a protease inhibitor

## Clarification

After solubilization, the mixture must be clarified to remove:
- Insoluble membrane debris
- Unsolubilized protein aggregates
- Nucleic acids (if not treated with DNase)

Standard clarification:
- **Centrifugation**: 100,000-370,000 g for 30-60 min at 4°C
- **Collection**: Supernatant contains solubilized membrane protein
- **Yield check**: Measure protein concentration of supernatant vs. total (before centrifugation) to assess solubilization efficiency

## Detergent Exchange

When the initial solubilization detergent is not optimal for downstream steps, detergent exchange is performed:

- **Affinity column exchange**: Load in high-detergent buffer, wash in lower detergent, elute
- **Dialysis**: Slow exchange over 12-24 hours
- **SEC-based exchange**: Load concentrated sample onto SEC column equilibrated in new detergent
- **Detergent-coated beads**: Use detergent-conjugated resins for exchange

Example: [nTMATE2-transporter](/proteins/nTMATE2-transporter/) was solubilized in 2% DDM, then exchanged to 0.03% LMNG for SEC purification [10.1002##1873-3468.14136].

## Proteins Using Solubilization (from this wiki)

| Protein | Solubilization Detergent | Stabilizers | Notes |
|---|---|---|---|
| [nTMATE2-transporter](/proteins/nTMATE2-transporter/) | 2% DDM | 10% glycerol | From *Pichia pastoris*; exchanged to 0.03% LMNG |
| [acrB](/proteins/acrB/) | 2% DDM | 10% glycerol | From *E. coli*; maintained at 0.2% throughout |
| [etb-receptor](/proteins/etb-receptor/) | 1% DDM + 0.2% CHS | — | From Sf9; exchanged to 0.1% LMNG + 0.01% CHS |
| [angiotensin-ii-type-1-receptor](/proteins/angiotensin-ii-type-1-receptor/) | 1% DDM + 0.2% CHS | — | From Sf9; exchanged to 0.01% MNG + 0.001% CHS |
| [psi-lhci-supercomplex](/proteins/psi-lhci-supercomplex/) | β-DDM (2%) | — | Thylakoid membranes; exchanged to GDN for cryo-EM |
| [kirbac](/proteins/kirbac/) | 1% DDM | Structural phospholipids | Bacterial potassium channel |
| [opsin-gpcr](/proteins/opsin-gpcr/) | OG | — | Primary solubilization detergent |
| [5ht2b-receptor](/proteins/5ht2b-receptor/) | 1% DDM + 0.1% CHS | 0.01% CHS in purification | From HEK293F cells |
| [kappa-opioid-receptor](/proteins/kappa-opioid-receptor/) | 1% DDM + 0.1% CHS | — | From HEK293F cells |
| [adenine-nucleotide-transporter](/proteins/adenine-nucleotide-transporter/) | 2% DM | — | Mitochondrial AAC |
| [sotb](/proteins/sotb/) | 2% DDM | 10% glycerol | From *E. coli* |
| [mmpL3](/proteins/mmpL3/) | 1% DDM | 0.1% CHS | From *M. smegmatis* |

## Related Methods

- [affinity-chromatography](/methods/purification/affinity-chromatography.html) — typically the next step after solubilization
- [size-exclusion-chromatography](/methods/purification/size-exclusion-chromatography.html) — used after detergent exchange
- [centrifugation](/methods/purification/centrifugation.html) — membrane isolation and clarification
- DDM, LMNG, OG, GDN, DM, [digitonin](/reagents/detergents/digitonin/) — various non-ionic detergents used for solubilization
- [cholesterol-hydrogen-succinate](/reagents/lipids/cholesterol-hydrogen-succinate/) — essential stabilizer for GPCR solubilization

## Key Principles

1. **DDM is the default**: Almost all membrane protein solubilizations start with DDM at 1-2% (w/v)
2. **GPCRs need CHS**: For GPCRs, 1% DDM + 0.1-0.2% CHS is the standard starting point
3. **4°C is universal**: All solubilization steps are performed at 4°C to minimize degradation
4. **Exchange is common**: DDM is often replaced by milder detergents (LMNG, MNG, GDN) for downstream steps
5. **Clarification is essential**: Ultracentrifugation removes insoluble debris and determines solubilization efficiency
6. **Buffer composition matters**: Tris/HEPES, 150-500 mM NaCl, 5-10% glycerol are standard components