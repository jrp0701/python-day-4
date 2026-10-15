def user_input():
    answer = input("Say something. ")
    answer = answer.replace(" ", "...")
    print(answer)

user_input()