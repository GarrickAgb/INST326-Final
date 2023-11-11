import sys
import argparse
import sklearn
print "Hello World"
def repo():
    
print("Murtaaz")
print("LazoWill")
print("Abhiram")


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
class OrderSummary:
    """
    """
# Many elements for the classes/methods are missing key data inputs, just an idea as to what it will look like.
