"""
Programa que simule una encuesta de 3 productos
    1. Se muestra los nombres de los productos
    2. El usuario ingresa el nombre del producto de su preferencia
    3. El programa acumula la preferencia elegida
    4. Si el nombre ingresado es “Final” finaliza la encuesta
    5. Se muestra como resultados el % de votos de cada producto o según ordenado descendentemente según preferencias
"""

# DEFINIMOS LISTA
productos = [
    {
        'nombre': 'PHP',
        'cantidad': 0
    },
    {
        'nombre': 'Python',
        'cantidad': 0
    },
    {
        'nombre': 'JavaScript',
        'cantidad': 0
    }
]

producto_elegido = ""
while producto_elegido != "Final":
    # LISTAMOS PRODUCTOS
    print("\n---- Encuesta de 3 productos ----")
    for value in productos:
        print("- " + value['nombre'])

    # ELEGIMOS PRODUCTO
    producto_elegido = input("\nElige producto ('Final' para finalizar): ")

    # DETENEMOS SI ESCRIBE FINAL
    if producto_elegido == "Final":
        exit()

    # ACUMULACION DE PRODUCTOS VOTADOS
    for value in productos:
        if(value['nombre'] == producto_elegido):
            value['cantidad'] += 1

    # OBTENEMOS TOTAL DE VOTOS
    total_votos = 0;
    for value in productos:
        total_votos += value['cantidad']

    # RESULTADO DE VOTOS EN PORCENTAJE
    print("\n---- Votos ----")
    for value in productos:
        nombre = value['nombre']
        cantidad = value['cantidad']
        porcentaje = 0
        if total_votos > 0: # Validacion division entre cero, en caso el total de votos sea 0
            porcentaje = (cantidad * 100) / total_votos
        print("- " + nombre + ": " + str(cantidad) + " (" + str(round(porcentaje,2)) + "%)")
