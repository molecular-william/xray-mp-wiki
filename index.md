---
title: X-ray MP Wiki
---

This is a wiki on reagents and procedures for X-ray crystallography of membrane proteins.

## Categories

- [Proteins](/xray-mp-wiki/categories/proteins/) - All protein pages
- [Reagents](/xray-mp-wiki/categories/reagents/) - Detergents, buffers, additives, lipids, ligands
- [Methods](/xray-mp-wiki/categories/methods/) - Crystallization, purification, expression systems
- [Concepts](/xray-mp-wiki/categories/concepts/) - Scientific concepts and mechanisms

## Content

This wiki contains pages organized into the categories above. Browse the category pages to find content on specific topics.

## Documentation

- [Wiki Reference](../references/WIKI-REFERENCE.md) — Domain, conventions, directory structure, entity page structures, tag taxonomy, correction policy, source-truth verification
- [Wiki Workflow](../references/WIKI-WORKFLOW.md) — Complete per-entity workflows: YAML schemas, generate/update commands, merge rules, pitfalls
- [Wiki Scripts](../references/WIKI-SCRIPTS.md) — Script inventory, usage, architecture, testing

## Health

Last updated: {{ site.time | date: "%Y-%m-%d" }}

{% assign protein_count = 0 %}
{% assign reagent_count = 0 %}
{% assign method_count = 0 %}
{% assign concept_count = 0 %}
{% assign total_count = 0 %}

{% for page in site.pages %}
{% if page.path contains '.md' %}
{% unless page.path contains 'index.md' %}
{% unless page.path contains 'SCHEMA' %}
{% assign total_count = total_count | plus: 1 %}
{% if page.path contains 'proteins/' %}
{% assign protein_count = protein_count | plus: 1 %}
{% elsif page.path contains 'reagents/' %}
{% assign reagent_count = reagent_count | plus: 1 %}
{% elsif page.path contains 'methods/' %}
{% assign method_count = method_count | plus: 1 %}
{% elsif page.path contains 'concepts/' %}
{% assign concept_count = concept_count | plus: 1 %}
{% endif %}
{% endunless %}
{% endunless %}
{% endif %}
{% endfor %}

| Category | Pages |
|----------|-------|
| Proteins | {{ protein_count }} |
| Reagents | {{ reagent_count }} |
| Methods | {{ method_count }} |
| Concepts | {{ concept_count }} |
| **Total** | **{{ total_count }}** |

{% assign stale_count = 0 %}
{% for page in site.pages %}
{% if page.path contains 'proteins/' or page.path contains 'reagents/' or page.path contains 'methods/' or page.path contains 'concepts/' %}
{% if page.path contains '.md' %}
{% unless page.path contains 'index.md' %}
{% unless page.path contains 'SCHEMA' %}
{% if page.updated %}
{% assign updated = page.updated | date: "%s" %}
{% assign now = "now" | date: "%s" %}
{% assign diff = now | minus: updated %}
{% if diff > 2592000 %}
{% assign stale_count = stale_count | plus: 1 %}
{% endif %}
{% endif %}
{% endunless %}
{% endunless %}
{% endif %}
{% endif %}
{% endfor %}

**{{ stale_count }}** pages not updated in the last 30 days.

For a detailed audit: `python3 ~/Desktop/Research/coding_projects/xray-mp-wiki/scripts/lint.py`

<!-- WIKI CATALOG
| type | path | title | summary |
|------|------|-------|---------|
| concept | concepts/construct-design/agonist-to-antagonist-conversion/ | Agonist-to-Antagonist Conversion via C8 Modification | Concept: agonist-to-antagonist-conversion |
| concept | concepts/construct-design/autophagic-snare-fusion-mechanism/ | Autophagic SNARE Fusion Mechanism | Autophagosome-lysosome fusion is mediated by the autophagic [SNARE Complex](/xra |
| concept | concepts/construct-design/darpin/ | Designed Ankyrin Repeat Protein (DARPin) | Designed Ankyrin Repeat Proteins (DARPins) are modular protein scaffolds
| concept | concepts/construct-design/nonhallucinogenic-psychedelic-analog-design/ | Nonhallucinogenic Psychedelic Analog Design | Structure-based design of nonhallucinogenic psychedelic analogs represents a the |
| concept | concepts/construct-design/pe-ppe-fusion-proteins/ | PE-PPE Fusion Proteins | PE-PPE fusion proteins are chimeric proteins that combine the N-terminal PE (Pro |
| concept | concepts/construct-design/structure-based-antipsychotic-design/ | Structure-Based Design of Third-Generation Antipsychotics | Structure-based design of third-generation antipsychotics represents a rational  |
| concept | concepts/construct-design/thermostabilization/ | Protein Thermostabilization | Protein thermostabilization is a construct design strategy in which targeted poi |
| concept | concepts/construct-design/voltage-sensor-paddle/ | Voltage-Sensor Paddle | The voltage-sensor paddle is a helix-turn-helix structural motif found in voltag |
| concept | concepts/construct-design/voltage-sensor-trapping/ | Voltage-Sensor Trapping | Voltage-sensor trapping is a mechanism of ion channel inhibition in which a smal |
| concept | concepts/enzyme-mechanisms/aaa-protease-mechanism/ | AAA Protease Mechanism | [AAA](/xray-mp-wiki/reagents/ligands/aaa/)+ proteases (ATPases associated with v |
| concept | concepts/enzyme-mechanisms/binding-change-mechanism/ | Binding-Change Mechanism | The binding-change mechanism is the catalytic mechanism proposed for ATP synthas |
| concept | concepts/enzyme-mechanisms/caax-protein-processing/ | CAAX Protein Processing | CAAX protein processing is a series of post-translational modifications of the C |
| concept | concepts/enzyme-mechanisms/carboxylate-dyad/ | Carboxylate Dyad in Oligosaccharyltransferase | The carboxylate dyad is a catalytic motif in oligosaccharyltransferase (OST) enz |
| concept | concepts/enzyme-mechanisms/diiron-center-mechanism/ | Diiron Center Mechanism in Membrane Desaturases | The diiron center in membrane-bound desaturases, exemplified by [Stearoyl-CoA](/ |
| concept | concepts/enzyme-mechanisms/disulfide-bond-formation/ | Disulfide Bond Formation in Bacteria | Disulfide bond formation in bacteria is catalyzed by the Dsb system, comprising  |
| concept | concepts/enzyme-mechanisms/enzyme-rhodopsins/ | Enzyme Rhodopsins | Enzyme rhodopsins are a recently discovered class of microbial
| concept | concepts/enzyme-mechanisms/f1-atpase-rotary-mechanism/ | F1-ATPase Rotary Catalytic Mechanism | Concept: f1-atpase-rotary-mechanism |
| concept | concepts/enzyme-mechanisms/gamma-secretase/ | Gamma-Secretase Complex | Gamma-secretase is an intramembrane protease complex responsible for the generat |
| concept | concepts/enzyme-mechanisms/gxgd-proteases/ | GXGD Proteases | Concept: gxgd-proteases |
| concept | concepts/enzyme-mechanisms/internal-counterion-mechanism/ | Internal Counterion Mechanism in P-Type ATPases | Many P-type ATPases require counterion transport to complete their reaction cycl |
| concept | concepts/enzyme-mechanisms/kok-cycle/ | Kok Cycle | The Kok cycle (also known as the S-state cycle) is the four-step mechanism of wa |
| concept | concepts/enzyme-mechanisms/nickel-pincer-nucleotide-cofactor-biosynthesis/ | Nickel-Pincer Nucleotide Cofactor Biosynthesis | Concept: nickel-pincer-nucleotide-cofactor-biosynthesis |
| concept | concepts/enzyme-mechanisms/non-competitive-inhibition/ | Non-competitive Inhibition of Rhomboid Proteases | Non-competitive inhibition is the characteristic mode of inhibition exhibited by |
| concept | concepts/enzyme-mechanisms/nucleoside-inhibitor-binding-mray/ | Nucleoside Inhibitor Binding to MraY: Chemical Logic and Hotspot Barcode | MraY (phospho-MurNAc-pentapeptide translocase) is the target of five
| concept | concepts/enzyme-mechanisms/ost-catalytic-cycle/ | Catalytic Cycle of Oligosaccharyltransferase | Concept: ost-catalytic-cycle |
| concept | concepts/enzyme-mechanisms/p-type-atpase-mechanism/ | P-type ATPase Mechanism | Concept: p-type-atpase-mechanism |
| concept | concepts/enzyme-mechanisms/peripheral-stalk-elasticity/ | Peripheral Stalk Elasticity in Rotary ATPases | Concept: peripheral-stalk-elasticity |
| concept | concepts/enzyme-mechanisms/phosphoenzyme-e2p-state/ | Phosphoenzyme E2P State | The E2P state is a phosphorylated intermediate of P-type ATPases in which the en |
| concept | concepts/enzyme-mechanisms/ping-pong-mechanism/ | Ping-Pong Catalytic Mechanism | Concept: ping-pong-mechanism |
| concept | concepts/enzyme-mechanisms/quinol-fumarate-reductase/ | Quinol-Fumarate Reductase (QFR) | Concept: quinol-fumarate-reductase |
| concept | concepts/enzyme-mechanisms/rhomboid-protease-substrate-specificity/ | Rhomboid Protease Substrate Specificity | Rhomboid intramembrane proteases exhibit sequence-specific cleavage of transmemb |
| concept | concepts/enzyme-mechanisms/rotary-atpase-mechanism/ | Rotary ATPase Mechanism | Concept: rotary-atpase-mechanism |
| concept | concepts/enzyme-mechanisms/ser-lys-catalytic-mechanism/ | Ser/Lys Catalytic Mechanism | Concept: ser-lys-catalytic-mechanism |
| concept | concepts/enzyme-mechanisms/serca-e2-e1-transition/ | SERCA E2 to E1 Transition Mechanism | The E2→E1 transition in SERCA (sarco(endo)plasmic reticulum Ca²⁺-ATPase) is the
| concept | concepts/enzyme-mechanisms/serca-e2p-dephosphorylation-counterion-occlusion/ | SERCA E2-P Dephosphorylation and Counterion Occlusion | The dephosphorylation of the SERCA calcium pump E2-P state is coupled to occlusi |
| concept | concepts/enzyme-mechanisms/si-face-cleavage/ | si-Face Cleavage in Rhomboid Proteases | Concept: si-face-cleavage |
| concept | concepts/enzyme-mechanisms/trex1-rnase-activity/ | TREX1 RNase Activity and DNA/RNA Hybrid Processing | [Mouse TREX1 (Three Prime Repair Exonuclease 1)](/xray-mp-wiki/proteins/gpcr/tre |
| concept | concepts/enzyme-mechanisms/two-stage-catalytic-mechanism/ | Two-Stage Catalytic Mechanism of Rhomboid Proteases | Rhomboid intramembrane proteases catalyze substrate cleavage through a two-stage |
| concept | concepts/enzyme-mechanisms/vanadate-inhibition/ | Vanadate Inhibition of P-type ATPases | Vanadate is the hallmark inhibitor of the P-type ATPase family. Crystal structur |
| concept | concepts/enzyme-mechanisms/vitamin-k-cycle/ | Vitamin K Cycle | The [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) cycle is a biochemi |
| concept | concepts/membrane-mimetics/computational-transmembrane-protein-design/ | Computational Design of Multipass Transmembrane Proteins | A methodology for the de novo computational design of multipass transmembrane pr |
| concept | concepts/membrane-mimetics/force-from-lipid-principle/ | Force-from-Lipid Principle in Mechanosensation | The force-from-lipid (FFL) principle posits that mechanosensitive ion channels a |
| concept | concepts/membrane-mimetics/heavy-atom-derivative-detergents-and-lipids/ | Heavy Atom Derivative Detergents and Lipids for Membrane Protein Crystallography | Heavy atom derivative detergents and lipids are artificially synthesized amphiph |
| concept | concepts/membrane-mimetics/inner-membrane/ | Inner Membrane | The inner (cytoplasmic) membrane of Gram-negative bacteria is the primary permea |
| concept | concepts/membrane-mimetics/intramembrane-ion-coordination/ | Intramembrane Ion Coordination | Intramembrane ion coordination refers to the phenomenon where metal cations (suc |
| concept | concepts/membrane-mimetics/intramembrane-proteolysis/ | Intramembrane Proteolysis | Concept: intramembrane-proteolysis |
| concept | concepts/membrane-mimetics/lipid-annulus/ | Lipid Annulus in Membrane Protein Structures | A lipid annulus is a belt of ordered lipid molecules surrounding a membrane prot |
| concept | concepts/membrane-mimetics/lipidic-sponge-phase/ | Lipidic Sponge Phase (LSP) | The lipidic sponge phase (LSP) is a liquid-like isotropic phase formed by a mixt |
| concept | concepts/membrane-mimetics/membrane-mimetics/ | Membrane Mimetics and Structural Biology | Concept: membrane-mimetics |
| concept | concepts/membrane-mimetics/membrane-protein-crystals-for-neutron-diffraction/ | Membrane-Protein Crystals for Neutron Diffraction | Neutron macromolecular crystallography (NMX) can identify individual protons
| concept | concepts/membrane-mimetics/membrane-protein-lipid-adaptation/ | Membrane Protein-Lipid Bilayer Adaptation | Membrane protein-lipid bilayer adaptation refers to the mutual structural adjust |
| concept | concepts/membrane-mimetics/n-glycosylation-sequon/ | N-Glycosylation Sequon | The N-glycosylation sequon (Asn-X-Ser/Thr, where X is not Pro) is the minimal co |
| concept | concepts/membrane-mimetics/noble-gas-anaesthetic-mechanism/ | Noble Gas Anaesthetic Mechanism via Membrane Protein Surface Binding | Noble gases (xenon, krypton, argon) are general anaesthetics whose mechanism of  |
| concept | concepts/membrane-mimetics/outer-membrane/ | Outer Membrane | The outer membrane is the outermost lipid bilayer of Gram-negative bacteria, com |
| concept | concepts/membrane-mimetics/selective-lipid-binding/ | Selective Lipid Binding in Membrane Proteins | Selective lipid binding refers to the phenomenon where membrane proteins discrim |
| concept | concepts/membrane-mimetics/self-processing/ | Self-processing of Membrane Proteins | Self-processing refers to the phenomenon where a membrane protein cleaves its ow |
| concept | concepts/membrane-mimetics/site-directed-spin-labeling-membrane-protein/ | Site-Directed Spin Labeling on Membrane Protein alpha-Helical Sites | Site-directed spin labeling (SDSL) combined with electron paramagnetic resonance |
| concept | concepts/membrane-mimetics/yidc-dual-function/ | YidC Dual Insertase/Chaperone Function | The YidC protein from Gram-negative bacteria is a unique dual-function membrane  |
| concept | concepts/methods-techniques/c41-e-coli-expression-strain/ | E. coli C41 Expression Strain | E. coli C41 is a genetically engineered expression strain derived from E. coli B |
| concept | concepts/methods-techniques/continuous-diffraction/ | Continuous Diffraction in Macromolecular Crystallography | Continuous diffraction refers to the incoherent sum of Fraunhofer diffraction pa |
| concept | concepts/methods-techniques/epitaxial-twinning/ | Epitaxial Twinning | Epitaxial twinning is a crystallographic phenomenon in which two or more crystal |
| concept | concepts/methods-techniques/high-viscosity-sample-injection-for-sfx/ | High-Viscosity Sample Injection for Serial Femtosecond Crystallography | High-viscosity sample injection is a sample delivery method for [Serial Femtosec |
| concept | concepts/methods-techniques/in-situ-crystallography/ | In situ X-ray Crystallography | In situ X-ray crystallography is a technique where X-ray diffraction data are co |
| concept | concepts/methods-techniques/lcp-microseeding-for-serial-crystallography/ | LCP Microseeding for Serial Crystallography | LCP microseeding for serial crystallography is a crystallization strategy that c |
| concept | concepts/methods-techniques/long-wavelength-native-sad-phasing/ | Long-Wavelength Native-SAD Phasing | Long-wavelength native-SAD phasing is an experimental X-ray crystallographic pha |
| concept | concepts/methods-techniques/merohedral-twinning/ | Merohedral Twinning in Protein Crystallography | Merohedral twinning is a crystal growth defect in which two or more crystal
| concept | concepts/methods-techniques/multiphoton-effects-in-time-resolved-crystallography/ | Multiphoton Effects in Time-Resolved Serial Femtosecond Crystallography | Time-resolved serial femtosecond crystallography (TR-SFX) at X-ray free-electron |
| concept | concepts/methods-techniques/serial-millisecond-crystallography/ | Serial Millisecond Crystallography (SMX) | Serial millisecond crystallography (SMX) is a room-temperature crystallographic  |
| concept | concepts/methods-techniques/steered-molecular-dynamics/ | Steered Molecular Dynamics (SMD) | Steered Molecular Dynamics (SMD) is a computational simulation technique where a |
| concept | concepts/methods-techniques/truncation/ | Protein Truncation for Crystallization | Protein truncation is a construct design strategy in which flexible, unstructure |
| concept | concepts/methods-techniques/x-ray-radiation-damage/ | X-Ray Radiation Damage in Crystallography | Concept: x-ray-radiation-damage |
| concept | concepts/miscellaneous/axillary-malodour-production-pathway/ | Axillary Malodour Production Pathway | Axillary (underarm) malodour is produced by specific skin bacteria metabolizing  |
| concept | concepts/miscellaneous/binder-clip-motion/ | Binder Clip Motion | Binder clip-like motion is a conformational mechanism in [SemiSWEET Transporter  |
| concept | concepts/miscellaneous/calcium-bowl/ | Ca2+ Bowl | The Ca2+ bowl is a stretch of well-conserved aspartate residues within the secon |
| concept | concepts/miscellaneous/carbon-catabolite-repression/ | Carbon Catabolite Repression | Carbon catabolite repression (CCR) is a global regulatory phenomenon in bacteria |
| concept | concepts/miscellaneous/cardiac-glycoside-binding-mechanism/ | Cardiac Glycoside Binding Mechanism | Cardiac glycosides (e.g., [Ouabain](/xray-mp-wiki/reagents/ligands/ouabain), dig |
| concept | concepts/miscellaneous/cardiotonic-steroids/ | Cardiotonic Steroids | Cardiotonic steroids (CTS), also known as cardiac glycosides, are a class of inh |
| concept | concepts/miscellaneous/charge-transfer-interaction/ | Charge-Transfer Interaction | A charge-transfer interaction is a non-covalent interaction between an electron  |
| concept | concepts/miscellaneous/cholesterol-dependent-cytolysins/ | Cholesterol-Dependent Cytolysins | Cholesterol-dependent cytolysins (CDCs) are a family of bacterial pore-forming t |
| concept | concepts/miscellaneous/claudin-paracellular-ion-selectivity/ | Claudin-Mediated Paracellular Ion Selectivity | Claudins are the major structural components of tight junctions (TJs) that contr |
| concept | concepts/miscellaneous/co2-concentrating-mechanism/ | CO2-Concentrating Mechanism (CCM) | The CO2-concentrating mechanism (CCM) is an adaptive system evolved by cyanobact |
| concept | concepts/miscellaneous/flickering-gate-mechanism/ | Flickering-Gate Mechanism | The flickering-gate mechanism proposes that the extracellular gate of P-type ATP |
| concept | concepts/miscellaneous/get-pathway/ | GET Pathway for Tail-Anchored Protein Insertion | The guided entry of tail-anchored proteins (GET) pathway is a conserved eukaryot |
| concept | concepts/miscellaneous/hydrogen-bonding-networks-reaction-centers/ | Hydrogen-Bonding Networks in Photosynthetic Reaction Centers | Hydrogen-bonding networks near the primary electron donor ([Bacteriochlorophyll] |
| concept | concepts/miscellaneous/hydrophilic-groove-insertion/ | Hydrophilic Groove Insertion Mechanism | The hydrophilic groove insertion mechanism describes how YidC inserts single-spa |
| concept | concepts/miscellaneous/hydrophobic-tunnel-smo/ | Hydrophobic Tunnel for Sterol Access in Smoothened | The hydrophobic tunnel is a conduit between transmembrane helices TM5 and TM6 of |
| concept | concepts/miscellaneous/inducer-exclusion/ | Inducer Exclusion | Inducer exclusion is a mechanism of [Carbon Catabolite Repression](/xray-mp-wiki |
| concept | concepts/miscellaneous/k-lt-intermediate/ | K_LT Intermediate | The K_LT intermediate is a low-temperature photointermediate in the [Bacteriorho |
| concept | concepts/miscellaneous/k2p-modulator-pocket/ | K2P Modulator Pocket | Concept: k2p-modulator-pocket |
| concept | concepts/miscellaneous/ligand-efficiency/ | Ligand Efficiency in Drug Discovery | Ligand efficiency (LE) is a metric used in drug discovery to assess how efficien |
| concept | concepts/miscellaneous/manganese-calcium-cluster/ | Manganese-Calcium Cluster (Mn4Ca Cluster) | Concept: manganese-calcium-cluster |
| concept | concepts/miscellaneous/mechanotransmission/ | Mechanotransmission | Mechanotransmission is a transmembrane conformational coupling mechanism used by |
| concept | concepts/miscellaneous/nephrogenic-diabetes-insipidus/ | Nephrogenic Diabetes Insipidus | Nephrogenic diabetes insipidus (NDI) is a water balance disorder
| concept | concepts/miscellaneous/non-photochemical-quenching/ | Non-photochemical Quenching (NPQ) in LHC-II | Non-photochemical quenching (NPQ) is a photoprotective mechanism in plants that  |
| concept | concepts/miscellaneous/p-glycoprotein-induced-fit-binding/ | P-glycoprotein Induced-Fit Binding | P-glycoprotein (P-gp) employs an induced-fit mechanism for substrate
| concept | concepts/miscellaneous/periplasm/ | Periplasm (Periplasmic Space) | The periplasm is the gel-like compartment between the inner and outer membranes  |
| concept | concepts/miscellaneous/ph-dependent-quinone-binding-reaction-center/ | pH-Dependent Quinone Binding in Photosynthetic Reaction Centers | The secondary quinone (QB) in bacterial photosynthetic reaction centers occupies |
| concept | concepts/miscellaneous/qse-efg-three-component-system/ | QseE/F/G Three-Component System | The QseE/F/G three-component system is a bacterial signal transduction system th |
| concept | concepts/miscellaneous/quartet-core/ | Quartet Core Mechanism in S1PR3 | The quartet core is a set of four residues in the sphingosine-1-phosphate recept |
| concept | concepts/miscellaneous/selective-starvation/ | Selective Starvation of Malaria Parasites | The selective starvation strategy is an antimalarial approach that exploits the  |
| concept | concepts/miscellaneous/sodium-motive-force/ | Sodium-Motive Force (SMF) | The sodium-motive force (smf) is an electrochemical gradient of Na+ ions
| concept | concepts/miscellaneous/sulfonamide-resistance/ | Sulfonamide Resistance | Sulfonamide resistance is a major clinical problem that emerged rapidly followin |
| concept | concepts/miscellaneous/surface-hydroxyl-acidity/ | Surface Hydroxyl Acidity | The acidity of individual surface hydroxyl groups determines the deprotonation/p |
| concept | concepts/miscellaneous/syringe-injection-mechanism/ | Syringe-Like Injection Mechanism of Tc Toxins | The syringe-like injection mechanism describes how Tc (toxin complex) toxins fro |
| concept | concepts/miscellaneous/termini-restraining/ | Termini Restraining | Termini restraining is a protein engineering strategy for stabilizing small memb |
| concept | concepts/miscellaneous/ton-complex/ | Ton Complex | The Ton complex is an energy-transducing protein assembly located in the inner m |
| concept | concepts/miscellaneous/vault-ribonucleoprotein-particles/ | Vault Ribonucleoprotein Particles | Vaults are large ribonucleoprotein (RNP) particles found in a wide variety of eu |
| concept | concepts/protein-families/alpha-helical-pore-forming-toxin-family/ | Alpha-Helical Pore-Forming Toxin Family (pfam05791) | The alpha-helical pore-forming toxin family (pfam05791) comprises a group of
| concept | concepts/protein-families/cation-diffusion-facilitator-family/ | Cation Diffusion Facilitator (CDF) Family | The Cation Diffusion Facilitator (CDF) family is a ubiquitous family of
| concept | concepts/protein-families/cdp-alcohol-phosphotransferase-family/ | CDP-Alcohol Phosphotransferase Family | The CDP-alcohol phosphotransferase (CDP-AP) family comprises integral membrane e |
| concept | concepts/protein-families/cytochrome-b561-family/ | Cytochrome b561 (Cyt b561) Protein Family | The cytochrome b561 (Cyt b561) family is a group of highly conserved
| concept | concepts/protein-families/deddh-exonuclease-family/ | DEDDh Exonuclease Family | The DEDDh exonuclease family is named after four catalytic residues (Asp, Glu, A |
| concept | concepts/protein-families/dhhc-palmitoyltransferase-family/ | DHHC Palmitoyltransferase Family | The DHHC (Asp-His-His-Cys) palmitoyltransferase family comprises eukaryotic
| concept | concepts/protein-families/di-iron-desaturase/ | Di-Iron-Containing Desaturase Family | The di-iron-containing desaturase family comprises enzymes that catalyze the int |
| concept | concepts/protein-families/duf3413-family/ | DUF3413 (PF11893) Protein Family | DUF3413 (Domain of Unknown Function 3413, Pfam family PF11893) is a conserved
| concept | concepts/protein-families/mapag-superfamily/ | MAPEG Superfamily | The MAPEG (Membrane-Associated Proteins involved in Eicosanoid and Glutathione m |
| concept | concepts/protein-families/mce-protein-family/ | MCE Protein Family | The MCE (mammalian cell entry) protein superfamily comprises highly conserved pr |
| concept | concepts/protein-families/mfs-transporter/ | Major Facilitator Superfamily (MFS) | The Major Facilitator Superfamily (MFS) is one of the largest families of second |
| concept | concepts/protein-families/nitrilase-superfamily/ | Nitrilase Superfamily | Concept: nitrilase-superfamily |
| concept | concepts/protein-families/nnp-family/ | Nitrate/Nitrite Porter (NNP) Family | The nitrate/nitrite porter (NNP) family is a subfamily of the major facilitator
| concept | concepts/protein-families/p-type-atpase/ | P-type ATPase Family | P-type ATPases are a major family of ion-transporting ATPases that form a covale |
| concept | concepts/protein-families/pap2-family/ | Type II Phosphatidic Acid Phosphatase (PAP2) Family | Type II [Phosphatidic Acid](/xray-mp-wiki/reagents/lipids/phosphatidic-acid/) ph |
| concept | concepts/protein-families/pib-4-atpase-family/ | PIB-4-Type ATPase Family | PIB-4-ATPases are a subclass of heavy-metal transporting P-type (P1B) ATPases wi |
| concept | concepts/protein-families/pnpt-superfamily/ | PNPT Superfamily (Polypropenyl-phosphate N-acetyl hexosamine 1-phosphate Transferase) | The polypropenyl-phosphate N-acetyl hexosamine 1-phosphate transferase (PNPT)
| concept | concepts/protein-families/pot-family-substrate-specificity/ | POT Family Substrate Specificity by Electrostatic Interactions | Peptide transporters of the proton-dependent oligopeptide transporter (POT)
| concept | concepts/protein-families/pq-loop-family/ | PQ-Loop Family | The PQ-loop family is a group of membrane transporters defined by a conserved Pr |
| concept | concepts/protein-families/rh-amt-mep-protein-family/ | Rh/Amt/MEP Protein Family | Concept: rh-amt-mep-protein-family |
| concept | concepts/protein-families/rhomboid-protease/ | Rhomboid Protease Family | Concept: rhomboid-protease |
| concept | concepts/protein-families/rnd-superfamily/ | Resistance-Nodulation-Cell Division (RND) Superfamily | The RND superfamily comprises large tripartite efflux pumps that transport diver |
| concept | concepts/protein-families/sed-s-protein-family/ | SEDS Protein Family | The Shape, Elongation, Division, and Sporulation (SEDS) proteins are a large fam |
| concept | concepts/protein-families/site-2-protease-family-mechanism/ | Site-2 Protease Family Mechanism | Site-2 proteases (S2Ps) are a conserved family of zinc metalloproteases that per |
| concept | concepts/protein-families/slac1-superfamily/ | SLAC1 Superfamily | The [SLAC1 (SLOW ANION CHANNEL 1 from Arabidopsis thaliana)](/xray-mp-wiki/prote |
| concept | concepts/protein-families/slc11-nramp-family/ | SLC11 (NRAMP) Family | The SLC11 (Solute Carrier 11) family, also known as the NRAMP (Natural Resistanc |
| concept | concepts/protein-families/sm-family/ | SMR Family (Small Multidrug Resistance Family) | The small multidrug resistance (SMR) family is a group of bacterial multidrug ef |
| concept | concepts/protein-families/sugar-porter-family/ | Sugar Porter (SP) Family | Concept: sugar-porter-family |
| concept | concepts/protein-families/tetraspanin-family/ | Tetraspanin Family | Tetraspanins are a large family of four-pass transmembrane proteins (TM4SF)
| concept | concepts/protein-families/tmbim-protein-family/ | TMBIM Protein Family | The TMBIM (transmembrane Bax inhibitor motif) protein family comprises highly co |
| concept | concepts/protein-families/tmem16-family/ | TMEM16 Family (Anoctamin Protein Family) | The TMEM16 family (also known as anoctamin family) is a group of eukaryotic memb |
| concept | concepts/protein-families/wxg100-family-proteins/ | WxG100 Family Proteins | The WxG100 family (also known as the ESAT-6 family) comprises small helical prot |
| concept | concepts/protein-families/yidc-oxa1-alb3-insertase-family/ | YidC/Oxa1/Alb3 Insertase Family | The [YidC/Oxa1/Alb3 Family](/xray-mp-wiki/concepts/protein-families/yidc-oxa1-al |
| concept | concepts/rhodopsin-mechanisms/bacteriorhodopsin-photocycle/ | Bacteriorhodopsin Photocycle | The bacteriorhodopsin photocycle is a sequence of light-induced conformational
| concept | concepts/rhodopsin-mechanisms/blue-shifted-rhodopsin-design/ | Blue-Shifted Rhodopsin Design Principle | The blue-shifted rhodopsin design principle uses atomistic rational design to cr |
| concept | concepts/rhodopsin-mechanisms/cyanorhodopsin/ | CyanoRhodopsin (CyR) | Concept: cyanorhodopsin |
| concept | concepts/rhodopsin-mechanisms/dark-adapted-state/ | Dark-Adapted State of Microbial Rhodopsins | The dark-adapted (DA) state is a desensitized conformation of microbial rhodopsi |
| concept | concepts/rhodopsin-mechanisms/dtg-dts-rhodopsin/ | DTG/DTS Rhodopsin | DTG/DTS rhodopsins are a family of light-driven outward proton-pumping [Microbia |
| concept | concepts/rhodopsin-mechanisms/evolution-of-rhodopsins/ | Evolution of Rhodopsins | Concept: evolution-of-rhodopsins |
| concept | concepts/rhodopsin-mechanisms/light-adapted-state/ | Light-Adapted State of Microbial Rhodopsins | The light-adapted (LA) state is the ground state of microbial rhodopsins establi |
| concept | concepts/rhodopsin-mechanisms/microbial-rhodopsins/ | Microbial Rhodopsins | Microbial rhodopsins are a family of seven-transmembrane helix proteins
| concept | concepts/rhodopsin-mechanisms/proton-release-complex/ | Proton Release Complex in Microbial Rhodopsins | The proton release complex (PRC) is a conserved structural motif in microbial rh |
| concept | concepts/rhodopsin-mechanisms/retinal-isomerization/ | Retinal Isomerization in Microbial Rhodopsins | Retinal isomerization is the fundamental photochemical event in microbial rhodop |
| concept | concepts/rhodopsin-mechanisms/rhodopsin-photocycle/ | Rhodopsin Photocycle | The rhodopsin photocycle involves light-induced isomerization of retinal from al |
| concept | concepts/signaling-receptors/anion-mediated-ligand-binding/ | Anion-Mediated Ligand Binding in iGluRs | Anion-mediated ligand binding is a mechanism in which chloride ions serve as sur |
| concept | concepts/signaling-receptors/antiparallel-dimerization/ | Antiparallel Dimerization in GPCR Crystallization | Antiparallel dimerization in the context of GPCR crystallization refers to the a |
| concept | concepts/signaling-receptors/beta-arrestin-signaling/ | Beta-Arrestin Signaling | Concept: beta-arrestin-signaling |
| concept | concepts/signaling-receptors/beta-arrestin/ | Beta-Arrestin | Beta-arrestins are multifunctional adaptor proteins that regulate GPCR signaling |
| concept | concepts/signaling-receptors/biased-agonism/ | Biased Agonism in G Protein-Coupled Receptors | Biased agonism refers to the ability of different ligands to preferentially acti |
| concept | concepts/signaling-receptors/calcium-as-gpcr-ligand-cofactor/ | Calcium as a Cofactor for GPCR Ligand Binding | Calcium ions (Ca2+) can act as a cofactor for ligand binding at the orthosteric  |
| concept | concepts/signaling-receptors/cck-receptor-peptide-selectivity/ | Peptide Selectivity in Cholecystokinin Receptors | Peptide selectivity in cholecystokinin receptors refers to the molecular basis b |
| concept | concepts/signaling-receptors/cck-receptor-stepwise-activation/ | Stepwise Activation of Cholecystokinin Receptors | The stepwise activation of cholecystokinin receptors (CCKₐR and CCKᴅR) describes |
| concept | concepts/signaling-receptors/central-core-disease/ | Central Core Disease and Ryanodine Receptor SPRY1 Domain | Central core disease (CCD) is a congenital myopathy associated with mutations in |
| concept | concepts/signaling-receptors/competitive-antagonism-cys-loop/ | Competitive Antagonism in Cys-Loop Receptors | Competitive antagonism in Cys-loop receptors occurs when a ligand binds to the o |
| concept | concepts/signaling-receptors/conserved-core-triad/ | Conserved Core Triad in GPCR Activation | The conserved core triad (FPI triad) consists of three highly conserved amino ac |
| concept | concepts/signaling-receptors/constitutive-active-gpcr-mutations/ | Constitutive Active GPCR Mutations | Constitutive active mutations (CAMs) in G-protein-coupled receptors (GPCRs) are
| concept | concepts/signaling-receptors/cpvt/ | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) and Ryanodine Receptor | Catecholaminergic polymorphic ventricular tachycardia (CPVT) is a genetic cardia |
| concept | concepts/signaling-receptors/cys-loop-receptor-family/ | Cys-Loop Receptor Family | Concept: cys-loop-receptor-family |
| concept | concepts/signaling-receptors/desensitization-in-cys-loop-receptors/ | Desensitization in Cys-Loop Receptors | Desensitization is a fundamental regulatory mechanism in Cys-loop receptors wher |
| concept | concepts/signaling-receptors/dual-orexin-receptor-antagonist/ | Dual Orexin Receptor Antagonist (DORA) | Dual orexin receptor antagonists (DORAs) are therapeutic compounds that inhibit  |
| concept | concepts/signaling-receptors/efficacy-switches/ | Efficacy Switches in GPCR Signaling | Efficacy switches are molecular mechanisms by which specific residues in G prote |
| concept | concepts/signaling-receptors/er-retrieval-mechanism/ | ER Retrieval Mechanism (KDEL Receptor) | Concept: er-retrieval-mechanism |
| concept | concepts/signaling-receptors/extra-helical-binding-site/ | Extra-helical Binding Site in GPCRs | Concept: extra-helical-binding-site |
| concept | concepts/signaling-receptors/extracellular-domain-gpcr-allostery/ | Extracellular Domain-Mediated Allostery in GPCRs | Extracellular domain-mediated allostery refers to the mechanism by which large e |
| concept | concepts/signaling-receptors/g-protein/ | Heterotrimeric G Protein | Heterotrimeric G proteins are composed of alpha, beta, and gamma subunits. They  |
| concept | concepts/signaling-receptors/gpcr-active-conformation/ | GPCR Active Conformation | GPCRs adopt distinct active and inactive conformations. The active state is char |
| concept | concepts/signaling-receptors/gpcr-active-state-high-affinity-agonist-binding/ | GPCR Active State High-Affinity Agonist Binding | A mechanistic principle explaining why G protein-coupled receptors (GPCRs) in th |
| concept | concepts/signaling-receptors/gpcr-chemokine-recognition/ | GPCR-Chemokine Recognition (CRS1/CRS1.5/CRS2) | Chemokine receptors (CKRs) are class A G protein-coupled receptors (GPCRs) that  |
| concept | concepts/signaling-receptors/gpcr-dimerization/ | GPCR Dimerization | GPCR dimerization refers to the formation of homo- and hetero-oligomeric complex |
| concept | concepts/signaling-receptors/gpcr-g-protein-arrestin-common-interface/ | GPCR G Protein-Arrestin Common Interface | G-protein-coupled receptors (GPCRs) transmit extracellular signals to activate i |
| concept | concepts/signaling-receptors/gpcr-g-protein-coupling/ | GPCR-G Protein Coupling Mechanism | GPCR-G protein coupling is the fundamental mechanism by which G protein-coupled  |
| concept | concepts/signaling-receptors/gpcr-inactive-conformation/ | GPCR Inactive Conformation | The inactive conformation of G-protein-coupled receptors (GPCRs), also known as  |
| concept | concepts/signaling-receptors/gpcr/ | G Protein-Coupled Receptor (GPCR) Family | GPCRs are the largest family of cell surface receptors, characterized by seven t |
| concept | concepts/signaling-receptors/gpr6-constitutive-activity/ | GPR6 High Constitutive Activity and Orphan Receptor Signaling | [GPR6 — Orphan G Protein-Coupled Receptor Implicated in Parkinson's Disease](/xr |
| concept | concepts/signaling-receptors/helical-recoil-desensitization/ | Helical Recoil Model of P2X Receptor Desensitization | The helical recoil model describes the molecular mechanism of P2X receptor desen |
| concept | concepts/signaling-receptors/heteromeric-ampa-receptor-organization/ | Heteromeric AMPA Receptor Organization | Heteromeric AMPA-type glutamate receptors (AMPARs), composed of GluA1-4 subunits |
| concept | concepts/signaling-receptors/intracellular-allosteric-antagonism/ | Intracellular Allosteric Antagonism at Chemokine Receptors | Intracellular allosteric antagonism is a mechanism of GPCR inhibition where
| concept | concepts/signaling-receptors/inverse-agonism/ | Inverse Agonism in GPCR Signaling | Inverse agonism refers to the ability of certain ligands to reduce the basal (co |
| concept | concepts/signaling-receptors/kctd-modulation-gabab-receptor/ | KCTD-Mediated Modulation of GABA_B Receptor Signaling | KCTD (potassium channel tetramerization domain-containing) proteins, specificall |
| concept | concepts/signaling-receptors/lipid-activation-5ht2a-receptor/ | Lipid Activation of 5-HT2A Receptor | The human serotonin 2A receptor (5-HT2AR) is modulated by lipids including monoo |
| concept | concepts/signaling-receptors/malignant-hyperthermia/ | Malignant Hyperthermia and Ryanodine Receptor Mutations | Malignant hyperthermia is a genetic disorder associated with mutations in the [R |
| concept | concepts/signaling-receptors/n-terminal-t4-lysozyme-fusion/ | N-Terminal T4 Lysozyme Fusion for GPCR Crystallization | N-terminal T4 lysozyme ([T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/)) |
| concept | concepts/signaling-receptors/negative-allosteric-modulation/ | Negative Allosteric Modulation in GPCRs | Negative allosteric modulation (NAM) refers to the ability of a ligand to bind t |
| concept | concepts/signaling-receptors/ntd-lbd-allosteric-coupling-iglurs/ | NTD-LBD Allosteric Coupling in Ionotropic Glutamate Receptors | In heteromeric AMPA receptors, the compact O-shape architecture brings the N-ter |
| concept | concepts/signaling-receptors/orexin-receptor-subtype-selectivity/ | Structure-Based GPCR Subtype Selectivity via Single Residue Differences | Structure-based exploitation of single amino acid differences between GPCR subty |
| concept | concepts/signaling-receptors/p2x-receptor-family/ | P2X Receptor Family | The P2X receptor family comprises a group of ligand-gated ion channels activated |
| concept | concepts/signaling-receptors/p2y-receptor-family/ | P2Y Receptor Family | The P2Y receptors are a family of purinergic G-protein-coupled receptors (GPCRs) |
| concept | concepts/signaling-receptors/paqr-family/ | PAQR Family (Progesterone and AdipoQ Receptor Family) | The progesterone and adipoQ receptor (PAQR) family comprises integral membrane p |
| concept | concepts/signaling-receptors/photocyclic-gpcr-activation/ | Photocyclic GPCR Activation | Photocyclic GPCR activation refers to the ability of a G protein-coupled recepto |
| concept | concepts/signaling-receptors/phototaxis-signaling-rhodopsin/ | Phototaxis Signaling in Microbial Rhodopsins | Phototaxis signaling in microbial rhodopsins is a process where light-activated  |
| concept | concepts/signaling-receptors/pii-protein-family/ | PII Signal Transduction Protein Family | The PII signal transduction protein family is a widespread family of small trime |
| concept | concepts/signaling-receptors/polar-network-gpcr-activation/ | Polar Network in GPCR Activation | The polar network is an extensive system of hydrogen bonds and water-mediated in |
| concept | concepts/signaling-receptors/prostanoid-receptor-family/ | Prostanoid Receptor Family | Prostanoid receptors are a family of class A G protein-coupled receptors that me |
| concept | concepts/signaling-receptors/sodium-allosteric-modulation/ | Sodium Ion Allosteric Modulation in GPCRs | Sodium ions (Na+) act as negative allosteric modulators of many class A G protei |
| concept | concepts/signaling-receptors/spyr-domain/ | SPRY Domain in Ryanodine Receptors | The SPRY domain is a protein domain named after 'SPIA kinase and Ryanodine Recep |
| concept | concepts/signaling-receptors/steric-trigger-mechanism/ | Steric Trigger Mechanism in Rhodopsin Signaling | The steric trigger mechanism describes how a specific hydrogen-bonded threonine- |
| concept | concepts/signaling-receptors/three-finger-toxin-gpcr-modulation/ | Three-Finger Toxin Scaffold for GPCR Modulation | Three-finger toxins (3FTs) are a superfamily of small protein toxins (65-80 amin |
| concept | concepts/signaling-receptors/two-component-signaling-system/ | Two-Component Signaling System (TCS) in Membrane Sensors | Two-component signaling systems (TCS) are the primary mechanism by which
| concept | concepts/signaling-receptors/two-site-binding-mode/ | Two-Site Peptide Ligand Binding Mode | Concept: two-site-binding-mode |
| concept | concepts/signaling-receptors/water-network-in-ligand-binding/ | Water Networks in GPCR Ligand Binding | Water molecules in GPCR ligand binding sites play a crucial role in determining  |
| concept | concepts/structural-mechanisms/3-omega-motif/ | 3 Omega Motif in Microbial Rhodopsins | The 3 omega motif is a structural motif in microbial rhodopsins formed by three  |
| concept | concepts/structural-mechanisms/ago-allosteric-modulator/ | Ago-Allosteric Modulator | An ago-allosteric modulator is a ligand that both activates a receptor (agonist  |
| concept | concepts/structural-mechanisms/allosteric-regulation/ | Allosteric Regulation in Membrane Proteins | Allosteric regulation is a fundamental mechanism by which ligand binding at one  |
| concept | concepts/structural-mechanisms/apolar-side-chain-packing/ | Apolar Side-Chain Packing in Membrane Proteins | Apolar side-chain packing is the primary driving force for folding and assembly  |
| concept | concepts/structural-mechanisms/atcase-allosteric-mechanism/ | Allosteric Mechanism of Aspartate Carbamoyltransferase | Aspartate carbamoyltransferase (ATCase) from Escherichia coli is the archetypal  |
| concept | concepts/structural-mechanisms/atp-induced-domain-rearrangement-p-type-atpases/ | ATP-Induced Domain Rearrangement in P-type ATPases | In P-type ATPases such as SERCA, ATP binding alone — without Ca2+ or phosphoryla |
| concept | concepts/structural-mechanisms/c-terminus/ | C-Terminus (C-Terminal Domain) | The C-terminus (C-terminal domain) of a protein is the end of the polypeptide ch |
| concept | concepts/structural-mechanisms/c-type-inactivation/ | C-type Inactivation | Concept: c-type-inactivation |
| concept | concepts/structural-mechanisms/carboxylate-shift/ | Carboxylate Shift | The carboxylate shift is a catalytic mechanism observed in Class I
| concept | concepts/structural-mechanisms/chloride-binding-sites-psii/ | Chloride-Binding Sites in Photosystem II | The chloride ion (Cl-) is an essential cofactor for oxygen evolution in photosys |
| concept | concepts/structural-mechanisms/claudin-tight-junction-architecture/ | Claudin Tight Junction Architecture | Claudins are the major structural components of tight junctions (TJs), forming c |
| concept | concepts/structural-mechanisms/common-drug-binding-site-atp-synthase-c-ring/ | Common Drug-Binding Site on ATP Synthase c-Ring | Concept: common-drug-binding-site-atp-synthase-c-ring |
| concept | concepts/structural-mechanisms/conformational-change/ | Conformational Change | Conformational changes are structural rearrangements within a protein that enabl |
| concept | concepts/structural-mechanisms/conformational-dynamics-mppases/ | Conformational Dynamics in M-PPases | M-PPases (membrane-bound H+-pumping pyrophosphatases) undergo large-scale confor |
| concept | concepts/structural-mechanisms/cork-in-bottle-occlusion/ | Cork-in-Bottle Occlusion | Cork-in-bottle occlusion is a mechanism of ion channel block in which a bound pr |
| concept | concepts/structural-mechanisms/cpe-induced-tight-junction-disassembly/ | CpE-Induced Tight Junction Disassembly | Clostridium perfringens enterotoxin (CpE) causes tight junction (TJ) disassembly |
| concept | concepts/structural-mechanisms/crd-cholesterol-binding-site-smo/ | CRD Cholesterol Binding Site of Smoothened | The CRD cholesterol binding site is a shallow groove on the surface of the cyste |
| concept | concepts/structural-mechanisms/cross-protomer-interaction-proteorhodopsin/ | Cross-Protomer Interactions in Proteorhodopsin Oligomers | Proteorhodopsins (PRs) form oligomeric assemblies (hexamers or pentamers) in whi |
| concept | concepts/structural-mechanisms/cupin-fold/ | Cupin Fold | The cupin fold is a structural motif found in a large superfamily of proteins ch |
| concept | concepts/structural-mechanisms/de-novo-design-transmembrane-pores/ | De Novo Design of Transmembrane Pores | De novo design of transmembrane pores involves the computational design and
| concept | concepts/structural-mechanisms/deep-7tm-sterol-binding-site/ | Deep 7TM Sterol-Binding Site of Smoothened | The deep 7TM sterol-binding site is a cholesterol-binding pocket located deep wi |
| concept | concepts/structural-mechanisms/domain-swapping/ | Three-Dimensional Domain Swapping | Concept: domain-swapping |
| concept | concepts/structural-mechanisms/dual-topology-architecture/ | Dual-Topology Membrane Protein Architecture | Dual-topology membrane protein architecture refers to the assembly of a function |
| concept | concepts/structural-mechanisms/embedded-lipid-in-binding-cavity/ | Embedded Lipid in the Binding Cavity | The presence of an embedded lipid within the substrate-binding cavity of a
| concept | concepts/structural-mechanisms/engineered-disulfide-bridge-trapping/ | Engineered Disulfide Bridge Conformational Trapping | Engineered disulfide bridge conformational trapping is a protein engineering str |
| concept | concepts/structural-mechanisms/entropic-spring-mechanism/ | Entropic Spring Mechanism in Tc Toxin Injection | The entropic spring mechanism describes how the linker connecting the shell and  |
| concept | concepts/structural-mechanisms/gated-pore-mechanism/ | Gated-Pore Mechanism | The gated-pore mechanism is an alternating access transport mode in which a tran |
| concept | concepts/structural-mechanisms/grana-stacking-mechanism/ | Grana Stacking Mechanism | Concept: grana-stacking-mechanism |
| concept | concepts/structural-mechanisms/gt-a-fold/ | GT-A Fold (Glycosyltransferase A Fold) | Concept: gt-a-fold |
| concept | concepts/structural-mechanisms/gxxxg-motif/ | GXXXG Motif (Helix Packing Motif) | The GXXXG motif is a helix-helix packing motif commonly found in transmembrane p |
| concept | concepts/structural-mechanisms/heliorhodopsin-schiff-base-cavity/ | Heliorhodopsin Schiff Base Cavity | The Schiff base cavity (SBC) is a large hydrophilic cavity located in the cytopl |
| concept | concepts/structural-mechanisms/helix-pi-bulge/ | Helix Pi-Bulge in Membrane Proteins | A pi-bulge is a local disruption of the alpha-helical hydrogen-bonding pattern w |
| concept | concepts/structural-mechanisms/horizontal-helix-spring-mechanism/ | Horizontal Helix Spring Mechanism | The horizontal helix spring mechanism is a structural mechanism discovered in th |
| concept | concepts/structural-mechanisms/interdigitated-inverted-topology-repeat/ | Interdigitated Inverted Topology Repeat (IITR) | The interdigitated inverted topology repeat (IITR) is a protein fold in which tw |
| concept | concepts/structural-mechanisms/intramolecular-salt-bridge/ | Intramolecular Salt Bridge | Concept: intramolecular-salt-bridge |
| concept | concepts/structural-mechanisms/isoprenoid-quinone-in-atp-synthase-c-ring/ | Isoprenoid Quinones inside the ATP Synthase c-Ring Pore | The hypothesis that isoprenoid quinones (plastoquinone in chloroplasts,
| concept | concepts/structural-mechanisms/large-domain-motion-in-p-type-atpases/ | Large Domain Motion in P-type ATPases | The cytoplasmic headpiece consists of three domains (A, N, and P) that undergo
| concept | concepts/structural-mechanisms/lipid-asymmetry/ | Membrane Lipid Asymmetry | Membrane lipid asymmetry refers to the non-random distribution of lipids between |
| concept | concepts/structural-mechanisms/low-barrier-hydrogen-bond/ | Low-Barrier Hydrogen Bond | A low-barrier hydrogen bond (LBHB) is a very short, strong hydrogen bond (typica |
| concept | concepts/structural-mechanisms/mcu-dimer-of-dimers-architecture/ | MCU Dimer-of-Dimers Architecture | The mitochondrial calcium uniporter (MCU) assembles as a tetrameric channel with |
| concept | concepts/structural-mechanisms/membrane-protein-insertase-substrate-exit-gate/ | YidC Substrate Exit Gate and Helical Bundle Rearrangement | The [YidC/Oxa1/Alb3 Family](/xray-mp-wiki/concepts/protein-families/yidc-oxa1-al |
| concept | concepts/structural-mechanisms/membrane-recognition-helix/ | Membrane Recognition Helix | A membrane recognition helix is an amphipathic alpha-helix that lies on the memb |
| concept | concepts/structural-mechanisms/mir-domain/ | MIR Domain (Mannosyltransferase, IP3R, RyR) | The MIR domain (Mannosyltransferase, IP3R, and RyR) is a structural domain found |
| concept | concepts/structural-mechanisms/motif-a-mfs/ | MFS Motif A and Charge-Helix Dipole Interactions | Motif A is a highly conserved sequence motif (GxxxD rxGR kp) found in most MFS
| concept | concepts/structural-mechanisms/n-terminus/ | N-Terminus (N-Terminal Domain) | The N-terminus of a protein is the start of the polypeptide chain terminating in |
| concept | concepts/structural-mechanisms/narghi-quinol-binding-site/ | NarGHI Quinol Binding Site | The quinol binding site (Q-site) of Escherichia coli nitrate reductase A (NarGHI |
| concept | concepts/structural-mechanisms/non-crystallographic-symmetry/ | Non-Crystallographic Symmetry (NCS) | Non-crystallographic symmetry (NCS) refers to symmetry relationships between mol |
| concept | concepts/structural-mechanisms/npc1-c-luminal-domain/ | NPC1-C Luminal Domain | NPC1-C is the C-terminal luminal domain (also called domain C or CTD-like domain |
| concept | concepts/structural-mechanisms/npxxy-motif/ | NPxxY Motif | The NPxxY motif is a conserved sequence motif (Asn-Pro-Xaa-Xaa-Tyr) found in tra |
| concept | concepts/structural-mechanisms/peptide-binding-pocket/ | PepT_So2 Substrate-Binding Pockets (P1, P2, P3) | The substrate-binding site of PepT_So2 (a proton-dependent oligopeptide transpor |
| concept | concepts/structural-mechanisms/pilz-domain/ | PilZ Domain (c-di-GMP Binding Domain) | Concept: pilz-domain |
| concept | concepts/structural-mechanisms/pore-forming-toxins/ | Pore-Forming Toxins | Pore-forming toxins (PFTs) are a large class of bacterial virulence factors that |
| concept | concepts/structural-mechanisms/positive-allosteric-modulation/ | Positive Allosteric Modulation | Positive allosteric modulators (PAMs) are small molecules that bind to an allost |
| concept | concepts/structural-mechanisms/proton-locked-conformation/ | Proton-Locked Conformation | The proton-locked conformation is a stable structural state of the conserved glu |
| concept | concepts/structural-mechanisms/pz-pocket-pot-inhibition/ | PZ Pocket: Inhibitor-Induced Binding Pocket in POTs | The PZ pocket is a previously undescribed mostly hydrophobic pocket in proton-de |
| concept | concepts/structural-mechanisms/rck-domain-activation-mechanism/ | RCK Domain Activation Mechanism | The RCK (Regulator of K+ conductance) domain activation mechanism describes how  |
| concept | concepts/structural-mechanisms/retinal-chromophore-conformation/ | Retinal Chromophore Conformation | [Retinal](/xray-mp-wiki/reagents/ligands/retinal/) chromophore conformation in [ |
| concept | concepts/structural-mechanisms/right-handed-coiled-coil-architecture/ | Right-Handed Coiled-Coil Architecture in Rotary ATPases | The peripheral stalk of rotary ATPases adopts an unusual right-handed coiled-coi |
| concept | concepts/structural-mechanisms/rocker-switch-mechanism/ | Rocker-Switch Mechanism | The rocker-switch mechanism is an alternating access transport mode in which two |
| concept | concepts/structural-mechanisms/rocking-bundle-mechanism/ | Rocking-Bundle Mechanism | The rocking-bundle mechanism is a transport mechanism in which a transporter und |
| concept | concepts/structural-mechanisms/s4-s5-linker-interaction-motif/ | S4-S5 Linker Interaction Motif | The S4-S5 linker interaction motif is a three-way structural interaction in volt |
| concept | concepts/structural-mechanisms/sequential-allosteric-regulation/ | Sequential Allosteric Regulation | Concept: sequential-allosteric-regulation |
| concept | concepts/structural-mechanisms/slc6-substrate-recognition-gmg-motif/ | SLC6 Substrate Recognition by the GMG Motif | The (G/A/C)PheG motif (GMG in [MhsT Multi-Hydrophobic Amino Acid Transporter fro |
| concept | concepts/structural-mechanisms/sliding-helix-mechanism/ | Sliding Helix Mechanism | The sliding helix mechanism is a model for voltage-dependent gating in voltage-g |
| concept | concepts/structural-mechanisms/sn2-like-displacement-mechanism/ | SN2-Like Displacement Mechanism in Phosphotransferases | Concept: sn2-like-displacement-mechanism |
| concept | concepts/structural-mechanisms/snare-complex/ | SNARE Complex | The SNARE (Soluble N-ethylmaleimide-sensitive factor Attachment protein REceptor |
| concept | concepts/structural-mechanisms/snare-core-complex-assembly/ | SNARE Core Complex Assembly and Layer Architecture | SNARE (SNAP Receptor) core complexes are four-helix bundles that mediate membran |
| concept | concepts/structural-mechanisms/symmetry-mismatch-rotary-motor/ | Symmetry Mismatch in Rotary Molecular Motors | Symmetry mismatch between rotor and stator components is a recurring design prin |
| concept | concepts/structural-mechanisms/transmembrane-allosteric-binding-site-acrb/ | Transmembrane Domain Allosteric Binding Pocket (TMD-BP) of AcrB | The transmembrane domain-binding pocket (TMD-BP) of the AcrB RND multidrug efflu |
| concept | concepts/structural-mechanisms/type-i-crystal-packing/ | Type I Crystal Packing | Type I crystal packing is a crystallographic arrangement characteristic of membr |
| concept | concepts/structural-mechanisms/water-networks-membrane-protein-oligomerization/ | Water Networks in Membrane Protein Oligomerization | Water molecules at the interface between protein subunits play critical roles in |
| concept | concepts/transport-mechanisms/2-hydroxycarboxylate-transporter-family/ | 2-Hydroxycarboxylate Transporter (2-HCT) Family | The 2-hydroxycarboxylate transporter (2-HCT) family (TC 2.A.24) comprises second |
| concept | concepts/transport-mechanisms/abc-transporter-allosteric-regulation/ | ABC Transporter Allosteric Regulation | ABC transporters can be allosterically regulated through regulatory domains fuse |
| concept | concepts/transport-mechanisms/abc-transporter-family/ | ABC Transporter Family | The ATP-binding cassette (ABC) transporter superfamily comprises a large group o |
| concept | concepts/transport-mechanisms/abc-transporter-outward-occluded-mechanism/ | ABC Transporter Outward-Occluded Mechanism | The outward-occluded conformation of ABC exporters represents an intermediate
| concept | concepts/transport-mechanisms/abc-transporter-substrate-specificity/ | ABC Transporter Substrate Specificity | Substrate specificity in ABC transporters is not determined solely by
| concept | concepts/transport-mechanisms/abgt-family/ | AbgT Family of Transporters | The AbgT family is a large family of approximately 13,000 putative membrane tran |
| concept | concepts/transport-mechanisms/acetate-uptake-transporter-family/ | Acetate Uptake Transporter (AceTr) Family | The acetate uptake transporter (AceTr) family (TC 2.A.96) comprises bacterial an |
| concept | concepts/transport-mechanisms/ag-sf-coupling/ | Activation Gate–Selectivity Filter (AG–SF) Coupling | AG–SF coupling is the allosteric communication mechanism between the activation  |
| concept | concepts/transport-mechanisms/allosteric-site-in-nss-transporters/ | Allosteric Site in NSS Transporters | Concept: allosteric-site-in-nss-transporters |
| concept | concepts/transport-mechanisms/alternating-access-mechanism/ | Alternating Access Mechanism | The alternating access mechanism is a fundamental transport mechanism
| concept | concepts/transport-mechanisms/alternating-access-sodium-transport/ | Alternating Access Model for Light-Driven Sodium Transport | The alternating access model for light-driven sodium transport describes how Kro |
| concept | concepts/transport-mechanisms/alternating-ion-bound-configurations/ | Alternating Ion-Bound Configurations in K+ Channel Selectivity Filters | The alternating ion-bound configurations model proposes that a K+ channel's sele |
| concept | concepts/transport-mechanisms/amate-1-subfamily/ | aMATE-1 Subfamily — Archaeal MATE Transporters | The aMATE-1 (archaeal MATE-1) subfamily is a newly identified clade of the multi |
| concept | concepts/transport-mechanisms/anion-channel-gating/ | Anion Channel Gating via Phenylalanine Gate | Anion channel gating via a conserved phenylalanine gate is a mechanism of ion ch |
| concept | concepts/transport-mechanisms/anion-pi-interaction/ | Anion-&#x3C0; Interaction in Ion Transport | Anion-&#x3C0; interactions are non-covalent interactions between an anion
| concept | concepts/transport-mechanisms/antibiotic-efflux-pump/ | Antibiotic Efflux Pumps | Antibiotic efflux pumps are membrane transporters that export toxic compounds, i |
| concept | concepts/transport-mechanisms/apc-superfamily/ | APC Superfamily (Amino Acid-Polyamine-Organocation Transporter Family) | The APC (amino acid-polyamine-organocation) superfamily comprises membrane trans |
| concept | concepts/transport-mechanisms/aquaporin/ | Aquaporin Family | Concept: aquaporin |
| concept | concepts/transport-mechanisms/arginine-oscillation-mechanism/ | Arginine Oscillation Mechanism in LeuT-Type Transporters | Concept: arginine-oscillation-mechanism |
| concept | concepts/transport-mechanisms/autoinhibitory-domains/ | Autoinhibitory Domains in Ion Pumps | Concept: autoinhibitory-domains |
| concept | concepts/transport-mechanisms/bacterial-pump-oligomerization-structural-determinants/ | Bacterial Pump Oligomerization Classification by Structural Determinants | A classification system for bacterial light-driven pumps based on the
| concept | concepts/transport-mechanisms/ball-and-chain-model/ | Ball-and-Chain Model for SLC38A9 | The ball-and-chain model describes a conformational regulation mechanism in SLC3 |
| concept | concepts/transport-mechanisms/barbiturate-binding-mechanism/ | Barbiturate Binding Mechanism in Pentameric Ligand-Gated Ion Channels | Barbiturates are sedative-hypnotic drugs that modulate pentameric ligand-gated i |
| concept | concepts/transport-mechanisms/bcct-family/ | BCCT Family (Betaine/Carnitine/Choline Transporter Family) | The BCCT (Betaine/Carnitine/Choline Transporter) family comprises secondary acti |
| concept | concepts/transport-mechanisms/bcs1-folded-protein-translocation/ | Bcs1 Folded Protein Translocation Mechanism | Bcs1 is a mitochondrial AAA+ ATPase that translocates folded proteins across the |
| concept | concepts/transport-mechanisms/biogenic-amine-transporters/ | Biogenic Amine Transporters | Biogenic amine transporters (BATs) are integral-membrane symporters that clear n |
| concept | concepts/transport-mechanisms/caca-superfamily/ | Ca2+:Cation Antiporter (CaCA) Superfamily | The Ca2+:cation (CaCA) superfamily is a large and ancient family of integral mem |
| concept | concepts/transport-mechanisms/camera-iris-gating/ | Camera Iris Gating | Camera iris gating describes a mechanism of channel opening where transmembrane  |
| concept | concepts/transport-mechanisms/cardiolipin-transport/ | Cardiolipin Transport in Gram-Negative Bacteria | [Cardiolipin](/xray-mp-wiki/reagents/lipids/cardiolipin/) (CL) transport in Gram |
| concept | concepts/transport-mechanisms/channel-4/ | Channel 4 (CH4) - PN2/PC1 Drug Transport Pathway in AcrB | Channel 4 (CH4) is a proposed drug transport pathway in the AcrB multidrug efflu |
| concept | concepts/transport-mechanisms/channel-like-mechanism/ | Channel-like Mechanism in Membrane Transport | Concept: channel-like-mechanism |
| concept | concepts/transport-mechanisms/channelrhodopsin-photocycle/ | Channelrhodopsin Photocycle | Concept: channelrhodopsin-photocycle |
| concept | concepts/transport-mechanisms/cl1-channel/ | Cl1 Proton Channel of Photosystem II | The Cl1 channel is a proton release pathway in Photosystem II (PSII) that connec |
| concept | concepts/transport-mechanisms/clc-chloride-channel-glutamate-gating/ | CLC Chloride Channel Glutamate Gating | CLC chloride channel gating is mediated by a conserved glutamate residue (E148 i |
| concept | concepts/transport-mechanisms/clc-proton-transport-mechanism/ | CLC Cl-/H+ Exchange Transport Mechanism | CLC Cl-/H+ exchange transporters couple the downhill movement of chloride ions ( |
| concept | concepts/transport-mechanisms/clc-two-gate-mechanism/ | CLC Two-Gate Transport Mechanism | The CLC two-gate transport mechanism describes how CLC-type Cl-/H+ exchangers co |
| concept | concepts/transport-mechanisms/clc-windmill-antiport-mechanism/ | CLC Windmill Antiport Mechanism | The windmill mechanism is a proposed model for CLCF-type F-/H+
| concept | concepts/transport-mechanisms/conformational-asymmetry-abc-transporters/ | Conformational Asymmetry in ABC Transporters | Conformational asymmetry in ABC transporters refers to the observation that the  |
| concept | concepts/transport-mechanisms/conformational-coupling-gating/ | Conformational Coupling Between Activation Gate and Selectivity Filter | Conformational coupling between the activation gate and selectivity filter is a  |
| concept | concepts/transport-mechanisms/conformational-dynamics-mfs/ | Conformational Dynamics in MFS Transporters | [MFS](/xray-mp-wiki/concepts/protein-families/mfs-transporter/) transporters exh |
| concept | concepts/transport-mechanisms/cora-mg-transporter/ | CorA Mg2+ Transporter | Concept: cora-mg-transporter |
| concept | concepts/transport-mechanisms/cora-mrs2-alr1-superfamily/ | CorA-Mrs2-Alr1 Superfamily of Mg2+ Channels | Concept: cora-mrs2-alr1-superfamily |
| concept | concepts/transport-mechanisms/dass-family/ | Divalent Anion/Na+ Symporter (DASS) Family | The Divalent Anion/Na+ Symporter (DASS) family (TC 2.A.47) is a large family
| concept | concepts/transport-mechanisms/dmt-superfamily/ | DMT Superfamily (Drug/Metabolite Transporter Superfamily) | The drug/metabolite transporter (DMT) superfamily is a large group of membrane t |
| concept | concepts/transport-mechanisms/dual-drug-binding-sites-mfs/ | Dual Drug-Binding Sites in MFS Multidrug Transporters | X-ray structures of the MdfA variant I239T/G354E revealed that this multidrug tr |
| concept | concepts/transport-mechanisms/dual-mode-inhibition-abc-transporters/ | Dual-Mode Inhibition of ABC Transporters | Dual-mode inhibition refers to a mechanism where a single small-molecule inhibit |
| concept | concepts/transport-mechanisms/dual-topology-channels/ | Dual-Topology Channels | Dual-topology channels are membrane protein complexes in which the subunits that |
| concept | concepts/transport-mechanisms/ecf-transporter-family/ | ECF (Energy Coupling Factor) Transporter Family | The Energy Coupling Factor (ECF) transporter family is a specialized class of
| concept | concepts/transport-mechanisms/ecf-transporter/ | ECF Transporter (Energy-Coupling Factor Transporter) | Energy-coupling factor (ECF) transporters are a unique family of membrane transp |
| concept | concepts/transport-mechanisms/electrostatic-gating-sodium-pump/ | Electrostatic Gating in Light-Driven Sodium Pumps | The electrostatic gating mechanism describes how light-driven sodium pumps such  |
| concept | concepts/transport-mechanisms/elevator-mechanism/ | Elevator Mechanism | Concept: elevator-mechanism |
| concept | concepts/transport-mechanisms/esx-1-secretion-system/ | ESX-1 Secretion System | The ESX-1 secretion system is a type VII protein secretion system in Mycobacteri |
| concept | concepts/transport-mechanisms/extended-selectivity-filter/ | Extended Selectivity Filter | The extended selectivity filter is a five-position motif in the pore of
| concept | concepts/transport-mechanisms/fluc-family/ | Fluc Family of Fluoride Ion Channels | The Fluc family comprises F- specific ion channels that protect prokaryotes and  |
| concept | concepts/transport-mechanisms/fnt-family/ | FNT Family (Formate/Nitrite Transporter Family) | The FNT (formate/nitrite transporter) family comprises pentameric membrane chann |
| concept | concepts/transport-mechanisms/functionally-rotating-mechanism/ | Functionally Rotating Mechanism in Multidrug Transporters | The functionally rotating mechanism is a drug export mechanism proposed for the  |
| concept | concepts/transport-mechanisms/gaba-transporters-gats/ | GABA Transporters (GATs) | GABA transporters (GATs) are members of the neurotransmitter/sodium symporter (N |
| concept | concepts/transport-mechanisms/gap-junction-voltage-gating/ | Gap Junction Voltage-Dependent Gating (Vj Gating) | Gap junction channels exhibit voltage-dependent gating in response to the transj |
| concept | concepts/transport-mechanisms/gas-conducting-aquaporins/ | Gas-Conducting Aquaporins | Gas-conducting aquaporins are a proposed subclass of the aquaporin superfamily
| concept | concepts/transport-mechanisms/gas-selectivity-filter/ | GAS Selectivity Filter | The GAS (Gly-Ala-Ser) selectivity filter is the ion selectivity determinant in a |
| concept | concepts/transport-mechanisms/gating-charge-transfer-center/ | Gating Charge Transfer Center in Voltage Sensors | The gating charge transfer center is a conserved structural feature in voltage-s |
| concept | concepts/transport-mechanisms/gating-modifier-toxin-binding/ | Gating Modifier Toxin Binding Mechanism | Concept: gating-modifier-toxin-binding |
| concept | concepts/transport-mechanisms/gating-pore-current/ | Gating Pore Current (Omega Current) | The gating pore current (also called omega current) is a pathological ionic curr |
| concept | concepts/transport-mechanisms/gating-ring/ | Gating Ring (RCK Domain Assembly) | A gating ring is a large tetrameric or octameric assembly of RCK (Regulator of C |
| concept | concepts/transport-mechanisms/glucose-h-symport-mechanism/ | Glucose/H+ Symport Mechanism | The glucose/H+ symport mechanism describes how members of the
| concept | concepts/transport-mechanisms/gluex-conformational-states-clc/ | Gluex Conformational States in CLC Transport Cycle | The critical glutamate residue (Gluex) in CLC Cl-/H+ antiporters adopts multiple |
| concept | concepts/transport-mechanisms/glutamate-transporter-family/ | Glutamate Transporter Family (SLC1/EAAT) | The glutamate transporter family (SLC1 in humans, also known as excitatory
| concept | concepts/transport-mechanisms/glycine-gating-hinge/ | Glycine-Gating Hinge | The glycine-gating hinge is a conserved [Glycine](/xray-mp-wiki/reagents/buffers |
| concept | concepts/transport-mechanisms/gpcr-lateral-ligand-entry-channel/ | GPCR Lateral Ligand Entry Channel | Some G-protein-coupled receptors (GPCRs), particularly those that bind lipophili |
| concept | concepts/transport-mechanisms/h-plus-countertransport-p-type-atpases/ | H⁺ Countertransport in P-type ATPases | H⁺ countertransport in P-type ATPases refers to the coupled movement of
| concept | concepts/transport-mechanisms/helix-shift-mechanism/ | Helix Shift Mechanism for Carboxylate Drug Transport | The helix shift mechanism describes how carboxylate drugs are actively transport |
| concept | concepts/transport-mechanisms/hme-rnd-efflux-pump/ | HME-RND Efflux Pump (Heavy-Metal Efflux RND) | The heavy-metal efflux resistance-nodulation-cell division (HME-RND) subfamily c |
| concept | concepts/transport-mechanisms/hp1-hp2-gating-mechanism/ | HP1-HP2 Gating Mechanism in Glutamate Transporters | The HP1-HP2 gating mechanism describes how glutamate transporters control altern |
| concept | concepts/transport-mechanisms/hydrophobic-gating/ | Hydrophobic Gating (Vapor Lock Mechanism) | Hydrophobic gating, also known as the "vapor lock" mechanism, is a principle by  |
| concept | concepts/transport-mechanisms/inward-facing-conformation/ | Inward-Facing Conformation of ABC Transporters | The inward-facing conformation is a structural state of ABC transporters in whic |
| concept | concepts/transport-mechanisms/inward-facing-occluded-mfs-state/ | Inward Facing Occluded State in MFS Transporters | The inward facing occluded state is a conformational intermediate in the transpo |
| concept | concepts/transport-mechanisms/inward-rectification/ | Inward Rectification in Potassium Channels | Inward rectification is the property of certain potassium channels (Kir channels |
| concept | concepts/transport-mechanisms/ion-release-pathway/ | Ion-Release Pathway in Copper-Transporting P-type ATPases | The ion-release pathway in copper-transporting P-type ATPases (P_IB ATPases) is  |
| concept | concepts/transport-mechanisms/ionic-locks-mfs/ | Ionic Locks in MFS Transporters | Concept: ionic-locks-mfs |
| concept | concepts/transport-mechanisms/knock-off-mechanism/ | Knock-off Mechanism of Ion Permeation | The knock-off mechanism is a model of ion permeation through selectivity filters |
| concept | concepts/transport-mechanisms/lateral-gating-mechanism/ | Lateral Gating Mechanism in Rhomboid Proteases | The lateral gating mechanism is a feature of rhomboid intramembrane proteases th |
| concept | concepts/transport-mechanisms/leu25-gatekeeper/ | Leu25 Gatekeeper Mechanism in NSS Transporters | The Leu25 gatekeeper is a conserved mechanism in the NSS (neurotransmitter:sodiu |
| concept | concepts/transport-mechanisms/lid-domain/ | Lid Domain in Sugar Transport Proteins (STPs) | The Lid domain is a conserved structural feature of Sugar Transport Proteins
| concept | concepts/transport-mechanisms/lipid-mediated-gating-of-kir-channels/ | Lipid-Mediated Gating of Kir Potassium Channels | Kir (inwardly rectifying) potassium channels conduct K+ through a narrow pore th |
| concept | concepts/transport-mechanisms/lumenal-gating-mechanism/ | Lumenal Gating Mechanism in P-type ATPases | The lumenal gating mechanism describes how P-type ATPases control ion release to |
| concept | concepts/transport-mechanisms/m-ppase-ion-pumping-mechanism/ | M-PPase Ion Pumping Mechanism | Membrane-integral pyrophosphatases (M-PPases) are ion pumps that couple the
| concept | concepts/transport-mechanisms/m2-conformational-equilibrium/ | M2 Proton Channel Conformational Equilibrium | The [Influenza A M2 Proton Channel](/xray-mp-wiki/proteins/other-ion-channels/in |
| concept | concepts/transport-mechanisms/malodour-precursor-recognition-pot/ | Malodour Precursor Recognition by POT Transporters | The crystal structure of PepT_Sh bound to S-Cys-Gly-3M3SH (PDB 6EXS, 2.5 A) reve |
| concept | concepts/transport-mechanisms/mate-transporter-family/ | MATE Transporter Family | Concept: mate-transporter-family |
| concept | concepts/transport-mechanisms/mechanosensitive-gating/ | Mechanosensitive Gating in Ion Channels | Mechanosensitive gating is a mechanism by which ion channels open or close in re |
| concept | concepts/transport-mechanisms/methionine-mediated-metal-transport/ | Methionine-Mediated Metal Transport | Methionine-mediated metal transport is a mechanism where methionine residues, ei |
| concept | concepts/transport-mechanisms/mit-superfamily/ | Metal Ion Transporter (MIT) Superfamily | The Metal Ion Transporter (MIT) superfamily includes transporters for Mg2+, Co2+ |
| concept | concepts/transport-mechanisms/mmpl3-lipid-transport-mechanism/ | MmpL3 Lipid Transport Mechanism | [MmpL3 from Mycobacterium smegmatis](/xray-mp-wiki/proteins/abc-transporters/mmp |
| concept | concepts/transport-mechanisms/modal-gating-in-k-channels/ | Modal Gating in K+ Channels | Modal gating is a phenomenon in which ion channels switch abruptly between perio |
| concept | concepts/transport-mechanisms/mop-transporter-superfamily/ | MOP Transporter Superfamily | The multidrug/oligosaccharidyl-lipid/polysaccharide (MOP) exporter superfamily i |
| concept | concepts/transport-mechanisms/mscl-gating-mechanism/ | MscL Gating Mechanism (Mechanosensitive Channel of Large Conductance) | Concept: mscl-gating-mechanism |
| concept | concepts/transport-mechanisms/mtrcde-tripartite-efflux-pump/ | MtrCDE Tripartite Multidrug Efflux Pump | The MtrCDE tripartite multidrug efflux pump from Neisseria gonorrhoeae is a memb |
| concept | concepts/transport-mechanisms/ncs1-family/ | Nucleobase-Cation-Symport-1 (NCS1) Family | The Nucleobase-Cation-Symport-1 (NCS1) family is a group of membrane transport p |
| concept | concepts/transport-mechanisms/nitrate-nitrite-antiport-mechanism/ | Nitrate/Nitrite Antiport Mechanism | The nitrate/nitrite antiport mechanism is the transport mechanism used by NNP fa |
| concept | concepts/transport-mechanisms/nss-family/ | Neurotransmitter/Sodium Symporter (NSS) Family | The NSS (neurotransmitter/sodium symporter) family is a major group of secondary |
| concept | concepts/transport-mechanisms/ntq-motif/ | NTQ Motif in Chloride Pumping Rhodopsins | The NTQ motif (Asn98-Thr102-Gln109) is a conserved amino acid sequence
| concept | concepts/transport-mechanisms/o1-channel/ | O1 Water Channel of Photosystem II | The O1 channel is a water intake pathway in Photosystem II (PSII) that connects  |
| concept | concepts/transport-mechanisms/orthosteric-allosteric-dual-inhibition/ | Orthosteric–Allosteric Dual Inhibition of Transporters | Orthosteric–allosteric dual inhibition is a paradigm-shifting drug design strate |
| concept | concepts/transport-mechanisms/outward-facing-conformation/ | Outward-Facing Conformation of ABC Transporters | The outward-facing conformation is a structural state of ABC transporters in whi |
| concept | concepts/transport-mechanisms/oxygen-ladder-selectivity-filter/ | Oxygen Ladder in Selectivity Filters | Concept: oxygen-ladder-selectivity-filter |
| concept | concepts/transport-mechanisms/periplasmic-drug-binding-site-rnd/ | Periplasmic Drug-Binding Site in RND Efflux Pumps | The periplasmic drug-binding site of [RND Efflux Pumps](/xray-mp-wiki/concepts/t |
| concept | concepts/transport-mechanisms/peristaltic-pump-mechanism/ | Peristaltic Pump Mechanism of RND Transporters | Concept: peristaltic-pump-mechanism |
| concept | concepts/transport-mechanisms/ph-dependent-gating/ | pH-Dependent Gating in Membrane Proteins | pH-dependent gating is a regulatory mechanism in membrane transport proteins
| concept | concepts/transport-mechanisms/pip2-activation-of-kir-channels/ | PIP2 Activation of Inward Rectifier K+ Channels | Phosphatidylinositol 4,5-bisphosphate (PIP2) is the primary agonist for classica |
| concept | concepts/transport-mechanisms/pot-family/ | POT Family (Proton-Dependent Oligopeptide Transporters) | The POT (proton-dependent oligopeptide transporter) family is a subgroup of the  |
| concept | concepts/transport-mechanisms/potassium-counter-transport/ | Potassium Counter-Transport in P-type ATPases | Counter-transport (antiport) of K⁺ ions is a functional hallmark of certain P-ty |
| concept | concepts/transport-mechanisms/proton-pump-mechanism/ | Proton Pump Mechanism in Bacteriorhodopsin | The proton pump mechanism of bacteriorhodopsin is a light-driven ion translocati |
| concept | concepts/transport-mechanisms/proton-release-channel-archaeal-rhodopsins/ | Proton-Release Channel in Archaeal Rhodopsins | The proton-release channel is a conserved structural feature in
| concept | concepts/transport-mechanisms/proton-wire/ | Proton Wire (Chain of Hydrogen Bonds) | A proton wire (also known as a chain of hydrogen bonds, CHB, or proton conduit)  |
| concept | concepts/transport-mechanisms/pyridylpiperazine-allosteric-epis/ | Pyridylpiperazine-based Allosteric Efflux Pump Inhibitors | Pyridylpiperazine-based compounds represent a novel class of allosteric efflux p |
| concept | concepts/transport-mechanisms/rck-domain/ | RCK Domain (Regulator of Conductance of K+) | An RCK (Regulator of Conductance of K+) domain is a conserved structural module  |
| concept | concepts/transport-mechanisms/remote-coupling-mechanism/ | Remote Coupling Mechanism in Membrane Transporters | Remote coupling is a mechanism by which structural changes in the transmembrane  |
| concept | concepts/transport-mechanisms/rnd-efflux-pumps/ | RND Efflux Pumps | Resistance nodulation cell division (RND) transporters are a family of multidrug |
| concept | concepts/transport-mechanisms/scissor-switch-gating/ | Scissor-Switch Gating in POT Family Transporters | The scissor-switch gating mechanism is a specialized form of the alternating-acc |
| concept | concepts/transport-mechanisms/selectivity-filter/ | Ion Channel Selectivity Filter | The selectivity filter is a narrow region of the ion channel pore that determine |
| concept | concepts/transport-mechanisms/semisweet/ | SemiSWEET Transporter Family | SemiSWEETs are bacterial homologues of the eukaryotic SWEET (Sugars Will Eventua |
| concept | concepts/transport-mechanisms/side-entry-ion-conduction-pathway/ | Side-Entry Ion Conduction Pathway | The side-entry ion conduction pathway is a non-canonical mechanism for ion perme |
| concept | concepts/transport-mechanisms/sl35-family/ | SLC35 Family (Nucleotide Sugar Transporters) | Concept: sl35-family |
| concept | concepts/transport-mechanisms/slc29-family/ | SLC29 Family of Nucleoside Transporters | The SLC29 family (Equilibrative Nucleoside Transporters, ENTs) comprises
| concept | concepts/transport-mechanisms/sodium-channel-gating/ | Sodium Channel Gating and Selectivity | Concept: sodium-channel-gating |
| concept | concepts/transport-mechanisms/sodium-channel-inactivation-gating/ | Sodium Channel Inactivation Gating | Sodium channel inactivation gating in prokaryotic voltage-gated sodium channels  |
| concept | concepts/transport-mechanisms/sodium-channel-ion-permeability-selectivity/ | Sodium Channel Ion Permeability and Selectivity | Voltage-gated sodium channels (Nav) achieve high selectivity for Na+ over other  |
| concept | concepts/transport-mechanisms/sss-family/ | Sodium Solute Symporter (SSS) Family | The sodium solute symporter (SSS) family (SLC5 in humans) is a large family of s |
| concept | concepts/transport-mechanisms/substrate-binding-in-asbt-yf/ | Substrate Binding in ASBT_Yf | The apical sodium-dependent bile acid transporter (ASBT) is an SLC10 family
| concept | concepts/transport-mechanisms/substrate-induced-transition-fit/ | Substrate-Induced Transition Fit in 5+5 Inverted Repeat Transporters | The substrate-induced transition fit mechanism describes how secondary transport |
| concept | concepts/transport-mechanisms/substrate-polyspecificity-smr-transporters/ | Substrate Polyspecificity in SMR Transporters | Substrate polyspecificity — the ability to transport multiple structurally
| concept | concepts/transport-mechanisms/substrate-protonation-coupling/ | Substrate-Protonation Coupling in MFS Symporters | Substrate-protonation coupling is a fundamental mechanism in proton-driven MFS s |
| concept | concepts/transport-mechanisms/sweet-transporter/ | SWEET Transporter Family | The SWEET family of sugar transporters is a widespread class of uniporters found |
| concept | concepts/transport-mechanisms/switch-loop-gating-rnd-transporters/ | Switch-Loop Gating in RND Multidrug Transporters | The switch-loop (also called the G-loop or substrate-gating loop) is a conformat |
| concept | concepts/transport-mechanisms/tat-pathway/ | Twin-Arginine Translocation (TAT) Pathway | Concept: tat-pathway |
| concept | concepts/transport-mechanisms/tca-inhibition-mechanism/ | Tricyclic Antidepressant (TCA) Inhibition Mechanism in NSS Transporters | Tricyclic antidepressants (TCAs) such as clomipramine, desipramine, imipramine,  |
| concept | concepts/transport-mechanisms/tm6-kinking-abc-export-directionality/ | TM6 Kinking and Export Directionality in ABC Transporters | In the [NaAtm1 ABC Exporter from Novosphingobium aromaticivorans](/xray-mp-wiki/ |
| concept | concepts/transport-mechanisms/trans-inhibition-in-abc-transporters/ | Trans-Inhibition in ABC Transporters | Concept: trans-inhibition-in-abc-transporters |
| concept | concepts/transport-mechanisms/tric-channel-gating/ | TRIC Channel Gating Mechanism | The TRIC (Trimeric Intracellular Cation) channel gating mechanism is a complex,  |
| concept | concepts/transport-mechanisms/twin-histidine-motif/ | Twin-Histidine Motif in Ammonium Channels | The twin-histidine motif is a pair of conserved histidine residues that form a h |
| concept | concepts/transport-mechanisms/type-ii-abc-transporter-family/ | Type II ABC Transporter Family | Type II ABC transporters are a distinct subclass of bacterial ABC importers that |
| concept | concepts/transport-mechanisms/viral-channelrhodopsins/ | Viral Channelrhodopsins (VirChR) | Viral channelrhodopsins (VirChR1s) represent a distinct family of light-gated io |
| concept | concepts/transport-mechanisms/virtual-proton-pump/ | Virtual Proton Pump | A virtual proton pump is a transport mechanism in which the free energy of subst |
| method | methods/cell-lysis/french-press/ | French Press Cell Lysis | French press cell lysis is a high-pressure homogenization technique used to disr |
| method | methods/crystallization/2d-crystallization-detergent-dialysis/ | 2D Crystallization by Detergent Dialysis | 2D crystallization by detergent dialysis reconstitutes detergent-solubilized mem |
| method | methods/crystallization/batch-crystallization-free-interface-diffusion/ | Batch Crystallization with Free Interface Diffusion | Batch crystallization with free interface diffusion is a membrane protein crysta |
| method | methods/crystallization/bicelle-crystallization/ | Bicelle Crystallization for Membrane Proteins | Bicelle crystallization uses a lipid-detergent mixture (typically DMPC/CHAPSO) t |
| method | methods/crystallization/hanging-drop-vapor-diffusion/ | Hanging-Drop Vapor Diffusion | Hanging-drop vapor diffusion is a widely used protein crystallization technique  |
| method | methods/crystallization/hilide-crystallization/ | HiLiDe Crystallization | HiLiDe (Hydrophobic Interaction-Driven) crystallization is a membrane protein cr |
| method | methods/crystallization/imisx-in-situ-crystallization/ | IMISX In-Situ Serial Crystallography | IMISX (in meso in situ) is a serial X-ray crystallography technique that combine |
| method | methods/crystallization/lipidic-cubic-phase/ | Lipidic Cubic Phase Crystallization | Lipidic cubic phase (LCP) crystallization, also known as the in meso method, is  |
| method | methods/crystallization/lipidic-sponge-phase-crystallization/ | Lipidic Sponge Phase Crystallization | Lipidic sponge phase (LSP) crystallization is a variant of lipidic cubic phase ( |
| method | methods/crystallization/microbatch-crystallization-under-oil/ | Microbatch Crystallization Under Oil | Microbatch crystallization under oil is a crystallization method where protein a |
| method | methods/crystallization/on-chip-crystallization/ | On-Chip Crystallization for Serial Crystallography | On-chip crystallization is a method for growing protein crystals directly on mic |
| method | methods/crystallization/sitting-drop-vapor-diffusion/ | Sitting-Drop Vapor Diffusion | Sitting-drop vapor diffusion is a widely used protein crystallization technique  |
| method | methods/crystallization/vapor-diffusion/ | Vapor Diffusion Crystallization | Vapor diffusion is the most widely used method for protein crystallization. A dr |
| method | methods/expression-systems/baculovirus-expression-system/ | Baculovirus Expression System in Sf9 Cells | The baculovirus expression system using Spodoptera frugiperda (Sf9) insect cells |
| method | methods/expression-systems/cell-free-protein-synthesis/ | Cell-Free Protein Synthesis for Membrane Proteins | Cell-free protein synthesis systems can be supplemented with both lipid and dete |
| method | methods/expression-systems/iptg-induction/ | IPTG Induction of Protein Expression | IPTG (isopropyl-beta-D-thiogalactopyranoside) is a molecular mimic of allolactos |
| method | methods/expression-systems/lexsy-expression-system/ | LEXSY Leishmania tarentolae Expression System | The LEXSY (Leishmania Expression System) is a eukaryotic protein expression plat |
| method | methods/expression-systems/pichia-pastoris/ | Pichia pastoris Expression System | Method: pichia-pastoris |
| method | methods/expression-systems/ribosome-display/ | Ribosome Display | Ribosome display is an in vitro selection technique for the isolation of
| method | methods/expression-systems/sf9-expression-system/ | Sf9 Insect Cell Expression System | The Sf9 insect cell expression system uses Spodoptera frugiperda (fall armyworm) |
| method | methods/purification/affinity-chromatography/ | Affinity Chromatography | Affinity chromatography is a purification method that separates proteins based o |
| method | methods/purification/hydroxyapatite-chromatography/ | Hydroxyapatite Chromatography | Hydroxyapatite chromatography is a separation technique that exploits the affini |
| method | methods/purification/ion-exchange-chromatography/ | Ion-Exchange Chromatography | Ion-exchange chromatography (IEX) is a purification method that separates protei |
| method | methods/purification/limited-proteolysis/ | Limited Proteolysis | Limited proteolysis is a technique where a protease is used to selectively cleav |
| method | methods/purification/size-exclusion-chromatography/ | Size-Exclusion Chromatography | Size-exclusion chromatography (SEC), also known as gel filtration, separates mol |
| method | methods/purification/ultracentrifugation/ | Ultracentrifugation | Ultracentrifugation uses high centrifugal force (100,000-500,000 x g) to separat |
| method | methods/quality-assessment/circular-dichroism-spectroscopy/ | Circular Dichroism Spectroscopy | Circular dichroism (CD) spectroscopy measures the differential absorption of lef |
| method | methods/quality-assessment/deer-spectroscopy/ | Double Electron Electron Resonance (DEER) Spectroscopy | Double electron electron resonance (DEER), also known as pulsed electron double  |
| method | methods/quality-assessment/fluorescence-size-exclusion-chromatography/ | Fluorescence Size-Exclusion Chromatography (FSEC) | Fluorescence size-exclusion chromatography (FSEC) is a high-throughput screening |
| method | methods/quality-assessment/gas-phase-unfolding/ | Gas-Phase Unfolding Analysis | Gas-phase unfolding is an ion mobility mass spectrometry (IM-MS) technique used  |
| method | methods/quality-assessment/grafix/ | GraFix (Glycerol-Glutaraldehyde Gradient Fixation) | GraFix (Glycerol-Glutaraldehyde Gradient Fixation) is a sample preparation metho |
| method | methods/quality-assessment/hdx-ms/ | Hydrogen-Deuterium Exchange Mass Spectrometry (HDX-MS) | Hydrogen-deuterium exchange mass spectrometry (HDX-MS) is a biophysical
| method | methods/quality-assessment/inside-out-patch-clamp/ | Inside-Out Patch Clamp Electrophysiology | Inside-out patch clamp electrophysiology is a variant of the patch clamp techniq |
| method | methods/quality-assessment/isothermal-titration-calorimetry/ | Isothermal Titration Calorimetry (ITC) | Isothermal titration calorimetry (ITC) directly measures the heat released or ab |
| method | methods/quality-assessment/native-mass-spectrometry/ | Native Mass Spectrometry | Native mass spectrometry (native MS) is a technique for analyzing intact macromo |
| method | methods/quality-assessment/nbd-phospholipid-scrambling-assay/ | NBD-Phospholipid Scrambling Assay | The NBD-phospholipid scrambling assay is a functional assay used to measure lipi |
| method | methods/quality-assessment/non-contact-atomic-force-microscopy/ | Non-Contact Atomic Force Microscopy (nc-AFM) with CO-Functionalized Tips | Non-contact atomic force microscopy (nc-AFM) is a scanning probe technique that  |
| method | methods/quality-assessment/proteoliposome-reconstitution/ | Proteoliposome Reconstitution | Proteoliposome reconstitution is a technique for incorporating purified membrane |
| method | methods/quality-assessment/sec-mals/ | Size Exclusion Chromatography with Multi-Angle Light Scattering (SEC-MALS) | SEC-MALS combines [Size-Exclusion Chromatography](/xray-mp-wiki/methods/purifica |
| method | methods/quality-assessment/solid-supported-membrane-electrophysiology/ | Solid-Supported Membrane Electrophysiology | Solid-supported membrane (SSM) electrophysiology is a technique for measuring
| method | methods/quality-assessment/static-light-scattering/ | Static Light Scattering | Static light scattering (SLS) is a biophysical technique used to determine the m |
| method | methods/quality-assessment/thermal-shift-assay/ | Thermal Shift Assay (Fluorescent CPM) | Thermal shift assays (also known as differential scanning fluorescence or CPM as |
| method | methods/quality-assessment/tr-fret/ | Time-Resolved Fluorescence Resonance Energy Transfer (TR-FRET) | Time-resolved fluorescence resonance energy transfer (TR-FRET) is a biophysical  |
| method | methods/quality-assessment/two-electrode-voltage-clamp/ | Two-Electrode Voltage Clamp (TEVC) | Two-electrode voltage clamp (TEVC) is an electrophysiological technique used to  |
| method | methods/solubilization/nanodisc-reconstitution/ | Nanodisc Reconstitution | Nanodisc reconstitution is a technique for embedding membrane proteins into smal |
| method | methods/structure-determination/cryo-em/ | Cryo-Electron Microscopy | Cryo-electron microscopy (cryo-EM) is a high-resolution structure determination  |
| method | methods/structure-determination/diffractive-imaging-imperfect-crystals/ | Diffractive Imaging of Imperfect Crystals | Diffractive imaging of imperfect crystals is a macromolecular structure determin |
| method | methods/structure-determination/free-energy-perturbation/ | Free Energy Perturbation | Free energy perturbation (FEP) is a computational method for calculating free en |
| method | methods/structure-determination/lcp-serial-millisecond-crystallography/ | LCP Serial Millisecond Crystallography (LCP-SMX) | LCP serial millisecond crystallography (LCP-SMX) is a serial crystallography tec |
| method | methods/structure-determination/miras/ | Multiple Isomorphous Replacement with Anomalous Scattering (MIRAS) | MIRAS (Multiple Isomorphous Replacement with Anomalous Scattering) is a crystall |
| method | methods/structure-determination/molecular-docking/ | Molecular Docking | Molecular docking is a computational method used to predict the preferred
| method | methods/structure-determination/molecular-dynamics-simulation/ | Molecular Dynamics Simulation | Molecular dynamics (MD) simulation is a computational technique for studying the |
| method | methods/structure-determination/molecular-replacement/ | Molecular Replacement | Molecular replacement is an X-ray crystallographic phasing method that uses a kn |
| method | methods/structure-determination/multi-wavelength-anomalous-diffraction/ | Multi-Wavelength Anomalous Diffraction | Multi-wavelength anomalous diffraction (MAD) is an X-ray crystallographic phasin |
| method | methods/structure-determination/normal-mode-xray-refinement/ | Normal-Mode-Based X-Ray Crystallographic Refinement | Normal-mode-based X-ray crystallographic refinement is a computational method th |
| method | methods/structure-determination/semet-sad-phasing/ | Selenomethionine Single-Wavelength Anomalous Dispersion (SeMet SAD) Phrasing | [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine/) s |
| method | methods/structure-determination/serial-femtosecond-crystallography/ | Serial Femtosecond Crystallography | Serial femtosecond crystallography (SFX) is an X-ray crystallography technique t |
| method | methods/structure-determination/single-crystal-microspectrophotometry/ | Single-Crystal Microspectrophotometry | Single-crystal microspectrophotometry is a technique for recording absorption sp |
| method | methods/structure-determination/single-wavelength-anomalous-diffraction/ | Single-Wavelength Anomalous Diffraction | Single-wavelength anomalous diffraction (SAD) is an X-ray crystallographic phasi |
| method | methods/structure-determination/solvent-contrast-modulation/ | X-ray Solvent Contrast Modulation | X-ray solvent contrast modulation is a crystallographic technique that resolves  |
| method | methods/structure-determination/time-resolved-serial-femtosecond-crystallography/ | Time-Resolved Serial Femtosecond Crystallography (TR-SFX) | Time-resolved [Serial Femtosecond Crystallography](/xray-mp-wiki/methods/structu |
| method | methods/structure-determination/time-resolved-serial-synchrotron-crystallography/ | Time-Resolved Serial Synchrotron Crystallography (TR-SMX) | Time-resolved serial synchrotron crystallography (TR-SMX) adapts injector-based  |
| method | methods/structure-determination/umbrella-sampling/ | Umbrella Sampling | Umbrella sampling (US) is an enhanced sampling molecular dynamics technique used |
| method | methods/structure-determination/xray-crystallography/ | X-ray Crystallography | X-ray crystallography is a technique for determining the atomic and molecular st |
| protein | proteins/abc-transporters/aaprtd/ | Aquifex aeolicus PrtD (AaPrtD) Type-1 Secretion System ABC Transporter | [AaPrtD](/xray-mp-wiki/proteins/aaprtd/) is the ABC transporter component of the |
| protein | proteins/abc-transporters/aawzmwzt/ | AaWzmWzt (O Antigen ABC Transporter from Aquifex aeolicus) | AaWzmWzt is an [ABC Transporter](/xray-mp-wiki/concepts/transport-mechanisms/abc |
| protein | proteins/abc-transporters/ab-macb/ | MacB ABC Transporter from Acinetobacter baumannii | MacB from Acinetobacter baumannii is an ATP-binding cassette (ABC) transporter t |
| protein | proteins/abc-transporters/abcb10/ | Human ABCB10 Mitochondrial ATP-Binding Cassette Transporter | ABCB10 is a human [ATP](/xray-mp-wiki/reagents/ligands/atp/)-binding cassette (A |
| protein | proteins/abc-transporters/abcg1/ | ABCG1 | ABCG1 is a member of the ATP-binding cassette (ABC) G subfamily of lipid transpo |
| protein | proteins/abc-transporters/abcg2/ | ABCG2 | ABCG2 (breast cancer resistance protein, BCRP) is the sole multidrug transporter |
| protein | proteins/abc-transporters/abcg5-abcg8-hetero-dimer/ | Human ABCG5/ABCG8 Sterol Transporter Heterodimer | ABCG5 and ABCG8 form an obligate heterodimer that functions as a sterol efflux t |
| protein | proteins/abc-transporters/abcg5/ | ABCG5 | ABCG5 is a member of the ATP-binding cassette (ABC) G subfamily of transporter p |
| protein | proteins/abc-transporters/abcg8/ | ABCG8 | ABCG8 is a member of the ATP-binding cassette (ABC) G subfamily of transporter p |
| protein | proteins/abc-transporters/acra/ | AcrA multidrug efflux pump periplasmic protein | AcrA is a periplasmic membrane fusion protein from Escherichia coli that partner |
| protein | proteins/abc-transporters/acrb/ | AcrB Multidrug Efflux Transporter | AcrB is the inner membrane component of the [AcrA multidrug efflux pump periplas |
| protein | proteins/abc-transporters/adeb/ | AdeB Multidrug Efflux Transporter | AdeB is a multidrug efflux transporter from the Gram-negative pathogen Acinetoba |
| protein | proteins/abc-transporters/algm1m2ss/ | AlgM1M2SS Alginate ABC Transporter | AlgM1M2SS is an [ATP](/xray-mp-wiki/reagents/ligands/atp/)-binding cassette (ABC |
| protein | proteins/abc-transporters/aq_128/ | Aq_128 (Aquifex aeolicus MATE Family Multidrug Resistance Transporter) — aMATE-1 Subfamily Prototype | Aq_128 is a multidrug and toxic compound extrusion (MATE) family transporter fro |
| protein | proteins/abc-transporters/archaeoglobus-fulgidus-modbc/ | Archaeoglobus fulgidus ModB2C2 Molybdate ABC Transporter with ModA | The molybdate/tungstate ABC transporter from Archaeoglobus fulgidus is a |
| protein | proteins/abc-transporters/art-qn2/ | Art(QN)2 ABC Amino Acid Importer from Thermoanaerobacter tengcongensis | Art(QN)2 is a homodimeric type I ABC importer from the thermophilic bacterium Th |
| protein | proteins/abc-transporters/bhuuv-t/ | Burkholderia cenocepacia Haem Importer Complex BhuUV-T | The BhuUV-T complex is a type II ATP-binding cassette (ABC) haem importer from t |
| protein | proteins/abc-transporters/bhuuv/ | Burkholderia cenocepacia Haem Importer Complex BhuUV | The BhuUV complex is the transmembrane and nucleotide-binding domain core of the |
| protein | proteins/abc-transporters/bpeb/ | BpeB Multidrug Efflux Transporter from Burkholderia pseudomallei | BpeB is a Resistance-Nodulation-Division (RND) superfamily multidrug efflux tran |
| protein | proteins/abc-transporters/bpef/ | BpeF Multidrug Efflux Transporter from Burkholderia pseudomallei | BpeF is a Resistance-Nodulation-Division (RND) superfamily multidrug efflux tran |
| protein | proteins/abc-transporters/btucd-btuf-complex/ | BtuCD-BtuF Complex (E. coli Vitamin B12 ABC Transporter) | The BtuCD-BtuF complex is the membrane-bound vitamin B12 (cyanocobalamin) ABC tr |
| protein | proteins/abc-transporters/c-elegans-p-glycoprotein/ | C. elegans P-glycoprotein (P-gp) | P-glycoprotein (P-gp) from Caenorhabditis elegans is an [ATP](/xray-mp-wiki/reag |
| protein | proteins/abc-transporters/casmate/ | CasMATE (Camelina sativa MATE Transporter) | CasMATE is a multidrug and toxic compound extrusion (MATE) family transporter fr |
| protein | proteins/abc-transporters/clbm/ | ClbM — MATE Transporter from Escherichia coli | ClbM is a MATE (Multidrug and Toxic Compound Extrusion) family transporter from  |
| protein | proteins/abc-transporters/cmabcb1/ | CmABCB1 (Homodimeric P-glycoprotein from Cyanidioschyzon merolae) | CmABCB1 is a homodimeric P-glycoprotein from the red alga Cyanidioschyzon
| protein | proteins/abc-transporters/cmeb/ | Campylobacter jejuni CmeB Multidrug Efflux Pump | CmeB is the inner membrane Resistance-Nodulation-Division (RND) multidrug efflux |
| protein | proteins/abc-transporters/cusA/ | CusA Inner Membrane Efflux Pump | CusA is the inner-membrane component of the CusABC tripartite copper/silver effl |
| protein | proteins/abc-transporters/cusB/ | CusB Membrane Fusion Protein | CusB is a periplasmic membrane fusion protein (MFP) from Escherichia coli, funct |
| protein | proteins/abc-transporters/cusC/ | CusC Outer Membrane Channel | CusC is the outer-membrane channel component of the CusABC tripartite copper/sil |
| protein | proteins/abc-transporters/cusa-efflux-pump/ | CusA Heavy-Metal Efflux RND Transporter (E. coli) | CusA is the inner-membrane transporter component of the CusCBA tripartite efflux |
| protein | proteins/abc-transporters/dinf-bh/ | DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter | DinF-BH is a multidrug and toxic compound extrusion (MATE) family transporter fr |
| protein | proteins/abc-transporters/ec-cor-a/ | Escherichia coli CorA Mg2+ Channel (Cytoplasmic Domain) | CorA from Escherichia coli is the family prototype of the CorA Mg2+ transporter  |
| protein | proteins/abc-transporters/eiiaglc/ | EIIA^Glc (Escherichia coli Enzyme IIA^Glc) | EIIA^Glc (Enzyme IIA^Glc) is a central signaling protein in the Escherichia coli |
| protein | proteins/abc-transporters/emre/ | EmrE (E. coli Small Multidrug Resistance Transporter) | EmrE is a small multidrug resistance (SMR) family proton-coupled multidrug efflu |
| protein | proteins/abc-transporters/fbpc/ | FbpC (Nucleotide-Binding Domain of the FbpABC Iron Transporter) | FbpC is the nucleotide-binding domain (NBD) of the FbpABC ferric  uptake -bindin |
| protein | proteins/abc-transporters/gdx-clo/ | Gdx-Clo SMR Transporter (Clostridales oral taxon 876) | Gdx-Clo is a small multidrug resistance (SMR) family transporter from *Clostrida |
| protein | proteins/abc-transporters/hi1470-1/ | HI1470/1 Putative Metal-Chelate-Type ABC Transporter | HI1470/1 is a putative metal-chelate-type ABC transporter from Haemophilus influ |
| protein | proteins/abc-transporters/hmuuv/ | Yersinia pestis Heme Transporter HmuUV | The HmuUV complex is the transmembrane and nucleotide-binding domain core of the |
| protein | proteins/abc-transporters/hpnn/ | HpnN Hopanoid Transporter from Burkholderia multivorans | HpnN from *Burkholderia multivorans* is a member of the hopanoid biosynthesis-as |
| protein | proteins/abc-transporters/irtab-mycobacterium-thermoresistibile/ | IrtAB ABC Exporter from Mycobacterium thermoresistibile | IrtAB is a heterodimeric ATP-binding cassette (ABC) transporter from
| protein | proteins/abc-transporters/lptb2fg-pseudomonas-aeruginosa/ | Pseudomonas aeruginosa LptB2FG LPS Extraction Complex | LptB2FG is an ATP-binding cassette (ABC) transporter complex responsible for ext |
| protein | proteins/abc-transporters/lptb2fgc-complex/ | LptB2FGC LPS Transport Complex from Enterobacter cloacae and Vibrio cholerae | The LptB2FGC complex is the inner membrane component of the lipopolysaccharide ( |
| protein | proteins/abc-transporters/macb/ | MacB ABC Transporter from Aggregatibacter actinomycetemcomitans | MacB is an ABC transporter from Aggregatibacter actinomycetemcomitans that forms |
| protein | proteins/abc-transporters/malF/ | MalF (Escherichia coli Maltose Transporter Transmembrane Subunit) | MalF is a transmembrane subunit of the Escherichia coli [Maltose](/xray-mp-wiki/ |
| protein | proteins/abc-transporters/malG/ | MalG (Escherichia coli Maltose Transporter Transmembrane Subunit) | MalG is a transmembrane subunit of the Escherichia coli [Maltose](/xray-mp-wiki/ |
| protein | proteins/abc-transporters/malK/ | MalK (Escherichia coli Maltose Transporter ATPase Subunit) | MalK is the cytoplasmic ATP-binding cassette (NBD) subunit of the Escherichia co |
| protein | proteins/abc-transporters/maltose-binding-protein/ | MBP (Escherichia coli Maltose-Binding Protein) | MBP (maltose-binding protein) is the periplasmic binding protein component of
| protein | proteins/abc-transporters/maltose-transporter-malfgk2/ | Maltose Transporter MalFGK2 (E. coli) | The maltose transporter from Escherichia coli (MalFGK2) is a prototype
| protein | proteins/abc-transporters/mamodbc/ | Methanosarcina acetivorans ModBC Molybdate/Tungstate ABC Transporter (MaModBC) | The crystal structure of Methanosarcina acetivorans ModBC (MaModBC),
| protein | proteins/abc-transporters/mcjd/ | McjD - Antibacterial Peptide ABC Exporter from Escherichia coli | McjD is an ATP-binding cassette (ABC) exporter from Escherichia coli that
| protein | proteins/abc-transporters/metni-abc-transporter/ | E. coli Methionine ABC Transporter MetNI | The MetNI complex is the high-affinity methionine ABC transporter from *Escheric |
| protein | proteins/abc-transporters/mexB/ | MexB (Pseudomonas aeruginosa multidrug exporter) | MexB is the inner-membrane component of the MexAB-OprM tripartite efflux pump in |
| protein | proteins/abc-transporters/mexY/ | MexY (Pseudomonas aeruginosa multidrug exporter) | MexY is the inner-membrane component of the MexXY-OprM tripartite efflux pump in |
| protein | proteins/abc-transporters/mexa/ | MexA multidrug efflux pump periplasmic adaptor | MexA is the periplasmic adaptor (membrane fusion protein) component of the MexAB |
| protein | proteins/abc-transporters/mexb/ | MexB Multidrug Efflux Pump | [MexB (Pseudomonas aeruginosa multidrug exporter)](/xray-mp-wiki/proteins/abc-tr |
| protein | proteins/abc-transporters/mmpL3/ | MmpL3 from Mycobacterium smegmatis | MmpL3 (Mycobacterial membrane protein Large 3) is an inner membrane](/xray-mp-wi |
| protein | proteins/abc-transporters/mouse-p-glycoprotein/ | Mouse P-glycoprotein | Mouse P-glycoprotein (P-gp; ABCB1; Mdr1a) is an ATP-binding cassette (ABC) trans |
| protein | proteins/abc-transporters/msba/ | MsbA Lipid A Flippase | MsbA is an essential ATP-binding cassette (ABC) transporter in Gram-negative bac |
| protein | proteins/abc-transporters/mtre/ | MtrE Outer Membrane Channel from Neisseria gonorrhoeae | MtrE is the outer membrane channel component of the [MtrCDE Tripartite Multidrug |
| protein | proteins/abc-transporters/murj/ | MurJ (Lipid II Flippase from E. coli and T. africanus) | MurJ is an essential integral membrane protein in Gram-negative bacteria that fl |
| protein | proteins/abc-transporters/murj/ | MurJ (Lipid II Flippase from E. coli and T. africanus) | MurJ is an essential integral membrane protein in Gram-negative bacteria that fl |
| protein | proteins/abc-transporters/murj/ | MurJ (Lipid II Flippase from E. coli and T. africanus) | MurJ is an essential integral membrane protein in Gram-negative bacteria that fl |
| protein | proteins/abc-transporters/murj/ | MurJ (Lipid II Flippase from E. coli and T. africanus) | MurJ is an essential integral membrane protein in Gram-negative bacteria that fl |
| protein | proteins/abc-transporters/murj/ | MurJ (Lipid II Flippase from E. coli and T. africanus) | MurJ is an essential integral membrane protein in Gram-negative bacteria that fl |
| protein | proteins/abc-transporters/murj/ | MurJ (Lipid II Flippase from E. coli and T. africanus) | MurJ is an essential integral membrane protein in Gram-negative bacteria that fl |
| protein | proteins/abc-transporters/murj/ | MurJ (Lipid II Flippase from E. coli and T. africanus) | MurJ is an essential integral membrane protein in Gram-negative bacteria that fl |
| protein | proteins/abc-transporters/murj/ | MurJ (Lipid II Flippase from E. coli and T. africanus) | MurJ is an essential integral membrane protein in Gram-negative bacteria that fl |
| protein | proteins/abc-transporters/murj/ | MurJ (Lipid II Flippase from E. coli and T. africanus) | MurJ is an essential integral membrane protein in Gram-negative bacteria that fl |
| protein | proteins/abc-transporters/murj/ | MurJ (Lipid II Flippase from E. coli and T. africanus) | MurJ is an essential integral membrane protein in Gram-negative bacteria that fl |
| protein | proteins/abc-transporters/murj/ | MurJ (Lipid II Flippase from E. coli and T. africanus) | MurJ is an essential integral membrane protein in Gram-negative bacteria that fl |
| protein | proteins/abc-transporters/murj/ | MurJ (Lipid II Flippase from E. coli and T. africanus) | MurJ is an essential integral membrane protein in Gram-negative bacteria that fl |
| protein | proteins/abc-transporters/murj/ | MurJ (Lipid II Flippase from E. coli and T. africanus) | MurJ is an essential integral membrane protein in Gram-negative bacteria that fl |
| protein | proteins/abc-transporters/murj/ | MurJ (Lipid II Flippase from E. coli and T. africanus) | MurJ is an essential integral membrane protein in Gram-negative bacteria that fl |
| protein | proteins/abc-transporters/murj/ | MurJ (Lipid II Flippase from E. coli and T. africanus) | MurJ is an essential integral membrane protein in Gram-negative bacteria that fl |
| protein | proteins/abc-transporters/naatm1/ | NaAtm1 ABC Exporter from Novosphingobium aromaticivorans | NaAtm1 is an Atm1/ABCB7/HMT1/ABCB6-family ABC exporter from the Gram-negative ba |
| protein | proteins/abc-transporters/nor-mng/ | NorM-NG (Neisseria gonorrhoeae NorM) - MATE Family Na+-Coupled Transporter | NorM-NG is a multidrug and toxic compound extrusion (MATE) family transporter fr |
| protein | proteins/abc-transporters/norM-vc/ | NorM-VC (Vibrio cholerae NorM) - MATE Family Multidrug Efflux Transporter | NorM-VC is a multidrug and toxic compound extrusion (MATE) family transporter fr |
| protein | proteins/abc-transporters/ntmate2/ | NtMATE2 (Nicotiana tabacum MATE2) - Nicotine MATE transporter | NtMATE2 is a multidrug and toxic compound extrusion (MATE) family transporter fr |
| protein | proteins/abc-transporters/nuclear-cap-binding-complex/ | Nuclear Cap-Binding Complex (CBC) | The nuclear cap-binding complex (CBC) is a heterodimer of CBP20 (NCBP2, 20 kDa)  |
| protein | proteins/abc-transporters/oqxb/ | OqxB efflux pump from Klebsiella pneumoniae | OqxB is a Resistance-Nodulation-Division (RND) efflux pump from *Klebsiella pneu |
| protein | proteins/abc-transporters/pcat1/ | PCAT1 (Peptidase-Containing ABC Transporter from Clostridium thermocellum) | PCAT1 is a peptidase-containing ATP-binding cassette (ABC) transporter from Clos |
| protein | proteins/abc-transporters/pfmate/ | PfMATE (Pyrococcus furiosus Multidrug and Toxic Compound Extrusion Transporter) | PfMATE is a multidrug and toxic compound extrusion (MATE) family transporter fro |
| protein | proteins/abc-transporters/pglk/ | PglK ABC Flippase | PglK is an ATP-binding cassette (ABC) flippase from Campylobacter jejuni that tr |
| protein | proteins/abc-transporters/sav1866/ | Sav1866 (Staphylococcus aureus Multidrug ABC Transporter) | Sav1866 is a homodimeric ABC half-transporter from Staphylococcus aureus that ex |
| protein | proteins/abc-transporters/spr0693/ | Spr0693 Membrane Fusion Protein from Streptococcus pneumoniae | Spr0693 is the membrane fusion protein (MFP) component of the MacAB-like efflux
| protein | proteins/abc-transporters/spr0694-0695/ | Spr0694-0695 ABC Transporter from Streptococcus pneumoniae | The Spr0694-0695 complex from the Gram-positive pathogen Streptococcus pneumonia |
| protein | proteins/abc-transporters/tm287-288/ | TM287/288 Heterodimeric ABC Exporter from Thermotoga maritima | TM287/288 is a heterodimeric ATP-binding cassette (ABC) exporter from
| protein | proteins/abc-transporters/tmrab/ | TmrAB Heterodimeric ABC Transporter from Thermus thermophilus | TmrAB (TmrA/TmrB) from *Thermus thermophilus* is a heterodimeric ABC half-transp |
| protein | proteins/abc-transporters/vcmn/ | VcmN MATE Transporter | VcmN is a multidrug and toxic compound extrusion (MATE) transporter from the pat |
| protein | proteins/abc-transporters/yajc/ | E. coli YajC Transmembrane Protein | YajC is a single transmembrane (TM) protein from Escherichia coli that associate |
| protein | proteins/abc-transporters/yeast-atm1/ | Yeast Mitochondrial ABC Transporter Atm1 | Yeast Atm1 (ABC transporter of mitochondria 1) is a mitochondrial inner membrane |
| protein | proteins/abc-transporters/zneA/ | ZneA Zn(II)/Proton Antiporter from Cupriavidus metallidurans | ZneA is a proton-driven efflux pump specific for Zn(II) from the heavy metal-res |
| protein | proteins/arabidopsis-nitrate-transporter-nrt1-1/ | Arabidopsis thaliana Nitrate Transporter NRT1.1 (CHL1/NPF6.3) | NRT1.1 (CHL1/NPF6.3) is a dual-affinity nitrate transporter from Arabidopsis |
| protein | proteins/arabidopsis-thaliana-cystinosin/ | Arabidopsis thaliana cystinosin (AtCystinosin) | Arabidopsis thaliana cystinosin is a proton-coupled lysosomal cystine transporte |
| protein | proteins/cys-loop-receptors/acetylcholine-binding-protein/ | Acetylcholine-Binding Protein (AChBP) | [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/)-binding protein ( |
| protein | proteins/cys-loop-receptors/declic/ | DeCLIC (Desulfofustis deltaproteobacterium Pentameric Ligand-Gated Ion Channel) | DeCLIC is a prokaryotic pentameric ligand-gated ion channel (pLGIC) from a Desul |
| protein | proteins/cys-loop-receptors/elic/ | ELIC (Erwinia chrysanthemi Pentameric Ligand-Gated Ion Channel) | ELIC is a prokaryotic pentameric ligand-gated ion channel (pLGIC) from the bacte |
| protein | proteins/cys-loop-receptors/gabar-b3/ | Human GABA_A Receptor Beta-3 Subunit | The Human GABA_A Mouse 5-HT3A Receptor Beta-3 PH-E Subunit E of F-[ATP](/xray-mp |
| protein | proteins/cys-loop-receptors/glic-ecd/ | GLIC ECD (Extracellular Domain of Gloeobacter violaceus Ion Channel) | The extracellular domain (ECD) of the [Pentameric Ligand-Gated Ion Channel (pLGI |
| protein | proteins/cys-loop-receptors/glic/ | GLIC (Gloeobacter violaceus Ion Channel) | GLIC is a prokaryotic pentameric ligand-gated ion channel (pLGIC) from the cyano |
| protein | proteins/cys-loop-receptors/glucl/ | GluCl (C. elegans Glutamate-Gated Chloride Channel) | GluCl is the glutamate-gated chloride channel from Caenorhabditis elegans, a pen |
| protein | proteins/cys-loop-receptors/glycine-receptor-alpha3/ | Human Glycine Receptor Alpha-3 Homopentamer (GlyRα3) | The human [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) receptor alpha-3 su |
| protein | proteins/cys-loop-receptors/glyr-alpha3/ | Human Glycine Receptor Alpha 3 (GlyRα3) | Human [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) receptor alpha 3 (GlyRα |
| protein | proteins/cys-loop-receptors/human-alpha4beta2-nicotinic-receptor/ | Human Alpha4Beta2 Nicotinic Receptor | The human alpha4beta2 nicotinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/a |
| protein | proteins/cys-loop-receptors/mouse-5ht3a-receptor/ | Mouse 5-HT3A Receptor | The mouse [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands |
| protein | proteins/cys-loop-receptors/stelic/ | sTeLIC (Tevnia jerichonana Endosymbiont Pentameric Ligand-Gated Ion Channel) | sTeLIC is a prokaryotic pentameric ligand-gated ion channel (pLGIC) from a gamma |
| protein | proteins/enzymes/acer3/ | Alkaline Ceramidase 3 (ACER3) | Alkaline ceramidase 3 (ACER3) is a human integral membrane protein with a seven- |
| protein | proteins/enzymes/adipor2/ | Adiponectin Receptor 2 (ADIPOR2) | [Adiponectin](/xray-mp-wiki/proteins/structural-adhesion/adiponectin/) receptor  |
| protein | proteins/enzymes/af2299/ | AF2299 CDP-Alcohol Phosphotransferase from Archaeoglobus fulgidus | AF2299 is a CDP-alcohol phosphotransferase (CDP-AP) from the hyperthermophilic a |
| protein | proteins/enzymes/afaglb/ | Archaeoglobus fulgidus Oligosaccharyltransferase AfAglB | AfAglB is the catalytic subunit of the oligosaccharyltransferase (OST) from the  |
| protein | proteins/enzymes/afubia/ | AfUbiA - Archaeoglobus fulgidus UbiA Family Prenyltransferase | AfUbiA is a membrane-embedded prenyltransferase from the archaeon *Archaeoglobus |
| protein | proteins/enzymes/aglB/ | A. fulgidus AglB-L Oligosaccharyltransferase | AglB-L (archaeal glycosylation B, Long form) from Archaeoglobus fulgidus is a si |
| protein | proteins/enzymes/apubia/ | ApUbiA (UbiA from Aeropyrum pernix) — Intramembrane Prenyltransferase | ApUbiA is an intramembrane prenyltransferase from the hyperthermophilic archaeon |
| protein | proteins/enzymes/aquifex-aeolicus-ftsh/ | FtsH from Aquifex aeolicus (A. aeolicus AAA Protease) | FtsH is a universally conserved [ATP](/xray-mp-wiki/reagents/ligands/atp/)-depen |
| protein | proteins/enzymes/aquifex-aeolicus-mray/ | Aquifex aeolicus MraY Phospho-MurNAc-pentapeptide Translocase | MraY (phospho-MurNAc-pentapeptide translocase) from Aquifex aeolicus
| protein | proteins/enzymes/archaeoglobus-fulgidus-aglb/ | Archaeoglobus fulgidus AglB (AfAglB) | Archaeoglobus fulgidus AglB (AfAglB) is the catalytic subunit of the archaeal ol |
| protein | proteins/enzymes/arnt/ | 4-Amino-4-deoxy-L-arabinose Transferase ArnT from Cupriavidus metallidurans | ArnT (PmrK) is an integral membrane lipid-to-lipid glycosyltransferase that |
| protein | proteins/enzymes/ascaris-suum-quinol-fumarate-reductase/ | Ascaris suum Quinol-Fumarate Reductase (QFR) | The X-ray crystal structure of mitochondrial quinol–fumarate reductase (QFR) fro |
| protein | proteins/enzymes/baca/ | Undecaprenyl Pyrophosphate Phosphatase (UppP/BacA) from Escherichia coli | Undecaprenyl pyrophosphate phosphatase (UppP, also known as BacA) is a 30 kDa po |
| protein | proteins/enzymes/bc-chbc/ | bcChbC (Bacillus cereus Chitobiose Transporter) | bcChbC is a [Diacetylchitobiose](/xray-mp-wiki/reagents/ligands/diacetylchitobio |
| protein | proteins/enzymes/bc-malt/ | bcMalT (Bacillus cereus Maltose Transporter) | bcMalT is a [Maltose](/xray-mp-wiki/reagents/additives/maltose) transporter from |
| protein | proteins/enzymes/bcsa/ | BcsA from Rhodobacter sphaeroides (Cellulose Synthase Catalytic Subunit) | BcsA is the catalytically active subunit of the bacterial cellulose synthase com |
| protein | proteins/enzymes/bcsb/ | BcsB from Rhodobacter sphaeroides (Cellulose Synthase Periplasmic Subunit) | BcsB is a periplasmic protein that associates with the catalytic [Bcsa](/xray-mp |
| protein | proteins/enzymes/beetle-icmt/ | Isoprenylcysteine Carboxyl Methyltransferase (ICMT) from Tribolium castaneum | ICMT (isoprenylcysteine carboxyl methyltransferase) from the beetle Tribolium ca |
| protein | proteins/enzymes/cd53/ | Human CD53 Tetraspanin | CD53 (also known as TSPAN25 or OX-44) is a human tetraspanin protein belonging
| protein | proteins/enzymes/clostridium-boltrea-mray/ | Clostridium boltrea MraY Phospho-MurNAc-pentapeptide Translocase with Tunicamycin | MraY (phospho-MurNAc-pentapeptide translocase) is an essential integral membrane |
| protein | proteins/enzymes/clpp/ | ClpP Protease | ClpP is an ATP-dependent, general protease from bacterial cytoplasm that works w |
| protein | proteins/enzymes/cytochrome-b/ | Cytochrome b (EcHyd-1 Partner) | Cytochrome b is the physiological partner of Escherichia coli Hydrogenase 1 (EcH |
| protein | proteins/enzymes/cytochrome-b5-reductase/ | Cytochrome b5 Reductase | Cytochrome b5 reductase (b5R) is a membrane-embedded flavoprotein that catalyzes |
| protein | proteins/enzymes/cytochrome-b5/ | Cytochrome b5 | Cytochrome b5 is a membrane-embedded electron transfer protein consisting of a s |
| protein | proteins/enzymes/cytochrome-b561/ | Cytochrome b561 (Cyt b561) from Arabidopsis thaliana | Cytochrome b561 (Cyt b561) from Arabidopsis thaliana is a transmembrane
| protein | proteins/enzymes/dgka/ | E. coli Diacylglycerol Kinase (DgkA) | Diacylglycerol kinase (DgkA) from Escherichia coli is a 121-residue integral mem |
| protein | proteins/enzymes/dltb/ | DltB (Membrane-Bound O-Acyltransferase) | DltB is a membrane-bound O-acyltransferase (MBOAT) from Streptococcus thermophil |
| protein | proteins/enzymes/dsbA/ | DsbA | DsbA is a periplasmic dithiol oxidase from Escherichia coli belonging to the thi |
| protein | proteins/enzymes/dsbB/ | DsbB (Disulfide Bond Formation Protein B) | DsbB is an integral membrane protein from Escherichia coli that functions as the |
| protein | proteins/enzymes/e-coli-lgt/ | E. coli Lipoprotein Diacylglyceryl Transferase (Lgt) | Lgt (phosphatidylglycerol:prolipoprotein diacylglyceryl transferase) is an integ |
| protein | proteins/enzymes/e-coli-lnt/ | Escherichia coli Apolipoprotein N-Acyl Transferase (Lnt) | Apolipoprotein N-acyl transferase (Lnt) from Escherichia coli is a 512-residue i |
| protein | proteins/enzymes/ec-hyd-1/ | Escherichia coli Hydrogenase 1 (EcHyd-1) | Hydrogenase 1 (EcHyd-1) is a membrane-bound, O2-tolerant [NiFe]-hydrogenase from |
| protein | proteins/enzymes/ecglpg-cyto/ | Cytoplasmic Domain of Escherichia coli Rhomboid Protease GlpG | Crystal structure of the soluble cytoplasmic domain of the Escherichia coli rhom |
| protein | proteins/enzymes/ecpgb/ | E. coli Phosphatidylglycerophosphate Phosphatase B (ecPgpB) | ecPgpB is an E. coli membrane-integrated type II [Phosphatidic Acid](/xray-mp-wi |
| protein | proteins/enzymes/ecrsep/ | Escherichia coli Site-2 Protease Homolog RseP (EcRseP) | EcRseP is the E. coli homolog of [Site-2 Protease (mjS2P) from Methanocaldococcu |
| protein | proteins/enzymes/escherichia-coli-sppa/ | E. coli Signal Peptide Peptidase (SppA, Protease IV) | SppA (signal peptide peptidase, also known as protease IV) from Escherichia coli |
| protein | proteins/enzymes/etf-qo/ | Electron Transfer Flavoprotein-Ubiquinone Oxidoreductase (ETF-QO) | ETF-QO (Electron Transfer Flavoprotein- Oxidoreductase) is a 4Fe4S flavoprotein  |
| protein | proteins/enzymes/flak/ | FlaK (Preflagellin Peptidase from Methanococcus maripaludis) | FlaK is a preflagellin peptidase (PFP) from the archaeon Methanococcus maripalud |
| protein | proteins/enzymes/flap/ | 5-Lipoxygenase Activating Protein (FLAP) | FLAP (5-lipoxygenase activating protein, also known as ALOX5AP) is an integral m |
| protein | proteins/enzymes/glpd-e-coli/ | E. coli Glycerol-3-Phosphate Dehydrogenase (GlpD) | E. coli glycerol-3-phosphate dehydrogenase (GlpD) is an essential monotopic memb |
| protein | proteins/enzymes/glpg/ | GlpG (Escherichia coli Rhomboid Protease) | GlpG is an Escherichia coli rhomboid intramembrane serine protease. It consists  |
| protein | proteins/enzymes/gtrb/ | GtrB Polyisoprenyl-Phosphate Glycosyltransferase from Synechocystis | GtrB is a polyisoprenyl-phosphate glycosyltransferase (PI-GT) from the cyanobact |
| protein | proteins/enzymes/hiGlpG/ | HiGlpG (Haemophilus influenzae Rhomboid Protease) | HiGlpG is the rhomboid intramembrane protease from Haemophilus influenzae, a mem |
| protein | proteins/enzymes/hmmbh/ | Methanosarcina barkeri Membrane-Bound Hydrogenase (HmMBH) | HmMBH is a membrane-bound hydrogenase from Methanosarcina barkeri that forms (SL |
| protein | proteins/enzymes/hsvkor/ | Human Vitamin K Epoxide Reductase (HsVKOR) | Human [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) epoxide reductase |
| protein | proteins/enzymes/human-dhhc20/ | Human DHHC20 Palmitoyltransferase | Human DHHC20 (hDHHC20) is an integral membrane S-acyltransferase of the DHHC
| protein | proteins/enzymes/human-ebp/ | Human Emopamil-Binding Protein (EBP) | Emopamil-Binding Protein (EBP), also known as 3-beta-hydroxysteroid-Delta8,Delta |
| protein | proteins/enzymes/ipct-dipps/ | IPCT/DIPPS from Archaeoglobus fulgidus (Bifunctional CTP:Inositol-1-Phosphate Cytidylyltransferase/CDP-Inositol:Inositol-1-Phosphate Phosphotransferase) | IPCT/DIPPS is a bifunctional membrane enzyme from the hyperthermophilic archaeon |
| protein | proteins/enzymes/jagn1/ | JAGN1 (Jagunal Homolog 1) from Homo sapiens | JAGN1 (Jagunal Homolog 1) is a human four-transmembrane helix protein involved i |
| protein | proteins/enzymes/kkrsep/ | Kangiella koreensis Site-2 Protease Homolog (KkRseP) | KkRseP is an ortholog of E. coli RseP from the marine bacterium Kangiella koreen |
| protein | proteins/enzymes/larB/ | LarB (Lactiplantibacillus plantarum) | LarB is an enzyme from Lactiplantibacillus plantarum (formerly Lactobacillus pla |
| protein | proteins/enzymes/leut/ | LeuT Amino Acid Transporter from Aquifex aeolicus | LeuT is a bacterial amino acid transporter from Aquifex aeolicus that belongs to |
| protein | proteins/enzymes/leut/ | LeuT Amino Acid Transporter from Aquifex aeolicus | LeuT is a bacterial amino acid transporter from Aquifex aeolicus that belongs to |
| protein | proteins/enzymes/lnt/ | Apolipoprotein N-acyltransferase (Lnt) from Escherichia coli | Apolipoprotein N-acyltransferase (Lnt) is an integral membrane enzyme that catal |
| protein | proteins/enzymes/lpcat3/ | LPCAT3 (Lysophosphatidylcholine Acyltransferase 3) | LPCAT3 ([LPC](/xray-mp-wiki/reagents/lipids/lysophosphatidylcholine) Acyltransfe |
| protein | proteins/enzymes/lspa/ | LspA from Staphylococcus aureus (Lipoprotein Signal Peptidase II) | LspA (lipoprotein signal peptidase II) is an integral membrane aspartyl protease |
| protein | proteins/enzymes/ltc4-synthase/ | Human Leukotriene C4 Synthase (LTC4S) | Leukotriene C4 synthase (LTC4S) is a membrane-bound enzyme in the MAPEG (Membran |
| protein | proteins/enzymes/ma-icmt/ | Isoprenylcysteine Carboxyl Methyltransferase (ICMT) from Methanosarcina acetivorans | ICMT (isoprenylcysteine carboxyl methyltransferase) is an integral membrane meth |
| protein | proteins/enzymes/masr1/ | Delta14-sterol reductase MaSR1 from Methylomicrobium alcaliphilum | MaSR1 is a Delta14-sterol reductase from the methanotrophic bacterium Methylomic |
| protein | proteins/enzymes/methanococcus-maripaludis-rce1/ | Methanococcus maripaludis Rce1 (MmRce1) | Rce1 (Ras and α-factor converting enzyme 1) is an intramembrane protease that pr |
| protein | proteins/enzymes/mgst2/ | Human Microsomal Glutathione S-Transferase 2 (MGST2) | Microsomal [GSH](/xray-mp-wiki/reagents/additives/glutathione/) S-transferase 2  |
| protein | proteins/enzymes/mjs2p/ | Site-2 Protease (mjS2P) from Methanocaldococcus jannaschii | The crystal structure of the transmembrane core domain of an S2P family
| protein | proteins/enzymes/mmpsh/ | Archaeal Presenilin Homolog PSH from Methanoculleus marisnigri | PSH (Presenilin Homolog) from Methanoculleus marisnigri (mmPSH) is an archaeal i |
| protein | proteins/enzymes/mouse-scd1/ | Mouse Stearoyl-CoA Desaturase 1 (mSCD1) | Mouse [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) desaturase 1  |
| protein | proteins/enzymes/mpges-1/ | Human Microsomal Prostaglandin E2 Synthase 1 (mPGES-1) | Human microsomal prostaglandin E2 synthase 1 (mPGES-1) is a 152 amino-acid membe |
| protein | proteins/enzymes/mt-pgsa1/ | Phosphatidylinositol Phosphate Synthase PgsA1 from Mycobacterium tuberculosis | Mycobacterium tuberculosis [Phosphatidylinositol](/xray-mp-wiki/reagents/lipids/ |
| protein | proteins/enzymes/narghi/ | Nitrate Reductase A (NarGHI) from Escherichia coli | Nitrate reductase A (NarGHI) is a membrane-bound quinol:nitrate oxidoreductase f |
| protein | proteins/enzymes/narq/ | NarQ (E. coli Nitrate/Nitrite Sensor Histidine Kinase) | NarQ is a transmembrane sensor histidine kinase from Escherichia coli that
| protein | proteins/enzymes/nicastrin/ | Nicastrin from Dictyostelium purpureum (DpNCT) | Nicastrin is a type I transmembrane glycoprotein and the largest component of th |
| protein | proteins/enzymes/nm-epta/ | NmEptA - Lipid A Phosphoethanolamine Transferase from Neisseria meningitidis | NmEptA is a [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) phosphoethanolamin |
| protein | proteins/enzymes/nrfh-quinol-dehydrogenase/ | NrfH Quinol Dehydrogenase from Desulfovibrio vulgaris | NrfH is a membrane-bound cytochrome c quinol dehydrogenase from Desulfovibrio vu |
| protein | proteins/enzymes/orexin-1-receptor/ | Human Orexin 1 Receptor | The human orexin 1 receptor (OX1R, HCRTR1) is a class A [G Protein-Coupled Recep |
| protein | proteins/enzymes/pbgA-yejM/ | PbgA (YejM) Inner Membrane LPS Sensor | [PbgA (YejM) Cardiolipin Transport Protein](/xray-mp-wiki/proteins/enzymes/pbgA- |
| protein | proteins/enzymes/pbsrd5a/ | PbSRD5A Steroid 5α-Reductase (Proteobacteria bacterium) | PbSRD5A is a steroid 5α-reductase from *Proteobacteria bacterium*, a homolog of  |
| protein | proteins/enzymes/pc-mangt/ | PcManGT Mannosyltransferase | PcManGT is a crenarchaeal membrane glycosyltransferase from Pyrobaculum calidifo |
| protein | proteins/enzymes/pglb-campylobacter-lari/ | PglB (Campylobacter lari Oligosaccharyltransferase) | PglB is a single-subunit oligosaccharyltransferase (OST) from the Gram-negative  |
| protein | proteins/enzymes/pip-synthase-rs/ | Phosphatidylinositol-Phosphate Synthase (RsPIPS) from Renibacterium salmoninarum | Phosphatidylinositol-phosphate (PIP) synthase catalyses the first step of [Phosp |
| protein | proteins/enzymes/pmmo/ | Particulate Methane Monooxygenase (pMMO) from Methylococcus capsulatus (Bath) | Particulate methane monooxygenase (pMMO) is an integral membrane metalloenzyme t |
| protein | proteins/enzymes/pmulaa/ | Pasteurella multocida Ascorbate Transporter EIIC (pmUlaA) | pmUlaA is the EIIC component of the L-ascorbate (vitamin C) phosphoenolpyruvate- |
| protein | proteins/enzymes/polysulfide-reductase/ | Polysulfide Reductase (PsrABC) from Thermus thermophilus | Polysulfide reductase (PsrABC) from Thermus thermophilus is an integral membrane |
| protein | proteins/enzymes/pseudomonas-aeruginosa-lnt/ | Pseudomonas aeruginosa Apolipoprotein N-Acyl Transferase (LntPae) | Pseudomonas aeruginosa apolipoprotein N-acyltransferase (LntPae) is a 57 kDa int |
| protein | proteins/enzymes/qsee-periplasmic-domain/ | QseE Periplasmic Sensor Domain (E. coli) | QseE is a histidine kinase (HK) and the sensor component of the QseE/F/G three-c |
| protein | proteins/enzymes/qseg-outer-membrane-lipoprotein/ | QseG Outer Membrane Lipoprotein (E. coli) | QseG (also known as YfhG) is an outer membrane lipoprotein from enterohemorrhagi |
| protein | proteins/enzymes/rat-kmo/ | Rat Kynurenine 3-Monooxygenase (Rat KMO) | Rat Kynurenine 3-monooxygenase (KMO) from Rattus norvegicus is a class A flavopr |
| protein | proteins/enzymes/rembh/ | Ralstonia eutropha Membrane-Bound Hydrogenase (ReMBH) | ReMBH is a membrane-bound, O2-tolerant [NiFe]-hydrogenase from Ralstonia eutroph |
| protein | proteins/enzymes/rod-a/ | Thermus thermophilus RodA | RodA is a 359-residue transmembrane peptidoglycan polymerase from the Shape, Elo |
| protein | proteins/enzymes/sa-pgsa/ | Phosphatidylglycerol Phosphate Synthase PgsA from Staphylococcus aureus | [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol) phosp |
| protein | proteins/enzymes/sagb-spdc-complex/ | SagB-SpdC Complex | The SagB-SpdC complex from Staphylococcus aureus is a membrane protein complex t |
| protein | proteins/enzymes/sc-pmt2-mir-domain/ | Pmt2-MIR Domain (S. cerevisiae Protein O-Mannosyltransferase MIR Domain) | The Pmt2-MIR domain is the luminal MIR (mannosyltransferase, IP3R, and RyR) doma |
| protein | proteins/enzymes/sc-pmt3-mir-domain/ | Pmt3-MIR Domain (S. cerevisiae Protein O-Mannosyltransferase MIR Domain) | The Pmt3-MIR domain is the luminal MIR domain of Pmt3, a member of the PMT2 subf |
| protein | proteins/enzymes/sehyd-1/ | Salmonella enterica Hydrogenase 1 (SeHyd-1) | SeHyd-1 is an O2-tolerant membrane-bound hydrogenase from the prevalent human pa |
| protein | proteins/enzymes/sehyd-5/ | Salmonella enterica Hydrogenase 5 (SeHyd-5) | SeHyd-5 is an O2-tolerant membrane-bound hydrogenase from the prevalent human pa |
| protein | proteins/enzymes/smste24p/ | SmSte24p CAAX Protease from Saccharomyces cerevisiae | SmSte24p (Ste24p) is an integral membrane zinc metalloprotease from Saccharomyce |
| protein | proteins/enzymes/spcs1/ | SPCS1 (Signal Peptidase Complex Subunit 1) from Gallus gallus | SPCS1 (Signal Peptidase Complex Subunit 1) from Gallus gallus (chicken) is a sma |
| protein | proteins/enzymes/sppa-bs/ | Signal Peptide Peptidase A from Bacillus subtilis | Signal peptide peptidase A (SppA) is a membrane-bound self-compartmentalized ser |
| protein | proteins/enzymes/sppa-ec/ | Signal Peptide Peptidase A from Escherichia coli | Signal peptide peptidase (SppA) from *Escherichia coli* is the first crystal str |
| protein | proteins/enzymes/stearoyl-coa-desaturase-1/ | Stearoyl-CoA Desaturase-1 (hSCD1) | [Stearoyl-CoA](/xray-mp-wiki/reagents/ligands/stearoyl-coa/) desaturase-1 (SCD1) |
| protein | proteins/enzymes/steroid-sulfatase/ | Steroid Sulfatase (hSTS) | Steroid sulfatase (hSTS) from human placenta is an integral membrane enzyme of t |
| protein | proteins/enzymes/sulfide-quinone-oxidoreductase/ | Sulfide:Quinone Oxidoreductase (SQR) from Aquifex aeolicus | Sulfide:quinone oxidoreductase (SQR) from Aquifex aeolicus is a flavoprotein tha |
| protein | proteins/enzymes/synechococcus-vkor/ | VKOR from Synechococcus sp. | VKOR ([Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) Epoxide Reductase |
| protein | proteins/enzymes/tat-a-substrate/ | TatA Substrate of E. coli Rhomboid Protease GlpG | TatA is a prokaryotic substrate of the E. coli rhomboid intramembrane protease [ |
| protein | proteins/enzymes/thermotoga-maritima-ftsh/ | Thermotoga maritima FtsH (Apo-FtsH AAA Protease) | FtsH is a universally conserved membrane-anchored ATP-dependent zinc metalloprot |
| protein | proteins/enzymes/tmcdsa/ | TmCdsA CDP-DAG Synthetase | TmCdsA is the CDP-diacylglycerol (CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag/)) |
| protein | proteins/enzymes/transhydrogenase-dii-domain/ | Transhydrogenase dII Domain (Thermus thermophilus) | The transhydrogenase dII domain from Thermus thermophilus is the transmembrane p |
| protein | proteins/enzymes/trvkorl/ | TrVKORL (Pufferfish Vitamin K Epoxide Reductase-Like) | TrVKORL is a [Vitamin K](/xray-mp-wiki/reagents/cofactors/vitamin-k/) epoxide re |
| protein | proteins/enzymes/ulaA/ | UlaA Vitamin C Transporter (E. coli) | UlaA is the membrane-embedded transporter component of the phosphoenolpyruvate-d |
| protein | proteins/enzymes/wzxe/ | WzxE - Lipid III Flippase from Escherichia coli | WzxE is the lipid III flippase from Escherichia coli, responsible for translocat |
| protein | proteins/enzymes/zmpste24/ | Human ZMPSTE24 (Zinc Metalloprotease) | ZMPSTE24 (zinc metalloprotease STE24) is a human integral membrane zinc metallop |
| protein | proteins/flap/ | 5-Lipoxygenase Activating Protein (FLAP) | FLAP (5-lipoxygenase activating protein, also known as ALOX5AP) is an integral m |
| protein | proteins/gpcr/5ht2a-receptor/ | Human 5-HT2A Receptor | The human [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands |
| protein | proteins/gpcr/5ht2b-receptor/ | Human 5-HT2B Receptor | The human serotonin 2B (5-HT2B) receptor is a class A GPCR that signals primaril |
| protein | proteins/gpcr/5ht2c-receptor/ | Human 5-HT2C Serotonin Receptor | The 5-HT2C [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligand |
| protein | proteins/gpcr/a2a-psb1-bril/ | Human Adenosine A2A Receptor A2A-PSB1-bRIL Complex | The [A2AAR](/xray-mp-wiki/proteins/human-adenosine-a2a-receptor-a2ar) (A2AAR) is |
| protein | proteins/gpcr/alpha-1b-adrenergic-receptor/ | Human Alpha-1B Adrenergic Receptor (alpha1B AR) | The human alpha-1B adrenergic receptor (alpha1B AR, ADRA1B) is a class A G prote |
| protein | proteins/gpcr/apelin-receptor/ | Human Apelin Receptor (APJR) | The human apelin receptor (APJR), also known as angiotensin receptor-like 1 (AGT |
| protein | proteins/gpcr/at1r/ | Angiotensin II Type 1 Receptor | The [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) type 1 rece |
| protein | proteins/gpcr/at2r/ | Angiotensin II Type 2 Receptor | The [Angiotensin II](/xray-mp-wiki/reagents/ligands/angiotensin-ii/) type 2 rece |
| protein | proteins/gpcr/beta1-adrenergic-receptor/ | Turkey Beta1-Adrenergic Receptor (beta1AR) | The turkey beta1-adrenergic receptor (beta1AR) is a class A G-protein-coupled re |
| protein | proteins/gpcr/beta2-adrenergic-receptor/ | Human Beta2-Adrenergic Receptor (beta2 AR) | The human beta2-adrenergic receptor (beta2 AR) is a class A G protein-coupled re |
| protein | proteins/gpcr/blt1/ | Leukotriene B4 Receptor 1 (BLT1) — Guinea Pig and Human | The leukotriene B4 receptor 1 (BLT1) is a class A G protein-coupled receptor tha |
| protein | proteins/gpcr/bovine-rhodopsin/ | Bovine Rhodopsin | Rhodopsin is the photoreceptor GPCR in vertebrate retina rod cells, responsible  |
| protein | proteins/gpcr/c5ar1/ | Human Complement C5a Receptor 1 (C5aR1) | The human complement C5a receptor 1 (C5aR1, also known as CD88) is a class A G p |
| protein | proteins/gpcr/cb2/ | Cannabinoid Receptor 2 (CNR2/CB2) | [Cannabinoid](/xray-mp-wiki/concepts/cannabinoid) receptor 2 (CNR2, commonly kno |
| protein | proteins/gpcr/ccr2-t4l/ | CC Chemokine Receptor 2 with T4 Lysozyme Fusion (CCR2-T4L) | CC chemokine receptor 2 (CCR2) is a class A G protein-coupled receptor expressed |
| protein | proteins/gpcr/ccr2a/ | CC Chemokine Receptor 2A (CCR2A) | CC chemokine receptor 2A (CCR2A) is a class A G protein-coupled receptor and the |
| protein | proteins/gpcr/ccr5/ | CCR5 Chemokine Receptor (C-C Chemokine Receptor Type 5) | CCR5 (C-C chemokine receptor type 5) is a class A G protein-coupled receptor (GP |
| protein | proteins/gpcr/ccr7/ | Human CC Chemokine Receptor 7 (CCR7) | The CC chemokine receptor 7 (CCR7) is a class A G protein-coupled receptor (GPCR |
| protein | proteins/gpcr/ccr9/ | CC Chemokine Receptor 9 (CCR9) | CC Chemokine Receptor 9 (CCR9) is a G-protein-coupled receptor (GPCR) activated  |
| protein | proteins/gpcr/cnr1/ | Cannabinoid Receptor 1 (CNR1/CB1) | Cannabinoid receptor 1 (CNR1, commonly known as CB1) is a class A G protein-coup |
| protein | proteins/gpcr/crf1r-star-t4l/ | Human Corticotropin-Releasing Factor 1 Receptor StaR-T4L (CRF1R) | The human corticotropin-releasing factor 1 receptor (CRF1R) is a class A G prote |
| protein | proteins/gpcr/crth2/ | Human CRTH2 (PGD2 Receptor) | CRTH2 (chemoattractant receptor-homologous molecule expressed on Th2 cells, also |
| protein | proteins/gpcr/cxcr4/ | Human CXCR4 Chemokine Receptor | CXCR4 is a G protein-coupled chemokine receptor activated exclusively by the che |
| protein | proteins/gpcr/cyslt1r/ | Cysteinyl Leukotriene Receptor 1 (CysLT1R) | Cysteinyl leukotriene receptor type 1 (CysLT1R) is a class A G protein-coupled r |
| protein | proteins/gpcr/cyslt2r/ | Cysteinyl Leukotriene Receptor 2 (CysLT2R) | Cysteinyl leukotriene receptor type 2 (CysLT2R) is a class A G protein-coupled r |
| protein | proteins/gpcr/d4-dopamine-receptor/ | D4 Dopamine Receptor (DRD4) | The human D4 [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor (DRD4 |
| protein | proteins/gpcr/delta-opioid-receptor/ | Human Delta-Opioid Receptor (DOP) | The δ-opioid receptor (DOP) is a class A G protein-coupled receptor (GPCR) that  |
| protein | proteins/gpcr/drd2/ | Human D2 Dopamine Receptor (DRD2) | The human D2 dopamine receptor (DRD2) is a class A G protein-coupled receptor th |
| protein | proteins/gpcr/drd2/ | Human D2 Dopamine Receptor (DRD2) | The human D2 dopamine receptor (DRD2) is a class A G protein-coupled receptor th |
| protein | proteins/gpcr/dstable-t4-lysozyme/ | dsT4L (Disulfide-Stabilized T4 Lysozyme) | dsT4L is a disulfide-stabilized variant of T4 lysozyme engineered for use as a f |
| protein | proteins/gpcr/ep3-receptor/ | Prostaglandin E2 Receptor EP3 (Prostanoid EP3 Receptor) | The [Prostaglandin E2 (PGE2, Dinoprostone)](/xray-mp-wiki/reagents/ligands/prost |
| protein | proteins/gpcr/etb-receptor-bosentan/ | Human Endothelin ETB Receptor Bound to Bosentan | The human endothelin ETB receptor is a class A G-protein-coupled receptor (GPCR) |
| protein | proteins/gpcr/etb-s6b-complex/ | Human Endothelin ETB Receptor in Complex with Sarafotoxin S6b | The human endothelin ETB receptor (ETBR) is a class A GPCR that binds endothelin |
| protein | proteins/gpcr/fpr2/ | Human Formyl Peptide Receptor 2 (FPR2) | The Human formyl Peptide 5 (Truncated GLP-1 Agonist Nonapeptide) (Truncated GLP- |
| protein | proteins/gpcr/frizzled-4/ | Frizzled 4 Receptor (FZD4) | The Human Frizzled 4 Mouse 5-HT3A Receptor (FZD4) is a class-F G-Rh Protein from |
| protein | proteins/gpcr/gcgr/ | Human Glucagon Receptor (GCGR) | The Human glucagon Mouse 5-HT3A Receptor (GCGR, UniProt P47871) is a class B G-R |
| protein | proteins/gpcr/ghrelin-receptor/ | Human Ghrelin Receptor (GHSR) | The human ghrelin receptor (GHSR, growth hormone secretagogue receptor) is a cla |
| protein | proteins/gpcr/glp1r/ | Human Glucagon-Like Peptide-1 Receptor (GLP-1R) | The human glucagon-like Peptide 5 (Truncated GLP-1 Agonist Nonapeptide) (Truncat |
| protein | proteins/gpcr/gnrh1-receptor/ | Human Gonadotropin-Releasing Hormone Receptor (GnRH1R) | The human gonadotropin-releasing hormone receptor (GnRH1R, also known as luteini |
| protein | proteins/gpcr/gpr52/ | Orphan GPR52 (G Protein-Coupled Receptor 52) | GPR52 is a class-A orphan G-protein-coupled receptor (GPCR) highly expressed in  |
| protein | proteins/gpcr/gpr6/ | GPR6 — Orphan G Protein-Coupled Receptor Implicated in Parkinson's Disease | GPR6 is an orphan class A G protein-coupled receptor belonging to the MECA clust |
| protein | proteins/gpcr/gs-alpha/ | Gs Protein Alpha Subunit (Galpha s) | The Gs protein alpha subunit (Galpha s) is the catalytic subunit of the stimulat |
| protein | proteins/gpcr/gs-beta/ | Gs Protein Beta Subunit (Gbeta1) | The Gs protein beta subunit (Gbeta1) is one of the three subunits of the stimula |
| protein | proteins/gpcr/gs-gamma/ | Gs Protein Gamma Subunit (Ggamma2) | The Gs protein gamma subunit (Ggamma2) is the smallest subunit of the stimulator |
| protein | proteins/gpcr/hgpr40/ | Human Free Fatty Acid Receptor 1 (GPR40) | Human GPR40 (Free Fatty Acid Receptor 1, FFAR1) is a G-protein-coupled receptor  |
| protein | proteins/gpcr/human-5-ht1b-receptor/ | Human 5-HT1B Serotonin Receptor | The human 5-HT1B receptor is a class A G protein-coupled receptor for serotonin  |
| protein | proteins/gpcr/human-5-ht2b-receptor/ | Human 5-HT2B Serotonin Receptor Bound to Ergotamine | The 5-HT2B receptor is a class A G protein-coupled receptor (GPCR) for [Serotoni |
| protein | proteins/gpcr/human-adenosine-a1-receptor-a1ar/ | Human Adenosine A1 Receptor (A1AR) | The human adenosine A1 receptor (A1AR) is a class A G protein-coupled receptor t |
| protein | proteins/gpcr/human-adenosine-a2a-receptor-a2ar/ | Human Adenosine A2A Receptor (A2AR) | The human adenosine A2A receptor (A2AR) is a class A GPCR that regulates glutama |
| protein | proteins/gpcr/human-beta-2-adrenergic-receptor/ | Human Beta-2 Adrenergic Receptor (β2AR) | The human beta-2 adrenergic receptor (β2AR) is a prototypic class A G-protein-co |
| protein | proteins/gpcr/human-beta1-ar/ | Human Beta-1 Adrenergic Receptor (beta1 AR) | The beta-1 adrenergic receptor (beta1 AR) is a G protein-coupled receptor (GPCR) |
| protein | proteins/gpcr/human-ccka-receptor/ | Human Cholecystokinin A Receptor (CCKₐR) | The human cholecystokinin A receptor (CCKₐR) is a class A G-protein-coupled rece |
| protein | proteins/gpcr/human-cckb-receptor/ | Human Cholecystokinin B Receptor (CCKᴅR) | The human cholecystokinin B receptor (CCKᴅR) is a class A G-protein-coupled rece |
| protein | proteins/gpcr/human-dopamine-d3-receptor/ | Human Dopamine D3 Receptor (D3R) | The human dopamine D3 receptor (D3R) is a class A G protein-coupled receptor
| protein | proteins/gpcr/human-endothelin-etb-receptor-et1/ | Human Endothelin ETB Receptor Bound to Endothelin-1 | The human endothelin ETB receptor is a class A GPCR that binds the endogenous
| protein | proteins/gpcr/human-endothelin-etb-receptor-irl2500/ | Human Endothelin ETB Receptor in Complex with IRL2500 | The human endothelin ETB receptor (ETB) is a class A GPCR that binds the endogen |
| protein | proteins/gpcr/human-ep4-receptor/ | Human Prostaglandin E Receptor EP4 | The prostaglandin E2 receptor EP4 (EP4) is a class A G protein-coupled receptor  |
| protein | proteins/gpcr/human-gabab-receptor/ | Human GABA_B Receptor | The human GABA_B receptor (GABA_B R) is a class C G-protein-coupled receptor tha |
| protein | proteins/gpcr/human-gpr132/ | Human GPR132 (G2A) Receptor | GPR132 (also known as G2A) is a proton-sensing G protein-coupled receptor that r |
| protein | proteins/gpcr/human-gpr4/ | Human GPR4 Proton-Sensing Receptor | GPR4 is a proton-sensing G protein-coupled receptor (GPCR) that responds to extr |
| protein | proteins/gpcr/human-gpr65/ | Human GPR65 Proton-Sensing Receptor (TDAG8) | GPR65 (also known as TDAG8) is a proton-sensing G protein-coupled receptor predo |
| protein | proteins/gpcr/human-gpr68/ | Human GPR68 Proton-Sensing Receptor (OGR1) | GPR68 (also known as OGR1, Ovarian Cancer G Protein-coupled Receptor 1) is a pro |
| protein | proteins/gpcr/human-histamine-h1-receptor/ | Human Histamine H1 Receptor (H1R) | The human histamine H1 receptor (H1R) is a [G Protein](/xray-mp-wiki/concepts/si |
| protein | proteins/gpcr/human-histamine-h3-receptor/ | Human Histamine H3 Receptor (H3R) | The human histamine H3 receptor (H3R) is a [G Protein](/xray-mp-wiki/concepts/si |
| protein | proteins/gpcr/human-mt1-melatonin-receptor/ | Human MT1 Melatonin Receptor | The MT1 melatonin receptor (type 1A) is a class A G-protein-coupled receptor tha |
| protein | proteins/gpcr/human-mt2-melatonin-receptor/ | Human MT2 Melatonin Receptor | The human MT2 melatonin receptor (type 1B, MTNR1B) is a class A G-protein-couple |
| protein | proteins/gpcr/human-neurokinin-1-receptor/ | Human Neurokinin 1 Receptor (NK1R) | The human neurokinin 1 receptor (NK1R, TACR1) is a class A G protein-coupled rec |
| protein | proteins/gpcr/human-p2y1-receptor/ | Human P2Y1 Receptor | The human P2Y1 receptor (P2Y1R) is a class A [G Protein](/xray-mp-wiki/concepts/ |
| protein | proteins/gpcr/human-pafr/ | Human Platelet-Activating Factor Receptor (PAFR) | The human platelet-activating factor receptor (PAFR) is a class A [G Protein](/x |
| protein | proteins/gpcr/human-pth1-receptor/ | Human Parathyroid Hormone 1 Receptor (PTH1R) | The human parathyroid hormone 1 receptor (PTH1R) is a class B G-protein-coupled  |
| protein | proteins/gpcr/human-rhodopsin-e113q-m257y/ | Human Rhodopsin E113Q/M257Y Mutant | Human rhodopsin is the visual pigment [GPCR](/xray-mp-wiki/concepts/signaling-re |
| protein | proteins/gpcr/human-smoothened-hsmo/ | Human Smoothened (SMO) — Extracellular Domain Regulation | Human Smoothened (SMO) is a Class F G-protein-coupled receptor (GPCR) and Hedgeh |
| protein | proteins/gpcr/human-y1-receptor-npy1r/ | Human Neuropeptide Y Y1 Receptor (Y1R, NPY1R) | The neuropeptide Y (NPY) Y1 receptor (Y1R, NPY1R) is a class A
| protein | proteins/gpcr/human-y2-receptor-npy2r/ | Human Neuropeptide Y Y2 Receptor (Y2R, NPY2R) | The human neuropeptide Y (NPY) Y2 receptor (Y2R, NPY2R) is a class A G-protein-c |
| protein | proteins/gpcr/jumping-spider-rhodopsin-1/ | Jumping Spider Rhodopsin-1 (JSR1) | The jumping spider rhodopsin-1 (JSR1) from Hasarius adansoni is a class A G prot |
| protein | proteins/gpcr/kappa-opioid-receptor/ | Kappa Opioid Receptor | The human kappa opioid receptor (KOP) is a class A G-protein coupled receptor (G |
| protein | proteins/gpcr/kctd16/ | KCTD16 (Potassium Channel Tetramerization Domain-Containing Protein 16) | KCTD16 is a potassium channel tetramerization domain-containing protein that fun |
| protein | proteins/gpcr/kir7-1/ | Kir7.1 Inwardly Rectifying Potassium Channel | Kir7.1 (encoded by KCNJ13) is an inwardly rectifying potassium channel expressed |
| protein | proteins/gpcr/lpa1/ | Lysophosphatidic Acid Receptor 1 (LPA1) | Lysophosphatidic acid receptor 1 (LPA1, also known as LPAR1 or EDG2) is a class  |
| protein | proteins/gpcr/lpa6/ | Lysophosphatidic Acid Receptor 6 (LPA6/P2Y5) | Lysophosphatidic acid receptor 6 (LPA6, also known as P2Y5 or LPAR6) is a class  |
| protein | proteins/gpcr/m1-muscarinic-acetylcholine-receptor/ | M1 Muscarinic Acetylcholine Receptor | The M1 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine/) |
| protein | proteins/gpcr/m1-star-t4l/ | M1-StaR-T4L | M1-StaR-[T4L](/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/) is a thermostabi |
| protein | proteins/gpcr/m2-muscarinic-acetylcholine-receptor/ | Human M2 Muscarinic Acetylcholine Receptor | The human M2 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcho |
| protein | proteins/gpcr/m3-muscarinic-acetylcholine-receptor/ | M3 Muscarinic Acetylcholine Receptor | The M3 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcholine)  |
| protein | proteins/gpcr/m4-muscarinic-acetylcholine-receptor/ | Human M4 Muscarinic Acetylcholine Receptor | The human M4 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcho |
| protein | proteins/gpcr/m5-muscarinic-acetylcholine-receptor/ | Human M5 Muscarinic Acetylcholine Receptor | The human M5 muscarinic [Acetylcholine](/xray-mp-wiki/reagents/ligands/acetylcho |
| protein | proteins/gpcr/mc4-r/ | Human Melanocortin 4 Receptor (MC4-R) | The human melanocortin 4 receptor (MC4-R) is a class A G protein-coupled recepto |
| protein | proteins/gpcr/metabotropic-glutamate-receptor-5/ | Metabotropic Glutamate Receptor 5 (mGlu5) | Metabotropic glutamate receptor 5 (mGlu5) is a Class C G protein-coupled recepto |
| protein | proteins/gpcr/metarhodopsin-ii/ | Metarhodopsin II | Metarhodopsin II is the light-activated conformation of [Bovine Rhodopsin](/xray |
| protein | proteins/gpcr/mglu1-receptor/ | Human mGlu1 Receptor 7TM Domain (Metabotropic Glutamate Receptor 1) | The human mGlu1 (metabotropic glutamate receptor 1) is a class C G protein-coupl |
| protein | proteins/gpcr/molybdenum-storage-protein/ | Molybdenum Storage Protein (MOSTO) | Molybdenum storage protein (MOSTO) is a heterohexameric (αβ)₃ cage-like protein  |
| protein | proteins/gpcr/mouse-drd4/ | Mouse Dopamine Receptor D4 (DRD4) | Mouse [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) receptor D4 ([DRD4](/ |
| protein | proteins/gpcr/mouse-visual-arrestin-3a/ | Mouse Visual Arrestin (3A) | Mouse visual arrestin 1 (arrestin-1) is a cytosolic protein that binds to phosph |
| protein | proteins/gpcr/mt4l-lysozyme/ | mT4L (Minimal T4 Lysozyme) | mT4L is a minimal variant of T4 lysozyme engineered for [GPCR](/xray-mp-wiki/con |
| protein | proteins/gpcr/mu-opioid-receptor/ | Murine Mu-Opioid Receptor | The murine mu-opioid receptor (muOR, MOP) is a class A G-protein-coupled recepto |
| protein | proteins/gpcr/navae1p-sodium-channel/ | NavAe1p Prokaryotic Sodium Channel Pore | NavAe1p is a pore-only construct of the prokaryotic voltage-gated sodium channel |
| protein | proteins/gpcr/neurotensin-receptor-1/ | Rat Neurotensin Receptor 1 (NTSR1) | The rat [Neurotensin](/xray-mp-wiki/reagents/ligands/neurotensin/) receptor 1 (N |
| protein | proteins/gpcr/nop-receptor/ | Nociceptin/Orphanin FQ Peptide Receptor (NOP) | The nociceptin/orphanin FQ peptide receptor (NOP), also known as ORL-1, is a mem |
| protein | proteins/gpcr/ntsr1-el/ | NTSR1-EL Constitutively Active Mutant | NTSR1-EL is a constitutively active mutant of the rat [Neurotensin](/xray-mp-wik |
| protein | proteins/gpcr/ntsr1-lf/ | NTSR1-LF Mutant | NTSR1-LF is a thermostabilized mutant of the [Neurotensin](/xray-mp-wiki/reagent |
| protein | proteins/gpcr/opsin/ | Opsin (Retinal-Free Rhodopsin Apoprotein) | Opsin is the apoprotein form of rhodopsin, the G-protein-coupled receptor respon |
| protein | proteins/gpcr/orexin-2-receptor/ | Human Orexin 2 Receptor | The human orexin 2 receptor (OX2R, HCRTR2) is a class A GPCR that binds the neur |
| protein | proteins/gpcr/oxytocin-receptor/ | Human Oxytocin Receptor (OTR) | The human oxytocin receptor (OTR) is a class A G protein-coupled receptor (GPCR) |
| protein | proteins/gpcr/p2y12-receptor/ | Human P2Y12 Receptor | The P2Y12 receptor is a class A G protein-coupled receptor (GPCR) expressed on h |
| protein | proteins/gpcr/par1/ | Human Protease-Activated Receptor 1 (PAR1) | Human Protease-Activated Receptor 1 (PAR1) is a class A G protein-coupled recept |
| protein | proteins/gpcr/par2/ | Human Protease-Activated Receptor 2 (PAR2) - Stabilized T4L Fusion | Human Protease-Activated Receptor 2 (PAR2) is a class A G protein-coupled recept |
| protein | proteins/gpcr/rhodopsin-2-2a/ | Bovine Rhodopsin (2.2 A Resolution, PDB 1U19) | High-resolution 2.2 A crystal structure of bovine rhodopsin in the dark state (P |
| protein | proteins/gpcr/rhodopsin-n2c-d282c-mutant/ | Rhodopsin N2C/D282C Mutant | The N2C/D282C mutant of rhodopsin is a thermally stabilized recombinant form wit |
| protein | proteins/gpcr/s1p1/ | Sphingosine-1-Phosphate Receptor 1 (S1P1) | [Sphingosine](/xray-mp-wiki/reagents/lipids/sphingosine)-1-phosphate receptor 1  |
| protein | proteins/gpcr/s1p3/ | Human S1PR3 (Sphingosine-1-Phosphate Receptor 3) | S1PR3 (Sphingosine-1-Phosphate Receptor 3, also known as EDG3) is a class A G pr |
| protein | proteins/gpcr/s1p5/ | Sphingosine-1-Phosphate Receptor 5 (S1P5) | Sphingosine-1-phosphate receptor 5 (S1P5, S1PR5, EDG8) is a class A G protein-co |
| protein | proteins/gpcr/smoothened-fla-fusion/ | SMO-FLA Fusion Construct (SMO-Flavodoxin) | The SMO-FLA fusion construct is an engineered human [SMO](/xray-mp-wiki/proteins |
| protein | proteins/gpcr/smoothened/ | Mouse Smoothened (SMO) — Class F GPCR | Smoothened (SMO) is a seven-transmembrane (7TM) oncoprotein and member of the cl |
| protein | proteins/gpcr/squid-rhodopsin/ | Squid Rhodopsin (Class A GPCR, Gq-coupled) | Squid rhodopsin from Todarodes pacificus is an invertebrate visual pigment that  |
| protein | proteins/gpcr/sstr2/ | Somatostatin Receptor 2 (SSTR2) | Somatostatin receptor 2 (SSTR2) is a class A G protein-coupled receptor that is  |
| protein | proteins/gpcr/sstr4/ | Somatostatin Receptor 4 (SSTR4) | Somatostatin receptor 4 (SSTR4) is a class A G protein-coupled receptor belongin |
| protein | proteins/gpcr/sucnr1/ | SUCNR1 (Succinate Receptor 1 / GPR91) | SUCNR1 ([Succinate (Succinic Acid)](/xray-mp-wiki/reagents/ligands/succinate/) r |
| protein | proteins/gpcr/thromboxane-a2-receptor/ | Human Thromboxane A2 Receptor (TP) | The human thromboxane A2 receptor (TP) is a class A G-protein-coupled receptor t |
| protein | proteins/gpcr/tm86v-delta-ic3a/ | NTSR1 TM86V-ΔIC3A Mutant | [NTSR1](/xray-mp-wiki/proteins/gpcr/neurotensin-receptor-1/) TM86V-ΔIC3A is a di |
| protein | proteins/gpcr/trex1/ | Mouse TREX1 (Three Prime Repair Exonuclease 1) | TREX1 (Three prime repair exonuclease 1) is a crucial mammalian enzyme consistin |
| protein | proteins/gpcr/tubulin-darpin-complex-td1/ | Tubulin-DARPin Complex (TD1) | The Tubulin-DARPin complex (TD1) is a model system for studying ligand binding t |
| protein | proteins/gpcr/turkey-beta1-ar-ligand-free-basal/ | Turkey Beta1-Adrenergic Receptor Ligand-Free Basal State | Turkey beta1-adrenergic receptor (beta1-AR) in its ligand-free basal state, dete |
| protein | proteins/gpcr/turkey-beta1-ar-m23-2vt4/ | Turkey Beta1-Adrenergic Receptor Thermostabilized Mutant M23 with Cyanopindolol (2VT4) | The turkey beta1-adrenergic receptor (beta1AR) thermostabilized mutant M23 was c |
| protein | proteins/gpcr/turkey-beta1-ar-m23/ | Turkey Beta1-Adrenergic Receptor M23 | The turkey beta1-adrenergic receptor (beta1AR) is a class A G protein-coupled re |
| protein | proteins/gpcr/us28/ | US28 Viral Chemokine Receptor | US28 is a G-protein-coupled receptor encoded by human cytomegalovirus (CMV) that |
| protein | proteins/kdel-receptor/ | Human KDEL Receptor | The human KDEL receptor is a seven-pass transmembrane receptor that retrieves es |
| protein | proteins/mfs-transporters/arabidopsis-nitrate-transporter-nrt1-1/ | Arabidopsis thaliana Nitrate Transporter NRT1.1 (CHL1/NPF6.3) | NRT1.1 (CHL1/NPF6.3) is a dual-affinity nitrate transporter from Arabidopsis |
| protein | proteins/mfs-transporters/arabidopsis-thaliana-cystinosin/ | Arabidopsis thaliana cystinosin (AtCystinosin) | Arabidopsis thaliana cystinosin is a proton-coupled lysosomal cystine transporte |
| protein | proteins/mfs-transporters/at-suc1/ | Arabidopsis thaliana Sucrose Transporter SUC1 | Arabidopsis thaliana SUC1 is a low-affinity sucrose-proton symporter from the SU |
| protein | proteins/mfs-transporters/bbfpn/ | BbFPN — Putative Bacterial Ferroportin Homologue from Bdellovibrio bacteriovorus | BbFPN is a putative bacterial homologue of ferroportin (FPN/SLC40A1) from Bdello |
| protein | proteins/mfs-transporters/dtpb/ | Escherichia coli DtpB Peptide Transporter | DtpB is a proton-dependent oligopeptide transporter (POT) from the Major Facilit |
| protein | proteins/mfs-transporters/emrd/ | EmrD Multidrug MFS Transporter from Escherichia coli | EmrD is a multidrug resistance (MDR) Major Facilitator Superfamily (MFS)
| protein | proteins/mfs-transporters/fucose-permease-fucp/ | Fucose Permease (FucP) | [L-Fucose](/xray-mp-wiki/reagents/ligands/l-fucose/) permease (FucP) from E. col |
| protein | proteins/mfs-transporters/gkpot/ | GkPOT Proton-Coupled Oligopeptide Transporter | GkPOT is a [Influenza A M2 Proton Channel](/xray-mp-wiki/proteins/other-ion-chan |
| protein | proteins/mfs-transporters/glcp-se/ | GlcP_Se (Staphylococcus epidermidis Glucose/H+ Symporter) | GlcP_Se is a glucose/H+ symporter from Staphylococcus epidermidis and a
| protein | proteins/mfs-transporters/glpT/ | GlpT Glycerol-3-Phosphate Transporter from Escherichia coli | GlpT (glycerol-3-phosphate transporter) from the E. coli inner Solid-Supported M |
| protein | proteins/mfs-transporters/glut1/ | Human Glucose Transporter GLUT1 (SLC2A1) | The human [Glucose](/xray-mp-wiki/reagents/additives/glucose) transporter GLUT1  |
| protein | proteins/mfs-transporters/glut5/ | GLUT5 Fructose Transporter | GLUT5 is a fructose-specific facilitated-diffusion transporter belonging to the  |
| protein | proteins/mfs-transporters/hglut1/ | hGLUT1 (Human Glucose Transporter 1) | Human [Glucose](/xray-mp-wiki/reagents/additives/glucose/) transporter 1 (hGLUT1 |
| protein | proteins/mfs-transporters/hglut3/ | hGLUT3 (Human Glucose Transporter 3) | Human [Glucose](/xray-mp-wiki/reagents/additives/glucose/) transporter 3 (hGLUT3 |
| protein | proteins/mfs-transporters/human-glut3/ | Human Glucose Transporter 3 (GLUT3) | Human [Glucose](/xray-mp-wiki/reagents/additives/glucose/) transporter 3 (GLUT3, |
| protein | proteins/mfs-transporters/lac-y/ | Lactose Permease of Escherichia coli (LacY) | Lactose permease (LacY) from Escherichia coli is a galactoside/H+ symporter and  |
| protein | proteins/mfs-transporters/lmrp/ | LmrP Multidrug Transporter from Lactococcus lactis | LmrP is a prototypical multidrug efflux pump from Lactococcus lactis belonging
| protein | proteins/mfs-transporters/lprg/ | LprG Lipoprotein (Rv1411) from Mycobacterium tuberculosis | LprG (Rv1411) is a periplasmic [lipoprotein](/xray-mp-wiki/concepts/lipoprotein/ |
| protein | proteins/mfs-transporters/ltaa/ | LtaA — S. aureus Lipid-Linked Disaccharide Flippase | LtaA is a proton-coupled antiporter flippase from Staphylococcus aureus
| protein | proteins/mfs-transporters/mdfA/ | MdfA Multidrug Efflux Transporter | MdfA is a secondary multidrug efflux transporter from Escherichia coli belonging |
| protein | proteins/mfs-transporters/mdfa-i239t-g354e/ | MdfA Multidrug Transporter I239T/G354E Variant (E. coli) | [MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA |
| protein | proteins/mfs-transporters/mdfa/ | Multidrug Transporter MdfA (E26T/D34M/A150E) from Escherichia coli | [MdfA Multidrug Efflux Transporter](/xray-mp-wiki/proteins/mfs-transporters/mdfA |
| protein | proteins/mfs-transporters/melbst/ | Melibiose Permease from Salmonella typhimurium (MelBSt) | [Melibiose](/xray-mp-wiki/reagents/ligands/melibiose) permease (MelB) from Salmo |
| protein | proteins/mfs-transporters/nark/ | NarK Nitrate/Nitrite Antiporter from Escherichia coli | NarK is a nitrate/nitrite antiporter from the nitrate/nitrite porter (NNP) famil |
| protein | proteins/mfs-transporters/naru/ | NarU Nitrate/Nitrite Transporter from Escherichia coli | NarU is a nitrate/nitrite transporter from Escherichia coli belonging to the
| protein | proteins/mfs-transporters/nupg/ | NupG Nucleoside Proton Symporter from Escherichia coli | NupG is a nucleoside proton symporter from [Escherichia coli](/xray-mp-wiki/prot |
| protein | proteins/mfs-transporters/oxit/ | Oxalate Transporter OxIT from Oxalobacter formigenes | Oxalate transporter OxIT is an oxalate:formate antiporter (OFA) from the gut bac |
| protein | proteins/mfs-transporters/pept-sh/ | PepT_Sh — SLC15/POT Family Peptide Transporter from Staphylococcus hominis | PepT_Sh is a prokaryotic homolog of the mammalian proton-coupled oligopeptide tr |
| protein | proteins/mfs-transporters/pept-so/ | PepT_So Oligopeptide Transporter | PepT_So is a proton-coupled oligopeptide transporter from Shewanella oneidensis. |
| protein | proteins/mfs-transporters/pept-so2/ | PepT_So2 Oligopeptide Transporter | PepT_So2 is a proton-dependent oligopeptide transporter from Shewanella oneidens |
| protein | proteins/mfs-transporters/pept-st/ | PepT_St Proton-Dependent Oligopeptide Transporter from Streptococcus thermophilus | PepT_St is a proton-dependent oligopeptide transporter (POT) from Streptococcus  |
| protein | proteins/mfs-transporters/peptst-transporter/ | PepTSt Peptide Transporter from Streptococcus thermophilus | PepTSt is a proton-dependent oligopeptide transporter (POT) from the Major Facil |
| protein | proteins/mfs-transporters/pfht1/ | PfHT1 (Plasmodium falciparum Hexose Transporter 1) | PfHT1 (PF3D7_0204700) is the sole hexose transporter in Plasmodium falciparum,
| protein | proteins/mfs-transporters/rv1410/ | Rv1410 (P55) MFS Transporter from Mycobacterium tuberculosis | Rv1410 (P55) is a proton-driven Major Facilitator Superfamily (MFS) transporter  |
| protein | proteins/mfs-transporters/sotb/ | SotB (Escherichia coli Drug-Proton Antiporter) | SotB is a drug-proton antiporter (DHA) from the DHA1 family (TCDB: 2.A.1.2) of t |
| protein | proteins/mfs-transporters/stp10/ | A. thaliana STP10 | A. thaliana STP10 is a high-affinity [Glucose](/xray-mp-wiki/reagents/additives/ |
| protein | proteins/mfs-transporters/xyle/ | XylE (Escherichia coli Sugar Transporter) | XylE is an Escherichia coli homologue of the human [Glucose](/xray-mp-wiki/reage |
| protein | proteins/mfs-transporters/yajr-transporter/ | YajR Transporter (E. coli MFS Drug Efflux Transporter) | YajR is a 49-kDa putative proton-driven [MFS](/xray-mp-wiki/concepts/major-facil |
| protein | proteins/mfs-transporters/ybgH/ | E. coli YbgH Peptide Transporter | YbgH (also known as DtpD) is a proton-dependent oligopeptide transporter (POT) f |
| protein | proteins/mfs-transporters/yegt/ | YegT Nucleoside Proton Symporter from Escherichia coli | YegT is a member of the nucleoside proton symporter (NHS) family within the [Maj |
| protein | proteins/mfs-transporters/yepept/ | YePEPT (Yersinia enterocolitica Peptide Transporter) | YePEPT is a proton-dependent oligopeptide transporter (POT) family member from
| protein | proteins/miscellaneous/a-thaliana-sweet1/ | A. thaliana SWEET1 | A. thaliana SWEET1 is a glucose transporter from the SWEET family found in Arabi |
| protein | proteins/miscellaneous/af-tmem16/ | afTMEM16 (TMEM16 Lipid Scramblase from Aspergillus fumigatus) | afTMEM16 is a calcium-activated lipid scramblase from the fungus Aspergillus fum |
| protein | proteins/miscellaneous/arabidopsis-thaliana-cystinosin/ | Arabidopsis thaliana cystinosin (AtCystinosin) | Arabidopsis thaliana cystinosin is a proton-coupled lysosomal cystine transporte |
| protein | proteins/miscellaneous/cd47-bril-b6h12/ | CD47 BRIL-B6H12 complex from Homo sapiens | CD47 is the only 5-transmembrane (5-TM) spanning receptor of the immune system.  |
| protein | proteins/miscellaneous/ec-semisweet/ | E. coli SemiSWEET (EcSemiSWEET) | EcSemiSWEET is a sugar transporter from the SWEET family found in Escherichia co |
| protein | proteins/miscellaneous/lbsemisweet/ | LbSemiSWEET from Leptospira biflexa | LbSemiSWEET is a sugar transporter from the SWEET family found in the bacterium  |
| protein | proteins/miscellaneous/mlaA/ | E. coli MlaA Outer Membrane Lipoprotein | MlaA is an [outer membrane](/xray-mp-wiki/concepts/membrane-mimetics/outer-membr |
| protein | proteins/miscellaneous/mtmem16a/ | mTMEM16A (Murine TMEM16A Calcium-Activated Chloride Channel) | mTMEM16A is the murine ortholog of TMEM16A (Ano1), the long sought-after Ca2+-ac |
| protein | proteins/miscellaneous/nhtmem16/ | nhTMEM16 (TMEM16 Lipid Scramblase from Nectria haematococca) | nhTMEM16 is a calcium-activated lipid scramblase from the fungus Nectria haemato |
| protein | proteins/miscellaneous/o-sativa-sweet2b/ | O. sativa SWEET2b (OsSWEET2b) | OsSWEET2b is a vacuolar glucose transporter from the SWEET family found in rice  |
| protein | proteins/miscellaneous/phospholamban/ | Phospholamban (PLB) | Phospholamban (PLB, also known as PLN) is a small (~52 amino acid) membrane prot |
| protein | proteins/miscellaneous/pl5-pentamer/ | PL5 Designed Pentameric Transmembrane Protein | PL5 is a designed homopentameric transmembrane helical bundle based on the apola |
| protein | proteins/miscellaneous/porb-corynebacterium-glutamicum/ | Porin B (PorB) from Corynebacterium glutamicum | Porin B (PorB) is an alpha-helical porin from Corynebacterium glutamicum, a myco |
| protein | proteins/miscellaneous/rocker/ | Rocker — De Novo Designed Zn²⁺ Transporter | Rocker is a de novo designed membrane-spanning four-helical bundle that
| protein | proteins/miscellaneous/tmem266/ | TMEM266 (mouse voltage-sensor protein) | TMEM266 (C15orf27 in human) is a voltage-sensor domain (VSD)-containing protein  |
| protein | proteins/miscellaneous/tysemisweet/ | TySemiSWEET from Thermotoga yellowstonii | TySemiSWEET is a bacterial sugar transporter from the [SemiSWEET Transporter Fam |
| protein | proteins/miscellaneous/vibrio-sp-semisweet/ | Vibrio sp. SemiSWEET | Vibrio sp. [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/transport-mecha |
| protein | proteins/miscellaneous/wza/ | Wza (E. coli Capsular Polysaccharide Export Outer Membrane Lipoprotein) | Wza is an outer membrane lipoprotein from Escherichia coli that forms an octamer |
| protein | proteins/miscellaneous/yeeE/ | YeeE Thiosulfate Transporter from Shewanella thermophila | YeeE is a bacterial membrane protein that mediates thiosulfate uptake for use as |
| protein | proteins/other-ion-channels/a-fulgidus-amt1/ | Amt-1 ammonium transporter from Archaeoglobus fulgidus | Amt-1 is one of three ammonium transporters (Amts) encoded in the genome of the  |
| protein | proteins/other-ion-channels/amp2x/ | AmP2X — P2X Receptor from Amblyomma maculatum (Gulf Coast Tick) | AmP2X is an invertebrate P2X receptor from the Gulf Coast tick Amblyomma maculat |
| protein | proteins/other-ion-channels/amt-b/ | Ammonium Transporter AmtB (E. coli) | AmtB (ammonium transporter B) is a trimeric ammonium channel from
| protein | proteins/other-ion-channels/aqp0/ | Aquaporin 0 (AQP0) from Bos taurus | Aquaporin 0 (AQP0) is the major integral membrane protein of the vertebrate lens |
| protein | proteins/other-ion-channels/aqp1/ | Aquaporin-1 (AQP1) | [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/)-1 (AQP1) is  |
| protein | proteins/other-ion-channels/aqp2/ | Aquaporin-2 (AQP2) | Aquaporin-2 (AQP2) is a water-selective channel expressed in the kidney
| protein | proteins/other-ion-channels/aqpm-methanothermobacter-marburgensis/ | AqpM (Aquaporin from Methanothermobacter marburgensis) | AqpM is the aquaporin from the methanogenic archaeon Methanothermobacter marburg |
| protein | proteins/other-ion-channels/aquaporin-z/ | Aquaporin Z (AqpZ) | [Aquaporin](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) Z (AqpZ) is  |
| protein | proteins/other-ion-channels/aqy1/ | Aqy1 - Yeast Aquaporin from Pichia pastoris | Aqy1 is a water-selective aquaporin from the yeast Pichia pastoris (Komagataella |
| protein | proteins/other-ion-channels/asic1a/ | Acid-Sensing Ion Channel 1a | Acid-sensing ion channel 1a (ASIC1a) is a proton-gated, sodium-selective ion cha |
| protein | proteins/other-ion-channels/atpip2-4/ | AtPIP2;4 (Arabidopsis thaliana Plasma Membrane Intrinsic Protein 2;4) | AtPIP2;4 is a plasma membrane intrinsic protein (PIP) [Aquaporin](/xray-mp-wiki/ |
| protein | proteins/other-ion-channels/attip2-1/ | AtTIP2;1 - Arabidopsis thaliana Tonoplast Intrinsic Protein 2;1 | AtTIP2;1 is an ammonia-permeable [Aquaporin](/xray-mp-wiki/concepts/transport-me |
| protein | proteins/other-ion-channels/avglur1/ | AvGluR1 Ligand-Binding Domain (LBD) | The ligand-binding domain (LBD) of AvGluR1, an ionotropic glutamate receptor fro |
| protein | proteins/other-ion-channels/bovine-urea-transporter-b-utb/ | Bovine Urea Transporter B (UT-B) | Bovine UT-B is a mammalian urea transporter encoded by the SLC14A1 gene. It is a |
| protein | proteins/other-ion-channels/bpe-fluoride-channel/ | Fluoride Channel from B. pertussis (Bpe) | The fluoride channel from [Bordetella pertussis](/xray-mp-wiki/organisms/bordete |
| protein | proteins/other-ion-channels/chicken-bestrophin-1/ | Chicken BEST1 Bestrophin-1 Ca2+-activated Cl- channel | Bestrophin-1 (BEST1) is a calcium-activated chloride channel (CaCC) that regulat |
| protein | proteins/other-ion-channels/chicken-p2x7-receptor/ | Chicken P2X7 Receptor (ckP2X7) | The P2X7 receptor is an [ATP](/xray-mp-wiki/reagents/ligands/atp/)-gated non-sel |
| protein | proteins/other-ion-channels/cpaqp1aa/ | cpAQP1aa (Climbing Perch Aquaporin 1aa) | cpAQP1aa is a water-specific [Aquaporin](/xray-mp-wiki/concepts/transport-mechan |
| protein | proteins/other-ion-channels/ecsatp/ | EcSatP — Bacterial Succinate-Acetate Transporter (AceTr Family) | SatP (also known as yaaH) is a member of the  uptake transporter (AceTr) family
| protein | proteins/other-ion-channels/exbB/ | ExbB (E. coli) | ExbB is an integral polytopic membrane protein from Escherichia coli that is a c |
| protein | proteins/other-ion-channels/exbD/ | ExbD (E. coli) | ExbD is an integral polytopic membrane protein from Escherichia coli that, toget |
| protein | proteins/other-ion-channels/fluc-ec2/ | Fluc-Ec2 Fluoride Channel | Fluc Family of Fluoride Ion Channels-Ec2 is a Ec2-specific Ion Ec2 from an E. co |
| protein | proteins/other-ion-channels/focA-vibrio-cholerae/ | FocA (Formate Channel A from Vibrio cholerae) | FocA (formate channel A) is a pentameric membrane channel belonging to the FNT ( |
| protein | proteins/other-ion-channels/glnk/ | GlnK PII Signal Transduction Protein (E. coli) | GlnK is a PII Prostanoid Receptor Family signal transduction Rh Protein from Nit |
| protein | proteins/other-ion-channels/glpf/ | GlpF (Glycerol Facilitator from E. coli) | GlpF is the [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) facilitator ( |
| protein | proteins/other-ion-channels/gluN1-gluN2b-nmda-receptor/ | GluN1-GluN2B NMDA Receptor (Xenopus laevis, Full-Length) | The full-length N-methyl-[D Aspartate](/xray-mp-wiki/reagents/substrates/l-aspar |
| protein | proteins/other-ion-channels/gluN1b-gluN2b-atd/ | GluN1b-GluN2B ATD (Amino-Terminal Domain of NMDA Receptor Subunits) | The isolated amino-terminal domains (ATD) of the GluN1b and GluN2B subunits of t |
| protein | proteins/other-ion-channels/glua2-3-ampa-receptor/ | GluA2/3 Heteromeric AMPA Receptor | GluA2/3 is a heteromeric AMPA-type ionotropic glutamate receptor composed of Glu |
| protein | proteins/other-ion-channels/glua2-ampa-receptor/ | GluA2 AMPA Receptor — Structures with Antagonists, NAMs, and Allosteric Modulators | GluA2 (also known as GluR2) is an AMPA-subtype ionotropic glutamate receptor (iG |
| protein | proteins/other-ion-channels/glua2-lbd/ | GluA2 Ligand-Binding Domain (L504Y, N775S) | The ligand-binding domain ([LBD](/xray-mp-wiki/proteins/other-ion-channels/avglu |
| protein | proteins/other-ion-channels/hpurel/ | Helicobacter pylori Urea Channel (HpUrel) | HpUrel is a [UREA](/xray-mp-wiki/reagents/substrates/urea/) channel from Helicob |
| protein | proteins/other-ion-channels/hsc/ | HSC (Hydrosulfide Channel from Clostridium difficile) | HSC (hydrosulfide channel) is a pentameric membrane channel from Clostridium dif |
| protein | proteins/other-ion-channels/human-aqp10/ | Human Aquaporin 10 (AQP10) | Human [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) |
| protein | proteins/other-ion-channels/human-aqp5/ | Human Aquaporin 5 (AQP5) | Human Aquaporin 5 (HsAQP5) is a water-selective channel protein belonging to the |
| protein | proteins/other-ion-channels/human-aqp7/ | Human Aquaporin 7 (AQP7) | Human [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) |
| protein | proteins/other-ion-channels/human-aquaporin-1/ | Human Aquaporin 1 (hAQP1) | Human [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) |
| protein | proteins/other-ion-channels/human-aquaporin-2/ | Human Aquaporin 2 (AQP2) | Human [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) |
| protein | proteins/other-ion-channels/human-aquaporin-4/ | Human Aquaporin 4 (hAQP4) | Human [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms/aquaporin/) |
| protein | proteins/other-ion-channels/human-p2x3-receptor/ | Human P2X3 Receptor (hP2X3) | The human P2X3 receptor (hP2X3) is a ligand-gated ion channel from Homo sapiens  |
| protein | proteins/other-ion-channels/influenza-a-m2-proton-channel/ | Influenza A M2 Proton Channel | The M2 proton channel of influenza A virus is a homotetrameric ion channel that  |
| protein | proteins/other-ion-channels/kpbest/ | KpBest Bestrophin Ion Channel | KpBest is a bestrophin ion channel from *Klebsiella pneumoniae* whose crystal st |
| protein | proteins/other-ion-channels/ks-amt5/ | Ks-Amt5 Ammonium Sensor Histidine Kinase from Candidatus Kuenenia stuttgartiensis | Ks-Amt5 (gene locus kust_3690) from the anammox bacterium "Candidatus Kuenenia s |
| protein | proteins/other-ion-channels/lsi1-cryst/ | Rice silicon channel Lsi1 crystallization construct | Lsi1 is the Low silicon rice 1 channel, a silicon (Si) uptake transporter from r |
| protein | proteins/other-ion-channels/mep2-ammonium-transceptor/ | Mep2 Ammonium Transceptor (S. cerevisiae and C. albicans) | Mep2 (methylammonium permease) proteins are fungal ammonium transceptors that fu |
| protein | proteins/other-ion-channels/mgt-e-thermus-thermophilus/ | MgtE (Magnesium Transport Channel) | MgtE is a magnesium-selective ion channel from Thermus thermophilus that mediate |
| protein | proteins/other-ion-channels/mscl/ | Mechanosensitive Channel of Large Conductance MscL (Mycobacterium tuberculosis) | MscL (mechanosensitive channel of large conductance) from Mycobacterium tubercul |
| protein | proteins/other-ion-channels/nerh50/ | NeRh50 (Nitrosomonas europaea Rh50 Ammonia Channel) | NeRh50 is a bacterial homologue of the human Rhesus (Rh) 50 glycoprotein from Ni |
| protein | proteins/other-ion-channels/osnip2-1/ | OsNIP2;1 (Silicon Transporter Lsi1 from Oryza sativa) | OsNIP2;1 (Nodulin26-like Intrinsic Protein 2;1) is a silicon transporter from th |
| protein | proteins/other-ion-channels/pfaqp/ | Aquaglyceroporin PfAQP from Plasmodium falciparum | PfAQP is the sole [Aquaporin Family](/xray-mp-wiki/concepts/transport-mechanisms |
| protein | proteins/other-ion-channels/rh-protein-nitrosomonas-europaeae/ | Rh Protein from Nitrosomonas europaea | The Rh protein from Nitrosomonas europaea is the first determined structure of a |
| protein | proteins/other-ion-channels/rhcg/ | Human Rhesus C Glycoprotein (RhCG) | RhCG (Rhesus C glycoprotein) is a human ammonia channel belonging to the Rh fami |
| protein | proteins/other-ion-channels/salmonella-typhimurium-foca/ | Salmonella typhimurium FocA Formate Channel (StFocA) | FocA (formate channel) from Salmonella typhimurium is a pentameric integral memb |
| protein | proteins/other-ion-channels/sctr1/ | sCtr1 (High-Affinity Copper Transporter from Salmo salar) | Ctr1 is the evolutionarily conserved high-affinity Cu⁺ transporter crucial for d |
| protein | proteins/other-ion-channels/slac1/ | SLAC1 (SLOW ANION CHANNEL 1 from Arabidopsis thaliana) | SLAC1 (SLOW ANION CHANNEL 1) is a plant anion channel from Arabidopsis thaliana  |
| protein | proteins/other-ion-channels/so-pip2-1/ | SoPIP2;1 (Spinach Plasma Membrane Aquaporin) | SoPIP2;1 is a plasma membrane intrinsic protein (PIP) from spinach (Spinacia ole |
| protein | proteins/other-ion-channels/teha/ | TehA (E. coli) | TehA from Escherichia coli is a 314-residue membrane protein and a bacterial
| protein | proteins/other-ion-channels/teha/ | TehA (E. coli) | TehA from Escherichia coli is a 314-residue membrane protein and a bacterial
| protein | proteins/other-ion-channels/teha/ | TehA (E. coli) | TehA from Escherichia coli is a 314-residue membrane protein and a bacterial
| protein | proteins/other-ion-channels/teha/ | TehA (E. coli) | TehA from Escherichia coli is a 314-residue membrane protein and a bacterial
| protein | proteins/other-ion-channels/teha/ | TehA (E. coli) | TehA from Escherichia coli is a 314-residue membrane protein and a bacterial
| protein | proteins/other-ion-channels/teha/ | TehA (E. coli) | TehA from Escherichia coli is a 314-residue membrane protein and a bacterial
| protein | proteins/other-ion-channels/teha/ | TehA (E. coli) | TehA from Escherichia coli is a 314-residue membrane protein and a bacterial
| protein | proteins/other-ion-channels/teha/ | TehA (E. coli) | TehA from Escherichia coli is a 314-residue membrane protein and a bacterial
| protein | proteins/other-ion-channels/teha/ | TehA (E. coli) | TehA from Escherichia coli is a 314-residue membrane protein and a bacterial
| protein | proteins/other-ion-channels/teha/ | TehA (E. coli) | TehA from Escherichia coli is a 314-residue membrane protein and a bacterial
| protein | proteins/other-ion-channels/teha/ | TehA (E. coli) | TehA from Escherichia coli is a 314-residue membrane protein and a bacterial
| protein | proteins/other-ion-channels/teha/ | TehA (E. coli) | TehA from Escherichia coli is a 314-residue membrane protein and a bacterial
| protein | proteins/other-ion-channels/teha/ | TehA (E. coli) | TehA from Escherichia coli is a 314-residue membrane protein and a bacterial
| protein | proteins/other-ion-channels/teha/ | TehA (E. coli) | TehA from Escherichia coli is a 314-residue membrane protein and a bacterial
| protein | proteins/other-ion-channels/teha/ | TehA (E. coli) | TehA from Escherichia coli is a 314-residue membrane protein and a bacterial
| protein | proteins/other-ion-channels/thaumatin/ | Thaumatin | Thaumatin is a sweet-tasting protein isolated from the West African katemfe
| protein | proteins/other-ion-channels/tonB/ | TonB (E. coli) | TonB is an integral polytopic membrane protein from Escherichia coli that serves |
| protein | proteins/other-ion-channels/urea-transporter-dvut/ | Urea Transporter from Desulfovibrio vulgaris (dvUT) | The [UREA](/xray-mp-wiki/reagents/substrates/urea) transporter from *Desulfovibr |
| protein | proteins/other-ion-channels/zfp2x4/ | Zebrafish P2X4 Receptor (zfP2X4) | The zebrafish P2X4 receptor (zfP2X4) is a ligand-gated ion channel from Danio re |
| protein | proteins/photosynthesis/blastochloris-viridis-photosynthetic-reaction-centre/ | Blastochloris viridis Photosynthetic Reaction Centre (RCvir) | The photosynthetic reaction center from Blastochloris viridis (RCvir, formerly R |
| protein | proteins/photosynthesis/blastochloris-viridis-reaction-center/ | Blastochloris viridis Photosynthetic Reaction Center (RC_vir) | The photosynthetic reaction center from Blastochloris viridis (RC_vir, formerly  |
| protein | proteins/photosynthesis/cp29-spinach/ | CP29 Light-Harvesting Complex from Spinach (Spinacia oleracea) | CP29 is a minor light-harvesting chlorophyll a/b-binding protein from photosyste |
| protein | proteins/photosynthesis/fcp-phaeodactylum-tricornutum/ | Fucoxanthin Chlorophyll a/c-Binding Protein (FCP) from Phaeodactylum tricornutum |  chlorophyll a/c-binding protein (FCP) is a light-harvesting antenna protein fro |
| protein | proteins/photosynthesis/heliobacterial-reaction-center/ | Heliobacterial Reaction Center (HbRC) | The heliobacterial reaction center (HbRC) from Heliobacterium modesticaldum is
| protein | proteins/photosynthesis/lh1-rc-supercomplex-tepidum/ | LH1-RC Supercomplex from Thermochromatium tepidum | The light-harvesting complex 1 (LH1) and reaction centre (RC) form a membrane-pr |
| protein | proteins/photosynthesis/lh1-rc-thermochromatium-tepidum/ | LH1-RC complex from Thermochromatium tepidum | The light-harvesting core antenna (LH1) and the reaction centre (RC) from Thermo |
| protein | proteins/photosynthesis/lh2-rps-acidophila/ | B800-850 LH2 Light-Harvesting Complex from Rhodopseudomonas acidophila | The B800-850 light-harvesting complex II (LH2) from Rhodopseudomonas acidophila  |
| protein | proteins/photosynthesis/lh2-rs-molischianum/ | B800-850 Light-Harvesting Complex II (LH2) from Rhodospirillum molischianum | The B800-850 light-harvesting complex II (LH2) from Rhodospirillum molischianum  |
| protein | proteins/photosynthesis/pea-light-harvesting-complex-ii/ | Pea Light-Harvesting Complex II (LHC-II) | The pea light-harvesting complex II (LHC-II) is the major light-harvesting pigme |
| protein | proteins/photosynthesis/photosystem-i-thermosynechococcus-elongatus/ | Photosystem I from Thermosynechococcus elongatus | Photosystem I (PS I) from the thermophilic cyanobacterium Thermosynechococcus el |
| protein | proteins/photosynthesis/photosystem-ii-red-alga/ | Photosystem II from Cyanidium caldarium (red alga) | [Photosystem II](/xray-mp-wiki/proteins/photosynthesis/photosystem-ii/) (PSII) c |
| protein | proteins/photosynthesis/photosystem-ii/ | Photosystem II | Photosystem II (PSII) from Thermosynechococcus elongatus/vulcanus is a homodimer |
| protein | proteins/photosynthesis/photosystem-ii/ | Photosystem II | Photosystem II (PSII) from Thermosynechococcus elongatus/vulcanus is a homodimer |
| protein | proteins/photosynthesis/photosystem-ii/ | Photosystem II | Photosystem II (PSII) from Thermosynechococcus elongatus/vulcanus is a homodimer |
| protein | proteins/photosynthesis/photosystem-ii/ | Photosystem II | Photosystem II (PSII) from Thermosynechococcus elongatus/vulcanus is a homodimer |
| protein | proteins/photosynthesis/photosystem-ii/ | Photosystem II | Photosystem II (PSII) from Thermosynechococcus elongatus/vulcanus is a homodimer |
| protein | proteins/photosynthesis/photosystem-ii/ | Photosystem II | Photosystem II (PSII) from Thermosynechococcus elongatus/vulcanus is a homodimer |
| protein | proteins/photosynthesis/photosystem-ii/ | Photosystem II | Photosystem II (PSII) from Thermosynechococcus elongatus/vulcanus is a homodimer |
| protein | proteins/photosynthesis/photosystem-ii/ | Photosystem II | Photosystem II (PSII) from Thermosynechococcus elongatus/vulcanus is a homodimer |
| protein | proteins/photosynthesis/photosystem-ii/ | Photosystem II | Photosystem II (PSII) from Thermosynechococcus elongatus/vulcanus is a homodimer |
| protein | proteins/photosynthesis/photosystem-ii/ | Photosystem II | Photosystem II (PSII) from Thermosynechococcus elongatus/vulcanus is a homodimer |
| protein | proteins/photosynthesis/photosystem-ii/ | Photosystem II | Photosystem II (PSII) from Thermosynechococcus elongatus/vulcanus is a homodimer |
| protein | proteins/photosynthesis/photosystem-ii/ | Photosystem II | Photosystem II (PSII) from Thermosynechococcus elongatus/vulcanus is a homodimer |
| protein | proteins/photosynthesis/photosystem-ii/ | Photosystem II | Photosystem II (PSII) from Thermosynechococcus elongatus/vulcanus is a homodimer |
| protein | proteins/photosynthesis/photosystem-ii/ | Photosystem II | Photosystem II (PSII) from Thermosynechococcus elongatus/vulcanus is a homodimer |
| protein | proteins/photosynthesis/photosystem-ii/ | Photosystem II | Photosystem II (PSII) from Thermosynechococcus elongatus/vulcanus is a homodimer |
| protein | proteins/photosynthesis/psba2-psii/ | PsbA2-PSII dimer from Thermosynechococcus elongatus | The [Photosystem II](/xray-mp-wiki/proteins/photosynthesis/photosystem-ii/) (PSI |
| protein | proteins/photosynthesis/psba3-psii/ | PsbA3-PSII dimer from Thermosynechococcus elongatus | The [Photosystem II](/xray-mp-wiki/proteins/photosynthesis/photosystem-ii/) (PSI |
| protein | proteins/photosynthesis/psbs-spinach/ | PsbS from Spinach (Spinacia oleracea) | PsbS is a photosystem II protein essential for qE-type non-photochemical quenchi |
| protein | proteins/photosynthesis/psi-lhci-chlamydomonas/ | PSI-LHCI supercomplex from Chlamydomonas reinhardtii | The photosystem I–light-harvesting complex I (PSI-LHCI) supercomplex from the gr |
| protein | proteins/photosynthesis/psi-lhci-pea/ | PSI-LHCI supercomplex from pea (Pisum sativum) at 2.4 A resolution | Photosystem I (PSI) is one of the two photosystems in oxygenic photosynthesis, p |
| protein | proteins/photosynthesis/rhodobacter-sphaeroides-reaction-center/ | Rhodobacter sphaeroides Photosynthetic Reaction Center | The photosynthetic reaction center (RC) from Rhodobacter sphaeroides is a membra |
| protein | proteins/photosynthesis/rps-viridis-reaction-centre/ | Rps. viridis Photosynthetic Reaction Centre | The photosynthetic reaction centre from the purple bacterium Rhodopseudomonas vi |
| protein | proteins/photosynthesis/spinach-light-harvesting-complex-ii/ | Spinach Light-Harvesting Complex II (LHC-II) | The spinach light-harvesting complex II ([LHC-II](/xray-mp-wiki/proteins/photosy |
| protein | proteins/photosynthesis/thermochromatium-tepidum-hipip/ | High-Potential Iron-Sulfur Protein (HiPIP) from Thermochromatium tepidum | The high-potential iron-sulfur protein (HiPIP) from the thermophilic purple sulf |
| protein | proteins/photosynthesis/thermochromatium-tepidum-photosynthetic-reaction-center/ | Photosynthetic Reaction Center from Thermochromatium tepidum | The photosynthetic reaction center (RC) from the thermophilic purple sulfur bact |
| protein | proteins/porb-corynebacterium-glutamicum/ | Porin B (PorB) from Corynebacterium glutamicum | Porin B (PorB) is an alpha-helical porin from Corynebacterium glutamicum, a myco |
| protein | proteins/pumps-atpases/af-copa/ | CopA from Archaeoglobus fulgidus (AfCopA) | CopA from Archaeoglobus fulgidus (AfCopA) is a copper-transporting P1B-type ATPa |
| protein | proteins/pumps-atpases/atp11c-cdc50a/ | ATP11C-CDC50A (Human Plasma Membrane Phospholipid Flippase) | ATP11C is a member of the P4-ATPase family that functions as an aminophospholipi |
| protein | proteins/pumps-atpases/bacillus-pseudofirmus-of4-c12-ring/ | Bacillus pseudofirmus OF4 ATP Synthase A16/20G c12 Ring | The [ATP](/xray-mp-wiki/reagents/ligands/atp/) synthase c-ring from the extreme  |
| protein | proteins/pumps-atpases/bacillus-pseudofirmus-of4-c13-ring/ | Bacillus pseudofirmus OF4 ATP Synthase c13 Ring (Wild-Type) | The [ATP](/xray-mp-wiki/reagents/ligands/atp/) synthase c-ring from the extreme  |
| protein | proteins/pumps-atpases/bioy-lactococcus-lactis/ | BioY - Biotin S Component from Lactococcus lactis | BioY is the biotin-specific S component of the Energy-Coupling Factor (ECF) tran |
| protein | proteins/pumps-atpases/bovine-atp-synthase-c8-ring/ | Bovine Mitochondrial F-ATPase c8-Ring (F1-c-ring Complex) | The bovine mitochondrial F-ATPase (ATP synthase) c8-ring is part of the membrane |
| protein | proteins/pumps-atpases/bovine-f1-atpase-azide-free/ | Bovine F1-ATPase (azide-free ground state) | Bovine F1-ATPase is the catalytic domain of the mitochondrial F1Fo-ATP synthase. |
| protein | proteins/pumps-atpases/bovine-f1-atpase-efrapeptin-complex/ | Bovine F1-ATPase-Efrapeptin Complex | The structure of bovine mitochondrial F1-ATPase complexed with efrapeptin C, a m |
| protein | proteins/pumps-atpases/bovine-f1-atpase-stator-complex/ | Bovine Mitochondrial F1-ATPase-Stator Complex (Membrane Extrinsic Region) | The bovine mitochondrial F1-ATPase-stator complex (F1-stator_T) is a subcomplex  |
| protein | proteins/pumps-atpases/bovine-f1-atpase/ | Bovine F1-ATPase (azide-inhibited form) | Bovine F1-ATPase is the catalytic domain of the mitochondrial F1Fo-ATP synthase, |
| protein | proteins/pumps-atpases/bovine-na-k-atpase/ | Na+,K+-ATPase (Bovine Kidney) | The bovine kidney Na+,K+-ATPase is a P-type ATPase responsible for the
| protein | proteins/pumps-atpases/c-thermarum-f1-atpase/ | F1-ATPase from Caldalkalibacillus thermarum | The F1-ATPase from Caldalkalibacillus thermarum is the water-soluble catalytic d |
| protein | proteins/pumps-atpases/chloroplast-atp-synthase-c-ring/ | Chloroplast ATP Synthase c-Ring from Pisum sativum | The chloroplast [ATP](/xray-mp-wiki/reagents/ligands/atp/) synthase c-ring from  |
| protein | proteins/pumps-atpases/chloroplast-atp-synthase-c14-ring-spinach/ | Spinach Chloroplast ATP Synthase c14-Ring | The c14-ring of the F1Fo ATP synthase from spinach (Spinacia oleracea)
| protein | proteins/pumps-atpases/ecf-cbrt/ | ECF-CbrT (ECF-type ABC Transporter for Vitamin B12 from Lactobacillus delbrueckii) | ECF-CbrT is an Energy Coupling Factor (ECF)-type ABC transporter from Lactobacil |
| protein | proteins/pumps-atpases/ecf-foit-lactobacillus-delbrueckii/ | ECF-FoIT Energy-Coupling Factor Transporter for Folate from Lactobacillus delbrueckii | ECF-FoIT is a group II energy-coupling factor (ECF) transporter from Lactobacill |
| protein | proteins/pumps-atpases/ecf-pant/ | ECF-PanT (Energy-Coupling Factor Pantothenate Transporter) | ECF-PanT is a group II energy-coupling factor (ECF) transporter that mediates th |
| protein | proteins/pumps-atpases/ehirae-v-atpase-k-ring/ | V-Type Na+-ATPase Rotor Ring (NtpK10) from Enterococcus hirae | The membrane rotor ring from the vacuolar-type (V-type) sodium ion-pumping ATPas |
| protein | proteins/pumps-atpases/enterococcus-hirae-v1-atpase/ | V1-ATPase from Enterococcus hirae (EhV1) | [V1-ATPase from Thermus thermophilus](/xray-mp-wiki/proteins/pumps-atpases/v1-at |
| protein | proteins/pumps-atpases/f-nucleatum-f1-atpase/ | F1-ATPase from Fusobacterium nucleatum | The [F1-ATPase from Trypanosoma brucei](/xray-mp-wiki/proteins/pumps-atpases/tbr |
| protein | proteins/pumps-atpases/folate-ecf-transporter-lactobacillus-brevis/ | Folate ECF Transporter from Lactobacillus brevis | The folate [Free Energy Perturbation](/xray-mp-wiki/methods/structure-determinat |
| protein | proteins/pumps-atpases/gastric-hk-atpase/ | Gastric H+,K+-ATPase (Gastric Proton Pump) | The gastric H+,K+-[F1-ATPase from Trypanosoma brucei](/xray-mp-wiki/proteins/pum |
| protein | proteins/pumps-atpases/hmp-ecf-transporter-lactobacillus-brevis/ | HMP ECF Transporter from Lactobacillus brevis | The HMP (hydroxymethyl pyrimidine) energy-coupling factor (ECF) transporter from |
| protein | proteins/pumps-atpases/ilyobacter-tartaricus-c-subunit/ | F-Type Na+-ATPase c11 Rotor Ring from Ilyobacter tartaricus | The crystal structure of the membrane-embedded rotor ring of the sodium ion-tran |
| protein | proteins/pumps-atpases/kdpfabc/ | KdpFABC Potassium-Importing Complex | The KdpFABC complex is a four-subunit potassium pump from Escherichia coli that  |
| protein | proteins/pumps-atpases/ktra/ | KtrA (Cytosolic Regulatory Protein from Bacillus subtilis) | KtrA is a cytosolic regulatory protein from the bacterium Bacillus subtilis that |
| protein | proteins/pumps-atpases/ktrb/ | KtrB (Potassium Transporter Membrane Subunit from Bacillus subtilis) | KtrB is a membrane protein component of the KtrAB potassium transporter from the |
| protein | proteins/pumps-atpases/lp-copa/ | LpCopA (Copper-Transporting P-type ATPase from Legionella pneumophila) | LpCopA is a copper-transporting P_IB-type ATPase from the bacterium Legionella p |
| protein | proteins/pumps-atpases/na-k-atpase-pig-kidney/ | Na+,K+-ATPase (Pig Kidney) | The Na+,K+-ATPase is a P-type ATPase pump that maintains the electrochemical gra |
| protein | proteins/pumps-atpases/ng-hka/ | Non-Gastric H+/K+-ATPase (ngHKA) | The non-gastric H+/K+-ATPase (ngHKA, [ATP](/xray-mp-wiki/reagents/ligands/atp)12 |
| protein | proteins/pumps-atpases/ph-e-subunit-e/ | PH-E Subunit E of F-ATP Synthase Peripheral Stalk | Subunit E of the F-ATP synthase peripheral stalk from Haloarcula marismortui is  |
| protein | proteins/pumps-atpases/ribu/ | RibU (ECF-Type Riboflavin Transporter S Component from Staphylococcus aureus) | RibU is the S component (substrate-binding protein) of the energy-coupling facto |
| protein | proteins/pumps-atpases/sarcolipin/ | Sarcolipin (SLN) | Sarcolipin (SLN) is a small (~30 amino acid) membrane protein that regulates the |
| protein | proteins/pumps-atpases/serca1a/ | SERCA1a (Sarcoplasmic Reticulum Ca²⁺-ATPase 1a) | SERCA1a is the Ca²⁺-ATPase of fast-twitch skeletal muscle sarcoplasmic reticulum |
| protein | proteins/pumps-atpases/serca2a/ | SERCA2a (Cardiac Sarco/Endoplasmic Reticulum Ca2+-ATPase) | SERCA2a is the cardiac isoform of sarco/endoplasmic reticulum Ca2+-ATPase, a P-t |
| protein | proteins/pumps-atpases/serca2b/ | Human SERCA2b — Sarco/Endoplasmic Reticulum Ca²⁺-ATPase 2b | SERCA2b is a ubiquitously expressed isoform of sarco/endoplasmic reticulum Ca²⁺- |
| protein | proteins/pumps-atpases/shark-na-k-atpase/ | Na+,K+-ATPase from Squalus acanthias (Shark) | Na+,K+-ATPase from the shark rectal gland (Squalus acanthias) is a P-type ATPase |
| protein | proteins/pumps-atpases/spinach-chloroplast-c14-rotor-ring/ | Spinach Chloroplast c14 Rotor Ring (CFo c14 Ring) | The crystal structure of the membrane-integral c14 rotor ring of the proton tran |
| protein | proteins/pumps-atpases/spirulina-platensis-c15-ring/ | Spirulina platensis ATP Synthase c15 Ring | The c15 ring from the proton-coupled F1Fo ATP synthase of Spirulina platensis is |
| protein | proteins/pumps-atpases/ss-znta/ | SsZntA (Shigella sonnei Zn2+-ATPase) | SsZntA is a Zn2+-ATPase from Shigella sonnei, a P-type ATPase that functions
| protein | proteins/pumps-atpases/sulfitobacter-scoat/ | sCoaT (Co2+/Zn2+-transporting PIB-4-ATPase from Sulfitobacter sp. NAS14-1) | sCoaT is a PIB-4-type ATPase from Sulfitobacter sp. NAS14-1 (UniProt ID A3T2G5)  |
| protein | proteins/pumps-atpases/t-thermophilus-atpase-peripheral-stalk/ | A-type ATPase peripheral stalk from Thermus thermophilus | The crystal structure of the EG peripheral stalk complex from the A-type ATPase  |
| protein | proteins/pumps-atpases/tbrucei-f1-atpase/ | F1-ATPase from Trypanosoma brucei | The F1-ATPase from Trypanosoma brucei is the catalytic domain of its
| protein | proteins/pumps-atpases/thermus-thermophilus-a-atpase-peripheral-stalk/ | Thermus thermophilus A-ATPase Peripheral Stalk (PS2) | The Thermus thermophilus A-ATPase peripheral stalk (PS2) is a heterodimer of sub |
| protein | proteins/pumps-atpases/thit/ | ThiT — thiamin transporter S-component | ThiT is the thiamin (vitamin B1)-specific S-component of an energy-coupling fact |
| protein | proteins/pumps-atpases/tmppase/ | TmPPase (Thermotoga maritima H+-Pumping Pyrophosphatase) | TmPPase (H+-pumping inorganic pyrophosphatase from Thermotoga maritima) is a mem |
| protein | proteins/pumps-atpases/trka/ | TrkA (ATP-binding Regulatory Subunit from Klebsiella pneumoniae) | TrkA is a cytoplasmic ATP-binding regulatory subunit from the bacterium Klebsiel |
| protein | proteins/pumps-atpases/trkh/ | TrkH (Potassium Channel from Klebsiella pneumoniae) | TrkH is a potassium channel protein from the bacterium Klebsiella pneumoniae tha |
| protein | proteins/pumps-atpases/v1-atpase-t-thermophilus/ | V1-ATPase from Thermus thermophilus | V-type ATPase (V-ATPase) is a rotary ATPase complex that mediates energy convers |
| protein | proteins/pumps-atpases/vit1/ | Plant Vacuolar Iron Transporter 1 (VIT1) | Vacuolar [IRON](/xray-mp-wiki/reagents/additives/iron/) transporter 1 (VIT1) fro |
| protein | proteins/pumps-atpases/vp-trkh/ | TrkH from Vibrio parahaemolyticus (VpTrkH) | [TRKH](/xray-mp-wiki/proteins/pumps-atpases/trkh/) from Vibrio parahaemolyticus  |
| protein | proteins/pumps-atpases/vrh-ppase/ | VrH+PPase (Vigna radiata H+-Pumping Inorganic Pyrophosphatase) | VrH+-PPase (H+-pumping inorganic pyrophosphatase from Vigna radiata, also known  |
| protein | proteins/pumps-atpases/vrppase/ | VrPPase (Vibrio rotiferans H+-Pumping Pyrophosphatase) | VrPPase (H+-pumping inorganic pyrophosphatase from Vibrio rotiferans) is a membr |
| protein | proteins/pumps-atpases/yarrowia-lipolytica-atp-synthase/ | Yarrowia lipolytica F1Fo-ATP Synthase | The F1Fo-ATP synthase from the strictly aerobic yeast Yarrowia lipolytica is a r |
| protein | proteins/pumps-atpases/yeast-atp-synthase-c10-ring/ | Yeast ATP Synthase c10 Ring (Oligomycin-Bound) | The c10 ring of the yeast mitochondrial F1Fo ATP synthase is a homomeric ring of |
| protein | proteins/pumps-atpases/yeast-f1-atpase/ | Yeast Mitochondrial F1 ATPase from Saccharomyces cerevisiae | Yeast mitochondrial F1 ATPase is the water-soluble catalytic domain of the F1F0  |
| protein | proteins/pumps-atpases/yeast-f1c10-atp-synthase-subcomplex/ | Yeast F1c10-ATP Synthase Subcomplex (Mg-ADP Inhibited) | The F1c10 subcomplex of the Saccharomyces cerevisiae F1F0-ATP synthase includes  |
| protein | proteins/pumps-atpases/yeast-mitochondrial-atp-synthase-c10-ring/ | Yeast Mitochondrial ATP Synthase c10 Ring | The c10 ring is the membrane-embedded rotor component of the mitochondrial ATP s |
| protein | proteins/pumps-atpases/yeast-v-atpase-egc-head-peripheral-stalk/ | Yeast V-ATPase EGC_head Peripheral Stalk Complex | The EGC_head complex is a heterotrimeric subcomplex of the yeast vacuolar
| protein | proteins/pumps-atpases/yeast-v-atpase-subunits-d-f-scdf/ | Yeast V-ATPase Subunits D and F (ScDF Assembly) | The DF assembly of the Saccharomyces cerevisiae V-ATPase (ScDF) is a central sta |
| protein | proteins/pumps-atpases/yeast-v1-atpase/ | Yeast V1-ATPase from Saccharomyces cerevisiae | V-type ATPase (V-ATPase) is a rotary ATPase complex that couples ATP hydrolysis  |
| protein | proteins/receptors-signaling/dap12/ | DAP12 (CD331) | DAP12 (Discoidin Domain-Related Protein 12, also known as CD331 or KARAP) is a e |
| protein | proteins/receptors-signaling/il-17a/ | Interleukin-17A (IL-17A) | IL-17A is a secreted cytokine and the best-studied member of the IL-17 cytokine  |
| protein | proteins/receptors-signaling/il-17f/ | Interleukin-17F (IL-17F) | IL-17F is a secreted cytokine and a member of the IL-17 cytokine family. It form |
| protein | proteins/receptors-signaling/il-17ra/ | Interleukin-17 Receptor A (IL-17RA) | IL-17RA is the founding and best-known member of the interleukin-17 receptor (IL |
| protein | proteins/receptors-signaling/il-17rc/ | Interleukin-17 Receptor C (IL-17RC) | IL-17RC is a single-pass type I transmembrane glycoprotein and a member of the i |
| protein | proteins/receptors-signaling/kdel-receptor/ | Human KDEL Receptor | The human KDEL receptor is a seven-pass transmembrane receptor that retrieves es |
| protein | proteins/receptors-signaling/sigma-1-receptor/ | Human Sigma-1 Receptor (SIGMAR1) | The human sigma-1 receptor (SIGMAR1) is an ER-resident single-pass transmembrane |
| protein | proteins/receptors-signaling/sigma-2-receptor/ | Human Sigma-2 Receptor (TMEM97) | The human sigma-2 receptor (σ2 receptor, encoded by TMEM97) is an orphan transme |
| protein | proteins/receptors-signaling/xl-sigma-1-receptor/ | Sigma-1 Receptor from Xenopus laevis (xlS1R) | The sigma-1 receptor (S1R) from Xenopus laevis (xlS1R) is a non-opioid transmemb |
| protein | proteins/rhodopsins/acetabularia-rhodopsin-ii/ | Acetabularia Rhodopsin II | Acetabularia rhodopsin II (ARII) is a light-driven proton pump from the marine a |
| protein | proteins/rhodopsins/anabaena-sensory-rhodopsin/ | Anabaena Sensory Rhodopsin | Anabaena Sensory Rhodopsin (ASR) is a photochromic color sensor
| protein | proteins/rhodopsins/archaerhodopsin-1/ | Archaerhodopsin-1 from Halorubrum sp. aus-1 | Archaerhodopsin-1 (aR-1) is a light-driven proton pump from Halorubrum sp. aus-1 |
| protein | proteins/rhodopsins/archaerhodopsin-2/ | Archaerhodopsin-2 | Archaerhodopsin-2 (aR2) is a light-driven proton pump found in the claret |
| protein | proteins/rhodopsins/archaerhodopsin-3/ | Archaerhodopsin-3 (AR3) | Archaerhodopsin-3 (AR3) is a light-driven proton pump from the archaebacterium H |
| protein | proteins/rhodopsins/bacteriorhodopsin/ | Bacteriorhodopsin (bR) from Halobacterium salinarum | Bacteriorhodopsin (bR) is a light-driven proton pump from the archaeon
| protein | proteins/rhodopsins/bcxer/ | BcXeR (Xenorhodopsin from Bacillus coahuilensis) | BcXeR is a light-driven inward proton pump (xenorhodopsin) from Bacillus coahuil |
| protein | proteins/rhodopsins/c1c2ga/ | C1C2GA (C1C2 T198G/G202A) | C1C2GA is a blue-shifted mutant of the channelrhodopsin chimera C1C2, created by |
| protein | proteins/rhodopsins/channelrhodopsin-2/ | Channelrhodopsin 2 (ChR2) from Chlamydomonas reinhardtii | Channelrhodopsin 2 (ChR2) is a light-gated cation channel from the green alga
| protein | proteins/rhodopsins/channelrhodopsin-c1c2/ | Channelrhodopsin C1C2 | Channelrhodopsin C1C2 is a chimeric construct between Chlamydomonas reinhardtii  |
| protein | proteins/rhodopsins/chrimson/ | Chrimson Channelrhodopsin | Chrimson is a red light-activated channelrhodopsin from the algae *Chlamydomonas |
| protein | proteins/rhodopsins/cir-nonlabens-marinus/ | CIR Chloride-Pumping Rhodopsin from Nonlabens marinus | CIR (Chloride-pumping Rhodopsin/rhodopsin 3, also called NmHR) from the
| protein | proteins/rhodopsins/coccomyxa-rhodopsin/ | Coccomyxa subellipsoidea Rhodopsin (CsR) | Coccomyxa subellipsoidea rhodopsin (CsR) is a light-driven proton pump from the  |
| protein | proteins/rhodopsins/cruxrhodopsin-3/ | Cruxrhodopsin-3 (cR3) from Haloarcula vallismortis | Cruxrhodopsin-3 (cR3) is a light-driven proton pump from the archaeon Haloarcula |
| protein | proteins/rhodopsins/exiguobacterium-sibiricum-rhodopsin/ | Exiguobacterium sibiricum Rhodopsin (ESR) | Exiguobacterium sibiricum rhodopsin (ESR) is a light-driven proton pump
| protein | proteins/rhodopsins/gloeobacter-rhodopsin/ | Gloeobacter Rhodopsin (GR) from Gloeobacter violaceus | Gloeobacter rhodopsin (GR) is a light-driven proton pump from the
| protein | proteins/rhodopsins/gr/ | GR (Halobacterium sp. GR Bacteriorhodopsin) | GR (Halobacterium sp. GR [Bacteriorhodopsin](/xray-mp-wiki/proteins/bacteriorhod |
| protein | proteins/rhodopsins/gtacr1/ | GtACR1 Anion Channelrhodopsin from Guillardia theta | GtACR1 is a natural light-gated anion channelrhodopsin from the cryptophyte alga |
| protein | proteins/rhodopsins/halorhodopsin/ | Halorhodopsin (HR) from Halobacterium salinarum | Halorhodopsin (HR) is a light-driven chloride pump from Halobacterium
| protein | proteins/rhodopsins/heliorhodopsin-48c12/ | Heliorhodopsin 48C12 from actinobacterial fosmid (Lake Kinneret) | HeR-48C12 is a bacterial heliorhodopsin (HeR) discovered in an actinobacterial f |
| protein | proteins/rhodopsins/heliorhodopsin-taher/ | Heliorhodopsin (TaHeR) from Thermoplasmatales archaeon SG8-52-1 | Heliorhodopsin (HeR) from an uncultured Thermoplasmatales archaeon SG8-52-1 (TaH |
| protein | proteins/rhodopsins/hot75bpr-proteorhodopsin/ | HOT75BPR (Blue-Light-Absorbing Proteorhodopsin from Pacific Ocean) | HOT75BPR is a blue-light-absorbing proteorhodopsin isolated from the Pacific Oce |
| protein | proteins/rhodopsins/htrii-transducer/ | HtrII Transducer (Sensory Rhodopsin II Transducer) | HtrII (Halobacterial transducer for sensory rhodopsin II) is the cognate
| protein | proteins/rhodopsins/hwbr/ | Haloquadratum walsbyi Bacteriorhodopsin (HwBR) | HwBR is a light-driven proton pump from the square halophilic archaeon Haloquadr |
| protein | proteins/rhodopsins/ic-plus-plus/ | iC++ (Designed Anion Channelrhodopsin) | iC++ is a designed anion-conducting channelrhodopsin (dACR) created by structure |
| protein | proteins/rhodopsins/kr2-krokinobacter-eikastus-rhodopsin/ | KR2 — Krokinobacter eikastus Rhodopsin 2 (Sodium Pump) | [KR2 (Krokinobacter eikastus Rhodopsin 2) — Light-Driven Sodium Pump](/xray-mp-w |
| protein | proteins/rhodopsins/kr2-rhodopsin/ | Krokinobacter eikastus Rhodopsin 2 (KR2) — Light-Driven Sodium Pump | Krokinobacter eikastus rhodopsin 2 (KR2) is a prototypical light-driven sodium p |
| protein | proteins/rhodopsins/kr2/ | KR2 (Krokinobacter eikastus Rhodopsin 2) — Light-Driven Sodium Pump | KR2 (Krokinobacter eikastus rhodopsin 2) is a light-driven sodium-pumping rhodop |
| protein | proteins/rhodopsins/leptosphaeria-rhodopsin/ | Leptosphaeria Rhodopsin (LR/Mac) | Leptosphaeria rhodopsin (LR), also referred to as LR (Mac), is a light-driven
| protein | proteins/rhodopsins/mastr/ | MastR (Mastigocladopsis repens Rhodopsin) | MastR (Mastigocladopsis repens rhodopsin, also known as MrHR) is a cyanobacteria |
| protein | proteins/rhodopsins/med12bpr-proteorhodopsin/ | Med12BPR (Blue-Light-Absorbing Proteorhodopsin from Mediterranean Sea) | Med12BPR is a blue-light-absorbing proteorhodopsin (BPR) isolated from an uncult |
| protein | proteins/rhodopsins/n2098r/ | N2098R — CyanoRhodopsin from Calothrix sp. NIES-2098 | N2098R is a light-driven outward proton-pumping rhodopsin from the cyanobacteriu |
| protein | proteins/rhodopsins/n4075r/ | N4075R — CyanoRhodopsin from cyanobacterium NIES-4075 | N4075R is a light-driven outward proton-pumping rhodopsin from a cyanobacterial  |
| protein | proteins/rhodopsins/nsxer-xenorhodopsin/ | NsXeR (Xenorhodopsin from Nanosalina) | NsXeR is a light-driven inward proton pump (xenorhodopsin) from the nanohaloarch |
| protein | proteins/rhodopsins/olpvr1/ | OLPVR1 | OLPVR1 is a viral channelrhodopsin from the VR1 group, encoded by the Organic La |
| protein | proteins/rhodopsins/olpvr2/ | OLPVRII (Organic Lake Phycodnavirus Rhodopsin II) | OLPVRII (Organic Lake Phycodnavirus Rhodopsin II) is a viral rhodopsin from grou |
| protein | proteins/rhodopsins/pharaonis-halorhodopsin/ | pharaonis Halorhodopsin (phR) | pharaonis [Halorhodopsin (HR) from Halobacterium salinarum](/xray-mp-wiki/protei |
| protein | proteins/rhodopsins/pspr/ | PspR (DTG Rhodopsin from Pseudomonas putida) | PspR is a light-driven outward proton-pumping microbial rhodopsin from Pseudomon |
| protein | proteins/rhodopsins/schizorhodopsin/ | Schizorhodopsin SzR4 (AM_5_00977) | Schizorhodopsins (SzRs) are a family of light-driven inward H+ pumps identified
| protein | proteins/rhodopsins/sensory-rhodopsin-ii/ | Sensory Rhodopsin II (NpSRII) | Sensory Rhodopsin II (NpSRII) is a phototaxis receptor from the haloarchaeon
| protein | proteins/rhodopsins/srrh-pde/ | Rhodopsin Phosphodiesterase (Rh-PDE) from Salpingoeca rosetta | Rhodopsin phosphodiesterase (Rh-PDE) is an enzyme rhodopsin from the
| protein | proteins/rhodopsins/synechocystis-halorhodopsin/ | Synechocystis Halorhodopsin (SyHR) | Synechocystis [Halorhodopsin (HR) from Halobacterium salinarum](/xray-mp-wiki/pr |
| protein | proteins/rhodopsins/virchr1/ | VirChR1 | VirChR1 is a viral channelrhodopsin from the VR1 group, encoded by TARA-146-SRF- |
| protein | proteins/rhodopsins/xanthorhodopsin/ | Xanthorhodopsin | Xanthorhodopsin is a light-driven proton pump from the eubacterium Salinibacter  |
| protein | proteins/secretion-translocon/bacillus-halodurans-yidc2/ | Bacillus halodurans YidC2 (BhYidC2) | YidC is a conserved membrane protein insertase that inserts its substrates into  |
| protein | proteins/secretion-translocon/bcs1/ | Mouse Bcs1 (AAA Protein Translocase) | Bcs1 is a mitochondrial membrane-bound [AAA](/xray-mp-wiki/reagents/ligands/aaa/ |
| protein | proteins/secretion-translocon/ec-yidc/ | Escherichia coli YidC | YidC is an essential bacterial membrane protein insertase and chaperone that med |
| protein | proteins/secretion-translocon/espB/ | EspB | EspB is a secreted virulence factor from Mycobacterium tuberculosis, encoded wit |
| protein | proteins/secretion-translocon/espg1/ | EspG1 | EspG1 is the ESX-1-specific chaperone from Mycobacterium tuberculosis that belon |
| protein | proteins/secretion-translocon/ftsblq-complex/ | FtsB-FtsL-FtsQ (FtsBLQ) Complex from Escherichia coli | The FtsB-FtsL-FtsQ (FtsBLQ) complex is a heterotrimeric Solid-Supported Membrane |
| protein | proteins/secretion-translocon/geobacillus-thermodenitrificans-secye/ | Geobacillus thermodenitrificans SecYE Active Translocation Channel | The [Single-Crystal Microspectrophotometry](/xray-mp-wiki/methods/structure-dete |
| protein | proteins/secretion-translocon/get1-get2-complex/ | Get1/Get2 GET Insertase Complex | The Get1/Get2 complex (also known as WRB/CAML in metazoans) is the membrane prot |
| protein | proteins/secretion-translocon/get3/ | Get3 (TRC40) TA Protein Targeting Factor | Get3 (TRC40 in metazoans) is a homodimeric ATPase chaperone that delivers tail-a |
| protein | proteins/secretion-translocon/mj0480/ | Mj0480 Archaeal DUF106 Protein | Mj0480 is an archaeal DUF106 protein from Methanocaldococcus jannaschii that fun |
| protein | proteins/secretion-translocon/mycp1/ | MycP1 | MycP1 (Mycobacterial Protease 1) is a membrane-anchored serine protease of the m |
| protein | proteins/secretion-translocon/pe25/ | PE25 | PE25 is the conserved N-terminal domain of the PE (Pro-Glu) protein family from  |
| protein | proteins/secretion-translocon/ppe41/ | PPE41 | PPE41 is the conserved N-terminal domain of the PPE (Pro-Pro-Glu) protein family |
| protein | proteins/secretion-translocon/pyrococcus-furiosus-secye/ | Pyrococcus furiosus SecYE Translocon | The [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/)/SecE complex (SecY |
| protein | proteins/secretion-translocon/secdf/ | Thermus thermophilus SecDF Protein Translocation Motor | SecDF is a membrane protein belonging to the resistance-nodulation-division (RND |
| protein | proteins/secretion-translocon/sece/ | Thermus thermophilus SecE Accessory Subunit | SecE is an essential accessory subunit of the bacterial Sec translocon that stab |
| protein | proteins/secretion-translocon/secg/ | Thermus thermophilus SecG Accessory Subunit | SecG is an accessory subunit of the bacterial Sec translocon that comprises two  |
| protein | proteins/secretion-translocon/secy/ | Thermus thermophilus SecY Core Channel Subunit | SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric |
| protein | proteins/secretion-translocon/secy/ | Thermus thermophilus SecY Core Channel Subunit | SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric |
| protein | proteins/secretion-translocon/secy/ | Thermus thermophilus SecY Core Channel Subunit | SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric |
| protein | proteins/secretion-translocon/secy/ | Thermus thermophilus SecY Core Channel Subunit | SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric |
| protein | proteins/secretion-translocon/secy/ | Thermus thermophilus SecY Core Channel Subunit | SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric |
| protein | proteins/secretion-translocon/secy/ | Thermus thermophilus SecY Core Channel Subunit | SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric |
| protein | proteins/secretion-translocon/secy/ | Thermus thermophilus SecY Core Channel Subunit | SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric |
| protein | proteins/secretion-translocon/secy/ | Thermus thermophilus SecY Core Channel Subunit | SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric |
| protein | proteins/secretion-translocon/secy/ | Thermus thermophilus SecY Core Channel Subunit | SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric |
| protein | proteins/secretion-translocon/secy/ | Thermus thermophilus SecY Core Channel Subunit | SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric |
| protein | proteins/secretion-translocon/secy/ | Thermus thermophilus SecY Core Channel Subunit | SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric |
| protein | proteins/secretion-translocon/secy/ | Thermus thermophilus SecY Core Channel Subunit | SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric |
| protein | proteins/secretion-translocon/secy/ | Thermus thermophilus SecY Core Channel Subunit | SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric |
| protein | proteins/secretion-translocon/secy/ | Thermus thermophilus SecY Core Channel Subunit | SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric |
| protein | proteins/secretion-translocon/secy/ | Thermus thermophilus SecY Core Channel Subunit | SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric |
| protein | proteins/secretion-translocon/secyeg/ | Thermus thermophilus SecYEG Translocon Complex | The SecYEG translocon from Thermus thermophilus is a heterotrimeric protein-cond |
| protein | proteins/secretion-translocon/thermotoga-maritima-seca/ | Thermotoga maritima SecA ATPase | SecA is the cytoplasmic ATPase motor of the bacterial Sec protein translocation  |
| protein | proteins/secretion-translocon/tmyidc/ | TmYidC (Thermotoga maritima YidC Insertase) | TmYidC is the YidC insertase/chaperone from the thermophilic bacterium Thermotog |
| protein | proteins/slc-transporters/adic/ | AdiC Arginine/Agmatine Antiporter | AdiC is an arginine/agmatine antiporter from the APC (amino acid-polyamine-organ |
| protein | proteins/slc-transporters/apct/ | ApcT Amino Acid Transporter from Methanocaldococcus jannaschii | ApcT is a 435-amino acid amino acid transporter from the archaeon Methanocaldoco |
| protein | proteins/slc-transporters/asbt-nm/ | ASBT-NM (Bacterial Homologue of the Bile Acid Sodium Symporter ASBT) | ASBT-NM is a bacterial homologue of the apical sodium-dependent bile acid transp |
| protein | proteins/slc-transporters/asbt-yf/ | ASBT_Yf (Apical Sodium-Dependent Bile Acid Transporter from Yersinia frederiksenii) | _Yf (Apical Sodium-Dependent Bile Acid Transporter from Yersinia frederiksenii) |
| protein | proteins/slc-transporters/basc/ | BasC (Bacterial Alanine-Serine-Cysteine Exchanger) | BasC is a bacterial L-amino acid transporter (LAT) from the alanine-serine-cyste |
| protein | proteins/slc-transporters/bbzip/ | BbZIP (Bordetella bronchiseptica ZIP metal transporter) | BbZIP (ZIPB) is a prokaryotic ZIP family divalent metal transporter from Bordete |
| protein | proteins/slc-transporters/betp/ | BetP (Na+/Betaine Symporter from Corynebacterium glutamicum) | BetP is a Na+-coupled glycine betaine symporter from the bacterium [Corynebacter |
| protein | proteins/slc-transporters/bovine-adp-atp-carrier/ | Bovine ADP/ATP Carrier | The bovine ADP/ATP carrier (AAC) is a mitochondrial inner membrane protein that  |
| protein | proteins/slc-transporters/cait/ | CaiT Carnitine Antiporter from Escherichia coli | CaiT is an [L-Carnitine](/xray-mp-wiki/reagents/ligands/l-carnitine/)/[Gamma-But |
| protein | proteins/slc-transporters/cax-af-h-ca-exchanger/ | CAX_Af H+/Ca2+ Exchanger (Archaeoglobus fulgidus) | CAX_Af is a H+/Ca2+ exchanger from the hyperthermophilic archaeon Archaeoglobus
| protein | proteins/slc-transporters/clc-ec1/ | CLC-ec1 Cl-/H+ Antiporter | CLC-ec1 is a prokaryotic CLC Cl-/H+ antiporter from Escherichia coli that has se |
| protein | proteins/slc-transporters/clc-sy1/ | CLC-sy1 (CLC Cl-/H+ Antiporter from Synechocystis sp. PCC6803) | CLC-sy1 (SY) is a CLC Cl-/H+ exchange transporter from the cyanobacterium Synech |
| protein | proteins/slc-transporters/cmclc/ | CmCLC Cl-/H+ Antiporter | CmCLC is a CLC Cl-/H+ antiporter from the red alga Cyanidioschyzon merolae. Unli |
| protein | proteins/slc-transporters/cysz/ | CysZ bacterial sulfate permease | CysZ is a bacterial inner-membrane sulfate (SO₄²⁻) permease/channel found exclus |
| protein | proteins/slc-transporters/d-dat/ | Drosophila melanogaster Dopamine Transporter | The Drosophila melanogaster [DOPAMINE](/xray-mp-wiki/reagents/ligands/dopamine)  |
| protein | proteins/slc-transporters/d-dopamine-transporter/ | Drosophila Dopamine Transporter (dDAT) | The Drosophila melanogaster [DOPAMINE](/xray-mp-wiki/reagents/ligands/dopamine)  |
| protein | proteins/slc-transporters/ddat-gat/ | dDAT_GAT (GAT1-Engineered Drosophila Dopamine Transporter) | dDAT_GAT is an engineered construct of the Drosophila melanogaster dopamine tran |
| protein | proteins/slc-transporters/dgot/ | DgoT (E. coli D-galactonate Transporter) | DgoT (D-galactonate transporter) is a proton-coupled D-galactonate/H+ symporter  |
| protein | proteins/slc-transporters/dra-nramp/ | Deinococcus radiodurans Nramp (DraNramp) | DraNramp is a divalent metal transporter from Deinococcus radiodurans belonging  |
| protein | proteins/slc-transporters/drslc38a9/ | Zebrafish SLC38A9 (drSLC38A9) | Zebrafish SLC38A9 (drSLC38A9) is a lysosomal amino acid transporter from Danio r |
| protein | proteins/slc-transporters/dtpa/ | E. coli DtpA Peptide Transporter | DtpA is a proton-dependent oligopeptide transporter (POT) from Escherichia coli  |
| protein | proteins/slc-transporters/eaat1/ | Human Excitatory Amino Acid Transporter 1 (EAAT1) | Human excitatory amino acid transporter 1 (EAAT1, SLC1A3) is a member of the
| protein | proteins/slc-transporters/eca-clcf/ | Eca CLCF (CLC-type F-/H+ Antiporter from Enterococcus casseliflavus) | Eca CLCF is a fluoride/proton (F-/H+) antiporter from the bacterium
| protein | proteins/slc-transporters/ecodmt/ | EcoDMT - Eremococcus coleocola NRAMP Divalent Metal Transporter | EcoDMT is a prokaryotic divalent metal transporter from Eremococcus coleocola be |
| protein | proteins/slc-transporters/gadc/ | GadC Glutamate/GABA Antiporter | GadC is a SLC1/EAAT/GATs antiporter from the Apc (JLK-6 acid-polyamine-organocat |
| protein | proteins/slc-transporters/gkApcT/ | GkApcT Amino Acid Transporter (CAT Homologue) | GkApcT is a proton-coupled amino acid transporter from Geobacillus kaustophilus  |
| protein | proteins/slc-transporters/glt-ph/ | GltPh (Glutamate Transporter Homologue from Pyrococcus horikoshii) | GltPh is a sodium-coupled aspartate transporter from the archaeon Pyrococcus hor |
| protein | proteins/slc-transporters/glttk/ | GltTk — substrate-free aspartate transporter | GltTk is a sodium-coupled aspartate transporter from Thermococcus kodakarensis,
| protein | proteins/slc-transporters/glttk/ | GltTk — substrate-free aspartate transporter | GltTk is a sodium-coupled aspartate transporter from Thermococcus kodakarensis,
| protein | proteins/slc-transporters/glttk/ | GltTk — substrate-free aspartate transporter | GltTk is a sodium-coupled aspartate transporter from Thermococcus kodakarensis,
| protein | proteins/slc-transporters/glttk/ | GltTk — substrate-free aspartate transporter | GltTk is a sodium-coupled aspartate transporter from Thermococcus kodakarensis,
| protein | proteins/slc-transporters/glttk/ | GltTk — substrate-free aspartate transporter | GltTk is a sodium-coupled aspartate transporter from Thermococcus kodakarensis,
| protein | proteins/slc-transporters/glttk/ | GltTk — substrate-free aspartate transporter | GltTk is a sodium-coupled aspartate transporter from Thermococcus kodakarensis,
| protein | proteins/slc-transporters/glttk/ | GltTk — substrate-free aspartate transporter | GltTk is a sodium-coupled aspartate transporter from Thermococcus kodakarensis,
| protein | proteins/slc-transporters/glttk/ | GltTk — substrate-free aspartate transporter | GltTk is a sodium-coupled aspartate transporter from Thermococcus kodakarensis,
| protein | proteins/slc-transporters/glttk/ | GltTk — substrate-free aspartate transporter | GltTk is a sodium-coupled aspartate transporter from Thermococcus kodakarensis,
| protein | proteins/slc-transporters/glttk/ | GltTk — substrate-free aspartate transporter | GltTk is a sodium-coupled aspartate transporter from Thermococcus kodakarensis,
| protein | proteins/slc-transporters/glttk/ | GltTk — substrate-free aspartate transporter | GltTk is a sodium-coupled aspartate transporter from Thermococcus kodakarensis,
| protein | proteins/slc-transporters/glttk/ | GltTk — substrate-free aspartate transporter | GltTk is a sodium-coupled aspartate transporter from Thermococcus kodakarensis,
| protein | proteins/slc-transporters/glttk/ | GltTk — substrate-free aspartate transporter | GltTk is a sodium-coupled aspartate transporter from Thermococcus kodakarensis,
| protein | proteins/slc-transporters/glttk/ | GltTk — substrate-free aspartate transporter | GltTk is a sodium-coupled aspartate transporter from Thermococcus kodakarensis,
| protein | proteins/slc-transporters/glttk/ | GltTk — substrate-free aspartate transporter | GltTk is a sodium-coupled aspartate transporter from Thermococcus kodakarensis,
| protein | proteins/slc-transporters/h276395-glt-ph/ | H276,395-GltPh (Humanized GltPh Mutant, R276S/M395R) | H276,395-[GLTPH](/xray-mp-wiki/proteins/slc-transporters/glt-ph/) is a humanized |
| protein | proteins/slc-transporters/hace2/ | Human Angiotensin-Converting Enzyme 2 (hACE2) | Human angiotensin-converting enzyme 2 (hACE2) is a membrane-bound zinc metallopr |
| protein | proteins/slc-transporters/hent1/ | Human Equilibrative Nucleoside Transporter 1 (hENT1) | hENT1 (SLC29A1) is the founding member of the SLC29 family of equilibrative nucl |
| protein | proteins/slc-transporters/human-ae1-anion-exchanger/ | Human AE1 Anion Exchanger (Band 3) - C-Terminal Membrane Domain | Human AE1 (anion exchanger 1, also known as Band 3) is the most abundant membran |
| protein | proteins/slc-transporters/human-glyt1/ | Human Glycine Transporter 1 (GlyT1) | Human [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) transporter 1 (GlyT1, e |
| protein | proteins/slc-transporters/leubat/ | LeuBAT (LeuT Engineered for Antidepressant Pharmacology) | LeuBAT is an engineered mutant of the bacterial leucine transporter [LEUT](/xray |
| protein | proteins/slc-transporters/mhp1/ | Mhp1 Benzyl-Hydantoin Transporter from Microbacterium liquefaciens | Mhp1 is a member of the Nucleobase-Cation-Symport-1 (NCS1) family from Microbact |
| protein | proteins/slc-transporters/mhsT/ | MhsT Multi-Hydrophobic Amino Acid Transporter from Bacillus halodurans | MhsT is a multi-hydrophobic amino acid transporter from Bacillus halodurans belo |
| protein | proteins/slc-transporters/mj-cora/ | MjCorA — CorA Mg2+ Transporter from Methanocaldococcus jannaschii | CorA is the primary Mg2+ transport system in most prokaryotes and is conserved t |
| protein | proteins/slc-transporters/mjnhaP1/ | MjNhaP1 Sodium/Proton Antiporter | MjNhaP1 is an electroneutral Na+/H+ antiporter from the archaeon *Methanocaldoco |
| protein | proteins/slc-transporters/mtcorb-ac/ | MtCorB Delta-C from Methanoculleus thermophilus | MtCorB Delta-C is a CNNM/CorB family magnesium transporter from the thermophilic |
| protein | proteins/slc-transporters/nap-a/ | Na+/H+ Antiporter NapA from Thermus thermophilus | NapA from Thermus thermophilus is a Na+/H+ antiporter belonging to the CPA2 clad |
| protein | proteins/slc-transporters/ncx-mj/ | NCX_Mj Sodium/Calcium Exchanger from Methanococcus jannaschii | NCX_Mj is a sodium/calcium exchanger (NCX) from the archaeon Methanococcus janna |
| protein | proteins/slc-transporters/nhaa/ | Na+/H+ Antiporter NhaA from Escherichia coli | NhaA from Escherichia coli is a Na+/H+ antiporter belonging to the Major Facilit |
| protein | proteins/slc-transporters/panhap/ | PaNhaP Sodium/Proton Antiporter from Pyrococcus abyssi | PaNhaP is an electroneutral Na+/H+ antiporter from the hyperthermophilic archaeo |
| protein | proteins/slc-transporters/sars-cov-2-ctd/ | SARS-CoV-2 Spike Protein C-Terminal Domain | The C-terminal domain (CTD) of the SARS-CoV-2 spike (S) protein, also known as t |
| protein | proteins/slc-transporters/sbta/ | SbtA (High-Affinity Sodium-Dependent Bicarbonate Transporter, Synechocystis sp. PCC 6803) | SbtA is a high-affinity, sodium-dependent bicarbonate (HCO3-) transporter found  |
| protein | proteins/slc-transporters/sbtb/ | SbtB (PII-Like Regulatory Protein, Synechocystis sp. PCC 6803) | SbtB is a PII-like signal transduction protein from the cyanobacterium Synechocy |
| protein | proteins/slc-transporters/sca-dmt/ | ScaDMT Divalent Metal-Ion Transporter | ScaDMT is a divalent metal-ion transporter from Staphylococcus capitis belonging |
| protein | proteins/slc-transporters/se-cits/ | Salmonella enterica Citrate/Sodium Symporter (SeCitS) | SeCitS is a [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/cit |
| protein | proteins/slc-transporters/siat/ | SiaT Sialic Acid Transporter from Proteus mirabilis | SiaT is a secondary active sialic acid transporter from the uropathogen Proteus  |
| protein | proteins/slc-transporters/slc26dg/ | SLC26Dg (Deinococcus geothermalis Fumarate Transporter) | SLC26Dg is a prokaryotic fumarate transporter from the bacterium Deinococcus geo |
| protein | proteins/slc-transporters/slc35a1/ | SLC35A1 Human CMP-Sialic Acid Transporter (mCST) | SLC35A1 is the human CMP-sialic acid transporter, a member of the SLC35 family o |
| protein | proteins/slc-transporters/slc35c1/ | SLC35C1 Human GDP-Fucose Transporter | SLC35C1 is the human [GDP-Fucose](/xray-mp-wiki/reagents/substrates/gdp-fucose/) |
| protein | proteins/slc-transporters/ssert/ | Human Serotonin Transporter (SERT) | The human [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ligands |
| protein | proteins/slc-transporters/starkeya-novella-yddg/ | Starkeya novella YddG (SnYddG) | SnYddG is a member of the drug/metabolite transporter (DMT) superfamily from the |
| protein | proteins/slc-transporters/stclc/ | StClC CIC Chloride Channel | StClC is a prokaryotic CIC chloride channel from Salmonella enterica serovar typ |
| protein | proteins/slc-transporters/thermothelomyces-thermophila-adp-atp-carrier/ | Thermothelomyces thermophila ADP/ATP Carrier | The Thermothelomyces thermophila ADP/ATP carrier (TtAac) is a mitochondrial inne |
| protein | proteins/slc-transporters/thermotoga-maritima-cora/ | Thermotoga maritima CorA Mg2+ Transporter | The [CorA Magnesium Transporter from Thermotoga maritima](/xray-mp-wiki/proteins |
| protein | proteins/slc-transporters/tm-cora/ | Thermotoga maritima CorA (TmCorA) Magnesium Channel | CorA from Thermotoga maritima (TmCorA) is a homopentameric magnesium ion channel |
| protein | proteins/slc-transporters/tmpit/ | Sodium-dependent Phosphate Transporter TmPiT from Thermotoga maritima | TmPiT (locus Tm0261) is a sodium-dependent phosphate transporter from the hypert |
| protein | proteins/slc-transporters/tpcorc-magnesium-transporter/ | TpCorC Magnesium Transporter from Thermus parvatiensis | CorC is a prokaryotic member of the CNNM/CorC family of Mg2+ transporters, widel |
| protein | proteins/slc-transporters/uapA/ | Uric acid/xanthine H+ symporter UapA from Aspergillus nidulans | UapA from Aspergillus nidulans is a high-affinity purine/H+ symporter specific f |
| protein | proteins/slc-transporters/uraA/ | Uracil:Proton Symporter UraA from Escherichia coli | UraA from Escherichia coli is a [URACIL](/xray-mp-wiki/reagents/ligands/uracil/) |
| protein | proteins/slc-transporters/vccnt/ | vcCNT (Vibrio cholerae Concentrative Nucleoside Transporter) | vcCNT is a concentrative nucleoside transporter from Vibrio cholerae, a member o |
| protein | proteins/slc-transporters/vcindy/ | VcINDY Sodium-Dependent Dicarboxylate Transporter | VcINDY is a sodium-dependent dicarboxylate transporter from Vibrio cholerae, bel |
| protein | proteins/slc-transporters/vcx1/ | Vcx1 (Saccharomyces cerevisiae Vacuolar Ca2+/H+ Exchanger) | Vcx1 (also known as Hum1p) is a vacuolar Ca2+/H+ exchanger from Saccharomyces ce |
| protein | proteins/slc-transporters/vp-zntb/ | Vp-ZntB Cytoplasmic Domain (Vibrio parahaemolyticus Zinc Transporter) | ZntB is a distant homolog of the [CorA Mg2+ Transporter](/xray-mp-wiki/concepts/ |
| protein | proteins/slc-transporters/vrg4/ | Vrg4 GDP-Mannose Transporter (Saccharomyces cerevisiae) | Vrg4 is a [GDP-Mannose](/xray-mp-wiki/reagents/substrates/gdp-mannose) transport |
| protein | proteins/slc-transporters/vsglt/ | V. parahaemolyticus Sodium-Galactose Transporter (vSGLT) | V. parahaemolyticus Sodium-Galactose Transporter (vSGLT) is a secondary active t |
| protein | proteins/slc-transporters/ydah/ | A. borkumensis YdaH transporter | YdaH is an integral membrane protein from Alcanivorax borkumensis encoded by the |
| protein | proteins/slc-transporters/yeast-adp-atp-carrier/ | Yeast ADP/ATP Carrier (Aac2p and Aac3p) | The yeast ADP/ATP carriers (Aac2p and Aac3p) are archetypal members of the
| protein | proteins/slc-transporters/yfke/ | YfkE Ca2+/H+ Antiporter from Bacillus subtilis | YfkE is a Ca2+/H+ antiporter from *Bacillus subtilis* belonging to the [Ca2+:Cat |
| protein | proteins/slc-transporters/yiiP/ | Escherichia coli Zinc Transporter YiiP | YiiP is a Zn²⁺/H⁺ antiporter from the [Cation Diffusion Facilitator (CDF) Family |
| protein | proteins/structural-adhesion/adiponectin/ | Adiponectin | Adiponectin is a hormone secreted mainly from adipocytes that stimulates glucose |
| protein | proteins/structural-adhesion/adiponectin/ | Adiponectin | Adiponectin is a hormone secreted mainly from adipocytes that stimulates glucose |
| protein | proteins/structural-adhesion/adiponectin/ | Adiponectin | Adiponectin is a hormone secreted mainly from adipocytes that stimulates glucose |
| protein | proteins/structural-adhesion/adiponectin/ | Adiponectin | Adiponectin is a hormone secreted mainly from adipocytes that stimulates glucose |
| protein | proteins/structural-adhesion/adiponectin/ | Adiponectin | Adiponectin is a hormone secreted mainly from adipocytes that stimulates glucose |
| protein | proteins/structural-adhesion/adiponectin/ | Adiponectin | Adiponectin is a hormone secreted mainly from adipocytes that stimulates glucose |
| protein | proteins/structural-adhesion/adiponectin/ | Adiponectin | Adiponectin is a hormone secreted mainly from adipocytes that stimulates glucose |
| protein | proteins/structural-adhesion/adiponectin/ | Adiponectin | Adiponectin is a hormone secreted mainly from adipocytes that stimulates glucose |
| protein | proteins/structural-adhesion/adiponectin/ | Adiponectin | Adiponectin is a hormone secreted mainly from adipocytes that stimulates glucose |
| protein | proteins/structural-adhesion/adiponectin/ | Adiponectin | Adiponectin is a hormone secreted mainly from adipocytes that stimulates glucose |
| protein | proteins/structural-adhesion/adiponectin/ | Adiponectin | Adiponectin is a hormone secreted mainly from adipocytes that stimulates glucose |
| protein | proteins/structural-adhesion/adipor1/ | Adiponectin Receptor 1 (ADIPOR1) | [Adiponectin](/xray-mp-wiki/proteins/adiponectin) receptor 1 (ADIPOR1) is an int |
| protein | proteins/structural-adhesion/bctspo/ | BcTSPO Translocator Protein from Bacillus cereus | BcTSPO is the translocator protein (TSPO) homolog from *Bacillus cereus*, a bact |
| protein | proteins/structural-adhesion/cd81/ | Human CD81 Tetraspanin | CD81 (also known as TAPA-1 or tspan28) is a human tetraspanin protein belonging  |
| protein | proteins/structural-adhesion/cd9/ | CD9 (Tetraspanin) | CD9 is a member of the tetraspanin family, a class of four-transmembrane domain  |
| protein | proteins/structural-adhesion/claudin-19-mouse/ | Mouse Claudin-19 (mCldn19) | Mouse claudin-19 (mCldn19) is a tight junction membrane protein belonging to the |
| protein | proteins/structural-adhesion/gabarap/ | GABARAP (Gamma-aminobutyric Acid Receptor-Associated Protein) | GABARAP (Gamma-aminobutyric acid receptor-associated protein) is a member of the |
| protein | proteins/structural-adhesion/glycophorin-a/ | Glycophorin A Transmembrane Domain (GpA-TM) | Glycophorin A (GpA) is a type I single-pass transmembrane sialoglycoprotein foun |
| protein | proteins/structural-adhesion/human-claudin-1/ | Human Claudin-1 (hCLDN-1) | Human claudin-1 (hCLDN-1) is a tetraspanning tight junction membrane protein of  |
| protein | proteins/structural-adhesion/human-claudin-3/ | Human Claudin-3 (hCLDN-3) | Human claudin-3 (hCLDN-3) is a tetraspanning tight junction membrane protein of  |
| protein | proteins/structural-adhesion/human-claudin-4/ | Human Claudin-4 (hCLDN-4) | Human claudin-4 (hCLDN-4) is a 23-34 kDa tetraspanning tight junction membrane p |
| protein | proteins/structural-adhesion/human-claudin-9/ | Human Claudin-9 (hCLDN-9) | Human claudin-9 (hCLDN-9) is a tetraspanning tight junction membrane protein bel |
| protein | proteins/structural-adhesion/human-niemann-pick-c1/ | Human Niemann-Pick C1 (NPC1) | Human NPC1 (Niemann-Pick C1) is a large multi-domain membrane protein essential  |
| protein | proteins/structural-adhesion/mlaC/ | E. coli MlaC Periplasmic Lipid-Binding Protein | MlaC is a soluble [periplasmic](/xray-mp-wiki/concepts/miscellaneous/periplasm/) |
| protein | proteins/structural-adhesion/mlaD/ | E. coli MlaD MCE Protein | MlaD is an [inner membrane](/xray-mp-wiki/concepts/membrane-mimetics/inner-membr |
| protein | proteins/structural-adhesion/mlab/ | E. coli MlaB STAS Domain Protein | MlaB is a small STAS (Sulfate Transporter and Anti-Sigma factor Antagonist) doma |
| protein | proteins/structural-adhesion/mlaf/ | E. coli MlaF ABC ATPase | MlaF is the cytoplasmic ABC ATPase (nucleotide binding domain, NBD) component of |
| protein | proteins/structural-adhesion/mouse-claudin-15/ | Mouse Claudin-15 (mCldn15) | Mouse claudin-15 (mCldn15) is a tight junction membrane protein belonging to the |
| protein | proteins/structural-adhesion/mouse-claudin-3/ | Mouse Claudin-3 (mCLDN-3) | Mouse claudin-3 (mCLDN-3) is a tetraspanning tight junction membrane protein of  |
| protein | proteins/structural-adhesion/mouse-claudin-4/ | Mouse Claudin-4 (mCLDN-4) | Mouse claudin-4 (mCLDN-4) is a tetraspanning tight junction membrane protein who |
| protein | proteins/structural-adhesion/mvins/ | MvINS - Mycobacterial Insig Homolog from Mycobacterium vanbaalenii | MvINS is a mycobacterial homolog of mammalian Insig proteins, identified from My |
| protein | proteins/structural-adhesion/ncr1/ | Saccharomyces cerevisiae Niemann-Pick Type C-Related Protein 1 (NCR1) | NCR1 (Niemann-Pick type C-Related protein 1) from Saccharomyces cerevisiae is a  |
| protein | proteins/structural-adhesion/pqiB/ | E. coli PqiB Syringe-like MCE Protein | PqiB is a periplasm-spanning MCE (mammalian cell entry) protein from Escherichia |
| protein | proteins/structural-adhesion/rstspo/ | RsTSPO Translocator Protein from Rhodobacter sphaeroides | The 18-kDa translocator protein (TSPO) from *Rhodobacter sphaeroides* (RsTSPO) i |
| protein | proteins/structural-adhesion/snap-25a/ | SNAP-25A (Rat Neuronal Qbc-SNARE Protein) | SNAP-25A (Synaptosomal-Associated Protein of 25 kDa, isoform A) is a neuronal Qb |
| protein | proteins/structural-adhesion/snap29/ | SNAP29 (Synaptosomal-Associated Protein 29) | SNAP29 is a Qbc-SNARE protein that provides both Qb- and Qc-SNARE motifs for the |
| protein | proteins/structural-adhesion/synaptobrevin-2/ | Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein) | Synaptobrevin-2 (also known as VAMP-2) is a neuronal Qc-SNARE protein from rat t |
| protein | proteins/structural-adhesion/syntaxin-1a/ | Syntaxin-1A (Rat Neuronal Qa-SNARE Protein) | Syntaxin-1A is a neuronal Qa-SNARE protein from rat that plays a central role in |
| protein | proteins/structural-adhesion/syntaxin17/ | Syntaxin17 (STX17) | Syntaxin17 (STX17) is a key autophagosomal Qa-SNARE protein essential for autoph |
| protein | proteins/structural-adhesion/tlg2/ | Tlg2 (Cryptococcus thermophilum Qa-SNARE Protein) | Tlg2 is a Qa-SNARE protein from the filamentous fungus Cryptococcus thermophilum |
| protein | proteins/structural-adhesion/vamp8/ | VAMP8 (Vesicle-Associated Membrane Protein 8) | VAMP8 (also known as endobrevin) is an R-SNARE protein that, together with the Q |
| protein | proteins/structural-adhesion/vps45/ | Vps45 (Cryptococcus thermophilum SM Protein) | Vps45 is a Sec1/Munc18-family (SM) protein from the filamentous fungus Cryptococ |
| protein | proteins/structural-adhesion/yebT/ | E. coli YebT Tube-like MCE Protein | YebT (also known as MAM7) is a periplasm-spanning MCE (mammalian cell entry) pro |
| protein | proteins/tg2/ | Human Transglutaminase 2 (TG2) | Transglutaminase 2 (TG2) is a multifunctional enzyme that catalyzes Ca2+-depende |
| protein | proteins/toxins/ahlabc/ | AhlABC Tripartite Alpha-Pore Forming Toxin from Aeromonas hydrophila | AhlABC is a tripartite alpha-pore forming toxin (alpha-PFT) from the Gram-negati |
| protein | proteins/toxins/clyA/ | ClyA Cytotoxin from Escherichia coli | ClyA (also known as HlyE and SheA) is a pore-forming cytotoxin from Escherichia  |
| protein | proteins/toxins/cry6aa/ | Cry6Aa (Bacillus thuringiensis Pore-Forming Toxin) | Cry6Aa is a pesticidal crystal (Cry) toxin from Bacillus thuringiensis with
| protein | proteins/toxins/fragaceatoxin-c/ | Fragaceatoxin C (FraC) from Actinia fragacea | Fragaceatoxin C (FraC) is a potent haemolytic pore-forming toxin (PFT) from the  |
| protein | proteins/toxins/human-dermcidin/ | Human Dermcidin (DCD) Antimicrobial Channel | Dermcidin (DCD) is a human antimicrobial host-defense peptide that forms transme |
| protein | proteins/toxins/listeriolysin-o/ | Listeriolysin O | Listeriolysin O (LLO) is a cholesterol-dependent cytolysin (CDC) and essential v |
| protein | proteins/toxins/smhA/ | SmhA from Serratia marcescens | SmhA is the A component of the SmhABC tripartite alpha-pore-forming toxin (alpha |
| protein | proteins/toxins/smhB/ | SmhB from Serratia marcescens | SmhB is the B component of the SmhABC tripartite alpha-pore-forming toxin (alpha |
| protein | proteins/toxins/tcdA1/ | TcdA1 Toxin Complex A Subunit from Photorhabdus luminescens | TcdA1 is the TcA subunit of the toxin complex from Photorhabdus luminescens subs |
| protein | proteins/toxins/tcdB2-tccC3/ | TcdB2-TccC3 Toxin Complex B-C Fusion from Photorhabdus luminescens | TcdB2-TccC3 is a fusion protein from Photorhabdus luminescens subsp. akhurstii c |
| protein | proteins/voltage-gated-channels/a-pernix-kvap/ | KvAP voltage-dependent K+ channel from Aeropyrum pernix | [KvAP Voltage-Dependent Potassium Channel](/xray-mp-wiki/proteins/voltage-gated- |
| protein | proteins/voltage-gated-channels/atpc1/ | AtTPC1 - Arabidopsis thaliana Two-pore Channel 1 | AtTPC1 (Arabidopsis thaliana Two-pore Channel 1) is a plant vacuolar cation chan |
| protein | proteins/voltage-gated-channels/atpcc1/ | AtTPC1 Vacuolar Two-pore Channel from Arabidopsis thaliana | AtTPC1 is a vacuolar two-pore channel (TPC) from Arabidopsis thaliana that |
| protein | proteins/voltage-gated-channels/bk-channel/ | Human BK (Slo1/MaxiK) Large-Conductance Ca2+-Gated K+ Channel | BK channels (also called MaxiK or Slo1, gene KCNMA1) are large-conductance Ca2+- |
| protein | proteins/voltage-gated-channels/bsyetj/ | BsYetJ TMBIM Ca2+ Channel | BsYetJ is a transmembrane Bax inhibitor motif (TMBIM) protein from Bacillus subt |
| protein | proteins/voltage-gated-channels/ca-vab/ | CaVAb Bacterial Voltage-Gated Calcium Channel | CaVAb is a bacterial voltage-gated calcium channel that serves as an evolutionar |
| protein | proteins/voltage-gated-channels/ci-vsd/ | Ci-VSD Voltage-Sensing Domain | Ci-VSD is the isolated voltage-sensing domain from the Ciona intestinalis voltag |
| protein | proteins/voltage-gated-channels/cmtmem175/ | CmTMEM175 — Prokaryotic TMEM175 Lysosomal Potassium Channel | CmTMEM175 is a prokaryotic homologue of the lysosomal potassium channel TMEM175  |
| protein | proteins/voltage-gated-channels/cp-tric/ | CpTRIC Channel from Clostridium perfringens | CpTRIC is a Trimeric Intracellular Cation (TRIC) channel from the bacterium Clos |
| protein | proteins/voltage-gated-channels/drosophila-orai/ | Drosophila melanogaster Orai (CRAC Channel) | Orai is the pore-forming subunit of the calcium release-activated calcium (CRAC) |
| protein | proteins/voltage-gated-channels/fkbp12/ | FKBP12 (FK506 Binding Protein 12) | FKBP12 (FK506 binding protein 12) is a 12 kDa accessory protein that associates  |
| protein | proteins/voltage-gated-channels/ggtric-a/ | GgTRIC-A (Chicken Trimeric Intracellular Cation Channel A) | GgTRIC-A is the Chicken BEST1 Bestrophin-1 Ca2+-activated Cl- channel (Gallus ga |
| protein | proteins/voltage-gated-channels/girk1-cytoplasmic-pore/ | GIRK1 Cytoplasmic Pore (G Protein-Gated Inward Rectifier K+ Channel) | The G Rh Protein from Nitrosomonas europaea from Nitrosomonas europaea-Gated-Por |
| protein | proteins/voltage-gated-channels/girk2-kir3-2/ | Mouse GIRK2 (Kir3.2) G Protein-Gated Inward Rectifier K+ Channel | GIRK2 (Kir3.2) is a G Rh Protein from Nitrosomonas europaea from Nitrosomonas eu |
| protein | proteins/voltage-gated-channels/gsuk/ | GsuK Multi-Ligand Gated K+ Channel | GsuK is a two-transmembrane, RCK-regulated K+ channel from *Geobacter sulfurredu |
| protein | proteins/voltage-gated-channels/hslo3/ | Human SLO3 (hSLO3) pH- and Voltage-Gated Potassium Channel | hSLO3 (KCNU1) is a pH- and voltage-gated potassium channel from the SLO family,  |
| protein | proteins/voltage-gated-channels/hstpc2/ | HsTPC2 - Human Two-pore Channel 2 | HsTPC2 (Human Two-pore Channel 2) is an endo/lysosomal cation channel belonging  |
| protein | proteins/voltage-gated-channels/human-bk-channel-slo1/ | Human BK Channel (Slo1) | The BK (Slo1) channel is a high-conductance voltage- and Ca2+-activated K+ chann |
| protein | proteins/voltage-gated-channels/human-connexin-26-gap-junction-channel/ | Human Connexin 26 (Cx26/GJB2) Gap Junction Channel | Connexin 26 (Cx26, also known as GJB2) is a member of the connexin family of gap |
| protein | proteins/voltage-gated-channels/human-k2p1-twik-1/ | Human K2P1 (TWIK-1) Potassium Channel | Human K2P1 (also known as TWIK-1, encoded by KCNK1) is a two-pore domain potassi |
| protein | proteins/voltage-gated-channels/human-task-1-k2p3-1/ | Human TASK-1 (K2P 3.1) Potassium Channel | TWIK-related acid-sensitive potassium (TASK) channels (K2P 3.1/KCNK3) are
| protein | proteins/voltage-gated-channels/k2p-2-1-trek-1/ | K2P 2.1 (TREK-1) Potassium Channel | K2P 2.1 (also known as TREK-1, encoded by KCNK2) is a polymodal thermo- and mech |
| protein | proteins/voltage-gated-channels/k2p2-1/ | Human K2P2.1 (TREK-1) Potassium Channel I110D Mutant | K2P2.1 (TREK-1, KCNK2) is a two-pore domain potassium channel from the K2P chann |
| protein | proteins/voltage-gated-channels/kcsa/ | KcsA Potassium Channel | KcsA is a prokaryotic potassium channel from Streptomyces lividans that serves a |
| protein | proteins/voltage-gated-channels/kir2-2-channel/ | Chicken Kir2.2 Inward Rectifier K+ Channel | Chicken Kir2.2 (cKir2.2) is a classical inward rectifier potassium channel whose |
| protein | proteins/voltage-gated-channels/kir3-1-kirbac1-3-chimera/ | Kir3.1-KirBac1.3 Chimeric GIRK Channel | The Kir3.1 (GIRK1) K+ channel is a G-protein-gated inward rectifier that partici |
| protein | proteins/voltage-gated-channels/kirbac-potassium-channels/ | KirBac Potassium Channels | KirBac1.1 and KirBac3.1 are prokaryotic inward-rectifier potassium channels from |
| protein | proteins/voltage-gated-channels/kv1-2-2-1-2m-channel/ | Kv1.2-2.1-2m Chimeric Channel (W362F, S367T) | The Kv1.2-2.1-2m channel is a double mutant (W362F, S367T) of the Kv1.2-2.1 chim |
| protein | proteins/voltage-gated-channels/kv1-2-2-1-3m-channel/ | Kv1.2-2.1-3m Chimeric Channel (C-type Inactivated State) | The Kv1.2-2.1-3m channel is a triple mutant (W362F, S367T, V377T) of the Kv1.2-2 |
| protein | proteins/voltage-gated-channels/kv1-2-2-1-v406w/ | Kv1.2-2.1 Chimeric Channel V406W (C-type Inactivation Mutant) | The Kv1.2-2.1 chimeric channel is a mammalian voltage-gated K+ channel construct |
| protein | proteins/voltage-gated-channels/kvap/ | KvAP Voltage-Dependent Potassium Channel | KvAP is a voltage-dependent potassium channel from the thermophilic archaebacter |
| protein | proteins/voltage-gated-channels/kvlm-pore-module/ | KvLm Pore Module (Voltage-Gated K+ Channel Pore from Listeria monocytogenes) | The KvLm pore module (PM) is a sensorless pore module dissected from the KvLm vo |
| protein | proteins/voltage-gated-channels/ma-mscl/ | MaMscL (Methanosarcina acetivorans Mechanosensitive Channel of Large Conductance) | [MSCL](/xray-mp-wiki/proteins/other-ion-channels/mscl/) (mechanosensitive channe |
| protein | proteins/voltage-gated-channels/mhv1cc/ | mHv1cc Mouse Voltage-Gated Proton Channel | mHv1cc is a crystallizable construct of the mouse voltage-gated proton channel ( |
| protein | proteins/voltage-gated-channels/mitochondrial-calcium-uniporter-mcu/ | Mitochondrial Calcium Uniporter (MCU) | The mitochondrial calcium uniporter (MCU) is the pore-forming subunit of the mit |
| protein | proteins/voltage-gated-channels/mlotik1/ | MlotiK1 (Mesorhizobium loti Cyclic Nucleotide-Regulated Potassium Channel) | MlotiK1 is a bacterial cyclic nucleotide-regulated potassium channel from Mesorh |
| protein | proteins/voltage-gated-channels/mscs-a106v/ | E. coli MscS Mechanosensitive Channel (A106V Open Form) | The structure of an open form of the *Escherichia coli* mechanosensitive channel |
| protein | proteins/voltage-gated-channels/mscs/ | E. coli MscS (Mechanosensitive Channel of Small Conductance) | MscS (mechanosensitive channel of small conductance) is a mechanosensitive ion c |
| protein | proteins/voltage-gated-channels/mt-tmem175/ | MtTMEM175 K+ channel from Marivirga tractuosa | TMEM175 is a family of non-canonical K⁺ channels found in animals, eubacteria,
| protein | proteins/voltage-gated-channels/mthk/ | MthK (Methanobacterium thermoautotrophicum K+ Channel) | MthK is a calcium-gated potassium channel from the archaeon Methanobacterium the |
| protein | proteins/voltage-gated-channels/nachbac/ | NaChBac Bacterial Voltage-Gated Sodium Channel | [NaChBac](/xray-mp-wiki/proteins/nachbac/) is a bacterial voltage-gated sodium c |
| protein | proteins/voltage-gated-channels/nak-channel/ | NaK Channel from Bacillus cereus | NaK is a non-selective tetrameric cation channel from Bacillus cereus that condu |
| protein | proteins/voltage-gated-channels/nav1-4-cterm-cam/ | Human Naᵥ1.4 C-Terminal Domain in Complex with Calmodulin | Voltage-gated sodium channels Naᵥ1.4 (skeletal muscle) and Naᵥ1.5 (cardiac) are  |
| protein | proteins/voltage-gated-channels/nav1-7/ | Human Nav1.7 Voltage-Gated Sodium Channel | Nav1.7 (encoded by SCN9A) is a voltage-gated sodium channel isoform highly expre |
| protein | proteins/voltage-gated-channels/navab/ | NavAb Bacterial Voltage-Gated Sodium Channel | NavAb is a bacterial voltage-gated sodium channel (BacNav) from Arcobacter butzl |
| protein | proteins/voltage-gated-channels/navms/ | NavMs Sodium Channel | NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus mar |
| protein | proteins/voltage-gated-channels/navms/ | NavMs Sodium Channel | NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus mar |
| protein | proteins/voltage-gated-channels/navms/ | NavMs Sodium Channel | NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus mar |
| protein | proteins/voltage-gated-channels/navms/ | NavMs Sodium Channel | NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus mar |
| protein | proteins/voltage-gated-channels/navms/ | NavMs Sodium Channel | NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus mar |
| protein | proteins/voltage-gated-channels/navms/ | NavMs Sodium Channel | NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus mar |
| protein | proteins/voltage-gated-channels/navms/ | NavMs Sodium Channel | NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus mar |
| protein | proteins/voltage-gated-channels/navms/ | NavMs Sodium Channel | NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus mar |
| protein | proteins/voltage-gated-channels/navms/ | NavMs Sodium Channel | NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus mar |
| protein | proteins/voltage-gated-channels/navms/ | NavMs Sodium Channel | NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus mar |
| protein | proteins/voltage-gated-channels/navms/ | NavMs Sodium Channel | NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus mar |
| protein | proteins/voltage-gated-channels/navms/ | NavMs Sodium Channel | NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus mar |
| protein | proteins/voltage-gated-channels/navms/ | NavMs Sodium Channel | NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus mar |
| protein | proteins/voltage-gated-channels/navms/ | NavMs Sodium Channel | NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus mar |
| protein | proteins/voltage-gated-channels/navms/ | NavMs Sodium Channel | NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus mar |
| protein | proteins/voltage-gated-channels/navrh/ | NavRh (NaChBac Orthologue from HIMB114) | NavRh is a bacterial voltage-gated sodium channel from the marine alphaproteobac |
| protein | proteins/voltage-gated-channels/navsulp/ | NavSulP (Sulfitobacter pontiacus Voltage-Gated Sodium Channel) | NavSulP is a prokaryotic voltage-gated sodium channel (NavBac) cloned from
| protein | proteins/voltage-gated-channels/paddle-chimaera-channel/ | Paddle-Chimaera Voltage-Dependent Potassium Channel | The paddle-chimaera channel is a chimeric voltage-dependent K+ (Kv) channel cons |
| protein | proteins/voltage-gated-channels/ptr-chimera/ | Engineered Paddle-Chimera Voltage-Gated Potassium Channel | The Paddle-Chimera (PTR) is an engineered voltage-gated potassium channel create |
| protein | proteins/voltage-gated-channels/ry1-repeat12/ | Rabbit RyR1 Repeat12 Domain | The Repeat12 domain of rabbit Ryanodine Receptor Type 1 (RyR1), spanning residue |
| protein | proteins/voltage-gated-channels/ry1/ | Ryanodine Receptor Type 1 (RyR1) | Ryanodine receptor type 1 (RyR1) is the calcium release channel isoform primaril |
| protein | proteins/voltage-gated-channels/ry2-spry1/ | Mouse RyR2 SPRY1 Domain | The SPRY1 domain of mouse Ryanodine Receptor Type 2 (RyR2), spanning residues 65 |
| protein | proteins/voltage-gated-channels/ry2/ | Ryanodine Receptor Type 2 (RyR2) | Ryanodine receptor type 2 (RyR2) is the calcium release channel isoform primaril |
| protein | proteins/voltage-gated-channels/ry3/ | Ryanodine Receptor Type 3 (RyR3) | [Ryanodine Receptor (RyR)](/xray-mp-wiki/proteins/voltage-gated-channels/ryanodi |
| protein | proteins/voltage-gated-channels/ryanodine-receptor/ | Ryanodine Receptor (RyR) | Ryanodine receptors (RyRs) are large (~2.2 MDa) calcium release channels located |
| protein | proteins/voltage-gated-channels/sa-mscl/ | Staphylococcus aureus MscL (Mechanosensitive Channel of Large Conductance) | SaMscL is the mechanosensitive channel of large conductance from Staphylococcus  |
| protein | proteins/voltage-gated-channels/sa-tric/ | SaTRIC Channel from Sulfolobus acidocaldarius | SaTRIC is a Trimeric Intracellular Cation (TRIC) channel from the archaeon Sulfo |
| protein | proteins/voltage-gated-channels/shaker-kv1-2/ | Shaker Kv1.2 Potassium Channel | Kv1.2 is a voltage-dependent potassium channel from Rattus norvegicus belonging  |
| protein | proteins/voltage-gated-channels/spoiiq-spoiiah-complex/ | SpoIIQ-SpoIIIAH Intercellular Channel Complex from Bacillus subtilis | The SpoIIQ-SpoIIIAH complex is an intercellular channel formed between the fores |
| protein | proteins/voltage-gated-channels/traak/ | Human TRAAK Potassium Channel | TRAAK (tandem pore domain potassium channel 4, KCNK4) is a mechanosensitive two- |
| protein | proteins/voltage-gated-channels/trek-2/ | Human TREK-2 Potassium Channel (KCNK10) | TREK-2 (KCNK10) is a member of the Two-Pore Domain (K2P) potassium
| protein | proteins/voltage-gated-channels/tric-b1/ | C. elegans TRIC-B1 Channel | TRIC-B1 is an intracellular cation channel from Caenorhabditis elegans belonging |
| protein | proteins/voltage-gated-channels/tric-b2/ | C. elegans TRIC-B2 Channel | TRIC-B2 is an intracellular cation channel from Caenorhabditis elegans belonging |
| protein | proteins/voltage-gated-channels/tric-channel/ | Prokaryotic TRIC Trimeric Intracellular Cation Channels | TRIC (trimeric intracellular cation) channels are monovalent cation channels loc |
| protein | proteins/voltage-gated-channels/trpml1/ | Human TRPML1 (Mucolipin-1) - Luminal Domain | Human TRPML1 is a Ca2+-release channel primarily located in lysosomes, belonging |
| protein | proteins/voltage-gated-channels/trpv2/ | Transient Receptor Potential Vanilloid 2 (TRPV2) | TRPV2 is a transient receptor potential vanilloid channel belonging to the TRPV  |
| protein | proteins/voltage-gated-channels/trpv5/ | Epithelial Calcium Channel TRPV5 | TRPV5 is a Ca²⁺-selective transient receptor potential vanilloid channel that, t |
| protein | proteins/voltage-gated-channels/trpv6/ | Epithelial Calcium Channel TRPV6 | TRPV6 is a Ca2+-selective transient receptor potential vanilloid channel uniquel |
| protein | proteins/voltage-gated-channels/xtric-b/ | XTRIC-B (Xenopus TRIC-B Channel) | XTRIC-B is the Xenopus tropicalis ortholog of the TRIC-B subtype of trimeric int |
| reagent | reagents/additives/1,4-butanediol/ | 1,4-Butanediol | 1,4-Butanediol is a linear diol used as a crystallization precipitant and additi |
| reagent | reagents/additives/1-6-hexanediol/ | 1,6-Hexanediol | 1,6-Hexanediol is a linear six-carbon diol used as a crystallization additive in |
| reagent | reagents/additives/2,6-di-t-butyl-p-cresol/ | 2,6-di-t-butyl-p-cresol | 2,6-di-t-butyl-p-cresol (2,6-di-t-BPC, BPC) is an antioxidant and preservative u |
| reagent | reagents/additives/5-iodo-a-85380/ | 5-Iodo-A-85380 | 5-Iodo-A-85380 is a potent agonist ligand selective for the alpha4beta2 subtype  |
| reagent | reagents/additives/acetazolamide/ | Acetazolamide | Acetazolamide is a carbonic anhydrase inhibitor reported as an AQP4 inhibitor. I |
| reagent | reagents/additives/agitoxin-2/ | Agitoxin-2 (AgTx2) | Agitoxin-2 (AgTx2) is a scorpion toxin from Leiurus quinquestriatus hebraeus tha |
| reagent | reagents/additives/ammonium-chloride/ | Ammonium Chloride | Ammonium chloride is an inorganic salt used as a crystallization precipitant for |
| reagent | reagents/additives/ammonium-formate/ | Ammonium Formate | Ammonium formate is a volatile salt used as a crystallization additive to improv |
| reagent | reagents/additives/ammonium-sulfate/ | Ammonium Sulfate | Ammonium sulfate is a common precipitant used in protein crystallization and pur |
| reagent | reagents/additives/ammonium-tartrate/ | Ammonium Tartrate | Ammonium tartrate is a salt of tartaric acid and ammonia used as a crystallizati |
| reagent | reagents/additives/aurachin-c/ | Aurachin C | Aurachin C is a quinone analogue that acts as a potent competitive inhibitor of  |
| reagent | reagents/additives/aurovertin-b/ | Aurovertin B | Aurovertin B is a polyketide antibiotic from the fungus Calcarisporium arbuscula |
| reagent | reagents/additives/bapta/ | BAPTA (1,2-Bis(o-aminophenoxy)ethane-N,N,N,N,-tetraacetic Acid) | BAPTA (1,2-bis(o-aminophenoxy)ethane-N,N,N,N-tetraacetic acid) is a calcium-sele |
| reagent | reagents/additives/barium-chloride/ | Barium Chloride | Barium chloride (BaCl2) is an inorganic salt that dissociates into Ba2+ ions in  |
| reagent | reagents/additives/beta-mercaptoethanol/ | beta-Mercaptoethanol | beta-Mercaptoethanol (2-mercaptoethanol) is a small thiol-containing reducing ag |
| reagent | reagents/additives/bodipy/ | BODIPY Fluorophore | BODIPY (boron-dipyromethene) is a fluorescent dye used for labeling molecules fo |
| reagent | reagents/additives/cadmium-chloride/ | Cadmium Chloride | Cadmium chloride (CdCl2) is an inorganic salt that provides cadmium ions (Cd2+)  |
| reagent | reagents/additives/calcium-acetate/ | Calcium Acetate | Calcium acetate is a calcium salt used as a crystallization additive and buffer  |
| reagent | reagents/additives/calcium-chloride/ | Calcium Chloride (CaCl2) | Calcium chloride (CaCl2) is an inorganic salt commonly used in membrane protein  |
| reagent | reagents/additives/capuramycin/ | Capuramycin | Capuramycin is a nucleoside natural product that inhibits bacterial MraY
| reagent | reagents/additives/cbfs/ | CBFS (8-(chloromercuri)-2-dibenzofuransulfonic acid) | CBFS (8-(chloromercuri)-2-dibenzofuransulfonic acid) is a mercurial compound use |
| reagent | reagents/additives/cellobiose/ | Cellobiose | Cellobiose is a disaccharide composed of two [Glucose](/xray-mp-wiki/reagents/ad |
| reagent | reagents/additives/cesium-chloride/ | Cesium Chloride | Cesium chloride (CsCl) is an inorganic salt that provides cesium ions (Cs+) used |
| reagent | reagents/additives/cobalt-hexamine/ | Hexaamminecobalt(III) (Cobalt Hexamine) | Hexaamminecobalt(III) chloride, commonly known as cobalt hexamine or Co(NH3)6 3+ |
| reagent | reagents/additives/dccd/ | N,N'-Dicyclohexylcarbodiimide (DCCD) | DCCD (N,N'-dicyclohexylcarbodiimide) is a carboxyl-modifying reagent that covale |
| reagent | reagents/additives/decavanadate/ | Decavanadate | Decavanadate (V10O28 6-) is a polyvanadate anion consisting of ten vanadium atom |
| reagent | reagents/additives/decylubiquinone/ | Decylubiquinone | Decylubiquinone is a water-soluble [Ubiquinone](/xray-mp-wiki/reagents/cofactors |
| reagent | reagents/additives/deoxycholate/ | Deoxycholate (DXC) | Deoxycholate (DXC), or sodium deoxycholate, is a bile salt with anionic detergen |
| reagent | reagents/additives/dioxane/ | Dioxane | Dioxane (1,4-dioxane) is a cyclic ether used as a cryoprotectant and organic sol |
| reagent | reagents/additives/dmapp/ | Dimethylallyl Diphosphate (DMAPP) | Dimethylallyl diphosphate (DMAPP) is a C5 isoprenoid compound that serves as the |
| reagent | reagents/additives/dtt/ | Dithiothreitol (DTT) | Dithiothreitol (DTT, also known as Cleland's reagent) is a strong reducing agent |
| reagent | reagents/additives/dysprosium-chloride/ | Dysprosium Chloride | Dysprosium(III) chloride is a heavy atom compound used for single-wavelength ano |
| reagent | reagents/additives/edta/ | Ethylenediaminetetraacetic Acid (EDTA) | Ethylenediaminetetraacetic acid (EDTA) is a hexadentate chelating agent that bin |
| reagent | reagents/additives/egta/ | EGTA (Ethylene Glycol Tetraacetic Acid) | EGTA ([Ethylene Glycol](/xray-mp-wiki/reagents/additives/ethylene-glycol/) tetra |
| reagent | reagents/additives/endoh/ | Endoglycosidase H (EndoH) | Endoglycosidase H (EndoH) is a glycosidase enzyme that cleaves high-mannose and  |
| reagent | reagents/additives/epibatidine/ | Epibatidine | Epibatidine is a potent alkaloid ligand that binds to nicotinic [Acetylcholine]( |
| reagent | reagents/additives/ethyl-mercury-thiosalicylate/ | Ethyl Mercury Thiosalicylate EMTS Heavy Metal Derivative | Ethyl [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/m |
| reagent | reagents/additives/ethylene-glycol/ | Ethylene Glycol | Ethylene glycol (ethane-1,2-diol) is a small polyol compound used as a cryoprote |
| reagent | reagents/additives/flavin-adenine-dinucleotide/ | Flavin Adenine Dinucleotide (FAD) | Flavin adenine dinucleotide (FAD) is a redox cofactor derived from [Riboflavin ( |
| reagent | reagents/additives/g418/ | G418 (Geneticin) | G418 (geneticin) is an aminoglycoside antibiotic used as a selection agent in eu |
| reagent | reagents/additives/gadolinium-chloride/ | Gadolinium Chloride (GdCl3) | Gadolinium chloride (GdCl3) is a lanthanide salt that dissociates into Gd3+ ions |
| reagent | reagents/additives/glucose/ | Glucose | Glucose is a monosaccharide (simple sugar) that serves as a control compound in  |
| reagent | reagents/additives/glutathione/ | Glutathione (GSH) | Glutathione (gamma-L-glutamyl-L-cysteinylglycine, GSH) is a tripeptide thiol tha |
| reagent | reagents/additives/glycerol-3-phosphate/ | Glycerol 3-Phosphate | [Glycerol](/xray-mp-wiki/reagents/additives/glycerol/) 3-phosphate (G3P) is a ph |
| reagent | reagents/additives/glycerol/ | Glycerol | Glycerol (propane-1,2,3-triol) is a small polyol widely used as a cryoprotectant |
| reagent | reagents/additives/glycylglycylglycine/ | Glycylglycylglycine (Gly3) | Glycylglycylglycine (Gly3, Gly-Gly-Gly) is a tripeptide composed of three [Glyci |
| reagent | reagents/additives/gold-iii-chloride/ | Gold(III) Chloride | Gold(III) chloride (AuCl3) is an inorganic salt that provides gold ions (Au3+) u |
| reagent | reagents/additives/gpp/ | Geranyl Diphosphate (GPP) | Geranyl diphosphate (GPP) is a C10 isoprenoid compound consisting of two isopren |
| reagent | reagents/additives/guanidine-hydrochloride/ | Guanidine Hydrochloride | Guanidine hydrochloride is a strong chaotropic agent used to chemically denature |
| reagent | reagents/additives/h2dids/ | H2DIDS (4,4-Diisothiocyanatodihydro-stilbene-2,2-disulfonic acid) | H2DIDS (4,4-diisothiocyanatodihydro-stilbene-2,2-disulfonic acid) is a disulfoni |
| reagent | reagents/additives/had13a/ | HAD13a (Heavy-Atom Additive 13a) | HAD13a (heavy-atom additive 13a) is an iodine-labeled detergent composed of
| reagent | reagents/additives/hiload-sp-sepharose/ | Hiload SP Sepharose Ion Exchange Resin | Hiload SP Sepharose is a strong cation exchange chromatography resin from GE Hea |
| reagent | reagents/additives/hoechst-33342/ | Hoechst 33342 | Hoechst 33342 is a fluorescent DNA-binding dye that also serves as a
| reagent | reagents/additives/hrv-3c-protease/ | HRV 3C Protease | HRV 3C protease (Human Rhinovirus 3C protease) is a cysteine protease that speci |
| reagent | reagents/additives/imidazole/ | Imidazole | Imidazole is a heterocyclic organic compound commonly used in protein
| reagent | reagents/additives/iodoacetamide/ | Iodoacetamide | Iodoacetamide is an alkylating agent that specifically modifies cysteine residue |
| reagent | reagents/additives/iohexol/ | Iohexol (Histodenz) | Iohexol (trade name Histodenz, also known as Nycodenz) is a non-ionic, iodinated |
| reagent | reagents/additives/iptg/ | IPTG (Isopropyl-beta-D-thiogalactopyranoside) | Isopropyl-beta-D-thiogalactopyranoside ([IPTG](/xray-mp-wiki/reagents/additives/ |
| reagent | reagents/additives/iron/ | Iron (Fe) | Iron is a transition metal that serves as a cofactor in many membrane proteins i |
| reagent | reagents/additives/isopropyl-beta-d-thiogalactoside/ | Isopropyl beta-D-1-Thiogalactopyranoside (IPTG) | Isopropyl beta-D-1-thiogalactopyranoside (IPTG) is a non-hydrolyzable analog of  |
| reagent | reagents/additives/jeffamine-ed-2001/ | Jeffamine ED-2001 Polyalkylene Glycol | Jeffamine ED-2001 is a branched polyalkylene glycol used as a crystallization pr |
| reagent | reagents/additives/jeffamine-m-600/ | Jeffamine M-600 | Jeffamine M-600 is a polyether amine (polyoxyalkyleneamine) used as a precipitan |
| reagent | reagents/additives/jeffamine-m600/ | Jeffamine M600 | Jeffamine M600 is a branched polyamine copolymer used as a crystallization preci |
| reagent | reagents/additives/kanamycin/ | Kanamycin | Kanamycin is an aminoglycoside antibiotic used as a selection agent in bacterial |
| reagent | reagents/additives/lithium-citrate/ | Lithium Citrate | Lithium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate |
| reagent | reagents/additives/lithium-ion/ | Lithium Ion (Li+) | Lithium ion (Li+) is a coupling cation for the melibiose permease (MelB), which  |
| reagent | reagents/additives/lithium-sulfate/ | Lithium Sulfate | Lithium sulfate is an inorganic salt used as a crystallization additive and prec |
| reagent | reagents/additives/lutetium-acetate/ | Lutetium Acetate | Lutetium(III) acetate is a heavy atom compound used for single-wavelength anomal |
| reagent | reagents/additives/m2m/ | M2M (Bis-(3-Sulfanylpropionyl)disulfide, 2-Carbon Linker MTS Reagent) | M2M is a bifunctional maleimide thiosulfonate (MTS) reagent with a 2-carbon link |
| reagent | reagents/additives/m4m/ | M4M (Bis-(3-Sulfanylpropionyl)disulfide, 4-Carbon Linker MTS Reagent) | M4M is a bifunctional maleimide reagent (MTS: monobromobimane thiosulfonate) wit |
| reagent | reagents/additives/m8m/ | M8M (Bis-(3-Sulfanylpropionyl)disulfide, 8-Carbon Linker MTS Reagent) | M8M is a bifunctional maleimide thiosulfonate (MTS) reagent with an 8-carbon lin |
| reagent | reagents/additives/magnesium-chloride/ | Magnesium Chloride | Magnesium chloride (MgCl2) is a metal salt commonly used in protein crystallizat |
| reagent | reagents/additives/magnesium-sulfate/ | Magnesium Sulfate (MgSO4) | Magnesium sulfate (MgSO4) is an inorganic salt used as a source of magnesium ion |
| reagent | reagents/additives/magnesium-tetrafluoride/ | Magnesium Tetrafluoride (MgF₄²⁻) | Magnesium tetrafluoride (MgF₄²⁻) is a phosphate analogue used to trap P-type ATP |
| reagent | reagents/additives/maltose/ | Maltose | Maltose is a disaccharide composed of two glucose units linked by an alpha-1,4 g |
| reagent | reagents/additives/mercury/ | Mercury (HgCl2) - Aquaporin Inhibitor | [Mercury (HgCl2) - Aquaporin Inhibitor](/xray-mp-wiki/reagents/additives/mercury |
| reagent | reagents/additives/methanol/ | Methanol | Methanol is the primary carbon source and inducer for the AOX1 (alcohol oxidase  |
| reagent | reagents/additives/methylmercury-chloride/ | Methylmercury Chloride | Methylmercury chloride (CH3HgCl) is a mercury-containing heavy metal derivative  |
| reagent | reagents/additives/milnacipran/ | Milnacipran | Milnacipran is a serotonin-norepinephrine reuptake inhibitor (SNRI) with an unco |
| reagent | reagents/additives/mpd/ | 2-Methyl-2,4-pentanediol (MPD) | 2-Methyl-2,4-pentanediol (MPD) is a low-viscosity organic compound commonly used |
| reagent | reagents/additives/mtset/ | MTSET ((2-trimethylammonium)ethyl methanethiosulfonate) | MTSET (2-trimethylammonium)ethyl methanethiosulfonate) is a positively charged,  |
| reagent | reagents/additives/muraymycin-d2/ | Muraymycin D2 (MD2) | Muraymycin D2 (MD2) is a naturally occurring nucleoside antibiotic that
| reagent | reagents/additives/n-methyl-d-glucamine/ | N-Methyl-D-Glucamine (NMG) | N-Methyl-D-glucamine (NMG) is an organic compound used as an ion substitute in i |
| reagent | reagents/additives/nickel-nta/ | Ni-NTA Agarose Resin | Ni-NTA (Nickel-Nitrilotriacetic acid) agarose resin is a chromatography medium c |
| reagent | reagents/additives/nickel-sulfate/ | Nickel Sulfate (NiSO₄) | Nickel sulfate is an inorganic salt used in membrane protein crystallography, pa |
| reagent | reagents/additives/norfluoxetine/ | Norfluoxetine | Norfluoxetine is the major active metabolite of the antidepressant
| reagent | reagents/additives/peg-1450/ | Polyethylene Glycol 1450 (PEG 1450) | Polyethylene glycol 1450 (PEG 1450) is a medium molecular weight polyethylene gl |
| reagent | reagents/additives/peg-350-mme/ | Polyethylene Glycol 350 Monomethyl Ether (PEG 350 MME) | Polyethylene glycol 350 monomethyl ether ([PEG](/xray-mp-wiki/reagents/additives |
| reagent | reagents/additives/peg-400/ | Polyethylene Glycol 400 (PEG 400) | Polyethylene glycol 400 (PEG 400) is a water-soluble polymer with an average mol |
| reagent | reagents/additives/peg-4000/ | PEG 4000 (Polyethylene Glycol 4000) | [PEG](/xray-mp-wiki/reagents/additives/peg/) 4000 (polyethylene glycol with mole |
| reagent | reagents/additives/peg-5000-mme/ | Polyethylene Glycol 5000 Monomethyl Ether (PEG 5000 MME) | Polyethylene glycol 5000 monomethyl ether (PEG 5000 MME) is a high molecular wei |
| reagent | reagents/additives/peg-550mme/ | PEG 550MME (Polyethylene Glycol 550 Monomethyl Ether) | [PEG](/xray-mp-wiki/reagents/additives/peg/) 550MME (polyethylene glycol 550 mon |
| reagent | reagents/additives/peg-600/ | PEG 600 | [PEG 600](/xray-mp-wiki/reagents/additives/peg-600/) (polyethylene glycol with m |
| reagent | reagents/additives/peg-6000/ | PEG 6000 (Polyethylene Glycol 6000) | [PEG](/xray-mp-wiki/reagents/additives/peg/) 6000 (polyethylene glycol with mole |
| reagent | reagents/additives/peg-8000/ | Polyethylene Glycol 8000 (PEG 8000) | Polyethylene Glycol 8000 (PEG 8000) is a high-molecular-weight polymer commonly  |
| reagent | reagents/additives/peg/ | PEG (Polyethylene Glycol) | Polyethylene glycol (PEG) is a water-soluble polymer used as a linker in conjuga |
| reagent | reagents/additives/peg200/ | Polyethylene Glycol 200 (PEG200) | Polyethylene glycol 200 (PEG200) is a low-molecular-weight [PEG](/xray-mp-wiki/r |
| reagent | reagents/additives/peg2000/ | PEG 2000 | Polyethylene glycol with an average molecular weight of 2,000 Da ([PEG](/xray-mp |
| reagent | reagents/additives/peg300/ | Polyethylene Glycol 300 (PEG300) | Polyethylene glycol 300 (PEG300) is a low molecular weight polyethylene glycol u |
| reagent | reagents/additives/peg3000/ | PEG 3000 | Polyethylene glycol 3000 (PEG 3000) is a precipitating agent used in protein cry |
| reagent | reagents/additives/peg6000/ | Polyethylene Glycol 6000 (PEG6000) | Polyethylene glycol 6000 (PEG6000) is a water-soluble polymer used as a precipit |
| reagent | reagents/additives/platinum-ii-chloride/ | Platinum(II) Chloride | Platinum(II) chloride (PtCl2) is an inorganic salt that provides platinum ions ( |
| reagent | reagents/additives/pmsf/ | PMSF (Phenylmethylsulfonyl Fluoride) | PMSF is a serine protease inhibitor commonly used during protein purification to |
| reagent | reagents/additives/pngase-f/ | Peptide:N-Glycosidase F (PNGase F) | Peptide:N-glycosidase F (PNGase F) is a glycosidase enzyme that cleaves all type |
| reagent | reagents/additives/polyethylene-glycol-4000/ | Polyethylene Glycol 4000 (PEG 4000) | Polyethylene glycol 4000 (PEG 4000) is a common polymeric precipitant used in pr |
| reagent | reagents/additives/potassium-acetate/ | Potassium acetate | Potassium acetate (CH₃COOK) is a potassium salt used as a crystallization additi |
| reagent | reagents/additives/potassium-chloride-kcl/ | Potassium Chloride (KCl) | Potassium chloride (KCl) is a common inorganic salt used in protein biochemistry |
| reagent | reagents/additives/potassium-ferricyanide/ | Potassium Ferricyanide | Potassium ferricyanide (K3[Fe(CN)6]) is an oxidizing agent used as an artificial |
| reagent | reagents/additives/potassium-fluoride/ | Potassium Fluoride (KF) | Potassium fluoride is a salt used as a crystallization additive in membrane prot |
| reagent | reagents/additives/potassium-formate/ | Potassium Formate | Potassium formate (HCOOK) is a small organic salt used as a precipitating agent  |
| reagent | reagents/additives/potassium-tetrakis-hydroxido-platinate-ii/ | Potassium Tetrakis(Hydroxido)platinate(II) K2Pt(NO2)4 Heavy Metal Derivative | Potassium tetrakis(hydroxido)platinate(II), K2Pt(NO2)4, is a heavy metal derivat |
| reagent | reagents/additives/pre-scission-protease/ | PreScission Protease | PreScission protease is a genetically engineered fusion of Human Rhinovirus 3C p |
| reagent | reagents/additives/pre084/ | PRE084 | PRE084 is a high-affinity sigma-1 receptor (S1R) ligand used to study the ligand |
| reagent | reagents/additives/retosiban/ | Retosiban | Retosiban is a potent, nonpeptidic antagonist of the human oxytocin receptor (OT |
| reagent | reagents/additives/rizatriptan/ | Rizatriptan | Rizatriptan is a [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/reagents/ |
| reagent | reagents/additives/rubidium-acetate/ | Rubidium acetate | Rubidium acetate (RbCH₃COO) is a Rb⁺ salt used as a K⁺ congener for crystallogra |
| reagent | reagents/additives/s-cys-gly-3m3sh-malodour-precursor/ | S-Cys-Gly-3M3SH (Malodour Precursor Peptide) | S-Cys-Gly-3M3SH (S-[1-(2-hydroxyethyl)-1-methylbutyl]-L-cysteinylglycine) is the |
| reagent | reagents/additives/s1ra/ | S1RA (4-[2-(5-methyl-1-(naphthalene-2-yl)-1H-pyrazol-3-yl)oxy]ethyl]morpholine) | S1RA is a sigma-1 receptor ligand purchased from Topscience Co. Ltd. It was used |
| reagent | reagents/additives/sa47/ | SA47 | SA47 is a potent exofacial inhibitor of human [Glucose](/xray-mp-wiki/reagents/a |
| reagent | reagents/additives/selenomethionine/ | Selenomethionine (SeMet) | Selenomethionine (SeMet) is a selenium-containing analog of the amino acid methi |
| reagent | reagents/additives/sodium-bicarbonate/ | Sodium Bicarbonate (NaHCO3) | Sodium bicarbonate (NaHCO3) is an inorganic salt that serves as a pH buffer and  |
| reagent | reagents/additives/sodium-butyrate/ | Sodium Butyrate | Sodium butyrate is the sodium salt of butyric acid (a four-carbon carboxylic aci |
| reagent | reagents/additives/sodium-chloride/ | Sodium Chloride | Sodium chloride is a common inorganic salt used in protein biochemistry and crys |
| reagent | reagents/additives/sodium-cyanoborohydride/ | Sodium Cyanoborohydride | Sodium cyanoborohydride (NaBH3CN) is a reducing agent used in the reductive meth |
| reagent | reagents/additives/sodium-ethylmercurithiosalicylate/ | Sodium Ethylmercurithiosalicylate | Sodium ethylmercurithiosalicylate (also referred to as ethylmercurithiosalicylic |
| reagent | reagents/additives/sodium-malonate/ | Sodium Malonate | Sodium malonate is a dicarboxylic acid salt used as a crystallization additive a |
| reagent | reagents/additives/sodium-sulfite/ | Sodium Sulfite (Na2SO3) | Sodium sulfite (Na2SO3) is an inorganic salt that provides sulfite ions (SO3 2-) |
| reagent | reagents/additives/sodium-thiocyanate/ | Sodium Thiocyanate (NaSCN) | Sodium thiocyanate (NaSCN) is an inorganic salt used as a crystallization additi |
| reagent | reagents/additives/sorbitol/ | Sorbitol | Sorbitol (glucitol) is a sugar alcohol commonly used as an osmotic agent and sta |
| reagent | reagents/additives/spermine/ | Spermine | Spermine is a polyamine used as a crystallization additive in membrane protein c |
| reagent | reagents/additives/superdex-200/ | Superdex 200 Increase SEC Resin | Superdex 200 Increase is a prepacked size-exclusion chromatography (SEC) column  |
| reagent | reagents/additives/sypro-orange/ | SYPRO Orange Fluorescent Dye | SYPRO Orange is a fluorescent dye from Invitrogen used in fluorescence-based the |
| reagent | reagents/additives/talon/ | TALON Cobalt Affinity Resin | TALON cobalt affinity resin is a immobilized metal affinity chromatography (IMAC |
| reagent | reagents/additives/tboa/ | DL-threo-beta-Benzyloxyaspartic Acid (TBOA) | TBOA (DL-threo-beta-Benzyloxyaspartic acid) is a competitive transport blocker o |
| reagent | reagents/additives/tcep/ | Tris(2-carboxyethyl)phosphine (TCEP) | Tris(2-carboxyethyl)phosphine (TCEP) is a water-soluble, strong reducing agent u |
| reagent | reagents/additives/tert-butanol/ | tert-Butanol | tert-Butanol (2-methyl-2-propanol) is a small, branched organic alcohol used as  |
| reagent | reagents/additives/tev-protease/ | TEV Protease (Tobacco Etch Virus Protease) | TEV protease is a highly sequence-specific cysteine protease derived from the To |
| reagent | reagents/additives/thallium-acetate/ | Thallium acetate | Thallium acetate (TlCH₃COO) is a Tl⁺ salt used as a K⁺ congener for crystallogra |
| reagent | reagents/additives/thermolysin/ | Thermolysin | Thermolysin is a thermostable neutral metalloprotease produced by Bacillus therm |
| reagent | reagents/additives/tocopherol/ | Tocopherol (Vitamin E) | Tocopherol (commonly known as vitamin E) is a lipophilic antioxidant that protec |
| reagent | reagents/additives/tramadol/ | Tramadol | Tramadol is a synthetic opioid analgesic that also acts as a norepinephrine reup |
| reagent | reagents/additives/trehalose/ | Trehalose | Trehalose is a non-reducing disaccharide used as a cryoprotectant and crystalliz |
| reagent | reagents/additives/trypsin/ | Trypsin | Trypsin is a serine protease that cleaves peptide bonds at the C-terminal side o |
| reagent | reagents/additives/vercirnon/ | Vercirnon (GSK1605786, CCX282-B) | Vercirnon (GSK1605786, CCX282-B) is a selective small-molecule antagonist of CC  |
| reagent | reagents/additives/vstx1/ | VSTX1 Tarantula Toxin | VSTX1 is a voltage-sensor toxin purified from tarantula venom that specifically  |
| reagent | reagents/additives/zinc-chloride/ | Zinc Chloride | Zinc chloride (ZnCl2) is an inorganic salt that provides zinc ions (Zn2+) used a |
| reagent | reagents/antibiotics/actinomycin-d/ | Actinomycin D | Actinomycin D is a cytotoxic polypeptide antibiotic that intercalates into DNA a |
| reagent | reagents/antibiotics/ampicillin/ | Ampicillin | Ampicillin is a beta-lactam antibiotic that inhibits bacterial cell wall synthes |
| reagent | reagents/antibiotics/chloramphenicol/ | Chloramphenicol | Chloramphenicol (Cm) is a broad-spectrum antibiotic that inhibits bacterial prot |
| reagent | reagents/antibiotics/dicloxacillin/ | Dicloxacillin | Dicloxacillin (DCX) is a beta-lactam antibiotic of the isoxazolyl penicillin cla |
| reagent | reagents/antibiotics/fusidic-acid/ | Fusidic Acid | Fusidic acid (FUA) is a steroid antibiotic that inhibits bacterial protein synth |
| reagent | reagents/antibiotics/isocoumarin/ | Isocoumarin | Isocoumarin is a non-peptidic inhibitor of rhomboid protease [GLPG](/xray-mp-wik |
| reagent | reagents/antibiotics/linezolid/ | Linezolid | Linezolid ((S)-N-{3-[3-fluoro-4-(morpholin-4-yl)phenyl]-2-oxo-1,3-oxazolidin-5-y |
| reagent | reagents/antibiotics/nafcillin/ | Nafcillin | Nafcillin is a beta-lactam antibiotic (penicillinase-resistant penicillin) that  |
| reagent | reagents/antibiotics/oxacillin/ | Oxacillin | Oxacillin (OXA) is a beta-lactam antibiotic of the penicillin class, part of the |
| reagent | reagents/antibiotics/piperacillin/ | Piperacillin | Piperacillin (PIP) is a broad-spectrum beta-lactam antibiotic of the ureidopenic |
| reagent | reagents/antibiotics/tunicamycin/ | Tunicamycin | Tunicamycin is a naturally occurring antibiotic that inhibits phospho-MurNAc-pen |
| reagent | reagents/antibiotics/valganciclovir/ | Valganciclovir | Valganciclovir is an antiviral prodrug consisting of a guanosine analog (gancicl |
| reagent | reagents/antibodies/2b12/ | 2B12 Antibody Fragment | 2B12 is a conformation-specific monoclonal antibody fragment (Fab) that selectiv |
| reagent | reagents/antibodies/6a10/ | 6A10 Antibody Fragment | 6A10 is a conformation-specific monoclonal antibody fragment (Fab) that selectiv |
| reagent | reagents/antibodies/8b6-antibody/ | 8B6 Monoclonal Antibody (SERT-specific) | 8B6 is a monoclonal antibody raised against human [Serotonin (5-Hydroxytryptamin |
| reagent | reagents/antibodies/fab-9d5/ | Fab 9D5 | Fab 9D5 is a monoclonal antibody fragment used as a crystallization aid for memb |
| reagent | reagents/antibodies/fab21/ | Fab21 Antibody Fragment | Fab21 is a monoclonal antibody fragment (Fab) derived from a type-2a IgG raised  |
| reagent | reagents/antibodies/fab2838/ | Fab2838 Antibody Fragment | Fab2838 is a mouse monoclonal antibody Fab fragment raised against the human ade |
| reagent | reagents/antibodies/fab4a03/ | Fab4A03 Antibody Fragment | Fab4A03 is a monoclonal antibody fragment (Fab) that specifically binds the huma |
| reagent | reagents/antibodies/fab5/ | Fab5 Antibody Fragment | Fab5 is a monoclonal antibody fragment (Fab) derived from the Mab5 immunoglobuli |
| reagent | reagents/antibodies/mab3949/ | MAB3949 Monoclonal Antibody (PAR2-specific) | MAB3949 is a commercial monoclonal antibody that binds with high affinity to hum |
| reagent | reagents/antibodies/nanobody-nb80/ | Nanobody Nb80 | Nanobody Nb80 is a conformation-specific camelid single-domain antibody (nanobod |
| reagent | reagents/antibodies/nb-at110i1/ | Nb.AT110i1 Synthetic Nanobody | Nb.AT110i1 is a synthetic conformation-specific nanobody discovered using a yeas |
| reagent | reagents/antibodies/nb-n00/ | N00 Conformation-Selective Nanobody | N00 is a conformation-selective nanobody discovered through immunization of came |
| reagent | reagents/antibodies/nb35/ | Nb35 Nanobody | Nb35 is a conformation-selective nanobody (single-domain antibody fragment deriv |
| reagent | reagents/antibodies/nb9-8/ | Nb9-8 Nanobody | Nb9-8 is a G-protein mimetic camelid [Nanobody](/xray-mp-wiki/reagents/protein-t |
| reagent | reagents/antibodies/scfv16/ | scFv16 Antibody Fragment | scFv16 is a single-chain variable fragment (scFv) antibody used as a stabilizing |
| reagent | reagents/antibodies/srp2070fab/ | SRP2070Fab (Anti-BRIL Antibody Fragment) | SRP2070Fab is a monoclonal antibody fragment raised against the thermostabilized |
| reagent | reagents/antibodies/vhh15/ | VHH15 Nanobody | VHH15 is a llama-derived single-domain antibody (nanobody) that specifically tar |
| reagent | reagents/buffers/aces/ | ACES Buffer (N-(2-Acetamido)iminodiacetic Acid) | ACES (2-[N-(2-Acetamido)iminodiacetic acid]) is a zwitterionic buffering agent c |
| reagent | reagents/buffers/acetate/ | Acetate Buffer (Sodium Acetate) | Acetate buffer, typically prepared from [Sodium Acetate](/xray-mp-wiki/reagents/ |
| reagent | reagents/buffers/ammonium-acetate/ | Ammonium Acetate | Ammonium acetate is a volatile salt commonly used in protein crystallization as  |
| reagent | reagents/buffers/ammonium-phosphate/ | Ammonium Phosphate (Monobasic) | Ammonium phosphate (monobasic) is a commonly used buffer and crystallization pre |
| reagent | reagents/buffers/bicine/ | Bicine Buffer | Bicine (N,N-bis(2-hydroxyethyl)[Glycine](/xray-mp-wiki/reagents/buffers/glycine/ |
| reagent | reagents/buffers/buffer-bis-tris-propane/ | Bis-Tris Propane Buffer | Bis-Tris propane (1,3-bis[tris(hydroxymethyl)methylamino]propane) is a zwitterio |
| reagent | reagents/buffers/buffer-ches/ | CHES Buffer | CHES (N-cyclohexyl-2-aminoethanesulfonic acid) is a zwitterionic buffer with a u |
| reagent | reagents/buffers/buffer-succinate/ | Succinate Buffer | Succinate buffer is a dicarboxylic acid buffering agent with pKa values of 4.2 a |
| reagent | reagents/buffers/cacodylate/ | Cacodylate (Sodium Dimethylarsenate) | Cacodylate (sodium dimethylarsenate) is a buffering agent used in protein crysta |
| reagent | reagents/buffers/caps-buffer/ | CAPS Buffer (N-Cyclohexyl-3-Aminopropanesulfonic Acid) | CAPS (N-cyclohexyl-3-aminopropanesulfonic acid) is a zwitterionic buffer with a  |
| reagent | reagents/buffers/citrate/ | Citrate Buffer (Sodium Citrate) | Citrate buffer, prepared from citric acid and sodium citrate, is a buffer system |
| reagent | reagents/buffers/glycine/ | Glycine | [Glycine](/xray-mp-wiki/reagents/buffers/glycine/) is the simplest amino acid, w |
| reagent | reagents/buffers/hepes/ | HEPES Buffer | HEPES (4-(2-hydroxyethyl)-1-piperazineethanesulfonic acid) is a zwitterionic buf |
| reagent | reagents/buffers/mes/ | 2-(N-Morpholino)ethanesulfonic Acid (MES) | MES (2-(N-morpholino)ethanesulfonic acid) is a zwitterionic Good's buffer widely |
| reagent | reagents/buffers/mops/ | MOPS (3-(N-Morpholino)propanesulfonic Acid) | MOPS (3-(N-morpholino)propanesulfonic acid) is a zwitterionic Good's buffer wide |
| reagent | reagents/buffers/pipes/ | PIPES (Piperazine-1,4-Bis(2-Ethanesulfonic Acid)) | PIPES (piperazine-1,4-bis(2-ethanesulfonic acid)) is a Good's buffer commonly us |
| reagent | reagents/buffers/sodium-acetate/ | Sodium Acetate | Sodium acetate is a common buffer used in membrane protein crystallization, part |
| reagent | reagents/buffers/sodium-cacodylate/ | Sodium Cacodylate | Sodium cacodylate (dimethylarsinic acid sodium salt) is an organic buffer
| reagent | reagents/buffers/sodium-citrate/ | Sodium Citrate (Na-Citrate Buffer) | Sodium [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate/ |
| reagent | reagents/buffers/sodium-phosphate/ | Sodium Phosphate | Sodium phosphate buffer at pH 5.6 was used at 3 M concentration as the reservoir |
| reagent | reagents/buffers/tes/ | TES Buffer (N-Tris(hydroxymethyl)methyl-2-aminoethanesulfonic acid) | TES (N-tris(hydroxymethyl)methyl-2-aminoethanesulfonic acid) is a zwitterionic G |
| reagent | reagents/buffers/tricine/ | Tricine Buffer | Tricine (N-[Tris(hydroxymethyl)methyl]glycine) is a Good's buffer with a pKa of  |
| reagent | reagents/buffers/tris/ | Tris (Tris-HCl Buffer) | Tris (tris(hydroxymethyl)aminomethane) is a common buffer used in biochemical an |
| reagent | reagents/cofactors/bacteriochlorophyll/ | Bacteriochlorophyll | Bacteriochlorophyll (BChl) is a magnesium-coordinated chlorin pigment found in a |
| reagent | reagents/cofactors/bacteriopheophytin/ | Bacteriopheophytin | Bacteriopheophytin (BPhe) is a chlorin pigment found in photosynthetic reaction  |
| reagent | reagents/cofactors/menaquinone-7/ | Menaquinone-7 (MK-7) | Menaquinone-7 (MK-7) is a lipid-soluble electron carrier in bacterial electron t |
| reagent | reagents/cofactors/nadh/ | NADH | Nicotinamide adenine dinucleotide (reduced form, NADH) is a universal electron c |
| reagent | reagents/cofactors/nicotinic-acid-adenine-dinucleotide/ | Nicotinic Acid Adenine Dinucleotide (NaAD) | Nicotinic acid adenine dinucleotide (NaAD) is a nucleotide cofactor and the auth |
| reagent | reagents/cofactors/riboflavin/ | Riboflavin (Vitamin B2) | Riboflavin (vitamin B2) is an essential precursor for flavin mononucleotide (FMN |
| reagent | reagents/cofactors/s-adenosyl-l-homocysteine/ | S-Adenosyl-L-Homocysteine (AdoHcy) | S-adenosyl-L-homocysteine (AdoHcy) is the product of methyl transfer reactions c |
| reagent | reagents/cofactors/sam/ | S-Adenosyl-L-Methionine (SAM) | S-adenosyl-[L-Methionine](/xray-mp-wiki/reagents/ligands/l-methionine/) (SAM) is |
| reagent | reagents/cofactors/ubiquinone/ | Ubiquinone | Ubiquinone (Coenzyme Q10) is a lipid-soluble electron carrier in the mitochondri |
| reagent | reagents/cofactors/vitamin-k/ | Vitamin K | Vitamin K is a fat-soluble vitamin that exists in several forms, including vitam |
| reagent | reagents/detergents/anzergent-3-12/ | Anzergent 3,12 | Anzergent 3,12 is a mild zwitterionic detergent used for solubilizing membrane p |
| reagent | reagents/detergents/c12e8/ | C12E8 (Octaethylene Glycol Monododecyl Ether) | C12E8 (octaethylene glycol monododecyl ether) is a nonionic detergent with a dod |
| reagent | reagents/detergents/c12e9/ | C12E9 (Dodecyl Nonaglycol) | C12E9 (dodecyl nonaethylene glycol ether, also known as Thesit or polidocanol) i |
| reagent | reagents/detergents/c14-betaine/ | Tetradecylbetaine (C14-betaine) | Tetradecylbetaine (C14-betaine) is a zwitterionic detergent with a tetradecyl (C |
| reagent | reagents/detergents/c8e4/ | Octyltetraoxyethylene (C8E4) | Octyltetraoxyethylene (C8E4, n-octyltetraoxyethylene) is a nonionic detergent wi |
| reagent | reagents/detergents/chapso/ | CHAPSO | CHAPSO (3-[(3-cholamidopropyl)dimethylammonio]-2-hydroxy-1-propanesulfonate) is  |
| reagent | reagents/detergents/cholesterol-hydrogen-succinate/ | Cholesteryl Hemisuccinate (CHS) | Cholesteryl hemisuccinate (CHS) is a cholesterol derivative used as a membrane p |
| reagent | reagents/detergents/cymal-4/ | Cymal-4 | Cymal-4 (4-cyclohexyl-1-butyl-beta-D-maltoside) is a short-chain nonionic deterg |
| reagent | reagents/detergents/cymal-6/ | Cymal-6 | Cymal-6 (6-cyclohexyl-1-hexyl-beta-D-maltoside) is a nonionic detergent in the C |
| reagent | reagents/detergents/ddm/ | n-Dodecyl-beta-D-maltopyranoside (DDM) | n-Dodecyl-β-D-maltopyranoside (DDM) is a nonionic, mild detergent widely used fo |
| reagent | reagents/detergents/dhpc/ | 1,2-Dihexanoyl-sn-glycero-3-phosphocholine (DHPC) | DHPC (1,2-dihexanoyl-sn-glycero-3-phosphocholine) is a zwitterionic detergent de |
| reagent | reagents/detergents/digitonin/ | Digitonin | Digitonin is a mild nonionic triterpene glycoside detergent extracted from the r |
| reagent | reagents/detergents/dm/ | n-Decyl-beta-D-Maltoside (DM) | Decyl-β-D-maltoside (DM) is a mild nonionic detergent with a 10-carbon alkyl cha |
| reagent | reagents/detergents/dmng/ | Decyl Maltose Neopentyl Glycol (DMng) | Decyl [Maltose](/xray-mp-wiki/reagents/additives/maltose/) neopentyl glycol (DMn |
| reagent | reagents/detergents/dodecanoylmorpholine/ | Dodecanoylmorpholine (DM) | Dodecanoylmorpholine (DM) is a nonionic surfactant commonly used as a mild deter |
| reagent | reagents/detergents/dodecylphosphocholine/ | Dodecylphosphocholine (DPC) | Dodecylphosphocholine ([DPC](/xray-mp-wiki/reagents/detergents/dpc/)) is a zwitt |
| reagent | reagents/detergents/dpc/ | Decylphosphocholine (DPC) | Decylphosphocholine ([DPC](/xray-mp-wiki/reagents/detergents/dodecylphosphocholi |
| reagent | reagents/detergents/fa-3/ | FA-3 (Facade-EM Facial Amphiphile) | FA-3 (Facade-EM, 3alpha-hydroxy-7alpha,12alpha-di-((O-beta-D-maltosyl)-2-hydroxy |
| reagent | reagents/detergents/fos-choline-11/ | Fos-Choline 11 (FC-11) | Fos-[Choline](/xray-mp-wiki/reagents/ligands/choline/) 11 (FC-11), also known as |
| reagent | reagents/detergents/fos-choline-9/ | Fos-Choline 9 (FC-9) | Fos-[Choline](/xray-mp-wiki/reagents/ligands/choline/) 9 (FC-9), also known as n |
| reagent | reagents/detergents/foscholine-12/ | Foscholine-12 | Foscholine-12 is a nonionic detergent from the Fc (foscholine) series developed  |
| reagent | reagents/detergents/glyco-diosgenin/ | Glyco-diosgenin (GDN) | Glyco-diosgenin (GDN) is a mild nonionic detergent derived from diosgenin, a ste |
| reagent | reagents/detergents/hega-10/ | Decanoyl-N-Hydroxyethylglucamide (HEGA-10) | Decanoyl-N-Hydroxyethylglucamide (HEGA-10) is a nonionic glucoside detergent use |
| reagent | reagents/detergents/heptylglucoside/ | Heptylglucoside (HpG) | Heptylglucoside (HpG, n-heptyl beta-D-glucopyranoside) is a nonionic detergent w |
| reagent | reagents/detergents/heptylthioglucoside/ | Heptylthioglucoside (HpTG) | Heptylthioglucoside (HpG) is a mild nonionic detergent with a 7-carbon alkyl cha |
| reagent | reagents/detergents/hexylmaltoside/ | Hexyl Maltoside (HxM) | Hexyl maltoside (HxM, n-hexyl-beta-D-maltopyranoside) is a nonionic detergent wi |
| reagent | reagents/detergents/lapao/ | LAPAO | LAPAO (3-laurylamido-N,N'-dimethylpropylaminoxyde) is a zwitterionic detergent u |
| reagent | reagents/detergents/ldao/ | n-Dodecyl-N,N-dimethylamine-N-oxide (LDAO) | Lauryldimethylamine N-oxide (LDAO) is a zwitterionic detergent with a 12-carbon  |
| reagent | reagents/detergents/lmng/ | Lauryl Maltose Neopentyl Glycol (LMNG) | LMNG (lauryl maltose neopentyl glycol, also known as MNG or MNG-3) is a nonionic |
| reagent | reagents/detergents/lppg/ | Lysophosphatidylcholine Phosphatidylglycerol (LPPG) | LPPG is a zwitterionic lipid-based detergent used in solution NMR studies of mem |
| reagent | reagents/detergents/mng-3-c8/ | Maltose Neopentyl Glycol 3-C8 (MNG-3-C8) | MNG-3-C8 is a [Maltose](/xray-mp-wiki/reagents/additives/maltose/) neopentyl gly |
| reagent | reagents/detergents/n-dodecyl-beta-d-maltoside/ | n-Dodecyl-beta-D-Maltoside (DDM) | n-Dodecyl-beta-D-maltoside (DDM) is a mild nonionic detergent widely used in mem |
| reagent | reagents/detergents/n-methyl-beta-d-glucoside/ | n-Methyl-beta-D-glucoside (BNG) | n-Methyl-beta-D-glucoside (BNG or NG) is a mild nonionic detergent with a methyl |
| reagent | reagents/detergents/n-n-bis-3-d-gluconamidopropyl-deoxycholamide/ | N,N-Bis-(3-D-gluconamidopropyl)deoxycholamide (DBC) | N,N-Bis-(3-D-gluconamidopropyl)deoxycholamide (DBC) is a zwitterionic detergent  |
| reagent | reagents/detergents/n-nonyl-beta-d-glucopyranoside/ | n-Nonyl-beta-D-Glucopyranoside (Nonyl Glucoside) | n-Nonyl-beta-D-glucopyranoside (nonyl glucoside, NG) is a nonionic detergent wit |
| reagent | reagents/detergents/n-octyl-beta-d-glucopyranoside/ | n-Octyl-beta-D-Glucopyranoside (OG) | n-Octyl-beta-D-glucopyranoside (octylglucoside, OG) is a mild nonionic detergent |
| reagent | reagents/detergents/n-octyl-beta-d-maltoside/ | n-Octyl-beta-D-maltoside (OM) | n-Octyl-beta-D-maltoside (OM) is a nonionic detergent with an octyl (C8) alkyl c |
| reagent | reagents/detergents/n-undecyl-beta-d-maltoside/ | n-Undecyl-β-D-maltoside (UDM) | n-Undecyl-β-D-maltoside (UDM) is a nonionic detergent with an 11-carbon alkyl ch |
| reagent | reagents/detergents/nm/ | n-Nonyl-beta-D-maltopyranoside (NM) | n-Nonyl-beta-D-maltopyranoside (NM) is a nonionic maltoside detergent with a 9-c |
| reagent | reagents/detergents/nonylglucoside/ | Nonylglucoside (NG) | Nonylglucoside (NG, n-nonyl beta-D-glucopyranoside) is a nonionic detergent with |
| reagent | reagents/detergents/octaethylene-glycol-mono-n-dodecylether/ | Octaethylene Glycol Mono-n-Dodecylether (C12E6) | Octaethylene glycol mono-n-dodecylether (C12E6) is a nonionic detergent with a d |
| reagent | reagents/detergents/octyl-beta-d-galactopyranoside/ | Octyl-beta-D-galactopyranoside | Octyl-beta-D-galactopyranoside is a nonionic galactoside detergent used in membr |
| reagent | reagents/detergents/octylthioglucoside/ | Octylthioglucoside (OTG) | Octylthioglucoside (OG or OTG) is a mild nonionic detergent with an 8-carbon alk |
| reagent | reagents/detergents/og/ | n-Octyl beta-D-glucopyranoside (OG) | n-Octyl beta-D-glucopyranoside (OG) is a mild nonionic detergent with an 8-carbo |
| reagent | reagents/detergents/ogng/ | Octyl Glucose Neopentyl Glycol (OGNG) | Octyl [Glucose](/xray-mp-wiki/reagents/additives/glucose/) neopentyl glycol (OGN |
| reagent | reagents/detergents/sodium-cholate/ | Sodium Cholate | Sodium cholate is an anionic bile salt detergent commonly used as a co-detergent |
| reagent | reagents/detergents/sucrose-monododecanoate/ | Sucrose Monododecanoate (SM) | [Sucrose](/xray-mp-wiki/reagents/ligands/sucrose/) monododecanoate (SM) is a non |
| reagent | reagents/detergents/thesit/ | Thesit (Polyoxyethylene 9-dodecyl ether) | Thesit (polyoxyethylene 9-dodecyl ether), also known as C12E9 or dodecyl nonaoxy |
| reagent | reagents/detergents/tridecylmaltoside/ | Tridecyl Maltoside (TDM) | Tridecyl maltoside (TDM) is a mild nonionic detergent with a 13-carbon alkyl cha |
| reagent | reagents/detergents/triton-x-100/ | Triton X-100 | Triton X-100 is a nonionic octylphenyl polyethoxylate detergent used for solubil |
| reagent | reagents/detergents/tween-20/ | Tween-20 Polysorbate 20 Nonionic Detergent | Tween-20 (polysorbate 20) is a nonionic detergent used at low concentrations (0. |
| reagent | reagents/detergents/udm/ | n-Undecyl-beta-D-maltoside (UDM) | n-Undecyl-beta-D-maltoside ([UDM](/xray-mp-wiki/reagents/detergents/udm/)) is a  |
| reagent | reagents/ligands/11-cis-retinal/ | 11-cis-Retinal | 11-cis-retinal is the light-sensitive chromophore covalently bound to the apopro |
| reagent | reagents/ligands/15r-methyl-pgd2/ | 15R-methyl-PGD2 (15mPGD2) | 15R-methyl-[PGD2](/xray-mp-wiki/reagents/ligands/prostaglandin-d2/) (15mPGD2) is |
| reagent | reagents/ligands/2-ag/ | 2-AG (2-Arachidonoylglycerol) | 2-Arachidonoylglycerol (2-AG) is an endogenous cannabinoid (endocannabinoid) and |
| reagent | reagents/ligands/2me-sadp/ | 2-Methylthio-ADP (2MeSADP) | 2-Methylthio-adenosine 5'-diphosphate (2MeSADP) is a stable analog of adenosine  |
| reagent | reagents/ligands/2me-satp/ | 2-Methylthio-ATP (2MeSATP) | 2-Methylthio-adenosine 5'-triphosphate (2MeSATP) is a stable analog of adenosine |
| reagent | reagents/ligands/2npg/ | 4-Nitrophenyl-alpha-D-galactopyranoside (2NPG) | 4-Nitrophenyl-alpha-D-galactopyranoside (2NPG) is a galactopyranoside analog use |
| reagent | reagents/ligands/3-4-dichlorophenethylamine/ | 3,4-Dichlorophenethylamine (DCP) | 3,4-Dichlorophenethylamine (DCP) is a halogenated phenethylamine derivative that |
| reagent | reagents/ligands/3-quinuclidinyl-benzilate/ | 3-Quinuclidinyl-benzilate (QNB) | 3-Quinuclidinyl-benzilate (QNB) is a potent, high-affinity muscarinic [Acetylcho |
| reagent | reagents/ligands/4-hydroxytamoxifen/ | 4-Hydroxytamoxifen | 4-Hydroxytamoxifen (4-OH-Tam) is a primary metabolite of tamoxifen formed by 4-h |
| reagent | reagents/ligands/4-ibp/ | 4-IBP (4-Iodo-N-benzylpiperidine) | 4-IBP (4-iodo-N-benzylpiperidine) is a sigma-1 receptor ligand with incompletely |
| reagent | reagents/ligands/5-aminolevulinic-acid/ | 5-Aminolevulinic Acid | 5-Aminolevulinic acid (5-ALA) is an endogenous nonprotein amino acid that forms  |
| reagent | reagents/ligands/6-aminohexanoic-acid/ | 6-Aminohexanoic Acid (6-AHA) | 6-Aminohexanoic acid (6-AHA) is a seven-carbon amino acid (epsilon-aminocaproic  |
| reagent | reagents/ligands/6mr-six-carbon-ring-retinal/ | 6mr (Six-Carbon-Ring Retinal) | 6mr (six-carbon-ring [Retinal](/xray-mp-wiki/reagents/ligands/retinal/)) is a sy |
| reagent | reagents/ligands/7-benzylidenenaltrexone/ | 7-Benzylidenenaltrexone (BNTX) | 7-Benzylidenenaltrexone (BNTX) is a selective delta-opioid receptor (δ-OR) antag |
| reagent | reagents/ligands/77-lh-28-1/ | 77-LH-28-1 | 77-LH-28-1 is a potent orthosteric full agonist of the [M1 Muscarinic Acetylchol |
| reagent | reagents/ligands/a-317491/ | A-317491 | A-317491 is a small-molecule competitive antagonist of P2X receptors, particular |
| reagent | reagents/ligands/aaa/ | Ala-Ala-Ala (AAA) | Ala-Ala-Ala (AAA) is a tripeptide composed of three alanine residues. It was use |
| reagent | reagents/ligands/abi-pp/ | ABI-PP (tert-butyl thiazolyl aminocarboxyl pyridopyrimidine) | ABI-PP is a pyridopyrimidine derivative that acts as a specific inhibitor of the |
| reagent | reagents/ligands/ac-fata-cmk/ | Ac-FATA-cmk (N-Acetyl-Phe-Ala-Thr-Ala-Chloromethylketone) | Ac-FATA-cmk is a tetrapeptidyl chloromethylketone (CMK) irreversible inhibitor o |
| reagent | reagents/ligands/ac-iata-cmk/ | Ac-IATA-cmk (N-Acetyl-Ile-Ala-Thr-Ala-Chloromethylketone) | Ac-IATA-cmk is a tetrapeptidyl chloromethylketone (CMK) irreversible inhibitor o |
| reagent | reagents/ligands/acetylcholine/ | Acetylcholine | Acetylcholine (ACh) is the endogenous neurotransmitter that activates muscarinic |
| reagent | reagents/ligands/acpc/ | ACPC (1-Aminocyclopropane-1-carboxylic Acid) | ACPC (1-aminocyclopropane-1-carboxylic acid) is a cyclic amino acid that acts as |
| reagent | reagents/ligands/act-462206/ | ACT-462206 | ACT-462206 is a dual orexin receptor antagonist (DORA) with a proline sulfonamid |
| reagent | reagents/ligands/adp/ | Adenosine Diphosphate (ADP) | Adenosine diphosphate (ADP) is a nucleotide that serves as the endogenous agonis |
| reagent | reagents/ligands/aea/ | AEA (Anandamide / N-Arachidonoylethanolamine) | Anandamide (AEA, N-arachidonoylethanolamine) is an endogenous cannabinoid (endoc |
| reagent | reagents/ligands/ag(i)/ | Silver(I) Ion | Silver(I) (Ag+) is a monovalent silver ion that serves as a substrate for the Cu |
| reagent | reagents/ligands/agmatine/ | Agmatine | Agmatine (4-aminobutylamine) is a polyamine formed by the arginine decarboxylati |
| reagent | reagents/ligands/alafosfalin/ | Alafosfalin | Alafosfalin is an anti-bacterial peptidomimetic phosphonodipeptide that serves a |
| reagent | reagents/ligands/alf4/ | AlF4 (Aluminum Fluoride) | Aluminum fluoride (AlF4-) is a phosphate analog used in structural biology to tr |
| reagent | reagents/ligands/alginate/ | Alginate | Alginate is an acidic polysaccharide produced by brown seaweeds and certain bact |
| reagent | reagents/ligands/alprenolol/ | Alprenolol | Alprenolol is a well-known non-selective beta-adrenergic receptor antagonist. It |
| reagent | reagents/ligands/am-3607/ | AM-3607 | AM-3607 is a synthetic cannabinoid derivative and a novel class of analgesic pot |
| reagent | reagents/ligands/am10257/ | AM10257 | AM10257 is a synthetic cannabinoid antagonist that binds to the CB2 receptor. It |
| reagent | reagents/ligands/am12033/ | AM12033 | AM12033 is a synthetic cannabinoid agonist with a tricyclic tetrahydrocannabinol |
| reagent | reagents/ligands/am6538/ | AM6538 | AM6538 is a tight-binding, wash-resistant antagonist of the human cannabinoid
| reagent | reagents/ligands/am841/ | AM841 | AM841 is a synthetic THC-like cannabinoid agonist with high affinity for the CB1 |
| reagent | reagents/ligands/amantadine/ | Amantadine | Amantadine (1-aminoadamantane) is a small adamantyl-amine antiviral drug that in |
| reagent | reagents/ligands/amg3054/ | AMG3054 | AMG3054 is a designed 17-amino-acid apelin mimetic peptide agonist of the human  |
| reagent | reagents/ligands/amiloride/ | Amiloride | Amiloride is a pharmacological ion channel blocker that targets acid-sensing ion |
| reagent | reagents/ligands/amino-methoxy-isocoumarin/ | Amino-Methoxy-Isocoumarin (JLK-6) | Amino-methoxy-[Isocoumarin](/xray-mp-wiki/reagents/antibiotics/isocoumarin/) (7- |
| reagent | reagents/ligands/amlodipine/ | Amlodipine | Amlodipine is a dihydropyridine calcium channel antagonist used primarily for th |
| reagent | reagents/ligands/amp-pnp/ | AMP-PNP | AMP-PNP (adenosine-5'-(beta,gamma-imido)triphosphate) is a non-hydrolyzable anal |
| reagent | reagents/ligands/amppcp/ | Adenylyl Methylenediphosphonate (AMP-PCP / AMPPCP) | Adenylyl methylenediphosphonate (AMP-PCP or AMPPCP) is a non-hydrolyzable ATP an |
| reagent | reagents/ligands/angiotensin-ii/ | Angiotensin II | Angiotensin II (AngII) is an octapeptide hormone and the endogenous agonist of t |
| reagent | reagents/ligands/anta-xv/ | Anta XV | Anta XV is a small-molecule antagonist of the human Smoothened (SMO) receptor. I |
| reagent | reagents/ligands/apelin-13/ | Apelin-13 | Apelin-13 is the shortest endogenous peptide agonist of the human apelin recepto |
| reagent | reagents/ligands/apelin-17/ | Apelin-17 | Apelin-17 is an endogenous peptide agonist of the human apelin receptor ([APJR]( |
| reagent | reagents/ligands/aprepitant/ | Aprepitant | Aprepitant is an FDA-approved small-molecule antagonist of the human neurokinin  |
| reagent | reagents/ligands/atenolol/ | Atenolol | Atenolol is a selective beta-1 adrenergic receptor antagonist (beta-blocker) use |
| reagent | reagents/ligands/atp-gamma-s/ | ATPγS (Adenosine 5'-O-(3-thiotriphosphate)) | ATPγS (adenosine 5'-O-(3-thiotriphosphate)) is a non-hydrolyzable ATP analog in  |
| reagent | reagents/ligands/atp/ | Adenosine Triphosphate (ATP) | Adenosine triphosphate (ATP) is the primary energy currency of cells and also se |
| reagent | reagents/ligands/atropine/ | Atropine | Atropine is a competitive antagonist at muscarinic [Acetylcholine](/xray-mp-wiki |
| reagent | reagents/ligands/au1235/ | AU1235 | AU1235 is an adamantyl urea compound that shows good bactericidal activity again |
| reagent | reagents/ligands/aybr-a/ | Ala-Tyr(L-3,5-diBr)-Ala (AY(Br)A) | Ala-Tyr(L-3,5-diBr)-Ala (AY(Br)A) is a tripeptide composed of [L-Alanine](/xray- |
| reagent | reagents/ligands/aybr/ | Ala-Tyr(L-3,5-diBr) | Ala-Tyr(L-3,5-diBr) is a dipeptide composed of [L-Alanine](/xray-mp-wiki/reagent |
| reagent | reagents/ligands/az3451/ | AZ3451 (PAR2 Antagonist) | AZ3451 is a potent small-molecule antagonist of the human protease-activated rec |
| reagent | reagents/ligands/az8838/ | AZ8838 (PAR2 Antagonist) | AZ8838 is a selective small-molecule antagonist of the human protease-activated  |
| reagent | reagents/ligands/azd1283/ | AZD1283 | AZD1283 is a non-nucleotide reversible antagonist of the [Human P2Y12 Receptor]( |
| reagent | reagents/ligands/azilsartan/ | Azilsartan | Azilsartan is a clinically used angiotensin receptor blocker (ARB) featuring a b |
| reagent | reagents/ligands/batimastat/ | Batimastat | Batimastat is a peptide-mimetic inhibitor of site-2 protease (S2P) family member |
| reagent | reagents/ligands/bde-100/ | BDE-100 (2,2',4,4'-Tetrabromodiphenyl Ether) | BDE-100 (2,2',4,4'-tetrabromodiphenyl ether) is a brominated flame retardant
| reagent | reagents/ligands/bdm88832-iodo-pyridylpiperazine/ | BDM88832 (5-Iodo Pyridylpiperazine EPI) | BDM88832 (compound 8) is a pyridylpiperazine-based efflux pump inhibitor with a  |
| reagent | reagents/ligands/bdm88855-pyridylpiperazine-epi/ | BDM88855 (Pyridylpiperazine Efflux Pump Inhibitor) | BDM88855 (compound 9) is a pyridylpiperazine-based small molecule that acts as a |
| reagent | reagents/ligands/bef3/ | BeF3 (Beryllium Fluoride) | Beryllium fluoride (BeF3-) is a phosphate analog used in structural biology to t |
| reagent | reagents/ligands/benzamidine/ | Benzamidine | Benzamidine is a carboximidamide compound with diverse pharmacological propertie |
| reagent | reagents/ligands/benzyl-hydantoin/ | Benzyl-Hydantoin | Benzyl-hydantoin (L-5-benzyl-hydantoin) is a substrate analog of the NCS1 family |
| reagent | reagents/ligands/beta-cft/ | beta-CFT (CFT) | beta-CFT (2-beta-carbomethoxy-3-beta-(4-fluorophenyl)tropane) is a tropane alkal |
| reagent | reagents/ligands/beta-fna/ | beta-FNA (beta-Funaltrexamine) | beta-Funaltrexamine (beta-FNA) is an irreversible narcotic antagonist that coval |
| reagent | reagents/ligands/beta-foa/ | beta-FOA (beta-Fuoxymorphamine) | beta-Fuoxymorphamine (beta-FOA) is a morphinan agonist that differs from the ant |
| reagent | reagents/ligands/bi-167107/ | BI-167107 | BI-167107 is a potent, selective full agonist ligand for the human beta2-adrener |
| reagent | reagents/ligands/biil260/ | BIIL260 | BIIL260 is a selective antagonist for the leukotriene B4 receptor [Leukotriene B |
| reagent | reagents/ligands/bms-681/ | BMS-681 | BMS-681 is a potent, selective small-molecule orthosteric antagonist of the CC c |
| reagent | reagents/ligands/bongkrekic-acid/ | Bongkrekic Acid | Bongkrekic acid (BKA) is a polyunsaturated methoxy tricarboxylic acid polyketide |
| reagent | reagents/ligands/bptu/ | BPTU | BPTU [1-(2-(2-(tert-butyl)phenoxy)pyridin-3-yl)-3-(4-(trifluoromethoxy)phenyl)[U |
| reagent | reagents/ligands/br-memantine/ | Br-Memantine (Bromo-memantine) | Br-memantine (3-bromo-5,7-dimethyladamantan-1-amine hydrochloride) is a brominat |
| reagent | reagents/ligands/br-verapamil/ | Br-Verapamil | Br-[Verapamil](/xray-mp-wiki/reagents/ligands/verapamil/) is a brominated deriva |
| reagent | reagents/ligands/bremazocine/ | Bremazocine | Bremazocine is a kappa-opioid receptor (κ-OR) agonist with delta-opioid receptor |
| reagent | reagents/ligands/brodifacoum/ | Brodifacoum | Brodifacoum is a superwarfarin, a highly potent second-generation vitamin K anta |
| reagent | reagents/ligands/bromo-lidocaine/ | Bromo-lidocaine | Bromo-[Lidocaine](/xray-mp-wiki/reagents/ligands/lidocaine/) is a derivative of  |
| reagent | reagents/ligands/bromoacetate/ | Bromoacetate | Bromoacetate (BrCH2COO-) is a short carboxylic acid that serves as an anomalousl |
| reagent | reagents/ligands/bromobarbital/ | Bromobarbital | Bromobarbital (5-(2-bromo-ethyl)-5-ethyl-pyrimidine-2,4,6-trione) is a barbitura |
| reagent | reagents/ligands/bromoform/ | Bromoform (Tribromomethane) | Bromoform (tribromomethane, CHBr3) is a trihalomethane general anesthetic that i |
| reagent | reagents/ligands/bu72/ | BU72 | BU72 is a high-affinity morphinan agonist at the mu-opioid receptor (muOR). It i |
| reagent | reagents/ligands/bu74/ | BU74 | BU74 is a morphinan antagonist at the mu-opioid receptor. It is a complex oripav |
| reagent | reagents/ligands/bucindolol/ | Bucindolol | Bucindolol is a beta blocker (antagonist of the G protein-coupled pathway of bet |
| reagent | reagents/ligands/bufalin/ | Bufalin | Bufalin is a bufadienolide cardiotonic steroid, characterized by a six-membered  |
| reagent | reagents/ligands/bw373u86/ | BW373U86 | BW373U86 is a selective delta-opioid receptor (δ-OR) agonist that displays minim |
| reagent | reagents/ligands/c-cpe/ | C-CPE (Clostridium perfringens Enterotoxin) | C-CPE (C-terminal fragment of *Clostridium perfringens* enterotoxin) is a ~25 kD |
| reagent | reagents/ligands/c3361/ | C3361 (PfHT1 Inhibitor) | C3361 is a moderate PfHT1-specific inhibitor that was used as a reference compou |
| reagent | reagents/ligands/caffeine/ | Caffeine | Caffeine (1,3,7-trimethylxanthine) is a non-selective, weak antagonist of adenos |
| reagent | reagents/ligands/candesartan/ | Candesartan | Candesartan is an insurmountable inverse agonist at the angiotensin II type 1 re |
| reagent | reagents/ligands/carazolol/ | Carazolol | Carazolol is a potent inverse agonist ligand for the beta-adrenergic receptors.  |
| reagent | reagents/ligands/carbamylcholine/ | Carbamylcholine | Carbamylcholine (carbachol) is a synthetic [Choline](/xray-mp-wiki/reagents/liga |
| reagent | reagents/ligands/carboxymycobactin/ | Carboxymycobactin (Fe-cMBT) | Carboxymycobactin (cMBT) is a water-soluble siderophore produced by mycobacteria |
| reagent | reagents/ligands/carmoterol/ | Carmoterol | Carmoterol is a potent beta-adrenergic receptor agonist used in structural studi |
| reagent | reagents/ligands/carotenoid/ | Carotenoid | Carotenoids are lipid-soluble pigments found in photosynthetic complexes and oth |
| reagent | reagents/ligands/carryatractyloside/ | Carboxyatractyloside | Carboxyatractyloside is a specific inhibitor of the mitochondrial ADP/ATP carrie |
| reagent | reagents/ligands/carvedilol/ | Carvedilol | Carvedilol is a beta blocker that acts as a biased agonist of beta-adrenoceptors |
| reagent | reagents/ligands/ccr2-ra-r/ | CCR2-RA-[R] | CCR2-RA-[R] is a potent, selective small-molecule allosteric antagonist of the C |
| reagent | reagents/ligands/cgs21680/ | CGS21680 | CGS21680 (2-[p-(2-carboxyethyl)phenylethylamino]-5'-N-ethylcarboxamidoadenosine) |
| reagent | reagents/ligands/chloride-ion/ | Chloride Ion (Cl-) | Chloride ion (Cl-) is an essential co-transport ion for [Neurotransmitter/Sodium |
| reagent | reagents/ligands/chlorophacinone/ | Chlorophacinone | Chlorophacinone is a superwarfarin belonging to the 1,3-indandione class of vita |
| reagent | reagents/ligands/choline/ | Choline | Choline is a quaternary ammonium compound that serves as an essential nutrient i |
| reagent | reagents/ligands/ciprofloxacin/ | Ciprofloxacin - Fluoroquinolone Antibiotic | Ciprofloxacin (Cip) is a broad-spectrum fluoroquinolone antibiotic that inhibits |
| reagent | reagents/ligands/cis-22a/ | cis-22a (PCHPD TRPV6 Inhibitor) | cis-22a is a (4-phenylcyclohexyl)piperazine derivative (PCHPD) that acts as a po |
| reagent | reagents/ligands/clomipramine/ | Clomipramine (CMI) | Clomipramine (CMI) is a tricyclic antidepressant (TCA) of the dibenzazepine clas |
| reagent | reagents/ligands/cmp2105/ | Cmp2105 | Cmp2105 is a small molecule intracellular allosteric antagonist of the human
| reagent | reagents/ligands/cobalamin/ | Cobalamin (Vitamin B12) | Cobalamin (vitamin B12) is the largest and most complex B vitamin. It consists
| reagent | reagents/ligands/cocaine/ | Cocaine | Cocaine is a tropane alkaloid that acts as a competitive inhibitor of the dopami |
| reagent | reagents/ligands/compound-1/ | Compound 1 | Compound 1 (Cpd 1) is a quinazolinone-biphenyltetrazole derivative that acts as  |
| reagent | reagents/ligands/compound-14-pyridothiadiazinone/ | Compound 14 (Pyridothiadiazinone) | Compound 14 is a pyridothiadiazinone-3-one 1,1-dioxide derivative described as a |
| reagent | reagents/ligands/compound-15-pa/ | Cmpd-15PA (Compound-15PA) | Cmpd-15PA is a negative allosteric modulator of the beta2-adrenergic receptor (b |
| reagent | reagents/ligands/compound-15/ | Cmpd-15 (Compound-15) | Cmpd-15 is a negative allosteric modulator of the beta2-adrenergic receptor (bet |
| reagent | reagents/ligands/compound-16-diazaspirodecane/ | Compound 16 (Diazaspirodecane) | Compound 16 is a diazaspirodecane sulfonamide synthesized as a benchmark from th |
| reagent | reagents/ligands/compound-2-beta2-ar/ | Compound 2 (Kolb et al., 2009) | Compound 2 is a potent inverse agonist of the human beta2-adrenergic receptor, o |
| reagent | reagents/ligands/compound-2/ | Compound 2 (AT2R dual ligand) | Compound 2 (Cpd 2) is a quinazolinone-biphenyltetrazole derivative that acts as  |
| reagent | reagents/ligands/compound-3-mpges1-inhibitor/ | Compound 3 (Biarylindole mPGES-1 Inhibitor) | Compound 3 is a biarylindole inhibitor of microsomal prostaglandin E synthase 1  |
| reagent | reagents/ligands/compound-30-mk886-derivative-mpges1-inhibitor/ | Compound 30 (MK-886 Derivative, Biarylindole mPGES-1 Inhibitor) | Compound 30 is a biarylindole inhibitor of microsomal prostaglandin E synthase 1 |
| reagent | reagents/ligands/compound-5-mpges1-inhibitor/ | Compound 5 (Biarylimidazole mPGES-1 Inhibitor) | Compound 5 is a nanomolar biarylimidazole inhibitor of microsomal prostaglandin  |
| reagent | reagents/ligands/compound-pi1/ | Compound PI1 (5-(4-bromophenyl)-2-(4-bromophenethyl)-1H-isoindole-1,3(2H)-dione) | PI1 is a brominated isoindole-dione compound that acts as a potent sodium channe |
| reagent | reagents/ligands/con-ikot-ikot-toxin/ | Con-ikot-ikot Toxin | Con-ikot-ikot is a homodimeric cone snail toxin from Conus striatus that acts as |
| reagent | reagents/ligands/cp-376395/ | CP-376395 | CP-376395 is a potent inverse agonist ligand for the human corticotropin-releasi |
| reagent | reagents/ligands/cp-99-994/ | CP-99,994 | CP-99,994 is a high-affinity, selective non-peptide antagonist of the human neur |
| reagent | reagents/ligands/cp55940/ | CP55,940 | CP55,940 is a non-selective synthetic cannabinoid agonist that binds to both CB1 |
| reagent | reagents/ligands/cu(i)/ | Copper(I) Ion | Copper(I) (Cu+) is a monovalent copper ion that serves as a substrate for the Cu |
| reagent | reagents/ligands/cvx15/ | CVX15 | CVX15 is a 16-residue cyclic peptide antagonist of the chemokine receptor [Human |
| reagent | reagents/ligands/cyanopindolol/ | Cyanopindolol | Cyanopindolol is a high-affinity antagonist ligand for beta-adrenergic receptors |
| reagent | reagents/ligands/cyclazocine/ | Cyclazocine | Cyclazocine is a mixed mu/kappa-opioid receptor agonist with delta-opioid recept |
| reagent | reagents/ligands/cyclic-di-gmp/ | Cyclic-di-GMP (Bis-(3'-5')-Cyclic Diguanylic Acid) | Cyclic-di-GMP (bis-(3'-5')-cyclic diguanylic acid) is a ubiquitous bacterial sec |
| reagent | reagents/ligands/cyclopamine/ | Cyclopamine | Cyclopamine is a naturally occurring teratogen and the first selective small-mol |
| reagent | reagents/ligands/cyclopiazonic-acid/ | Cyclopiazonic Acid (CPA) | Cyclopiazonic acid (CPA) is a specific inhibitor of the sarco/endoplasmic reticu |
| reagent | reagents/ligands/d-alanine/ | D-Alanine | D-Alanine is a D-enantiomer of the amino acid alanine, used as a ligand to study |
| reagent | reagents/ligands/d-amphetamine/ | D-Amphetamine | D-amphetamine is a psychostimulant and phenethylamine derivative that acts as a  |
| reagent | reagents/ligands/d-aspartate/ | D-Aspartic Acid (D-Aspartate) | D-aspartate is the D-enantiomer of the amino acid aspartate. Unlike most
| reagent | reagents/ligands/d-fructose/ | D-Fructose | D-Fructose is a monosaccharide sugar that serves as the primary substrate of the |
| reagent | reagents/ligands/d-galactose/ | D-Galactose | D-Galactose is a monosaccharide (aldohexose) that serves as the primary substrat |
| reagent | reagents/ligands/d-myo-inositol-3-phosphate/ | D-myo-Inositol-3-Phosphate | D-myo-inositol-3-phosphate (ino-P) is a soluble substrate of
| reagent | reagents/ligands/dadle/ | DADLE (D-Ala2-MePhe4-Glyol5-Enkephalin) | DADLE (D-Ala2-MePhe4-Glyol5-enkephalin) is a selective delta-opioid receptor (δ- |
| reagent | reagents/ligands/daltroban/ | Daltroban | Daltroban is a nonprostanoid antagonist of the thromboxane A2 receptor (TP) that |
| reagent | reagents/ligands/dansyl-galactopyranoside-d2g/ | Dansyl-galactopyranoside (D2G) | Dansyl-galactopyranoside (D2G), formally 2'-(N-dansyl)aminoalkyl-1-thio-beta-D-g |
| reagent | reagents/ligands/daptomycin/ | Daptomycin | Daptomycin is a cyclic lipopeptide antibiotic used for treating serious infectio |
| reagent | reagents/ligands/daridorexant/ | Daridorexant | Daridorexant (ACT-541468, formerly nemorexant) is a dual orexin receptor antagon |
| reagent | reagents/ligands/daunomycin/ | Daunomycin | Daunomycin is an anthracycline anticancer drug that acts as a substrate for the  |
| reagent | reagents/ligands/dequalinium/ | Dequalinium - Quaternary Ammonium Cation | Dequalinium (Dq) is a quaternary ammonium cation with two quinolinium moieties c |
| reagent | reagents/ligands/desflurane/ | Desflurane | Desflurane (1,2,2,2-tetrafluoroethyl difluoromethyl ether) is a volatile general |
| reagent | reagents/ligands/desipramine/ | Desipramine | Desipramine is a tricyclic antidepressant (TCA) of the dibenzazepine class. It a |
| reagent | reagents/ligands/desthiobiotin/ | Desthiobiotin | Desthiobiotin is a biotin analog lacking the sulfur atom in the tetrahydrothioph |
| reagent | reagents/ligands/desvenlafaxine/ | Desvenlafaxine | Desvenlafaxine is a serotonin-noradrenaline reuptake inhibitor (SNRI) antidepres |
| reagent | reagents/ligands/dhea/ | Dehydroepiandrosterone (DHEA) | Dehydroepiandrosterone (DHEA) is an endogenous androgen steroid hormone and a ke |
| reagent | reagents/ligands/dht/ | Dihydrotestosterone (DHT) | Dihydrotestosterone (DHT) is the most potent endogenous androgen steroid hormone |
| reagent | reagents/ligands/diacetylchitobiose/ | Diacetylchitobiose (GlcNAc2) | Diacetylchitobiose, also known as (GlcNAc)2 or chitobiose, is a disaccharide con |
| reagent | reagents/ligands/digitoxin/ | Digitoxin | Digitoxin (DTX) is a cardiotonic steroid (cardiac glycoside) of the cardenolide  |
| reagent | reagents/ligands/digoxin/ | Digoxin | Digoxin is a cardiotonic steroid (cardiac glycoside) of the cardenolide class, c |
| reagent | reagents/ligands/diisopropyl-fluorophosphate/ | Diisopropyl Fluorophosphate (DFP) | Diisopropyl fluorophosphate (DFP) is an organophosphate mechanism-based inhibito |
| reagent | reagents/ligands/dilazep/ | Dilazep | Dilazep is a non-nucleoside adenosine reuptake inhibitor (AdoRI) clinically used |
| reagent | reagents/ligands/dinicotinic-acid-adenine-dinucleotide/ | Dinicotinic Acid Adenine Dinucleotide (DaAD) | Dinicotinic acid adenine dinucleotide (DaAD) is a reaction intermediate in the n |
| reagent | reagents/ligands/diprenorphine/ | Diprenorphine | Diprenorphine is a broad-spectrum opioid receptor antagonist with affinity for m |
| reagent | reagents/ligands/dobutamine/ | Dobutamine | Dobutamine is a synthetic catecholamine derivative and a beta1-adrenergic recept |
| reagent | reagents/ligands/dopamine/ | Dopamine | Dopamine is the endogenous neurotransmitter substrate of the dopamine transporte |
| reagent | reagents/ligands/doxepin/ | Doxepin | Doxepin is a first-generation H1 receptor antagonist (antihistamine) belonging t |
| reagent | reagents/ligands/doxorubicin/ | Doxorubicin - Anthracycline Anticancer Drug | Doxorubicin is a widely used anthracycline anticancer antibiotic that functions  |
| reagent | reagents/ligands/dpcpx/ | DPCPX (8-Cyclopentyl-1,3-dipropylxanthine) | DPCPX (8-cyclopentyl-1,3-dipropylxanthine) is a selective adenosine A1 receptor  |
| reagent | reagents/ligands/du172/ | DU172 | DU172 (4-((3-(8-cyclohexyl-2,6-dioxo-1-propyl-1,2,6,7-tetrahydro-3H-purin-3-yl)p |
| reagent | reagents/ligands/duloxetine/ | Duloxetine | Duloxetine is a serotonin-noradrenaline reuptake inhibitor (SNRI) antidepressant |
| reagent | reagents/ligands/e-4-hydroxytamoxifen/ | E-4-Hydroxytamoxifen | E-4-Hydroxytamoxifen is the E-isomer of 4-hydroxytamoxifen, a primary metabolite |
| reagent | reagents/ligands/e-endoxifen/ | E-Endoxifen | E-Endoxifen is the E-isomer of endoxifen (4-hydroxy-N-desmethyltamoxifen), the p |
| reagent | reagents/ligands/elinogrel/ | Elinogrel | Elinogrel is a reversible antagonist of the P2Y12 receptor that was studied in f |
| reagent | reagents/ligands/empa/ | EMPA (N-ethyl-2-[(6-methoxy-pyridin-3-yl)-(toluene-2-sulfonyl)-amino]-N-pyridin-3-yl-methyl) | EMPA (N-ethyl-2-[(6-methoxy-pyridin-3-yl)-(toluene-2-sulfonyl)-amino]-N-pyridin- |
| reagent | reagents/ligands/endoxifen/ | Endoxifen | Endoxifen (4-hydroxy-N-desmethyltamoxifen) is the primary active metabolite of t |
| reagent | reagents/ligands/epinephrine/ | Epinephrine | Epinephrine (also known as adrenaline) is an endogenous catecholamine hormone pr |
| reagent | reagents/ligands/eprosartan/ | Eprosartan | Eprosartan is a clinically used angiotensin receptor blocker (ARB) featuring a b |
| reagent | reagents/ligands/ergotamine/ | Ergotamine (ERG) | Ergotamine is an ergoline alkaloid and GPCR ligand that acts as a biased agonist |
| reagent | reagents/ligands/erythromycin/ | Erythromycin | Erythromycin is a macrolide antibiotic (Mr ~734) that inhibits bacterial protein |
| reagent | reagents/ligands/estradiol/ | 17beta-Estradiol (E2) | 17beta-Estradiol (E2) is the most potent endogenous estrogen steroid hormone. It |
| reagent | reagents/ligands/estrone/ | Estrone (E1) | Estrone (E1) is an endogenous estrogen steroid hormone and the product of estron |
| reagent | reagents/ligands/ethidium/ | Ethidium - Fluorescent Intercalating Dye | Ethidium (Et) is a fluorescent intercalating dye that is widely used as a substr |
| reagent | reagents/ligands/eticlopride/ | Eticlopride | Eticlopride is a D2/D3 [Dopamine](/xray-mp-wiki/reagents/ligands/dopamine/) rece |
| reagent | reagents/ligands/etorphine/ | Etorphine | Etorphine is a potent broad-spectrum opioid receptor agonist with high affinity  |
| reagent | reagents/ligands/eu93-108/ | EU93-108 | EU93-108 is a novel piperazine-containing GluN2B-selective negative allosteric m |
| reagent | reagents/ligands/fenobam/ | Fenobam | Fenobam is a negative allosteric modulator (NAM) of the [Metabotropic Glutamate  |
| reagent | reagents/ligands/ferulenol/ | Ferulenol | Ferulenol is a natural product and close structural analog of [Warfarin](/xray-m |
| reagent | reagents/ligands/flecainide/ | Flecainide | Flecainide is a class IC antiarrhythmic drug (AAD) used for treatment of atrial
| reagent | reagents/ligands/fluorowilliardiine/ | Fluorowilliardiine (FW) | Fluorowilliardiine (FW) is a halogenated willardiine derivative that acts as a p |
| reagent | reagents/ligands/fluoxetine/ | Fluoxetine | Fluoxetine is a selective [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/ |
| reagent | reagents/ligands/fluvoxamine/ | Fluvoxamine | Fluvoxamine is a selective [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki |
| reagent | reagents/ligands/formoterol/ | Formoterol | Formoterol is a long-acting selective beta2-adrenergic receptor agonist used in  |
| reagent | reagents/ligands/fscpx/ | FSCPX | FSCPX is a covalent xanthine antagonist of the adenosine A1 receptor. It promote |
| reagent | reagents/ligands/fucoxanthin/ | Fucoxanthin | Fucoxanthin (Fx) is a carotenoid pigment found in brown algae and diatoms that g |
| reagent | reagents/ligands/g247-optimized-quinoline-msba-inhibitor/ | G247 (Optimized Quinoline MsbA Inhibitor) | G247 is an optimized quinoline-based inhibitor of [MSBA](/xray-mp-wiki/proteins/ |
| reagent | reagents/ligands/g592-initial-quinoline-msba-inhibitor/ | G592 (Initial Quinoline MsbA Inhibitor) | G592 is the initial quinoline hit identified from a library of approximately 3,0 |
| reagent | reagents/ligands/g907-quinoline-msba-inhibitor/ | G907 (Quinoline MsbA Inhibitor) | G907 is a quinoline-based small molecule that acts as a potent and selective inh |
| reagent | reagents/ligands/gamma-butyrobetaine/ | Gamma-Butyrobetaine (4-Trimethylaminobutyrate) | Gamma-Butyrobetaine (also known as 4-trimethylaminobutyrate) is a quaternary amm |
| reagent | reagents/ligands/gdc-0449/ | GDC-0449 (Vismodegib) | GDC-0449 (vismodegib) is a small-molecule antagonist of the human Smoothened (SM |
| reagent | reagents/ligands/gdp/ | Guanosine Diphosphate (GDP) | Guanosine diphosphate (GDP) is a nucleotide that binds to the G alpha subunit of |
| reagent | reagents/ligands/globomycin/ | Globomycin | Globomycin is a cyclic depsipeptide antibiotic produced by select strains of Str |
| reagent | reagents/ligands/glycine-betaine/ | Glycine Betaine | Glycine betaine (betaine) is a quaternary ammonium compound derived from the ami |
| reagent | reagents/ligands/gsk1034702/ | GSK1034702 | GSK1034702 is a bitopic orthosteric agonist of the [M1 Muscarinic Acetylcholine  |
| reagent | reagents/ligands/gsk1059865/ | GSK1059865 | GSK1059865 is an orexin 1 receptor-selective antagonist (1-SORA) that was widely |
| reagent | reagents/ligands/gx-936/ | GX-936 | GX-936 is an aryl sulfonamide small-molecule antagonist that selectively inhibit |
| reagent | reagents/ligands/haloperidol/ | Haloperidol | Haloperidol is a typical antipsychotic drug belonging to the butyrophenone class |
| reagent | reagents/ligands/heme/ | Heme | Heme is an iron-containing porphyrin cofactor found in many membrane proteins in |
| reagent | reagents/ligands/htl14242/ | HTL14242 (Compound 25) | HTL14242 (compound 25) is 3-chloro-5-[6-(5-fluoropyridin-2-yl)pyrimidin-4-yl]ben |
| reagent | reagents/ligands/htl6641/ | HTL6641 | HTL6641 is a dual orexin receptor antagonist (DORA) with a central benzo- or pyr |
| reagent | reagents/ligands/htl9936/ | HTL9936 | HTL9936 is a selective, partial orthosteric agonist of the human [M1 Muscarinic  |
| reagent | reagents/ligands/hu-308/ | HU-308 | HU-308 is a highly CB2-selective synthetic cannabinoid agonist. It shows approxi |
| reagent | reagents/ligands/ica38/ | ICA38 | ICA38 is an indolcarboxamide compound that targets MmpL3, an essential mycobacte |
| reagent | reagents/ligands/ici-118-551/ | ICI 118,551 | ICI 118,551 is a potent and selective beta2-adrenergic receptor antagonist (inve |
| reagent | reagents/ligands/ici-174-864/ | ICI-174,864 | ICI-174,864 is a selective delta-opioid receptor (δ-OR) inverse agonist. It is u |
| reagent | reagents/ligands/idp/ | Inositol Pyrophosphate (IDP) | Inositol pyrophosphate (IDP) serves as a substrate analog for inorganic pyrophos |
| reagent | reagents/ligands/ifenprodil/ | Ifenprodil | Ifenprodil is a selective negative allosteric modulator (NAM) of NMDA receptors  |
| reagent | reagents/ligands/ihch7009/ | IHCH7009 (Novel Third-Generation Antipsychotic Lead) | IHCH7009 is a novel third-generation antipsychotic compound designed through str |
| reagent | reagents/ligands/ihch7010/ | IHCH7010 (Novel Third-Generation Antipsychotic Lead) | IHCH7010 is a novel third-generation antipsychotic compound designed through str |
| reagent | reagents/ligands/ihch7041-active-enantiomer/ | (-)-IHCH7041 (Active Enantiomer Antipsychotic Lead) | (-)-[IHCH7041 (Racemic Third-Generation Antipsychotic Lead)](/xray-mp-wiki/reage |
| reagent | reagents/ligands/ihch7041/ | IHCH7041 (Racemic Third-Generation Antipsychotic Lead) | IHCH7041 is a racemic third-generation antipsychotic lead compound featuring a p |
| reagent | reagents/ligands/imipramine/ | Imipramine | Imipramine is a tricyclic antidepressant (TCA) of the dibenzazepine class. It wa |
| reagent | reagents/ligands/iperoxo/ | Iperoxo | Iperoxo is a high-affinity muscarinic [Acetylcholine](/xray-mp-wiki/reagents/lig |
| reagent | reagents/ligands/irbesartan/ | Irbesartan | Irbesartan is a clinically used angiotensin receptor blocker (ARB) featuring a b |
| reagent | reagents/ligands/irl2500/ | IRL2500 | IRL2500 is a peptide-mimetic of the C-terminal tripeptide of endothelin-1 (ET-1) |
| reagent | reagents/ligands/isoprenaline/ | Isoprenaline (Isoproterenol) | Isoprenaline (also known as isoproterenol) is a synthetic catecholamine and a po |
| reagent | reagents/ligands/istaroxime/ | Istaroxime | Istaroxime (IST) is a next-generation cardiotonic steroid (CTS) developed for th |
| reagent | reagents/ligands/it1t/ | IT1t | IT1t is a small-molecule antagonist of the chemokine receptor [Human CXCR4 Chemo |
| reagent | reagents/ligands/ivermectin/ | Ivermectin | Ivermectin is a macrocyclic anthelmintic drug from the avermectin family that ac |
| reagent | reagents/ligands/jdtc/ | JDTic | JDTic is a potent and selective [Kappa Opioid Receptor](/xray-mp-wiki/proteins/g |
| reagent | reagents/ligands/jnj-31020028/ | JNJ-31020028 | JNJ-31020028 is a potent, selective, brain-penetrant small-molecule antagonist o |
| reagent | reagents/ligands/kaad-cyclopamine/ | KAAD-cyclopamine | KAAD-cyclopamine is a BODIPY-tagged derivative of cyclopamine with a long-chain  |
| reagent | reagents/ligands/kainate/ | Kainate (KA) | Kainate (KA) is a natural marine product originally isolated from the red alga D |
| reagent | reagents/ligands/ketamine/ | Ketamine | Ketamine is a dissociative anesthetic and NMDA receptor antagonist that also inh |
| reagent | reagents/ligands/kw-6356/ | KW-6356 | KW-6356 (N-[4-(furan-2-yl)-5-(oxane-4-carbonyl)-1,3-thiazol-2-yl]-6-methylpyridi |
| reagent | reagents/ligands/l-759-656/ | L-759,656 | L-759,656 is a CB2-selective synthetic cannabinoid agonist. It shows approximate |
| reagent | reagents/ligands/l-carnitine/ | L-Carnitine | L-Carnitine is a quaternary ammonium compound essential for the transport of act |
| reagent | reagents/ligands/l-fucose/ | L-Fucose | L-Fucose (6-deoxy-L-galactose) is a monosaccharide that is a major constituent o |
| reagent | reagents/ligands/l-leucine/ | L-Leucine | L-Leucine is an essential branched-chain amino acid and the canonical substrate  |
| reagent | reagents/ligands/l-methionine/ | L-Methionine | L-Methionine is a hydrophobic neutral amino acid that binds to the [LBD](/xray-m |
| reagent | reagents/ligands/l-phenylalanine/ | L-Phenylalanine | L-Phenylalanine is a large hydrophobic amino acid that binds to the [LBD](/xray- |
| reagent | reagents/ligands/l745870/ | L745870 | L745870 (1,4-disubstituted aromatic piperidine/piperazine, 1,4-DAP compound) is  |
| reagent | reagents/ligands/lamotrigine/ | Lamotrigine | Lamotrigine is a clinically important antiepileptic drug that blocks voltage-gat |
| reagent | reagents/ligands/lemborexant/ | Lemborexant | Lemborexant (Dayvigo) is a dual orexin receptor antagonist (DORA) approved by th |
| reagent | reagents/ligands/lidocaine/ | Lidocaine | Lidocaine is a widely used local anesthetic (LA) and class IB antiarrhythmic dru |
| reagent | reagents/ligands/lisuride/ | Lisuride | Lisuride is a semisynthetic ergoline derivative that acts as a [Dopamine](/xray- |
| reagent | reagents/ligands/lj-4517/ | LJ-4517 (Compound 2) | LJ-4517 (compound 2) is a novel truncated nucleoside antagonist of the adenosine |
| reagent | reagents/ligands/losartan/ | Losartan | Losartan is the first clinically used angiotensin receptor blocker (ARB), or sar |
| reagent | reagents/ligands/lsd/ | LSD (Lysergic Acid Diethylamide) | LSD (lysergic acid diethylamide) is a potent ergoline-class hallucinogen and one |
| reagent | reagents/ligands/ltb4/ | Leukotriene B4 (LTB4) | Leukotriene B4 (LTB4) is a potent inflammatory lipid mediator derived from arach |
| reagent | reagents/ligands/luf5833/ | LUF5833 (Compound 8) | LUF5833 (compound 8) is a nonriboside partial agonist of the human adenosine A2A |
| reagent | reagents/ligands/lutein/ | Lutein | Lutein is a major [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) pigme |
| reagent | reagents/ligands/ly2033298/ | LY2033298 | LY2033298 is a positive allosteric modulator (PAM) of the muscarinic M4 [Acetylc |
| reagent | reagents/ligands/ly2119620/ | LY2119620 | LY2119620 is a positive allosteric modulator (PAM) of the muscarinic M2 [Acetylc |
| reagent | reagents/ligands/ly2940680/ | LY2940680 | LY2940680 is a small-molecule antagonist of the smoothened (SMO) receptor, desig |
| reagent | reagents/ligands/m-mpep/ | M-MPEP | M-[MPEP](/xray-mp-wiki/reagents/ligands/mpep/) (2-[(3-methoxyphenyl)ethynyl]-6-m |
| reagent | reagents/ligands/maraviroc/ | Maraviroc | Maraviroc (UK-427,857) is an antiretroviral drug used for the treatment of HIV-1 |
| reagent | reagents/ligands/mavoglurant/ | Mavoglurant (AFQ056) | Mavoglurant (AFQ056, methyl (3aR,4S,7aR)-4-hydroxy-4-[(3-methylphenyl)ethynyl]oc |
| reagent | reagents/ligands/mazindol/ | Mazindol | Mazindol is a stimulant drug that acts as a [Norepinephrine](/xray-mp-wiki/reage |
| reagent | reagents/ligands/melibiose/ | Melibiose | Melibiose is an alpha-linked disaccharide composed of galactose and glucose. It  |
| reagent | reagents/ligands/memantine/ | Memantine | Memantine is an aminoadamantane derivative clinically used in the treatment of A |
| reagent | reagents/ligands/menaquinone/ | Menaquinone | Menaquinone (vitamin K2) is a lipid-soluble electron carrier in the electron tra |
| reagent | reagents/ligands/methamphetamine/ | Methamphetamine | Methamphetamine is a potent psychostimulant and phenethylamine derivative that a |
| reagent | reagents/ligands/methylgeromertrine/ | Methylgeromertrine | Methylgeromertrine is a semisynthetic ergoline derivative and a [Serotonin (5-Hy |
| reagent | reagents/ligands/mf63-mpges1-inhibitor/ | MF63 (Compound 63, Phenanthrene Imidazole mPGES-1 Inhibitor) | MF63 (compound 63) is a substituted phenanthrene imidazole inhibitor of microsom |
| reagent | reagents/ligands/minocycline/ | Minocycline | Minocycline is a tetracycline antibiotic (Mr ~457) that inhibits bacterial prote |
| reagent | reagents/ligands/misoprostol/ | Misoprostol | Misoprostol is a synthetic prostaglandin E1 analog used clinically as a uteroton |
| reagent | reagents/ligands/mittx/ | MitTx Toxin | MitTx (MITxin) is a heterodimeric toxin from the venom of the Texas coral snake  |
| reagent | reagents/ligands/mk-0812/ | MK-0812 | MK-0812 is a tetrahydropyranyl cyclopentyl tetrahydropyridopyridine derivative d |
| reagent | reagents/ligands/mk-0893/ | MK-0893 | MK-0893 is a potent glucagon receptor (GCGR) antagonist discovered by Merck for  |
| reagent | reagents/ligands/mk-591/ | MK-591 | MK-591 is a small-molecule inhibitor of 5-lipoxygenase-activating protein
| reagent | reagents/ligands/mk-801/ | MK-801 (Dizocilpine) | MK-801 (dizocilpine) is a non-competitive, open-channel blocker of N-methyl-[D-A |
| reagent | reagents/ligands/ml056/ | ML056 | ML056 is a selective agonist of the sphingosine-1-phosphate receptor 1 (S1P1). I |
| reagent | reagents/ligands/ml335/ | ML335 (N-aryl-sulfonamide K2P activator) | ML335 (N-[(2,4-dichlorophenyl)methyl]-4-(methanesulfonamido)benzamide) is a sele |
| reagent | reagents/ligands/ml402/ | ML402 (thiophene-carboxamide K2P activator) | ML402 (N-[2-(4-chloro-2-methylphenoxy)ethyl]thiophene-2-carboxamide) is a select |
| reagent | reagents/ligands/mp1104/ | MP1104 | MP1104 is a potent epoxymorphinan opioid agonist with an iodobenzamide substitue |
| reagent | reagents/ligands/mpep/ | MPEP (2-Methyl-6-(phenylethynyl)pyridine) | MPEP (2-methyl-6-(phenylethynyl)pyridine) is a potent, selective negative allost |
| reagent | reagents/ligands/mrs2500/ | MRS2500 | MRS2500 [(1'R,2'S,4'S,5'S)-4-(2-iodo-6-methylaminopurin-9-yl)-1-[(phosphato)meth |
| reagent | reagents/ligands/msx-2/ | MSX-2 | MSX-2 is a xanthine-based radioligand used for binding assays at adenosine recep |
| reagent | reagents/ligands/mt7/ | MT7 (Muscarinic Toxin 7) | MT7 is a 65-amino acid three-finger toxin (3FT) from the venom of the green mamb |
| reagent | reagents/ligands/mycobactin/ | Mycobactin (Fe-MBT) | Mycobactin (MBT) is a lipid-bound siderophore produced by mycobacteria for iron
| reagent | reagents/ligands/n-acetyl-s-geranylgeranyl-l-cysteine/ | N-Acetyl-S-Geranylgeranyl-L-Cysteine (AGGC) | N-Acetyl-S-geranylgeranyl-L-cysteine (AGGC) is a prenylcysteine substrate analog |
| reagent | reagents/ligands/n-desmethyltamoxifen/ | N-Desmethyltamoxifen | N-Desmethyltamoxifen (NM-Tam) is the primary metabolite of tamoxifen formed by N |
| reagent | reagents/ligands/n-methylscopolamine/ | N-methylscopolamine (NMS) | N-methylscopolamine (NMS) is a quaternary ammonium derivative of [Scopolamine](/ |
| reagent | reagents/ligands/n-n-dimethylurea/ | N,N'-Dimethylurea (DMU) | N,N'-Dimethylurea (DMU) is a urea analogue in which both amide nitrogen atoms ar |
| reagent | reagents/ligands/naltriben/ | Naltriben | Naltriben is a selective delta-opioid receptor (δ-OR) antagonist containing a cy |
| reagent | reagents/ligands/naltrindole/ | Naltrindole | Naltrindole is a selective delta-opioid receptor (δ-OR) antagonist containing a  |
| reagent | reagents/ligands/navarixin/ | Navarixin (SCH-527123 / MK-7123) | Navarixin (also known as SCH-527123 or MK-7123) is a small molecule antagonist
| reagent | reagents/ligands/nbmpr/ | NBMPR (S-(4-Nitrobenzyl)-6-thioinosine) | NBMPR (S-(4-Nitrobenzyl)-6-thioinosine) is a potent nucleoside-derived adenosine |
| reagent | reagents/ligands/ndt9513727/ | NDT9513727 | NDT9513727 is a non-peptide inverse agonist of the complement C5a receptor 1 ([H |
| reagent | reagents/ligands/neca/ | NECA | NECA (5'-N-ethylcarboxamidoadenosine) is a non-selective adenosine receptor agon |
| reagent | reagents/ligands/nemonapride/ | Nemonapride | Nemonapride is an antipsychotic drug that acts as a D2-like [Dopamine](/xray-mp- |
| reagent | reagents/ligands/neoxanthin/ | Neoxanthin | Neoxanthin is a [Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/) pigment |
| reagent | reagents/ligands/netupitant/ | Netupitant | Netupitant is an FDA-approved small-molecule antagonist of the human neurokinin  |
| reagent | reagents/ligands/neurotensin/ | Neurotensin | Neurotensin is an endogenous tridecapeptide (YLSRNKEDPKYYP) that acts as the pri |
| reagent | reagents/ligands/nicotine/ | Nicotine | Nicotine is a naturally occurring alkaloid produced in Nicotiana species as a na |
| reagent | reagents/ligands/nimodipine/ | Nimodipine | Nimodipine is a dihydropyridine calcium channel antagonist used for the treatmen |
| reagent | reagents/ligands/nisoxetine/ | Nisoxetine | Nisoxetine is a selective norepinephrine reuptake inhibitor (NRI) and antidepres |
| reagent | reagents/ligands/nitd-349/ | NITD-349 | NITD-349 (N-(4,4-dimethylcyclohexyl)-4,6-difluoro-1H-indole-2-carboxamide) is an |
| reagent | reagents/ligands/nn-c0640/ | NNC0640 | NNC0640 is a small-molecule negative allosteric modulator (NAM) that targets bot |
| reagent | reagents/ligands/no711/ | NO711 | NO711 (also known as NO-711 or NNC-711) is a potent and selective inhibitor of G |
| reagent | reagents/ligands/norepinephrine/ | Norepinephrine | Norepinephrine (also known as noradrenaline) is an endogenous catecholamine neur |
| reagent | reagents/ligands/nortriptyline/ | Nortriptyline | Nortriptyline is a tricyclic antidepressant (TCA) that acts as a potent inhibito |
| reagent | reagents/ligands/oleoyl-coa/ | Oleoyl-CoA | Oleoyl-CoA (18:1-CoA) is the monounsaturated product of the [Stearoyl-CoA](/xray |
| reagent | reagents/ligands/oligomycin/ | Oligomycin | Oligomycin is a macrolide antibiotic that potently inhibits the mitochondrial F1 |
| reagent | reagents/ligands/olmesartan/ | Olmesartan | Olmesartan is a clinically used angiotensin receptor blocker (ARB) featuring a b |
| reagent | reagents/ligands/onb-hydroxyaspartate/ | ONB-hydroxyaspartate (o-nitrobenzyl-hydroxyaspartate) | ONB-hydroxyaspartate is a photocaged compound consisting of beta-hydroxyaspartat |
| reagent | reagents/ligands/ono-3080573/ | ONO-3080573 | ONO-3080573 is a selective antagonist of the lysophosphatidic acid receptor 1 (L |
| reagent | reagents/ligands/ono-9780307/ | ONO-9780307 | ONO-9780307 is a selective antagonist of the lysophosphatidic acid receptor 1 (L |
| reagent | reagents/ligands/ono-9910539/ | ONO-9910539 | ONO-9910539 is a selective antagonist of the lysophosphatidic acid receptor 1 (L |
| reagent | reagents/ligands/orthovanadate/ | Orthovanadate (VO₃⁻) | Orthovanadate (VO₃⁻) is the monomeric form of vanadate and a potent inhibitor of |
| reagent | reagents/ligands/ouabain/ | Ouabain | Ouabain is a cardiotonic steroid (cardiac glycoside) that specifically inhibits  |
| reagent | reagents/ligands/p-ome-azo-tboa/ | p-OMe-azo-TBOA (4-methoxyazobenzene-TBOA) | p-OMe-azo-[TBOA](/xray-mp-wiki/reagents/ligands/tboa/) is a photoswitchable azob |
| reagent | reagents/ligands/paclitaxel/ | Paclitaxel | Paclitaxel (Taxol) is a microtubule-stabilizing antimitotic agent widely used in |
| reagent | reagents/ligands/paroxetine/ | Paroxetine | Paroxetine is a selective [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/ |
| reagent | reagents/ligands/pc-tx1/ | Pilidium Toxin 1 (PcTx1) | Pilidium toxin 1 (PcTx1) is a 37-amino-acid peptide toxin from the venom of the  |
| reagent | reagents/ligands/pd144418/ | PD144418 | PD144418 is a high-affinity, selective sigma-1 receptor antagonist used in struc |
| reagent | reagents/ligands/pentachlorophenol/ | Pentachlorophenol (PCP) | Pentachlorophenol (PCP) is a chlorinated phenolic compound that functions as a q |
| reagent | reagents/ligands/peptide-5/ | Peptide 5 (Truncated GLP-1 Agonist Nonapeptide) | Peptide 5 is a truncated GLP-1 receptor agonist nonapeptide designed for structu |
| reagent | reagents/ligands/pf-03716556/ | PF-03716556 | PF-03716556 is a potassium-competitive acid blocker (P-CAB) of the imidazopyridi |
| reagent | reagents/ligands/pf-06372222/ | PF-06372222 | PF-06372222 is a negative allosteric modulator (NAM) of the human glucagon-like  |
| reagent | reagents/ligands/pg-934/ | PG-934 | PG-934 is a seven-residue macrocyclic peptide antagonist of the human melanocort |
| reagent | reagents/ligands/phenindione/ | Phenindione | Phenindione is a vitamin K antagonist belonging to the 1,3-indandione class, use |
| reagent | reagents/ligands/photoNECA-blue/ | trans-photoNECA (blue) | trans-photoNECA (blue) is a novel photoswitchable ligand designed for  structura |
| reagent | reagents/ligands/pirenzepine/ | Pirenzepine | Pirenzepine is a selective muscarinic [Acetylcholine](/xray-mp-wiki/reagents/lig |
| reagent | reagents/ligands/pk11195/ | PK11195 | PK11195 is an isoquinoline carboxamide ligand that binds to the translocator pro |
| reagent | reagents/ligands/plastoquinone/ | Plastoquinone | Plastoquinone (PQ) is a lipophilic benzoquinone electron carrier in the photosyn |
| reagent | reagents/ligands/preladenant/ | Preladenant | Preladenant (SCH-420814) is a potent, highly selective non-xanthine antagonist o |
| reagent | reagents/ligands/propofol/ | Propofol | Propofol (2,6-diisopropylphenol) is a widely used intravenous general anesthetic |
| reagent | reagents/ligands/prostaglandin-d2/ | Prostaglandin D2 (PGD2) | Prostaglandin D2 (PGD2) is an endogenous eicosanoid signaling lipid derived from |
| reagent | reagents/ligands/prostaglandin-e2/ | Prostaglandin E2 (PGE2, Dinoprostone) | Prostaglandin E2 (PGE2, dinoprostone) is the most abundant prostanoid in the hum |
| reagent | reagents/ligands/protoporphyrin-ix/ | Protoporphyrin IX (PpIX) | Protoporphyrin IX (PpIX) is an endogenous porphyrin compound that serves as a na |
| reagent | reagents/ligands/psb-2113/ | PSB-2113 (PEGylated Preladenant) | PSB-2113 is a PEGylated derivative of [Preladenant](/xray-mp-wiki/reagents/ligan |
| reagent | reagents/ligands/psb36/ | PSB36 | PSB36 is a selective adenosine A1 receptor antagonist with a 3-hydroxy-propyl gr |
| reagent | reagents/ligands/pyridinium-3-5-biscarboxylic-acid-mononucleotide/ | Pyridinium-3,5-Biscarboxylic Acid Mononucleotide (P2CMN) | Pyridinium-3,5-biscarboxylic acid mononucleotide (P2CMN) is the direct product o |
| reagent | reagents/ligands/r-r-2b/ | (R,R)-2b | (R,R)-2b is a high-affinity positive allosteric modulator (PAM) of AMPA-subtype  |
| reagent | reagents/ligands/ramatroban/ | Ramatroban | Ramatroban (BAY U 3405) is a nonprostanoid antagonist of the thromboxane A2 rece |
| reagent | reagents/ligands/reboxetine/ | Reboxetine | Reboxetine is a selective norepinephrine reuptake inhibitor (NRI) and antidepres |
| reagent | reagents/ligands/resiniferatoxin/ | Resiniferatoxin (RTx) | Resiniferatoxin (RTx) is an ultrapotent vanilloid toxin derived from the latex o |
| reagent | reagents/ligands/retinal/ | Retinal | Retinal (vitamin A aldehyde) is the light-absorbing chromophore covalently bound |
| reagent | reagents/ligands/revaprazan/ | Revaprazan | Revaprazan is a potassium-competitive acid blocker (P-CAB) with a pyrimidine-bas |
| reagent | reagents/ligands/rhodamine-6g/ | Rhodamine 6G - Fluorescent Xanthene Dye | Rhodamine 6G is a fluorescent xanthene dye widely used as a substrate probe for  |
| reagent | reagents/ligands/rifampicin/ | Rifampicin | Rifampicin is a high-molecular-mass antibiotic (Mr ~823) that inhibits bacterial |
| reagent | reagents/ligands/rimantadine/ | Rimantadine | Rimantadine is a racemic adamantyl-amine antiviral drug that inhibits the M2 pro |
| reagent | reagents/ligands/rimonabant/ | Rimonabant | Rimonabant is a cannabinoid CB1 receptor antagonist that was approved by the Eur |
| reagent | reagents/ligands/risperidone/ | Risperidone | Risperidone is an atypical antipsychotic drug with a benzisoxazole scaffold. It  |
| reagent | reagents/ligands/ro25-6981/ | Ro25-6981 | Ro25-6981 is a potent, GluN2B-selective negative allosteric modulator (NAM) of N |
| reagent | reagents/ligands/rolofylline/ | Rolofylline | Rolofylline is a selective adenosine A1 receptor antagonist with a 3-nor-adamant |
| reagent | reagents/ligands/rostafuroxin/ | Rostafuroxin | Rostafuroxin (ROS) is a novel cardiotonic steroid (CTS) developed as a potential |
| reagent | reagents/ligands/rti-3a/ | RTI-3a (Partial NTSR1 Agonist) | RTI-3a is a nonpeptide partial agonist of the rat [Neurotensin](/xray-mp-wiki/re |
| reagent | reagents/ligands/rti-55/ | RTI-55 | RTI-55 (2-beta-carbomethoxy-3-beta-(4-iodophenyl)tropane) is a tropane alkaloid  |
| reagent | reagents/ligands/s-5-nitrowillardine/ | (S)-5-Nitrowillardine (NOW) | (S)-5-Nitrowillardine (NOW) is a partial agonist of AMPA-subtype ionotropic glut |
| reagent | reagents/ligands/s-citalopram/ | (S)-Citalopram | (S)-Citalopram is the pharmacologically active enantiomer of citalopram, a selec |
| reagent | reagents/ligands/s1i8/ | S1I8 Peptide | S1I8 (Sarcosine1, Isoleucine8-Angiotensin II) is a partial agonist peptide analo |
| reagent | reagents/ligands/s1p/ | S1P (Sphingosine-1-Phosphate) | Sphingosine-1-phosphate (S1P) is a bioactive lysophospholipid signaling molecule |
| reagent | reagents/ligands/sag1.5/ | SAG1.5 | SAG1.5 (3-chloro-4,7-difluoro-N-[trans-4-(methylamino)cyclohexyl]-N-[[3-(4-pyrid |
| reagent | reagents/ligands/salbutamol/ | Salbutamol (Albuterol) | Salbutamol (also known as albuterol in the United States) is a synthetic catecho |
| reagent | reagents/ligands/salinixanthin/ | Salinixanthin | Salinixanthin is a C40-[Carotenoid](/xray-mp-wiki/reagents/ligands/carotenoid/)  |
| reagent | reagents/ligands/salvinorin-a/ | Salvinorin A | Salvinorin A (SalA) is a selective kappa opioid receptor (KOP) agonist derived f |
| reagent | reagents/ligands/sant1/ | SANT1 | SANT1 (N-[(1E)-(3,5-dimethyl-1-phenyl-1H-pyrazol-4-yl)methylidene]-4-(phenylmeth |
| reagent | reagents/ligands/sb-334867/ | SB-334867 | SB-334867 is the first selective orexin-1 receptor antagonist (1-SORA) disclosed |
| reagent | reagents/ligands/sb-408124/ | SB-408124 | SB-408124 is a selective [UREA](/xray-mp-wiki/reagents/substrates/urea/) antagon |
| reagent | reagents/ligands/sb-674042/ | SB-674042 | SB-674042 is a selective orexin 1 receptor antagonist (SORA) with high affinity  |
| reagent | reagents/ligands/sbl-mc-31/ | SBL-MC-31 | SBL-MC-31 is a newly synthesized seven-residue macrocyclic peptide antagonist of |
| reagent | reagents/ligands/scopolamine/ | Scopolamine | Scopolamine (hyoscyamine) is a non-selective muscarinic receptor antagonist that |
| reagent | reagents/ligands/selatogrel/ | Selatogrel | Selatogrel (ACT-246475) is a potent, reversible, and highly selective inverse ag |
| reagent | reagents/ligands/selenocyanobarbital/ | Selenocyanobarbital | Selenocyanobarbital is a synthetic barbiturate derivative containing a selenium  |
| reagent | reagents/ligands/serotonin/ | Serotonin (5-Hydroxytryptamine, 5-HT) | Serotonin (5-hydroxytryptamine, 5-HT) is a biogenic amine neurotransmitter that  |
| reagent | reagents/ligands/sertraline/ | Sertraline | Sertraline is a selective [Serotonin (5-Hydroxytryptamine, 5-HT)](/xray-mp-wiki/ |
| reagent | reagents/ligands/shu9119/ | SHU9119 | SHU9119 is a six-residue macrocyclic peptide antagonist of melanocortin receptor |
| reagent | reagents/ligands/skf89976a/ | SKF89976a | SKF89976a is a potent inhibitor of GABA transporter 1 (GAT1) with a unique dual  |
| reagent | reagents/ligands/slv320/ | SLV320 | SLV320 is a selective adenosine A1 receptor antagonist with a unique pyrrolopyri |
| reagent | reagents/ligands/sodium-ion/ | Sodium Ion (Na+) | Sodium ion (Na+) serves as a negative allosteric modulator in many class A G pro |
| reagent | reagents/ligands/soraprazan/ | Soraprazan | Soraprazan is a potassium-competitive acid blocker (P-CAB) of the imidazonaphthy |
| reagent | reagents/ligands/spiperone/ | Spiperone | Spiperone is a typical antipsychotic drug of the butyrophenone class with high a |
| reagent | reagents/ligands/spiro-adamantyl-amine/ | Spiro-Adamantyl Amine | Spiro-adamantyl amine is a member of the adamantyl-amine class of [Influenza A M |
| reagent | reagents/ligands/spiro/ | SPIRO | SPIRO (1-((2,3-dihydrobenzobdioxin-6-yl)methyl)-6',7'-dihydrospiro[piperidine-4, |
| reagent | reagents/ligands/sq109/ | SQ109 | SQ109 (N-[1-(2,6-dioxopiperidin-3-yl)-1-(4-fluorophenyl)ethyl]-N-(2-(piperidin-1 |
| reagent | reagents/ligands/sr142948/ | SR142948 | SR142948 is a non-peptide neurotensin receptor antagonist. In the structural
| reagent | reagents/ligands/sr48692/ | SR48692 | SR48692 is a potent, selective, non-peptide antagonist of the neurotensin recept |
| reagent | reagents/ligands/sri-9829/ | SRI-9829 (Full NTSR1 Agonist) | SRI-9829 is a novel nonpeptide full agonist of the rat [Neurotensin](/xray-mp-wi |
| reagent | reagents/ligands/stearoyl-coa/ | Stearoyl-CoA | Stearoyl-coenzyme A (stearoyl-CoA) is a fatty acyl-CoA thioester consisting of a |
| reagent | reagents/ligands/strychnine/ | Strychnine | Strychnine is a potent indole alkaloid antagonist of the glycine receptor (GlyR) |
| reagent | reagents/ligands/succinate/ | Succinate (Succinic Acid) | Succinate (succinic acid) is a small dicarboxylic acid and a crucial intermediat |
| reagent | reagents/ligands/sucrose/ | Sucrose | Sucrose is a non-reducing disaccharide composed of glucose and fructose units li |
| reagent | reagents/ligands/suvorexant/ | Suvorexant | Suvorexant is a dual orexin receptor antagonist (DORA) with subnanomolar affinit |
| reagent | reagents/ligands/t-acbd/ | t-ACBD (trans-1-Aminocyclobutane-1,3-dicarboxylic Acid) | t-ACBD (trans-1-aminocyclobutane-1,3-dicarboxylic acid) is a cyclic amino acid t |
| reagent | reagents/ligands/tak-875/ | TAK-875 (Fasiglifam) | TAK-875 (fasiglifam) is an orally available, potent and selective partial agonis |
| reagent | reagents/ligands/tamoxifen/ | Tamoxifen | Tamoxifen is a triphenylethylene-based selective estrogen receptor modulator (SE |
| reagent | reagents/ligands/taniborbactam/ | Taniborbactam (VNRX-5133) | Taniborbactam (VNRX-5133) is a boronic acid-based beta-lactamase inhibitor with  |
| reagent | reagents/ligands/taranabant/ | Taranabant | Taranabant is a potent, selective CB1 receptor inverse agonist used for structur |
| reagent | reagents/ligands/tboa/ | DL-threo-beta-Benzyloxyaspartic Acid (TBOA) | TBOA (DL-threo-beta-Benzyloxyaspartic acid) is a competitive transport blocker o |
| reagent | reagents/ligands/tc114/ | TC114 (SMO Ligand) | TC114 is a designed small-molecule ligand for the human smoothened (SMO) recepto |
| reagent | reagents/ligands/tdg/ | Thiodigalactoside (TDG) | Thiodigalactoside (TDG) is a non-hydrolyzable galactoside analog used as a high- |
| reagent | reagents/ligands/tegoprazan/ | Tegoprazan | Tegoprazan is a potassium-competitive acid blocker (P-CAB) belonging to the benz |
| reagent | reagents/ligands/telmisartan/ | Telmisartan | Telmisartan is a clinically used angiotensin receptor blocker (ARB) that uniquel |
| reagent | reagents/ligands/tetrabutylammonium-bromide/ | Tetrabutylammonium Bromide (TBSb) | [TBA](/xray-mp-wiki/reagents/ligands/tetrabutylammonium/) bromide (TBSb) is a qu |
| reagent | reagents/ligands/tetrabutylammonium/ | Tetrabutylammonium (TBA) | Tetrabutylammonium (TBA) is a quaternary ammonium compound that acts as a potent |
| reagent | reagents/ligands/tetraethylammonium/ | Tetraethylammonium (TEA) | Tetraethylammonium (TEA) is a quaternary ammonium compound that acts as a potent |
| reagent | reagents/ligands/tetramethylammonium/ | Tetramethylammonium (TMA) | Tetramethylammonium (TMA) is the smallest quaternary ammonium compound used as a |
| reagent | reagents/ligands/th-pf01/ | TH-PF01 (Orthosteric–Allosteric Dual PfHT1 Inhibitor) | TH-PF01 is a lead compound from the TH-PF series of orthosteric–allosteric dual  |
| reagent | reagents/ligands/th-pf02/ | TH-PF02 (Orthosteric–Allosteric Dual PfHT1 Inhibitor) | TH-PF02 is a lead compound from the TH-PF series of orthosteric–allosteric dual  |
| reagent | reagents/ligands/th-pf03/ | TH-PF03 (Orthosteric–Allosteric Dual PfHT1 Inhibitor) | TH-PF03 is the most potent lead compound from the TH-PF series of orthosteric– a |
| reagent | reagents/ligands/thapsigargin/ | Thapsigargin | Thapsigargin is a sesquiterpene lactone that acts as a specific, non-competitive |
| reagent | reagents/ligands/theophylline/ | Theophylline | Theophylline (1,3-dimethylxanthine) is a non-selective, weak antagonist of adeno |
| reagent | reagents/ligands/thiopental/ | Thiopental | Thiopental is a clinically used barbiturate anesthetic. It contains a sulfur ato |
| reagent | reagents/ligands/ticagrelor/ | Ticagrelor | Ticagrelor is a reversible, market-approved antagonist of the [Human P2Y12 Recep |
| reagent | reagents/ligands/tiotropium/ | Tiotropium | Tiotropium is a long-acting anticholinergic medication used in the maintenance t |
| reagent | reagents/ligands/tnp-atp/ | 2'3'-O-(4,5-Dinitrobenzoyl)adenosine 5'-triphosphate (TNP-ATP) | TNP-ATP is a fluorescent analog of adenosine triphosphate (ATP) in which the ade |
| reagent | reagents/ligands/trv023/ | TRV023 | TRV023 is a beta-arrestin-biased peptide agonist of the angiotensin II type 1 re |
| reagent | reagents/ligands/trv026/ | TRV026 | TRV026 is a beta-arrestin-biased peptide agonist of the angiotensin II type 1 re |
| reagent | reagents/ligands/tungstate/ | Tungstate (WO4 2-) | Tungstate (WO4 2-) is a structural analog of inorganic phosphate (Pi) and inorga |
| reagent | reagents/ligands/tx24/ | Tx24 (Engineered M2-Selective Muscarinic Toxin) | Tx24 is an engineered variant of [MT7](/xray-mp-wiki/reagents/ligands/mt7/) with |
| reagent | reagents/ligands/u18666a/ | U18666A | U18666A is a [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) biosynthe |
| reagent | reagents/ligands/ubiquinone-1/ | Ubiquinone-1 (UQ1) | Ubiquinone-1 (UQ1) is the one-isoprenoid-unit variant of [Ubiquinone](/xray-mp-w |
| reagent | reagents/ligands/ubiquinone-2/ | Ubiquinone-2 | Ubiquinone-2 (Q-2, Coenzyme Q-2) is a short-chain ubiquinone homolog with
| reagent | reagents/ligands/uk-432097/ | UK-432097 | UK-432097 (2-(3-[1-(pyridin-2-yl)piperidin-4-yl]ureido)ethyl-6-N-(2,2-diphenylet |
| reagent | reagents/ligands/uk-59811/ | UK-59811 | UK-59811 is a brominated dihydropyridine calcium channel antagonist. The bromine |
| reagent | reagents/ligands/uracil/ | Uracil | Uracil is a pyrimidine base and the natural substrate of the uracil:proton sympo |
| reagent | reagents/ligands/valacyclovir/ | Valacyclovir | Valacyclovir (trade names Valtrex, Zelitrex) is a prodrug derivative of the anti |
| reagent | reagents/ligands/valinomycin/ | Valinomycin | Valinomycin is a macyclic ionophore antibiotic that selectively transports potas |
| reagent | reagents/ligands/valsartan/ | Valsartan | Valsartan is a clinically used angiotensin receptor blocker (ARB) featuring a bi |
| reagent | reagents/ligands/verapamil/ | Verapamil | Verapamil is a phenylalkylamine calcium channel blocker and one of the earliest  |
| reagent | reagents/ligands/violaxanthin/ | Violaxanthin | Violaxanthin is a xanthophyll [Carotenoid](/xray-mp-wiki/reagents/ligands/carote |
| reagent | reagents/ligands/vismodegib/ | Vismodegib (GDC-0449) | Vismodegib (GDC-0449) is an FDA-approved small-molecule antagonist of the smooth |
| reagent | reagents/ligands/vmip-ii/ | vMIP-II (Viral CC Chemokine Antagonist) | vMIP-II is a CC chemokine encoded by Kaposi's sarcoma-associated herpesvirus (KS |
| reagent | reagents/ligands/vorapaxar/ | Vorapaxar | Vorapaxar is a functionally irreversible small-molecule antagonist of the human  |
| reagent | reagents/ligands/w-54011/ | W-54011 | W-54011 is a small-molecule competitive antagonist of the complement C5a recepto |
| reagent | reagents/ligands/warfarin/ | Warfarin | Warfarin is a coumarin-derived anticoagulant drug that acts as a competitive inh |
| reagent | reagents/ligands/z-4-hydroxytamoxifen/ | Z-4-Hydroxytamoxifen | Z-4-Hydroxytamoxifen is the Z-isomer of 4-hydroxytamoxifen, a primary metabolite |
| reagent | reagents/ligands/z-endoxifen/ | Z-Endoxifen | Z-Endoxifen is the Z-isomer of endoxifen (4-hydroxy-N-desmethyltamoxifen), the p |
| reagent | reagents/ligands/zcz011/ | ZCZ011 | ZCZ011 is a positive allosteric modulator (PAM) of the cannabinoid receptor CB1. |
| reagent | reagents/ligands/zd7155/ | ZD7155 | ZD7155 is a high-affinity, selective non-peptide antagonist of the angiotensin I |
| reagent | reagents/ligands/zm241385/ | ZM241385 | ZM241385 is a bicyclic xanthine-based antagonist of the adenosine A2A receptor ( |
| reagent | reagents/ligands/zotepine/ | Zotepine | Zotepine is a second-generation antipsychotic drug with a dibenzothiepine scaffo |
| reagent | reagents/lipids/20s-hydroxycholesterol/ | 20(S)-Hydroxycholesterol (20S-OHC) | 20(S)-hydroxycholesterol (20S-OHC) is a cholesterol-derived oxysterol that acts  |
| reagent | reagents/lipids/6-ddtre/ | 6-n-Dodecyl-alpha,alpha-trehalose (6-DDTre) | 6-n-Dodecyl-alpha,alpha-[Trehalose](/xray-mp-wiki/reagents/additives/trehalose/) |
| reagent | reagents/lipids/7-10-mag/ | 7.10 MAG | 7.10 MAG (7.10 monoacylglycerol) is a novel monoacylglycerol lipid developed for |
| reagent | reagents/lipids/bacterioruberin/ | Bacterioruberin | Bacterioruberin is a C50 carotenoid pigment found in halophilic archaea. It abso |
| reagent | reagents/lipids/cardiolipin/ | Cardiolipin | Cardiolipin (CL), also known as diphosphatidylglycerol, is a unique anionic
| reagent | reagents/lipids/ceramide/ | Ceramide | Ceramide is a sphingolipid composed of a [Sphingosine](/xray-mp-wiki/reagents/li |
| reagent | reagents/lipids/cholesterol/ | Cholesterol | Cholesterol is a sterol lipid and essential component of eukaryotic cell membran |
| reagent | reagents/lipids/cytidine-diphosphate-diacylglycerol/ | Cytidine Diphosphate Diacylglycerol | Cytidine diphosphate-diacylglycerol (CDP-[DAG](/xray-mp-wiki/reagents/lipids/dag |
| reagent | reagents/lipids/dag/ | Diacylglycerol (DAG) | Diacylglycerol (DAG) is a lipid signaling molecule composed of two fatty acyl ch |
| reagent | reagents/lipids/diacylglycerol/ | Diacylglycerol | Diacylglycerol (DAG) is a glycerolipid consisting of two fatty acid chains ester |
| reagent | reagents/lipids/digalactosyl-diacylglycerol/ | Digalactosyl Diacylglycerol | Digalactosyl diacylglycerol (DGDG) is a galactolipid consisting of a digalactose |
| reagent | reagents/lipids/dioctanoyl-ppa/ | Dioctanoyl Glycerol Pyrophosphatidic Acid (PPA) | Dioctanoyl glycerol pyrophosphatidic acid (PPA) is a small anionic lipid with a  |
| reagent | reagents/lipids/dmpc/ | DMPC (Dimyristoyl Phosphatidylcholine) | DMPC (1,2-dimyristoyl-sn-glycero-3-phosphocholine) is a diacyl phospholipid with |
| reagent | reagents/lipids/dopc/ | 1,2-Dioleoyl-sn-glycero-3-phosphocholine (DOPC) | 1,2-Dioleoyl-sn-glycero-3-phosphocholine (DOPC) is a synthetic phospholipid with |
| reagent | reagents/lipids/dope/ | 1,2-Dioleoyl-sn-glycero-3-phosphoethanolamine (DOPE) | DOPE (1,2-dioleoyl-sn-glycero-3-phosphoethanolamine) is a zwitterionic
| reagent | reagents/lipids/dopg/ | 1,2-Dioleoyl-sn-glycero-3-phospho-(1'-rac-glycerol) (DOPG) | DOPG (1,2-dioleoyl-sn-glycero-3-phospho-(1'-rac-glycerol)) is a diacyl
| reagent | reagents/lipids/e-coli-polar-lipids/ | E. coli Polar Lipids | E. coli polar lipids are a mixture of phospholipids extracted from Escherichia c |
| reagent | reagents/lipids/erococ-17-4/ | EROCOC17+4 (Isoprenoid-Chained Lipid) | EROCOC17+4 is an isoprenoid-chained lipid (IPCL) consisting of an erythritol hea |
| reagent | reagents/lipids/glycolipid/ | Glycolipid | Glycolipids are lipids with attached carbohydrate groups, used as membrane mimet |
| reagent | reagents/lipids/lipid-a/ | Lipid A | Lipid A is the hydrophobic anchor of lipopolysaccharide (LPS) in the outer membr |
| reagent | reagents/lipids/lysophosphatidylcholine/ | Lysophosphatidylcholine (LPC) | Lysophosphatidylcholine (LPC) is a monoacyl phospholipid consisting of a [Glycer |
| reagent | reagents/lipids/mag-8.7/ | MAG 8.7 (Monoolein, Avanti) | [MAG](/xray-mp-wiki/reagents/lipids/mag/) 8.7 is a monoglyceride lipid (1-monool |
| reagent | reagents/lipids/mag/ | Monoacylglycerol (MAG) | Monoacylglycerol (MAG), specifically 7.9 MAG (a mixture with average chain lengt |
| reagent | reagents/lipids/monogalactosyl-diacylglycerol/ | Monogalactosyl Diacylglycerol (MGDG) | Monogalactosyl diacylglycerol (MGDG) is the most abundant lipid in thylakoid mem |
| reagent | reagents/lipids/monoolein/ | Monoolein | Monoolein (mono-oleoyl-glycerol) is a monoacyl lipid used for preparing the lipi |
| reagent | reagents/lipids/monopalmitolein/ | Monopalmitolein | Monopalmitolein (9.7 MAG, 1-(9Z-hexadecenoyl)-rac-glycerol) is a monoacylglycero |
| reagent | reagents/lipids/monovaccenin/ | Monovaccenin | Monovaccenin (11.7 MAG, 1-(11Z-octadecenoyl)-rac-glycerol) is a monoacylglycerol |
| reagent | reagents/lipids/nbd-pe/ | NBD-Phosphatidylethanolamine (NBD-PE) | NBD-[Phosphatidylethanolamine](/xray-mp-wiki/reagents/lipids/phosphatidylethanol |
| reagent | reagents/lipids/nbd-ps/ | NBD-Phosphatidylserine (NBD-PS) | NBD-[Phosphatidylserine](/xray-mp-wiki/reagents/lipids/phosphatidylserine/) (NBD |
| reagent | reagents/lipids/oleic-acid/ | Oleic Acid | Oleic acid is a monounsaturated omega-9 fatty acid (cis-9-octadecenoic acid, C18 |
| reagent | reagents/lipids/phosphatidic-acid/ | Phosphatidic Acid | Phosphatidic acid (PA) is the simplest phospholipid, consisting of a diacylglyce |
| reagent | reagents/lipids/phosphatidylcholine/ | Phosphatidylcholine | Phosphatidylcholine (PC) is a major class of phospholipids found in cell membran |
| reagent | reagents/lipids/phosphatidylethanolamine/ | Phosphatidylethanolamine | Phosphatidylethanolamine (PE) is a glycerophospholipid consisting of a diglyceri |
| reagent | reagents/lipids/phosphatidylglycerol-phosphate/ | Phosphatidylglycerol Phosphate | [Phosphatidylglycerol](/xray-mp-wiki/reagents/lipids/phosphatidylglycerol/) phos |
| reagent | reagents/lipids/phosphatidylglycerol/ | Phosphatidylglycerol | Phosphatidylglycerol (PG) is a glycerophospholipid consisting of a diglyceride b |
| reagent | reagents/lipids/phosphatidylinositol-4-5-bisphosphate/ | Phosphatidylinositol-4,5-Bisphosphate (PIP2) | Phosphatidylinositol-4,5-bisphosphate (PIP2, also known as PtdIns(4,5)P2) is an  |
| reagent | reagents/lipids/phosphatidylinositol/ | Phosphatidylinositol | Phosphatidylinositol (PI) is an acidic phospholipid consisting of a diacylglycer |
| reagent | reagents/lipids/phosphatidylserine/ | Phosphatidylserine | L-alpha-phosphatidylserine is a negatively charged phospholipid used as a crysta |
| reagent | reagents/lipids/popc/ | POPC (1-Palmitoyl-2-oleoyl-sn-glycero-3-phosphocholine) | POPC (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphocholine) is a synthetic phospholi |
| reagent | reagents/lipids/pope/ | POPE (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine) | POPE (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine) is a zwitterionic p |
| reagent | reagents/lipids/popg/ | 1-Palmitoyl-2-Oleoylphosphatidylglycerol (POPG) | 1-Palmitoyl-2-oleoylphosphatidylglycerol (POPG) is a diacyl phospholipid with a  |
| reagent | reagents/lipids/sphingosine/ | Sphingosine | Sphingosine (D-erythro-sphingosine, d18:1) is a sphingoid base that serves as th |
| reagent | reagents/lipids/squalane/ | Squalane | Squalane (C30H62) is a fully saturated hydrocarbon (2,6,10,15,19,23-
| reagent | reagents/lipids/squalene/ | Squalene | Squalene is a linear triterpene lipid found in Halobacterium salinarum purple me |
| reagent | reagents/lipids/stigmasterol/ | Stigmasterol | Stigmasterol is a plant sterol (phytosterol) and a dietary component found in ve |
| reagent | reagents/lipids/sulfoquinovosyl-diacylglycerol/ | Sulfoquinovosyl Diacylglycerol (SQDG) | Sulfoquinovosyl diacylglycerol (SQDG) is an anionic galactolipid found in thylak |
| reagent | reagents/protein-tags/bril/ | BRIL (Thermostabilized Apocytochrome b562RIL) | BRIL (b562RIL) is a thermostabilized variant of apocytochrome b562 from
| reagent | reagents/protein-tags/darpin/ | Designed Ankyrin Repeat Protein (DARPin) | Designed ankyrin repeat proteins (DARPins) are engineered, non-immunoglobulin bi |
| reagent | reagents/protein-tags/flag-tag/ | FLAG Tag | The FLAG tag is a short peptide epitope tag (DYKDDDDK) commonly used for affinit |
| reagent | reagents/protein-tags/gfp/ | Green Fluorescent Protein (GFP) | Green Fluorescent Protein (GFP) from the jellyfish Aequorea victoria is widely u |
| reagent | reagents/protein-tags/his6-tag/ | Polyhistidine Tag (His6) | The polyhistidine tag (His6) is a short peptide sequence of six consecutive hist |
| reagent | reagents/protein-tags/monobody-l2/ | Monobody L2 | Monobody L2 is an engineered protein inhibitor selected from a combinatorial lib |
| reagent | reagents/protein-tags/monobody-l3/ | Monobody L3 | Monobody L3 is an engineered fibronectin type III domain (FN3) protein selected  |
| reagent | reagents/protein-tags/monobody-mb15/ | MB-15 Monobody | MB-15 is a synthetic ICMT-binding monobody engineered as a crystallization chape |
| reagent | reagents/protein-tags/monobody-s7/ | Monobody S7 | Monobody S7 is an engineered protein inhibitor selected from a combinatorial lib |
| reagent | reagents/protein-tags/monobody-s8/ | Monobody S8 | Monobody S8 is an engineered fibronectin type III domain (FN3) protein selected  |
| reagent | reagents/protein-tags/monobody-s9/ | Monobody S9 | Monobody S9 is an engineered protein inhibitor selected from a combinatorial lib |
| reagent | reagents/protein-tags/nanobody/ | Nanobody | A nanobody is a single-domain antibody fragment derived from camelid heavy-chain |
| reagent | reagents/protein-tags/pgs-fusion/ | PGS (Pyrococcus abyssi Glycogen Synthase) Fusion | PGS (glycogen synthase from the hyperthermophilic archaeon Pyrococcus abyssi) is |
| reagent | reagents/protein-tags/pyrococcus-abyssi-glycogen-synthase/ | Pyrococcus abyssi Glycogen Synthase (PGS) | Pyrococcus abyssi glycogen synthase (PGS) is a 196-amino-acid protein from the h |
| reagent | reagents/protein-tags/rubredoxin/ | Rubredoxin Fusion Protein | Rubredoxin is a small iron-sulfur protein used as a fusion partner to replace th |
| reagent | reagents/protein-tags/sumo-tag/ | SUMO Tag (Small Ubiquitin-like Modifier) | SUMO (Small Ubiquitin-like Modifier) is a 11 kDa protein tag used to enhance sol |
| reagent | reagents/protein-tags/t4-lysozyme/ | T4 Lysozyme (T4L) | T4 lysozyme (T4L) is a fusion partner protein used to replace flexible intracell |
| reagent | reagents/protein-tags/thrombin-protease/ | Thrombin Protease | Thrombin is a serine protease that specifically cleaves at the sequence Leu-Val- |
| reagent | reagents/substrates/d-xylose/ | D-Xylose | D-Xylose is an aldopentose (five-carbon sugar) that serves as the natural substr |
| reagent | reagents/substrates/gdp-fucose/ | GDP-Fucose | GDP-fucose (guanosine 5'-diphosphate-[L-Fucose](/xray-mp-wiki/reagents/ligands/l |
| reagent | reagents/substrates/gdp-mannose/ | GDP-Mannose | GDP-mannose (guanosine 5'-diphosphate-alpha-D-mannose) is an activated sugar don |
| reagent | reagents/substrates/l-alanine/ | L-Alanine | L-Alanine is a small neutral amino acid that binds to the [LBD](/xray-mp-wiki/pr |
| reagent | reagents/substrates/l-arginine/ | L-Arginine | L-arginine is a basic, semi-essential amino acid that serves as the primary subs |
| reagent | reagents/substrates/l-aspartate/ | L-Aspartate | L-Aspartate is an acidic amino acid and a canonical agonist for ionotropic gluta |
| reagent | reagents/substrates/l-glutamate/ | L-Glutamate | L-Glutamate is the primary endogenous excitatory neurotransmitter and the canoni |
| reagent | reagents/substrates/l-serine/ | L-Serine | L-Serine is a polar neutral amino acid that binds to the [LBD](/xray-mp-wiki/pro |
| reagent | reagents/substrates/silicic-acid/ | Silicic Acid | Silicic acid (H4SiO4) is the bioavailable form of silicon in biological systems. |
| reagent | reagents/substrates/udp-glucose/ | UDP-Glucose (UDP-Glc) | UDP-[Glucose](/xray-mp-wiki/reagents/additives/glucose/) (UDP-Glc) is a nucleoti |
| reagent | reagents/substrates/urea/ | Urea | Urea (CH4N2O) is a small polar molecule with a strong dipole moment (4.6 D) that |
END WIKI CATALOG -->
