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

- [Wiki Reference](/xray-mp-wiki/WIKI-REFERENCE.md) — Domain, conventions, directory structure, entity page structures, tag taxonomy, correction policy, source-truth verification
- [Wiki Workflow](/xray-mp-wiki/WIKI-WORKFLOW.md) — Complete per-entity workflows: YAML schemas, generate/update commands, merge rules, pitfalls
- [Wiki Scripts](/xray-mp-wiki/WIKI-SCRIPTS.md) — Script inventory, usage, architecture, testing

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

<!-- WIKI CATALOG -->
| type | path | title | summary |
|------|------|-------|---------|
| concept | concepts/aquaporin/ | Aquaporin Family | Aquaporins (AQPs) are integral membrane channel proteins that mediate bidirectio |
| concept | concepts/channelrhodopsin-photocycle/ | Channelrhodopsin Photocycle | The channelrhodopsin photocycle is a sequence of light-induced conformational an |
| concept | concepts/cora-mg-transporter/ | CorA Mg2+ Transporter | CorA is a magnesium transporter found in most prokaryotes and some eukaryotes, r |
| concept | concepts/domain-swapping/ | Three-Dimensional Domain Swapping | Three-dimensional domain swapping is a mechanism by which identical protein mono |
| concept | concepts/er-retrieval-mechanism/ | ER Retrieval Mechanism (KDEL System) | The ER retrieval system maintains the luminal composition of the endoplasmic ret |
| concept | concepts/intramembrane-proteolysis/ | Intramembrane Proteolysis | Intramembrane proteases are specialized membrane proteins that cleave transmembr |
| concept | concepts/membrane-mimetics/ | Membrane Mimetics and Structural Biology Concepts | Membrane proteins require specialized techniques for structural determination du |
| concept | concepts/peripheral-stalk-elasticity/ | Peripheral Stalk Elasticity in A-ATP Synthases | The peripheral stalk elasticity model proposes that the peripheral stalks of A-A |
| concept | concepts/rhomboid-protease/ | Rhomboid Protease Family | The rhomboid family comprises intramembrane serine proteases found across all ki |
| concept | concepts/rotary-atpase-mechanism/ | Rotary ATPase Mechanism and Asymmetry | The rotary ATPase mechanism involves conversion between chemical energy of ATP a |
| concept | concepts/ser-lys-catalytic-mechanism/ | Ser/Lys Catalytic Mechanism in SppA | The Ser/Lys catalytic mechanism is a proteolytic mechanism used by signal peptid |
| concept | concepts/si-face-cleavage/ | si-Face Cleavage in Rhomboid Proteases | Rhomboid intramembrane proteases cleave transmembrane substrates on the si-face  |
| concept | concepts/sodium-channel-gating/ | Sodium Channel Gating and Ion Selectivity | Voltage-gated sodium channels (NaV) belong to the voltage-gated ion channel (VGI |
| concept | concepts/x-ray-radiation-damage/ | X-Ray Radiation Damage in Protein Crystallography | X-ray radiation damage is a fundamental limitation in macromolecular crystallogr |
| method | methods/crystallization/lipidic-cubic-phase/ | Lipidic Cubic Phase Crystallization | Lipidic cubic phase (LCP) crystallization, also known as the in meso method, is  |
| method | methods/expression-systems/cell-free-protein-synthesis/ | Cell-Free Protein Synthesis for Membrane Proteins | Cell-free protein synthesis systems can be supplemented with both lipid and dete |
| method | methods/purification/affinity-chromatography/ | Affinity Chromatography | Affinity chromatography is a purification method that separates proteins based o |
| method | methods/purification/limited-proteolysis/ | Limited Proteolysis | Limited proteolysis is a technique where a protease is used to selectively cleav |
| method | methods/purification/size-exclusion-chromatography/ | Size-Exclusion Chromatography | Size-exclusion chromatography (SEC), also known as gel filtration, separates mol |
| method | methods/time-resolved-serial-femtosecond-crystallography/ | Time-Resolved Serial Femtosecond Crystallography (TR-SFX) | Time-resolved serial femtosecond crystallography (TR-SFX) is an X-ray crystallog |
| protein | proteins/a2a-psb1-bril/ | A2A-PSB1-bRIL Adenosine A2A Receptor | The adenosine A2A receptor (A2AAR) is a class A GPCR and important drug target f |
| protein | proteins/acetabularia-rhodopsin-ii/ | Acetabularia Rhodopsin II (ARII) | Acetabularia rhodopsin II (ARII) is a light-driven proton pump from the marine a |
| protein | proteins/acrB/ | AcrB Efflux Pump | AcrB (Acriflavine resistance protein B) is the inner membrane component of the A |
| protein | proteins/aquaporin-z/ | Aquaporin Z (AqpZ) - Escherichia coli | X-ray crystal structures of Escherichia coli Aquaporin Z (AqpZ) mutants in compl |
| protein | proteins/archaerhodopsin-2/ | Archaerhodopsin-2 (aR2) - Halorubrum sp. aus-2 | Crystal structures of Archaerhodopsin-2 (aR2), a light-driven proton pump from H |
| protein | proteins/bacteriorhodopsin/ | Bacteriorhodopsin (Ground State) | Bacteriorhodopsin (bR) is a light-driven proton pump from the halophilic archaeo |
| protein | proteins/bovine-adp-atp-carrier/ | Bovine ADP/ATP Carrier | The bovine mitochondrial ADP/ATP carrier (AAC) is the most abundant protein in t |
| protein | proteins/bovine-rhodopsin/ | Bovine Rhodopsin (Dark State) | Bovine rhodopsin is the photoreceptor GPCR in vertebrate retinal rod cells, resp |
| protein | proteins/channelrhodopsin-c1c2/ | Channelrhodopsin C1C2 (ChR1/ChR2 Chimera) | Channelrhodopsin C1C2 is a chimeric construct between Chlamydomonas reinhardtii  |
| protein | proteins/ecglpg-cyto/ | Cytoplasmic Domain of Escherichia coli Rhomboid Protease GlpG (ecGlpG-cyto) | The cytoplasmic domain of Escherichia coli rhomboid protease GlpG (ecGlpG-cyto)  |
| protein | proteins/glpg/ | GlpG Rhomboid Intramembrane Protease (E. coli) | The crystal structure of Escherichia coli GlpG, a rhomboid family serine intrame |
| protein | proteins/hiGlpG/ | hiGlpG (Haemophilus influenzae Rhomboid Protease) | hiGlpG is the rhomboid intramembrane protease from Haemophilus influenzae, a 7-T |
| protein | proteins/kdel-receptor/ | KDEL Receptor (Chicken/Human) | The KDEL receptor is a seven-transmembrane protein that retrieves escaped ER lum |
| protein | proteins/kirbac-potassium-channels/ | KirBac Potassium Channels | KirBac1.1 and KirBac3.1 are prokaryotic inward-rectifier potassium channels from |
| protein | proteins/mexB/ | MexB Multidrug Exporter from Pseudomonas aeruginosa | MexB is the inner-membrane component of the MexAB-OprM tripartite efflux pump in |
| protein | proteins/navae1p-sodium-channel/ | NavAe1p Prokaryotic Sodium Channel Pore | NavAe1p is a pore-only construct of the prokaryotic voltage-gated sodium channel |
| protein | proteins/ntmate2/ | NtMATE2 Nicotine Transporter | NtMATE2 is a multidrug and toxic compound extrusion (MATE) family transporter fr |
| protein | proteins/opsin/ | Opsin (Retinal-Free Rhodopsin) | Opsin is the apoprotein form of rhodopsin, the G-protein-coupled receptor (GPCR) |
| protein | proteins/ph-e-subunit-e/ | Subunit E of Pyrococcus horikoshii OT3 A-ATP Synthase (PhE) | Subunit E from Pyrococcus horikoshii OT3 A-ATP synthase (PhE) is a component of  |
| protein | proteins/porb-corynebacterium-glutamicum/ | Porin B (PorB) from Corynebacterium glutamicum | Porin B (PorB) is an alpha-helical porin from Corynebacterium glutamicum, a myco |
| protein | proteins/psi-lhci-chlamydomonas/ | PSI-LHCI from Chlamydomonas reinhardtii | The photosystem I-light harvesting complex I (PSI-LHCI) supercomplex from the gr |
| protein | proteins/rhodobacter-sphaeroides-reaction-centre-zn-bchl/ | Rhodobacter sphaeroides Reaction Centre with Zn-Bacteriochlorophyll | The photosynthetic reaction centre (RC) from the purple bacterium Rhodobacter sp |
| protein | proteins/rhodopsin-2-2a/ | Rhodopsin (2.2 A Resolution, 1U19) | High-resolution 2.2 A crystal structure of bovine rhodopsin in the dark state (P |
| protein | proteins/rhodopsin-n2c-d282c-mutant/ | Rhodopsin N2C/D282C Mutant | The N2C/D282C mutant of bovine rhodopsin is a thermally stabilized recombinant f |
| protein | proteins/rps-viridis-reaction-centre/ | Rps. viridis Photosynthetic Reaction Centre | The photosynthetic reaction centre from the purple bacterium Rhodopseudomonas vi |
| protein | proteins/sppa-bs/ | Signal Peptide Peptidase A from Bacillus subtilis (SppA_BS) | Signal Peptide Peptidase A from Bacillus subtilis (SppA_BS) is a membrane-bound  |
| protein | proteins/sppa-ec/ | Signal Peptide Peptidase A from Escherichia coli (SppA_EC) | Signal Peptide Peptidase A from Escherichia coli (SppA_EC) is a membrane-bound s |
| protein | proteins/squid-rhodopsin/ | Squid Rhodopsin (Photoreaction States) | Squid rhodopsin from Todarodes pacificus is an invertebrate visual pigment that  |
| protein | proteins/tlg2/ | Tlg2 Qa-SNARE (C. thermophilum) | Tlg2 is a Qa-SNARE protein from the filamentous fungus Cryptococcus thermophilum |
| protein | proteins/v1-atpase-t-thermophilus/ | V1-ATPase from Thermus thermophilus | The V1-ATPase from Thermus thermophilus is the extrinsic membrane domain of the  |
| protein | proteins/vp-zntb/ | Vp-ZntB Cytoplasmic Domain | ZntB is a zinc/cadmium efflux transporter from the metal ion transporter (MIT) s |
| protein | proteins/vps45/ | Vps45 SM Protein (C. thermophilum) | Vps45 is a Sec1/Munc18-family (SM) protein from the filamentous fungus Cryptococ |
| reagent | reagents/additives/ammonium-sulfate/ | Ammonium Sulfate | Ammonium sulfate is a common precipitant used in protein crystallization and pur |
| reagent | reagents/additives/bodipy/ | BODIPY Fluorophore | BODIPY (boron-dipyromethene) is a fluorescent dye used for labeling molecules fo |
| reagent | reagents/additives/jeffamine-m600/ | Jeffamine M600 | Jeffamine M600 is a branched polyamine copolymer used as a crystallization preci |
| reagent | reagents/additives/lithium-sulfate/ | Lithium Sulfate | Lithium sulfate (Li2SO4) is an inorganic salt used as a crystallization precipit |
| reagent | reagents/additives/mpd/ | 2-Methyl-2,4-pentanediol (MPD) | 2-Methyl-2,4-pentanediol (MPD) is a low-viscosity organic compound commonly used |
| reagent | reagents/additives/peg/ | PEG (Polyethylene Glycol) | Polyethylene glycol (PEG) is a water-soluble polymer used as a linker in conjuga |
| reagent | reagents/buffers/acetate/ | Acetate Buffer (Sodium Acetate) | Acetate buffer, typically prepared from sodium acetate and acetic acid, is a com |
| reagent | reagents/buffers/ammonium-acetate/ | Ammonium Acetate | Ammonium acetate is a volatile salt commonly used in protein crystallization as  |
| reagent | reagents/buffers/bicine/ | Bicine Buffer | Bicine (N,N-bis(2-hydroxyethyl)glycine) is a zwitterionic Good's buffer commonly |
| reagent | reagents/buffers/cacodylate/ | Cacodylate (Sodium Dimethylarsenate) | Cacodylate (sodium dimethylarsenate) is a buffering agent used in protein crysta |
| reagent | reagents/buffers/citrate/ | Citrate Buffer (Sodium Citrate) | Citrate buffer, prepared from citric acid and sodium citrate, is a buffer system |
| reagent | reagents/buffers/glycine/ | Glycine Buffer | Glycine is a simple amino acid that can be used as a buffer in the alkaline pH r |
| reagent | reagents/buffers/hepes/ | HEPES (4-(2-Hydroxyethyl)-1-piperazineethanesulfonic Acid) | HEPES (4-(2-hydroxyethyl)-1-piperazineethanesulfonic acid) is a zwitterionic Goo |
| reagent | reagents/buffers/mops/ | MOPS (3-(N-Morpholino)propanesulfonic Acid) | MOPS (3-(N-morpholino)propanesulfonic acid) is a zwitterionic Good's buffer wide |
| reagent | reagents/buffers/pipes/ | PIPES (Piperazine-1,4-bis(2-ethanesulfonic acid)) | PIPES (piperazine-1,4-bis(2-ethanesulfonic acid)) is a zwitterionic Good's buffe |
| reagent | reagents/buffers/sodium-phosphate/ | Sodium Phosphate Buffer | Sodium phosphate buffer is one of the most widely used buffer systems in protein |
| reagent | reagents/buffers/tes/ | TES Buffer (N-Tris(hydroxymethyl)methyl-2-aminoethanesulfonic acid) | TES (N-tris(hydroxymethyl)methyl-2-aminoethanesulfonic acid) is a zwitterionic G |
| reagent | reagents/buffers/tris/ | Tris (Tris-HCl Buffer) | Tris (tris(hydroxymethyl)aminomethane) is a widely used buffering agent in membr |
| reagent | reagents/c8e4/ | Octyltetraoxyethylene (C8E4) | Octyltetraoxyethylene (C8E4, n-octyltetraoxyethylene) is a nonionic detergent wi |
| reagent | reagents/detergents/anzergent-3-12/ | Anzergent 3,12 | Anzergent 3,12 is a mild zwitterionic detergent used for solubilizing membrane p |
| reagent | reagents/detergents/beta-ddm/ | n-Dodecyl-beta-D-maltopyranoside (beta-DDM) | n-Dodecyl-beta-D-maltopyranoside (beta-DDM) is a mild nonionic detergent with a  |
| reagent | reagents/detergents/c8e4/ | Octyltetraoxyethylene (C8E4) | Octyltetraoxyethylene (C8E4, n-octyltetraoxyethylene) is a nonionic detergent wi |
| reagent | reagents/detergents/cholesterol-hydrogen-succinate/ | Cholesterol Hydrogen Succinate (CHS) | Cholesterol hydrogen succinate (CHS) is a cholesterol derivative with a succinat |
| reagent | reagents/detergents/ddm/ | n-Dodecyl-beta-D-maltopyranoside (DDM) | n-Dodecyl-beta-D-maltopyranoside (DDM) is a mild nonionic detergent with a 12-ca |
| reagent | reagents/detergents/glyco-diosgenin/ | Glyco-diosgenin (GDN) | Glyco-diosgenin (GDN) is a mild nonionic detergent derived from diosgenin, a ste |
| reagent | reagents/detergents/heptylthioglucoside/ | Heptylthioglucoside (HpG) | Heptylthioglucoside (HpG) is a mild nonionic detergent with a 7-carbon alkyl cha |
| reagent | reagents/detergents/lDAO/ | Lauryldimethylamine N-oxide (LDAO) | Lauryldimethylamine N-oxide (LDAO) is a zwitterionic detergent with a 12-carbon  |
| reagent | reagents/detergents/lapao/ | LAPAO | LAPAO (3-laurylamido-N,N'-dimethylpropylaminoxyde) is a zwitterionic detergent u |
| reagent | reagents/detergents/lmng/ | Lauryl Maltose Neopentyl Glycol (LMNG) | Lauryl maltose neopentyl glycol (LMNG) is a mild nonionic detergent with a 12-ca |
| reagent | reagents/detergents/og/ | n-Octyl beta-D-glucopyranoside (OG) | n-Octyl beta-D-glucopyranoside (OG) is a mild nonionic detergent with an 8-carbo |
| reagent | reagents/detergents/triton-x-100/ | Triton X-100 | Triton X-100 is a nonionic octylphenyl polyethoxylate detergent used for solubil |
| reagent | reagents/ligands/11-cis-retinal/ | 11-cis-Retinal | 11-cis-retinal is the light-sensitive chromophore covalently bound to the apopro |
| reagent | reagents/ligands/bacteriochlorophyll/ | Bacteriochlorophyll | Bacteriochlorophyll (BChl) is a magnesium-coordinated chlorin pigment found in a |
| reagent | reagents/ligands/bacteriopheophytin/ | Bacteriopheophytin | Bacteriopheophytin (BPhe) is a chlorin pigment found in photosynthetic reaction  |
| reagent | reagents/ligands/linezolid/ | Linezolid | Linezolid ((S)-N-{3-[3-fluoro-4-(morpholin-4-yl)phenyl]-2-oxo-1,3-oxazolidin-5-y |
| reagent | reagents/ligands/msx-2/ | MSX-2 | MSX-2 is a xanthine-based radioligand used for binding assays at adenosine recep |
| reagent | reagents/ligands/neca/ | NECA | NECA (5'-N-ethylcarboxamidoadenosine) is a non-selective adenosine receptor agon |
| reagent | reagents/ligands/preladenant/ | Preladenant | Preladenant (SCH-420814) is a potent, highly selective non-xanthine antagonist o |
| reagent | reagents/ligands/zm241385/ | ZM241385 | ZM241385 is a bicyclic xanthine-based antagonist of the adenosine A2A receptor ( |
| reagent | reagents/lipids/bacterioruberin/ | Bacterioruberin | Bacterioruberin is a C50 carotenoid pigment found in halophilic archaea, particu |
| reagent | reagents/lipids/cardiolipin/ | Cardiolipin | Cardiolipin is a double-phospholipid found predominantly in the inner mitochondr |
| reagent | reagents/lipids/monoolein/ | Monoolein | Monoolein (1-monoolein) is a monoglyceride consisting of a single oleic acid (ci |
| reagent | reagents/mercury/ | Mercury (HgCl2) - Aquaporin Inhibitor | Mercury(II) chloride (HgCl2) is a mercurial compound historically used to define |
| reagent | reagents/nicotine/ | Nicotine | Nicotine is a naturally occurring alkaloid produced in Nicotiana species as a na |
| reagent | reagents/protein-tags/bril/ | BRIL Fusion Protein | BRIL (thermostabilized apocytochrome b562 RIL) is a fusion partner protein used  |
| reagent | reagents/protein-tags/sumo-tag/ | SUMO Tag (Small Ubiquitin-like Modifier) | SUMO (Small Ubiquitin-like Modifier) is a 11 kDa protein tag used to enhance sol |
| reagent | reagents/protein-tags/tevp-protease/ | TEV Protease (Tobacco Etch Virus Protease) | TEV protease (tobacco etch virus protease) is a highly specific cysteine proteas |
| reagent | reagents/thermolysin/ | Thermolysin | Thermolysin is a thermostable neutral metalloprotease produced by Bacillus therm |
<!-- END WIKI CATALOG -->
