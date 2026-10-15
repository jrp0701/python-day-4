def main():
    answer = input("Happy or Sad?")
    answer = answer.replace(":)", "🙂").replace(":(", "🙁")
    print(answer)

main()