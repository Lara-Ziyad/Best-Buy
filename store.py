from products import Product  # Make sure products.py is in the same folder


class Store:
    """
    A class to represent a store containing multiple products.
    """

    def __init__(self, products):
        """
        Initializes the store with a list of Product instances.
        """
        self.products = products

    def add_product(self, product):
        """
        Adds a product to the store.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store if it exists.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """
        Returns the total quantity of all products in the store.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """
        Returns a list of all active products in the store.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """
        Accepts a list of (Product, quantity) tuples.
        Returns the total cost of the purchase.
        """
        return sum(product.buy(quantity) for product, quantity in shopping_list)


# Example usage (for testing)
if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    print("All active products:")
    for p in best_buy.get_all_products():
        print(p.show())

    print("\nTotal quantity in store:", best_buy.get_total_quantity())

    total_price = best_buy.order([
        (product_list[0], 1),  # MacBook
        (product_list[1], 2)   # Bose
    ])
    print(f"\nOrder cost: {total_price} dollars")
