# * pattern in python

# n = 7
# for i in range(n):
#     print(i)
#     for j in range(i):
#         print('*' , end=" ")
#     print()

# Diamond pattern

for i in range(5):
    print(' ' * (5 - i - 1) + '* ' * (i +1))

for i in range(5 - 2 , -1 , -1):
    print(' ' * (5 - i - 1) + '* ' * (i +1))







   