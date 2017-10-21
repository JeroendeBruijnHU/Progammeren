#Uitvoer 8_3A:
a = 3

def f(y):
    global a #gebruikt a = 3
    a = 9
    return 2*y + a  #2 keer 0 plus 3
print(a)