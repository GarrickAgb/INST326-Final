import sys
import argparse
import sklearn
print "Hello World"
def repo():
    
print("Murtaaz")
print("LazoWill")
print("Abhiram")

displaying the shoe inventory data - Murtaaz
with open('shoe_inventory.txt', 'r', encoding = 'utf-8') as file:
    shoe_inventory = []

    for line in file:
        values = line.strip().split(', ')
        shoe_inventory.append(values)

for shoe in shoe_inventory:
    print(shoe)
    
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

        
        filtered_shoes = []
        for shoe in self.shoe_inventory:
            if (not brand or brand in shoe[0].lower()) and \
               (not gender or gender in shoe[1].lower()) and \
               (not size or size == shoe[2]) and \
               (not color or color in shoe[3].lower()) and \
               (not availability or availability == shoe[4].lower()):
                filtered_shoes.append(shoe)

        if filtered_shoes:
            print("\nFiltered Shoes:")
            for shoe in filtered_shoes:
                print(shoe)
        else:
            print("\nNo matching shoes found")

search = Shoe_Search(shoe_inventory)
search.display_shoes()

class ShoeInventory_Graphs
#will hope to add a class containing methods where i can display a visualization of our inventory and sales through graphs using Pandas.

Sorting Through File w Parsing & Sorting Inventory - Will:

def parse_inventory_data('file_path'):
#reads and parses CSV shoe inventory file into a list of dictionaries 
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        inventory_list = [dict(item) for item in reader]
#converts numerical fields from strings to neccesary data types
for item in inventory_list:
    item['size'] = int(item['size'])
    item['price'] = float(item['price'])
return inventory_list

def sort_inventory(inventory_list, sort_key);
#sorts inventory based on given sort key
    return sorted(inventory_list, key=lambda x: x[sort_key])
    
inventory_list = parse_inventory_data('path_to_csv_file')

#sorts the shoe inventory by different criteria: size, price, availability
sorted_inventory_by_size = sort_inventory(inventory_list, 'size')
sorted_inventory_by_price = sort_inventory(inventory_list, 'price')
sorted_inventory_by_availability = sort_inventory(inventory_list, 'availability')

#print sorted inventory 
print(sorted_inventory_by_size)
print(sorted_inventory_by_price)
print(sorted_inventory_by_availability)

Account Information - Garrick
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
    def __init__ (self, item_name, qunatity, price):
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
class Order:
    """
    """
    def __init__ (self, order_number, customer, address,cart):
        """
        """
        self.order_number = order_number
        self.customer = customer
        self.address = address
        self.cart = Cart()
        
    def order_summary(self, payment_type= None, status = "Processed)":
        """ Order Summary to display to the customer

        Arguments:
        payment_type(str): User's payment method and will be based on their choice.
        order_status(str): The status of the order, and default will be Processed
        
        """
        total_cost = 0.0
        for item in self.cart.items:
            total_cost += item.price * item.quantity
        total_cost_display = f"Total Cost: ${total_cost}\n"
        order_info= f"Order Item:{self.cart.items)\nOrder Number: {self.order_number}\nCustomer: {self.customer}\nAddress: {self.address}\n"
        payment_type = f"Payment Information:{payment_type}\n"
        order_status = f"Order Status: {status}\n"
        return_policy = f"\nReturn Policy: All orders are accepted for return up to 30 days with full refund"
        summary = order_info + total_cost_display + payment_type + order_status + order_status + return_policy
# Many elements for the classes/methods are missing key data inputs, just an idea as to what it will look like.
