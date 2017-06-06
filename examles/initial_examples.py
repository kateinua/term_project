from craigslist import CraigslistHousing, CraigslistJobs,  CraigslistEvents, CraigslistForSale

# looking for rooms in Miami with price 700 - 1200$ and private room
cl_h = CraigslistHousing(site='miami', category='roo',
                         filters={'min_price': 700, 'max_price': 1200, 'private_room': True})
# sort all by price increasing with geotag and we want to see only 3 examples
for result in cl_h.get_results(sort_by='price_asc', geotagged=True, limit=3):
    print(result)
'''
{'url': 'http://miami.craigslist.org/mdc/roo/5973430111.html', 'price': '$700', 'where': 'KENDALL',
'datetime': '2017-02-22 11:40', 'id': '5973430111', 'geotag': (25.6574, -80.3627), 'has_image': True, 'has_map': True,
'name': 'ROOMATE FOR KENDALL'}
{'url': 'http://miami.craigslist.org/brw/roo/5977652263.html', 'price': '$700', 'where': 'Ft Lauderdale',
'datetime': '2017-02-21 08:49', 'id': '5977652263', 'geotag': (26.142563, -80.121966), 'has_image': False,
'has_map': True, 'name': 'GWM seeking roommate'}
{'url': 'http://miami.craigslist.org/mdc/roo/5980692115.html', 'price': '$700',
'where': 'Miami, Kendall, MDC, Colleges', 'datetime': '2017-02-24 14:07', 'id': '5980692115',
'geotag': (25.683497, -80.367823), 'has_image': True, 'has_map': True,
'name': 'Walk to everything, Close to Bus* Furnished large Room, Wi-Fi, Cable'}
'''

# searching english internship in New York
cl_j = CraigslistJobs(site='newyork', category='eng',
                      filters={'is_internship': True})
# print all of the results sorted by date
for result in cl_j.get_results(sort_by='newest'):
    print(result)

'''
{'url': 'http://newjersey.craigslist.org/eng/6036161223.html', 'price': None, 'where': None,
'datetime': '2017-03-09 08:36', 'id': '6036161223', 'geotag': None, 'has_image': False, 'has_map': True,
'name': 'Virtual Assistant Wanted to help NYC thought leader'}
'''

# search for events in Totonto that is free and with food
cl_e = CraigslistEvents(site='toronto', filters={'free': True, 'food': True})
# sort by date and print 4 of them
for result in cl_e.get_results(sort_by='newest', limit=4):
    print(result)

'''
{'has_map': True, 'url': 'http://toronto.craigslist.org/tor/eve/6071597240.html', 'price': None, 'id': '6071597240',
'where': 'Toronto', 'datetime': None, 'geotag': None, 'name': 'African Wine Tasting +snacks', 'has_image': True}
{'has_map': True, 'url': 'http://toronto.craigslist.org/tor/eve/6037382901.html', 'price': None, 'id': '6037382901',
'where': '427 Bloor St. W', 'datetime': None, 'geotag': None, 'name': 'An EnChanted Evening - Sundays',
'has_image': True}
{'has_map': True, 'url': 'http://toronto.craigslist.org/tor/eve/6035793210.html', 'price': None, 'id': '6035793210',
'where': None, 'datetime': None, 'geotag': None, 'name': 'Reclaim Your Voice - Taking the Stand pt 2',
'has_image': True}
{'has_map': True, 'url': 'http://toronto.craigslist.org/tor/eve/5937376115.html', 'price': None, 'id': '5937376115',
'where': None, 'datetime': None, 'geotag': None, 'name': 'Participants needed for OCAD Film Project',
'has_image': False}
'''

# search for cars in Chicago with price less than 5000 and less miles than 109000
cl_f = CraigslistForSale(site='chicago', filters={'max_price': 5000, 'max_miles': 109000})
# sort by price decrease and print 3 elements
for result in cl_f.get_results(sort_by='price_desc', limit=3):
    print(result)

'''
{'where': 'michigan city', 'price': '$5000', 'name': '1998 Mercedes Benz', 'datetime': '2017-03-19 18:29',
'has_map': True, 'geotag': None, 'url': 'http://chicago.craigslist.org/nwi/cto/6013391101.html', 'has_image': False,
'id': '6013391101'}
{'where': 'Berwyn', 'price': '$5000', 'name': '***84 Delta 88 Royale Brougham', 'datetime': '2017-03-21 17:42',
'has_map': True, 'geotag': None, 'url': 'http://chicago.craigslist.org/chc/cto/6015985964.html', 'has_image': False,
'id': '6015985964'}
{'where': 'Chicago', 'price': '$5000', 'name': '08 Chevrolet Silverado 1500', 'datetime': '2017-03-15 19:00',
'has_map': True, 'geotag': None, 'url': 'http://chicago.craigslist.org/chc/cto/6019797294.html', 'has_image': True,
'id': '6019797294'}
'''

