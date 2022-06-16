
def crear_matriz(M,N):
    return [[0 for j in range (N)]for i in range (M)]
filas=int(input("ponga numero de filas:"))
columnas=int(input("ponga numero de columnas:"))
matriz = crear_matriz(filas,columnas)
print(matriz)