def func_cntry_cnt(country_list):
	"""
	Create a dict, country_counts whose keys are country names, 
				and whose values are the number of times the country occurs 
				in the countries list. 

	country_list = list of strings			
	"""

	dict_country = {}

	for c in country_list:
		if c not in dict_country: 
			dict_country[c] = country_list.count(c)
			#print(dict_country)	

	return dict_country		

country_list = ['Malta',
 'Malta',
 'Malta',
 'Jamaica',
 'Pakistan',
 'Netherlands',
 'Venezuela']

print(func_cntry_cnt(country_list))
