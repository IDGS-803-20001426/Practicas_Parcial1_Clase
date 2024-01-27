function enviarFormulario() {
    document.getElementById("error").innerHTML = ""
    var formulario = document.getElementById('form-cine');
    var formData = new FormData(formulario);

    fetch('/procesar_formulario', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {

        if (data.estatus == "error"){
            document.getElementById("error").innerHTML = data.mensaje
            return;
        }

        document.getElementById('cant-pagar').value = data.mensaje;
        document.getElementById('nom-comprador').value = data.comprador;
    })
    .catch(error => document.getElementById("error").innerHTML=error);
}

function limpiarCampos(){
    document.getElementById('nombre').value = "";
    document.getElementById('cant-compradores').value = "";
    document.getElementById('cant-boletos').value = "";
    document.getElementById('cant-pagar').value = "";
    document.getElementById('nom-comprador').value = "";
    document.getElementById('error').innerHTML = "";
}