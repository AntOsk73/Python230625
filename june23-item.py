items = []

num_items = int(input("How many items do you want to buy? "))

for i in range(num_items):
    name = input(f"\nEnter name of item {i+1}: ")
    price = float(input(f"Enter price of {name}: "))
    quantity = int(input(f"Enter quantity of {name}: "))
    items.append({"name": name, "price": price, "quantity": quantity})

print("\nReceipt:")
subtotal = 0

for item in items:
    total_price = item["price"] * item["quantity"]
    subtotal += total_price
    print(f"- {item['name']} x{item['quantity']} = ${total_price:.2f}")

discount = 0.1 * subtotal  # 10% discount
tax = 0.05 * (subtotal - discount)
total = subtotal - discount + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount applied: -${discount:.2f}")
print(f"Tax (5%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
