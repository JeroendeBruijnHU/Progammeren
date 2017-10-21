#HOE GA JE NAAR DE GEVANGENIS?
import random


def monopolyworp():
    dice_1 = int(random.randrange(1, 7))
    dice_2 = int(random.randrange(1, 7))

    worp = (dice_1 + dice_2)

    if dice_1 == dice_2:
        print(dice_1, "+", dice_2, "=", worp, ",""dubbel, gooi nog een keer")
    else:
        print(dice_1, "+", dice_2, "=", worp)


monopolyworp()