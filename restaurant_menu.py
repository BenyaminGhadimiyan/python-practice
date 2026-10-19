"""Restaurant menu: choose items, build an order, show the total."""

# Sample prices - change them as you like.
MENU = {
    1: ("Ash (soup)", 6.0),
    2: ("Khoresht (stew)", 12.0),
    3: ("Salad", 5.0),
    4: ("Fast food", 15.0),
}


def show_menu():
    print("\n--- Menu ---")
    for number, (name, price) in MENU.items():
        print(f"{number} = {name} (${price:.2f})")
    print("0 = Finish order")


def main():
    order = []

    while True:
        show_menu()
        try:
            choice = int(input("Enter the item number: "))
        except ValueError:
            print("Please enter numbers only.")
            continue

        if choice == 0:
            break
        if choice not in MENU:
            print("This number is not on the menu.")
            continue

        name, price = MENU[choice]
        order.append((name, price))
        print(f"{name} added to your order.")

    print("\n--- Your order ---")
    if not order:
        print("No items ordered.")
        return
    for name, price in order:
        print(f"{name}: ${price:.2f}")
    total = sum(price for _, price in order)
    print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()
