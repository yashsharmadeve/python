
# def function(x):
#     base condition
#     if

#     return recursive call 

def fact(x):
    if x == 0 or x == 1:
        return 1
    return fact(x-1)*x # return is important in recursion

# print(fact(3))

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(3)) 
# means 3 times iterate
# starts from highest for above example 3