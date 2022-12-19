def is_triangle_equilateral(t_dim):
	"""An equilateral triangle has all three sides the same length."""
	if t_dim.count(t_dim[0]) == 3:
		return True
	return False


def is_triangle_isosceles(t_dim):
	"""An isosceles triangle has two sides the same length."""
	if t_dim.count(t_dim[0]) == 2 or t_dim.count(t_dim[1]) == 2:
		return True

	return False


def is_triangle_scalene(t_dim):
	"""A scalene triangle has all sides of different lengths."""
	if t_dim.count(t_dim[0]) == 1 and t_dim.count(t_dim[1]) == 1:
		return True
	return False


def calculate_triangle_type(dim):
	print('calling calculate_triangle_type with dimensions' + str(dim))
	try:
		if is_triangle_equilateral(dim):
			return "equilateral"
		elif is_triangle_isosceles(dim):
			return "isosceles"
		elif is_triangle_scalene(dim):
			return "scalene"
		return "error"

	except Exception as e:
		print("A error occurred trying to calculate the triangle type. Detail: ", e)
