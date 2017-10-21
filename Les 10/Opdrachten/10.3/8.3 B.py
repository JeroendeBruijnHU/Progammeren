#Uitvoer 8_3B:                      #uitkomst is D, "3 3"
x = 1
y = 4

def fun():
    x = 2                           #gebruikt x = 1
    global  y
    y = 3                           #gebruikt y = 3
    print(y, end=" ")

fun()                               #uitkomst is 3
print(y, end=" ")                    #uitkomst is 3