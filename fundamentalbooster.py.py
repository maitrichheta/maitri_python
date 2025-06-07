print("Welcome to the Interactive Personal Data collector!\n")

name = input("Please Enter your name: ")
age = int(input("Please Enter your age: "))
height = float(input("Please Enter your height in meters: "))
fav_number = int(input("Please Enter your favourite number: "))

print("\n Thank you! Here is the information we collected:\n")

print(f"Name: {name} (Type: {type(name)},")
print(f"Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)},")
print(f"Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)},")
print(f"Memory Address: {id(height)})")
print(f"Favourite Number: {fav_number} (Type: {type(fav_number)},")
print(f"Memory Address: {id(fav_number)})\n")

birth_year = 2025 - age
print(f"Your birth_year is appoximately:\n{birth_year} (based on your age of {age}")
      
print("Thank you for using the personal Data Collector. Goodbye!")      

      

