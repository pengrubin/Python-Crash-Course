with open("pi_million_digits.txt") as rawdata:
	lines = rawdata.readlines()
pi_string = ""
for line in lines:
	pi_string += line.strip()
#birthday = input("please input your birthday")
birthday = "0112"
if birthday in pi_string:
	print("yes")
else:
	print("no")
