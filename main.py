import products
import store


def start(store_instance):
    """
    Starts the Best Buy user interface.
    """
    while True:
        print((f"\n--- Welcome to Best Buy ---"
               "1. List all products in store"
               "2. Show total amount in store"
               "3. Make an order"
               "4. Quit"))

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print("\n📦 Available Products:")
            for index, product in enumerate(store_instance.get_all_products(), start=1):
                print(f"{index}. {product.show()}")

        elif choice == "2":
            total = store_instance.get_total_quantity()
            print(f"\n📊 Total quantity in store: {total}")

        elif choice == "3":
            products_list = store_instance.get_all_products()
            shopping_list = []

            print("\nWhich product would you like to order?")
            for i, product in enumerate(products_list, start=1):
                print(f"{i}. {product.show()}")

            selection = input("------\n1Enter product number (or press Enter to finish):  ").strip()

            if not selection:
                continue  # Return to main menu

            if not selection.isdigit() or int(selection) < 1 or int(selection) > len(products_list):
                print("❌ Invalid selection.")
                continue

            product_index = int(selection) - 1
            selected_product = products_list[product_index]

            quantity_input = input(f"How many '{selected_product.name}' would you like to order? ").strip()

            if not quantity_input:
                print("🔙 Returning to main menu.")
                continue  # Go back to main menu

            try:
                quantity = int(quantity_input)
                if quantity <= 0:
                    print("❌ Quantity must be greater than 0.")
                    continue
                if quantity > selected_product.get_quantity():
                    print(f"❌ Not enough quantity in stock. Available: {selected_product.get_quantity()}")
                    continue
                shopping_list.append((selected_product, quantity))
                total_price = store_instance.order(shopping_list)
                print((f"✔️ '{selected_product.name}' added to the list."
                       f"\n✅ Order placed successfully! Total cost: ${total_price}"))
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "4":
            print("👋 Thank you for shopping with us!")
            break

        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")

# ---------------------------------------
# Initial inventory and app startup
# ---------------------------------------

if __name__ == "__main__":
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = store.Store(product_list)
    start(best_buy)
