import products
import store
from store_operations import show_option_list, show_store_products,show_store_quantity, make_order

# The list of menu options for the store (displayed in main menu)
option_list = (
    f"\n--- Welcome to Best Buy ---"
    "\n\n1. List all products in store"
    "\n2. Show total amount in store"
    "\n3. Make an order"
    "\n4. Quit"
)
def main():
    """
    Main function to initialize the store and run the user interface loop.
    """
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    # Create store instance with product list
    best_buy = store.Store(product_list)

    # Define the dispatcher dictionary
    dispatcher = {
        "1": lambda: show_store_products(best_buy.get_all_products()),
        "2": lambda: show_store_quantity(best_buy.get_total_quantity()),
        "3": lambda: make_order(best_buy)
    }

    # Main menu loop
    while True:
        show_option_list(option_list)

        choice = input("Enter your choice (1-4): ").strip()

        # Use dispatcher to call the corresponding function
        if choice in dispatcher:
            dispatcher[choice]()

        elif choice == "4":
            print("👋 Thank you for shopping with us!")
            break

        # Handle invalid input
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")


# Entry point of the script
if __name__ == "__main__":
    main()

