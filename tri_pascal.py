print ("Triangulo de Pascal")

# Funcion que calcula el factorial.
def factorial(n):
    fc = 1    # f es una variable auxiliar para ayudar a el calculo del numero a partir de n.
    while n > 0:    # Si n es mayor que 0 hara los calculos en cuenta regresiva.
        fc = fc * n    # f se multiplicara por el numero mayor e ira aumentando con n en disminucion.
        n = n-1    # n se quita 1 en cada ciclo.
    return (fc)    # Se retorna el valor f al salir del ciclo.

# Función que calcula el triangulo de pascal.
def tri_pascal(n):
    linea = list()    # Se crea una lista vacía.
    for k in range(n+1):    # Para k entre el intervalo 0 a n, sin contar n.
        coeficiente = factorial(n) // (factorial(k)*factorial(n-k))    # Calcula la combinatoria y la guarda en coeficiente.
        linea.append(coeficiente)    # Se agrega a la lista el coeficiente obtenido.
    if (n < 0):    # Si n es menor que cero.
        triangulo.reverse()    # Se da vuelta la lista traingulo que tiene las lineas con los coeficientes con los grados n.
        return triangulo    # Se retorna la lista con las listas obtenidas.
    else:
        triangulo.append(linea)    # Sino, se agrega a la lista triangulo la linea.
        return tri_pascal(n-1)    # Se retorna la función con n menos 1.

triangulo = list()    # Se crea una función vacía.
n = int(input("Ingrese n:  "))    # Se pide n.
if n < 0:
    print("n debe ser mayor o igual a cero.")
else:
    for elemento in tri_pascal(n):    # Para elemento en la lista retornada se muestran sus sublistas con los coeficientes.
        print(elemento)
