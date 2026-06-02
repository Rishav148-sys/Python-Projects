def process_order(inventory, cart):
    bill = {}
    grand_total = 0

    for item, quantity in cart.items():
        if item not in inventory:
            print(f"Sorry, '{item}' is not available in the shop.")
            continue

        available_stock = inventory[item]["stock"]
        price = inventory[item]["price"]

        if quantity > available_stock:
            print(f"Sorry, not enough stock for {item}")
        else:
            item_total = price * quantity
            bill[item] = (quantity, item_total)
            grand_total += item_total
            inventory[item]["stock"] -= quantity

    print("\n---- Bill ----")
    for item, (quantity, total) in bill.items():
        print(f"{item} x{quantity} = NPR {total}")
    print(f"Grand Total: NPR {grand_total}")
    print("--------------")

    print("\nUpdated stock:")
    stock_summary = ", ".join(f"{item}={details['stock']}" for item, details in inventory.items())
    print(stock_summary)


# Given data
inventory = {
    "rice":  {"price": 120, "stock": 20},
    "milk":  {"price":  90, "stock": 10},
    "bread": {"price":  60, "stock": 15},
    "eggs":  {"price":  15, "stock": 30}
}

cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}

process_order(inventory, cart)