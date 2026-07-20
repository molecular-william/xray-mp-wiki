---
title: "Digitoxin"
created: 2026-06-16
updated: 2026-06-16
type: reagent
category: reagents
layout: default
tags: [ligand, subdirectory-ligands]
sources: [doi/10.1073##pnas.2020438118]
verified: agent
---

# Digitoxin

## Overview

Digitoxin (DTX) is a cardiotonic steroid (cardiac glycoside) of the cardenolide class, characterized by a five-membered unsaturated lactone ring at C17 and a trisaccharide moiety (tridigitoxose) attached at C3 of the steroid core. Like digoxin, digitoxin has been prescribed for patients with heart failure. The difference between digitoxin and digoxin is the absence of a hydroxyl group at C12 in digitoxin. Crystal structures of the Na+,K+-ATPase E2P state with bound digitoxin at ~3.5 A resolution reveal that the tridigitoxose orientation differs slightly from digoxin due to the lack of the C12 hydroxyl, altering the path of the triose.

## Properties


## Use in Membrane Protein Work

### Na+,K+-ATPase inhibition

Digitoxin inhibits Na+,K+-ATPase by binding to the E2P phosphoenzyme state. The apparent affinities in E2P^Pi·Mg2+ for digitoxin and its aglycone digitoxigenin are similar, indicating that the tridigitoxose sugar moiety does not form strong hydrogen bonds with the protein. Unlike digoxin, digitoxin shows slightly higher K+ antagonism (4x vs 10x for digoxin at 100 mM K+). The lack of the C12 hydroxyl means digitoxin cannot hydrogen bond with the protein at that position, but also avoids the subtle push on Gly319 that slightly changes M4E inclination in digoxin.


### Clinical use in heart failure

Digitoxin has been used clinically for the treatment of heart failure for centuries, similar to digoxin. It has a longer half-life than digoxin and is eliminated primarily by hepatic metabolism rather than renal excretion.


## Examples from This Wiki

| Protein | Concentration | Context | Result |
|---|---|---|---|
| [Na+,K+-ATPase (Pig Kidney)](/xray-mp-wiki/proteins/pumps-atpases/na-k-atpase-pig-kidney/) | Crystallization conditions | Co-crystallized with pig kidney Na+,K+-ATPase in the E2P^Pi·Mg2+ state at ~3.5 A resolution | DTX binds in the same cavity as ouabain; tridigitoxose sugar moiety extends into extracellular vestibule |

## Binding Mode

### Binding to Na+,K+-ATPase alpha subunit (E2P state)

Digitoxin binds in the preformed extracellular cavity of the E2P state of Na+,K+-ATPase. The cis-trans-cis steroid core occupies the same binding pocket as ouabain, formed by alphaM1-M6. The OH14beta group hydrogen bonds with Thr797 (alphaM6). The tridigitoxose sugar moiety extends into the extracellular vestibule. Unlike ouabain's rhamnose, the first digitoxose sugar does not form hydrogen bonds with NKA due to steric hindrance within the sugar moiety. The third digitoxose residue comes closer to the beta-subunit than in digoxin, but the hydroxyl groups on the third sugar are still too distant from Gln84 to form a hydrogen bond. Molecular dynamics simulations show large thermal movements of the third (gamma) sugar residue.

- **Key residues**: Thr797 (M6), Gln111 (M1), Glu312 (M4), Arg880 (loop M7-8)

## Advantages and Disadvantages

No advantages/disadvantages recorded.

## Comparison with Related Reagents

No comparison data available.

## Cross-References

- [Na+,K+-ATPase (Pig Kidney)](/xray-mp-wiki/proteins/pumps-atpases/na-k-atpase-pig-kidney/) — Primary target; E2P-DTX complex structure determined
- [Digoxin](/xray-mp-wiki/reagents/ligands/digoxin/) — Related cardiotonic steroid; differs by C12 hydroxyl group
- [Ouabain](/xray-mp-wiki/reagents/ligands/ouabain/) — Classical cardiotonic steroid; structural comparison
- [Cardiotonic Steroids](/xray-mp-wiki/concepts/miscellaneous/cardiotonic-steroids/) — Digitoxin is a cardiotonic steroid of the cardenolide class
