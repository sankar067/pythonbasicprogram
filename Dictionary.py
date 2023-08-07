site_stats = {'site': 'tecbeamers.com', 'traffic': 10000, "type": "organic"}
#type(site_stats)
print(site_stats)
#Read From A Dictionary
print(site_stats.get('site'))
print (site_stats["traffic"])

#Traverse Through A Dictionary Object
for key,value in site_stats.items():
    print(key)
    print(value)

site_stats2 = {}
site_stats2['site'] = 'google.co.in'
print(site_stats2)
{'site': 'google.co.in'}
site_stats_new = {'traffic': 1000000, "type": "social media"}
site_stats2.update(site_stats_new)
print(site_stats2)
site_stats2.pop('type',None)
print(site_stats2)
print('type' in site_stats2)  # checking deleted item(key) in dictionary)
print('traffic' in site_stats2)
adict = {var: var ** 2 for var in range(10, 20)}
print(adict)