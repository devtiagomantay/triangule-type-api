def get_values_from_request(req, keyword):
	"""Get the values from the request using the keyword"""
	print('calling get_values_from_request function')
	try:
		values = req.json.get(keyword)
	except Exception as e:
		print('Error retrieving keyword. Detail ' + str(e))
		return []

	return values
