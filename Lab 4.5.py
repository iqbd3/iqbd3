i = 0
while i != 1:
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    if str(username) == "ITC" and str(password) == "P@ssword":
        print ("welcome you can use the system now !")
        i = i + 1
    else :
        print("Wrong username or password")