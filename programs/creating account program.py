# vars and bool
# ______________________
usernames = []
passwords = []

# funcs 
# ______________________
def add_username(name):
    usernames.append(name)

def add_password(pas):
    passwords.append(pas)

# loops
# ______________________
while True:
    print("1 sign up")
    print("2 sign in")
    print("3 exit")

    try:
        x = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number (1–3)")
        continue

    # if statements
    # ______________________
    if x == 1:
        name = input("Enter your username: ")
        if name in usernames:
            print("Already exists")
        else:
            pas = input("Enter your password: ")
            add_username(name)
            add_password(pas)
            print("Account created successfully")

        print(usernames, passwords)

    elif x == 2:
        name = input("Enter your username: ")
        if name in usernames:
            idx = usernames.index(name)
            pas = input("Enter your password: ")
            if passwords[idx] == pas:
                print("Welcome " + name)
            else:
                print("Wrong password")
        else:
            print("Wrong username")

    elif x == 3:
        print("Goodbye!")
        break
