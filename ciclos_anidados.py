#ciclos anidados

# for i in range(3):
#     for j in range(3):
#         print(f"i={i}, j={j}")


#procesamiento de matrices con cilcos anidados

#Ejemplo 1: Iprimir una matriz de forma que quede representada con su representacion matematica

matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for fila  in matriz:
    for elemento in fila:
        print(elemento,end=" ")
    print()

