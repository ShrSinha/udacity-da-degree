def func_most_prolific_yr(dict_discography):
	r"""Return the highest occuring value in dictionary."""

	temp_list =[]
	temp_count = 0
	
	for key in dict_discography:
		temp_list.append(dict_discography[key])
		
	for index in temp_list:
	    if temp_list.count(index) > temp_count:
	        temp_count = temp_list.count(index)
	        temp_year = index
	return temp_year	



Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

print(most_prolific(Beatles_Discography))  