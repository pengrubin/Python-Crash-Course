import json

filename = 'numbers.json'
with open('numbers.json') as file_object:
    numbers = json.load(file_object)
    
print(numbers)
