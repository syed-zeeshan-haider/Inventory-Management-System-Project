# inventory_management_system.py

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.role = None

    def login(self):
        # Simulated login with hardcoded credentials
        if self.username == "admin" and self.password == "admin":
            self.role = "Admin"
        elif self.username == "user" and self.password == "admin":
            self.role = "User"
        else:
            print("Invalid username or password.")
            return False
        print(f"Login successful! Role: {self.role}")
        return True


class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"{self.product_id}: {self.name} | Category: {self.category} | Price: ${self.price} | Stock: {self.stock_quantity}"


class Inventory:
    def __init__(self):
        self.products = {}  # Dictionary to store products by product_id

    def add_product(self, product):
        if product.product_id in self.products:
            print("Product with this ID already exists.")
        else:
            self.products[product.product_id] = product
            print("Product added successfully.")

    def update_product(self, product_id, name=None, category=None, price=None, stock_quantity=None):
        product = self.products.get(product_id)
        if product:
            if name:
                product.name = name
            if category:
                product.category = category
            if price is not None:
                product.price = price
            if stock_quantity is not None:
                product.stock_quantity = stock_quantity
            print("Product updated successfully.")
        else:
            print("Product not found.")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def view_products(self):
        if not self.products:
            print("No products in inventory.")
        else:
            for product in self.products.values():
                print(product)


def main():
    print("Welcome to the Inventory Management System (IMS)")

    # Login simulation
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user = User(username, password)

    if not user.login():
        return

    inventory = Inventory()

    while True:
        if user.role == "Admin":
            print("\nAdmin Menu:")
            print("1. Add Product")
            print("2. Update Product")
            print("3. Delete Product")
            print("4. View Products")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                # Add Product
                product_id = input("Enter Product ID: ")
                name = input("Enter Product Name: ")
                category = input("Enter Product Category: ")
                price = float(input("Enter Product Price: "))
                stock_quantity = int(input("Enter Stock Quantity: "))
                product = Product(product_id, name, category, price, stock_quantity)
                inventory.add_product(product)
            elif choice == "2":
                # Update Product
                product_id = input("Enter Product ID to update: ")
                name = input("Enter new Product Name (leave blank to skip): ")
                category = input("Enter new Product Category (leave blank to skip): ")
                price = input("Enter new Product Price (leave blank to skip): ")
                stock_quantity = input("Enter new Stock Quantity (leave blank to skip): ")
                inventory.update_product(
                    product_id,
                    name=name if name else None,
                    category=category if category else None,
                    price=float(price) if price else None,
                    stock_quantity=int(stock_quantity) if stock_quantity else None,
                )
            elif choice == "3":
                # Delete Product
                product_id = input("Enter Product ID to delete: ")
                inventory.delete_product(product_id)
            elif choice == "4":
                # View Products
                inventory.view_products()
            elif choice == "5":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

        elif user.role == "User":
            print("\nUser Menu:")
            print("1. View Products")
            print("2. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                # View Products
                inventory.view_products()
            elif choice == "2":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
