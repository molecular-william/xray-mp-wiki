---

title: TEV Protease
created: 2026-04-26
updated: 2026-04-27
type: reagent
tags: [purification-tag]
sources: [doi/10.1002##1873-3468.14136, doi/10.1016##j.bbrc.2019.12.091]

category: reagents
---
layout: default


# TEV Protease (Tobacco Etch Virus Protease)

## Overview

TEV protease is a highly specific cysteine protease that cleaves at the sequence ENLYFQG. It is the gold standard for removing affinity tags (His-tag, GST, MBP) from recombinant proteins after purification.

## Proteolysis Conditions (from this wiki)

- [nTMATE2-transporter](//xray-mp-wiki/proteins/nTMATE2-transporter/) — TEV(S219V) protease variant used
  - Condition: 4°C for 16 hours
  - Purpose: Remove C-terminal GFP-His8 tag after TALON affinity and SEC purification
  - The S219V mutation increases protease stability and activity at low temperature
- [etb-receptor](//xray-mp-wiki/proteins/etb-receptor/) — TEV protease cleavage between G57 and L66 to remove N-terminal Flag tag and disordered region; GFP-His₁₀ tag and TEV removed by TALON resin after cleavage

## Why TEV?

- **Specificity**: Recognizes 8-residue sequence (ENLYFQG), minimal off-target cleavage
- **Conditions**: Works at 4-30°C, pH 6-9, compatible with most buffers
- **Mutation variants**: TEV(S219V) is more stable than wild-type

## Related Purification Steps

- [talon-resin](//xray-mp-wiki/methods/purification/talon-resin/) — His-tag affinity capture (tag removed by TEV)
- [superdex-columns](//xray-mp-wiki/methods/purification/superdex-columns/) — SEC to separate cleaved tag and TEV protease