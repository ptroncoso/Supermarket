

import datetime #automatically puts in date and time

products = [{"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]




#Defining Product ids

product_ids = []

while True:
    product_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    if product_id == "DONE":
        break
    else:
        product_ids.append(int(product_id)) #makes an internal list of product ids
#Defining how to LOOK UP a product by it's product id (where we know that one id only corresponds to one product or item)
def lookup_product_by_id(product_id): # Filtering Technique
    matching_products = [product for product in products if product["id"] == product_id] # in this case, the matching "product" is only one
    return matching_products[0] # because the line above gives us a list and we want to return a single item.

#
# PRINT RECEIPT
#

running_total = 0

print("-------------------------------") # Margin
print("PALOMA'S FINE FOODS")
print("-------------------------------") # Space
print("Web: www.palomasfinefoods.com")
print("Phone: 1.123.456.7890")
print("Checkout Time: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S"))

print("-------------------------------") # Space
print("Shopping Cart Items:")
for product_id in product_ids:
    product = lookup_product_by_id(product_id)
    running_total += product["price"] # Running total variable updates itself
    price_usd = ' (${0:.2f})'.format(product["price"]) # Defining format for price
    print(" + " + product["name"] + price_usd)

print("-------------------------------")
print("Subtotal:", '${0:.2f}'.format(running_total)) # Defining format
tax = running_total * 0.08875
print("Plus NYC Sales Tax (8.875%):", '${0:.2f}'.format(tax)) # Defining format
total = running_total + tax
print("Total:", '${0:.2f}'.format(total)) # Defining format

print("-------------------------------") # Space
print("Thanks for your business! Please stop by again.")
