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
                print(f"{i+1}. {items[i]} - {prices[i]}$")
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
                    print(f"{n+1}. {cart[n]} - {pay[n]}$")
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
            break

        else:
            print("Invalid choice, try again.")
