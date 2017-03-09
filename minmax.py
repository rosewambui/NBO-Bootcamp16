def find_max_min(x):

	if type(x) == list:

		minimum = min(x)
		maximum = max(x)

		y = []

		if minimum == maximum:
			y.append(len(x))

		else:
			y.append(minimum)
			y.append(maximum)

		return y

	else:
		return "Input is not a list"