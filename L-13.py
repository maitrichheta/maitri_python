# Part:1  Use of Built-in Function in Python

import random

print("<==== Built-in Function on List ====>")

numbers = [4 , 2 , 7 , 9 , 5 , 6]

print("List : " , numbers)

# len()

print("Length Of List : " , len(numbers))

# max() and min()

print("Max Number : " , max(numbers))

print("Min Number : " , min(numbers))

# sum()

print("Sum Of List : " , sum(numbers))

# Part:2 Negative Float Number Operation

print("<==== Part:2 Operation in Negative Value")

num  = float(input("Enter a Negative float Number : "))

# abs()

print("Positive Version From The User : " , abs(num))

# pow()

print("Power of Value : " , pow(num , 10))

# round()

print("Roundof Value :" , round(num))

# Part:3 random List and Its Values / Analysis

print("<=== Random List and Its Values / Analysis ===>")

random_num = random.sample(range(1 , 100) , 5)

print(random_num)

# max() , and min() , sum()

print("Random List: " , random_num)

print ("Random Number max count: " , max(random_num))
print ("Random Number min count: " , min(random_num))
print ("Random Number sum count: " , sum(random_num))

# Part:4 Sort and Reverse a List

print("<=== Sort and Reverse a List ==>")

user_list = list(map(int , input("Enter Number seperated by space : ").split()))

print(user_list)

# sorted()

print("Sorted List Ascending" , sorted(user_list))

# reverse()

print("Reverse value of List : " , list(reversed(user_list)) )