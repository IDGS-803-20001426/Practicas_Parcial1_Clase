from flask import Flask, render_template,request, jsonify
from io import open
import Form
import Form_Resistencia
import FormArchivo
from math import sqrt, pow

app = Flask(__name__)

@app.route("/")
def index():
    escuela="UTL"
    alumnos = ["Mario", "Pedro", "Luis", "Dario"]
    return render_template("index.html", escuela=escuela, alumnos=alumnos)

@app.route("/formulario1")
def formulario():
    return render_template("formulario1.html")

@app.route("/operaciones", methods=["GET", "POST"])
def mult():
    if request.method == "POST":
        num1= request.form.get("n1")
        num2= request.form.get("n2")
        operacion = request.form.get("operacion")

        if operacion == "suma":
            resultado = str(int(num1)+int(num2))
        elif operacion == "resta":
            resultado  = str(int(num1)-int(num2))
        elif operacion == "multiplicacion":
            resultado = str(int(num1)*int(num2))
        elif operacion == "division":
            resultado = str(int(num1)/int(num2))
        
        return "<h1>El resultado de la {} es: {} </h1>".format(operacion, resultado)





@app.route("/cinepolis")
def cinepolis():
    return render_template("cinepolis.html")

@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    nombre = request.form.get("nombre")
    cantCompradores = request.form.get("cant-compradores")
    tarjeta = request.form.get("tarjeta")
    cantBoletos = request.form.get("cant-boletos")

    if (nombre == "" or cantCompradores == "" or tarjeta == "" or cantBoletos == ""):
        return jsonify({'estatus' : "error", 'mensaje': 'La información esta incompleta'})

    if(int(cantCompradores) <= 0):
        return jsonify({'estatus' : "error", 'mensaje': 'Los compradores no pueden ser {}'.format(cantCompradores)})
    
    if(int(cantBoletos) <= 0):
        return jsonify({'estatus' : "error", 'mensaje': 'Los boletos no pueden ser {}'.format(cantBoletos)})

    if( int(cantBoletos) > (int(cantCompradores)*7) ):
        return jsonify({'estatus' : "error", 'mensaje': 'Solo se permite comprar {} boletos'.format(int(cantCompradores)*7)})

    subTotal = int(cantBoletos)*12

    if(int(cantBoletos) > 5):
        total = subTotal - (subTotal*0.15)
    elif(int(cantBoletos) >= 3 and int(cantBoletos) <= 5):
        total = subTotal - (subTotal*0.10)
    else:
        total = subTotal

    if(tarjeta == "si"):
        total = total - (total*0.10)

    return jsonify({'estatus': 'success' ,'comprador': nombre,'mensaje': '${0:.2f}'.format(total)})


@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    x1=0
    x2=0
    y1=0
    y2=0
    dist_form=Form.UsersForm(request.form)
    if request.method == 'POST':
        x1=dist_form.x1.data
        x2=dist_form.x2.data
        y1=dist_form.y1.data
        y2=dist_form.y2.data

    distancia = sqrt(  ( (float(x2)-float(x1)) )**2 + (float(y2)-float(y1))**2 )

    print("x1: {}".format(x1))
    print("x2: {}".format(x2))
    print("y1: {}".format(y1))
    print("y2: {}".format(y2))
    print("primera parte: {}".format( ( int (x2) - int(x1) )**2 ) )
    print("segunda parte: {}".format((float(y2)-float(y1))**2))

    return render_template("formDistancia.html", form=dist_form, distancia=distancia)

@app.route("/resistencia", methods=["GET", "POST"])
def resistencia():
    dist_Selec = Form_Resistencia.UsersForm(request.form)
    if request.method == 'POST':
        color1=dist_Selec.color1.data
        color2=dist_Selec.color2.data
        color3=dist_Selec.color3.data
        tolerancia=dist_Selec.tolerancia.data
    return render_template("resistencia.html", form=dist_Selec);

@app.route("/procesarFormResistenca", methods=["GET", "POST"])
def formResistencia():
    color1 = request.form.get("color1")
    color2 = request.form.get("color2")
    color3 = request.form.get("color3")
    tolerancia = request.form.get("tolerancia")
    obj = Resistencia(color1, color2, color3, tolerancia)
    return obj.calcularValor()

class Resistencia:
    color1 = ''
    color2 = ''
    color3 = ''
    tolerancia = ''
    diccionarioColores = {'negro' : 0 , 'cafe' : 1, 'rojo': 2, 'naranja': 3, 'amarillo': 4, 'verde': 5, 'azul': 6, 'violeta': 7, 'gris': 8, 'blanco':9}
    diccionarioColores2 = {'negro' : 1 , 'cafe' : 10, 'rojo': 100, 'naranja': 1000, 'amarillo': 10000, 'verde': 100000, 'azul': 1000000, 'violeta': 10000000, 'gris': 100000000, 'blanco':1000000000}
    diccionarioColores3 = {'dorado' : .05, 'plata' : .1}

    #Definicion del constructor
    def __init__(self, a,b,c,d):
        self.color1 = a
        self.color2 = b
        self.color3 = c
        self.tolerancia = d

    def calcularValor(self):
        valorReal = int(str(self.diccionarioColores[self.color1]) + str(self.diccionarioColores[self.color2])) * self.diccionarioColores2[self.color3]
        valorMaximo = valorReal + (valorReal * self.diccionarioColores3[self.tolerancia])
        valorMinimo = valorReal - (valorReal * self.diccionarioColores3[self.tolerancia])
        
        print("valor {}, maximo {}, minimo {}".format(valorReal, valorMaximo, valorMinimo))

        return jsonify({
                'estatus': 'success' , 
                'valorReal': valorReal, 
                'valorMaximo': valorMaximo, 
                'valorMinimo': valorMinimo, 
                "color1": self.color1, 
                "color2": self.color2, 
                "color3": self.color3, 
                "tolerancia": self.tolerancia 
            })

dist_Archivo_Registro = FormArchivo.FormArchivoRegistro()
dist_Archivo_Busqueda = FormArchivo.FormArchivoBusqueda()

@app.route("/traductor", methods=["GET", "POST"])
def traductor():
    return render_template("traductor.html", form_registro=dist_Archivo_Registro, form_busqueda=dist_Archivo_Busqueda)

@app.route("/traductor-registrar", methods=["GET", "POST"])
def traductorRegistrar():
    form_registro = FormArchivo.FormArchivoRegistro(request.form)
    mensaje = None  # Inicializamos el mensaje como None

    if request.method == 'POST' and form_registro.validate():
        reg_esp = request.form.get("reg_espanol")
        reg_ingles = request.form.get("reg_ingles")

        obj = Archivo()
        obj.registrar(reg_esp, reg_ingles)

        mensaje = "¡Registrado con éxito!"  # Establecemos el mensaje

    return render_template("traductor.html", form_registro=form_registro, form_busqueda=dist_Archivo_Busqueda, mensaje=mensaje)


@app.route("/traductor-buscar", methods=["GET", "POST"])
def traductorBuscar():
    form_busqueda = FormArchivo.FormArchivoBusqueda(request.form)
    traduccion=''
    if request.method == 'POST' and form_busqueda.validate():
        select_idioma = request.form.get("select_idioma")
        leer_reg = request.form.get("leer_reg")

        obj = Archivo()
        traduccion = obj.buscar(select_idioma, leer_reg)

    return render_template("traductor.html", form_registro=dist_Archivo_Registro, form_busqueda=form_busqueda, traduccion=traduccion)

class Archivo:
    registro_español = ''
    registro_ingles = ''
    busqueda_select = ''
    busqueda_palabrea = ''
    #Definicion del constructor
    def __init__(self):
        pass

    def registrar(self, registro_español, registro_ingles):
        archivo=open("traductor.txt", 'a')
        archivo.write('\n' + registro_español + '-' + registro_ingles)
        archivo.close()
    
    def buscar(self, busqueda_select, busqueda_palabra):
        palabra_traducida=''
        archivo=open("traductor.txt", 'r')
        for lineas in archivo.readlines():
            columnas = lineas.rstrip().split('-')
            if busqueda_select == 'espanol':
                if busqueda_palabra.lower() in columnas[0].lower():
                    palabra_traducida=columnas[1]
                    break           
            
            if busqueda_select == 'ingles':
                if busqueda_palabra.lower() in columnas[1].lower():
                    palabra_traducida=columnas[0]
                    break

        archivo.close()

        if palabra_traducida == '':
            return 'No se encontró la traduccion'
        else:
            return palabra_traducida

if __name__=="__main__":
    app.run(debug=True)