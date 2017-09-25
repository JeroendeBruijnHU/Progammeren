def convert(graden_celcius):
    celcius = (graden_celcius * 1.8) + 32
    return celcius


for temperatuur in range(-30,40,10):
    fahrenheit = convert(temperatuur)


print('{:3}:{:3}'.format(celsius, fahrenheit))





