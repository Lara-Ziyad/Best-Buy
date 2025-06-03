class Product:
    """
    A class to represent a product in an inventory system.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a Product instance and validates inputs.
        Raises ValueError if any input is invalid.
        """
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Returns the current quantity."""
        return self.quantity

    def set_quantity(self, quantity)
        """Sets a new quantity and deactivates the product if it reaches 0."""

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        """Returns whether the product is active."""
        self.active = True

    def deactivate(self):
        """Activates the product."""
        self.active = False

    def show(self) -> str:
        """Returns a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """
        Buys a given quantity of the product.
        Returns the total price of the purchase.
        Raises an exception for invalid or unavailable quantities.
        """

        if not self.active:
            raise RuntimeError ("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than 0.")
        if quantity > self.quantity:
            raise RuntimeError("Not enough quantity in stock.")

        total_price = quantity * self.price
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price


# ---------------------- Usage Example ----------------------

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()