# ============================================
#         FOOD ORDER SYSTEM
# ============================================

# Menu stored as a list of tuples: (Item Name, Price)
menu = [
    ("ZInger Burger", 300),
    ("Regular Pizza", 450),
    ("Pasta", 280),
    ("Sandwich", 190),
    ("Loaded Fries", 170),
    ("Fried Rice", 250),
    ("Noodles", 230),
    ("Cold Drink", 80),
    ("Coffee", 120),
    ("Ice Cream", 100),
]

# List to store ordered items as tuples: (Item Name, Quantity, Price)
order_list = []


def display_menu():
    """Display the food menu in a formatted table."""
    print("\n" + "=" * 45)
    print("           ** FOOD MENU **")
    print("=" * 45)
    print(f"{'No.':<6}{'Item':<20}{'Price (Rs.)':>10}")
    print("-" * 45)
    for i in range(len(menu)):
        item_name, item_price = menu[i]
        print(f"{i + 1:<6}{item_name:<20}{item_price:>10}")
    print("-" * 45)

def discount(total):
    """If Items Greater than 2 then Apply Discount of 5%"""
    if len(order_list) > 2:
        discount_amount = total * 0.05
        return discount_amount
    return 0


def take_order():
    """Let the user select items and quantities."""
    while True:
        display_menu()
        print(f"\nItems in your cart: {len(order_list)}")
        print("\nEnter item number to order (0 to finish ordering): ", end="")
        choice = input()

        # Validate input is a number
        if not choice.isdigit():
            print(">> Invalid input! Please enter a valid number.")
            continue

        choice = int(choice)

        # Check if user wants to finish ordering
        if choice == 0:
            if len(order_list) == 0:
                print(">> You haven't ordered anything yet!")
                continue
            else:
                break

        # Validate menu item number
        if choice < 1 or choice > len(menu):
            print(f">> Invalid choice! Please select between 1 and {len(menu)}.")
            continue

        # Get selected item details from menu tuple
        selected_item, selected_price = menu[choice - 1]

        # Ask for quantity
        print(f"Enter quantity for {selected_item}: ", end="")
        qty = input()

        if not qty.isdigit() or int(qty) <= 0:
            print(">> Invalid quantity! Please enter a positive number.")
            continue

        qty = int(qty)

        # Add order as a tuple to the order list
        order_list.append((selected_item, qty, selected_price))
        print(f">> Added {qty} x {selected_item} to your order!")


def display_order_summary():
    """Display the final order summary with total bill."""
    print("\n" + "=" * 55)
    print("             ** ORDER SUMMARY **")
    print("=" * 55)
    print(f"{'Item':<20}{'Qty':>6}{'Price':>10}{'Subtotal':>12}")
    print("-" * 55)

    total = 0
    for item in order_list:
        name, qty, price = item
        subtotal = qty * price
        total = total + subtotal
        print(f"{name:<20}{qty:>6}{price:>10}{subtotal:>12}")

    print("-" * 55)
    discount_amount = discount(total)
    print(f"\n{'TOTAL BILL':.<40} Rs. {total}")
    if discount_amount > 0:
        print(f"{'DISCOUNT (5%)':.<40} - Rs. {discount_amount}")
        total -= discount_amount
    print(f"{'FINAL BILL':.<40} Rs. {total}")
    print("=" * 55)


# ============ MAIN PROGRAM ============

print("=" * 45)
print("    Welcome to the Food Order System!")
print("=" * 45)

take_order()
display_order_summary()

print("\nThank you for your order! Enjoy your meal!")

