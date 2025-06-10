# Break Statement in python

# for i in  range(1 , 6):
#   if i == 4:
#     break
#   print("For Loop :" , i)

# Continue Statement in python

# for i in range(1 , 6):
#   if i == 4:
#     continue
#   print("Foor Loop : " , i)

# Break and Continue in Nested Loop

# for i in range(1 , 4):
#  for j in range(1 , 2):
#   if j == 2:
#     break
#   print("j loop: " , j)
#  print ("i loop: " , i)

# for i in range(1 , 4):
#     print("i loop: " , i)
#     for j in range(2):
#         if i == 2:
#             break
#         print("j loop: " , j)

# pattern print in python

# pattern 1:- 
# for i in range(1 , 7):
#     for j in range(1 , i):
#         print(f"{j}" , end="")
#     print()

# pattern 2:-
# for i in range(6):
#     for j in range(i , -1 , -1):
#         print(f"{j+1}" , end="")
#     print()

# pattern 3:-
# for i in range(1 , 7):
#     for j in range(i):
#         print(f"{i}" , end="")
#     print()

# pattern 4:-
# for i in range(5):
#     for j in range(i+1):
#         print(f"{5-i}" , end="")
#     print()

# pattern 5:-
# for i in range(5):
#     for j in range(i , -1 , -1):
#         print(f"{5-j}" , end="")
#     print()

# pattern 6:-
for i in range(5):
    for j in range(i+1):
        print(f"{5-j}" , end="")
    print()
