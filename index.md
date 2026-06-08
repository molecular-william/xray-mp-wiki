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
| concept | concepts/3-omega-motif/ | 3 Omega Motif in Microbial Rhodopsins | The 3 omega motif is a structural motif in microbial rhodopsins formed by three  |
| concept | concepts/abc-transporter-family/ | ABC Transporter Family | The ATP-binding cassette (ABC) transporter superfamily comprises a large group o |
| concept | concepts/abgt-family/ | AbgT Family of Transporters | The AbgT family is a large family of approximately 13,000 putative membrane tran |
| concept | concepts/agonist-to-antagonist-conversion/ | Agonist-to-Antagonist Conversion via C8 Modification | Concept: agonist-to-antagonist-conversion |
| concept | concepts/allosteric-regulation/ | Allosteric Regulation in Membrane Proteins | Allosteric regulation is a fundamental mechanism by which ligand binding at one  |
| concept | concepts/allosteric-site-in-nss-transporters/ | Allosteric Site in NSS Transporters | Concept: allosteric-site-in-nss-transporters |
| concept | concepts/alternating-access-mechanism/ | Alternating-Access Mechanism | The alternating-access mechanism is a fundamental principle of membrane transpor |
| concept | concepts/anion-channel-gating/ | Anion Channel Gating via Phenylalanine Gate | Anion channel gating via a conserved phenylalanine gate is a mechanism of ion ch |
| concept | concepts/anion-mediated-ligand-binding/ | Anion-Mediated Ligand Binding in iGluRs | Anion-mediated ligand binding is a mechanism in which chloride ions serve as sur |
| concept | concepts/antibiotic-efflux-pump/ | Antibiotic Efflux Pumps | Antibiotic efflux pumps are membrane transporters that export toxic compounds, i |
| concept | concepts/antiparallel-dimerization/ | Antiparallel Dimerization in GPCR Crystallization | Antiparallel dimerization in the context of GPCR crystallization refers to the a |
| concept | concepts/apc-superfamily/ | APC Superfamily (Amino Acid-Polyamine-Organocation Transporter Family) | The APC (amino acid-polyamine-organocation) superfamily comprises membrane trans |
| concept | concepts/aquaporin/ | Aquaporin Family | Aquaporins are water channel proteins that facilitate water transport across cel |
| concept | concepts/autoinhibitory-domains/ | Autoinhibitory Domains in Ion Pumps | Concept: autoinhibitory-domains |
| concept | concepts/ball-and-chain-model/ | Ball-and-Chain Model for SLC38A9 | The ball-and-chain model describes a conformational regulation mechanism in SLC3 |
| concept | concepts/bcct-family/ | BCCT Family (Betaine/Carnitine/Choline Transporter Family) | The BCCT (Betaine/Carnitine/Choline Transporter) family comprises secondary acti |
| concept | concepts/beta-arrestin-signaling/ | Beta-Arrestin Signaling | Concept: beta-arrestin-signaling |
| concept | concepts/biased-agonism/ | Biased Agonism in G Protein-Coupled Receptors | Biased agonism refers to the ability of different ligands to preferentially acti |
| concept | concepts/binder-clip-motion/ | Binder Clip Motion | Binder clip-like motion is a conformational mechanism in SemiSWEET and related S |
| concept | concepts/binding-change-mechanism/ | Binding-Change Mechanism | The binding-change mechanism is the catalytic mechanism proposed for ATP synthas |
| concept | concepts/biogenic-amine-transporters/ | Biogenic Amine Transporters | Biogenic amine transporters (BATs) are integral-membrane symporters that clear n |
| concept | concepts/blue-shifted-rhodopsin-design/ | Blue-Shifted Rhodopsin Design Principle | The blue-shifted rhodopsin design principle uses atomistic rational design to cr |
| concept | concepts/c-type-inactivation/ | C-type Inactivation | C-type inactivation is a gating process in potassium channels whereby prolonged  |
| concept | concepts/c41-e-coli-expression-strain/ | E. coli C41 Expression Strain | E. coli C41 is a genetically engineered expression strain derived from E. coli B |
| concept | concepts/carboxylate-dyad/ | Carboxylate Dyad in Oligosaccharyltransferase | The carboxylate dyad is a catalytic motif in oligosaccharyltransferase (OST) enz |
| concept | concepts/cardiotonic-steroids/ | Cardiotonic Steroids | Cardiotonic steroids (CTS), also known as cardiac glycosides, are a class of inh |
| concept | concepts/cdp-alcohol-phosphotransferase-family/ | CDP-Alcohol Phosphotransferase Family | Concept: cdp-alcohol-phosphotransferase-family |
| concept | concepts/central-core-disease/ | Central Core Disease and Ryanodine Receptor SPRY1 Domain | Central core disease (CCD) is a congenital myopathy associated with mutations in |
| concept | concepts/channel-gating/ | Channel Gating via Plug Domain Displacement | Channel gating in the SecY translocation channel is mediated by the displacement |
| concept | concepts/channel-like-mechanism/ | Channel-like Mechanism in Membrane Transport | Concept: channel-like-mechanism |
| concept | concepts/channelrhodopsin-photocycle/ | Channelrhodopsin Photocycle | The channelrhodopsin photocycle is a sequence of light-induced conformational an |
| concept | concepts/charge-transfer-interaction/ | Charge-Transfer Interaction | A charge-transfer interaction is a non-covalent interaction between an electron  |
| concept | concepts/cholesterol-dependent-cytolysins/ | Cholesterol-Dependent Cytolysins | Cholesterol-dependent cytolysins (CDCs) are a family of bacterial pore-forming t |
| concept | concepts/cl1-channel/ | Cl1 Proton Channel of Photosystem II | The Cl1 channel is a proton release pathway in Photosystem II (PSII) that connec |
| concept | concepts/conformational-coupling-gating/ | Conformational Coupling Between Activation Gate and Selectivity Filter | Conformational coupling between the activation gate and selectivity filter is a  |
| concept | concepts/conformational-dynamics-mfs/ | Conformational Dynamics in MFS Transporters | MFS transporters exhibit complex conformational dynamics, alternating between in |
| concept | concepts/conformational-dynamics-mppases/ | Conformational Dynamics in M-PPases | M-PPases (membrane-bound H+-pumping pyrophosphatases) undergo large-scale confor |
| concept | concepts/conserved-core-triad/ | Conserved Core Triad in GPCR Activation | The conserved core triad (FPI triad) consists of three highly conserved amino ac |
| concept | concepts/continuous-diffraction/ | Continuous Diffraction in Macromolecular Crystallography | Continuous diffraction refers to the incoherent sum of Fraunhofer diffraction pa |
| concept | concepts/cora-mg-transporter/ | CorA Mg2+ Transporter | CorA is a Mg2+ transporter that forms a pentameric structure. It uses a common p |
| concept | concepts/cork-in-bottle-occlusion/ | Cork-in-Bottle Occlusion | Cork-in-bottle occlusion is a mechanism of ion channel block in which a bound pr |
| concept | concepts/cpvt/ | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) and Ryanodine Receptor | Catecholaminergic polymorphic ventricular tachycardia (CPVT) is a genetic cardia |
| concept | concepts/cupin-fold/ | Cupin Fold | The cupin fold is a structural motif found in a large superfamily of proteins ch |
| concept | concepts/cys-loop-receptor-family/ | Cys-Loop Receptor Family | Concept: cys-loop-receptor-family |
| concept | concepts/darpin/ | Designed Ankyrin Repeat Protein (DARPin) | Concept: darpin |
| concept | concepts/desensitization-in-cys-loop-receptors/ | Desensitization in Cys-Loop Receptors | Desensitization is a fundamental regulatory mechanism in Cys-loop receptors wher |
| concept | concepts/di-iron-desaturase/ | Di-Iron-Containing Desaturase Family | The di-iron-containing desaturase family comprises enzymes that catalyze the int |
| concept | concepts/diiron-center-mechanism/ | Diiron Center Mechanism in Membrane Desaturases | The diiron center in membrane-bound desaturases, exemplified by stearoyl-CoA des |
| concept | concepts/dmt-superfamily/ | DMT Superfamily (Drug/Metabolite Transporter Superfamily) | The drug/metabolite transporter (DMT) superfamily is a large group of membrane t |
| concept | concepts/domain-swapping/ | Three-Dimensional Domain Swapping | Three-dimensional domain swapping occurs when a protein unfolds partially and ex |
| concept | concepts/drd2-extended-binding-pocket/ | DRD2 Extended Binding Pocket (DRD2-EBP) | Concept: drd2-extended-binding-pocket |
| concept | concepts/dtg-dts-rhodopsin/ | DTG/DTS Rhodopsin | DTG/DTS rhodopsins are a family of light-driven outward proton-pumping microbial |
| concept | concepts/dual-topology-channels/ | Dual-Topology Channels | Dual-topology channels are membrane protein complexes in which the subunits that |
| concept | concepts/ecf-transporter/ | ECF Transporter (Energy-Coupling Factor Transporter) | Energy-coupling factor (ECF) transporters are a unique family of membrane transp |
| concept | concepts/efficacy-switches/ | Efficacy Switches in GPCR Signaling | Efficacy switches are molecular mechanisms by which specific residues in G prote |
| concept | concepts/elevator-mechanism/ | Elevator Mechanism | Concept: elevator-mechanism |
| concept | concepts/entropic-spring-mechanism/ | Entropic Spring Mechanism in Tc Toxin Injection | The entropic spring mechanism describes how the linker connecting the shell and  |
| concept | concepts/epitaxial-twinning/ | Epitaxial Twinning | Epitaxial twinning is a crystallographic phenomenon in which two or more crystal |
| concept | concepts/er-retrieval-mechanism/ | ER Retrieval Mechanism (KDEL Receptor) | The ER retrieval mechanism involves KDEL receptors that bind to proteins with C- |
| concept | concepts/esx-1-secretion-system/ | ESX-1 Secretion System | The ESX-1 secretion system is a type VII protein secretion system in Mycobacteri |
| concept | concepts/extra-helical-binding-site/ | Extra-helical Binding Site in GPCRs | Concept: extra-helical-binding-site |
| concept | concepts/flickering-gate-mechanism/ | Flickering-Gate Mechanism | The flickering-gate mechanism proposes that the extracellular gate of P-type ATP |
| concept | concepts/fnt-family/ | FNT Family (Formate/Nitrite Transporter Family) | The FNT (formate/nitrite transporter) family comprises pentameric membrane chann |
| concept | concepts/force-from-lipid-principle/ | Force-from-Lipid Principle in Mechanosensation | The force-from-lipid (FFL) principle posits that mechanosensitive ion channels a |
| concept | concepts/gas-selectivity-filter/ | GAS Selectivity Filter | The GAS (Gly-Ala-Ser) selectivity filter is the ion selectivity determinant in a |
| concept | concepts/gating-modifier-toxin-binding/ | Gating Modifier Toxin Binding Mechanism | Concept: gating-modifier-toxin-binding |
| concept | concepts/glycine-gating-hinge/ | Glycine-Gating Hinge | The glycine-gating hinge is a conserved glycine residue located within the S6 in |
| concept | concepts/gpcr-active-conformation/ | GPCR Active Conformation | GPCRs adopt distinct active and inactive conformations. The active state is char |
| concept | concepts/gpcr-g-protein-coupling/ | GPCR-G Protein Coupling Mechanism | GPCR-G protein coupling is the fundamental mechanism by which G protein-coupled  |
| concept | concepts/gpcr-inactive-conformation/ | GPCR Inactive Conformation | The inactive conformation of G-protein-coupled receptors (GPCRs), also known as  |
| concept | concepts/gt-a-fold/ | GT-A Fold (Glycosyltransferase A Fold) | Concept: gt-a-fold |
| concept | concepts/gxgd-proteases/ | GXGD Proteases | Concept: gxgd-proteases |
| concept | concepts/gxxxg-motif/ | GXXXG Motif (Helix Packing Motif) | The GXXXG motif is a helix-helix packing motif commonly found in transmembrane p |
| concept | concepts/helical-recoil-desensitization/ | Helical Recoil Model of P2X Receptor Desensitization | The helical recoil model describes the molecular mechanism of P2X receptor desen |
| concept | concepts/helix-shift-mechanism/ | Helix Shift Mechanism for Carboxylate Drug Transport | The helix shift mechanism describes how carboxylate drugs are actively transport |
| concept | concepts/horizontal-helix-spring-mechanism/ | Horizontal Helix Spring Mechanism | The horizontal helix spring mechanism is a structural mechanism discovered in th |
| concept | concepts/intramembrane-ion-coordination/ | Intramembrane Ion Coordination | Intramembrane ion coordination refers to the phenomenon where metal cations (suc |
| concept | concepts/intramembrane-proteolysis/ | Intramembrane Proteolysis | Intramembrane proteolysis is the cleavage of peptide bonds within the hydrophobi |
| concept | concepts/intramolecular-salt-bridge/ | Intramolecular Salt Bridge | Concept: intramolecular-salt-bridge |
| concept | concepts/inverse-agonism/ | Inverse Agonism in GPCR Signaling | Inverse agonism refers to the ability of certain ligands to reduce the basal (co |
| concept | concepts/inward-facing-conformation/ | Inward-Facing Conformation of ABC Transporters | The inward-facing conformation is a structural state of ABC transporters in whic |
| concept | concepts/ion-release-pathway/ | Ion-Release Pathway in Copper-Transporting P-type ATPases | The ion-release pathway in copper-transporting P-type ATPases (P_IB ATPases) is  |
| concept | concepts/ionic-locks-mfs/ | Ionic Locks in MFS Transporters | Concept: ionic-locks-mfs |
| concept | concepts/k-lt-intermediate/ | K_LT Intermediate | The K_LT intermediate is a low-temperature photointermediate in the bacteriorhod |
| concept | concepts/k2p-modulator-pocket/ | K2P Modulator Pocket | Concept: k2p-modulator-pocket |
| concept | concepts/knock-off-mechanism/ | Knock-off Mechanism of Ion Permeation | The knock-off mechanism is a model of ion permeation through selectivity filters |
| concept | concepts/kok-cycle/ | Kok Cycle | The Kok cycle (also known as the S-state cycle) is the four-step mechanism of wa |
| concept | concepts/large-domain-motion-in-p-type-atpases/ | Large Domain Motion in P-type ATPases | Large domain motions are a fundamental feature of P-type ATPase function. The cy |
| concept | concepts/leu25-gatekeeper/ | Leu25 Gatekeeper Mechanism in NSS Transporters | The Leu25 gatekeeper is a conserved mechanism in the NSS (neurotransmitter:sodiu |
| concept | concepts/leut-return-state-mechanism/ | LeuT Return State Mechanism | The LeuT return state mechanism describes the inward-to-outward transition of th |
| concept | concepts/m2-conformational-equilibrium/ | M2 Proton Channel Conformational Equilibrium | The influenza A M2 proton channel exists in two principal conformational states: |
| concept | concepts/malignant-hyperthermia/ | Malignant Hyperthermia and Ryanodine Receptor Mutations | Malignant hyperthermia is a genetic disorder associated with mutations in the ry |
| concept | concepts/manganese-calcium-cluster/ | Manganese-Calcium Cluster (Mn4Ca Cluster) | The manganese-calcium cluster (Mn4Ca cluster) is the catalytic center of the oxy |
| concept | concepts/mate-transporter-family/ | MATE Transporter Family | Concept: mate-transporter-family |
| concept | concepts/mce-protein-family/ | MCE Protein Family | The MCE (mammalian cell entry) protein superfamily comprises highly conserved pr |
| concept | concepts/mechanosensitive-gating/ | Mechanosensitive Gating in Ion Channels | Mechanosensitive gating is a mechanism by which ion channels open or close in re |
| concept | concepts/membrane-mimetics/ | Membrane Mimetics and Structural Biology | Membrane mimetics are artificial systems that replicate the lipid bilayer enviro |
| concept | concepts/mfs-transporter/ | Major Facilitator Superfamily (MFS) | The Major Facilitator Superfamily (MFS) is one of the largest families of second |
| concept | concepts/mit-superfamily/ | Metal Ion Transporter (MIT) Superfamily | The Metal Ion Transporter (MIT) superfamily includes transporters for Mg2+, Co2+ |
| concept | concepts/n-glycosylation-sequon/ | N-Glycosylation Sequon | The N-glycosylation sequon (Asn-X-Ser/Thr, where X is not Pro) is the minimal co |
| concept | concepts/nickel-pincer-nucleotide-cofactor-biosynthesis/ | Nickel-Pincer Nucleotide Cofactor Biosynthesis | Concept: nickel-pincer-nucleotide-cofactor-biosynthesis |
| concept | concepts/nitrate-nitrite-antiport-mechanism/ | Nitrate/Nitrite Antiport Mechanism | The nitrate/nitrite antiport mechanism is the transport mechanism used by NNP fa |
| concept | concepts/nitrilase-superfamily/ | Nitrilase Superfamily | Concept: nitrilase-superfamily |
| concept | concepts/nnp-family/ | Nitrate/Nitrite Porter (NNP) Family | The nitrate/nitrite porter (NNP) family is a group of membrane transporters with |
| concept | concepts/non-competitive-inhibition/ | Non-competitive Inhibition of Rhomboid Proteases | Non-competitive inhibition is the characteristic mode of inhibition exhibited by |
| concept | concepts/non-crystallographic-symmetry/ | Non-Crystallographic Symmetry (NCS) | Non-crystallographic symmetry (NCS) refers to symmetry relationships between mol |
| concept | concepts/non-photochemical-quenching/ | Non-photochemical Quenching (NPQ) in LHC-II | Non-photochemical quenching (NPQ) is a photoprotective mechanism in plants that  |
| concept | concepts/nss-family/ | Neurotransmitter/Sodium Symporter (NSS) Family | The NSS (neurotransmitter/sodium symporter) family is a major group of secondary |
| concept | concepts/ntq-motif/ | NTQ Motif in Chloride Pumping Rhodopsins | The NTQ motif (Asn-Thr-Gln) is a conserved residue pattern in the ion conduction |
| concept | concepts/o1-channel/ | O1 Water Channel of Photosystem II | The O1 channel is a water intake pathway in Photosystem II (PSII) that connects  |
| concept | concepts/outward-facing-conformation/ | Outward-Facing Conformation of ABC Transporters | The outward-facing conformation is a structural state of ABC transporters in whi |
| concept | concepts/oxygen-ladder-selectivity-filter/ | Oxygen Ladder in Selectivity Filters | Concept: oxygen-ladder-selectivity-filter |
| concept | concepts/p-type-atpase-mechanism/ | P-type ATPase Mechanism | P-type ATPases are a superfamily of primary active transporters that use ATP hyd |
| concept | concepts/p-type-atpase/ | P-type ATPase Family | P-type ATPases are a major family of ion-transporting ATPases that form a covale |
| concept | concepts/p2x-receptor-family/ | P2X Receptor Family | The P2X receptor family comprises a group of ligand-gated ion channels activated |
| concept | concepts/p2y-receptor-family/ | P2Y Receptor Family | The P2Y receptors are a family of purinergic G-protein-coupled receptors (GPCRs) |
| concept | concepts/paqr-family/ | PAQR Family (Progesterone and AdipoQ Receptor Family) | The progesterone and adipoQ receptor (PAQR) family comprises integral membrane p |
| concept | concepts/pe-ppe-fusion-proteins/ | PE-PPE Fusion Proteins | PE-PPE fusion proteins are chimeric proteins that combine the N-terminal PE (Pro |
| concept | concepts/peptide-binding-pocket/ | PepT_So2 Substrate-Binding Pockets (P1, P2, P3) | The substrate-binding site of PepT_So2 (a proton-dependent oligopeptide transpor |
| concept | concepts/peripheral-stalk-elasticity/ | Peripheral Stalk Elasticity in ATP Synthase | The peripheral stalk of ATP synthase connects the membrane-embedded F0 motor to  |
| concept | concepts/phosphoenzyme-e2p-state/ | Phosphoenzyme E2P State | The E2P state is a phosphorylated intermediate of P-type ATPases in which the en |
| concept | concepts/pilz-domain/ | PilZ Domain (c-di-GMP Binding Domain) | Concept: pilz-domain |
| concept | concepts/ping-pong-mechanism/ | Ping-Pong Catalytic Mechanism | Concept: ping-pong-mechanism |
| concept | concepts/polar-network-gpcr-activation/ | Polar Network in GPCR Activation | The polar network is an extensive system of hydrogen bonds and water-mediated in |
| concept | concepts/pore-forming-toxins/ | Pore-Forming Toxins | Pore-forming toxins (PFTs) are a large class of bacterial virulence factors that |
| concept | concepts/positive-allosteric-modulation/ | Positive Allosteric Modulation | Positive allosteric modulators (PAMs) are small molecules that bind to an allost |
| concept | concepts/pot-family/ | POT Family (Proton-Dependent Oligopeptide Transporters) | The POT (proton-dependent oligopeptide transporter) family is a subgroup of the  |
| concept | concepts/pq-loop-family/ | PQ-Loop Family | The PQ-loop family is a group of membrane transporters defined by a conserved Pr |
| concept | concepts/proton-locked-conformation/ | Proton-Locked Conformation | The proton-locked conformation is a stable structural state of the conserved glu |
| concept | concepts/rck-domain-activation-mechanism/ | RCK Domain Activation Mechanism | The RCK (Regulator of K⁺ conductance) domain activation mechanism describes how  |
| concept | concepts/remote-coupling-mechanism/ | Remote Coupling Mechanism in Membrane Transporters | Remote coupling is a mechanism by which structural changes in the transmembrane  |
| concept | concepts/retinal-chromophore-conformation/ | Retinal Chromophore Conformation | Retinal chromophore conformation in microbial rhodopsins is determined by the pr |
| concept | concepts/rhodopsin-photocycle/ | Rhodopsin Photocycle | The rhodopsin photocycle involves light-induced isomerization of retinal from al |
| concept | concepts/rhomboid-protease/ | Rhomboid Protease Family | Rhomboid proteases are intramembrane serine proteases that cleave transmembrane  |
| concept | concepts/right-handed-coiled-coil-architecture/ | Right-Handed Coiled-Coil Architecture in Rotary ATPases | The peripheral stalk of rotary ATPases adopts an unusual right-handed coiled-coi |
| concept | concepts/rnd-efflux-pumps/ | RND Efflux Pumps | Resistance nodulation cell division (RND) transporters are a family of multidrug |
| concept | concepts/rocker-switch-mechanism/ | Rocker-Switch Mechanism in MFS Transporters | The rocker-switch mechanism is a variant of alternating access specific to MFS t |
| concept | concepts/rocking-bundle-mechanism/ | Rocking-Bundle Mechanism | The rocking-bundle mechanism is a transport mechanism in which a transporter und |
| concept | concepts/rotary-atpase-mechanism/ | Rotary ATPase Mechanism | Rotary ATPases (F-type, V-type, A-type) use a rotary catalytic mechanism to synt |
| concept | concepts/s4-s5-linker-interaction-motif/ | S4-S5 Linker Interaction Motif | The S4-S5 linker interaction motif is a three-way structural interaction in volt |
| concept | concepts/scissor-switch-gating/ | Scissor-Switch Gating in POT Family Transporters | The scissor-switch gating mechanism is a specialized form of the alternating-acc |
| concept | concepts/sed-s-protein-family/ | SEDS Protein Family | The Shape, Elongation, Division, and Sporulation (SEDS) proteins are a large fam |
| concept | concepts/selective-lipid-binding/ | Selective Lipid Binding in Membrane Proteins | Selective lipid binding refers to the phenomenon where membrane proteins discrim |
| concept | concepts/selectivity-filter/ | Ion Channel Selectivity Filter | The selectivity filter is a narrow region of the ion channel pore that determine |
| concept | concepts/self-processing/ | Self-processing of Membrane Proteins | Self-processing refers to the phenomenon where a membrane protein cleaves its ow |
| concept | concepts/semisweet/ | SemiSWEET Transporter Family | SemiSWEETs are bacterial homologues of the eukaryotic SWEET (Sugars Will Eventua |
| concept | concepts/ser-lys-catalytic-mechanism/ | Ser/Lys Catalytic Mechanism | The ser-lys catalytic mechanism is found in rhomboid proteases and signal peptid |
| concept | concepts/si-face-cleavage/ | si-Face Cleavage in Rhomboid Proteases | Rhomboid proteases cleave substrates from the si-face (small interface) of the t |
| concept | concepts/sl35-family/ | SLC35 Family (Nucleotide Sugar Transporters) | Concept: sl35-family |
| concept | concepts/slac1-superfamily/ | SLAC1 Superfamily | The SLAC1 superfamily comprises a widespread group of anion channel proteins fou |
| concept | concepts/slc11-nramp-family/ | SLC11 (NRAMP) Family | The SLC11 (Solute Carrier 11) family, also known as the NRAMP (Natural Resistanc |
| concept | concepts/sliding-helix-mechanism/ | Sliding Helix Mechanism | The sliding helix mechanism is a model for voltage-dependent gating in voltage-g |
| concept | concepts/sm-family/ | SMR Family (Small Multidrug Resistance Family) | The small multidrug resistance (SMR) family is a group of bacterial multidrug ef |
| concept | concepts/sn2-like-displacement-mechanism/ | SN2-Like Displacement Mechanism in Phosphotransferases | Concept: sn2-like-displacement-mechanism |
| concept | concepts/snare-complex/ | SNARE Complex | The SNARE (Soluble N-ethylmaleimide-sensitive factor Attachment protein REceptor |
| concept | concepts/sodium-allosteric-modulation/ | Sodium Ion Allosteric Modulation in GPCRs | Sodium ions (Na+) act as negative allosteric modulators of many class A G protei |
| concept | concepts/sodium-channel-gating/ | Sodium Channel Gating and Selectivity | Voltage-gated sodium channels use a gating mechanism involving voltage-sensing d |
| concept | concepts/sodium-channel-inactivation-gating/ | Sodium Channel Inactivation Gating | Sodium channel inactivation gating in prokaryotic voltage-gated sodium channels  |
| concept | concepts/sodium-motive-force/ | Sodium-Motive Force (SMF) | Sodium-motive force is the electrochemical gradient of sodium ions across a memb |
| concept | concepts/spyr-domain/ | SPRY Domain in Ryanodine Receptors | The SPRY domain is a protein domain named after 'SPIA kinase and Ryanodine Recep |
| concept | concepts/steered-molecular-dynamics/ | Steered Molecular Dynamics (SMD) | Steered Molecular Dynamics (SMD) is a computational simulation technique where a |
| concept | concepts/substrate-protonation-coupling/ | Substrate-Protonation Coupling in MFS Symporters | Substrate-protonation coupling is a fundamental mechanism in proton-driven MFS s |
| concept | concepts/sugar-porter-family/ | Sugar Porter (SP) Family | Concept: sugar-porter-family |
| concept | concepts/sulfonamide-resistance/ | Sulfonamide Resistance | Sulfonamide resistance is a major clinical problem that emerged rapidly followin |
| concept | concepts/sweet-transporter/ | SWEET Transporter Family | The SWEET family of sugar transporters is a widespread class of uniporters found |
| concept | concepts/syringe-injection-mechanism/ | Syringe-Like Injection Mechanism of Tc Toxins | The syringe-like injection mechanism describes how Tc (toxin complex) toxins fro |
| concept | concepts/tat-pathway/ | Twin-Arginine Translocation (TAT) Pathway | Concept: tat-pathway |
| concept | concepts/thermostabilization/ | Protein Thermostabilization | Protein thermostabilization is a construct design strategy in which targeted poi |
| concept | concepts/tmbim-protein-family/ | TMBIM Protein Family | The TMBIM (transmembrane Bax inhibitor motif) protein family comprises highly co |
| concept | concepts/tmem16-family/ | TMEM16 Family (Anoctamin Protein Family) | The TMEM16 family (also known as anoctamin family) is a group of eukaryotic memb |
| concept | concepts/ton-complex/ | Ton Complex | The Ton complex is an energy-transducing protein assembly located in the inner m |
| concept | concepts/tric-channel-gating/ | TRIC Channel Gating Mechanism | The TRIC (Trimeric Intracellular Cation) channel gating mechanism is a complex,  |
| concept | concepts/truncation/ | Protein Truncation for Crystallization | Protein truncation is a construct design strategy in which flexible, unstructure |
| concept | concepts/two-site-binding-mode/ | Two-Site Peptide Ligand Binding Mode | Concept: two-site-binding-mode |
| concept | concepts/two-stage-catalytic-mechanism/ | Two-Stage Catalytic Mechanism of Rhomboid Proteases | Rhomboid intramembrane proteases catalyze substrate cleavage through a two-stage |
| concept | concepts/type-ii-abc-transporter-family/ | Type II ABC Transporter Family | Type II ABC transporters are a distinct subclass of bacterial ABC importers that |
| concept | concepts/virtual-proton-pump/ | Virtual Proton Pump | A virtual proton pump is a transport mechanism in which the free energy of subst |
| concept | concepts/vitamin-k-cycle/ | Vitamin K Cycle | The vitamin K cycle is a biochemical pathway that recycles vitamin K between its |
| concept | concepts/voltage-sensor-paddle/ | Voltage-Sensor Paddle | The voltage-sensor paddle is a helix-turn-helix structural motif found in voltag |
| concept | concepts/water-network-in-ligand-binding/ | Water Networks in GPCR Ligand Binding | Water molecules in GPCR ligand binding sites play a crucial role in determining  |
| concept | concepts/wxg100-family-proteins/ | WxG100 Family Proteins | The WxG100 family (also known as the ESAT-6 family) comprises small helical prot |
| concept | concepts/x-ray-radiation-damage/ | X-Ray Radiation Damage in Crystallography | X-ray radiation damage is a major limitation in macromolecular crystallography.  |
| concept | concepts/yidc-oxa1-alb3-insertase-family/ | YidC/Oxa1/Alb3 Insertase Family | The YidC/Oxa1/Alb3 family comprises evolutionarily conserved membrane protein in |
| method | methods/cell-lysis/french-press/ | French Press Cell Lysis | French press cell lysis is a high-pressure homogenization technique used to disr |
| method | methods/crystallization/batch-crystallization-free-interface-diffusion/ | Batch Crystallization with Free Interface Diffusion | Batch crystallization with free interface diffusion is a membrane protein crysta |
| method | methods/crystallization/bicelle-crystallization/ | Bicelle Crystallization | Bicelle crystallization is a membrane protein crystallization technique where th |
| method | methods/crystallization/hanging-drop-vapor-diffusion/ | Hanging-Drop Vapor Diffusion | Hanging-drop vapor diffusion is a widely used protein crystallization technique  |
| method | methods/crystallization/hilide-crystallization/ | HiLiDe Crystallization | HiLiDe (Hydrophobic Interaction-Driven) crystallization is a membrane protein cr |
| method | methods/crystallization/imisx-in-situ-crystallization/ | IMISX In-Situ Serial Crystallography | IMISX (in meso in situ) is a serial X-ray crystallography technique that combine |
| method | methods/crystallization/lipidic-cubic-phase/ | Lipidic Cubic Phase Crystallization | Lipidic cubic phase (LCP) crystallization, also known as the in meso method, is  |
| method | methods/crystallization/liquid-sponge-phase-crystallization/ | Liquid Sponge Phase Crystallization | Liquid sponge phase (LSP) crystallization is a membrane protein crystallization  |
| method | methods/crystallization/sitting-drop-vapor-diffusion/ | Sitting-Drop Vapor Diffusion | Sitting-drop vapor diffusion is a widely used protein crystallization technique  |
| method | methods/expression-systems/baculovirus-expression-system/ | Baculovirus Expression System in Sf9 Cells | The baculovirus expression system using Spodoptera frugiperda (Sf9) insect cells |
| method | methods/expression-systems/cell-free-protein-synthesis/ | Cell-Free Protein Synthesis for Membrane Proteins | Cell-free protein synthesis systems can be supplemented with both lipid and dete |
| method | methods/expression-systems/pichia-pastoris/ | Pichia pastoris Expression System | Method: pichia-pastoris |
| method | methods/purification/affinity-chromatography/ | Affinity Chromatography | Affinity chromatography is a purification method that separates proteins based o |
| method | methods/purification/hydroxyapatite-chromatography/ | Hydroxyapatite Chromatography | Hydroxyapatite chromatography is a separation technique that exploits the affini |
| method | methods/purification/ion-exchange-chromatography/ | Ion-Exchange Chromatography | Ion-exchange chromatography (IEX) is a purification method that separates protei |
| method | methods/purification/limited-proteolysis/ | Limited Proteolysis | Limited proteolysis is a technique where a protease is used to selectively cleav |
| method | methods/purification/size-exclusion-chromatography/ | Size-Exclusion Chromatography | Size-exclusion chromatography (SEC), also known as gel filtration, separates mol |
| method | methods/quality-assessment/circular-dichroism-spectroscopy/ | Circular Dichroism Spectroscopy | Circular dichroism (CD) spectroscopy measures the differential absorption of lef |
| method | methods/quality-assessment/deer-spectroscopy/ | Double Electron Electron Resonance (DEER) Spectroscopy | Double electron electron resonance (DEER), also known as pulsed electron double  |
| method | methods/quality-assessment/fluorescence-size-exclusion-chromatography/ | Fluorescence Size-Exclusion Chromatography (FSEC) | Fluorescence size-exclusion chromatography (FSEC) is a high-throughput screening |
| method | methods/quality-assessment/gas-phase-unfolding/ | Gas-Phase Unfolding Analysis | Gas-phase unfolding is an ion mobility mass spectrometry (IM-MS) technique used  |
| method | methods/quality-assessment/isothermal-titration-calorimetry/ | Isothermal Titration Calorimetry (ITC) | Isothermal titration calorimetry (ITC) directly measures the heat released or ab |
| method | methods/quality-assessment/nbd-phospholipid-scrambling-assay/ | NBD-Phospholipid Scrambling Assay | The NBD-phospholipid scrambling assay is a functional assay used to measure lipi |
| method | methods/quality-assessment/proteoliposome-reconstitution/ | Proteoliposome Reconstitution | Proteoliposome reconstitution is a technique for incorporating purified membrane |
| method | methods/quality-assessment/sec-mals/ | Size Exclusion Chromatography with Multi-Angle Light Scattering (SEC-MALS) | SEC-MALS combines size exclusion chromatography with multi-angle light scatterin |
| method | methods/quality-assessment/static-light-scattering/ | Static Light Scattering | Static light scattering (SLS) is a biophysical technique used to determine the m |
| method | methods/quality-assessment/thermal-shift-assay/ | Thermal Shift Assay (Fluorescent CPM) | Thermal shift assays (also known as differential scanning fluorescence or CPM as |
| method | methods/quality-assessment/tr-fret/ | Time-Resolved Fluorescence Resonance Energy Transfer (TR-FRET) | Time-resolved fluorescence resonance energy transfer (TR-FRET) is a biophysical  |
| method | methods/quality-assessment/two-electrode-voltage-clamp/ | Two-Electrode Voltage Clamp (TEVC) | Two-electrode voltage clamp (TEVC) is an electrophysiology technique for measuri |
| method | methods/structure-determination/cryo-em/ | Cryo-Electron Microscopy | Cryo-electron microscopy (cryo-EM) is a high-resolution structure determination  |
| method | methods/structure-determination/diffractive-imaging-imperfect-crystals/ | Diffractive Imaging of Imperfect Crystals | Diffractive imaging of imperfect crystals is a macromolecular structure determin |
| method | methods/structure-determination/free-energy-perturbation/ | Free Energy Perturbation | Free energy perturbation (FEP) is a computational method for calculating free en |
| method | methods/structure-determination/miras/ | Multiple Isomorphous Replacement with Anomalous Scattering (MIRAS) | MIRAS (Multiple Isomorphous Replacement with Anomalous Scattering) is a crystall |
| method | methods/structure-determination/molecular-dynamics-simulation/ | Molecular Dynamics Simulation | Molecular dynamics (MD) simulation is a computational technique for studying the |
| method | methods/structure-determination/molecular-replacement/ | Molecular Replacement | Molecular replacement is an X-ray crystallographic phasing method that uses a kn |
| method | methods/structure-determination/multi-wavelength-anomalous-diffraction/ | Multi-Wavelength Anomalous Diffraction | Multi-wavelength anomalous diffraction (MAD) is an X-ray crystallographic phasin |
| method | methods/structure-determination/semet-sad-phasing/ | Selenomethionine Single-Wavelength Anomalous Dispersion (SeMet SAD) Phrasing | Selenomethionine single-wavelength anomalous dispersion (SeMet SAD) phrasing is  |
| method | methods/structure-determination/serial-femtosecond-crystallography/ | Serial Femtosecond Crystallography | Serial femtosecond crystallography (SFX) is an X-ray crystallography technique t |
| method | methods/structure-determination/single-crystal-microspectrophotometry/ | Single-Crystal Microspectrophotometry | Single-crystal microspectrophotometry is a technique for recording absorption sp |
| method | methods/structure-determination/single-wavelength-anomalous-diffraction/ | Single-Wavelength Anomalous Diffraction | Single-wavelength anomalous diffraction (SAD) is an X-ray crystallographic phasi |
| method | methods/structure-determination/time-resolved-serial-femtosecond-crystallography/ | Time-Resolved Serial Femtosecond Crystallography (TR-SFX) | Time-resolved serial femtosecond crystallography (TR-SFX) is an X-ray crystallog |
| method | methods/structure-determination/umbrella-sampling/ | Umbrella Sampling | Umbrella sampling (US) is an enhanced sampling molecular dynamics technique used |
| protein | proteins/5ht2a-receptor/ | Human 5-HT2A Receptor | The human serotonin 2A (5-HT2A) receptor is a class A GPCR and the primary molec |
| protein | proteins/5ht2b-receptor/ | Human 5-HT2B Receptor | The human serotonin 2B (5-HT2B) receptor is a class A GPCR that signals primaril |
| protein | proteins/a-thaliana-sweet1/ | A. thaliana SWEET1 | A. thaliana SWEET1 is a glucose transporter from the SWEET family found in Arabi |
| protein | proteins/a2a-psb1-bril/ | L](/xray-mp-wiki/reagents/protein-tags/bril/ | The adenosine A2A receptor (A2AAR) is a class A GPCR and an important drug targe |
| protein | proteins/a2aar-d52n/ | Human Adenosine A2A Receptor D52N Variant (A2AAR-D52N) | The human adenosine A2A receptor D52N variant (A2AAR-D52N) is a point mutant of  |
| protein | proteins/a2aar-s91a/ | Human Adenosine A2A Receptor S91A Variant (A2AAR-S91A) | The human adenosine A2A receptor S91A variant (A2AAR-S91A) is a point mutant of  |
| protein | proteins/a2ar-star2-bril/ | Human Adenosine A2A Receptor A2A-StaR2-bRIL (PDB 7ARO) | The A2A-StaR2-bRIL construct is an engineered human adenosine A2A receptor with  |
| protein | proteins/a2ar-star2-s277-bril/ | Human Adenosine A2A Receptor A2A-StaR2-S277-bRIL (PDB 8CU6) | The A2A-StaR2-S277-bRIL construct is an engineered human adenosine A2A receptor  |
| protein | proteins/abcg1/ | ABCG1 | ABCG1 is a member of the ATP-binding cassette (ABC) G subfamily of lipid transpo |
| protein | proteins/abcg2/ | ABCG2 | ABCG2 (breast cancer resistance protein, BCRP) is the sole multidrug transporter |
| protein | proteins/abcg5/ | ABCG5 | ABCG5 is a member of the ATP-binding cassette (ABC) G subfamily of transporter p |
| protein | proteins/abcg8/ | ABCG8 | ABCG8 is a member of the ATP-binding cassette (ABC) G subfamily of transporter p |
| protein | proteins/acetabularia-rhodopsin-ii/ | Acetabularia Rhodopsin Ii | Acetabularia rhodopsin II (ARII) is a light-driven proton pump from the marine a |
| protein | proteins/acetylcholine-binding-protein/ | Acetylcholine-Binding Protein (AChBP) | Acetylcholine-binding protein (AChBP) is a soluble protein from the land snail B |
| protein | proteins/acrB/ | AcrB multidrug efflux pump | AcrB is the principal multidrug transporter in Escherichia coli, functioning as  |
| protein | proteins/acra/ | AcrA multidrug efflux pump periplasmic protein | AcrA is a periplasmic membrane fusion protein from Escherichia coli that partner |
| protein | proteins/adic/ | AdiC Arginine/Agmatine Antiporter | AdiC is an arginine/agmatine antiporter from the APC (amino acid-polyamine-organ |
| protein | proteins/adiponectin/ | Adiponectin | Adiponectin is a hormone secreted mainly from adipocytes that stimulates glucose |
| protein | proteins/adipor1/ | Adiponectin Receptor 1 (ADIPOR1) | Adiponectin receptor 1 (ADIPOR1) is an integral membrane protein that belongs to |
| protein | proteins/adipor2/ | Adiponectin Receptor 2 (ADIPOR2) | Adiponectin receptor 2 (ADIPOR2) is an integral membrane protein that belongs to |
| protein | proteins/af-copa/ | CopA from Archaeoglobus fulgidus (AfCopA) | CopA from Archaeoglobus fulgidus (AfCopA) is a copper-transporting P1B-type ATPa |
| protein | proteins/af-tmem16/ | afTMEM16 (TMEM16 Lipid Scramblase from Aspergillus fumigatus) | afTMEM16 is a calcium-activated lipid scramblase from the fungus Aspergillus fum |
| protein | proteins/algm1m2ss/ | AlgM1M2SS Alginate ABC Transporter | AlgM1M2SS is an ATP-binding cassette (ABC) importer from the alginate-assimilati |
| protein | proteins/apelin-receptor/ | Human Apelin Receptor (APJR) | The human apelin receptor (APJR), also known as angiotensin receptor-like 1 (AGT |
| protein | proteins/aqp1/ | Aquaporin-1 (AQP1) | Aquaporin-1 (AQP1) is a water-selective channel protein from bovine red blood ce |
| protein | proteins/aquaporin-z/ | n Z](/xray-mp-wiki/proteins/aquaporin-z/ | Aquaporin Z (AqpZ) is the bacterial homolog of human [aquaporin 1 (AQP1)(/xray-m |
| protein | proteins/archaeoglobus-fulgidus-aglb/ | Archaeoglobus fulgidus AglB (AfAglB) | Archaeoglobus fulgidus AglB (AfAglB) is the catalytic subunit of the archaeal ol |
| protein | proteins/archaerhodopsin-2/ | Archaerhodopsin-2 | Archaerhodopsin-2 (aR2) is a light-driven proton pump found in the claret membra |
| protein | proteins/asic1a/ | Acid-Sensing Ion Channel 1a | Acid-sensing ion channel 1a (ASIC1a) is a proton-gated, sodium-selective ion cha |
| protein | proteins/at1r/ | Angiotensin II Type 1 Receptor | The angiotensin II type 1 receptor (AT1R) is a class A G protein-coupled recepto |
| protein | proteins/at2r/ | Angiotensin II Type 2 Receptor | The angiotensin II type 2 receptor (AT2R) is a class A G protein-coupled recepto |
| protein | proteins/avglur1/ | AvGluR1 Ligand-Binding Domain (LBD) | The ligand-binding domain (LBD) of AvGluR1, an ionotropic glutamate receptor fro |
| protein | proteins/bacteriorhodopsin/ | Bacteriorhodopsin | Bacteriorhodopsin (bR) from Halobacterium salinarum is a light-driven proton pum |
| protein | proteins/bc-chbc/ | bcChbC (Bacillus cereus Chitobiose Transporter) | bcChbC is a diacetylchitobiose (GlcNAc2) transporter from Bacillus cereus, belon |
| protein | proteins/bcsa/ | BcsA from Rhodobacter sphaeroides (Cellulose Synthase Catalytic Subunit) | BcsA is the catalytically active subunit of the bacterial cellulose synthase com |
| protein | proteins/bcsb/ | BcsB from Rhodobacter sphaeroides (Cellulose Synthase Periplasmic Subunit) | BcsB is a periplasmic protein that associates with the catalytic BcsA subunit to |
| protein | proteins/beetle-icmt/ | Isoprenylcysteine Carboxyl Methyltransferase (ICMT) from Tribolium castaneum | ICMT (isoprenylcysteine carboxyl methyltransferase) from the beetle Tribolium ca |
| protein | proteins/beta2-adrenergic-receptor/ | Human Beta2-Adrenergic Receptor (beta2 AR) | The human beta2-adrenergic receptor (beta2 AR) is a class A G protein-coupled re |
| protein | proteins/betp/ | BetP (Na+/Betaine Symporter from Corynebacterium glutamicum) | BetP is a Na+-coupled glycine betaine symporter from the bacterium Corynebacteri |
| protein | proteins/bhuuv-t/ | Burkholderia cenocepacia Haem Importer Complex BhuUV-T | The BhuUV-T complex is a type II ATP-binding cassette (ABC) haem importer from t |
| protein | proteins/bhuuv/ | Burkholderia cenocepacia Haem Importer Complex BhuUV | The BhuUV complex is the transmembrane and nucleotide-binding domain core of the |
| protein | proteins/blastochloris-viridis-photosynthetic-reaction-centre/ | Blastochloris viridis Photosynthetic Reaction Centre | The photosynthetic reaction centre from Blastochloris viridis (RC_vir) is a four |
| protein | proteins/blt1/ | Guinea Pig Leukotriene B4 Receptor 1 (BLT1) | The leukotriene B4 receptor 1 (BLT1) is a class A G protein-coupled receptor tha |
| protein | proteins/bovine-adp-atp-carrier/ | Bovine ADP/ATP Carrier | The bovine ADP/ATP carrier (AAC) is a mitochondrial inner membrane protein that  |
| protein | proteins/bovine-f1-atpase/ | Bovine Mitochondrial F1-ATPase | Bovine mitochondrial F1-ATPase is the water-soluble catalytic domain of ATP synt |
| protein | proteins/bovine-rhodopsin/ | Bovine Rhodopsin | Rhodopsin is the photoreceptor GPCR in vertebrate retinal rod cells, responsible |
| protein | proteins/bpe-fluoride-channel/ | Fluoride Channel from B. pertussis (Bpe) | The fluoride channel from Bordetella pertussis (Bpe) is a member of the Fluc fam |
| protein | proteins/bsyetj/ | BsYetJ TMBIM Ca2+ Channel | BsYetJ is a transmembrane Bax inhibitor motif (TMBIM) protein from Bacillus subt |
| protein | proteins/c-elegans-p-glycoprotein/ | C. elegans P-glycoprotein (P-gp) | P-glycoprotein (P-gp) from Caenorhabditis elegans is an ATP-binding cassette (AB |
| protein | proteins/c1c2ga/ | C1C2GA (C1C2 T198G/G202A) | C1C2GA is a blue-shifted mutant of the channelrhodopsin chimera C1C2, created by |
| protein | proteins/c5ar1/ | Human Complement C5a Receptor 1 (C5aR1) | The human complement C5a receptor 1 (C5aR1, also known as CD88) is a class A G p |
| protein | proteins/ca-vab/ | CaVAb Bacterial Voltage-Gated Calcium Channel | CaVAb is a bacterial voltage-gated calcium channel that serves as an evolutionar |
| protein | proteins/cait/ | CaiT Carnitine Antiporter from Escherichia coli | CaiT is an L-carnitine/gamma-butyrobetaine antiporter from Escherichia coli that |
| protein | proteins/casmate/ | CasMATE (Camelina sativa MATE Transporter) | CasMATE is a multidrug and toxic compound extrusion (MATE) family transporter fr |
| protein | proteins/cb2/ | Cannabinoid Receptor 2 (CNR2/CB2) | Cannabinoid receptor 2 (CNR2, commonly known as CB2) is a class A G protein-coup |
| protein | proteins/ccr2-t4l/ | CC Chemokine Receptor 2 with T4 Lysozyme Fusion (CCR2-T4L) | CC chemokine receptor 2 (CCR2) is a class A G protein-coupled receptor expressed |
| protein | proteins/ccr2a/ | CC Chemokine Receptor 2A (CCR2A) | CC chemokine receptor 2A (CCR2A) is a class A G protein-coupled receptor and the |
| protein | proteins/cd47-bril-b6h12/ | CD47 BRIL-B6H12 complex from Homo sapiens | CD47 is the only 5-transmembrane (5-TM) spanning receptor of the immune system.  |
| protein | proteins/cd81/ | Human CD81 Tetraspanin | CD81 (also known as TAPA-1 or tspan28) is a human tetraspanin protein belonging  |
| protein | proteins/channelrhodopsin-c1c2/ | Channelrhodopsin C1C2 | Channelrhodopsin C1C2 is a chimeric construct between Chlamydomonas reinhardtii  |
| protein | proteins/clir/ | Chloride Ion Rhodopsin from Nonlabens marinus (CIR) | Chloride ion rhodopsin (CIR) from the flavobacterium Nonlabens marinus S1-08T is |
| protein | proteins/clpp/ | ClpP Protease | ClpP is an ATP-dependent, general protease from bacterial cytoplasm that works w |
| protein | proteins/cnr1/ | Cannabinoid Receptor 1 (CNR1/CB1) | Cannabinoid receptor 1 (CNR1, commonly known as CB1) is a class A G protein-coup |
| protein | proteins/cp-tric/ | CpTRIC Channel from Clostridium perfringens | CpTRIC is a Trimeric Intracellular Cation (TRIC) channel from the bacterium Clos |
| protein | proteins/crf1r-star-t4l/ | Human Corticotropin-Releasing Factor 1 Receptor StaR-T4L (CRF1R) | The human corticotropin-releasing factor 1 receptor (CRF1R) is a class A G prote |
| protein | proteins/cusA/ | CusA Inner Membrane Efflux Pump | CusA is the inner-membrane component of the CusABC tripartite copper/silver effl |
| protein | proteins/cusB/ | CusB Membrane Fusion Protein | CusB is a periplasmic membrane fusion protein (MFP) from Escherichia coli, funct |
| protein | proteins/cusC/ | CusC Outer Membrane Channel | CusC is the outer-membrane channel component of the CusABC tripartite copper/sil |
| protein | proteins/cytochrome-b/ | Cytochrome b (EcHyd-1 Partner) | Cytochrome b is the physiological partner of Escherichia coli Hydrogenase 1 (EcH |
| protein | proteins/cytochrome-b5-reductase/ | Cytochrome b5 Reductase | Cytochrome b5 reductase (b5R) is a membrane-embedded flavoprotein that catalyzes |
| protein | proteins/cytochrome-b5/ | Cytochrome b5 | Cytochrome b5 is a membrane-embedded electron transfer protein consisting of a s |
| protein | proteins/d-dat/ | Drosophila melanogaster Dopamine Transporter | The Drosophila melanogaster dopamine transporter (dDAT) is a Na+/Cl--coupled bio |
| protein | proteins/d-dopamine-transporter/ | Drosophila Dopamine Transporter (dDAT) | The Drosophila melanogaster dopamine transporter (dDAT) is a eukaryotic member o |
| protein | proteins/dap12/ | DAP12 (CD331) | DAP12 (Discoidin Domain-Related Protein 12, also known as CD331 or KARAP) is a e |
| protein | proteins/delta-opioid-receptor/ | Human Delta-Opioid Receptor (OPRD1) | The human delta-opioid receptor (δ-OR, OPRD1, UniProt P41143) is a class A G-pro |
| protein | proteins/diacylglycerol-kinase/ | Diacylglycerol Kinase (DgkA) | Diacylglycerol kinase (DgkA) from Escherichia coli is a 121-residue integral mem |
| protein | proteins/dinf-bh/ | DinF-BH (Bacillus halodurans DinF) - MATE Family H+-Coupled Transporter | DinF-BH is a multidrug and toxic compound extrusion (MATE) family transporter fr |
| protein | proteins/drd2/ | Human D₂ Dopamine Receptor (DRD2) | The human D2 dopamine receptor (DRD2) is a class A G protein-coupled receptor th |
| protein | proteins/drslc38a9/ | Zebrafish SLC38A9 (drSLC38A9) | Zebrafish SLC38A9 (drSLC38A9) is a lysosomal amino acid transporter from Danio r |
| protein | proteins/dsbA/ | DsbA | DsbA is a periplasmic dithiol oxidase from Escherichia coli belonging to the thi |
| protein | proteins/dsbB/ | DsbB | DsbB is an inner membrane quinone reductase from Escherichia coli that reoxidize |
| protein | proteins/dstable-t4-lysozyme/ | dsT4L (Disulfide-Stabilized T4 Lysozyme) | dsT4L is a disulfide-stabilized variant of T4 lysozyme engineered for use as a f |
| protein | proteins/dtpa/ | E. coli DtpA Peptide Transporter | DtpA is a proton-dependent oligopeptide transporter (POT) from Escherichia coli  |
| protein | proteins/e-coli-lnt/ | Escherichia coli Apolipoprotein N-Acyl Transferase (Lnt) | Apolipoprotein N-acyl transferase (Lnt) from Escherichia coli is a 512-residue i |
| protein | proteins/ec-cor-a/ | Escherichia coli CorA Mg2+ Channel (Cytoplasmic Domain) | CorA from Escherichia coli is the family prototype of the CorA Mg2+ transporter  |
| protein | proteins/ec-hyd-1/ | Escherichia coli Hydrogenase 1 (EcHyd-1) | Hydrogenase 1 (EcHyd-1) is a membrane-bound, O2-tolerant [NiFe]-hydrogenase from |
| protein | proteins/ec-semisweet/ | E. coli SemiSWEET (EcSemiSWEET) | EcSemiSWEET is a sugar transporter from the SWEET family found in Escherichia co |
| protein | proteins/ec2-fluoride-channel/ | Fluoride Channel from E. coli (Ec2) | The fluoride channel from Escherichia coli (Ec2) is a member of the Fluc family  |
| protein | proteins/ecglpg-cyto/ | Cytoplasmic Domain of Escherichia coli Rhomboid Protease  ( | Crystal structure of the soluble cytoplasmic domain of the Escherichia coli rhom |
| protein | proteins/elic/ | ELIC (Erwinia chrysanthemi Ligand-gated Ion Channel) | ELIC is a pentameric ligand-gated ion channel (pLGIC) from the bacterium Erwinia |
| protein | proteins/espB/ | EspB | EspB is a secreted virulence factor from Mycobacterium tuberculosis, encoded wit |
| protein | proteins/espg1/ | EspG1 | EspG1 is the ESX-1-specific chaperone from Mycobacterium tuberculosis that belon |
| protein | proteins/etb-receptor-bosentan/ | Human Endothelin ETB Receptor Bound to Bosentan | The human endothelin ETB receptor is a class A G-protein-coupled receptor (GPCR) |
| protein | proteins/etb-s6b-complex/ | Human Endothelin ETB Receptor in Complex with Sarafotoxin S6b | The human endothelin ETB receptor (ETBR) is a class A GPCR that binds endothelin |
| protein | proteins/exbB/ | ExbB (E. coli) | ExbB is an integral polytopic membrane protein from Escherichia coli that is a c |
| protein | proteins/exbD/ | ExbD (E. coli) | ExbD is an integral polytopic membrane protein from Escherichia coli that, toget |
| protein | proteins/fkbp12/ | FKBP12 (FK506 Binding Protein 12) | FKBP12 (FK506 binding protein 12) is a 12 kDa accessory protein that associates  |
| protein | proteins/flak/ | FlaK (Preflagellin Peptidase from Methanococcus maripaludis) | FlaK is a preflagellin peptidase (PFP) from the archaeon Methanococcus maripalud |
| protein | proteins/focA-vibrio-cholerae/ | FocA (Formate Channel A from Vibrio cholerae) | FocA (formate channel A) from Vibrio cholerae is a pentameric membrane channel b |
| protein | proteins/gabar-b3/ | Human GABA_A Receptor Beta-3 Subunit | The human GABA_A receptor beta-3 subunit (GABA_A R-β3) is a pentameric ligand-ga |
| protein | proteins/gadc/ | GadC Glutamate/GABA Antiporter | GadC is a glutamate/GABA antiporter from the APC (amino acid-polyamine-organocat |
| protein | proteins/gcgr/ | Human Glucagon Receptor (GCGR) | The human glucagon receptor (GCGR, UniProt P47871) is a class B G-protein-couple |
| protein | proteins/glic-ecd/ | GLIC ECD (Extracellular Domain of Gloeobacter violaceus Ion Channel) | The extracellular domain (ECD) of the pentameric ligand-gated ion channel (pLGIC |
| protein | proteins/glic/ | GLIC (Gloeobacter violaceus Ion Channel) | GLIC is a prokaryotic pentameric ligand-gated ion channel (pLGIC) from the cyano |
| protein | proteins/glp1r/ | Human Glucagon-Like Peptide-1 Receptor (GLP-1R) | The human glucagon-like peptide-1 receptor (GLP-1R, UniProt P48684) is a class B |
| protein | proteins/glpg/ | GlpG Rhomboid Intramembrane Protease | GlpG is the archetypal rhomboid intramembrane protease from Escherichia coli, be |
| protein | proteins/glt-ph/ | GltPh (Glutamate Transporter Homologue from Pyrococcus horikoshii) | GltPh is a sodium-coupled aspartate transporter from the archaeon Pyrococcus hor |
| protein | proteins/glt-tk/ | GltTk (Glutamate Transporter Homologue from Thermococcus kodakarensis) | GltTk is a homotrimeric glutamate transporter homologue from the archaeon Thermo |
| protein | proteins/gluN1-gluN2b-nmda-receptor/ | GluN1-GluN2B NMDA Receptor (Xenopus laevis, Full-Length) | The full-length N-methyl-D-aspartate (NMDA) receptor composed of GluN1 and GluN2 |
| protein | proteins/gluN1b-gluN2b-atd/ | GluN1b-GluN2B ATD (Amino-Terminal Domain of NMDA Receptor Subunits) | The isolated amino-terminal domains (ATD) of the GluN1b and GluN2B subunits of t |
| protein | proteins/glua2-lbd/ | GluA2 Ligand-Binding Domain (L504Y, N775S) | The ligand-binding domain (LBD) of the AMPA receptor subunit GluA2, engineered w |
| protein | proteins/glucl/ | GluCl (GABA-Gated Chloride Channel from C. elegans) | GluCl is the GABA-gated chloride channel from Caenorhabditis elegans. It is a pe |
| protein | proteins/glut1/ | Human Glucose Transporter GLUT1 (SLC2A1) | The human glucose transporter GLUT1 (encoded by SLC2A1) catalyses facilitative d |
| protein | proteins/glycerol-facilitator/ | Glycerol Facilitator (GlpF) | Glycerol Facilitator (GlpF) is a membrane transporter from Escherichia coli that |
| protein | proteins/glycine-receptor-alpha3/ | Human Glycine Receptor Alpha-3 Homopentamer (GlyRα3) | The human glycine receptor alpha-3 subunit (GlyRα3) is a pentameric ligand-gated |
| protein | proteins/gr/ | GR (Halobacterium sp. GR Bacteriorhodopsin) | GR (Halobacterium sp. GR bacteriorhodopsin) is a light-driven proton pump from H |
| protein | proteins/gs-alpha/ | Gs Protein Alpha Subunit (Galpha s) | The Gs protein alpha subunit (Galpha s) is the catalytic subunit of the stimulat |
| protein | proteins/gs-beta/ | Gs Protein Beta Subunit (Gbeta1) | The Gs protein beta subunit (Gbeta1) is one of the three subunits of the stimula |
| protein | proteins/gs-gamma/ | Gs Protein Gamma Subunit (Ggamma2) | The Gs protein gamma subunit (Ggamma2) is the smallest subunit of the stimulator |
| protein | proteins/h276395-glt-ph/ | H276,395-GltPh (Humanized GltPh Mutant, R276S/M395R) | H276,395-GltPh is a humanized mutant of the glutamate transporter homologue GltP |
| protein | proteins/hace2/ | Human Angiotensin-Converting Enzyme 2 (hACE2) | Human angiotensin-converting enzyme 2 (hACE2) is a membrane-bound zinc metallopr |
| protein | proteins/hiGlpG/ | Higlpg | HiGlpG is the rhomboid intramembrane protease from Haemophilus influenzae, a mem |
| protein | proteins/hiteha/ | HiTehA (TehA from Haemophilus influenzae) | HiTehA is the TehA anion channel protein from Haemophilus influenzae. It is a ba |
| protein | proteins/hmmbh/ | Methanosarcina barkeri Membrane-Bound Hydrogenase (HmMBH) | HmMBH is a membrane-bound hydrogenase from Methanosarcina barkeri that forms (SL |
| protein | proteins/hmuuv/ | Yersinia pestis Heme Transporter HmuUV | The HmuUV complex is the transmembrane and nucleotide-binding domain core of the |
| protein | proteins/hsc/ | HSC (Hydrosulfide Channel from Clostridium difficile) | HSC (hydrosulfide channel) is a pentameric membrane channel from Clostridium dif |
| protein | proteins/human-adenosine-a1-receptor-a1ar/ | Human Adenosine A1 Receptor (A1AR) | The human adenosine A1 receptor (A1AR) is a class A G protein-coupled receptor t |
| protein | proteins/human-adenosine-a2a-receptor-a2ar/ | Human Adenosine A2A Receptor (A2AR) | The human adenosine A2A receptor (A2AR) is a class A G protein-coupled receptor  |
| protein | proteins/human-alpha4beta2-nicotinic-receptor/ | Human Alpha4Beta2 Nicotinic Receptor | The human alpha4beta2 nicotinic acetylcholine receptor (nAChR) is a pentameric l |
| protein | proteins/human-glut3/ | Human Glucose Transporter 3 (GLUT3) | Human glucose transporter 3 (GLUT3, SLC2A3) is a major facilitator superfamily ( |
| protein | proteins/human-histamine-h3-receptor/ | Human Histamine H3 Receptor (H3R) | The human histamine H3 receptor (H3R) is a G protein-coupled receptor (GPCR) bel |
| protein | proteins/human-p2x3-receptor/ | Human P2X3 Receptor (hP2X3) | The human P2X3 receptor (hP2X3) is a ligand-gated ion channel from Homo sapiens  |
| protein | proteins/human-p2y1-receptor/ | Human P2Y1 Receptor | The human P2Y1 receptor (P2Y1R) is a class A G protein-coupled receptor (GPCR) t |
| protein | proteins/human-rhodopsin-e113q-m257y/ | Human Rhodopsin E113Q/M257Y Mutant | Human rhodopsin is the visual pigment GPCR in vertebrate retinal rod cells, resp |
| protein | proteins/hwbr/ | HwBR (Halomonas Water Bacteriorhodopsin) | HwBR (Halomonas water bacteriorhodopsin) is a light-driven proton pump from a Ha |
| protein | proteins/il-17a/ | Interleukin-17A (IL-17A) | IL-17A is a secreted cytokine and the best-studied member of the IL-17 cytokine  |
| protein | proteins/il-17f/ | Interleukin-17F (IL-17F) | IL-17F is a secreted cytokine and a member of the IL-17 cytokine family. It form |
| protein | proteins/il-17ra/ | Interleukin-17 Receptor A (IL-17RA) | IL-17RA is the founding and best-known member of the interleukin-17 receptor (IL |
| protein | proteins/il-17rc/ | Interleukin-17 Receptor C (IL-17RC) | IL-17RC is a single-pass type I transmembrane glycoprotein and a member of the i |
| protein | proteins/ilyobacter-tartaricus-c-subunit/ | Ilyobacter Tartaricus C Subunit | Signal peptide peptidase A (SppA) is a membrane-bound self-compartmentalized ser |
| protein | proteins/influenza-a-m2-proton-channel-s31n/ | Influenza A M2 Proton Channel S31N Mutant | The S31N mutant of the influenza A M2 proton channel is the most prevalent drug  |
| protein | proteins/influenza-a-m2-proton-channel/ | Influenza A M2 Proton Channel | The M2 proton channel of influenza A virus is a homotetrameric ion channel that  |
| protein | proteins/ipct-dipps/ | IPCT/DIPPS from Archaeoglobus fulgidus (Bifunctional CTP:Inositol-1-Phosphate Cytidylyltransferase/CDP-Inositol:Inositol-1-Phosphate Phosphotransferase) | IPCT/DIPPS is a bifunctional membrane enzyme from the hyperthermophilic archaeon |
| protein | proteins/k2p-2-1-trek-1/ | K2P 2.1 (TREK-1) Potassium Channel | K2P 2.1 (also known as TREK-1, encoded by KCNK2) is a polymodal thermo- and mech |
| protein | proteins/kappa-opioid-receptor/ | Kappa Opioid Receptor | The human kappa opioid receptor (KOP) is a class A G-protein coupled receptor th |
| protein | proteins/kcsa/ | KcsA Potassium Channel | KcsA is a prokaryotic voltage-gated potassium channel from Streptomyces lividans |
| protein | proteins/kdel-receptor/ | Kdel Receptor | The human KDEL receptor is a seven-pass transmembrane receptor that retrieves es |
| protein | proteins/kir7-1/ | Kir7.1 Inwardly Rectifying Potassium Channel | Kir7.1 (encoded by KCNJ13) is an inwardly rectifying potassium channel expressed |
| protein | proteins/kirbac-potassium-channels/ | Kirbac Potassium Channels | KirBac1.1 and KirBac3.1 are prokaryotic inward-rectifier potassium channels from |
| protein | proteins/ktra/ | KtrA (Cytosolic Regulatory Protein from Bacillus subtilis) | KtrA is a cytosolic regulatory protein from the bacterium Bacillus subtilis that |
| protein | proteins/ktrb/ | KtrB (Potassium Transporter Membrane Subunit from Bacillus subtilis) | KtrB is a membrane protein component of the KtrAB potassium transporter from the |
| protein | proteins/kvap/ | KvAP Voltage-Dependent Potassium Channel | KvAP is a voltage-dependent potassium channel from the thermophilic archaebacter |
| protein | proteins/lac-y/ | Lactose Permease of Escherichia coli (LacY) | Lactose permease (LacY) from Escherichia coli is a galactoside/H+ symporter and  |
| protein | proteins/larB/ | LarB (Lactiplantibacillus plantarum) | LarB is an enzyme from Lactiplantibacillus plantarum (formerly Lactobacillus pla |
| protein | proteins/lbsemisweet/ | LbSemiSWEET from Leptospira biflexa | LbSemiSWEET is a sugar transporter from the SWEET family found in the bacterium  |
| protein | proteins/leubat/ | LeuBAT Engineered Biogenic Amine Transporter Homologue | LeuBAT is an engineered mutant of the bacterial amino acid transporter LeuT from |
| protein | proteins/leut/ | LeuT Amino Acid Transporter from Aquifex aeolicus | LeuT is a bacterial amino acid transporter from Aquifex aeolicus that belongs to |
| protein | proteins/lh2-rps-acidophila/ | B800-850 LH2 Light-Harvesting Complex from Rhodopseudomonas acidophila | The B800-850 light-harvesting complex II (LH2) from Rhodopseudomonas acidophila  |
| protein | proteins/listeriolysin-o/ | Listeriolysin O | Listeriolysin O (LLO) is a cholesterol-dependent cytolysin (CDC) and essential v |
| protein | proteins/lp-copa/ | LpCopA (Copper-Transporting P-type ATPase from Legionella pneumophila) | LpCopA is a copper-transporting P_IB-type ATPase from the bacterium Legionella p |
| protein | proteins/lpa1/ | Lysophosphatidic Acid Receptor 1 (LPA1) | Lysophosphatidic acid receptor 1 (LPA1, also known as LPAR1 or EDG2) is a class  |
| protein | proteins/lpcat3/ | LPCAT3 (Lysophosphatidylcholine Acyltransferase 3) | LPCAT3 (Lysophosphatidylcholine Acyltransferase 3), also known as MBOAT5, is a m |
| protein | proteins/lsi1-cryst/ | Rice silicon channel Lsi1 crystallization construct | Lsi1 is the Low silicon rice 1 channel, a silicon (Si) uptake transporter from r |
| protein | proteins/m1-muscarinic-acetylcholine-receptor/ | M1 Muscarinic Acetylcholine Receptor | The M1 muscarinic acetylcholine receptor (M1 mAChR) is a class A G protein-coupl |
| protein | proteins/m1-star-t4l/ | M1-StaR-T4L | M1-StaR-T4L is a thermostabilized, engineered construct of the human M1 muscarin |
| protein | proteins/m2-muscarinic-acetylcholine-receptor/ | Human M2 Muscarinic Acetylcholine Receptor | The human M2 muscarinic acetylcholine receptor (M2 mAChR) is a class A G protein |
| protein | proteins/m3-muscarinic-acetylcholine-receptor/ | M3 Muscarinic Acetylcholine Receptor | The M3 muscarinic acetylcholine receptor (M3 mAChR) is a class A G protein-coupl |
| protein | proteins/m4-muscarinic-acetylcholine-receptor/ | Human M4 Muscarinic Acetylcholine Receptor | The human M4 muscarinic acetylcholine receptor (M4 mAChR) is a class A G protein |
| protein | proteins/ma-icmt/ | Ma Icmt | ICMT (isoprenylcysteine carboxyl methyltransferase) is an integral membrane meth |
| protein | proteins/malF/ | MalF (Escherichia coli Maltose Transporter Transmembrane Subunit) | MalF is a transmembrane subunit of the Escherichia coli maltose uptake system, a |
| protein | proteins/malG/ | MalG (Escherichia coli Maltose Transporter Transmembrane Subunit) | MalG is a transmembrane subunit of the Escherichia coli maltose uptake system, a |
| protein | proteins/malK/ | MalK (Escherichia coli Maltose Transporter ATPase Subunit) | MalK is the cytoplasmic ATP-binding cassette (NBD) subunit of the Escherichia co |
| protein | proteins/maltose-binding-protein/ | MBP (Escherichia coli Maltose-Binding Protein) | MBP (maltose-binding protein) is the periplasmic binding protein component of th |
| protein | proteins/mc4-r/ | Human Melanocortin 4 Receptor (MC4-R) | The human melanocortin 4 receptor (MC4-R) is a class A G protein-coupled recepto |
| protein | proteins/mdfA/ | MdfA Multidrug Efflux Transporter | MdfA is a secondary multidrug efflux transporter from Escherichia coli belonging |
| protein | proteins/melbst/ | Melibiose Permease from Salmonella typhimurium (MelBSt) | Melibiose permease (MelB) from Salmonella typhimurium is a Na+-coupled sugar sym |
| protein | proteins/metabotropic-glutamate-receptor-5/ | Metabotropic Glutamate Receptor 5 (mGlu5) | Metabotropic glutamate receptor 5 (mGlu5) is a Class C G protein-coupled recepto |
| protein | proteins/metarhodopsin-ii/ | Metarhodopsin II | Metarhodopsin II is the light-activated conformation of bovine rhodopsin, the vi |
| protein | proteins/methanococcus-jannaschii-secy/ | Methanococcus jannaschii SecY Translocation Channel | SecY from Methanococcus jannaschii is the core channel-forming subunit of the ar |
| protein | proteins/mexB/ | MexB (Pseudomonas aeruginosa multidrug exporter) | MexB is the inner-membrane component of the MexAB-OprM tripartite efflux pump in |
| protein | proteins/mexY/ | MexY (Pseudomonas aeruginosa multidrug exporter) | MexY is the inner-membrane component of the MexXY-OprM tripartite efflux pump in |
| protein | proteins/mgt-e-thermus-thermophilus/ | MgtE Mg2+ Transporter from Thermus thermophilus | MgtE from Thermus thermophilus is a magnesium transporter (Mg2+ influx system) b |
| protein | proteins/mhsT/ | MhsT Multi-Hydrophobic Amino Acid Transporter from Bacillus halodurans | MhsT is a multi-hydrophobic amino acid transporter from Bacillus halodurans belo |
| protein | proteins/mj0480/ | Mj0480 Archaeal DUF106 Protein | Mj0480 is an archaeal DUF106 protein from Methanocaldococcus jannaschii that fun |
| protein | proteins/mlaA/ | E. coli MlaA Outer Membrane Lipoprotein | MlaA is an outer membrane lipoprotein from Escherichia coli that forms a complex |
| protein | proteins/mlaC/ | E. coli MlaC Periplasmic Lipid-Binding Protein | MlaC is a soluble periplasmic lipid-binding protein from Escherichia coli that f |
| protein | proteins/mlaD/ | E. coli MlaD MCE Protein | MlaD is an inner membrane-associated MCE (mammalian cell entry) protein from Esc |
| protein | proteins/mmpL3/ | MmpL3 from Mycobacterium smegmatis | MmpL3 (Mycobacterial membrane protein Large 3) is an inner membrane transporter  |
| protein | proteins/mouse-5ht3a-receptor/ | Mouse 5-HT3A Receptor | The mouse serotonin 5-HT3A receptor is a pentameric ligand-gated ion channel (pL |
| protein | proteins/mouse-scd1/ | Mouse Stearoyl-CoA Desaturase 1 (mSCD1) | Mouse stearoyl-CoA desaturase 1 (SCD1) is a membrane-embedded diiron enzyme embe |
| protein | proteins/mouse-visual-arrestin-3a/ | Mouse Visual Arrestin (3A) | Mouse visual arrestin 1 (arrestin-1) is a cytosolic protein that binds to phosph |
| protein | proteins/mscs/ | E. coli MscS (Mechanosensitive Channel of Small Conductance) | MscS (mechanosensitive channel of small conductance) is a mechanosensitive ion c |
| protein | proteins/mt4l-lysozyme/ | mT4L (Minimal T4 Lysozyme) | mT4L is a minimal variant of T4 lysozyme engineered for GPCR crystallography by  |
| protein | proteins/mtcorb-ac/ | MtCorB Delta-C from Methanoculleus thermophilus | MtCorB Delta-C is a CNNM/CorB family magnesium transporter from the thermophilic |
| protein | proteins/mthk/ | MthK (Methanobacterium thermoautotrophicum K⁺ Channel) | MthK is a calcium-activated potassium channel from the archaeon Methanobacterium |
| protein | proteins/mtmem16a/ | mTMEM16A (Murine TMEM16A Calcium-Activated Chloride Channel) | mTMEM16A is the murine ortholog of TMEM16A (Ano1), the long sought-after Ca2+-ac |
| protein | proteins/mu-opioid-receptor/ | Murine Mu-Opioid Receptor | The murine mu-opioid receptor (muOR, MOP) is a class A G-protein-coupled recepto |
| protein | proteins/mycp1/ | MycP1 | MycP1 (Mycobacterial Protease 1) is a membrane-anchored serine protease of the m |
| protein | proteins/na-k-atpase-pig-kidney/ | Na+,K+-ATPase (Pig Kidney) | The Na+,K+-ATPase is a P-type ATPase pump that maintains the electrochemical gra |
| protein | proteins/na-k-atpase-shark/ | Na+,K+-ATPase from Squalus acanthias (Shark) | Na+,K+-ATPase from the shark rectal gland (Squalus acanthias) is a P-type ATPase |
| protein | proteins/nachbac/ | NaChBac Bacterial Voltage-Gated Sodium Channel | NaChBac is a bacterial voltage-gated sodium channel from Enterococcus hirae, rec |
| protein | proteins/nak-channel/ | NaK Channel from Bacillus cereus | NaK is a non-selective tetrameric cation channel from Bacillus cereus that condu |
| protein | proteins/nap-a/ | Na+/H+ Antiporter NapA from Thermus thermophilus | NapA from Thermus thermophilus is a Na+/H+ antiporter belonging to the CPA2 clad |
| protein | proteins/nark/ | NarK Nitrate/Nitrite Antiporter from Escherichia coli | NarK is a nitrate/nitrite antiporter from the nitrate/nitrite porter (NNP) famil |
| protein | proteins/naru/ | NarU Nitrate/Nitrite Antiporter from Escherichia coli | NarU is a nitrate/nitrite antiporter from the nitrate/nitrite porter (NNP) famil |
| protein | proteins/navab/ | NavAb Bacterial Voltage-Gated Sodium Channel | NavAb is a bacterial voltage-gated sodium channel from Alicyclobacillus sp. that |
| protein | proteins/navae1p-sodium-channel/ | Navae1P Sodium Channel | NavAe1p is a pore-only construct of the prokaryotic voltage-gated sodium channel |
| protein | proteins/navms/ | NavMs Sodium Channel | NavMs is a prokaryotic voltage-gated sodium channel (NaV) from Magnetococcus mar |
| protein | proteins/neurotensin-receptor-1/ | Rat Neurotensin Receptor 1 (NTSR1) | The rat neurotensin receptor 1 (NTSR1) is a class A G protein-coupled receptor t |
| protein | proteins/ng-hka/ | Non-Gastric H+/K+-ATPase (ngHKA) | The non-gastric H+/K+-ATPase (ngHKA, ATP12A) is a P-type 2C ATPase that particip |
| protein | proteins/nhaa/ | Na+/H+ Antiporter NhaA from Escherichia coli | NhaA from Escherichia coli is a Na+/H+ antiporter belonging to the Major Facilit |
| protein | proteins/nhtmem16/ | nhTMEM16 (TMEM16 Lipid Scramblase from Nectria haematococca) | nhTMEM16 is a calcium-activated lipid scramblase from the fungus Nectria haemato |
| protein | proteins/nor-mng/ | NorM-NG (Neisseria gonorrhoeae NorM) - MATE Family Na+-Coupled Transporter | NorM-NG is a multidrug and toxic compound extrusion (MATE) family transporter fr |
| protein | proteins/norM-vc/ | NorM-VC (Vibrio cholerae NorM) - MATE Family Multidrug Efflux Transporter | NorM-VC is a multidrug and toxic compound extrusion (MATE) family transporter fr |
| protein | proteins/ntmate2/ | NtMATE2 (Nicotiana tabacum MATE2) - Nicotine MATE transporter | NtMATE2 is a multidrug and toxic compound extrusion (MATE) family transporter fr |
| protein | proteins/ntsr1-el/ | NTSR1-ELF Mutant | NTSR1-ELF is a thermostabilized mutant of the neurotensin receptor 1 (NTSR1) con |
| protein | proteins/ntsr1-lf/ | NTSR1-LF Mutant | NTSR1-LF is a thermostabilized mutant of the neurotensin receptor 1 (NTSR1) cont |
| protein | proteins/nupg/ | NupG Nucleoside Proton Symporter from Escherichia coli | NupG is a nucleoside proton symporter from Escherichia coli belonging to the nuc |
| protein | proteins/opsin/ | Opsin (Retinal-Free Rhodopsin Apoprotein) | Opsin is the apoprotein form of rhodopsin, the G-protein-coupled receptor respon |
| protein | proteins/oqxb/ | OqxB efflux pump from Klebsiella pneumoniae | OqxB is a Resistance-Nodulation-Division (RND) efflux pump from *Klebsiella pneu |
| protein | proteins/orexin-1-receptor/ | Human Orexin 1 Receptor | The human orexin 1 receptor (OX1R, HCRTR1) is a class A GPCR that binds the neur |
| protein | proteins/orexin-2-receptor/ | Human Orexin 2 Receptor | The human orexin 2 receptor (OX2R, HCRTR2) is a class A GPCR that binds the neur |
| protein | proteins/osnip2-1/ | OsNIP2;1 (Silicon Transporter Lsi1 from Oryza sativa) | OsNIP2;1 (Nodulin26-like Intrinsic Protein 2;1) is a silicon transporter from th |
| protein | proteins/oxit/ | Oxalate Transporter OxIT from Oxalobacter formigenes | Oxalate transporter OxIT is an oxalate:formate antiporter (OFA) from the gut bac |
| protein | proteins/p2y12-receptor/ | Human P2Y12 Receptor | The P2Y12 receptor is a class A G protein-coupled receptor (GPCR) expressed on h |
| protein | proteins/par1/ | Human Protease-Activated Receptor 1 (PAR1) | Human Protease-Activated Receptor 1 (PAR1) is a class A G protein-coupled recept |
| protein | proteins/par2/ | Human Protease-Activated Receptor 2 (PAR2) - Stabilized T4L Fusion | Human Protease-Activated Receptor 2 (PAR2) is a class A G protein-coupled recept |
| protein | proteins/pe25/ | PE25 | PE25 is the conserved N-terminal domain of the PE (Pro-Glu) protein family from  |
| protein | proteins/pea-light-harvesting-complex-ii/ | Pea Light-Harvesting Complex II (LHC-II) | The pea light-harvesting complex II (LHC-II) is the major light-harvesting pigme |
| protein | proteins/pept-so/ | PepT_So Oligopeptide Transporter | PepT_So is a proton-coupled oligopeptide transporter from Shewanella oneidensis. |
| protein | proteins/pept-so2/ | PepT_So2 Oligopeptide Transporter | PepT_So2 is a proton-dependent oligopeptide transporter from Shewanella oneidens |
| protein | proteins/pept-st/ | PepT_St Proton-Dependent Oligopeptide Transporter from Streptococcus thermophilus | PepT_St is a proton-dependent oligopeptide transporter (POT) from Streptococcus  |
| protein | proteins/pglb-campylobacter-lari/ | PglB (Campylobacter lari Oligosaccharyltransferase) | PglB is a single-subunit oligosaccharyltransferase (OST) from the Gram-negative  |
| protein | proteins/ph-e-subunit-e/ | Subunit E of Pyrococcus horikoshii OT3 A-ATP Synthase (PhE) | Subunit E of the F-ATP synthase peripheral stalk from Haloarcula marismortui is  |
| protein | proteins/phospholamban/ | Phospholamban (PLB) | Phospholamban (PLB, also known as PLN) is a small (~52 amino acid) membrane prot |
| protein | proteins/photosystem-ii-core-dimer/ | Photosystem II core dimer from Thermosynechococcus elongatus | The Photosystem II (PSII) core dimer from the thermophilic cyanobacterium Thermo |
| protein | proteins/photosystem-ii/ | Photosystem II | Photosystem II (PSII) from Thermosynechococcus elongatus is a homodimeric multis |
| protein | proteins/pmmo/ | Particulate Methane Monooxygenase (pMMO) from Methylococcus capsulatus (Bath) | Particulate methane monooxygenase (pMMO) is an integral membrane metalloenzyme t |
| protein | proteins/polysulfide-reductase/ | Polysulfide Reductase (PsrABC) from Thermus thermophilus | Polysulfide reductase (PsrABC) from Thermus thermophilus is an integral membrane |
| protein | proteins/porb-corynebacterium-glutamicum/ | Porb Corynebacterium Glutamicum | Porin B (PorB) is an alpha-helical porin from Corynebacterium glutamicum, a myco |
| protein | proteins/ppe41/ | PPE41 | PPE41 is the conserved N-terminal domain of the PPE (Pro-Pro-Glu) protein family |
| protein | proteins/pqiB/ | E. coli PqiB Syringe-like MCE Protein | PqiB is a periplasm-spanning MCE (mammalian cell entry) protein from Escherichia |
| protein | proteins/psba2-psii/ | PsbA2-PSII dimer from Thermosynechococcus elongatus | The photosystem II (PSII) dimer from the thermophilic cyanobacterium Thermosynec |
| protein | proteins/psba3-psii/ | PsbA3-PSII dimer from Thermosynechococcus elongatus | The photosystem II (PSII) dimer from the thermophilic cyanobacterium Thermosynec |
| protein | proteins/psi-lhci-chlamydomonas/ | Psi Lhci Chlamydomonas | The photosystem I–light-harvesting complex I (PSI-LHCI) supercomplex from the gr |
| protein | proteins/pspr/ | PspR (DTG Rhodopsin from Pseudomonas putida) | PspR is a light-driven outward proton-pumping microbial rhodopsin from Pseudomon |
| protein | proteins/rembh/ | Ralstonia eutropha Membrane-Bound Hydrogenase (ReMBH) | ReMBH is a membrane-bound, O2-tolerant [NiFe]-hydrogenase from Ralstonia eutroph |
| protein | proteins/rhodobacter-sphaeroides-r26-reaction-center/ | Rhodobacter sphaeroides R-26 Reaction Center | The reaction center (RC) from the purple bacterium Rhodobacter sphaeroides R-26  |
| protein | proteins/rhodobacter-sphaeroides-reaction-centre-zn-bchl/ | l](/xray-mp-wiki/reagents/cofactors/bacteriochlorophyll/ | The Zn-BChl-containing reaction center (RC) from Rhodobacter sphaeroides, produc |
| protein | proteins/rhodopsin-2-2a/ | Rhodopsin (2.2 A Resolution, 1U19) | High-resolution 2.2 A crystal structure of bovine rhodopsin in the dark state (P |
| protein | proteins/rhodopsin-n2c-d282c-mutant/ | Rhodopsin N2C D282C Mutant | The N2C/D282C mutant of rhodopsin is a thermally stabilized recombinant form wit |
| protein | proteins/ribu/ | RibU (ECF-Type Riboflavin Transporter S Component from Staphylococcus aureus) | RibU is the S component (substrate-binding protein) of the energy-coupling facto |
| protein | proteins/rod-a/ | Thermus thermophilus RodA | RodA is a 359-residue transmembrane peptidoglycan polymerase from the Shape, Elo |
| protein | proteins/rps-viridis-reaction-centre/ | Rps. viridis Photosynthetic Reaction Centre | The photosynthetic reaction centre from the purple bacterium Rhodopseudomonas vi |
| protein | proteins/ry1-repeat12/ | Rabbit RyR1 Repeat12 Domain | The Repeat12 domain of rabbit Ryanodine Receptor Type 1 (RyR1), spanning residue |
| protein | proteins/ry1/ | Ryanodine Receptor Type 1 (RyR1) | Ryanodine receptor type 1 (RyR1) is the calcium release channel isoform primaril |
| protein | proteins/ry2-spry1/ | Mouse RyR2 SPRY1 Domain | The SPRY1 domain of mouse Ryanodine Receptor Type 2 (RyR2), spanning residues 65 |
| protein | proteins/ry2/ | Ryanodine Receptor Type 2 (RyR2) | Ryanodine receptor type 2 (RyR2) is the calcium release channel isoform primaril |
| protein | proteins/ry3/ | Ryanodine Receptor Type 3 (RyR3) | Ryanodine receptor type 3 (RyR3) is the calcium release channel isoform primaril |
| protein | proteins/ryanodine-receptor/ | Ryanodine Receptor (RyR) | Ryanodine receptors (RyRs) are large (~2.2 MDa) calcium release channels located |
| protein | proteins/s1p1/ | Sphingosine-1-Phosphate Receptor 1 (S1P1) | Sphingosine-1-phosphate receptor 1 (S1P1, also known as S1PR1 or EDG1) is a clas |
| protein | proteins/sa-pgsa/ | Phosphatidylglycerol Phosphate Synthase PgsA from Staphylococcus aureus | Phosphatidylglycerol phosphate synthase (PgsA) from Staphylococcus aureus (SaPgs |
| protein | proteins/sa-tric/ | SaTRIC Channel from Sulfolobus acidocaldarius | SaTRIC is a Trimeric Intracellular Cation (TRIC) channel from the archaeon Sulfo |
| protein | proteins/sarcolipin/ | Sarcolipin (SLN) | Sarcolipin (SLN) is a small (~30 amino acid) membrane protein that regulates the |
| protein | proteins/sars-cov-2-ctd/ | SARS-CoV-2 Spike Protein C-Terminal Domain | The C-terminal domain (CTD) of the SARS-CoV-2 spike (S) protein, also known as t |
| protein | proteins/sca-dmt-tru/ | ScaDMT^tru Truncated Divalent Metal-Ion Transporter | ScaDMT^tru is a truncated construct of ScaDMT from Staphylococcus capitis, lacki |
| protein | proteins/sca-dmt/ | ScaDMT Divalent Metal-Ion Transporter | ScaDMT is a divalent metal-ion transporter from Staphylococcus capitis belonging |
| protein | proteins/secdf/ | Thermus thermophilus SecDF Protein Translocation Motor | SecDF is a membrane protein belonging to the resistance-nodulation-division (RND |
| protein | proteins/sece/ | Thermus thermophilus SecE Accessory Subunit | SecE is an essential accessory subunit of the bacterial Sec translocon that stab |
| protein | proteins/secg/ | Thermus thermophilus SecG Accessory Subunit | SecG is an accessory subunit of the bacterial Sec translocon that comprises two  |
| protein | proteins/secy/ | Thermus thermophilus SecY Core Channel Subunit | SecY is the core channel-forming subunit of the Sec translocon, a heterotrimeric |
| protein | proteins/secyeg/ | Thermus thermophilus SecYEG Translocon Complex | The SecYEG translocon from Thermus thermophilus is a heterotrimeric protein-cond |
| protein | proteins/sehyd-1/ | Salmonella enterica Hydrogenase 1 (SeHyd-1) | SeHyd-1 is an O2-tolerant membrane-bound hydrogenase from the prevalent human pa |
| protein | proteins/sehyd-5/ | Salmonella enterica Hydrogenase 5 (SeHyd-5) | SeHyd-5 is an O2-tolerant membrane-bound hydrogenase from the prevalent human pa |
| protein | proteins/serca1a-e309q/ | SERCA1a E309Q Mutant | The SERCA1a E309Q mutant is a point mutant of the sarcoplasmic reticulum Ca²⁺-AT |
| protein | proteins/serca1a/ | SERCA1a (Sarcoplasmic Reticulum Ca²⁺-ATPase 1a) | SERCA1a is the Ca²⁺-ATPase of fast-twitch skeletal muscle sarcoplasmic reticulum |
| protein | proteins/shark-na-k-atpase/ | Na+,K+-ATPase (Shark Rectal Gland) | The Na+,K+-ATPase from shark (Squalus acanthias) rectal gland is a P-type ATPase |
| protein | proteins/sigma-1-receptor/ | Human Sigma-1 Receptor (SIGMAR1) | The human sigma-1 receptor (SIGMAR1) is an ER-resident single-pass transmembrane |
| protein | proteins/slac1/ | SLAC1 (SLOW ANION CHANNEL 1 from Arabidopsis thaliana) | SLAC1 (SLOW ANION CHANNEL 1) is a plant anion channel from Arabidopsis thaliana  |
| protein | proteins/slc26dg/ | SLC26Dg (Deinococcus geothermalis Fumarate Transporter) | SLC26Dg is a prokaryotic fumarate transporter from the bacterium Deinococcus geo |
| protein | proteins/slc35a1/ | SLC35A1 Human CMP-Sialic Acid Transporter | SLC35A1 is the human CMP-sialic acid transporter, a member of the SLC35 family o |
| protein | proteins/slc35c1/ | SLC35C1 Human GDP-Fucose Transporter | SLC35C1 is the human GDP-fucose transporter, a member of the SLC35 family of nuc |
| protein | proteins/smoothened-fla-fusion/ | SMO-FLA Fusion Construct (SMO-Flavodoxin) | The SMO-FLA fusion construct is an engineered human smoothened (SMO) receptor wi |
| protein | proteins/smoothened/ | Human Smoothened Receptor (SMO) | The human smoothened (SMO) receptor is a class frizzled (class F) G-protein-coup |
| protein | proteins/snap-25a/ | SNAP-25A (Rat Neuronal Qbc-SNARE Protein) | SNAP-25A (Synaptosomal-Associated Protein of 25 kDa, isoform A) is a neuronal Qb |
| protein | proteins/so-pip2-1/ | SoPIP2;1 (Spinach Plasma Membrane Aquaporin) | SoPIP2;1 is a plasma membrane intrinsic protein (PIP) from spinach (Spinacia ole |
| protein | proteins/spinach-light-harvesting-complex-ii/ | Spinach Light-Harvesting Complex II (LHC-II) | The spinach light-harvesting complex II (LHC-II) from Spinacia oleracea is the m |
| protein | proteins/spirulina-platensis-c15-ring/ | Spirulina platensis ATP Synthase c15 Ring | The c15 ring from the proton-coupled F1Fo ATP synthase of Spirulina platensis is |
| protein | proteins/sppa-bs/ | Signal Peptide Peptidase A from Bacillus subtilis | Signal peptide peptidase A (SppA) is a membrane-bound self-compartmentalized ser |
| protein | proteins/sppa-ec/ | Signal Peptide Peptidase A from Escherichia coli | Signal peptide peptidase (SppA) from *Escherichia coli* is the first crystal str |
| protein | proteins/squid-rhodopsin/ | Squid Rhodopsin (Primary Photochemical Reaction States) | Squid rhodopsin from Todarodes pacificus is an invertebrate visual pigment that  |
| protein | proteins/ssert/ | Human Serotonin Transporter (SERT) | The human serotonin transporter (SERT, also known as SLC6A4) is a neurotransmitt |
| protein | proteins/starkeya-novella-yddg/ | Starkeya novella YddG (SnYddG) | SnYddG is a member of the drug/metabolite transporter (DMT) superfamily from the |
| protein | proteins/stearoyl-coa-desaturase-1/ | Stearoyl-CoA Desaturase-1 (hSCD1) | Stearoyl-CoA desaturase-1 (SCD1) is an integral membrane enzyme in the endoplasm |
| protein | proteins/steroid-sulfatase/ | Steroid Sulfatase (hSTS) | Steroid sulfatase (hSTS) from human placenta is an integral membrane enzyme of t |
| protein | proteins/sucnr1/ | SUCNR1 (Succinate Receptor 1 / GPR91) | SUCNR1 (succinate receptor 1), also known as GPR91, is a class A G-protein-coupl |
| protein | proteins/synaptobrevin-2/ | Synaptobrevin-2 (Rat Neuronal Qc-SNARE Protein) | Synaptobrevin-2 (also known as VAMP-2) is a neuronal Qc-SNARE protein from rat t |
| protein | proteins/synechococcus-vkor/ | VKOR from Synechococcus sp. | VKOR (Vitamin K Epoxide Reductase) from Synechococcus sp. is a membrane-bound en |
| protein | proteins/synechocystis-halorhodopsin/ | Synechocystis Halorhodopsin (SyHR) | Synechocystis halorhodopsin (SyHR) is a light-driven anion pump from the cyanoba |
| protein | proteins/syntaxin-1a/ | Syntaxin-1A (Rat Neuronal Qa-SNARE Protein) | Syntaxin-1A is a neuronal Qa-SNARE protein from rat that plays a central role in |
| protein | proteins/tat-a-substrate/ | TatA Substrate of E. coli Rhomboid Protease GlpG | TatA is a prokaryotic substrate of the E. coli rhomboid intramembrane protease G |
| protein | proteins/tatc/ | Aquifex aeolicus TatC | Protein: tatc |
| protein | proteins/tcdA1/ | TcdA1 Toxin Complex A Subunit from Photorhabdus luminescens | TcdA1 is the TcA subunit of the toxin complex from Photorhabdus luminescens subs |
| protein | proteins/tcdB2-tccC3/ | TcdB2-TccC3 Toxin Complex B-C Fusion from Photorhabdus luminescens | TcdB2-TccC3 is a fusion protein from Photorhabdus luminescens subsp. akhurstii c |
| protein | proteins/thermothelomyces-thermophila-adp-atp-carrier/ | Thermothelomyces thermophila ADP/ATP Carrier | The Thermothelomyces thermophila ADP/ATP carrier (TtAac) is a mitochondrial inne |
| protein | proteins/thermus-thermophilus-a-atpase-peripheral-stalk/ | Thermus thermophilus A-ATPase Peripheral Stalk (PS2) | The Thermus thermophilus A-ATPase peripheral stalk (PS2) is a heterodimer of sub |
| protein | proteins/tlg2/ | Tlg2 | Tlg2 is a Qa-SNARE protein from the filamentous fungus Cryptococcus thermophilum |
| protein | proteins/tm287-288/ | TM287/288 (ABC Exporter from Thermotoga maritima) | TM287/288 is a heterodimeric ATP-binding cassette (ABC) exporter from the thermo |
| protein | proteins/tm86v-delta-ic3a/ | NTSR1 TM86V-ΔIC3A Mutant | NTSR1 TM86V-ΔIC3A is a directed evolution-selected mutant of the neurotensin rec |
| protein | proteins/tmppase/ | TmPPase (Thermotoga maritima H+-Pumping Pyrophosphatase) | TmPPase (H+-pumping inorganic pyrophosphatase from Thermotoga maritima) is a mem |
| protein | proteins/tonB/ | TonB (E. coli) | TonB is an integral polytopic membrane protein from Escherichia coli that serves |
| protein | proteins/traak/ | Human TRAAK Potassium Channel | TRAAK (tandem pore domain potassium channel 4, KCNK4) is a mechanosensitive two- |
| protein | proteins/transhydrogenase-dii-domain/ | Transhydrogenase dII Domain (Thermus thermophilus) | The transhydrogenase dII domain from Thermus thermophilus is the transmembrane p |
| protein | proteins/tric-b1/ | C. elegans TRIC-B1 Channel | TRIC-B1 is an intracellular cation channel from Caenorhabditis elegans belonging |
| protein | proteins/tric-b2/ | C. elegans TRIC-B2 Channel | TRIC-B2 is an intracellular cation channel from Caenorhabditis elegans belonging |
| protein | proteins/trka/ | TrkA (ATP-binding Regulatory Subunit from Klebsiella pneumoniae) | TrkA is a cytoplasmic ATP-binding regulatory subunit from the bacterium Klebsiel |
| protein | proteins/trkh/ | TrkH (Potassium Channel from Klebsiella pneumoniae) | TrkH is a potassium channel protein from the bacterium Klebsiella pneumoniae tha |
| protein | proteins/trpv5/ | Epithelial Calcium Channel TRPV5 | TRPV5 is a Ca²⁺-selective transient receptor potential vanilloid channel that, t |
| protein | proteins/trpv6/ | Epithelial Calcium Channel TRPV6 | TRPV6 is a Ca²⁺-selective transient receptor potential vanilloid channel uniquel |
| protein | proteins/turkey-beta1-ar-ligand-free-basal/ | Turkey Beta1-Adrenergic Receptor Ligand-Free Basal State | Turkey beta1-adrenergic receptor (beta1-AR) in its ligand-free basal state, dete |
| protein | proteins/turkey-beta1-ar-m23-2vt4/ | Turkey Beta1-Adrenergic Receptor Thermostabilized Mutant M23 with Cyanopindolol (2VT4) | The turkey beta1-adrenergic receptor (beta1AR) thermostabilized mutant M23 was c |
| protein | proteins/turkey-beta1-ar-m23/ | Turkey Beta1-Adrenergic Receptor M23 | The turkey beta1-adrenergic receptor (beta1AR) is a class A G protein-coupled re |
| protein | proteins/tysemisweet/ | TySemiSWEET from Thermotoga yellowstonii | TySemiSWEET is a bacterial sugar transporter from the SemiSWEET family found in  |
| protein | proteins/uraA/ | Uracil:Proton Symporter UraA from Escherichia coli | UraA from Escherichia coli is a uracil:proton symporter and a prototypical membe |
| protein | proteins/urea-transporter-dvut/ | Urea Transporter from Desulfovibrio vulgaris (dvUT) | The urea transporter from *Desulfovibrio vulgaris* (dvUT) is a bacterial
| protein | proteins/v1-atpase-t-thermophilus/ | V1-ATPase from Thermus thermophilus | V-type ATPase (V-ATPase) is a rotary ATPase complex that mediates energy convers |
| protein | proteins/vibrio-sp-semisweet/ | Vibrio sp. SemiSWEET | Vibrio sp. SemiSWEET is a bacterial sugar transporter from the SemiSWEET family  |
| protein | proteins/vp-zntb/ | Vp Zntb | The turkey beta1-adrenergic receptor (beta1AR-M23) is a class A G protein-couple |
| protein | proteins/vps45/ | Vps45 | Vps45 is a Sec1/Munc18-family (SM) protein from the filamentous fungus Cryptococ |
| protein | proteins/vrg4/ | Vrg4 GDP-Mannose Transporter (Saccharomyces cerevisiae) | Vrg4 is a GDP-mannose transporter from the yeast Saccharomyces cerevisiae, belon |
| protein | proteins/vrh-ppase/ | VrH+PPase (Vigna radiata H+-Pumping Inorganic Pyrophosphatase) | VrH+-PPase (H+-pumping inorganic pyrophosphatase from Vigna radiata, also known  |
| protein | proteins/vrppase/ | VrPPase (Vibrio rotiferans H+-Pumping Pyrophosphatase) | VrPPase (H+-pumping inorganic pyrophosphatase from Vibrio rotiferans) is a membr |
| protein | proteins/vsglt-k294a/ | vSGLT K294A Mutant | vSGLT K294A is a point mutant of the Vibrio parahaemolyticus Sodium-Galactose Tr |
| protein | proteins/vsglt-n64a/ | vSGLT N64A Mutant | vSGLT N64A is a point mutant of the Vibrio parahaemolyticus Sodium-Galactose Tra |
| protein | proteins/vsglt/ | V. parahaemolyticus Sodium-Galactose Transporter (vSGLT) | V. parahaemolyticus Sodium-Galactose Transporter (vSGLT) is a secondary active t |
| protein | proteins/xl-sigma-1-receptor/ | Sigma-1 Receptor from Xenopus laevis (xlS1R) | The sigma-1 receptor (S1R) from Xenopus laevis (xlS1R) is a non-opioid transmemb |
| protein | proteins/xyle/ | XylE (Escherichia coli Sugar Transporter) | XylE is an Escherichia coli homologue of the human glucose transporters GLUT1-4. |
| protein | proteins/yajc/ | E. coli YajC Transmembrane Protein | YajC is a single transmembrane (TM) protein from Escherichia coli that associate |
| protein | proteins/ybgH/ | E. coli YbgH Peptide Transporter | YbgH (also known as DtpD) is a proton-dependent oligopeptide transporter (POT) f |
| protein | proteins/ydah/ | A. borkumensis YdaH transporter | YdaH is an integral membrane protein from Alcanivorax borkumensis encoded by the |
| protein | proteins/yebT/ | E. coli YebT Tube-like MCE Protein | YebT (also known as MAM7) is a periplasm-spanning MCE (mammalian cell entry) pro |
| protein | proteins/zfp2x4/ | Zebrafish P2X4 Receptor (zfP2X4) | The zebrafish P2X4 receptor (zfP2X4) is a ligand-gated ion channel from Danio re |
| reagent | reagents/additives/1,4-butanediol/ | 1,4-Butanediol | 1,4-Butanediol is a linear diol used as a crystallization precipitant and additi |
| reagent | reagents/additives/1-6-hexanediol/ | 1,6-Hexanediol | 1,6-Hexanediol is a linear six-carbon diol used as a crystallization additive in |
| reagent | reagents/additives/2,6-di-t-butyl-p-cresol/ | 2,6-di-t-butyl-p-cresol | 2,6-di-t-butyl-p-cresol (2,6-di-t-BPC, BPC) is an antioxidant and preservative u |
| reagent | reagents/additives/5-iodo-a-85380/ | 5-Iodo-A-85380 | 5-Iodo-A-85380 is a potent agonist ligand selective for the alpha4beta2 subtype  |
| reagent | reagents/additives/ammonium-chloride/ | Ammonium Chloride | Ammonium chloride is an inorganic salt used as a crystallization precipitant for |
| reagent | reagents/additives/ammonium-formate/ | Ammonium Formate | Ammonium formate is a volatile salt used as a crystallization additive to improv |
| reagent | reagents/additives/ammonium-sulfate/ | Ammonium Sulfate | Ammonium sulfate is a common precipitant used in protein crystallization and pur |
| reagent | reagents/additives/ammonium-tartrate/ | Ammonium Tartrate | Ammonium tartrate is a salt of tartaric acid and ammonia used as a crystallizati |
| reagent | reagents/additives/bapta/ | BAPTA (1,2-Bis(o-aminophenoxy)ethane-N,N,N,N,-tetraacetic Acid) | BAPTA (1,2-bis(o-aminophenoxy)ethane-N,N,N,N-tetraacetic acid) is a calcium-sele |
| reagent | reagents/additives/barium-chloride/ | Barium Chloride | Barium chloride (BaCl2) is an inorganic salt that dissociates into Ba2+ ions in  |
| reagent | reagents/additives/beta-mercaptoethanol/ | beta-Mercaptoethanol | beta-Mercaptoethanol (2-mercaptoethanol) is a small thiol-containing reducing ag |
| reagent | reagents/additives/bodipy/ | BODIPY Fluorophore | BODIPY (boron-dipyromethene) is a fluorescent dye used for labeling molecules fo |
| reagent | reagents/additives/cadmium-chloride/ | Cadmium Chloride | Cadmium chloride (CdCl2) is an inorganic salt that provides cadmium ions (Cd2+)  |
| reagent | reagents/additives/calcium-acetate/ | Calcium Acetate | Calcium acetate is a calcium salt used as a crystallization additive and buffer  |
| reagent | reagents/additives/calcium-chloride/ | Calcium Chloride (CaCl₂) | Calcium chloride is a common inorganic salt used as a crystallization additive a |
| reagent | reagents/additives/cbfs/ | CBFS (8-(chloromercuri)-2-dibenzofuransulfonic acid) | CBFS (8-(chloromercuri)-2-dibenzofuransulfonic acid) is a mercurial compound use |
| reagent | reagents/additives/cellobiose/ | Cellobiose | Cellobiose is a disaccharide composed of two glucose units linked by a beta-1,4- |
| reagent | reagents/additives/cesium-chloride/ | Cesium Chloride | Cesium chloride (CsCl) is an inorganic salt that provides cesium ions (Cs+) used |
| reagent | reagents/additives/cholesteryl-hemisuccinate/ | Cholesteryl Hemisuccinate (CHS) | Cholesteryl hemisuccinate (CHS) is a cholesterol derivative commonly used as a s |
| reagent | reagents/additives/cobalt-hexamine/ | Hexaamminecobalt(III) (Cobalt Hexamine) | Hexaamminecobalt(III) chloride, commonly known as cobalt hexamine or Co(NH3)6 3+ |
| reagent | reagents/additives/decavanadate/ | Decavanadate | Decavanadate (V10O28 6-) is a polyvanadate anion consisting of ten vanadium atom |
| reagent | reagents/additives/deoxycholate/ | Deoxycholate (DXC) | Deoxycholate (DXC), or sodium deoxycholate, is a bile salt with anionic detergen |
| reagent | reagents/additives/dioxane/ | Dioxane | Dioxane (1,4-dioxane) is a cyclic ether used as a cryoprotectant and organic sol |
| reagent | reagents/additives/dtt/ | Dithiothreitol (DTT) | Dithiothreitol (DTT, also known as Cleland's reagent) is a strong reducing agent |
| reagent | reagents/additives/dysprosium-chloride/ | Dysprosium Chloride | Dysprosium(III) chloride is a heavy atom compound used for single-wavelength ano |
| reagent | reagents/additives/edta/ | Ethylenediaminetetraacetic Acid (EDTA) | Ethylenediaminetetraacetic acid (EDTA) is a hexadentate chelating agent that bin |
| reagent | reagents/additives/egta/ | EGTA (Ethylene Glycol Tetraacetic Acid) | EGTA (ethylene glycol tetraacetic acid) is a calcium-selective chelating agent w |
| reagent | reagents/additives/endoh/ | Endoglycosidase H (EndoH) | Endoglycosidase H (EndoH) is a glycosidase enzyme that cleaves high-mannose and  |
| reagent | reagents/additives/epibatidine/ | Epibatidine | Epibatidine is a potent alkaloid ligand that binds to nicotinic acetylcholine re |
| reagent | reagents/additives/ethyl-mercury-thiosalicylate/ | Ethyl Mercury Thiosalicylate EMTS Heavy Metal Derivative | Ethyl mercury thiosalicylate (EMTS) is a mercury-containing heavy metal derivati |
| reagent | reagents/additives/ethylene-glycol/ | Ethylene Glycol | Ethylene glycol (ethane-1,2-diol) is a small polyol compound used as a cryoprote |
| reagent | reagents/additives/g418/ | G418 (Geneticin) | G418 (geneticin) is an aminoglycoside antibiotic used as a selection agent in eu |
| reagent | reagents/additives/gadolinium-chloride/ | Gadolinium Chloride (GdCl3) | Gadolinium chloride (GdCl3) is a lanthanide salt that dissociates into Gd3+ ions |
| reagent | reagents/additives/glucose/ | Glucose | Glucose is a monosaccharide (simple sugar) that serves as a control compound in  |
| reagent | reagents/additives/glycerol-3-phosphate/ | Glycerol 3-Phosphate | Glycerol 3-phosphate (G3P) is a phosphorylated glycerol molecule that serves as  |
| reagent | reagents/additives/glycerol/ | Glycerol | Glycerol (propane-1,2,3-triol) is a small polyol widely used as a cryoprotectant |
| reagent | reagents/additives/glycylglycylglycine/ | Glycylglycylglycine (Gly3) | Glycylglycylglycine (Gly3, Gly-Gly-Gly) is a tripeptide composed of three glycin |
| reagent | reagents/additives/gold-iii-chloride/ | Gold(III) Chloride | Gold(III) chloride (AuCl3) is an inorganic salt that provides gold ions (Au3+) u |
| reagent | reagents/additives/guanidine-hydrochloride/ | Guanidine Hydrochloride | Guanidine hydrochloride is a strong chaotropic agent used to chemically denature |
| reagent | reagents/additives/hiload-sp-sepharose/ | Hiload SP Sepharose Ion Exchange Resin | Hiload SP Sepharose is a strong cation exchange chromatography resin from GE Hea |
| reagent | reagents/additives/hrv-3c-protease/ | HRV 3C Protease | HRV 3C protease (Human Rhinovirus 3C protease) is a cysteine protease that speci |
| reagent | reagents/additives/imidazole/ | Imidazole | Imidazole is a small organic compound commonly used as an eluent in Ni-NTA affin |
| reagent | reagents/additives/iodoacetamide/ | Iodoacetamide | Iodoacetamide is an alkylating agent that specifically modifies cysteine residue |
| reagent | reagents/additives/iptg/ | IPTG (Isopropyl-beta-D-thiogalactopyranoside) | Isopropyl-beta-D-thiogalactopyranoside (IPTG or IPTG) is a non-metabolizable ana |
| reagent | reagents/additives/iron/ | Iron (Fe) | Iron is a transition metal that serves as a cofactor in many membrane proteins i |
| reagent | reagents/additives/isopropyl-beta-d-thiogalactoside/ | Isopropyl beta-D-1-Thiogalactopyranoside (IPTG) | Isopropyl beta-D-1-thiogalactopyranoside (IPTG) is a non-hydrolyzable analog of  |
| reagent | reagents/additives/jeffamine-ed-2001/ | Jeffamine ED-2001 Polyalkylene Glycol | Jeffamine ED-2001 is a branched polyalkylene glycol used as a crystallization pr |
| reagent | reagents/additives/jeffamine-m600/ | Jeffamine M600 | Jeffamine M600 is a branched polyamine copolymer used as a crystallization preci |
| reagent | reagents/additives/kanamycin/ | Kanamycin | Kanamycin is an aminoglycoside antibiotic used as a selection agent in bacterial |
| reagent | reagents/additives/lithium-citrate/ | Lithium Citrate | Lithium citrate is a salt formed from citric acid and lithium, used as a crystal |
| reagent | reagents/additives/lithium-ion/ | Lithium Ion (Li+) | Lithium ion (Li+) is a coupling cation for the melibiose permease (MelB), which  |
| reagent | reagents/additives/lithium-sulfate/ | Lithium Sulfate | Lithium sulfate is an inorganic salt used as a crystallization additive and prec |
| reagent | reagents/additives/lutetium-acetate/ | Lutetium Acetate | Lutetium(III) acetate is a heavy atom compound used for single-wavelength anomal |
| reagent | reagents/additives/m2m/ | M2M (Bis-(3-Sulfanylpropionyl)disulfide, 2-Carbon Linker MTS Reagent) | M2M is a bifunctional maleimide thiosulfonate (MTS) reagent with a 2-carbon link |
| reagent | reagents/additives/m4m/ | M4M (Bis-(3-Sulfanylpropionyl)disulfide, 4-Carbon Linker MTS Reagent) | M4M is a bifunctional maleimide reagent (MTS: monobromobimane thiosulfonate) wit |
| reagent | reagents/additives/m8m/ | M8M (Bis-(3-Sulfanylpropionyl)disulfide, 8-Carbon Linker MTS Reagent) | M8M is a bifunctional maleimide thiosulfonate (MTS) reagent with an 8-carbon lin |
| reagent | reagents/additives/magnesium-chloride/ | Magnesium Chloride | Magnesium chloride (MgCl2) is a metal salt commonly used in protein crystallizat |
| reagent | reagents/additives/magnesium-sulfate/ | Magnesium Sulfate (MgSO4) | Magnesium sulfate (MgSO4) is an inorganic salt used as a source of magnesium ion |
| reagent | reagents/additives/maltose/ | Maltose | Maltose is a disaccharide composed of two glucose units linked by an alpha-1,4 g |
| reagent | reagents/additives/mercury-ii-chloride/ | Mercury(II) Chloride | Mercury(II) chloride (HgCl2) is an inorganic salt that provides mercury ions (Hg |
| reagent | reagents/additives/mercury/ | Mercury (HgCl2) - Aquaporin Inhibitor | Mercury(II) chloride (HgCl2) is a mercurial compound historically used to define |
| reagent | reagents/additives/methanol/ | Methanol | Methanol is the primary carbon source and inducer for the AOX1 (alcohol oxidase  |
| reagent | reagents/additives/methylmercury-chloride/ | Methylmercury Chloride | Methylmercury chloride (CH3HgCl) is a mercury-containing heavy metal derivative  |
| reagent | reagents/additives/mgcl2/ | Magnesium Chloride (MgCl₂) | Magnesium chloride is a common inorganic salt used as a crystallization additive |
| reagent | reagents/additives/mpd/ | 2-Methyl-2,4-pentanediol (MPD) | 2-Methyl-2,4-pentanediol (MPD) is a low-viscosity organic compound commonly used |
| reagent | reagents/additives/mtset/ | MTSET ((2-trimethylammonium)ethyl methanethiosulfonate) | MTSET (2-trimethylammonium)ethyl methanethiosulfonate) is a positively charged,  |
| reagent | reagents/additives/n-methyl-d-glucamine/ | N-Methyl-D-Glucamine (NMG) | N-Methyl-D-glucamine (NMG) is an organic compound used as an ion substitute in i |
| reagent | reagents/additives/nickel-nta/ | Ni-NTA Agarose Resin | Ni-NTA (Nickel-Nitrilotriacetic acid) agarose resin is a chromatography medium c |
| reagent | reagents/additives/nickel-sulfate/ | Nickel Sulfate (NiSO₄) | Nickel sulfate is an inorganic salt used in membrane protein crystallography, pa |
| reagent | reagents/additives/peg-1450/ | Polyethylene Glycol 1450 (PEG 1450) | Polyethylene glycol 1450 (PEG 1450) is a medium molecular weight polyethylene gl |
| reagent | reagents/additives/peg-350-mme/ | Polyethylene Glycol 350 Monomethyl Ether (PEG 350 MME) | Polyethylene glycol 350 monomethyl ether (PEG 350 MME) is a low molecular weight |
| reagent | reagents/additives/peg-400/ | Polyethylene Glycol 400 (PEG 400) | Polyethylene glycol 400 (PEG 400) is a water-soluble polymer with an average mol |
| reagent | reagents/additives/peg-4000/ | PEG 4000 (Polyethylene Glycol 4000) | PEG 4000 (polyethylene glycol with molecular weight 4000 Da) is a high molecular |
| reagent | reagents/additives/peg-5000-mme/ | Polyethylene Glycol 5000 Monomethyl Ether (PEG 5000 MME) | Polyethylene glycol 5000 monomethyl ether (PEG 5000 MME) is a high molecular wei |
| reagent | reagents/additives/peg-550mme/ | PEG 550MME (Polyethylene Glycol 550 Monomethyl Ether) | PEG 550MME (polyethylene glycol 550 monomethyl ether) is a low molecular weight  |
| reagent | reagents/additives/peg-600/ | PEG 600 | PEG 600 (polyethylene glycol with molecular weight 600 Da) is a water-soluble po |
| reagent | reagents/additives/peg-6000/ | PEG 6000 (Polyethylene Glycol 6000) | PEG 6000 (polyethylene glycol with molecular weight 6000 Da) is a high molecular |
| reagent | reagents/additives/peg/ | PEG (Polyethylene Glycol) | Polyethylene glycol (PEG) is a water-soluble polymer used as a linker in conjuga |
| reagent | reagents/additives/peg200/ | Polyethylene Glycol 200 (PEG200) | Polyethylene glycol 200 (PEG200) is a low-molecular-weight PEG used as a crystal |
| reagent | reagents/additives/peg300/ | Polyethylene Glycol 300 (PEG300) | Polyethylene glycol 300 (PEG300) is a low molecular weight polyethylene glycol u |
| reagent | reagents/additives/peg400/ | Polyethylene Glycol 400 (PEG400) | Polyethylene glycol 400 (PEG400) is a low molecular weight polyethylene glycol u |
| reagent | reagents/additives/peg600/ | PEG 600 | PEG 600 (polyethylene glycol with average molecular weight of approximately 600  |
| reagent | reagents/additives/peg6000/ | Polyethylene Glycol 6000 (PEG6000) | Polyethylene glycol 6000 (PEG6000) is a water-soluble polymer used as a precipit |
| reagent | reagents/additives/platinum-ii-chloride/ | Platinum(II) Chloride | Platinum(II) chloride (PtCl2) is an inorganic salt that provides platinum ions ( |
| reagent | reagents/additives/pmsf/ | PMSF (Phenylmethylsulfonyl Fluoride) | PMSF is a serine protease inhibitor commonly used during protein purification to |
| reagent | reagents/additives/pngase-f/ | Peptide:N-Glycosidase F (PNGase F) | Peptide:N-glycosidase F (PNGase F) is a glycosidase enzyme that cleaves all type |
| reagent | reagents/additives/potassium-acetate/ | Potassium acetate | Potassium acetate (CH₃COOK) is a potassium salt used as a crystallization additi |
| reagent | reagents/additives/potassium-chloride-kcl/ | Potassium Chloride (KCl) | Potassium chloride (KCl) is a common inorganic salt used in protein biochemistry |
| reagent | reagents/additives/potassium-ferricyanide/ | Potassium Ferricyanide | Potassium ferricyanide (K3[Fe(CN)6]) is an oxidizing agent used as an artificial |
| reagent | reagents/additives/potassium-fluoride/ | Potassium Fluoride (KF) | Potassium fluoride is a salt used as a crystallization additive in membrane prot |
| reagent | reagents/additives/potassium-formate/ | Potassium Formate | Potassium formate (HCOOK) is a small organic salt used as a precipitating agent  |
| reagent | reagents/additives/potassium-tetrakis-hydroxido-platinate-ii/ | Potassium Tetrakis(Hydroxido)platinate(II) K2Pt(NO2)4 Heavy Metal Derivative | Potassium tetrakis(hydroxido)platinate(II), K2Pt(NO2)4, is a heavy metal derivat |
| reagent | reagents/additives/pre-scission-protease/ | PreScission Protease | PreScission Protease is a site-specific protease that recognizes the seven-amino |
| reagent | reagents/additives/pre084/ | PRE084 | PRE084 is a high-affinity sigma-1 receptor (S1R) ligand used to study the ligand |
| reagent | reagents/additives/rubidium-acetate/ | Rubidium acetate | Rubidium acetate (RbCH₃COO) is a Rb⁺ salt used as a K⁺ congener for crystallogra |
| reagent | reagents/additives/s1ra/ | S1RA (4-[2-(5-methyl-1-(naphthalene-2-yl)-1H-pyrazol-3-yl)oxy]ethyl]morpholine) | S1RA is a sigma-1 receptor ligand purchased from Topscience Co. Ltd. It was used |
| reagent | reagents/additives/sa47/ | SA47 | SA47 is a potent exofacial inhibitor of human glucose transporters GLUT1 and GLU |
| reagent | reagents/additives/selenomethionine/ | Selenomethionine (SeMet) | Selenomethionine (SeMet) is a selenium-containing analog of the amino acid methi |
| reagent | reagents/additives/sodium-bicarbonate/ | Sodium Bicarbonate (NaHCO3) | Sodium bicarbonate (NaHCO3) is an inorganic salt that serves as a pH buffer and  |
| reagent | reagents/additives/sodium-butyrate/ | Sodium Butyrate | Sodium butyrate is the sodium salt of butyric acid (a four-carbon carboxylic aci |
| reagent | reagents/additives/sodium-chloride/ | Sodium Chloride | Sodium chloride is a common inorganic salt used in protein biochemistry and crys |
| reagent | reagents/additives/sodium-cyanoborohydride/ | Sodium Cyanoborohydride | Sodium cyanoborohydride (NaBH3CN) is a reducing agent used in the reductive meth |
| reagent | reagents/additives/sodium-ethylmercurithiosalicylate/ | Sodium Ethylmercurithiosalicylate | Sodium ethylmercurithiosalicylate (also referred to as ethylmercurithiosalicylic |
| reagent | reagents/additives/sodium-sulfite/ | Sodium Sulfite (Na2SO3) | Sodium sulfite (Na2SO3) is an inorganic salt that provides sulfite ions (SO3 2-) |
| reagent | reagents/additives/sodium-thiocyanate/ | Sodium Thiocyanate (NaSCN) | Sodium thiocyanate (NaSCN) is an inorganic salt used as a crystallization additi |
| reagent | reagents/additives/sorbitol/ | Sorbitol | Sorbitol (glucitol) is a sugar alcohol commonly used as an osmotic agent and sta |
| reagent | reagents/additives/spermine/ | Spermine | Spermine is a polyamine used as a crystallization additive in membrane protein c |
| reagent | reagents/additives/superdex-200/ | Superdex 200 Increase SEC Resin | Superdex 200 Increase is a prepacked size-exclusion chromatography (SEC) column  |
| reagent | reagents/additives/sypro-orange/ | SYPRO Orange Fluorescent Dye | SYPRO Orange is a fluorescent dye from Invitrogen used in fluorescence-based the |
| reagent | reagents/additives/talon/ | TALON Cobalt Affinity Resin | TALON cobalt affinity resin is a immobilized metal affinity chromatography (IMAC |
| reagent | reagents/additives/tcep/ | Tris(2-carboxyethyl)phosphine (TCEP) | Tris(2-carboxyethyl)phosphine (TCEP) is a water-soluble, strong reducing agent u |
| reagent | reagents/additives/tert-butanol/ | tert-Butanol | tert-Butanol (2-methyl-2-propanol) is a small, branched organic alcohol used as  |
| reagent | reagents/additives/thallium-acetate/ | Thallium acetate | Thallium acetate (TlCH₃COO) is a Tl⁺ salt used as a K⁺ congener for crystallogra |
| reagent | reagents/additives/thermolysin/ | Thermolysin | Thermolysin is a thermostable neutral metalloprotease produced by Bacillus therm |
| reagent | reagents/additives/tocopherol/ | Tocopherol (Vitamin E) | Tocopherol (commonly known as vitamin E) is a lipophilic antioxidant that protec |
| reagent | reagents/additives/trehalose/ | Trehalose | Trehalose is a non-reducing disaccharide used as a cryoprotectant and crystalliz |
| reagent | reagents/additives/trypsin/ | Trypsin | Trypsin is a serine protease that cleaves peptide bonds at the C-terminal side o |
| reagent | reagents/additives/vstx1/ | VSTX1 Tarantula Toxin | VSTX1 is a voltage-sensor toxin purified from tarantula venom that specifically  |
| reagent | reagents/additives/zinc-chloride/ | Zinc Chloride | Zinc chloride (ZnCl2) is an inorganic salt that provides zinc ions (Zn2+) used a |
| reagent | reagents/antibiotics/actinomycin-d/ | Actinomycin D | Actinomycin D is a cytotoxic polypeptide antibiotic that intercalates into DNA a |
| reagent | reagents/antibiotics/ampicillin/ | Ampicillin | Ampicillin is a beta-lactam antibiotic that inhibits bacterial cell wall synthes |
| reagent | reagents/antibiotics/chloramphenicol/ | Chloramphenicol | Chloramphenicol (Cm) is a broad-spectrum antibiotic that inhibits bacterial prot |
| reagent | reagents/antibiotics/fusidic-acid/ | Fusidic Acid | Fusidic acid is a steroidal antibacterial agent (CAS 6990-06-3) produced by Fusi |
| reagent | reagents/antibiotics/isocoumarin/ | Isocoumarin | Isocoumarin is a non-peptidic inhibitor of rhomboid protease GlpG that forms a c |
| reagent | reagents/antibiotics/linezolid/ | Linezolid | Linezolid ((S)-N-{3-[3-fluoro-4-(morpholin-4-yl)phenyl]-2-oxo-1,3-oxazolidin-5-y |
| reagent | reagents/antibiotics/nafcillin/ | Nafcillin | Nafcillin is a beta-lactam antibiotic (penicillinase-resistant penicillin) that  |
| reagent | reagents/antibiotics/valganciclovir/ | Valganciclovir | Valganciclovir is an antiviral prodrug consisting of a guanosine analog (gancicl |
| reagent | reagents/antibodies/2b12/ | 2B12 Antibody Fragment | 2B12 is a conformation-specific monoclonal antibody fragment (Fab) that selectiv |
| reagent | reagents/antibodies/6a10/ | 6A10 Antibody Fragment | 6A10 is a conformation-specific monoclonal antibody fragment (Fab) that selectiv |
| reagent | reagents/antibodies/8b6-antibody/ | 8B6 Monoclonal Antibody (SERT-specific) | 8B6 is a monoclonal antibody raised against human serotonin transporter (SERT).  |
| reagent | reagents/antibodies/fab-9d5/ | Fab 9D5 | Fab 9D5 is a monoclonal antibody fragment used as a crystallization aid for memb |
| reagent | reagents/antibodies/fab21/ | Fab21 Antibody Fragment | Fab21 is a monoclonal antibody fragment (Fab) derived from a type-2a IgG raised  |
| reagent | reagents/antibodies/fab5/ | Fab5 Antibody Fragment | Fab5 is a monoclonal antibody fragment (Fab) derived from the Mab5 immunoglobuli |
| reagent | reagents/antibodies/mab3949/ | MAB3949 Monoclonal Antibody (PAR2-specific) | MAB3949 is a commercial monoclonal antibody that binds with high affinity to hum |
| reagent | reagents/antibodies/nb-at110i1/ | Nb.AT110i1 Synthetic Nanobody | Nb.AT110i1 is a synthetic conformation-specific nanobody discovered using a yeas |
| reagent | reagents/antibodies/nb-n00/ | N00 Conformation-Selective Nanobody | N00 is a conformation-selective nanobody discovered through immunization of came |
| reagent | reagents/antibodies/nb35/ | Nb35 Nanobody | Nb35 is a conformation-selective nanobody (single-domain antibody fragment deriv |
| reagent | reagents/antibodies/nb9-8/ | Nb9-8 Nanobody | Nb9-8 is a G-protein mimetic camelid nanobody selected by conformational selecti |
| reagent | reagents/antibodies/scfv16/ | scFv16 Antibody Fragment | scFv16 is a single-chain variable fragment (scFv) antibody used as a stabilizing |
| reagent | reagents/antibodies/vhh15/ | VHH15 Nanobody | VHH15 is a llama-derived single-domain antibody (nanobody) that specifically tar |
| reagent | reagents/buffers/aces/ | ACES Buffer (N-(2-Acetamido)iminodiacetic Acid) | ACES (2-[N-(2-Acetamido)iminodiacetic acid]) is a zwitterionic buffering agent c |
| reagent | reagents/buffers/acetate/ | Acetate Buffer (Sodium Acetate) | Acetate buffer, typically prepared from sodium acetate and acetic acid, is a com |
| reagent | reagents/buffers/ammonium-acetate/ | Ammonium Acetate | Ammonium acetate is a volatile salt commonly used in protein crystallization as  |
| reagent | reagents/buffers/ammonium-phosphate/ | Ammonium Phosphate (Monobasic) | Ammonium phosphate (monobasic) is a commonly used buffer and crystallization pre |
| reagent | reagents/buffers/bicine/ | Bicine Buffer | Bicine (N,N-bis(2-hydroxyethyl)glycine) is a zwitterionic Good's buffer commonly |
| reagent | reagents/buffers/cacodylate/ | Cacodylate (Sodium Dimethylarsenate) | Cacodylate (sodium dimethylarsenate) is a buffering agent used in protein crysta |
| reagent | reagents/buffers/citrate/ | Citrate Buffer (Sodium Citrate) | Citrate buffer, prepared from citric acid and sodium citrate, is a buffer system |
| reagent | reagents/buffers/glycine/ | Glycine | Glycine is the simplest amino acid and is used as a buffer in protein crystalliz |
| reagent | reagents/buffers/hepes/ | HEPES Buffer | 4-(2-hydroxyethyl)-1-piperazineethanesulfonic acid (HEPES) is a commonly used zw |
| reagent | reagents/buffers/mes/ | 2-(N-Morpholino)ethanesulfonic Acid (MES) | 2-(N-Morpholino)ethanesulfonic acid (MES) is a Good's buffer commonly used in th |
| reagent | reagents/buffers/mops/ | MOPS (3-(N-Morpholino)propanesulfonic Acid) | MOPS (3-(N-morpholino)propanesulfonic acid) is a zwitterionic Good's buffer wide |
| reagent | reagents/buffers/pipes/ | PIPES (Piperazine-1,4-Bis(2-Ethanesulfonic Acid)) | PIPES (piperazine-1,4-bis(2-ethanesulfonic acid)) is a Good's buffer commonly us |
| reagent | reagents/buffers/sodium-citrate/ | Sodium Citrate | Sodium citrate is a buffer salt derived from citric acid, commonly used in bioch |
| reagent | reagents/buffers/sodium-phosphate/ | Sodium Phosphate | Sodium phosphate buffer is a widely used buffer system in protein crystallizatio |
| reagent | reagents/buffers/tes/ | TES Buffer (N-Tris(hydroxymethyl)methyl-2-aminoethanesulfonic acid) | TES (N-tris(hydroxymethyl)methyl-2-aminoethanesulfonic acid) is a zwitterionic G |
| reagent | reagents/buffers/tris-hcl/ | Tris-HCl Buffer | Tris-HCl (tris(hydroxymethyl)aminomethane hydrochloride) is a widely used buffer |
| reagent | reagents/buffers/tris/ | Tris (Tris-HCl Buffer) | Tris (tris(hydroxymethyl)aminomethane) is a widely used buffer in biochemistry,  |
| reagent | reagents/cofactors/bacteriochlorophyll/ | Bacteriochlorophyll | Bacteriochlorophyll (BChl) is a magnesium-coordinated chlorin pigment found in a |
| reagent | reagents/cofactors/bacteriopheophytin/ | Bacteriopheophytin | Bacteriopheophytin (BPhe) is a chlorin pigment found in photosynthetic reaction  |
| reagent | reagents/cofactors/menaquinone-7/ | Menaquinone-7 (MK-7) | Menaquinone-7 (MK-7) is a lipid-soluble electron carrier in bacterial electron t |
| reagent | reagents/cofactors/nadh/ | NADH | Nicotinamide adenine dinucleotide (reduced form, NADH) is a universal electron c |
| reagent | reagents/cofactors/nicotinic-acid-adenine-dinucleotide/ | Nicotinic Acid Adenine Dinucleotide (NaAD) | Nicotinic acid adenine dinucleotide (NaAD) is a nucleotide cofactor and the auth |
| reagent | reagents/cofactors/riboflavin/ | Riboflavin (Vitamin B2) | Riboflavin (vitamin B2) is an essential precursor for flavin mononucleotide (FMN |
| reagent | reagents/cofactors/s-adenosyl-l-homocysteine/ | S-Adenosyl-L-Homocysteine (AdoHcy) | S-adenosyl-L-homocysteine (AdoHcy) is the product of methyl transfer reactions c |
| reagent | reagents/cofactors/sam/ | S-Adenosyl-L-Methionine (SAM) | S-adenosyl-L-methionine (SAM) is the universal methyl donor used by methyltransf |
| reagent | reagents/cofactors/ubiquinone/ | Ubiquinone | Ubiquinone (Coenzyme Q10) is a lipid-soluble electron carrier in the mitochondri |
| reagent | reagents/cofactors/vitamin-k/ | Vitamin K | Vitamin K is a fat-soluble vitamin that exists in several forms, including vitam |
| reagent | reagents/detergents/anzergent-3-12/ | Anzergent 3,12 | Anzergent 3,12 is a mild zwitterionic detergent used for solubilizing membrane p |
| reagent | reagents/detergents/c12e8/ | Octaethylene Glycol Monododecyl Ether (C12E8) | Octaethylene glycol monododecyl ether (C12E8) is a nonionic detergent with a 12- |
| reagent | reagents/detergents/c12e9/ | C12E9 | C12E9 is a nonionic surfactant consisting of a dodecyl (C12) alkyl chain attache |
| reagent | reagents/detergents/c14-betaine/ | Tetradecylbetaine (C14-betaine) | Tetradecylbetaine (C14-betaine) is a zwitterionic detergent with a tetradecyl (C |
| reagent | reagents/detergents/c8e4/ | Octyltetraoxyethylene (C8E4) | Octyltetraoxyethylene (C8E4, n-octyltetraoxyethylene) is a nonionic detergent wi |
| reagent | reagents/detergents/chapso/ | CHAPSO | CHAPSO (3-[(3-cholamidopropyl)dimethylammonio]-2-hydroxy-1-propanesulfonate) is  |
| reagent | reagents/detergents/cholesterol-hydrogen-succinate/ | Cholesterol Hydrogen Succinate (CHS) | Cholesteryl hemisuccinate (CHS) is a cholesterol derivative used as a membrane p |
| reagent | reagents/detergents/cymal-4/ | Cymal-4 | Cymal-4 (4-(1-cyclohexylbutoxy)-3-cyclohexyl-1-propanol) is a nonionic detergent |
| reagent | reagents/detergents/cymal-6/ | Cymal-6 | Cymal-6 (6-(1-cyclohexylhexyloxy)-3-cyclohexyl-1-propanol) is a nonionic deterge |
| reagent | reagents/detergents/ddm/ | n-Dodecyl-beta-D-maltopyranoside (DDM) | n-Dodecyl-beta-D-maltopyranoside (DDM) is a mild nonionic detergent with a 12-ca |
| reagent | reagents/detergents/decylmaltoside/ | Decylmaltoside (DM) | Decylmaltoside (DM, n-decyl beta-D-maltopyranoside) is a nonionic detergent with |
| reagent | reagents/detergents/dhpc/ | 1,2-Dihexanoyl-sn-glycero-3-phosphocholine (DHPC) | DHPC (1,2-dihexanoyl-sn-glycero-3-phosphocholine) is a zwitterionic detergent de |
| reagent | reagents/detergents/digitonin/ | Digitonin | Digitonin is a mild nonionic triterpene glycoside detergent extracted from the r |
| reagent | reagents/detergents/dm/ | n-Decyl-beta-D-Maltoside (DM) | n-Decyl-beta-D-maltoside (DM) is a mild nonionic detergent with a 10-carbon alky |
| reagent | reagents/detergents/dmng/ | Decyl Maltose Neopentyl Glycol (DMng) | Decyl maltose neopentyl glycol (DMng) is a non-ionic detergent derived from the  |
| reagent | reagents/detergents/dodecanoyl-sucrose/ | Dodecanoyl Sucrose | Dodecanoyl sucrose is a sucrose-based nonionic detergent used for solubilizing a |
| reagent | reagents/detergents/dodecanoylmorpholine/ | Dodecanoylmorpholine (DM) | Dodecanoylmorpholine (DM) is a nonionic surfactant commonly used as a mild deter |
| reagent | reagents/detergents/dpc/ | Decylphosphocholine (DPC) | Decylphosphocholine (DPC) is a zwitterionic detergent commonly used in NMR studi |
| reagent | reagents/detergents/fos-choline-11/ | Fos-Choline 11 (FC-11) | Fos-Choline 11 (FC-11), also known as n-undecyl phosphocholine, is a zwitterioni |
| reagent | reagents/detergents/fos-choline-9/ | Fos-Choline 9 (FC-9) | Fos-Choline 9 (FC-9), also known as n-nonyl phosphocholine, is a zwitterionic de |
| reagent | reagents/detergents/foscholine-12/ | Foscholine-12 | Foscholine-12 is a nonionic detergent from the Fc (foscholine) series developed  |
| reagent | reagents/detergents/glyco-diosgenin/ | Glyco-diosgenin (GDN) | Glyco-diosgenin (GDN) is a mild nonionic detergent derived from diosgenin, a ste |
| reagent | reagents/detergents/hega-10/ | Decanoyl-N-Hydroxyethylglucamide (HEGA-10) | Decanoyl-N-Hydroxyethylglucamide (HEGA-10) is a nonionic glucoside detergent use |
| reagent | reagents/detergents/heptylglucoside/ | Heptylglucoside (HpG) | Heptylglucoside (HpG, n-heptyl beta-D-glucopyranoside) is a nonionic detergent w |
| reagent | reagents/detergents/heptylthioglucoside/ | Heptylthioglucoside (HpTG) | Heptylthioglucoside (HpG) is a mild nonionic detergent with a 7-carbon alkyl cha |
| reagent | reagents/detergents/hexylmaltoside/ | Hexyl Maltoside (HxM) | Hexyl maltoside (HxM, n-hexyl-beta-D-maltopyranoside) is a nonionic detergent wi |
| reagent | reagents/detergents/lDAO/ | Lauryldimethylamine N-oxide (LDAO) | Lauryldimethylamine N-oxide (LDAO) is a zwitterionic detergent with a 12-carbon  |
| reagent | reagents/detergents/lapao/ | LAPAO | LAPAO (3-laurylamido-N,N'-dimethylpropylaminoxyde) is a zwitterionic detergent u |
| reagent | reagents/detergents/lmng/ | Lauryl Maltose Neopentyl Glycol (LMNG) | LMNG (lauryl maltose neopentyl glycol, also known as MNG or MNG-3) is a nonionic |
| reagent | reagents/detergents/lppg/ | Lysophosphatidylcholine Phosphatidylglycerol (LPPG) | LPPG is a zwitterionic lipid-based detergent used in solution NMR studies of mem |
| reagent | reagents/detergents/mng-3-c8/ | Maltose Neopentyl Glycol 3-C8 (MNG-3-C8) | MNG-3-C8 is a maltose neopentyl glycol (MNG) detergent variant featuring an octy |
| reagent | reagents/detergents/n-methyl-beta-d-glucoside/ | n-Methyl-beta-D-glucoside (BNG) | n-Methyl-beta-D-glucoside (BNG or NG) is a mild nonionic detergent with a methyl |
| reagent | reagents/detergents/n-n-bis-3-d-gluconamidopropyl-deoxycholamide/ | N,N-Bis-(3-D-gluconamidopropyl)deoxycholamide (DBC) | N,N-Bis-(3-D-gluconamidopropyl)deoxycholamide (DBC) is a zwitterionic detergent  |
| reagent | reagents/detergents/n-nonyl-beta-d-maltopyranoside/ | n-Nonyl-beta-D-maltopyranoside (NM) | n-Nonyl-beta-D-maltopyranoside (NM) is a nonionic maltoside detergent with a 9-c |
| reagent | reagents/detergents/n-octyl-beta-d-maltoside/ | n-Octyl-beta-D-maltoside (OM) | n-Octyl-beta-D-maltoside (OM) is a nonionic detergent with an octyl (C8) alkyl c |
| reagent | reagents/detergents/nonylglucoside/ | Nonylglucoside (NG) | Nonylglucoside (NG, n-nonyl beta-D-glucopyranoside) is a nonionic detergent with |
| reagent | reagents/detergents/octaethylene-glycol-dodecylether-c12e8/ | Octaethylene Glycol Dodecylether (C12E8) | Octaethylene glycol dodecylether (C12E8) is a nonionic detergent with a dodecyl  |
| reagent | reagents/detergents/octaethylene-glycol-mono-n-dodecylether/ | Octaethylene Glycol Mono-n-Dodecylether (C12E6) | Octaethylene glycol mono-n-dodecylether (C12E6) is a nonionic detergent with a d |
| reagent | reagents/detergents/octyl-beta-d-galactopyranoside/ | Octyl-beta-D-galactopyranoside | Octyl-beta-D-galactopyranoside is a nonionic galactoside detergent used in membr |
| reagent | reagents/detergents/octylthioglucoside/ | Octylthioglucoside (OTG) | Octylthioglucoside (OG or OTG) is a mild nonionic detergent with an 8-carbon alk |
| reagent | reagents/detergents/og/ | n-Octyl beta-D-glucopyranoside (OG) | n-Octyl beta-D-glucopyranoside (OG) is a mild nonionic detergent with an 8-carbo |
| reagent | reagents/detergents/sodium-cholate/ | Sodium Cholate | Sodium cholate is an anionic bile salt detergent commonly used as a co-detergent |
| reagent | reagents/detergents/tridecylmaltoside/ | Tridecyl Maltoside (TDM) | Tridecyl maltoside (TDM) is a mild nonionic detergent with a 13-carbon alkyl cha |
| reagent | reagents/detergents/triton-x-100/ | Triton X-100 | Triton X-100 is a nonionic octylphenyl polyethoxylate detergent used for solubil |
| reagent | reagents/detergents/tween-20/ | Tween-20 Polysorbate 20 Nonionic Detergent | Tween-20 (polysorbate 20) is a nonionic detergent used at low concentrations (0. |
| reagent | reagents/detergents/udm/ | n-Undecyl-beta-D-maltoside (UDM) | n-Undecyl-beta-D-maltoside (UDM) is a nonionic maltoside detergent used for solu |
| reagent | reagents/ligands/11-cis-retinal/ | 11-cis-Retinal | 11-cis-retinal is the light-sensitive chromophore covalently bound to the apopro |
| reagent | reagents/ligands/2-ag/ | 2-AG (2-Arachidonoylglycerol) | 2-Arachidonoylglycerol (2-AG) is an endogenous cannabinoid (endocannabinoid) and |
| reagent | reagents/ligands/20s-hydroxycholesterol/ | 20(S)-Hydroxycholesterol (20S-OHC) | 20(S)-hydroxycholesterol (20S-OHC) is a cholesterol-derived oxysterol that acts  |
| reagent | reagents/ligands/2me-sadp/ | 2-Methylthio-ADP (2MeSADP) | 2-Methylthio-adenosine 5'-diphosphate (2MeSADP) is a stable analog of adenosine  |
| reagent | reagents/ligands/2npg/ | 4-Nitrophenyl-alpha-D-galactopyranoside (2NPG) | 4-Nitrophenyl-alpha-D-galactopyranoside (2NPG) is a galactopyranoside analog use |
| reagent | reagents/ligands/3-4-dichlorophenethylamine/ | 3,4-Dichlorophenethylamine (DCP) | 3,4-Dichlorophenethylamine (DCP) is a halogenated phenethylamine derivative that |
| reagent | reagents/ligands/3-quinuclidinyl-benzilate/ | 3-Quinuclidinyl-benzilate (QNB) | 3-Quinuclidinyl-benzilate (QNB) is a potent, high-affinity muscarinic acetylchol |
| reagent | reagents/ligands/4-hydroxytamoxifen/ | 4-Hydroxytamoxifen | 4-Hydroxytamoxifen (4-OH-Tam) is a primary metabolite of tamoxifen formed by 4-h |
| reagent | reagents/ligands/4-ibp/ | 4-IBP (4-Iodo-N-benzylpiperidine) | 4-IBP (4-iodo-N-benzylpiperidine) is a sigma-1 receptor ligand with incompletely |
| reagent | reagents/ligands/6-aminohexanoic-acid/ | 6-Aminohexanoic Acid (6-AHA) | 6-Aminohexanoic acid (6-AHA) is a seven-carbon amino acid (epsilon-aminocaproic  |
| reagent | reagents/ligands/7-benzylidenenaltrexone/ | 7-Benzylidenenaltrexone (BNTX) | 7-Benzylidenenaltrexone (BNTX) is a selective delta-opioid receptor (δ-OR) antag |
| reagent | reagents/ligands/77-lh-28-1/ | 77-LH-28-1 | 77-LH-28-1 is a potent orthosteric full agonist of the M1 muscarinic acetylcholi |
| reagent | reagents/ligands/a-317491/ | A-317491 | A-317491 is a small-molecule competitive antagonist of P2X receptors, particular |
| reagent | reagents/ligands/aaa/ | Ala-Ala-Ala (AAA) | Ala-Ala-Ala (AAA) is a tripeptide composed of three alanine residues. It was use |
| reagent | reagents/ligands/abi-pp/ | ABI-PP (tert-butyl thiazolyl aminocarboxyl pyridopyrimidine) | ABI-PP is a pyridopyrimidine derivative that acts as a specific inhibitor of the |
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
| reagent | reagents/ligands/am841/ | AM841 | AM841 is a synthetic THC-like cannabinoid agonist with high affinity for the CB1 |
| reagent | reagents/ligands/amantadine/ | Amantadine | Amantadine (1-aminoadamantane) is a small adamantyl-amine antiviral drug that in |
| reagent | reagents/ligands/amg3054/ | AMG3054 | AMG3054 is a designed 17-amino-acid apelin mimetic peptide agonist of the human  |
| reagent | reagents/ligands/amiloride/ | Amiloride | Amiloride is a pharmacological ion channel blocker that targets acid-sensing ion |
| reagent | reagents/ligands/amino-methoxy-isocoumarin/ | Amino-Methoxy-Isocoumarin (JLK-6) | Amino-methoxy-isocoumarin (7-amino-4-chloro-3-methoxy isocoumarin, also known as |
| reagent | reagents/ligands/amlodipine/ | Amlodipine | Amlodipine is a dihydropyridine calcium channel antagonist used primarily for th |
| reagent | reagents/ligands/amp-pnp/ | AMP-PNP (Adenylyl Imidodiphosphate) | AMP-PNP (adenylyl imidodiphosphate) is a non-hydrolysable ATP analogue commonly  |
| reagent | reagents/ligands/amppcp/ | AMPPCP (Adenosine 5'-[beta,gamma-methylene]triphosphate) | AMPPCP (adenosine 5'-[beta,gamma-methylene]triphosphate) is a non-hydrolyzable A |
| reagent | reagents/ligands/angiotensin-ii/ | Angiotensin II | Angiotensin II (AngII) is an octapeptide hormone and the endogenous agonist of t |
| reagent | reagents/ligands/anta-xv/ | Anta XV | Anta XV is a small-molecule antagonist of the human Smoothened (SMO) receptor. I |
| reagent | reagents/ligands/apelin-13/ | Apelin-13 | Apelin-13 is the shortest endogenous peptide agonist of the human apelin recepto |
| reagent | reagents/ligands/apelin-17/ | Apelin-17 | Apelin-17 is an endogenous peptide agonist of the human apelin receptor (APJR).  |
| reagent | reagents/ligands/atenolol/ | Atenolol | Atenolol is a selective beta-1 adrenergic receptor antagonist (beta-blocker) use |
| reagent | reagents/ligands/atp-gamma-s/ | ATPγS (Adenosine 5'-O-(3-thiotriphosphate)) | ATPγS (adenosine 5'-O-(3-thiotriphosphate)) is a non-hydrolyzable ATP analog in  |
| reagent | reagents/ligands/atp/ | Adenosine Triphosphate (ATP) | Adenosine triphosphate (ATP) is the universal energy currency of the cell and th |
| reagent | reagents/ligands/atropine/ | Atropine | Atropine is a competitive antagonist at muscarinic acetylcholine receptors. It i |
| reagent | reagents/ligands/au1235/ | AU1235 | AU1235 is an adamantyl urea compound that shows good bactericidal activity again |
| reagent | reagents/ligands/aybr-a/ | Ala-Tyr(L-3,5-diBr)-Ala (AY(Br)A) | Ala-Tyr(L-3,5-diBr)-Ala (AY(Br)A) is a tripeptide composed of L-alanine, L-tyros |
| reagent | reagents/ligands/aybr/ | Ala-Tyr(L-3,5-diBr) | Ala-Tyr(L-3,5-diBr) is a dipeptide composed of L-alanine and L-tyrosine substitu |
| reagent | reagents/ligands/az3451/ | AZ3451 (PAR2 Antagonist) | AZ3451 is a potent small-molecule antagonist of the human protease-activated rec |
| reagent | reagents/ligands/az8838/ | AZ8838 (PAR2 Antagonist) | AZ8838 is a selective small-molecule antagonist of the human protease-activated  |
| reagent | reagents/ligands/azd1283/ | AZD1283 | AZD1283 is a non-nucleotide reversible antagonist of the human P2Y12 receptor, d |
| reagent | reagents/ligands/bef3/ | BeF3 (Beryllium Fluoride) | Beryllium fluoride (BeF3-) is a phosphate analog used in structural biology to t |
| reagent | reagents/ligands/benzamidine/ | Benzamidine | Benzamidine is a carboximidamide compound with diverse pharmacological propertie |
| reagent | reagents/ligands/beta-cft/ | beta-CFT (CFT) | beta-CFT (2-beta-carbomethoxy-3-beta-(4-fluorophenyl)tropane) is a tropane alkal |
| reagent | reagents/ligands/beta-fna/ | beta-FNA (beta-Funaltrexamine) | beta-Funaltrexamine (beta-FNA) is an irreversible narcotic antagonist that coval |
| reagent | reagents/ligands/beta-foa/ | beta-FOA (beta-Fuoxymorphamine) | beta-Fuoxymorphamine (beta-FOA) is a morphinan agonist that differs from the ant |
| reagent | reagents/ligands/bi-167107/ | BI-167107 | BI-167107 is a potent, selective agonist ligand for the human beta2-adrenergic r |
| reagent | reagents/ligands/biil260/ | BIIL260 | BIIL260 is a selective antagonist for the leukotriene B4 receptor BLT1, bearing  |
| reagent | reagents/ligands/bms-681/ | BMS-681 | BMS-681 is a potent, selective small-molecule orthosteric antagonist of the CC c |
| reagent | reagents/ligands/bongkrekic-acid/ | Bongkrekic Acid | Bongkrekic acid (BKA) is a polyunsaturated methoxy tricarboxylic acid polyketide |
| reagent | reagents/ligands/bptu/ | BPTU | BPTU [1-(2-(2-(tert-butyl)phenoxy)pyridin-3-yl)-3-(4-(trifluoromethoxy)phenyl)ur |
| reagent | reagents/ligands/br-verapamil/ | Br-Verapamil | Br-verapamil is a brominated derivative of verapamil, a phenylalkylamine calcium |
| reagent | reagents/ligands/bremazocine/ | Bremazocine | Bremazocine is a kappa-opioid receptor (κ-OR) agonist with delta-opioid receptor |
| reagent | reagents/ligands/bromo-lidocaine/ | Bromo-lidocaine | Bromo-lidocaine is a derivative of the local anesthetic lidocaine with a bromine |
| reagent | reagents/ligands/bromoform/ | Bromoform (Tribromomethane) | Bromoform (tribromomethane, CHBr3) is a trihalomethane general anesthetic that i |
| reagent | reagents/ligands/bu72/ | BU72 | BU72 is a high-affinity morphinan agonist at the mu-opioid receptor (muOR). It i |
| reagent | reagents/ligands/bu74/ | BU74 | BU74 is a morphinan antagonist at the mu-opioid receptor. It is a complex oripav |
| reagent | reagents/ligands/bucindolol/ | Bucindolol | Bucindolol is a beta blocker (antagonist of the G protein-coupled pathway of bet |
| reagent | reagents/ligands/bw373u86/ | BW373U86 | BW373U86 is a selective delta-opioid receptor (δ-OR) agonist that displays minim |
| reagent | reagents/ligands/caffeine/ | Caffeine | Caffeine (1,3,7-trimethylxanthine) is a non-selective, weak antagonist of adenos |
| reagent | reagents/ligands/carazolol/ | Carazolol | Carazolol is a potent inverse agonist ligand for the beta-adrenergic receptors.  |
| reagent | reagents/ligands/carbamylcholine/ | Carbamylcholine | Carbamylcholine (carbachol) is a synthetic choline ester and a direct-acting mus |
| reagent | reagents/ligands/carmoterol/ | Carmoterol | Carmoterol is a potent beta-adrenergic receptor agonist used in structural studi |
| reagent | reagents/ligands/carotenoid/ | Carotenoid | Carotenoids are lipid-soluble pigments found in photosynthetic complexes and oth |
| reagent | reagents/ligands/carryatractyloside/ | Carboxyatractyloside | Carboxyatractyloside is a specific inhibitor of the mitochondrial ADP/ATP carrie |
| reagent | reagents/ligands/carvedilol/ | Carvedilol | Carvedilol is a beta blocker that acts as a biased agonist of beta-adrenoceptors |
| reagent | reagents/ligands/ccr2-ra-r/ | CCR2-RA-[R] | CCR2-RA-[R] is a potent, selective small-molecule allosteric antagonist of the C |
| reagent | reagents/ligands/chloride-ion/ | Chloride Ion (Cl-) | Chloride ion (Cl-) is an essential co-transport ion for neurotransmitter/sodium  |
| reagent | reagents/ligands/choline/ | Choline | Choline is a quaternary ammonium compound that serves as an essential nutrient i |
| reagent | reagents/ligands/clomipramine/ | Clomipramine (CMI) | Clomipramine (CMI) is a tricyclic antidepressant (TCA) used clinically for the t |
| reagent | reagents/ligands/cocaine/ | Cocaine | Cocaine is a tropane alkaloid that acts as a competitive inhibitor of the dopami |
| reagent | reagents/ligands/compound-1/ | Compound 1 | Compound 1 (Cpd 1) is a quinazolinone-biphenyltetrazole derivative that acts as  |
| reagent | reagents/ligands/compound-14-pyridothiadiazinone/ | Compound 14 (Pyridothiadiazinone) | Compound 14 is a pyridothiadiazinone-3-one 1,1-dioxide derivative described as a |
| reagent | reagents/ligands/compound-15-pa/ | Cmpd-15PA (Compound-15PA) | Cmpd-15PA is a negative allosteric modulator of the beta2-adrenergic receptor (b |
| reagent | reagents/ligands/compound-15/ | Cmpd-15 (Compound-15) | Cmpd-15 is a negative allosteric modulator of the beta2-adrenergic receptor (bet |
| reagent | reagents/ligands/compound-16-diazaspirodecane/ | Compound 16 (Diazaspirodecane) | Compound 16 is a diazaspirodecane sulfonamide synthesized as a benchmark from th |
| reagent | reagents/ligands/compound-2-beta2-ar/ | Compound 2 (Kolb et al., 2009) | Compound 2 is a potent inverse agonist of the human beta2-adrenergic receptor, o |
| reagent | reagents/ligands/compound-2/ | Compound 2 (AT2R dual ligand) | Compound 2 (Cpd 2) is a quinazolinone-biphenyltetrazole derivative that acts as  |
| reagent | reagents/ligands/cp-376395/ | CP-376395 | CP-376395 is a potent inverse agonist ligand for the human corticotropin-releasi |
| reagent | reagents/ligands/cp55940/ | CP55,940 | CP55,940 is a non-selective synthetic cannabinoid agonist that binds to both CB1 |
| reagent | reagents/ligands/cu(i)/ | Copper(I) Ion | Copper(I) (Cu+) is a monovalent copper ion that serves as a substrate for the Cu |
| reagent | reagents/ligands/cyanopindolol/ | Cyanopindolol | Cyanopindolol is a high-affinity antagonist ligand for beta-adrenergic receptors |
| reagent | reagents/ligands/cyclazocine/ | Cyclazocine | Cyclazocine is a mixed mu/kappa-opioid receptor agonist with delta-opioid recept |
| reagent | reagents/ligands/cyclic-di-gmp/ | Cyclic-di-GMP (Bis-(3'-5')-Cyclic Diguanylic Acid) | Cyclic-di-GMP (bis-(3'-5')-cyclic diguanylic acid) is a ubiquitous bacterial sec |
| reagent | reagents/ligands/cyclopamine/ | Cyclopamine | Cyclopamine is a naturally occurring teratogen and the first selective small-mol |
| reagent | reagents/ligands/d-amphetamine/ | D-Amphetamine | D-amphetamine is a psychostimulant and phenethylamine derivative that acts as a  |
| reagent | reagents/ligands/d-galactose/ | D-Galactose | D-Galactose is a monosaccharide (aldohexose) that serves as the primary substrat |
| reagent | reagents/ligands/dadle/ | DADLE (D-Ala2-MePhe4-Glyol5-Enkephalin) | DADLE (D-Ala2-MePhe4-Glyol5-enkephalin) is a selective delta-opioid receptor (δ- |
| reagent | reagents/ligands/dansyl-galactopyranoside-d2g/ | Dansyl-galactopyranoside (D2G) | Dansyl-galactopyranoside (D2G), formally 2'-(N-dansyl)aminoalkyl-1-thio-beta-D-g |
| reagent | reagents/ligands/daptomycin/ | Daptomycin | Daptomycin is a cyclic lipopeptide antibiotic used for treating serious infectio |
| reagent | reagents/ligands/daridorexant/ | Daridorexant | Daridorexant (ACT-541468, formerly nemorexant) is a dual orexin receptor antagon |
| reagent | reagents/ligands/daunomycin/ | Daunomycin | Daunomycin is an anthracycline anticancer drug that acts as a substrate for the  |
| reagent | reagents/ligands/desthiobiotin/ | Desthiobiotin | Desthiobiotin is a biotin analog lacking the sulfur atom in the tetrahydrothioph |
| reagent | reagents/ligands/desvenlafaxine/ | Desvenlafaxine | Desvenlafaxine is a serotonin-noradrenaline reuptake inhibitor (SNRI) antidepres |
| reagent | reagents/ligands/dhea/ | Dehydroepiandrosterone (DHEA) | Dehydroepiandrosterone (DHEA) is an endogenous androgen steroid hormone and a ke |
| reagent | reagents/ligands/dht/ | Dihydrotestosterone (DHT) | Dihydrotestosterone (DHT) is the most potent endogenous androgen steroid hormone |
| reagent | reagents/ligands/diacetylchitobiose/ | Diacetylchitobiose (GlcNAc2) | Diacetylchitobiose, also known as (GlcNAc)2 or chitobiose, is a disaccharide con |
| reagent | reagents/ligands/diisopropyl-fluorophosphate/ | Diisopropyl Fluorophosphate (DFP) | Diisopropyl fluorophosphate (DFP) is an organophosphate mechanism-based inhibito |
| reagent | reagents/ligands/dinicotinic-acid-adenine-dinucleotide/ | Dinicotinic Acid Adenine Dinucleotide (DaAD) | Dinicotinic acid adenine dinucleotide (DaAD) is a reaction intermediate in the n |
| reagent | reagents/ligands/diprenorphine/ | Diprenorphine | Diprenorphine is a broad-spectrum opioid receptor antagonist with affinity for m |
| reagent | reagents/ligands/dobutamine/ | Dobutamine | Dobutamine is a synthetic catecholamine derivative and a beta1-adrenergic recept |
| reagent | reagents/ligands/dopamine/ | Dopamine | Dopamine is the endogenous neurotransmitter substrate of the dopamine transporte |
| reagent | reagents/ligands/doxorubicin/ | Doxorubicin - Anthracycline Anticancer Drug | Doxorubicin is a widely used anthracycline anticancer antibiotic that functions  |
| reagent | reagents/ligands/dpcpx/ | DPCPX (8-Cyclopentyl-1,3-dipropylxanthine) | DPCPX (8-cyclopentyl-1,3-dipropylxanthine) is a selective adenosine A1 receptor  |
| reagent | reagents/ligands/du172/ | DU172 | DU172 (4-((3-(8-cyclohexyl-2,6-dioxo-1-propyl-1,2,6,7-tetrahydro-3H-purin-3-yl)p |
| reagent | reagents/ligands/duloxetine/ | Duloxetine | Duloxetine is a serotonin-noradrenaline reuptake inhibitor (SNRI) antidepressant |
| reagent | reagents/ligands/e-4-hydroxytamoxifen/ | E-4-Hydroxytamoxifen | E-4-Hydroxytamoxifen is the E-isomer of 4-hydroxytamoxifen, a primary metabolite |
| reagent | reagents/ligands/e-endoxifen/ | E-Endoxifen | E-Endoxifen is the E-isomer of endoxifen (4-hydroxy-N-desmethyltamoxifen), the p |
| reagent | reagents/ligands/elinogrel/ | Elinogrel | Elinogrel is a reversible antagonist of the P2Y12 receptor that was studied in f |
| reagent | reagents/ligands/empa/ | EMPA (N-ethyl-2-[(6-methoxy-pyridin-3-yl)-(toluene-2-sulfonyl)-amino]-N-pyridin-3-yl-methyl) | EMPA (N-ethyl-2-[(6-methoxy-pyridin-3-yl)-(toluene-2-sulfonyl)-amino]-N-pyridin- |
| reagent | reagents/ligands/endoxifen/ | Endoxifen | Endoxifen (4-hydroxy-N-desmethyltamoxifen) is the primary active metabolite of t |
| reagent | reagents/ligands/ergotamine/ | Ergotamine | Ergotamine is an ergoline-class alkaloid and a vasoconstrictor medication used f |
| reagent | reagents/ligands/estradiol/ | 17beta-Estradiol (E2) | 17beta-Estradiol (E2) is the most potent endogenous estrogen steroid hormone. It |
| reagent | reagents/ligands/estrone/ | Estrone (E1) | Estrone (E1) is an endogenous estrogen steroid hormone and the product of estron |
| reagent | reagents/ligands/etorphine/ | Etorphine | Etorphine is a potent broad-spectrum opioid receptor agonist with high affinity  |
| reagent | reagents/ligands/eu93-108/ | EU93-108 | EU93-108 is a novel piperazine-containing GluN2B-selective negative allosteric m |
| reagent | reagents/ligands/fenobam/ | Fenobam | Fenobam is a negative allosteric modulator (NAM) of the metabotropic glutamate r |
| reagent | reagents/ligands/ferulenol/ | Ferulenol | Ferulenol is a natural product and close structural analog of warfarin. It acts  |
| reagent | reagents/ligands/fluoxetine/ | Fluoxetine | Fluoxetine is a selective serotonin reuptake inhibitor (SSRI) antidepressant, on |
| reagent | reagents/ligands/fluvoxamine/ | Fluvoxamine | Fluvoxamine is a selective serotonin reuptake inhibitor (SSRI) antidepressant us |
| reagent | reagents/ligands/formoterol/ | Formoterol | Formoterol is a long-acting selective beta2-adrenergic receptor agonist used in  |
| reagent | reagents/ligands/fscpx/ | FSCPX | FSCPX is a covalent xanthine antagonist of the adenosine A1 receptor. It promote |
| reagent | reagents/ligands/gamma-butyrobetaine/ | Gamma-Butyrobetaine (4-Trimethylaminobutyrate) | Gamma-Butyrobetaine (also known as 4-trimethylaminobutyrate) is a quaternary amm |
| reagent | reagents/ligands/gdc-0449/ | GDC-0449 (Vismodegib) | GDC-0449 (vismodegib) is a small-molecule antagonist of the human Smoothened (SM |
| reagent | reagents/ligands/gdp/ | Guanosine Diphosphate (GDP) | Guanosine diphosphate (GDP) is a nucleotide that binds to the G alpha subunit of |
| reagent | reagents/ligands/glycine-betaine/ | Glycine Betaine | Glycine betaine (betaine) is a quaternary ammonium compound derived from the ami |
| reagent | reagents/ligands/gsk1034702/ | GSK1034702 | GSK1034702 is a bitopic orthosteric agonist of the M1 muscarinic acetylcholine r |
| reagent | reagents/ligands/gsk1059865/ | GSK1059865 | GSK1059865 is an orexin 1 receptor-selective antagonist (1-SORA) that was widely |
| reagent | reagents/ligands/heme/ | Heme | Heme is an iron-containing porphyrin cofactor found in many membrane proteins in |
| reagent | reagents/ligands/htl14242/ | HTL14242 (Compound 25) | HTL14242 (compound 25) is 3-chloro-5-[6-(5-fluoropyridin-2-yl)pyrimidin-4-yl]ben |
| reagent | reagents/ligands/htl6641/ | HTL6641 | HTL6641 is a dual orexin receptor antagonist (DORA) with a central benzo- or pyr |
| reagent | reagents/ligands/htl9936/ | HTL9936 | HTL9936 is a selective, partial orthosteric agonist of the human M1 muscarinic a |
| reagent | reagents/ligands/hu-308/ | HU-308 | HU-308 is a highly CB2-selective synthetic cannabinoid agonist. It shows approxi |
| reagent | reagents/ligands/ica38/ | ICA38 | ICA38 is an indolcarboxamide compound that targets MmpL3, an essential mycobacte |
| reagent | reagents/ligands/ici-118-551/ | ICI 118,551 | ICI 118,551 is a potent and selective beta2-adrenergic receptor antagonist (inve |
| reagent | reagents/ligands/ici-174-864/ | ICI-174,864 | ICI-174,864 is a selective delta-opioid receptor (δ-OR) inverse agonist. It is u |
| reagent | reagents/ligands/idp/ | Inositol Pyrophosphate (IDP) | Inositol pyrophosphate (IDP) serves as a substrate analog for inorganic pyrophos |
| reagent | reagents/ligands/ifenprodil/ | Ifenprodil | Ifenprodil is a selective negative allosteric modulator (NAM) of NMDA receptors  |
| reagent | reagents/ligands/iperoxo/ | Iperoxo | Iperoxo is a high-affinity muscarinic acetylcholine receptor agonist. It is a po |
| reagent | reagents/ligands/isoprenaline/ | Isoprenaline (Isoproterenol) | Isoprenaline (also known as isoproterenol) is a synthetic catecholamine and a po |
| reagent | reagents/ligands/ivermectin/ | Ivermectin | Ivermectin is a macrocyclic anthelmintic drug from the avermectin family that ac |
| reagent | reagents/ligands/kaad-cyclopamine/ | KAAD-cyclopamine | KAAD-cyclopamine is a BODIPY-tagged derivative of cyclopamine with a long-chain  |
| reagent | reagents/ligands/ketamine/ | Ketamine | Ketamine is a dissociative anesthetic and NMDA receptor antagonist that also inh |
| reagent | reagents/ligands/l-759-656/ | L-759,656 | L-759,656 is a CB2-selective synthetic cannabinoid agonist. It shows approximate |
| reagent | reagents/ligands/l-carnitine/ | L-Carnitine | L-Carnitine is a quaternary ammonium compound essential for the transport of act |
| reagent | reagents/ligands/l-leucine/ | L-Leucine | L-Leucine is an essential branched-chain amino acid and the canonical substrate  |
| reagent | reagents/ligands/l-methionine/ | L-Methionine | L-Methionine is a hydrophobic neutral amino acid that binds to the AvGluR1 ligan |
| reagent | reagents/ligands/l-phenylalanine/ | L-Phenylalanine | L-Phenylalanine is a large hydrophobic amino acid that binds to the AvGluR1 liga |
| reagent | reagents/ligands/lemborexant/ | Lemborexant | Lemborexant (Dayvigo) is a dual orexin receptor antagonist (DORA) approved by th |
| reagent | reagents/ligands/lj-4517/ | LJ-4517 (Compound 2) | LJ-4517 (compound 2) is a novel truncated nucleoside antagonist of the adenosine |
| reagent | reagents/ligands/lsd/ | LSD (Lysergic Acid Diethylamide) | LSD (lysergic acid diethylamide) is a potent ergoline-class hallucinogen and one |
| reagent | reagents/ligands/ltb4/ | Leukotriene B4 (LTB4) | Leukotriene B4 (LTB4) is a potent inflammatory lipid mediator derived from arach |
| reagent | reagents/ligands/luf5833/ | LUF5833 (Compound 8) | LUF5833 (compound 8) is a nonriboside partial agonist of the human adenosine A2A |
| reagent | reagents/ligands/lutein/ | Lutein | Lutein is a major carotenoid pigment found in photosynthetic light-harvesting co |
| reagent | reagents/ligands/ly2033298/ | LY2033298 | LY2033298 is a positive allosteric modulator (PAM) of the muscarinic M4 acetylch |
| reagent | reagents/ligands/ly2119620/ | LY2119620 | LY2119620 is a positive allosteric modulator (PAM) of the muscarinic M2 acetylch |
| reagent | reagents/ligands/ly2940680/ | LY2940680 | LY2940680 is a small-molecule antagonist of the smoothened (SMO) receptor, desig |
| reagent | reagents/ligands/m-mpep/ | M-MPEP | M-MPEP (2-[(3-methoxyphenyl)ethynyl]-6-methylpyridine) is a high-affinity negati |
| reagent | reagents/ligands/mavoglurant/ | Mavoglurant (AFQ056) | Mavoglurant (AFQ056, methyl (3aR,4S,7aR)-4-hydroxy-4-[(3-methylphenyl)ethynyl]oc |
| reagent | reagents/ligands/mazindol/ | Mazindol | Mazindol is a stimulant drug that acts as a norepinephrine and dopamine reuptake |
| reagent | reagents/ligands/melibiose/ | Melibiose | Melibiose is an alpha-linked disaccharide composed of galactose and glucose. It  |
| reagent | reagents/ligands/menaquinone/ | Menaquinone | Menaquinone (vitamin K2) is a lipid-soluble electron carrier in the electron tra |
| reagent | reagents/ligands/methamphetamine/ | Methamphetamine | Methamphetamine is a potent psychostimulant and phenethylamine derivative that a |
| reagent | reagents/ligands/mittx/ | MitTx Toxin | MitTx (MITxin) is a heterodimeric toxin from the venom of the Texas coral snake  |
| reagent | reagents/ligands/mk-0812/ | MK-0812 | MK-0812 is a tetrahydropyranyl cyclopentyl tetrahydropyridopyridine derivative d |
| reagent | reagents/ligands/mk-0893/ | MK-0893 | MK-0893 is a potent glucagon receptor (GCGR) antagonist discovered by Merck for  |
| reagent | reagents/ligands/mk-801/ | MK-801 (Dizocilpine) | MK-801 (dizocilpine) is a non-competitive, open-channel blocker of N-methyl-D-as |
| reagent | reagents/ligands/ml056/ | ML056 | ML056 is a selective agonist of the sphingosine-1-phosphate receptor 1 (S1P1). I |
| reagent | reagents/ligands/ml335/ | ML335 (N-aryl-sulfonamide K2P activator) | ML335 (N-[(2,4-dichlorophenyl)methyl]-4-(methanesulfonamido)benzamide) is a sele |
| reagent | reagents/ligands/ml402/ | ML402 (thiophene-carboxamide K2P activator) | ML402 (N-[2-(4-chloro-2-methylphenoxy)ethyl]thiophene-2-carboxamide) is a select |
| reagent | reagents/ligands/mp1104/ | MP1104 | MP1104 is a potent epoxymorphinan opioid agonist with an iodobenzamide substitue |
| reagent | reagents/ligands/mpep/ | MPEP (2-Methyl-6-(phenylethynyl)pyridine) | MPEP (2-methyl-6-(phenylethynyl)pyridine) is a potent, selective negative allost |
| reagent | reagents/ligands/mrs2500/ | MRS2500 | MRS2500 [(1'R,2'S,4'S,5'S)-4-(2-iodo-6-methylaminopurin-9-yl)-1-[(phosphato)meth |
| reagent | reagents/ligands/msx-2/ | MSX-2 | MSX-2 is a xanthine-based radioligand used for binding assays at adenosine recep |
| reagent | reagents/ligands/n-acetyl-s-geranylgeranyl-l-cysteine/ | N-Acetyl-S-Geranylgeranyl-L-Cysteine (AGGC) | N-Acetyl-S-geranylgeranyl-L-cysteine (AGGC) is a prenylcysteine substrate analog |
| reagent | reagents/ligands/n-desmethyltamoxifen/ | N-Desmethyltamoxifen | N-Desmethyltamoxifen (NM-Tam) is the primary metabolite of tamoxifen formed by N |
| reagent | reagents/ligands/n-methylscopolamine/ | N-methylscopolamine (NMS) | N-methylscopolamine (NMS) is a quaternary ammonium derivative of scopolamine tha |
| reagent | reagents/ligands/n-n-dimethylurea/ | N,N'-Dimethylurea (DMU) | N,N'-Dimethylurea (DMU) is a urea analogue in which both amide nitrogen atoms ar |
| reagent | reagents/ligands/naltriben/ | Naltriben | Naltriben is a selective delta-opioid receptor (δ-OR) antagonist containing a cy |
| reagent | reagents/ligands/naltrindole/ | Naltrindole | Naltrindole is a selective delta-opioid receptor (δ-OR) antagonist containing a  |
| reagent | reagents/ligands/ndt9513727/ | NDT9513727 | NDT9513727 is a non-peptide inverse agonist of the complement C5a receptor 1 (C5 |
| reagent | reagents/ligands/neca/ | NECA | NECA (5'-N-ethylcarboxamidoadenosine) is a non-selective adenosine receptor agon |
| reagent | reagents/ligands/neoxanthin/ | Neoxanthin | Neoxanthin is a carotenoid pigment found in photosynthetic light-harvesting comp |
| reagent | reagents/ligands/neurotensin/ | Neurotensin | Neurotensin is an endogenous tridecapeptide (YLSRNKEDPKYYP) that acts as the pri |
| reagent | reagents/ligands/nicotine/ | Nicotine | Nicotine is a naturally occurring alkaloid produced in Nicotiana species as a na |
| reagent | reagents/ligands/nimodipine/ | Nimodipine | Nimodipine is a dihydropyridine calcium channel antagonist used for the treatmen |
| reagent | reagents/ligands/nisoxetine/ | Nisoxetine | Nisoxetine is a selective norepinephrine reuptake inhibitor (NRI) and antidepres |
| reagent | reagents/ligands/nitd-349/ | NITD-349 | NITD-349 (N-(4,4-dimethylcyclohexyl)-4,6-difluoro-1H-indole-2-carboxamide) is an |
| reagent | reagents/ligands/nn-c0640/ | NNC0640 | NNC0640 is a small-molecule glucagon receptor (GCGR) antagonist developed by Nov |
| reagent | reagents/ligands/nortriptyline/ | Nortriptyline | Nortriptyline is a tricyclic antidepressant (TCA) that acts as a potent inhibito |
| reagent | reagents/ligands/oleoyl-coa/ | Oleoyl-CoA | Oleoyl-CoA (18:1-CoA) is the monounsaturated product of the stearoyl-CoA desatur |
| reagent | reagents/ligands/onb-hydroxyaspartate/ | ONB-hydroxyaspartate (o-nitrobenzyl-hydroxyaspartate) | ONB-hydroxyaspartate is a photocaged compound consisting of beta-hydroxyaspartat |
| reagent | reagents/ligands/ono-3080573/ | ONO-3080573 | ONO-3080573 is a selective antagonist of the lysophosphatidic acid receptor 1 (L |
| reagent | reagents/ligands/ono-9780307/ | ONO-9780307 | ONO-9780307 is a selective antagonist of the lysophosphatidic acid receptor 1 (L |
| reagent | reagents/ligands/ono-9910539/ | ONO-9910539 | ONO-9910539 is a selective antagonist of the lysophosphatidic acid receptor 1 (L |
| reagent | reagents/ligands/ouabain/ | Ouabain | Ouabain is a cardiotonic steroid (cardiac glycoside) that specifically inhibits  |
| reagent | reagents/ligands/p-ome-azo-tboa/ | p-OMe-azo-TBOA (4-methoxyazobenzene-TBOA) | p-OMe-azo-TBOA is a photoswitchable azobenzene derivative of TBOA (DL-threo-beta |
| reagent | reagents/ligands/paclitaxel/ | Paclitaxel | Paclitaxel (Taxol) is a microtubule-stabilizing antimitotic agent widely used in |
| reagent | reagents/ligands/paroxetine/ | Paroxetine | Paroxetine is a selective serotonin reuptake inhibitor (SSRI) antidepressant use |
| reagent | reagents/ligands/pc-tx1/ | Pilidium Toxin 1 (PcTx1) | Pilidium toxin 1 (PcTx1) is a 37-amino-acid peptide toxin from the venom of the  |
| reagent | reagents/ligands/pd144418/ | PD144418 | PD144418 is a high-affinity, selective sigma-1 receptor antagonist used in struc |
| reagent | reagents/ligands/pentachlorophenol/ | Pentachlorophenol (PCP) | Pentachlorophenol (PCP) is a chlorinated phenolic compound that functions as a q |
| reagent | reagents/ligands/peptide-5/ | Peptide 5 (Truncated GLP-1 Agonist Nonapeptide) | Peptide 5 is a truncated GLP-1 receptor agonist nonapeptide designed for structu |
| reagent | reagents/ligands/pg-934/ | PG-934 | PG-934 is a seven-residue macrocyclic peptide antagonist of the human melanocort |
| reagent | reagents/ligands/photoNECA-blue/ | trans-photoNECA (blue) | trans-photoNECA (blue) is a novel photoswitchable ligand designed for  structura |
| reagent | reagents/ligands/pirenzepine/ | Pirenzepine | Pirenzepine is a selective muscarinic acetylcholine receptor antagonist with pre |
| reagent | reagents/ligands/plastoquinone/ | Plastoquinone | Plastoquinone (PQ) is a lipophilic benzoquinone electron carrier in the photosyn |
| reagent | reagents/ligands/preladenant/ | Preladenant | Preladenant (SCH-420814) is a potent, highly selective non-xanthine antagonist o |
| reagent | reagents/ligands/psb-2113/ | PSB-2113 (PEGylated Preladenant) | PSB-2113 is a PEGylated derivative of Preladenant (SCH-420814), a potent and hig |
| reagent | reagents/ligands/psb36/ | PSB36 | PSB36 is a selective adenosine A1 receptor antagonist with a 3-hydroxy-propyl gr |
| reagent | reagents/ligands/pyridinium-3-5-biscarboxylic-acid-mononucleotide/ | Pyridinium-3,5-Biscarboxylic Acid Mononucleotide (P2CMN) | Pyridinium-3,5-biscarboxylic acid mononucleotide (P2CMN) is the direct product o |
| reagent | reagents/ligands/reboxetine/ | Reboxetine | Reboxetine is a selective norepinephrine reuptake inhibitor (NRI) and antidepres |
| reagent | reagents/ligands/retinal/ | Retinal | Retinal (vitamin A aldehyde) is the light-absorbing chromophore covalently bound |
| reagent | reagents/ligands/rhodamine-6g/ | Rhodamine 6G - Fluorescent Xanthene Dye | Rhodamine 6G is a fluorescent xanthene dye widely used as a substrate probe for  |
| reagent | reagents/ligands/rimantadine/ | Rimantadine | Rimantadine is a racemic adamantyl-amine antiviral drug that inhibits the M2 pro |
| reagent | reagents/ligands/rimonabant/ | Rimonabant | Rimonabant is a cannabinoid CB1 receptor antagonist that was approved by the Eur |
| reagent | reagents/ligands/risperidone/ | Risperidone | Risperidone is an atypical antipsychotic drug with a benzisoxazole scaffold. It  |
| reagent | reagents/ligands/ro25-6981/ | Ro25-6981 | Ro25-6981 is a potent, GluN2B-selective negative allosteric modulator (NAM) of N |
| reagent | reagents/ligands/rolofylline/ | Rolofylline | Rolofylline is a selective adenosine A1 receptor antagonist with a 3-nor-adamant |
| reagent | reagents/ligands/rti-55/ | RTI-55 | RTI-55 (2-beta-carbomethoxy-3-beta-(4-iodophenyl)tropane) is a tropane alkaloid  |
| reagent | reagents/ligands/s-citalopram/ | (S)-Citalopram | (S)-Citalopram is the pharmacologically active enantiomer of citalopram, a selec |
| reagent | reagents/ligands/s1i8/ | S1I8 Peptide | S1I8 (Sarcosine1, Isoleucine8-Angiotensin II) is a partial agonist peptide analo |
| reagent | reagents/ligands/s1p/ | S1P (Sphingosine-1-Phosphate) | Sphingosine-1-phosphate (S1P) is a bioactive lysophospholipid signaling molecule |
| reagent | reagents/ligands/sag1.5/ | SAG1.5 | SAG1.5 (3-chloro-4,7-difluoro-N-[trans-4-(methylamino)cyclohexyl]-N-[[3-(4-pyrid |
| reagent | reagents/ligands/salbutamol/ | Salbutamol (Albuterol) | Salbutamol (also known as albuterol in the United States) is a synthetic catecho |
| reagent | reagents/ligands/salvinorin-a/ | Salvinorin A | Salvinorin A (SalA) is a selective kappa opioid receptor (KOP) agonist derived f |
| reagent | reagents/ligands/sant1/ | SANT1 | SANT1 (N-[(1E)-(3,5-dimethyl-1-phenyl-1H-pyrazol-4-yl)methylidene]-4-(phenylmeth |
| reagent | reagents/ligands/sb-334867/ | SB-334867 | SB-334867 is the first selective orexin-1 receptor antagonist (1-SORA) disclosed |
| reagent | reagents/ligands/sb-408124/ | SB-408124 | SB-408124 is a selective urea antagonist of the orexin-1 receptor (1-SORA). It f |
| reagent | reagents/ligands/sbl-mc-31/ | SBL-MC-31 | SBL-MC-31 is a newly synthesized seven-residue macrocyclic peptide antagonist of |
| reagent | reagents/ligands/scopolamine/ | Scopolamine | Scopolamine (hyoscyamine) is a non-selective muscarinic receptor antagonist that |
| reagent | reagents/ligands/selatogrel/ | Selatogrel | Selatogrel (ACT-246475) is a potent, reversible, and highly selective inverse ag |
| reagent | reagents/ligands/serotonin/ | Serotonin (5-Hydroxytryptamine, 5-HT) | Serotonin (5-hydroxytryptamine, 5-HT) is a biogenic amine neurotransmitter that  |
| reagent | reagents/ligands/sertraline/ | Sertraline | Sertraline is a selective serotonin reuptake inhibitor (SSRI) antidepressant use |
| reagent | reagents/ligands/shu9119/ | SHU9119 | SHU9119 is a six-residue macrocyclic peptide antagonist of melanocortin receptor |
| reagent | reagents/ligands/slv320/ | SLV320 | SLV320 is a selective adenosine A1 receptor antagonist with a unique pyrrolopyri |
| reagent | reagents/ligands/sodium-ion/ | Sodium Ion (Na+) | Sodium ion (Na+) serves as a negative allosteric modulator in many class A G pro |
| reagent | reagents/ligands/spiperone/ | Spiperone | Spiperone is a typical antipsychotic drug of the butyrophenone class with high a |
| reagent | reagents/ligands/spiro-adamantyl-amine/ | Spiro-Adamantyl Amine | Spiro-adamantyl amine is a member of the adamantyl-amine class of influenza A M2 |
| reagent | reagents/ligands/spiro/ | SPIRO | SPIRO (1-((2,3-dihydrobenzobdioxin-6-yl)methyl)-6',7'-dihydrospiro[piperidine-4, |
| reagent | reagents/ligands/sq109/ | SQ109 | SQ109 (N-[1-(2,6-dioxopiperidin-3-yl)-1-(4-fluorophenyl)ethyl]-N-(2-(piperidin-1 |
| reagent | reagents/ligands/sr48692/ | SR48692 | SR48692 is a potent, selective, non-peptide antagonist of the neurotensin recept |
| reagent | reagents/ligands/stearoyl-coa/ | Stearoyl-CoA | Stearoyl-coenzyme A (stearoyl-CoA) is a fatty acyl-CoA thioester consisting of a |
| reagent | reagents/ligands/strychnine/ | Strychnine | Strychnine is a potent indole alkaloid antagonist of the glycine receptor (GlyR) |
| reagent | reagents/ligands/succinate/ | Succinate (Succinic Acid) | Succinate (succinic acid) is a small dicarboxylic acid and a crucial intermediat |
| reagent | reagents/ligands/sucrose/ | Sucrose | Sucrose is a non-reducing disaccharide composed of glucose and fructose units li |
| reagent | reagents/ligands/suvorexant/ | Suvorexant | Suvorexant is a dual orexin receptor antagonist (DORA) with subnanomolar affinit |
| reagent | reagents/ligands/t-acbd/ | t-ACBD (trans-1-Aminocyclobutane-1,3-dicarboxylic Acid) | t-ACBD (trans-1-aminocyclobutane-1,3-dicarboxylic acid) is a cyclic amino acid t |
| reagent | reagents/ligands/tamoxifen/ | Tamoxifen | Tamoxifen is a triphenylethylene-based selective estrogen receptor modulator (SE |
| reagent | reagents/ligands/taranabant/ | Taranabant | Taranabant is a potent, selective CB1 receptor inverse agonist used for structur |
| reagent | reagents/ligands/tboa/ | TBOA (DL-threo-beta-benzyloxyaspartic acid) | TBOA (DL-threo-beta-benzyloxyaspartic acid) is a competitive, nontransported inh |
| reagent | reagents/ligands/tc114/ | TC114 (SMO Ligand) | TC114 is a designed small-molecule ligand for the human smoothened (SMO) recepto |
| reagent | reagents/ligands/tdg/ | Thiodigalactoside (TDG) | Thiodigalactoside (TDG) is a non-hydrolyzable galactoside analog used as a high- |
| reagent | reagents/ligands/tetrabutylammonium-bromide/ | Tetrabutylammonium Bromide (TBSb) | Tetrabutylammonium bromide (TBSb) is a quaternary ammonium salt consisting of th |
| reagent | reagents/ligands/tetrabutylammonium/ | Tetrabutylammonium (TBA) | Tetrabutylammonium (TBA) is a quaternary ammonium compound that acts as a potent |
| reagent | reagents/ligands/tetraethylammonium/ | Tetraethylammonium (TEA) | Tetraethylammonium (TEA) is a quaternary ammonium compound that acts as a potent |
| reagent | reagents/ligands/tetramethylammonium/ | Tetramethylammonium (TMA) | Tetramethylammonium (TMA) is the smallest quaternary ammonium compound used as a |
| reagent | reagents/ligands/thapsigargin/ | Thapsigargin | Thapsigargin is a sesquiterpene lactone that acts as a specific, non-competitive |
| reagent | reagents/ligands/theophylline/ | Theophylline | Theophylline (1,3-dimethylxanthine) is a non-selective, weak antagonist of adeno |
| reagent | reagents/ligands/ticagrelor/ | Ticagrelor | Ticagrelor is a reversible, market-approved antagonist of the human P2Y12 recept |
| reagent | reagents/ligands/tiotropium/ | Tiotropium | Tiotropium is a long-acting anticholinergic medication used in the maintenance t |
| reagent | reagents/ligands/tnp-atp/ | 2'3'-O-(4,5-Dinitrobenzoyl)adenosine 5'-triphosphate (TNP-ATP) | TNP-ATP is a fluorescent analog of adenosine triphosphate (ATP) in which the ade |
| reagent | reagents/ligands/tungstate/ | Tungstate (WO4 2-) | Tungstate (WO4 2-) is a structural analog of inorganic phosphate (Pi) and inorga |
| reagent | reagents/ligands/ubiquinone-1/ | Ubiquinone-1 (UQ1) | Ubiquinone-1 (UQ1) is the one-isoprenoid-unit variant of ubiquinone (coenzyme Q1 |
| reagent | reagents/ligands/uk-59811/ | UK-59811 | UK-59811 is a brominated dihydropyridine calcium channel antagonist. The bromine |
| reagent | reagents/ligands/uk432097/ | UK432097 | UK432097 is a full agonist of the human adenosine A2A receptor (A2AR). It has be |
| reagent | reagents/ligands/uracil/ | Uracil | Uracil is a pyrimidine base and the natural substrate of the uracil:proton sympo |
| reagent | reagents/ligands/valinomycin/ | Valinomycin | Valinomycin is a macyclic ionophore antibiotic that selectively transports potas |
| reagent | reagents/ligands/verapamil/ | Verapamil | Verapamil is a phenylalkylamine calcium channel blocker and one of the earliest  |
| reagent | reagents/ligands/violaxanthin/ | Violaxanthin | Violaxanthin is a xanthophyll carotenoid that serves as a key component of the x |
| reagent | reagents/ligands/vismodegib/ | Vismodegib (GDC-0449) | Vismodegib (GDC-0449) is an FDA-approved small-molecule antagonist of the smooth |
| reagent | reagents/ligands/vorapaxar/ | Vorapaxar | Vorapaxar is a functionally irreversible small-molecule antagonist of the human  |
| reagent | reagents/ligands/w-54011/ | W-54011 | W-54011 is a small-molecule competitive antagonist of the complement C5a recepto |
| reagent | reagents/ligands/warfarin/ | Warfarin | Warfarin is a coumarin-derived anticoagulant drug that acts as a competitive inh |
| reagent | reagents/ligands/z-4-hydroxytamoxifen/ | Z-4-Hydroxytamoxifen | Z-4-Hydroxytamoxifen is the Z-isomer of 4-hydroxytamoxifen, a primary metabolite |
| reagent | reagents/ligands/z-endoxifen/ | Z-Endoxifen | Z-Endoxifen is the Z-isomer of endoxifen (4-hydroxy-N-desmethyltamoxifen), the p |
| reagent | reagents/ligands/zd7155/ | ZD7155 | ZD7155 is a high-affinity, selective non-peptide antagonist of the angiotensin I |
| reagent | reagents/ligands/zm241385/ | ZM241385 | ZM241385 is a bicyclic xanthine-based antagonist of the adenosine A2A receptor ( |
| reagent | reagents/lipids/6-ddtre/ | 6-n-Dodecyl-alpha,alpha-trehalose (6-DDTre) | 6-n-Dodecyl-alpha,alpha-trehalose (6-DDTre) is a lipid analog consisting of a do |
| reagent | reagents/lipids/bacterioruberin/ | Bacterioruberin | Bacterioruberin is a C50 carotenoid pigment found in halophilic archaea, particu |
| reagent | reagents/lipids/cardiolipin/ | Cardiolipin | Cardiolipin is a double-phospholipid found predominantly in the inner mitochondr |
| reagent | reagents/lipids/ceramide/ | Ceramide | Ceramide is a sphingolipid composed of a sphingosine base linked to a fatty acid |
| reagent | reagents/lipids/cholesterol-hydrogen-succinate/ | Cholesteryl Hemisuccinate (CHS) | Cholesteryl hemisuccinate (CHS) is a cholesterol derivative used as a membrane p |
| reagent | reagents/lipids/cholesterol/ | Cholesterol | Cholesterol is a sterol lipid and essential component of eukaryotic cell membran |
| reagent | reagents/lipids/cytidine-diphosphate-diacylglycerol/ | Cytidine Diphosphate Diacylglycerol | Cytidine diphosphate-diacylglycerol (CDP-DAG) is a nucleotide lipid intermediate |
| reagent | reagents/lipids/digalactosyl-diacylglycerol/ | Digalactosyl Diacylglycerol | Digalactosyl diacylglycerol (DGDG) is a galactolipid consisting of a digalactose |
| reagent | reagents/lipids/dmpc/ | DMPC (1,2-Dimyristoyl-sn-glycero-3-phosphocholine) | DMPC (1,2-dimyristoyl-sn-glycero-3-phosphocholine) is a synthetic diacyl phospho |
| reagent | reagents/lipids/dopc/ | 1,2-Dioleoyl-sn-glycero-3-phosphocholine (DOPC) | 1,2-Dioleoyl-sn-glycero-3-phosphocholine (DOPC) is a synthetic phospholipid with |
| reagent | reagents/lipids/e-coli-polar-lipids/ | E. coli Polar Lipids | E. coli polar lipids are a mixture of phospholipids extracted from Escherichia c |
| reagent | reagents/lipids/ecoli-phospholipids/ | E. coli Polar Phospholipids | E. coli polar phospholipids are a mixture of lipids extracted from Escherichia c |
| reagent | reagents/lipids/glycolipid/ | Glycolipid | Glycolipids are lipids with attached carbohydrate groups, used as membrane mimet |
| reagent | reagents/lipids/lysophosphatidylcholine/ | Lysophosphatidylcholine (LPC) | Lysophosphatidylcholine (LPC) is a monoacyl phospholipid consisting of a glycero |
| reagent | reagents/lipids/mag-8.7/ | MAG 8.7 (Monoolein, Avanti) | MAG 8.7 is a monoglyceride lipid (1-monooleoyl-glycerol) supplied by Avanti Pola |
| reagent | reagents/lipids/mag/ | Monoacylglycerol (MAG) | Monoacylglycerol (MAG), specifically 7.9 MAG (a mixture with average chain lengt |
| reagent | reagents/lipids/monogalactosyl-diacylglycerol/ | Monogalactosyl Diacylglycerol (MGDG) | Monogalactosyl diacylglycerol (MGDG) is the most abundant lipid in thylakoid mem |
| reagent | reagents/lipids/monoolein/ | Monoolein | Monoolein (1-monoolein) is a monoglyceride consisting of a single oleic acid (ci |
| reagent | reagents/lipids/monopalmitolein/ | Monopalmitolein | Monopalmitolein (9.7 MAG, 1-(9Z-hexadecenoyl)-rac-glycerol) is a monoacylglycero |
| reagent | reagents/lipids/monovaccenin/ | Monovaccenin | Monovaccenin (11.7 MAG, 1-(11Z-octadecenoyl)-rac-glycerol) is a monoacylglycerol |
| reagent | reagents/lipids/nbd-pe/ | NBD-Phosphatidylethanolamine (NBD-PE) | NBD-phosphatidylethanolamine (NBD-PE) is a fluorescent lipid probe consisting of |
| reagent | reagents/lipids/nbd-ps/ | NBD-Phosphatidylserine (NBD-PS) | NBD-phosphatidylserine (NBD-PS) is a fluorescent lipid probe consisting of a pho |
| reagent | reagents/lipids/oleic-acid/ | Oleic Acid | Oleic acid is a monounsaturated omega-9 fatty acid (cis-9-octadecenoic acid, C18 |
| reagent | reagents/lipids/phosphatidic-acid/ | Phosphatidic Acid | Phosphatidic acid (PA) is the simplest phospholipid, consisting of a diacylglyce |
| reagent | reagents/lipids/phosphatidylcholine/ | Phosphatidylcholine | Phosphatidylcholine (PC) is a major class of phospholipids found in cell membran |
| reagent | reagents/lipids/phosphatidylethanolamine/ | Phosphatidylethanolamine | Phosphatidylethanolamine (PE) is a glycerophospholipid consisting of a diglyceri |
| reagent | reagents/lipids/phosphatidylglycerol-phosphate/ | Phosphatidylglycerol Phosphate | Phosphatidylglycerol phosphate (PGP) is a glycerophospholipid intermediate in th |
| reagent | reagents/lipids/phosphatidylglycerol/ | Phosphatidylglycerol | Phosphatidylglycerol (PG) is a glycerophospholipid consisting of a diglyceride b |
| reagent | reagents/lipids/phosphatidylinositol-4-5-bisphosphate/ | Phosphatidylinositol-4,5-Bisphosphate (PIP2) | Phosphatidylinositol-4,5-bisphosphate (PIP2, also known as PtdIns(4,5)P2) is an  |
| reagent | reagents/lipids/phosphatidylinositol/ | Phosphatidylinositol | Phosphatidylinositol (PI) is an acidic phospholipid consisting of a diacylglycer |
| reagent | reagents/lipids/phosphatidylserine/ | Phosphatidylserine | L-alpha-phosphatidylserine is a negatively charged phospholipid used as a crysta |
| reagent | reagents/lipids/popc/ | 1-Palmitoyl-2-Oleoyl-sn-Glycero-3-Phosphocholine (POPC) | 1-Palmitoyl-2-oleoyl-sn-glycero-3-phosphocholine (POPC) is a major phospholipid  |
| reagent | reagents/lipids/pope/ | Palmitoyl-Oleoyl-Phosphatidylethanolamine (POPE) | Palmitoyl-oleoyl-phosphatidylethanolamine (POPE) is a diacyl phospholipid with a |
| reagent | reagents/lipids/popg/ | 1-Palmitoyl-2-Oleoylphosphatidylglycerol (POPG) | 1-Palmitoyl-2-oleoylphosphatidylglycerol (POPG) is a diacyl phospholipid with a  |
| reagent | reagents/lipids/sphingosine/ | Sphingosine | Sphingosine (D-erythro-sphingosine, d18:1) is a sphingoid base that serves as th |
| reagent | reagents/lipids/stigmasterol/ | Stigmasterol | Stigmasterol is a plant sterol (phytosterol) and a dietary component found in ve |
| reagent | reagents/lipids/sulfoquinovosyl-diacylglycerol/ | Sulfoquinovosyl Diacylglycerol (SQDG) | Sulfoquinovosyl diacylglycerol (SQDG) is an anionic galactolipid found in thylak |
| reagent | reagents/protein-tags/bril/ | BRIL Fusion Protein | BRIL (thermostabilized apocytochrome b562 RIL) is a fusion partner protein used  |
| reagent | reagents/protein-tags/flag-tag/ | FLAG Tag | The FLAG tag is a short peptide epitope tag (DYKDDDDK) commonly used for affinit |
| reagent | reagents/protein-tags/his6-tag/ | Polyhistidine Tag (His6) | The polyhistidine tag (His6) is a short peptide sequence of six consecutive hist |
| reagent | reagents/protein-tags/monobody-l2/ | Monobody L2 | Monobody L2 is an engineered protein inhibitor selected from a combinatorial lib |
| reagent | reagents/protein-tags/monobody-l3/ | Monobody L3 | Monobody L3 is an engineered fibronectin type III domain (FN3) protein selected  |
| reagent | reagents/protein-tags/monobody-mb15/ | MB-15 Monobody | MB-15 is a synthetic ICMT-binding monobody engineered as a crystallization chape |
| reagent | reagents/protein-tags/monobody-s7/ | Monobody S7 | Monobody S7 is an engineered protein inhibitor selected from a combinatorial lib |
| reagent | reagents/protein-tags/monobody-s8/ | Monobody S8 | Monobody S8 is an engineered fibronectin type III domain (FN3) protein selected  |
| reagent | reagents/protein-tags/monobody-s9/ | Monobody S9 | Monobody S9 is an engineered protein inhibitor selected from a combinatorial lib |
| reagent | reagents/protein-tags/nanobody/ | Nanobody | A nanobody is a single-domain antibody fragment derived from camelid heavy-chain |
| reagent | reagents/protein-tags/rubredoxin/ | Rubredoxin Fusion Protein | Rubredoxin is a small iron-sulfur protein used as a fusion partner to replace th |
| reagent | reagents/protein-tags/sumo-tag/ | SUMO Tag (Small Ubiquitin-like Modifier) | SUMO (Small Ubiquitin-like Modifier) is a 11 kDa protein tag used to enhance sol |
| reagent | reagents/protein-tags/t4-lysozyme/ | T4 Lysozyme (T4L) | T4 lysozyme (T4L) is a fusion partner protein used to replace flexible intracell |
| reagent | reagents/protein-tags/tevp-protease/ | TEV Protease (Tobacco Etch Virus Protease) | TEV protease (tobacco etch virus protease) is a highly specific cysteine proteas |
| reagent | reagents/protein-tags/thrombin-protease/ | Thrombin Protease | Thrombin is a serine protease that specifically cleaves at the sequence Leu-Val- |
| reagent | reagents/substrates/d-xylose/ | D-Xylose | D-Xylose is an aldopentose (five-carbon sugar) that serves as the natural substr |
| reagent | reagents/substrates/gdp-fucose/ | GDP-Fucose | GDP-fucose (guanosine 5'-diphosphate-L-fucose) is an activated sugar donor used  |
| reagent | reagents/substrates/gdp-mannose/ | GDP-Mannose | GDP-mannose (guanosine 5'-diphosphate-alpha-D-mannose) is an activated sugar don |
| reagent | reagents/substrates/l-alanine/ | L-Alanine | L-Alanine is a small neutral amino acid that binds to the AvGluR1 ligand-binding |
| reagent | reagents/substrates/l-arginine/ | L-Arginine | L-arginine is a basic, semi-essential amino acid that serves as the primary subs |
| reagent | reagents/substrates/l-aspartate/ | L-Aspartate | L-Aspartate is an acidic amino acid and a canonical agonist for ionotropic gluta |
| reagent | reagents/substrates/l-glutamate/ | L-Glutamate | L-Glutamate is the primary endogenous excitatory neurotransmitter and the canoni |
| reagent | reagents/substrates/l-serine/ | L-Serine | L-Serine is a polar neutral amino acid that binds to the AvGluR1 ligand-binding  |
| reagent | reagents/substrates/silicic-acid/ | Silicic Acid | Silicic acid (H4SiO4) is the bioavailable form of silicon in biological systems. |
| reagent | reagents/substrates/udp-glucose/ | UDP-Glucose (UDP-Glc) | UDP-glucose (UDP-Glc) is a nucleotide sugar that serves as the activated glucose |
| reagent | reagents/substrates/urea/ | Urea | Urea (CH4N2O) is a small polar molecule with a strong dipole moment (4.6 D) that |
END WIKI CATALOG -->
