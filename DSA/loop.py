# n = int(input())

# sum = 0
# for i in range(n):
#     sum+=i+1

# print(sum)


# range(start,end,step)

for i in range (2,8,2):
    print(i)


# for loop
for i in range(5): # iterates from 0 to 4
    print(i)
for i in range(1, 10, 2): # iterates from 1 to 9 with a step of 2
    print(i)
for char in "Hello": # iterates through each character in the string
    print(char)
for num in [1, 2, 3, 4, 5]: # iterates through each element in the list
    print(num)
x = [6, 7, 8, 9, 10]
for i in range(len(x)):
    print(x[i]) # prints each element of the list using its index

for i, element in enumerate(x): # iterates through the list with index and element
    print("Index:", i, "Element:", element)

# while loop
count = 0
while count < 5: # continues until condition is false
    print(count)
    count += 1 # increments count by 1 in each iteration