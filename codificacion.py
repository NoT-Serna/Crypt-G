#Funcion que recibe una cadena y devuelve un diccionario con los caracteres de esta junto a la frecuencia con la que aparecen en la cadena
def frecuencias(cadena):
    contador=0
    caracteres=[]
    repeticiones=[]
    
    while cadena!="":
        caracter=cadena[0]
        contador=0
        for i in cadena:
            if i==caracter:
                contador+=1
        caracteres.append(caracter)
        repeticiones.append(contador)
        cadena=cadena.replace(caracter,"")
    tupla=(caracteres, repeticiones)
    return tupla

#Objeto arbol binario con funcion insert
class Arbol():
    def __init__(self, valor, letra):
        self.valorRaiz=valor
        self.letra=letra
        self.left=None
        self.right=None

    def imprimirInOrden(self):
        if self.left != None:
            self.left.imprimirInOrden()
        else:
            print(" _", end="")

        print (self.letra, end="")

        if self.right != None:
            self.right.imprimirInOrden()
        else:
            print("_ ", end="")

    def imprimirPostOrden(self):
        if self.left != None:
            self.left.imprimirInOrden()
        else:
            print(" _", end="")

        if self.right != None:
            self.right.imprimirInOrden()
        else:
            print("_ ", end="")

        print (self.letra, end="")


    def agregar_nodoPrivado(self, valor, raiz, letra):
        if valor < raiz.valorRaiz:
            if raiz.left != None:
                self.agregar_nodoPrivado(valor, raiz.left, letra)
            else:
                raiz.left=Arbol(valor, letra)
        else:
            if raiz.right!=None:
                self.agregar_nodoPrivado(valor, raiz.right, letra)
            else:
                raiz.right=Arbol(valor, letra)
    def agregar_nodo(self, valor, letra):
        self.agregar_nodoPrivado(valor, self, letra)

    def agregar_arbol_derecha(self, arbol):
        self.right=arbol
    def agregar_arbol_izquierda(self, arbol):
        self.left=arbol
    def left_node(self):
        return self.left
    def right_node(self):
        return self.right

#Funcion que encuentra el indice del elemento minimo
def minimo(lista):
    pivote=9999999999
    indice=-1
    for i in range (0, len(lista)):
        if lista[i]<pivote:
            pivote=lista[i]
            indice=i
    return indice

#Funcion que crea un arbol a traves de codificacion de Huffman usando el grafo con frecuencias creado a partir de la cadena recibida
def huffman(grafoFrecuencias):
    caracteres=grafoFrecuencias[0]
    frecuenciass=grafoFrecuencias[1]
    arboles=[]
    
    for i in range (0, len(caracteres)):
        Arbol1=Arbol(frecuenciass[i],caracteres[i])
        arboles.append(Arbol1)
    #YA ESTA CREADA CADA LETRA COMO NODO/ARBOL JUNTO A SU FRECUENCIA, FALTA UNIRLOS YA A LO HUFFMAN
    #letras=len(arboles)
    while(len(arboles)>1):
        arbol1=arboles.pop(minimo(frecuenciass))
        frecuenciass.pop(minimo(frecuenciass))
        arbol2=arboles.pop(minimo(frecuenciass))
        frecuenciass.pop(minimo(frecuenciass))
        Arbol3=Arbol(arbol1.valorRaiz+arbol2.valorRaiz, arbol1.valorRaiz+arbol2.valorRaiz)
        Arbol3.agregar_arbol_izquierda(arbol1)
        Arbol3.agregar_arbol_derecha(arbol2)
        arboles.append(Arbol3)
        frecuenciass.append(Arbol3.valorRaiz)
    arbolHuffman=arboles[0]
    return arbolHuffman

#Funcion que recibe un arbol de huffman y devuelve una codificacion de huffman
def codificacion_huffman(a_huffman):
    return codificacion_huffman_interna(a_huffman, "")

#Funcion interna que recibe un arbol/nodo y un codigo y retorna una letra y su codigo
def codificacion_huffman_interna(arbol, codigo):
    cod_left=codigo+"0"
    cod_right=codigo+"1"
    codificaciones=[]
    if arbol.left_node()!=None:
        codificaciones.extend(codificacion_huffman_interna(arbol.left_node(), cod_left))
    else:
        letra=arbol.letra
        codigo=codigo
        return (letra, codigo)
    if arbol.right_node()!=None:
        codificaciones.extend(codificacion_huffman_interna(arbol.right_node(), cod_right))
    return codificaciones

#Funcion que codifica un mensaje dado
def codificacion_mensaje(mensaje):
    #recibir mensaje, volverlo lista de frecuencias, crear su arbol de huffman, su codigo de huffman y la lista en la que está guardado cada caracter junto a su
    #codificacion convertirla en un diccionario tomando como keys las letras y como values los codigos, el siguiente paso es ir buscando cada letra de la cadena
    #en el diccionario y añadiendo su codificacion en una cadena vacia, una vez terminado esto, se toma el ultimo numero que haya quedado en la cadena y se envia
    #al inicio, luego en una cadena aparte se debe ir guardando intercaladas las letras de la cadena junto a las frecuencias invertidas, al final concatenar estas 
    #dos  cadenas y lista la codificacion
    diccionario={}
    codificado=""
    freq_inv=[]
    freq_mensaje=[]
    intercalado=""
    intercalado2=""
    mitad=[]
    letras_y_frecuencias=frecuencias(mensaje)
    letras_mensaje=letras_y_frecuencias[0]
    for i in letras_y_frecuencias[1]:
        freq_mensaje.append(i)
    arbolin=huffman(letras_y_frecuencias)
    codificacion=codificacion_huffman(arbolin)
    for i in range(0, len(codificacion)):
        if i%2==0:
            diccionario[codificacion[i]]=codificacion[i+1]
    for i in mensaje:
        codificado+=str(diccionario[i])
    ultimo=codificado[len(codificado)-1:len(codificado)]
    codificado=ultimo+codificado[0:len(codificado)-1]

    while len(freq_mensaje)>0:
        freq_inv.append("_"+str(freq_mensaje.pop())+".")
    
    
    indice=len(letras_mensaje)//2
    for i in range ((len(letras_mensaje))//2, len(letras_mensaje)):
        mitad.append(letras_mensaje.pop(indice))
    for i in range(0, len(mitad)):
        if i<len(letras_mensaje):
            intercalado2+=letras_mensaje[i]
        intercalado2+=mitad[i]
    for i in range (0, len(intercalado2)):
        intercalado+=intercalado2[i]
        intercalado+=str(freq_inv[i])
    codificacion_completa=codificado+intercalado+str(len(codificado))+str((len(str(len(codificado)))))
    return codificacion_completa

#Funcion que decodifica un mensaje dado
def decodificacion_mensaje(cadena):
    suma=0
    codificacion=""
    l_y_f=""
    letras=""
    freq_inv=""
    bool_frecuencia=False
    frec_larga=""
    mensaje=""
    freq_inv_lista=[]
    freq_lista=[]
    letras_lista=[]
    mitad=[]
    principio=[]
    diccionario={}
    cifras=int(cadena[len(cadena)-1])
    for i in range(0, cifras):
        digito=cadena[len(cadena)-2-i]
        suma+=int(digito)*(10**i)
    for i in range(0, suma):
        codificacion+=cadena[i]
    for i in range(suma, len(cadena)):
        l_y_f+=cadena[i]
    digito=codificacion[0]
    codificacion=codificacion[1:len(codificacion)]+digito
    for i in range(0, len(l_y_f)-(cifras+1)):
        if l_y_f[i]=="_":
            bool_frecuencia=True
            frec_larga+=l_y_f[i]
        else:
            if l_y_f[i]!=".":
                if bool_frecuencia==True:
                    frec_larga+=l_y_f[i]
                else:
                    letras+=l_y_f[i]
        if l_y_f[i]==".":
            bool_frecuencia=False
            frec_larga+=l_y_f[i]
            freq_inv+=frec_larga
            frec_larga=""
    
    bool_frecuencia=False
    frec_larga=""
    for i in range(0,len(freq_inv)):
        if freq_inv[i]==".":
            bool_frecuencia=False
            freq_inv_lista.append(int(frec_larga))
            frec_larga=""
        if bool_frecuencia==True:
            frec_larga+=freq_inv[i]
        if freq_inv[i]=="_":
            bool_frecuencia=True
    for i in range(0, len(freq_inv_lista)):
        freq_lista.append(freq_inv_lista.pop())
    for i in range (0, len(letras)-1):
        if i%2==0:
            principio.append(letras[i])
        else:
            mitad.append(letras[i])
    mitad.append(letras[len(letras)-1])
    letras_lista=principio+mitad
    tupla=(letras_lista, freq_lista)
    emparejar=codificacion_huffman(huffman(tupla))  
    for i in range(0, len(emparejar)):
        if i%2==1:
            diccionario[emparejar[i]]=emparejar[i-1]  
    #YA LO UNICO UNICO UNICOOO QUE FALTA ES USAR EL DICCIONARIO PARA CONVERTIR LA CADENA DE UNOS Y CEROS EN EL MENSAJE  
    c_letra=""
    for i in range(0, len(codificacion)):
        c_letra+=codificacion[i]
        if c_letra in diccionario:
            mensaje+=diccionario[c_letra]
            c_letra=""
    return mensaje
