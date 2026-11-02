import math
# list/array

# Sum of list 
# n = int(input("Enter number: "))
# myList = input().split() 
# sum = 0

# for i in range(n):
#     sum += int(myList[i])

# print(sum)

# n = int(input("Enter List: "))
# myList = input().split()

# for i in range(len(myList)):
#     myList[i] = int(myList[i])

# sum for shortcut
# print(sum(myList))

myList = [1,2,232,23,4,4,4,4,3,4,3,5,56,655,34,43,45,33,23, 35]

maxElem=myList[0]
minElem=myList[0]

for i in range(len(myList)):
   if(myList[i] > maxElem):
        maxElem = myList[i]
   if(myList[i] < minElem):
        minElem = myList[i]

print(minElem,maxElem)

## min, max - method for shortcut
print(min(myList))
print(max(myList))

# mynewLIst = []
# for i in range(len(myList)):
#     for j in range(len(myList)):
#         if(myList[i] < myList[j]):
#             temp = myList[i]
#             myList[i] = myList[j]
#             myList[j] = temp

# print(myList)

## sort method
# myList.sort()
# print(myList)

# mean  - sum/lenght
print("mean", sum(myList)/len(myList))

#median - sorted array - if odd middle index value and if even then average of middle two values
myList.sort()
n = len(myList)

print("list",myList)
print("length", n)

if(n%2 == 0):
    # print((myList[(len(myList)/2)-1])/2+(myList[(len(myList)/2)]))
    # print((n//2) - 1)
    print(int((myList[(n//2)-1] + myList[n//2]) / 2))
else:
    print(myList[(n//2)]) ## will give the smallest number so 9.5 will be 9
    # print(len(myList)//2)

# mode - number which has highes t frequency in list
### Approach 1

# maxCount = 0
# maxElem = myList[0]
# for curElem in myList:
#     curCount = 0
#     for eachElem in myList:
#        if(curElem == eachElem):
#             curCount += 1
    
#     if(curCount > maxCount):
#         maxCount = curCount
#         maxElem = curElem

# print("maxElem",maxElem)
# print("maxCount",maxCount)

### Approach 2
maxCount = 0
maxElem = myList[0]
curCount = 1
for i in range(n-1):
    if myList[i] == myList[i+1]:
        curCount += 1
    else:
        if curCount > maxCount:
            maxCount = curCount
            maxElem = myList[i]
        curCount = 1

# if curCount > maxCount: ## - because above will never check the last index
#     maxCount = curCount
#     maxElem = myList[-1]
    
print("maxElem",maxElem)
print("maxCount",maxCount)


## Second Largest - Approach 1
# maxCount = myList[0]
# secondCount = 0

# for i in myList:
#     for j in myList:
#         if(j > maxCount):
#             maxCount = j
#         else:
#             if(j < maxCount and j > secondCount):
#                 secondCount = j

# print("maxCount",maxCount)
# print("secondCount",secondCount)

# Second largest = Approach 2
maxCount = 0
secondCount = 0
for i in myList:
    if(i > maxCount):
        secondCount = maxCount
        maxCount = i
    else:
        if(i < maxCount and i > secondCount):
            secondCount = i

print(secondCount)