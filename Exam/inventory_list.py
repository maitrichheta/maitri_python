print("\nWelcome to Inventory List Analyzer!\n")


items = {}
categories = []

while True:
    name = input("Enter item name: ").lower()
    category = input("Enter category: ").lower()
    quantity = int(input("Enter quantity: "))
    
    items[name] = quantity

    if category not in categories:
        categories.append(category)
    more = input("\nDo you want to add more items? (y/n): ")
    print()
    if more.lower() != 'y':
        break

print("\n========== INVENTORY SUMMARY ==========")

print("Total Different Items:", len(items))
print("Total Quantity in Stock:", sum(items.values()))

average = sum(items.values()) / len(items)
print("Average Quantity per Item:", average)

most = max(items, key=items.get)
least = min(items, key=items.get)

print("Most Stocked Item:", most, "-", items[most], "units")
print("Least Stocked Item:", least, "-", items[least], "units")

categories = sorted(categories)
print("\n----------------------------------------\n")
print(f"Unique Categories in Inventory: {set(categories)}")

print("\n-----------------------------------------\n")

print("\n📦 Items Sorted by Quantity (High to Low):")
sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
for item, quantity in sorted_items:
    print(item, "-", quantity, "units")

print("\n-----------------------------------------\n")

print("\n📂 Categories in Alphabetical Order:")
for i, catagory in enumerate(categories, 1):
    print(f"{i}. {catagory}")

print("\n========== END OF REPORT ==========")