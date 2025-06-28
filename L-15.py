# Q.1 Find the length of 1D array without len()

size = int(input("Enter array size : "))

arr = []

arr[0] = 10

print("Enter array Element : ")

# loop

print(arr)

for i in range(size):
    val = int(input(f"a[{i}] = "))
    aee.append(val)

# count length manually

print(len(arr))

length = 0

for _ in arr:
    length += 1

print(length)

# Q.2 Find the averageof a 1D array.

size = int(input("enter size of array : "))

arr = []

print("Enter array Element : ")

for i in range(size):
    val = int(input(f"a[{i}] = "))
    arr.append(val)

# calculate the average

total = 0
length = 0

for val in arr:
    total += val
    length += 1

average = total/length
print("average of an array: " , average)    
