#Uitvoer 8_3A:
a = 3

def f(y):
    global a #gebruikt a = 3
    a = 9
    return 2*y + a  #2 keer 0 plus 3
print(a)


#Uitvoer 8_3B:                      #uitkomst is D, "3 3"
x = 1
y = 4

def fun():
    x = 2                           #gebruikt x = 1
    global  y
    y = 3                           #gebruikt y = 3
    print(y, end="")

fun()                               #uitkomst is 3
print(y, end="")                    #uitkomst is 3



#Uitvoer 8_3C:
a = 3

def fun1 ():
    global a
    print("a:", a, end="  ")
    b = 7
    a = 0
    return b

def fun2(y):
    a = y + fun1()
    b = 7
    a += 1
    return a

a = 9
fun2(5)
print("a:", a)