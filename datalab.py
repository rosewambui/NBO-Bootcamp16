  
"""Takes the input provided and returns a value of the data type to the input """
def data_type(y):

	the_input = type(y)

	if the_input == str:
		return len(y)
	
	elif the_input == bool:
		return y

	elif the_input == int:
			"""include another ifelse statemnt that compare the input to 100 """
			if y == 100:
				return "equal to 100"
			elif y <100:
				return "less than 100"
			else:
				return "more than 100"

	elif the_input == list:
			if y [2:]:
				return 3
			elif y  [1:]:
				return None
			else:
				pass
	else:
		return 'no value'

if __name__ == '__main__':
    unittest.main()
