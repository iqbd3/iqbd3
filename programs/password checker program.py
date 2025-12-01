def paswwordchecker(password):
    # vars & bool
    # ______________________
    upp_let = False  # upper letter
    low_let = False  # lower letter
    num = False  # number
    sym = False  # symbol
    score = 0

    # funcs
    # ______________________
    for char in password:
        if char >= 'A' and char <= 'Z':
            upp_let = True
        elif char >= 'a' and char <= 'z':
            low_let = True
        elif char >= '0' and char <= '9':
            num = True
        elif char in "~!@#$%^&*+-/.,{}[]();:?<>\"'_":
            sym = True

    # if statements
    # _______________________
    if upp_let:
        score += 1
    if low_let:
        score += 1
    if num:
        score += 1
    if sym:
        score += 1
    if len(password) >= 8:
        score += 1
    if name.lower() in password.lower():
        score -= 1
    if year in password or month in password:
        score -= 1

    if score <= 0:
        print("Invalid password , try again ")
        return False
    elif score in range(1, 3):
        print("Weak password , try again ")
        return False
    elif score == 3:
        print("Medium password ")
        return True
    else:
        print("Strong password ")
        return True


# Main program
# ________________________
name = str(input("Enter your name: "))
year = str(input("Enter your born date (year): "))
if int(year) < 1925 or int(year) > 2025:
    print("error")
    quit()
month = str(input("Enter your born date (month): "))
if int(month) < 1 or int(month) > 12:
    print("error")
    quit()

while True:
    user_password = str(input("Enter your password: "))
    if paswwordchecker(user_password):
        break




