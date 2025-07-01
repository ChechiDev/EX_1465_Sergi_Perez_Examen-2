import os
from time import sleep
"""
Escribir un programa en Python que muestre todas las combinaciones posibles de tres dígitos distintos en orden estrictamente creciente, utilizando listas y estructuras de control.

# Requisitos funcionales:
- El programa debe generar todas las combinaciones de tres dígitos (del 0 al 9) sin repetir dígitos y donde cada combinación cumpla que el primer dígito < segundo dígito < tercer dígito. Ejemplo válido: 027 Ejemplo inválido: 272, 321, 999.

- El programa debe preguntar al usuario si desea que las combinaciones se muestren en:

Orden normal (de menor a mayor): 012, 013, 014, ..., 789
Orden invertido (de mayor a menor): 789, 788, ..., 012

- El resultado debe mostrarse en pantalla, separado por comas, en una sola línea.

# ---

# Requisitos técnicos:
No se permite usar itertools, set, sorted, sort(), ni funciones similares de ordenación o filtrado automático.
Solo se debe utilizar listas, bucles for, y estructuras de control como if.
El orden invertido debe implementarse manualmente, sin usar [::-1] ni .reverse().
"""

def print_comb(invert=False):
    """
    Generates and prints all combinations of three distinct digits in ascending or descending order.
    """
    n1 = 0
    n2 = 0
    n3 = 0
    comb = []

    # Lista creciente:
    if invert == False:
        for n1 in range(10):
            for n2 in range(n1 + 1, 10):
                    for n3 in range(n2 + 1, 10):
                            comb.append(str(n1) + str(n2) + str(n3))

        print(comb)

    # Lista decreciente
    if invert == True:
        for n1 in range(9, -1, -1):
            for n2 in range(9, n1, -1):
                    for n3 in range(9, n2, -1):
                            comb.append(str(n1) + str(n2) + str(n3))

        print(comb)

def main():    
    while True:
        os.system("cls")
        print("En qué orden desea ver las combinaciones?\n")
        opts = ["Creciente", "Decreciente"]
        
        for idx, opt in enumerate(opts):
             print(f"{idx + 1}. {opt}")
             
        select = input("\nPor favor, seleccione una opción: ")
        if select == "1":
            os.system("cls")
            print_comb(invert=False)
            break

        elif select == "2":
            os.system("cls")
            print_comb(invert=True)
            break
    
        else:
            print("Opción inválida....")
            sleep(1)
            continue

if __name__ == "__main__":
    main()
