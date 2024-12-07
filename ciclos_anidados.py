#ciclos anidados

# for i in range(3):
#     for j in range(3):
#         print(f"i={i}, j={j}")


#procesamiento de matrices con ciclos anidados

#Ejemplo 1: Iprimir una matriz de forma que quede representada con su representacion matematica

# matriz=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# suma=0
# for fila  in matriz:
#     for elemento in fila:
#         print(elemento,end=" ")
#         suma+=elemento
#     print()
# print(f"Suma total: {suma}")    


# for fila in matriz:
#     for elemento in fila:
#         suma+=elemento
# print(f"suma total: {suma}")

# contador_pares=0
# for fila in matriz:
#     for elemento in fila:
#         if elemento%2==0:
#             contador_pares+=1
# print(f"Hay {contador_pares} numeros pares en la matriz")            