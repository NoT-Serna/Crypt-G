from socket import *
import sys

IPServidor = "localhost"
puertoServidor = 9098

#se declaran e inicializan los valores del socket del cliente
socketCliente = socket(AF_INET, SOCK_STREAM)
socketCliente.connect((IPServidor, puertoServidor))

direccionServidor = "localhost"
puertoServidor2 = 9099

prueba_de_conexion= socket(AF_INET, SOCK_STREAM)


#Generamos un nuevo socket
socketServidor = socket( AF_INET, SOCK_STREAM )
#Establecemos la conexion
socketServidor.bind( (direccionServidor, puertoServidor2) )
socketServidor.listen()
corriendo=True
#CLIENTE
while corriendo==True:
    #Se establece conexion de este pivote al cliente
    socketConexion, addr = socketServidor.accept()
    print("Conectado con un cliente", addr)
    mensajeRecibido = socketConexion.recv(4096)
    while True:
        print(mensajeRecibido)
        #enviamos mensaje a servidor
        socketCliente.send(mensajeRecibido)
        #recibimos mensaje
        respuesta = socketCliente.recv(4096)
        if respuesta.decode()=="":
            break
        print(respuesta)
        socketConexion.send(respuesta)
        mensajeRecibido = socketConexion.recv(4096)
        
    corriendo=False
    socketCliente.send(mensajeRecibido)
    
