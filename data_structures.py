empty_list = []

grocery_list = ["apples", "bread", "ice cream", 300, True]
second_list = [[1,2], [3,4,5]]

students = ["Huck", "Shaun", "Lydia"]
print(students[1])
# This won't actually give us the first; indexed to 0.
students.append("Jeff")
print(students)

students.sort()
print(students)

empty = [] #empty list
empty = {} #empty dictionary

cars = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year" : 1964,
    "Color" : "Blue",
    "Status" : "For Sale"
}

print(cars.values())
