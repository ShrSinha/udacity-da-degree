def scores_to_rating(score1,score2,score3,score4,score5):
	"""
	Take 5 scores in any datatype, map and return corresponding rating. 

	score1 -- datatype agnostic
	score2 -- datatype agnostic
	score3 -- datatype agnostic
	score4 -- datatype agnostic
	score5 -- datatype agnostic
	"""
	score1 = convert_to_numeric(score1)
	score2 = convert_to_numeric(score2)
	score3 = convert_to_numeric(score3)
	score4 = convert_to_numeric(score4)
	score5 = convert_to_numeric(score5)

	average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3
	rating = scores_to_rating_string (average_score)
	return rating

def convert_to_numeric(score):
	"""
	Convert input to float datatype.

	score -- datatype agnostic
	"""
	return float(score)	

def sum_of_middle_three(score1,score2,score3,score4,score5):
	"""
	Calculate sum of middle three scores.

	score1 -- float
	score2 -- float
	score3 -- float
	score4 -- float
	score5 -- float
	"""
	return score1 + score2 + score3 + score4 + score5 - min(score1,score2,score3,score4,score5) - max(score1,score2,score3,score4,score5)

def scores_to_rating_string(av_score):
	"""
	Map average score to rating.

	av_score -- float
	"""
	if av_score < 1:
		return "Terrible"
	elif av_score < 2:
		return "Bad"
	elif av_score < 3:
		return "OK"
	elif av_score < 4:
		return "Good"
	else:
		return "Excellent"



print(scores_to_rating("1","2.4","3.567","4","5.1"))        


