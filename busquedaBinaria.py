#busqueda binaria
import math

elementos=[1,3,4,5,6,7,10,13,16,17,23,40]

class Resultado():
    exito=True
    def __init__(self,indice):
        self.indice=indice

    def setExito(self,exito):
        self.exito=exito

    def setIndex(self,index):
        self.indice=index
        
    def wasNumberFounded(self):
        return self.exito

    def getIndex(self):
        return self.indice

def preguntarNumero():
    while (True):
        try:
            numero=(input('Ingrese un Numero para Ejecutar la busqueda Binaria:'))
            if(numero=='SALIR'):
                return None

            numero=int(numero)
            
            return numero
        except:
            print('ERROR EN EL INGRESO DEL NUMERO')
    

def BuscarCoincidencia(numeroABuscar,centro,izq,derecha,repeticiones):
    if(numeroABuscar<elementos[0]):
       return 'F0'

    if(numeroABuscar>elementos[len(elementos)-1]):
        return f'F{len(elementos)}'
       
    if(numeroABuscar==elementos[centro]):
        return centro

    if(numeroABuscar==elementos[izq]):
        return izq

    if(numeroABuscar==elementos[derecha]):
        return derecha

    if((derecha-izq)==1):
        return -1

    if(repeticiones>len(elementos)):
        return -2

    

def busquedaBinaria(numeroABuscar):
    #terminar=False

    repeticiones=1
    izq=0
    derecha=len(elementos)-1

    while(True):
        
        centro=math.ceil((derecha-izq)/2)+izq

        resultado=BuscarCoincidencia(numeroABuscar,centro,izq,derecha,repeticiones)

        if(resultado!=None):
            try:
                #el numero se encontro entre las opciones
                #       o al menos esta dentro del rango de las opciones
                resultado=int(resultado)
                res=Resultado(resultado)
                
                if(resultado==-1):
                    #el elemento deberia estar en la posicion del la derecha
                    #   en el contexto de los limites establecidos de la busqueda
                    #   (no se refiere a la derecha absoluta del array sino a la
                    #    relativa de la comparacion actual)
                    res.setIndex(derecha)
                    res.setExito(False)
                print('Numero de repeticiones:',repeticiones)
 
            except Exception:
                #no se encontro pero esta fuera de los limites del array
                resultado=int(resultado[1:])
                res=Resultado(resultado)
                res.setExito(False)

            return res
        
        if(numeroABuscar>elementos[centro]):
            #debe estar en el lado derecho a partir del centro
            izq=centro
        else:
            #debe estar en el lado izquierdo a partir del centro
            derecha=centro

        repeticiones+=1

def MensajesDePosicion(resultado):
    if(resultado==0):
        print('AL INICIO DEL ARRAY')
        return 
    if(resultado==len(elementos)):
        print('AL FINAL DEL ARRAY')
        return 
    print(f'EN MEDIO DE    {elementos[resultado-1]}   y   {elementos[resultado]}')        
    
def makeBinarySearch(numero):
    res=busquedaBinaria(numero)
    resultado=res.getIndex()
    
    if(res.wasNumberFounded()):
        print(f'EL NUMERO ESTA EN LA POSICION[{resultado}]={elementos[resultado]}')
        return
    
    print(f'NO SE ENCONTRO EL NUMERO, SIN EMBARGO, DEBERIA OCUPAR EL LUGAR:  {resultado}')
    MensajesDePosicion(resultado)
     
    
    #print('HUBO UN ERROR EN MI ALGORITMO')

while(True):
    
    print(f'elementos:{elementos}')

    numero=preguntarNumero()

    if(numero==None):
        print('\nHAS SALIDO DEL PROGRAMA\n')
        break
    
    makeBinarySearch(numero)

    print('\n=======\n')

"""
num buscar=4


1,3,5,6,7,9,10,16,19,20

1,3,5,6,7

1,3,5

3,5

1,3,4,5,6,7,9,10,16,19,20

1,3,4,5,6,7
"""
