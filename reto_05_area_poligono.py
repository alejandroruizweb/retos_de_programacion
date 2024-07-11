"""/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */"""

def calcular_area(poligono, base, altura):
    if poligono == 't':
        area = (float(base) * float(altura) / 2)
    elif poligono == 'c':
        area = float(base) * float(base)
    elif poligono == 'r':
        area = float(base) * float(altura)
    else:
        area = False
        print("Ha habido un error al introducir los datos.\nRecuerde indicar el polígono: triangulo : t, cuadrado : c o rectángulo : r.\n También ha de incicar la base y la altura del polígono.")
    print(area)

while True:
    print("Para salir en cualquier momento introduzca q.")
    poligono = input("Introduzca el tipo de polígono. Si es triángulo : t, si es cuadrado : c y si es rectángulo : r: ")
    if poligono == 'q':
        break
    elif poligono == 'c':
        base = input("Introduzca la medida en cm de uno de sus lados: ")
        altura = 0
        if base == 'q':
            break
    else:
        base = input("Introduzca la base del polígono en cm: ")
        if base == 'q':
            break
        altura = input("Introduzca la altura del polígono en cm: ")
        if altura == 'q':
            break
    calcular_area(poligono, base, altura)