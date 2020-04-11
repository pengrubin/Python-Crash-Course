import json


def get_number():
	file_name = "choose_number.json"
	try:
		with open(file_name) as file:
			return json.load(file)
	except FileNotFoundError:
		return False


def get_new_number():
	file_name = "choose_number.json"
	number = input("what is your number?")
	with open(file_name,"w") as file:
		json.dump(number,file)
		return number


def print_number():
	number = get_number()
	if number:
		print("your number is " + number)
	else:
		number = get_new_number()
		print("your number is " + number)


if __name__ == "__main__":
	print_number()