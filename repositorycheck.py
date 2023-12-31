import sys
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re


# displaying the shoe inventory data - Murtaaz
class Shoe_Search:
    """
    A class for searching and filtering shoe inventory data through various input 
    statements.
    """

    def __init__(self, shoe_inventory):
        """
        Initialize a shoe search instance with the shoe inventory data.

        Args:
        shoe_inventory: A list of the shoe inventory which has another list in 
        it that represents a shoe's attributes.
        """
        self.shoe_inventory = shoe_inventory
        self.filtered_shoes = []

    def display_shoes(self):
        """
        Display filtered shoe inventory based on user preferences.

        The method prompts the user to enter filtering conditions such as brand, 
        gender, size, color, and availability, and then filters the shoe inventory 
        data accordingly.

        Displays the filtered results or a message if no matching shoes are found.
        """
        
        brand = input("Enter the brand (or leave empty to skip): ").lower()
        gender = input("Enter the gender (or leave empty to skip): ").lower()
        size = input("Enter the size (or leave empty to skip): ")
        color = input("Enter the color (or leave empty to skip): ").lower()
        availability = input("Enter the availability (in stock/out of stock or leave empty to skip): ").lower()


    
        # Convert size to float if it is not empty
        if size:
            size = float(size)
        
        self.filtered_shoes.clear()


        for shoe in self.shoe_inventory:
            if (not brand or brand == shoe[0].lower()) and \
               (not gender or gender == shoe[1].lower()) and \
               (not size or size == float(shoe[2])) and \
               (not color or color in shoe[3].lower()) and \
               (not availability or availability == shoe[4].lower()):
                self.filtered_shoes.append(shoe)

        if self.filtered_shoes:
            print("\nFiltered Shoes:")
            for i, shoe in enumerate(self.filtered_shoes):
                print(f"{i}: {shoe}")
        else:
            print("\nNo matching shoes found")

# Read the inventory data
def read_inventory_data():
    with open('shoe_inventory.txt', 'r', encoding = 'utf-8') as file:
        shoe_inventory = []

        for line in file:
            values = line.strip().split(', ')
            shoe_inventory.append(values)
    
    return shoe_inventory

# Shoe data graphs - Murtaaz
class ShoeDataAnalyzer: 
    """Class for analyzing shoe inventory data and generating different graphs."""
    
    def __init__(self):
        """Initialize the ShoeDataAnalyzer.

        Side Effects:
            Initializes the internal state, setting self.data to None.
        """
        self.data = None

    def gather_data_from_file(self, file_path):
        """Read shoe inventory data from a CSV file.

        Args:
            file_path (str): The path to the CSV file containing shoe inventory data.

        Raises:
            FileNotFoundError: If the specified file is not found.

        Side Effects:
            Reads data from the specified CSV file and sets self.data.
        """
        try:
            columns = ["Brand", "Model", "Gender", "Size", "Color", "Stock Status", "Price", "Quantity"]
            self.data = pd.read_csv("shoe_inventory.txt", header=None, names=columns)

            self.data['Price'] = pd.to_numeric(self.data['Price'], errors='coerce')
        except FileNotFoundError:
            print(f"File not found: {file_path}")

    def generate_graph(self):
         """Generate various graphs based on user choice.

        Users can choose from the following options:
        1. Histogram of Shoe Prices
        2. Boxplot of Shoe Prices by Gender
        3. Bar Plot of Average Quantity by Brand
        4. Count Plot of Stock Statuses by Brand

        Raises:
            ValueError: If an invalid choice is inputed.

        Side Effects:
            Displays the selected graph using matplotlib and seaborn libraries.
        """
        if self.data is None:
            print("No data available. Please run gather_data_from_file first.")
            return

        print("\nSelect the type of graph:")
        print("1. Histogram of Shoe Prices")
        print("2. Boxplot of Shoe Prices by Gender")
        print("3. Bar Plot of Average Quantity by Brand")
        print("4. Count Plot of Stock Statuses by Brand")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.data['Price'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black', figsize=(10, 6))
            plt.title('Histogram of Shoe Prices')
            plt.xlabel('Price')
            plt.ylabel('Frequency')
            plt.show()

        elif choice == '2':
            self.data.boxplot(column='Price', by='Gender', grid=False, figsize=(10, 6))
            plt.title('Boxplot of Shoe Prices by Gender')
            plt.suptitle('')
            plt.xlabel('Gender')
            plt.ylabel('Price')
            plt.show()

        elif choice == '3':
            avg_quantity_by_brand = self.data.groupby('Brand')['Quantity'].mean()
            plt.figure(figsize=(12, 6))
            sns.barplot(x=avg_quantity_by_brand.index, y=avg_quantity_by_brand.values, palette='viridis')
            plt.title('Bar Plot of Average Quantity by Brand')
            plt.xlabel('Brand')
            plt.ylabel('Average Quantity')
            plt.show()

        elif choice == '4':
            plt.figure(figsize=(14, 6))
            sns.countplot(x='Brand', hue='Stock Status', data=self.data)
            plt.title('Count Plot of Stock Statuses by Brand')
            plt.xlabel('Brand')
            plt.ylabel('Count')
            plt.legend(title='Stock Status', bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.show()

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Sorting Through File w Parsing & Sorting Inventory - Will:

def parse_inventory_data(filename):
    inventory_list = []

    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  
            if not line:
            # Skip empty lines
                continue

            elements = line.split(',')
            if len(elements) != 7:
            # Skip lines with incorrect format
                continue

            try:
                brand, gender, size, color, availability, price, units_sold = [element.strip() for element in elements]
                size = float(size)
                price = float(price)
                units_sold = int(units_sold)

                shoe_item = {
                    'brand': brand,
                    'gender': gender,
                    'size': size,
                    'color': color,
                    'availability': availability,
                    'price': price,
                    'units_sold': units_sold
                }
                inventory_list.append(shoe_item)
            except ValueError:
            # Skip lines with conversion errors
                continue

    return inventory_list

def sort_inventory(inventory_list, sort_key):
    
    return sorted(inventory_list, key=lambda item: item[sort_key])

inventory_list = parse_inventory_data('shoe_inventory.txt')

# Sort the inventory based on different attributes
sorted_inventory_by_size = sort_inventory(inventory_list, 'size')
sorted_inventory_by_price = sort_inventory(inventory_list, 'price')
sorted_inventory_by_availability = sort_inventory(inventory_list, 'availability')
sorted_inventory_by_units_sold = sort_inventory(inventory_list, 'units_sold')


# Print sorted inventories
print("Sorted by Size:")
for item in sorted_inventory_by_size:
    print(item)

print("\nSorted by Price:")
for item in sorted_inventory_by_price:
    print(item)

print("\nSorted by Availability:")
for item in sorted_inventory_by_availability:
    print(item)
    
print("\nSorted by Units_sold:")
for item in sorted_inventory_by_units_sold:
    print(item)

# Prompt the user to log in
user = user_login()

# Check if the user has a saved cart
cart = check_saved_cart(user)

# If the user has a saved cart, print the items in the cart
if not cart:
    cart = Cart()
    user.cart = cart

item_index = int(input("Enter the index of the item you want to add to the cart: "))
if item_index < 0 or item_index >= len(search.filtered_shoes):
    print("Invalid index. Please enter a number between 0 and", len(search.filtered_shoes) - 1)
else:
    item = search.filtered_shoes[item_index]
    item_name = item[0]
    quantity = int(input("Enter the quantity you want to add to the cart: "))
    price = float(item[6])

    cart.add_item(item_name, quantity, price)  

item = sorted_inventory_by_units_sold[item_index]
item_name = item['brand']
quantity = int(input("Enter the quantity you want to add to the cart: "))
price = item['price']

# Add the item to the cart
cart.add_item(item_name, quantity, price)



# Account Information - Garrick
class User:
    def __init__ (self, username, password):
        """ Initializing a user object.
        Parameters:
        - username (str): the username of the user
        - password (str): the password of the user
        """
        self.username = username
        self.password = password
        self.cart = []

class CartItem:
    def __init__ (self, item_name, quantity, price):
        """ Initializing a CartItem object
        Parameters:
        - item_name (str): The name of the item.
        - quantity (int): The quantity of the item.
        - price (float): The price of the item.
        """
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

class Cart:
    def __init__(self):
        """
        Initialize a part object with an empty list of items.
        """
        self.items = []

    def add_item(self, item_name, quantity, price):
        """
        Add an item to the cart.

        Parameters:
        - item_name (str): The name of the item.
        - quantity (int): The quantity of the item.
        - price (float): The price of the item.
        """
        item = CartItem(item_name, quantity, price)
        self.items.append(item)

def user_login():
    """
    Prompts the user to log in with a username and password.
    Returns a User object if login is successful, None otherwise.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the login is successful
    if validate_user(username, password):
        print(f"Welcome back, {username}!")
        return User(username, password)
    else:
        print("Invalid username or password. Please try again.")
        return None

def validate_user(username, password):
    """ Check for user validation
    
    Parameters:
    - username (str): The username entered by the user.
    - password (str): The password entered by the user.

    Returns:
    - bool: True if the user is valid, False otherwise.
    """
    return username == "sample_user" and password == "sample_password"

def check_saved_cart(user):
    """
    Checks if the user has a saved cart.

    Parameters:
    - user (User): The user object.

    Returns:
    - list: A list of CartItem objects representing the cart.
    """
    if user and user.cart:
        return user.cart
    else:
        return None
# Order summary- Abhiram
class Order:
    """
    Represents a customer order.

    Attributes:
        order_number (int): The number for the order.
        customer (str): The name of the customer placing the order.
        address (str): The delivery address for the order.
        cart (Cart): The shopping cart containing items in the order.

    Methods:
        order_summary(payment_type=None, status="Processed"):
            Generate and return an order summary for display to the customer
    
    """
    def __init__ (self, customer, address,cart):
        """
        Initializes an Order Object.
        """
        self.order_number = f"{random.randInt(1000,9999)}"
        self.customer = customer
        self.address = address
        self.cart = Cart()
        
    def order_summary(self, payment_type= None, status = "Processed)"):
        """ Order Summary to display to the customer

        Arguments:
        payment_type(str): User's payment method and will be based on their choice.
        order_status(str): The status of the order, and default will be Processed
        
        """
        total_cost = 0.0
        for item in self.cart.items:
            total_cost += item.price * item.quantity
        total_cost_display = f"Total Cost: ${total_cost}\n"
        order_info= f"Order Item:{self.cart.items}\nOrder Number: {self.order_number}\nCustomer: {self.customer}\nAddress: {self.address}\n"
        payment_type = f"Payment Information:{payment_type}\n"
        order_status = f"Order Status: {status}\n"
        return_policy = f"\nReturn Policy: All orders are accepted for return up to 30 days with full refund"
        summary = order_info + total_cost_display + payment_type + order_status + order_status + return_policy
    def __str__(self):
        return f"Order:{self.order_number} for {self.customer}" 
# Cart Information- Yonas 

class ShoppingCart:
    """
    Represents a final shopping cart
    """
    def __init__(self):
        """
        Initializes a new object from Cart

        Side effect:
        shipping_fee attribute is set to 0 

        """
        self.shipping_fee = 0

    def calculate_shipping_fee(self, user_address):
        """
        Calculates the shipping fee based on the users address 

        Args: 
        user_address(str): The users address

        Returns: 
        The shipping fee 
        """
        self.shipping_fee = 12 if user_address == 'United States of America' else 25 if user_address == 'Europe' else 35 
        
        return self.shipping_fee
    def process_payment(self, name, card_number, expiry_date, cvv, address, payment_type="Debit"):
        """
        Processes the payment for the order

        Args: 
        name (str): The name on the card
        card_number (str): The card number
        expiry_date (str): The expiry date of the card
        cvv (str): The CVV of the card
        address (str): The billing address
        payment_type (str): The type of the card. Set to Debit only

        Returns: 
        True if the payment is successful, False otherwise
        """
        if not re.match(r"""^[A-Za-z ]+$""", name):
            print("Invalid name.")
            return False
        if not re.match(r"""^\d{16}$""", card_number):
            print("Please enter a valid 16 digit debit card number")
            return False
        if not re.match(r"""^\d{2}/\d{2}$""", expiry_date):
            print("Please enter an expiray date in the format MM/YY")
            return False
        if not re.match(r"""^\d{3}$""", cvv):
            print("Please enter a valid 3 digit CVV number.")
            return False
