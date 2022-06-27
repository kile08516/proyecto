
from Computadora import *

computadora1=Computadora("encendido","apagado")
print(computadora1.ine)
print(computadora1.nombre)
computadora1.marca()
computadora1.color()

raton1=Raton("tipo_entrada","conexion")
print(raton1.tipo_entrada())
print(raton1.conexion())
print(raton1.conectar())
print(raton1.esconectar())
mi_archivo=open("persona.txt","w")
try
    mi_archivo.write(f"esta es una coputadora {raton1.nombre}n")
    mi_archivo.write(f"otra {raton1.nombre}n")
finally:
    mi_archivo.close()


