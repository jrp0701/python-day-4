gradebook = {
    "Jaylen" : "B",
    "Stacy" : "D",
    "Oswald" : "C"
}
grade = input("What is your name? ")

if gradebook.get(grade):
    print(grade, "got a", gradebook.get(grade))

else:
    print("Student not found.")