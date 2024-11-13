Inventory Management System (IMS) Project Overview

This Inventory Management System (IMS) is a console-based application designed to manage inventory for a small business. The system enables basic functionalities like adding, updating, deleting, and viewing products, with role-based permissions for "Admin" and "User" accounts. 

Key Components and Implementation:

1. User Authentication and Role Management: 
   - A `User` class allows for a basic login system where users enter a username and password. Only "admin" (password: "admin") has full privileges.
   - Role-based access is implemented, where admins can manage the inventory, while users can only view it.

2. Product Management: 
   - The `Product` class defines each product with attributes such as `product_id`, `name`, `category`, `price`, and `stock_quantity`.
   - Products are stored in a dictionary, with `product_id` as the key, allowing quick access and modifications.

3. Inventory Operations:
   - The `Inventory` class implements the core functionalities:
      - `add_product` adds new products to the inventory.
      - `update_product` modifies product attributes based on `product_id`.
      - `delete_product` removes products from inventory.
      - `view_products` lists all available products.
   - Admins access these operations through a simple menu interface.

4. Error Handling and Input Validation:
   - The program validates user inputs, handling errors for non-existent products and invalid choices, ensuring a smooth user experience.

Outcome:
This project demonstrates object-oriented programming principles, with encapsulation and CRUD operations for managing products. The system also introduces basic role-based access and authentication, preparing for further enhancements and scalability.
