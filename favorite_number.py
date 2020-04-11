import json
def show_number():
	file_name = "choose_number.json"
	try:
		with open(file_name) as file:
			number = json.load(file)
	except FileNotFoundError:
		number = input("what is the number?")
		with open(file_name,"w") as file:
			json.dump(number,file)
		print("I know your favatite number! It is " + number)
	else:
		print("I know your favatite number! It is " + number)

show_number()