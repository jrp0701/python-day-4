gradebook = {
    "Jaylen" : "B",
    "Stacy" : "D",
    "Oswald" : "C"
}
def main():
    answer = input("Who's grade would you like to see? ")
    grade = gradebook.get(answer)
    print(grade)

main()
    