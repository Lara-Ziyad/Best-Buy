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
    shopping_list = []

    while True:
        products_list = products_lst.get_all_products()

        print("\nWhich product would you like to order?")
        for i, product in enumerate(products_list, start=1):
            print(f"{i}. {product.show()}")

        selection = input("------\nEnter product number (or press Enter to finish): ").strip()

        if not selection:
            print("🔙 Returning to main menu.")
            break  # Exit Make an order mode and return to main menu

        if not selection.isdigit() or int(selection) < 1 or int(selection) > len(products_list):
            print("❌ Invalid selection.")
            continue

        product_index = int(selection) - 1
        selected_product = products_list[product_index]

        quantity_input = input(f"How many '{selected_product.name}' would you like to order? ").strip()

        if not quantity_input:
            print("🔙 Returning to main menu.")
            break

        try:
            quantity = int(quantity_input)
            if quantity <= 0:
                print("❌ Quantity must be greater than 0.")
                continue
            if quantity > selected_product.get_quantity():
                print(f"❌ Not enough quantity in stock. Available: {selected_product.get_quantity()}")
                continue

            shopping_list.append((selected_product, quantity))

            print(f"✔️ '{selected_product.name}' added to the list.")


        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        # Ask if the user wants to continue ordering
        keep_shopping = input("Do you want to buy more products? (Y/N): ").strip().lower()

        if keep_shopping == "n":
            total_price = products_lst.order(shopping_list)
            print(f"✅ Order placed successfully! Total cost: ${total_price}  ")
            print("🛒 You bought:")
            for product, quantity in shopping_list:
                print(f"- {product.name}: {quantity} unit(s)")
            break
        elif keep_shopping != "y":
            print("❌ Invalid choice. Please enter Y or N.")