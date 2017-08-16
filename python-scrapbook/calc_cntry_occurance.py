def func_cntry_cnt(country_list):
	r"""Return a dict, with country name as key and the number of times that country occurs 
	in the input countries list as value. 

	country_list -- string. List.			
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
