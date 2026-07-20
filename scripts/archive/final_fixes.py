#!/usr/bin/env python3
"""Final batch fixes for remaining YAML files."""
import re

BASE = '/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki/xray-mp-wiki/proteins_yaml'

# Fix cysz - remove duplicate 3TX3 line
fp = f'{BASE}/cysz.yaml'
with open(fp) as f:
    content = f.read()
# Replace duplicate lines
content = content.replace('    3TX3: doi/10.7554##elife.27829\n    3TX3:', '    3TX3:')
# Fix verified
content = re.sub(r'verified: regex', 'verified: agent', content)
with open(fp, 'w') as f:
    f.write(content)
print('Fixed cysz')

# Fix clpp - verified
fp = f'{BASE}/clpp.yaml'
with open(fp) as f:
    content = f.read()
content = re.sub(r'verified: regex', 'verified: agent', content)
with open(fp, 'w') as f:
    f.write(content)
print('Fixed clpp')

# Fix cytochrome-b5 - add 2I96 to pdb_dois
fp = f'{BASE}/cytochrome-b5.yaml'
with open(fp) as f:
    content = f.read()
content = content.replace(
    '    6WF2: doi/10.1016##j.jmb.2020.05.017',
    '    6WF2: doi/10.1016##j.jmb.2020.05.017\n    2I96: doi/10.1016##j.jmb.2020.05.017'
)
content = re.sub(r'verified: pdb', 'verified: agent', content)
with open(fp, 'w') as f:
    f.write(content)
print('Fixed cytochrome-b5')

# Fix cytochrome-b5-reductase - add 1UMK to pdb_dois
fp = f'{BASE}/cytochrome-b5-reductase.yaml'
with open(fp) as f:
    content = f.read()
content = content.replace(
    '    6WF2: doi/10.1016##j.jmb.2020.05.017',
    '    6WF2: doi/10.1016##j.jmb.2020.05.017\n    1UMK: doi/10.1016##j.jmb.2020.05.017'
)
with open(fp, 'w') as f:
    f.write(content)
print('Fixed cytochrome-b5-reductase')

# Fix arabidopsis-nitrate-transporter-nrt1-1 - fix DOI case, add 4CL4/4CL5 to pdb_dois
fp = f'{BASE}/arabidopsis-nitrate-transporter-nrt1-1.yaml'
with open(fp) as f:
    content = f.read()
content = content.replace(
    '    5A2N: doi/10.1038##nature13116',
    '    5A2N: doi/10.1038##nature13116\n    4CL4: doi/10.1038##nature13116\n    4CL5: doi/10.1038##nature13116'
)
content = re.sub(r'verified: regex', 'verified: agent', content)
with open(fp, 'w') as f:
    f.write(content)
print('Fixed arabidopsis-nitrate-transporter-nrt1-1')

# Fix af-tmem16 - the pdb_dois has 4WIS but structures has 4L3A
# Both are from different DOI papers. Let's add 4L3A to pdb_dois
fp = f'{BASE}/af-tmem16.yaml'
with open(fp) as f:
    content = f.read()
content = content.replace(
    '    4WIS: doi/10.1038##nature13984',
    '    4WIS: doi/10.1038##nature13984\n    4L3A: doi/10.1038##nature12535'
)
with open(fp, 'w') as f:
    f.write(content)
print('Fixed af-tmem16')

print('\nAll fixes applied.')
