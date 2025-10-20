import os
from datetime import datetime

# Global variables
cart = []
bill_number = 1
customer_name = ""

# Ensure bills directory exists
if not os.path.exists("bills"):
    os.makedirs("bills")

# Function to set customer name
def set_customer_name():
    global customer_name
    customer_name = input("Enter customer's name: ").strip()
    if not customer_name:
        print("Name cannot be blank. Please try again.")
        set_customer_name()

# Function to add a product to the cart
def add_product():
    if not customer_name:
        set_customer_name()
    product = input("Enter product name: ").strip()
    try:
        price = float(input("Price per unit (₹): "))
        qty = int(input("Quantity: "))
    except ValueError:
        print("Invalid input. Price and quantity must be numbers.")
        return
    cart.append((product, price, qty))
    print(f"{qty} x {product} added to the bill.")

# Function to save the bill to a file
def save_bill():
    global bill_number, cart
    if not cart:
        print("The bill is empty. Please add products first.")
        return

    filename = f"bill_{bill_number}.txt"
    path = os.path.join("bills", filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write("===== SHOP BILL =====\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Bill No: {bill_number}\n")
        f.write(f"Customer: {customer_name}\n\n")

        total = 0
        for product, price, qty in cart:
            cost = price * qty
            f.write(f"{product} – {qty} x ₹{price:.2f} = ₹{cost:.2f}\n")
            total += cost

        f.write(f"\nTotal = ₹{total:.2f}\n")
        f.write("=====================")

    print(f"\n✅ Bill created and saved: {path}")
    bill_number += 1
    cart.clear()

# Function to view saved bills
def view_bill():
    files = os.listdir("bills")
    if not files:
        print("No bills have been saved yet.")
        return

    print("\nAvailable bills:")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")

    try:
        choice = int(input("Enter the number of the bill to view: "))
        if 1 <= choice <= len(files):
            path = os.path.join("bills", files[choice - 1])
            with open(path, "r", encoding="utf-8") as f:
                print("\n----- Saved Bill -----\n")
                print(f.read())
                print("----------------------\n")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu loop
def main():
    while True:
        print("\n1. Set customer name")
        print("2. Add product")
        print("3. Save bill")
        print("4. View saved bills")
        print("5. Exit")
        choice = input("What would you like to do? (1/2/3/4/5): ").strip()

        if choice == "1":
            set_customer_name()
        elif choice == "2":
            add_product()
        elif choice == "3":
            save_bill()
        elif choice == "4":
            view_bill()
        elif choice == "5":
            print("🛑 Billing system exited.")
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
