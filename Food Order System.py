# ============================================
#         FOOD ORDER SYSTEM
# ============================================

# Menu stored as a dictionary: {Item Number: {"name": Item Name, "price": Price}}
menu = {
    1: {"name": "ZInger Burger", "price": 300},
    2: {"name": "Regular Pizza", "price": 450},
    3: {"name": "Pasta", "price": 280},
    4: {"name": "Sandwich", "price": 190},
    5: {"name": "Loaded Fries", "price": 170},
    6: {"name": "Fried Rice", "price": 250},
    7: {"name": "Noodles", "price": 230},
    8: {"name": "Cold Drink", "price": 80},
    9: {"name": "Coffee", "price": 120},
    10: {"name": "Ice Cream", "price": 100},
}

# Dictionary to store ordered items: {Item Name: {"qty": Quantity, "price": Price}}
order_dict = {}


def display_menu():
    """Display the food menu in a formatted table."""
    print("\n" + "=" * 45)
    print("           ** FOOD MENU **")
    print("=" * 45)
    print(f"{'No.':<6}{'Item':<20}{'Price (Rs.)':>10}")
    print("-" * 45)
    for item_no, item_data in menu.items():
        print(f"{item_no:<6}{item_data['name']:<20}{item_data['price']:>10}")
    print("-" * 45)

def discount(total):
    """If Items Greater than 2 then Apply Discount of 5%"""
    if len(order_dict) > 2:
        discount_amount = total * 0.05
        return discount_amount
    return 0


def take_order():
    """Let the user select items and quantities."""
    while True:
        display_menu()
        print(f"\nItems in your cart: {len(order_dict)}")
        print("\nEnter item number to order (0 to finish ordering): ", end="")
        choice = input()

        # Validate input is a number
        if not choice.isdigit():
            print(">> Invalid input! Please enter a valid number.")
            continue

        choice = int(choice)

        # Check if user wants to finish ordering
        if choice == 0:
            if len(order_dict) == 0:
                print(">> You haven't ordered anything yet!")
                continue
            else:
                break

        # Validate menu item number
        if choice < 1 or choice > len(menu):
            print(f">> Invalid choice! Please select between 1 and {len(menu)}.")
            continue

        # Get selected item details from menu dictionary
        selected_item = menu[choice]["name"]
        selected_price = menu[choice]["price"]

        # Ask for quantity
        print(f"Enter quantity for {selected_item}: ", end="")
        qty = input()

        if not qty.isdigit() or int(qty) <= 0:
            print(">> Invalid quantity! Please enter a positive number.")
            continue

        qty = int(qty)

        # Add/update item in the order dictionary
        if selected_item in order_dict:
            order_dict[selected_item]["qty"] += qty
        else:
            order_dict[selected_item] = {"qty": qty, "price": selected_price}

        print(f">> Added {qty} x {selected_item} to your order!")


def display_order_summary():
    """Display the final order summary with total bill."""
    print("\n" + "=" * 55)
    print("             ** ORDER SUMMARY **")
    print("=" * 55)
    print(f"{'Item':<20}{'Qty':>6}{'Price':>10}{'Subtotal':>12}")
    print("-" * 55)

    total = 0
    for name, item_data in order_dict.items():
        qty = item_data["qty"]
        price = item_data["price"]
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

