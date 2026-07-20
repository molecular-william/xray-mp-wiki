#!/usr/bin/env python3
"""Fix betp and glt-ph pdb_dois."""
import re, yaml

BASE = '/home/wtliaf/Desktop/Research/coding_projects/xray-mp-wiki/xray-mp-wiki/proteins_yaml'

# Fix betp: add 3JEO, 4AIN, 4AMR to pdb_dois
fp = f'{BASE}/betp.yaml'
with open(fp) as f:
    content = f.read()

# Add missing PDBs to pdb_dois
additions = """
    3JEO: doi/10.1038##nature07819
    4AIN: doi/10.1038##nature11403
    4AMR: doi/10.1038##nature11403"""
content = content.replace(
    '    4DOJ: doi/10.1038##nature11403',
    '    4DOJ: doi/10.1038##nature11403' + additions
)
content = re.sub(r'verified: regex', 'verified: agent', content)
with open(fp, 'w') as f:
    f.write(content)
print('Fixed betp')

# Fix glt-ph: add missing PDBs to pdb_dois
fp = f'{BASE}/glt-ph.yaml'
with open(fp) as f:
    content = f.read()

# Add missing PDBs
additions = """
    6WZB: doi/10.1038##s41586-021-03240-9
    6WYJ: doi/10.1038##s41586-021-03240-9
    6WYK: doi/10.1038##s41586-021-03240-9
    6WYL: doi/10.1038##s41586-021-03240-9
    4OYE: doi/10.7554##elife.02283
    4OYF: doi/10.7554##elife.02283
    4OYG: doi/10.7554##elife.02283
    4P1A: doi/10.7554##elife.02283
    4P3J: doi/10.7554##elife.02283
    4P6H: doi/10.7554##elife.02283"""
content = content.replace(
    '    7AHK: doi/10.1126##sciadv.aba9854',
    '    7AHK: doi/10.1126##sciadv.aba9854' + additions
)
content = re.sub(r'verified: regex', 'verified: agent', content)
with open(fp, 'w') as f:
    f.write(content)
print('Fixed glt-ph')

print('Done')
