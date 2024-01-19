'''
    Realizado por: Jose Daniel Salazar Briseño
    Grupo: IDGS-803
'''

#Inicio de la clase
class torre:
    numero = 0

    #definicion del constructor
    def __init__(self, a):
        self.numero = a

    #Función para contruir la torre de asteriscos
    def armarTorre(self):
        x = 1                       #Se define una variable para controlar el while
        while x <= self.numero:     
            print("* " * x)         #Se imprime un asterico multiplicado por el valor actual de x que es la vuelta en la que va el ciclo
            x+=1

#Función main
def main():
    num = int(input("Dame el valor del numero: "))  #Solicitamos la cantidad de filas de la torre
    obj = torre(num)                                ##Creamos objeto de la clase y le pasaos el valor
    obj.armarTorre()                                #Se llama el metodo que crea la torre

if __name__ == "__main__":
    main()