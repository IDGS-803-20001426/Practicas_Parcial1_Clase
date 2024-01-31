from flask import Flask, render_template,request, jsonify
import Ejercicio3_Forms
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
    dist_form=Ejercicio3_Forms.UsersForm(request.form)
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


if __name__=="__main__":
    app.run(debug=True)