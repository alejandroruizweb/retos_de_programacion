"""/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */"""
def anagrama(str1, str2):
	len_str1 = len(str1)
	len_str2 = len(str2)
	x = 0
	if len_str1 != len_str2:
		print("Las palabras tienen una longitud diferente.")
		return False
	elif str1 == str2:
		print("Son la misma palabra.")
		return False
	elif str1 == '' or str2 == '':
		print("Alguna palabra está vacía.")
		return False
	while x < len_str1:
		cuenta_compara_caracter(str1[x], str1, str2)
		x += 1


def salir(q):
	if q == 'q':
		quit()
def cuenta_compara_caracter(char, str1, str2, x=0, y=0):
	"""Cuenta cuantas veces está ese caracter en una cadena."""
	x = 0
	y = 0
	while y < len(str1):
		if char == str1[y]:
			x += 1
		y += 1
	final_x = x
	x = 0
	y = 0
	while y < len(str2):
		if char == str2[y]:
			x += 1
		y += 1
	final_x2 = x
	if final_x != final_x2:
		print("No es un anagrama.")
		return False

while True:
	print("\nVamos a comprobar si dos palabras son anagramas:")
	print("(Para salir teclee 'q' en cualquier momento)")
	str1 = input("Introduzca una palabra: ")
	salir(str1)
	str2 = input("Introduzca la segunda palabra: ")
	salir(str2) 
	anagrama(str1, str2)
	