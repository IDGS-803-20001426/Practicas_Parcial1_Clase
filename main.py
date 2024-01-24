from flask import Flask, render_template,request

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

if __name__=="__main__":
    app.run(debug=True)