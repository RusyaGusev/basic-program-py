
def main():
    print("Hello welcome to our new messenger! How can I call you?")
    username = input("Enter username: ")
    print("Hello, " + username + " Do you want to say something?")
    answer = input()
    gen_answer = answer.lower()
    while gen_answer != 'yes' and gen_answer != 'no':
        print("What do you want to say?")
        message = input()
        print(username + " said: " + message)
    while gen_answer != 'no':
        print("What do you want to say?")
        message = input()
        print(username + " said: " + message)
    while gen_answer != 'yes':
        print("What do you want to say?")
        message = input()
        print(username + " said: " + message)
    leave = input("Press enter to exit")
if __name__ == '__main__':
    main()


