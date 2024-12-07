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


#Generacion de parones con ciclos

#Triangulo de numeros

# n=int(input("Indicame el numero de pisos que tendra el triangulo"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#piramide invertida con piramide de espacios
# m=int(input("Indicame el numero de pisos que tendra el triangulo"))
# for i in range(m):
#     for j in range(1,m-i+1):
#         print(j,end=" ")
#     print("  "*(2*i),end="")
#     for j in range(m-i,0,-1):
#         print(j,end=" ")
#     print()        
    



#Tablero de ajedres

# n=8
# for i in range(n):
#     for j in range(n):
#         if(i+j)%2==0:
#             print("⬛",end="")
#         else:
#             print("⬜",end="")
#     print() 


#Hacer trasposicion de matrices

matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
traspuesta=[[0]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        traspuesta[j][i]=matriz[i][j]

for fila in traspuesta:
    print(fila)