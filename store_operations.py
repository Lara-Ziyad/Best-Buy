def show_option_list(lst):
    """
    Function to print the store options list.

    Args:
        lst (str): The menu options string to display.
    """
    print(lst)


def show_store_products(prods):
    """
    Function to display all active products in the store.

    Args:
        prods (list): List of Product instances.
    """
    print(
        "\n📦 Available Products:\n"
        f"{'-' * (len('📦 Available Products:') + 1)}"
    )
    for i, product in enumerate(prods, start=1):
        print(f"{i}. {product.show()}")


def show_store_quantity(total_quantity):
    """
    Function to display the total quantity of all products in the store.

    Args:
        total_quantity (int): The total quantity to display.
    """
    print(f"\n📊 Total quantity in store: {total_quantity}")

def make_order(products_lst):
    """
    Function to handle the 'Make an order' process.
    Allows user to select products and quantities, with validation.
    """
    cart = {}  # Dictionary: product -> reserved quantity

    while True:
        products_list = products_lst.get_all_products()

        print("\nWhich product would you like to order?")
        for i, product in enumerate(products_list, start=1):
            reserved_qty = cart.get(product, 0)
            available_quantity = product.get_quantity() - reserved_qty
            print(f"{i}. {product.name}, Price: {product.price}, Quantity: {available_quantity}")

        selection = input("------\nEnter product number (or press Enter to finish): ").strip()

        if not selection:
            if not cart:
                print("🔙 Returning to main menu.")
            else:
                try:
                    total_price = 0
                    for product, qty in cart.items():
                        total_price += product.buy(qty)

                    print(f"✅ Order placed successfully! Total cost: ${total_price}")
                    print("🛒 You bought:")
                    for product, quantity in cart.items():
                       print(f"- {product.name}: {quantity} unit(s)")
                except RuntimeError as e:
                    print(f"❌ Error processing order: {e}")
            break

        if not selection.isdigit() or int(selection) < 1 or int(selection) > len(products_list):
            print("❌ Invalid selection.")
            continue

        product_index = int(selection) - 1
        selected_product = products_list[product_index]

        while True:
            quantity_input = input(f"How many '{selected_product.name}' would you like to order? ").strip()

            if not quantity_input:
                print("❌ You must enter a quantity.")
                continue  # Re-ask quantity, not product list

            try:
                quantity = int(quantity_input)
                if quantity <= 0:
                    print("❌ Quantity must be greater than 0.")
                    continue  # Re-ask quantity

                # Check available quantity
                already_reserved = cart.get(selected_product, 0)
                available_quantity = selected_product.get_quantity() - already_reserved

                if quantity > available_quantity:
                    print(f"❌ Not enough quantity available. Available (excluding your cart): {available_quantity}")
                    continue  # Re-ask quantity

                # Add to cart and break inner loop
                cart[selected_product] = already_reserved + quantity
                print(f"✔️ '{selected_product.name}' ({quantity} unit(s)) added to the cart.")
                break  # Exit quantity-asking loop → go to Y/N "continue shopping"

            except ValueError:
                print("❌ Please enter a valid number.")
                continue  # Re-ask quantity

        # Ask if the user wants to continue ordering
        keep_shopping = input("Do you want to buy more products? (Y/N): ").strip().lower()

        if keep_shopping == "n":
            if not cart:
                print("🛒 Your cart is empty. Returning to main menu.")
                break
            try:
                total_price = 0
                for product, qty in cart.items():
                    total_price += product.buy(qty)

                print(f"✅ Order placed successfully! Total cost: ${total_price}")
                print("🛒 You bought:")
                for product, qty in cart.items():
                    print(f"- {product.name}: {qty} unit(s)")
            except RuntimeError as e:
                print(f"❌ Error processing order: {e}")
            break
        elif keep_shopping != "y":
            print("❌ Invalid choice. Please enter Y or N.")