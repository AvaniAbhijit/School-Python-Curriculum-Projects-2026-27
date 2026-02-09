# What is a Dictionary?
# A dictionary stores data in key : value format.
# It is written using { }.
# We can add, change, or remove items.

# Task 1: Create a dictionary of a car.
# Task 2: Print the brand name using key.
# Task 3: Print all items using a for loop.

# Create a dictionary of a mobile phone
mobile = {
    "brand": "Samsung",
    "model": "Galaxy A14",
    "price": 15000,
    "color": "Black"
}

# Print the dictionary
print("Mobile Details:", mobile)

# Print total number of items
print("Total items:", len(mobile))

# Print the brand name
print("Brand:", mobile["brand"])

# Print all details using loop
print("All Details:")
for key in mobile:
    print(key, ":", mobile[key])

# Change the price
mobile["price"] = 14000
print("Updated Price:", mobile)

# Add a new item
mobile["storage"] = "128GB"
print("After Adding Storage:", mobile)

# Remove an item
mobile.pop("color")
print("After Removing Color:", mobile)
