import json
file_name = "choose_number.json"
number = input("what is the number?")
with open(file_name,"w") as file:
	json.dump(number,file)
	print("I know your favatite number! It is " + number)
