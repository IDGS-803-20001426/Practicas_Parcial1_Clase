'''
    Realizado por: Jose Daniel Salazar Briseño
    Grupo: IDGS-803
'''

#Definicion de la clase
class listaNumeros:
    longLista = 0
    lista = []
    pares = []
    impares = []

    #Definicion del constructor
    def __init__(self, a):
        self.longLista = a

    #Método para leer la lista de numeros
    def leerLista(self):
        x = 1                                                           #Se define una variable para controlar el while
        while x <= self.longLista:
            self.lista.append(input("Dame el valor {} ".format(x)))     #Leemos cada valor y lo almacenamos en la lista
            x+=1                                                        #Aumentamos el contador
        self.lista.sort()                                               #Ordenamos la lista

    #Función para catalogar números pares e impares
    def mostrarParesImpares(self):
        for valor in self.lista:            #Ciclo para recorrer la lista
            if int(valor)%2 == 0:           #Con el operador % pregunntamos si es par
                self.pares.append(valor)    #Si se cumple metemos el numero en la lista pares
            else:
                self.impares.append(valor)  #Si no se cumple lo metemos a impares
        
        #Se impremen los numeros pares con un ciclo for
        print("Valores Pares")
        for valor in self.pares:
            print(valor)

        #Se imprimen los números impares con un for 
        print("Valores Impares")
        for valor in self.impares:
            print(valor)

    #Función para verificar cuantas veces se repite un número
    def contarRepeticiones(self):
        conteo = {}                 #Definimos un diccionario
        for valor in self.lista:    #Ciclo for para recorrer la lista de valores
            if valor in conteo:     #If para verificar si el numero ya esta dentro del diccionario
                conteo[valor] += 1  #Si es asi solo incrementamos en uno
            else:
                conteo[valor] = 1   #Si no significa que es la primera vez que se encuentra el número

        #Se imprime el diccionario con un ciclo for
        print("Número y frecuencia de repeticiones:")
        for num, rep in conteo.items():
            print("El número {} se repite {} veces".format(num, rep))
   
#Función main
def main():
    cantidadNumeros = int(input("¿Qué cantidad de numeros deseas ingresar? "))  #Preguntamos la cantidad de numeros
    obj = listaNumeros(cantidadNumeros) #Creamos el objeto y le pasamos la cantidad
    #Se mandan a llamar los tres metodos que realizan las acciones solicitadas
    obj.leerLista()
    obj.mostrarParesImpares()
    obj.contarRepeticiones()
    
if __name__ == "__main__":
    main()