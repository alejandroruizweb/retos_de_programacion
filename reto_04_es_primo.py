"""/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */"""
def one_hundred_prime_number():
    """Función que muestra los números primos del 1 al 100."""
    i = 0
    for is_prime in range (1,101):
        if is_prime <= 3:
            print(is_prime, end=", ")
        else:
            is_prime2 = int(is_prime) - 1
            while (is_prime2) > 1:
                if is_prime % is_prime2 == 0:
                    i = 1
                is_prime2 -= 1 
        if i == 0 and is_prime > 3:
            if is_prime == 97:
                print(is_prime, end=".")
            else:
                print(is_prime, end=", ")
        else:
            i = 0 

while True:
    print("\nPara salir introduzca en cualquier momento 'q'.\nSi quiere ver los números primos del 1 al 100 escriba '100 primos'")
    number = input("Para saber si un número es primo introdúzcalo un número: ")
    if number == 'q':
        break
    elif number == '100 primos':
        one_hundred_prime_number()
        break
    number = int(number)
    if number <= 2:
        print(f"{number} es un número primo.")
    else:
        i = 0
        for is_prime in range(2, number):
            if number % is_prime == 0:
                i = 1
        if i == 1:
            print(f"El número {number} NO es un número primo.")
        else:
            print(f"El número {number} es un número primo.")