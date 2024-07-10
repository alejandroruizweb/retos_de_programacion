"""/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */"""
fibonacci = []
i = 0

while i < 50:
    """Creamos un bucle para añadir 50 números a la lista."""
    if i == 0:
        """El primer número siempre es un 0."""
        number = 0
        number1 = 0
        fibonacci.append(number)
    elif i == 1:
        """El segundo es un 1."""
        number = 1
        number2 = 1
        fibonacci.append(number)
    else:
        """A partir del tercer número vamos sumando los dos últimos creados."""
        number3 = number1 + number2
        fibonacci.append(number3)
        number1 = number2
        number2 = number3
    i += 1
print(fibonacci)

lista_proporcionada = [
    
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 
    987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 
    121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 
    3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 
    63245986, 102334155, 165580141, 267914296, 433494437, 
    701408733, 1134903170, 1836311903, 2971215073, 4807526976, 
    7778742049
]
if lista_proporcionada == fibonacci:
    print("El ejercicio es correcto")
