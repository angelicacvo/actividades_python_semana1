import random

def roll_dice():
    return random.randint(1, 6)

# Ejemplo de uso:
result = roll_dice()
print(f"El resultado del lanzamiento es: {result}")
