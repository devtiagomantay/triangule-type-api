def get_payload_dimensions(req, keyword):
	"""Get the values from the request using the keyword"""
	print('calling get_values_from_request function')
	try:
		values = req.json.get(keyword)
		validate_payload_values(values)
	except BaseException:
		print('The payload is invalid')
		return False

	return values


def validate_payload_values(payload):
	# check_if_is_a_list(payload)
	check_if_has_3_dimensions(payload)
	check_if_values_are_numbers(payload)


# This is already checked by schema validation
# def check_if_is_a_list(values_list):
# 	if not isinstance(values_list, list):
# 		raise 'Payload is not a list'


def check_if_has_3_dimensions(values_list):
	if len(values_list) != 3:
		print("Payload doesn't have 3 values_lists")
		raise "Payload doesn't have 3 values_lists"


def check_if_values_are_numbers(values_list):
	for each_value in values_list:
		if not each_value.isnumeric():
			print('Values are not numeric')
			raise 'Values are not numeric'
