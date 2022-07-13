# Cosmic ray detector by TasfiqulTapu
ARRAY = [0 for _ in range(100)]
condition = True
while condition:
    for i in range(100):
        if ARRAY[i] != 0:
            condition = False
print("Cosmic ray detected")
