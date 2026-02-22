import json
# Task 1 — Read the inventory 
# Print the total number of books currently in the file
with open ("inventory.json" , "r") as file:
    inventory = json.load(file)
    print(f"Total Number of Books Currently available in the Inventory: {len(inventory)}")

# Task 2 — Update and save 
# Append new_book to the inventory list
# Write the updated list back to inventory.json
    new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}
    inventory.append(new_book)
with open ("inventory.json" , "w") as file:
    json.dump (inventory, file, indent=4)

# Task 3 — Display the inventory
# Read and print each book's details in the following format:
# Title: The Alchemist | Author: Paulo Coelho | Price: $12.99
# Title: 1984 | Author: George Orwell | Price: $9.99
# Title: Atomic Habits | Author: James Clear | Price: $14.99

with open ("inventory.json", "r") as file:
    inventory_updated = json.load (file)
    for item in inventory_updated:
        print(f"\nTitle: {item["title"]} | Author: {item["author"]} | Price: ${item["price"]}")

