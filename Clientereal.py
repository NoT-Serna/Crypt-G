from socket import *
import sys
import codificacion

IPServidor = "localhost"
puertoServidor = 9099

#se declaran e inicializan los valores del socket del cliente
socketCliente = socket(AF_INET, SOCK_STREAM)
socketCliente.connect((IPServidor, puertoServidor))



while True:
    #escribimos el mensaje
    mensaje = input()
    if mensaje != "adios":
        #enviamos mensaje
        mensaje=codificacion.codificacion_mensaje(mensaje)
        socketCliente.send(mensaje.encode())
        #recibimos mensaje
        respuesta = socketCliente.recv(4096).decode()
        respuesta = codificacion.decodificacion_mensaje(respuesta)
        print(respuesta)
    else:
        mensaje=codificacion.codificacion_mensaje(mensaje)
        socketCliente.send(mensaje.encode())
        #cerramos socket
        socketCliente.close()
        sys.exit()
