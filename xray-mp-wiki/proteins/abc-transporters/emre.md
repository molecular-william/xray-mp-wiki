---
title: "EmrE (E. coli Small Multidrug Resistance Transporter)"
created: 2026-06-08
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1073##pnas.0709387104, doi/10.7554##eLife.76766]
verified: agent
uniprot_id: P23895
---

# EmrE (E. coli Small Multidrug Resistance Transporter)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P23895">UniProt: P23895</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

EmrE is a small multidrug resistance (SMR) family proton-coupled multidrug efflux transporter from Escherichia coli. It functions as a dual-topology antiporter that exports a broad spectrum of structurally diverse antiseptics and antimicrobials, including polyaromatic cations, quaternary ammonium compounds, and quaternary phosphoniums. The first X-ray crystal structure, published in 2007 (Chen et al., PNAS), established that EmrE forms an antiparallel homodimer with the 'dual topology' model, where the two monomers adopt opposite orientations in the membrane. Selenomethionine markers clearly demonstrated the antiparallel arrangement, with the first three transmembrane helices from each monomer surrounding the substrate binding chamber while the fourth helices mediate dimer formation. Higher-resolution crystal structures were later solved using a multipurpose monobody crystallization chaperone (L10), revealing six structures at 2.9-3.9 A resolution: a low-pH proton-bound state (PDB 7MH6, 2.9 A) and five complexes with diverse substrates including methyl viologen, harmane, methyltriphenylphosphonium, tetraphenylphosphonium, and benzyltrimethylammonium. These structures reveal that binding site tryptophan and glutamate residues adopt different rotamers to accommodate diverse substrates without major backbone rearrangements.

## Publications

### doi/10.1073##pnas.0709387104

**Structures:**

<table class="wiki-table">
  <thead><tr>
    <th>PDB ID</th>
    <th>Resolution</th>
    <th>Space Group</th>
    <th>Construct</th>
    <th>Ligand/Co-factor</th>
  </tr></thead>
  <tbody>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3b5d">3B5D</a></td>
      <td>3.8</td>
      <td>C2</td>
      <td>EmrE in complex with tetraphenylphosphonium (TPP+), C2 crystal form. Selenomethionine-labeled protein for experimental phasing.</td>
      <td>Tetraphenylphosphonium (TPP+)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3b61">3B61</a></td>
      <td>4.5</td>
      <td>C2</td>
      <td>EmrE apo structure, C2 crystal form.</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3b62">3B62</a></td>
      <td>4.4</td>
      <td>P21</td>
      <td>EmrE in complex with tetraphenylphosphonium (TPP+), P21 crystal form.</td>
      <td>Tetraphenylphosphonium (TPP+)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41 (DE3)
- **Construct**: EmrE3 (E25N, W31I, V34M) with N-terminal hexahistidine tag and thrombin cut site in pET15b

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3b5d">3B5D</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">MNPYI</span><span class="topo-membrane">YLGGAILAEVIGTT</span><span class="topo-outside">LMKFSEGFTRLWPSVG</span><span class="topo-membrane">TIICYCASFWLLAQ</span><span class="topo-inside">TLAYIPTGI</span><span class="topo-membrane">AYAIWSGVGIVLISLL</span><span class="topo-outside">SWGFFGQRLDLPA</span><span class="topo-membrane">IIGMMLICAGVLIINL</span><span class="topo-inside">LS</span><span class="topo-unknown">RSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>6</td>
      <td>19</td>
      <td>6</td>
      <td>19</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>20</td>
      <td>35</td>
      <td>20</td>
      <td>35</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>36</td>
      <td>49</td>
      <td>36</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>58</td>
      <td>50</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>74</td>
      <td>59</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>87</td>
      <td>75</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>103</td>
      <td>88</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>105</td>
      <td>104</td>
      <td>105</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>106</td>
      <td>110</td>
      <td>106</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3b61">3B61</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">MNP</span><span class="topo-inside">YIY</span><span class="topo-membrane">LGGAILAEVIGTTL</span><span class="topo-outside">MKFSEGFTRLWPSVGTI</span><span class="topo-membrane">ICYCASFWLLAQTL</span><span class="topo-inside">AY</span><span class="topo-membrane">IPTGIAYAIWSGV</span><span class="topo-outside">GIVLISLLSWGFFGQRLDLPAIIGMMLICAGVLIINLLSRSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (8 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>4</td>
      <td>6</td>
      <td>4</td>
      <td>6</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>20</td>
      <td>7</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>21</td>
      <td>37</td>
      <td>21</td>
      <td>37</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>38</td>
      <td>51</td>
      <td>38</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>53</td>
      <td>52</td>
      <td>53</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>54</td>
      <td>66</td>
      <td>54</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>67</td>
      <td>110</td>
      <td>67</td>
      <td>110</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3b62">3B62</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">MNPYIY</span><span class="topo-outside">L</span><span class="topo-membrane">GGAILAEVIGTTLM</span><span class="topo-inside">KFSEGFTRLW</span><span class="topo-membrane">PSVGTIICYCASFWLLA</span><span class="topo-outside">QTLAYIP</span><span class="topo-membrane">TGIAYAIWSGVGIVLI</span><span class="topo-inside">SLLSWGFFGQRLDLPAIIGMMLICAGVLII</span><span class="topo-unknown">NLLSRSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>21</td>
      <td>8</td>
      <td>21</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>22</td>
      <td>31</td>
      <td>22</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>48</td>
      <td>32</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>55</td>
      <td>49</td>
      <td>55</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>71</td>
      <td>56</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>101</td>
      <td>72</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>110</td>
      <td>102</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3b62">3B62</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">MNPYIY</span><span class="topo-inside">LGGAILA</span><span class="topo-membrane">EVIGTTLMKFSE</span><span class="topo-outside">GF</span><span class="topo-membrane">TRLWPSVGTIICYCASFW</span><span class="topo-inside">LLAQTLAYIPTGIAYAIW</span><span class="topo-membrane">SGVGIVLISLLSWGF</span><span class="topo-outside">F</span><span class="topo-membrane">GQRLDLPAIIGMM</span><span class="topo-inside">L</span><span class="topo-unknown">ICAGVLIINLLSRSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>13</td>
      <td>7</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>25</td>
      <td>14</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>27</td>
      <td>26</td>
      <td>27</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>28</td>
      <td>45</td>
      <td>28</td>
      <td>45</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>46</td>
      <td>63</td>
      <td>46</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>78</td>
      <td>64</td>
      <td>78</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>79</td>
      <td>79</td>
      <td>79</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>92</td>
      <td>80</td>
      <td>92</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>93</td>
      <td>93</td>
      <td>93</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>110</td>
      <td>94</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3b62">3B62</a> — Chain C (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">MNPYIY</span><span class="topo-outside">L</span><span class="topo-membrane">GGAILAEVIGTTLMKF</span><span class="topo-inside">SEGFTRLWPS</span><span class="topo-membrane">VGTIICYCASFWLL</span><span class="topo-outside">AQTLAYIPTGIAYAIW</span><span class="topo-membrane">SGVGIVLISLLSWG</span><span class="topo-inside">FFGQRLD</span><span class="topo-membrane">LPAIIGMMLICAGVL</span><span class="topo-outside">II</span><span class="topo-unknown">NLLSRSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>23</td>
      <td>8</td>
      <td>23</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>24</td>
      <td>33</td>
      <td>24</td>
      <td>33</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>47</td>
      <td>34</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>63</td>
      <td>48</td>
      <td>63</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>77</td>
      <td>64</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>84</td>
      <td>78</td>
      <td>84</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>85</td>
      <td>99</td>
      <td>85</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>101</td>
      <td>100</td>
      <td>101</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>102</td>
      <td>110</td>
      <td>102</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3b62">3B62</a> — Chain D (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">MNPYIY</span><span class="topo-inside">L</span><span class="topo-membrane">GGAILAEVIGTTLM</span><span class="topo-outside">KFSEGFTRLW</span><span class="topo-membrane">PSVGTIICYCASFWLLAQTL</span><span class="topo-inside">AYIP</span><span class="topo-membrane">TGIAYAIWSGVGIVL</span><span class="topo-outside">ISLLSWGFFGQRLDLPAIIGMML</span><span class="topo-unknown">ICAGVLIINLLSRSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>6</td>
      <td>1</td>
      <td>6</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>21</td>
      <td>8</td>
      <td>21</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>22</td>
      <td>31</td>
      <td>22</td>
      <td>31</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>51</td>
      <td>32</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>55</td>
      <td>52</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>70</td>
      <td>56</td>
      <td>70</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>71</td>
      <td>93</td>
      <td>71</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>110</td>
      <td>94</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.7554##eLife.76766

**Structures:**

<table class="wiki-table">
  <thead><tr>
    <th>PDB ID</th>
    <th>Resolution</th>
    <th>Space Group</th>
    <th>Construct</th>
    <th>Ligand/Co-factor</th>
  </tr></thead>
  <tbody>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7mh6">7MH6</a></td>
      <td>2.9</td>
      <td>C121</td>
      <td>EmrE3 mutant (E25N, W31I, V34M) with L10 monobody, low pH (proton-bound) state</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7mgx">7MGX</a></td>
      <td>3.1</td>
      <td>P1</td>
      <td>EmrE3/L10 in complex with methyl viologen</td>
      <td>Methyl viologen</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7svx">7SVX</a></td>
      <td>3.8</td>
      <td>C121</td>
      <td>EmrE3/L10 in complex with harmane</td>
      <td>Harmane</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7ssu">7SSU</a></td>
      <td>3.2</td>
      <td>C121</td>
      <td>EmrE3/L10 in complex with methyltriphenylphosphonium (MeTPP+)</td>
      <td>Methyltriphenylphosphonium</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7sv9">7SV9</a></td>
      <td>3.4</td>
      <td>C121</td>
      <td>EmrE3/L10 in complex with tetraphenylphosphonium (TPP+)</td>
      <td>Tetraphenylphosphonium</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7t00">7T00</a></td>
      <td>3.9</td>
      <td>C121</td>
      <td>EmrE3/L10 in complex with benzyltrimethylammonium</td>
      <td>Benzyltrimethylammonium</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41 (DE3)
- **Construct**: EmrE3 (E25N, W31I, V34M) with N-terminal hexahistidine tag and thrombin cut site in pET15b

**Purification:**

<table class="wiki-table">
  <thead><tr>
    <th>Step</th>
    <th>Method</th>
    <th>Resin / Column</th>
    <th>Buffer + Detergent</th>
    <th>Notes</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>Cell growth and lysis</td>
      <td>Cells grown in Studier's autoinduction medium at 37 C overnight (15-18 hr). Pellets resuspended in breaking buffer (50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-Cl</a> pH 8.0, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM TCEP) with DNase, MgCl2, PMSF, lysozyme, pepstatin, leupeptin. Lysed by sonication.</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-Cl</a> pH 8.0, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM TCEP + --</td>
      <td>Lysate extracted with 2% n-Decyl-beta-D-Maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a>) for 2 hr at room temperature</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Clarified lysate loaded onto <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> cobalt resin, washed with wash buffer + 10 mM imidazole, eluted with 400 mM imidazole</td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> cobalt resin (Clontech)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-Cl</a> pH 8.0, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> + 5 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>Eluted with wash buffer supplemented with 400 mM imidazole</td>
    </tr>
    <tr>
      <td>Thrombin cleavage and SEC</td>
      <td>Buffer exchanged into wash buffer using PD-10 desalting columns. His tags cleaved with thrombin (1 U/mg EmrE3) overnight at 21 C. Final <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/) using <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> column.</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> (GE Healthcare)</td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> pH 7.5, 100 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 4 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> + 4 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> performed for final polishing step</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-drop vapor diffusion</a> with monobody L10 chaperone</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>EmrE3 (10 mg/mL) + L10 monobody (10 mg/mL) at 2.1:1 molar ratio, supplemented with 6.6 mM LDAO</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 0.1 M sodium cacodylate pH 5.2, 34% <a href="/xray-mp-wiki/reagents/additives/peg-600/">PEG 600</a> (low pH, no substrate)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>~4 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Flash frozen in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals formed in 96-well plates. Space group C121 (apo, TPP+, MeTPP+, harmane, benzyltrimethylammonium) or P1 (methyl viologen). Substrate-bound crystals grown in 0.1 M LiNO3 or 0.1 M (NH4)2SO4, 0.1 M ADA pH 6.5 or 0.1 M HEPES pH 7.1-7.3, 30-35% PEG 600 with substrates added from stock solutions (1 mM methyl viologen, 500 uM harmane, 300 uM benzyltrimethylammonium, 100 uM TPP+, 300 uM MeTPP+). Structures solved by molecular replacement using L10 monobody and Gdx-Clo helices as search models.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method (structured)</td>
      <td>vapor-diffusion</td>
    </tr>
    <tr>
      <td>Variant</td>
      <td>hanging-drop</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>5.2</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Sodium Chloride: 0.2 M [salt]  
- Sodium Cacodylate: 0.1 M [buffer]  
- Peg 600: 34 % [precipitant] (PEG 600 (low pH, no substrate))</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mh6">7MH6</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">N</span><span class="topo-membrane">PYIYLGGAILAEVIGTTLM</span><span class="topo-inside">KFSNGFTRLI</span><span class="topo-membrane">PSMGTIICYCASFWLLAQTL</span><span class="topo-outside">AYIPT</span><span class="topo-membrane">GIAYAIWSGVGIVLISLLS</span><span class="topo-inside">WGFFGQRLDLP</span><span class="topo-membrane">AIIGMMLICAGVLIIN</span><span class="topo-outside">LL</span><span class="topo-unknown">SRSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>21</td>
      <td>3</td>
      <td>21</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>22</td>
      <td>31</td>
      <td>22</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>51</td>
      <td>32</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>56</td>
      <td>52</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>75</td>
      <td>57</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>86</td>
      <td>76</td>
      <td>86</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>102</td>
      <td>87</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>104</td>
      <td>103</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>110</td>
      <td>105</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mh6">7MH6</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">N</span><span class="topo-membrane">PYIYLGGAILAEVIGTTLM</span><span class="topo-outside">KFSNGFTRL</span><span class="topo-membrane">IPSMGTIICYCASFWLLAQTL</span><span class="topo-inside">AYIPT</span><span class="topo-membrane">GIAYAIWSGVGIVLISL</span><span class="topo-outside">LSWGFFGQRLDLPAI</span><span class="topo-membrane">IGMMLICAGVLIINLL</span><span class="topo-unknown">SRSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>21</td>
      <td>3</td>
      <td>21</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>22</td>
      <td>30</td>
      <td>22</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>51</td>
      <td>31</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>56</td>
      <td>52</td>
      <td>56</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>73</td>
      <td>57</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>88</td>
      <td>74</td>
      <td>88</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>104</td>
      <td>89</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>105</td>
      <td>110</td>
      <td>105</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7mgx">7MGX</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">NPYI</span><span class="topo-membrane">YLGGAILAEVIGTTLMK</span><span class="topo-inside">FSNGFTRLI</span><span class="topo-membrane">PSMGTIICYCASFWLL</span><span class="topo-outside">AQTLAYIPTGIAY</span><span class="topo-membrane">AIWSGVGIVLISLLSWG</span><span class="topo-inside">FFGQRLDL</span><span class="topo-membrane">PAIIGMMLICAGVL</span><span class="topo-outside">IINLL</span><span class="topo-unknown">SRSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>5</td>
      <td>2</td>
      <td>5</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>22</td>
      <td>6</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>31</td>
      <td>23</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>47</td>
      <td>32</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>60</td>
      <td>48</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>61</td>
      <td>77</td>
      <td>61</td>
      <td>77</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>85</td>
      <td>78</td>
      <td>85</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>86</td>
      <td>99</td>
      <td>86</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>104</td>
      <td>100</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>110</td>
      <td>105</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7svx">7SVX</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">NPY</span><span class="topo-membrane">IYLGGAILAEVIGTTLM</span><span class="topo-outside">KFSNGFTRLIPSM</span><span class="topo-membrane">GTIICYCASFWLLAQ</span><span class="topo-inside">TLAYIPTG</span><span class="topo-membrane">IAYAIWSGVGIVLISLL</span><span class="topo-outside">SWGFFGQRLDLPA</span><span class="topo-membrane">IIGMMLICAGVLIIN</span><span class="topo-inside">LL</span><span class="topo-unknown">SRSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>21</td>
      <td>5</td>
      <td>21</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>22</td>
      <td>34</td>
      <td>22</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>49</td>
      <td>35</td>
      <td>49</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>57</td>
      <td>50</td>
      <td>57</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>74</td>
      <td>58</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>87</td>
      <td>75</td>
      <td>87</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>102</td>
      <td>88</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>104</td>
      <td>103</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>110</td>
      <td>105</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7svx">7SVX</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">NPY</span><span class="topo-membrane">IYLGGAILAEVIGTTLM</span><span class="topo-inside">KFSNGFTRL</span><span class="topo-membrane">IPSMGTIICYCASFWLLA</span><span class="topo-outside">QTLAYIPT</span><span class="topo-membrane">GIAYAIWSGVGIVLISLL</span><span class="topo-inside">SWGFFGQ</span><span class="topo-unknown">RL</span><span class="topo-inside">DLPAI</span><span class="topo-membrane">IGMMLICAGVLIIN</span><span class="topo-outside">L</span><span class="topo-unknown">LSRSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>21</td>
      <td>5</td>
      <td>21</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>22</td>
      <td>30</td>
      <td>22</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>48</td>
      <td>31</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>56</td>
      <td>49</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>74</td>
      <td>57</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>81</td>
      <td>75</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>82</td>
      <td>83</td>
      <td>82</td>
      <td>83</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>84</td>
      <td>88</td>
      <td>84</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>89</td>
      <td>102</td>
      <td>89</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>103</td>
      <td>103</td>
      <td>103</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>110</td>
      <td>104</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7ssu">7SSU</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">NPYI</span><span class="topo-membrane">YLGGAILAEVIGT</span><span class="topo-outside">TLMKFSNGFTRLIPSM</span><span class="topo-membrane">GTIICYCASFWLLA</span><span class="topo-inside">QTLAYIPTGIA</span><span class="topo-membrane">YAIWSGVGIVLISL</span><span class="topo-outside">LSWGFFGQRLDLPAII</span><span class="topo-membrane">GMMLICAGVLIIN</span><span class="topo-inside">LL</span><span class="topo-unknown">SRSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>5</td>
      <td>2</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>18</td>
      <td>6</td>
      <td>18</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>19</td>
      <td>34</td>
      <td>19</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>48</td>
      <td>35</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>59</td>
      <td>49</td>
      <td>59</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>73</td>
      <td>60</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>89</td>
      <td>74</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>102</td>
      <td>90</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>104</td>
      <td>103</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>110</td>
      <td>105</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7ssu">7SSU</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">NPYIYL</span><span class="topo-membrane">GGAILAEVIGTTLM</span><span class="topo-inside">KFSNGFTRL</span><span class="topo-membrane">IPSMGTIICYCASFWLL</span><span class="topo-outside">AQTLAYIPTGIA</span><span class="topo-membrane">YAIWSGVGIVLISLLS</span><span class="topo-inside">WGFFGQRLDLPA</span><span class="topo-membrane">IIGMMLICAGVL</span><span class="topo-outside">IINL</span><span class="topo-unknown">LSRSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>21</td>
      <td>8</td>
      <td>21</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>22</td>
      <td>30</td>
      <td>22</td>
      <td>30</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>47</td>
      <td>31</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>59</td>
      <td>48</td>
      <td>59</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>75</td>
      <td>60</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>87</td>
      <td>76</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>99</td>
      <td>88</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>103</td>
      <td>100</td>
      <td>103</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>110</td>
      <td>104</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7sv9">7SV9</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">NPY</span><span class="topo-membrane">IYLGGAILAEVIGTTLM</span><span class="topo-inside">KFSNGF</span><span class="topo-membrane">TRLIPSMGTIICYCASFWLLA</span><span class="topo-outside">QTLAYIPT</span><span class="topo-membrane">GIAYAIWSGVGIVLISLL</span><span class="topo-inside">SWGFFGQRLDLPAII</span><span class="topo-membrane">GMMLICAGVLIIN</span><span class="topo-outside">L</span><span class="topo-unknown">LSRSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>21</td>
      <td>5</td>
      <td>21</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>22</td>
      <td>27</td>
      <td>22</td>
      <td>27</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>28</td>
      <td>48</td>
      <td>28</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>56</td>
      <td>49</td>
      <td>56</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>74</td>
      <td>57</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>89</td>
      <td>75</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>102</td>
      <td>90</td>
      <td>102</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>103</td>
      <td>103</td>
      <td>103</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>110</td>
      <td>104</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7sv9">7SV9</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">NPYI</span><span class="topo-membrane">YLGGAILAEVIGTTLM</span><span class="topo-outside">KFSNGFTRLIPSM</span><span class="topo-membrane">GTIICYCASFWLLA</span><span class="topo-inside">QTLAYIPTGIA</span><span class="topo-membrane">YAIWSGVGIVLISLL</span><span class="topo-outside">SWGFFGQRLDLP</span><span class="topo-membrane">AIIGMMLICAGVL</span><span class="topo-inside">IINLL</span><span class="topo-unknown">SRSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>5</td>
      <td>2</td>
      <td>5</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>6</td>
      <td>21</td>
      <td>6</td>
      <td>21</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>22</td>
      <td>34</td>
      <td>22</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>48</td>
      <td>35</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>59</td>
      <td>49</td>
      <td>59</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>74</td>
      <td>60</td>
      <td>74</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>75</td>
      <td>86</td>
      <td>75</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>99</td>
      <td>87</td>
      <td>99</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>100</td>
      <td>104</td>
      <td>100</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>110</td>
      <td>105</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7t00">7T00</a> — Chain A (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">NPY</span><span class="topo-membrane">IYLGGAILAEVIGTTLMK</span><span class="topo-inside">FSNGFTRLI</span><span class="topo-membrane">PSMGTIICYCASFWLL</span><span class="topo-outside">AQTLAYIPTGIA</span><span class="topo-membrane">YAIWSGVGIVLISLLS</span><span class="topo-inside">WGFFGQRLDLPA</span><span class="topo-membrane">IIGMMLICAGVLII</span><span class="topo-outside">NLL</span><span class="topo-unknown">SRSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>22</td>
      <td>5</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>31</td>
      <td>23</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>47</td>
      <td>32</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>59</td>
      <td>48</td>
      <td>59</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>75</td>
      <td>60</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>87</td>
      <td>76</td>
      <td>87</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>88</td>
      <td>101</td>
      <td>88</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>104</td>
      <td>102</td>
      <td>104</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>110</td>
      <td>105</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7t00">7T00</a> — Chain B (4 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">N</span><span class="topo-membrane">PYIYLGGAILAEVIGT</span><span class="topo-outside">TLMKFSNGFTRLIPS</span><span class="topo-membrane">MGTIICYCASFWLLAQTL</span><span class="topo-inside">AYIP</span><span class="topo-membrane">TGIAYAIWSGVGIVLI</span><span class="topo-outside">SLLSWGFFGQRLDLPAII</span><span class="topo-membrane">GMMLICAGVLIINL</span><span class="topo-unknown">LSRSTPH</span></span>
<details class="topo-details"><summary>Topology coordinates (10 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>18</td>
      <td>3</td>
      <td>18</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>19</td>
      <td>33</td>
      <td>19</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>51</td>
      <td>34</td>
      <td>51</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>52</td>
      <td>55</td>
      <td>52</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>71</td>
      <td>56</td>
      <td>71</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>72</td>
      <td>89</td>
      <td>72</td>
      <td>89</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>103</td>
      <td>90</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>110</td>
      <td>104</td>
      <td>110</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Dual topology antiparallel homodimer

The 2007 X-ray structure (3.8 A, PDB 3B5D) provided definitive evidence for the antiparallel (dual topology) orientation of the EmrE homodimer. Selenomethionine-labeled crystals allowed unambiguous identification of the N-terminal region position relative to the membrane. The two monomers are oriented in opposite directions, with TM1-TM3 from each monomer surrounding the substrate binding chamber and TM4 helices participating only in dimer formation. This arrangement supports the "dual topology" model where small membrane proteins with an even number of TMs can insert in both orientations.

### Multipurpose crystallization chaperone for SMR proteins

A monobody (L10) originally developed for Gdx-Clo was repurposed as a crystallization chaperone for EmrE by introducing three conservative mutations (E25N, W31I, V34M) in loop 1. The EmrE3 mutant retains wild-type transport activity (Km within 2-fold of WT) and binds monobody L10 with Kd = 850 nM. The monobody mediates most crystal contacts, enabling both Gdx-Clo and EmrE to crystallize in a nearly identical unit cell despite 1-2 A displacements of binding pocket helices.

### Sidechain flexibility enables substrate polyspecificity

The EmrE binding site uses sidechain rearrangements rather than backbone movements to accommodate structurally diverse substrates. Key residues E14 and W63 adopt different rotamers depending on the bound substrate. E14 sidechains act like calipers, moving apart for large quaternary ammoniums or closer together for flat aromatic substrates. W63 rotamerizes to expand or narrow the binding pocket.

### Structural basis of the binding pocket

The substrate binding site is formed by residues from both subunits at the midpoint of the membrane, with two essential E14 residues defining the pocket edges. At pH 5.2 (proton-bound), both E14 residues are protonated. Substrates bind between the E14 residues, with their center of mass midway between the carboxylates. Aromatic residues Y60 and W63 contribute via ring stacking interactions.

### Comparison to Gdx-Clo reveals subtype-specific differences

The Qac-type EmrE and Gdx-type Gdx-Clo share high structural similarity (Calpha RMSD 1.2 A for the dimer) but differ in their H-bond network architecture. Gdx-Clo has a polarized stack of H-bond donors and acceptors (W16/E13/S42/W62) that constrains the central glutamate, whereas EmrE lacks this stack.

### Single-particle cryo-EM and structural validation

The crystal structure agrees closely with helical density from low-resolution EM maps and with computational models. Comparison to an NMR-based model of the S64V mutant (PDB 7JK8) shows a 2.3 A overall RMSD with differences in subunit packing and Y60 rotamer orientation.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/antibiotic-efflux-pump/">Antibiotic Efflux Pump</a> — EmrE is a multidrug efflux pump belonging to the SMR family
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — EmrE functions via dual-topology alternating access
- <a href="/xray-mp-wiki/concepts/protein-families/sm-family/">SMR (Small Multidrug Resistance) Family</a> — EmrE is the founding member of the SMR family
- <a href="/xray-mp-wiki/reagents/detergents/dm/">Decylmaltoside (DM)</a> — Primary detergent used for EmrE purification and crystallization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Reference detergent for SMR family purification
- <a href="/xray-mp-wiki/reagents/detergents/ldao/">Lauryldimethylamine N-oxide (LDAO)</a> — Used as crystallization additive
- <a href="/xray-mp-wiki/reagents/additives/peg-600/">PEG 600</a> — Precipitant for crystallization
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> — Used for affinity purification
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> — Buffer used in purification
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES</a> — Buffer used in size exclusion chromatography
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Used for elution in affinity chromatography
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride</a> — Salt used in purification buffers
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging-drop vapor diffusion</a> — Crystallization method
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Final polishing step in purification
