#importamos librerias
from socket import *
import codificacion
direccionServidor = "localhost"
puertoServidor = 9098

#Generamos un nuevo socket
socketServidor = socket( AF_INET, SOCK_STREAM )
#Establecemos la conexion
socketServidor.bind( (direccionServidor, puertoServidor) )
socketServidor.listen(1)

while True:
    #establecemos la conexion
    socketConexion, addr = socketServidor.accept()
    print("Conectado con un cliente", addr)
    while True:
        #recibimos el mensaje del cliente
        mensajeRecibido = socketConexion.recv(4096).decode()
        mensajeRecibido = codificacion.decodificacion_mensaje(mensajeRecibido)
        print(mensajeRecibido)
        #esta condicion no se cumplira hasta que la cadena sea adios
        if mensajeRecibido == "adios":
            break
        #mandamos mensaje al cliente
        socketConexion.send(codificacion.codificacion_mensaje(input()).encode())

    print("Desconectado el cliente", addr)
    #cerramos conexion
    socketConexion.close()
    break