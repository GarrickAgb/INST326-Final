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

