import json
file_name = "choose_number.json"
with open(file_name) as file:
	number = json.load(file)
	print(number)