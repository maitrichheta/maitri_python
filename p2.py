print("Welcome to Inventory List Analyzer!\n")

items = {}
categories = []

while True:
    name = input("Enter item name: ")
    category = input("Enter category: ")
    quantity = int(input("Enter quantity: "))

    items[name] = quantity

    if category not in categories:
        categories.append(category)

    more = input("Do you want to add more items? (y/n): ")
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

print("\nUnique Categories:")
for cat in sorted(categories):
    print(cat)

print("\nItems Sorted by Quantity:")
sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
for item, qty in sorted_items:
    print(item, "-", qty, "units")

print("\n========== END OF REPORT ==========")