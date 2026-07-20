---
title: "POPE (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine)"
created: 2026-06-11
updated: 2026-06-16
type: reagent
category: reagents
layout: default
tags: [lipid, subdirectory-lipids]
sources: [doi/10.1016##j.jmb.2019.12.025, doi/10.1016##j.str.2019.04.007, doi/10.1016##j.bbamem.2021.183825]
verified: regex
---

# POPE (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine)

## Overview

POPE (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine) is a zwitterionic phospholipid commonly used in membrane protein structural studies. It is the predominant lipid species in the inner membrane of E. coli and is widely used as a model bilayer for molecular dynamics simulations of membrane proteins. In AcrB studies, POPE was used in MD simulations to model the native membrane environment and investigate competitive binding between POPE acyl chains and carboxylated drugs at the TM1/TM2 groove. In MsbA studies, POPE was used in ATPase activity measurements and MD simulations to study lipid A transport.


## Properties

- **Molecular weight**: 718.0
- **Class**: Phosphatidylethanolamine (zwitterionic phospholipid)

## Use in Membrane Protein Work

### Model membrane for MD simulations of AcrB

POPE bilayers were used for microsecond-long MD simulations of wild-type, I27A, and V340A AcrB variants to study drug binding at the TM1/TM2 groove. POPE molecules at the groove formed H-bonds and salt bridges with residues N298, K334, and H338, competing with carboxylated drug substrates.


### Model membrane for MD simulations of MsbA

POPE bilayers were used in 200 ns MD simulations of MsbA to study lipid A dissociation from the periplasmic surface binding site. Strong electrostatic interactions between lipid A and POPE head groups were observed.


## Examples from This Wiki

| Protein | Concentration | Context | Result |
|---|---|---|---|
| [AcrB Multidrug Efflux Transporter](/xray-mp-wiki/proteins/abc-transporters/acrb/) |  | POPE bilayer MD simulations of wild-type and variant AcrB to study TM1/TM2 groove drug binding |  |
| [MsbA Lipid A Flippase](/xray-mp-wiki/proteins/abc-transporters/msba/) |  | POPE bilayer MD simulations of MsbA-lipid A interactions and ATPase activity measurements |  |

## Advantages and Disadvantages

No advantages/disadvantages recorded.

## Comparison with Related Reagents

No comparison data available.

## Cross-References

- [AcrB Multidrug Efflux Transporter](/xray-mp-wiki/proteins/abc-transporters/acrb/) — POPE bilayer used in MD simulations of AcrB to study TM1/TM2 groove drug binding
- [MsbA Lipid A Flippase](/xray-mp-wiki/proteins/abc-transporters/msba/) — POPE used in MsbA ATPase assays and MD simulations of lipid A transport
