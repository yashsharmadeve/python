def myFunc1():
    myFunc2()
    print('First Function')

def myFunc2():
    print('Second Function')
    
myFunc1()
myFunc2()

# in callstack they push one by one and works on LIFO.