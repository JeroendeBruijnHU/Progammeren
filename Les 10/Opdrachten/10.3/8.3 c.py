#Uitvoer 8_3C:                      #uitkomst is eerst 3 , dan 10
x = 2
y = 5

def fun():
    y = 3
    global x
    x = 1
    print(x*y, end = " ")   #3 * 1  = 3
    return x*y              # x wordt 3,

x = fun()
print(x*y, end = " ")        #2 * 5  = 10