def main():
    age = int(input("What is your age? "))
    if age <= 13:
        print("Your ticket is 8$.")
    elif age >= 65:
        print("Your ticket is 10$.")
    else:
        print("Your ticket is 1$")

main()