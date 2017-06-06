import urllib.request
import urllib.parse

import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)
"""
country {'name': 'Liechtenstein'}
country {'name': 'Singapore'}
country {'name': 'Panama'}
"""
print()
print(root[0][1].text)
"""

2008
"""

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

print()
"""
{'name': 'Austria', 'direction': 'E'}
{'name': 'Switzerland', 'direction': 'W'}
{'name': 'Malaysia', 'direction': 'N'}
{'name': 'Costa Rica', 'direction': 'W'}
{'name': 'Colombia', 'direction': 'E'}

"""
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)
"""
Liechtenstein 1
Singapore 4
Panama 68
"""
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')

tree.write('output1.xml')

for country in root.findall('country'):
     rank = int(country.find('rank').text)
     if rank > 50:
        root.remove(country)

tree.write('output2.xml')
