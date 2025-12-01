# vars and bool
# ______________________
usernames = []
passwords = []

# funcs
# ______________________
def shopping_cart():
    items = ["milk", "egg", "butter", "water", "coffee", "ice cream", "chips", "drinks"]
    prices = [3, 1.2, 5, 0.5, 2, 1.5, 1, 0.75]

    # sort both lists together by price
    combined = list(zip(items, prices))
    combined.sort(key=lambda x: x[1])
    items, prices = zip(*combined)
    items = list(items)
    prices = list(prices)

    cart = []
    pay = []

    a = 1
    while a == 1:
        print("_________________________________")
        print("1 Add item")
        print("2 Remove item")
        print("3 View cart")
        print("4 Check out and exit")
        print("_________________________________")

        try:
            x = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number between 1–4.")
            continue

        if x == 1:
            # Show available items
            print("Available items:")
            for i in range(len(items)):
                print(f"{i + 1}. {items[i]} - {prices[i]}$")
            while True:
                try:
                    itemChoice = int(input("Enter item number to add (0 to go back): "))
                except ValueError:
                    print("Enter a valid number.")
                    continue

                if itemChoice == 0:
                    break
                elif 1 <= itemChoice <= len(items):
                    cart.append(items[itemChoice - 1])
                    pay.append(prices[itemChoice - 1])
                    print(f"Added: {items[itemChoice - 1]}")
                else:
                    print("Invalid choice, try again.")

        elif x == 2:
            if not cart:
                print("Your cart is empty.")
                continue
            while True:
                print("Your cart:", cart)
                itemremove = input("Enter item name to remove (or 0 to go back): ").lower()
                if itemremove == "0":
                    break
                elif itemremove in [i.lower() for i in cart]:
                    idx = [i.lower() for i in cart].index(itemremove)
                    print(f"Removed: {cart[idx]}")
                    cart.pop(idx)
                    pay.pop(idx)
                else:
                    print("Item not found, try again.")

        elif x == 3:
            print("_________________________________")
            if cart:
                total = 0
                for n in range(len(cart)):
                    print(f"{n + 1}. {cart[n]} - {pay[n]}$")
                    total += pay[n]
                print(f"Total: {total}$")
            else:
                print("Your cart is empty.")
            print("_________________________________")

        elif x == 4:
            print("_________________________________")
            if cart:
                total = sum(pay)
                print("Your final cart:")
                for i in range(len(cart)):
                    print(f"{cart[i]} - {pay[i]}$")
                print("-----------------------------")
                print("Total:", total, "$")
                print("Thank you for shopping! ")
            else:
                print("You didn’t buy anything.")

        else:
            print("Invalid choice, try again.")


def paswwordchecker(password, real_name, year, month, username):
    # vars & bool
    # ______________________
    upp_let = False  # upper letter
    low_let = False  # lower letter
    num = False  # number
    sym = False  # symbol
    score = 0


    for char in password:
        if 'A' <= char <= 'Z':
            upp_let = True
        elif 'a' <= char <= 'z':
            low_let = True
        elif '0' <= char <= '9':
            num = True
        elif char in "~!@#$%^&*+-/.,{}[]();:?<>\"'_":
            sym = True

    # score
    #_______________________
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
    if real_name.lower() in password.lower():
        score -= 1
    if year in password or month in password:
        score -= 1
    if username.lower() in password.lower():
        score -= 1

    # results
    #_______________________
    if score <= 0:
        print("Invalid password, try again")
        return False
    elif score in range(1, 3):
        print("Weak password, try again")
        return False
    elif score == 3:
        print("Medium password")
        return True
    else:
        print("Strong password")
        return True


def add_username(name):
    usernames.append(name)

def add_password(pas):
    passwords.append(pas)


# Main program
# ________________________
real_name = str(input("Enter your name: "))
year = str(input("Enter your born date (year): "))
if int(year) < 1925 or int(year) > 2025:
    print("error")
    quit()
month = str(input("Enter your born date (month): "))
if int(month) < 1 or int(month) > 12:
    print("error")
    quit()

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
        username = input("Enter your username: ")
        if username in usernames:
            print("Already exists")
        else:
            while True:
                pas = input("Enter your password: ")
                if paswwordchecker(pas, real_name, year, month,username):
                    add_username(username)
                    add_password(pas)
                    print("Account created successfully")
                    break

    elif x == 2:
        username = input("Enter your username: ")
        if username in usernames:
            idx = usernames.index(username)
            pas = input("Enter your password: ")
            if passwords[idx] == pas:
                print("Welcome " + username)
                shopping_cart()
            else:
                print("Wrong password")
        else:
            print("Wrong username")

    elif x == 3:
        print("Goodbye")
        break
