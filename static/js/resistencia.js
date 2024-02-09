var columnas = []

function enviarFormulario() {
    var c = '';
    document.getElementById("error").innerHTML = ""
    var formulario = document.getElementById('form-resistencia');
    var formData = new FormData(formulario);
    console.log("enviando")
    fetch('/procesarFormResistenca', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {

        if (data.estatus == "error"){
            document.getElementById("error").innerHTML = data.mensaje
            return;
        }

        columnas.push("<tr>"
        + "<td class='"+data.color1+" text-white'>"+data.color1+"</td>"
         +"<td class='"+data.color2+" text-white'>"+data.color2+"</td>"
         +"<td class='"+data.color3+" text-white'>"+data.color3+"</td>"
         +"<td class='"+data.tolerancia+" text-white'>"+data.tolerancia + (data.tolerancia == "dorado" ? " 5%" : " 10%") +"</td>"
         +"<td>"+data.valorReal+"</td>"
         +"<td>"+data.valorMaximo+"</td>"
         +"<td>"+data.valorMinimo+"</td>"
     +"</tr>");

        document.getElementById('bodyTabla').innerHTML = "";

        columnas.forEach(col => {
            c += col;
        })

        document.getElementById('bodyTabla').innerHTML = c;
        
    })
    .catch(error => document.getElementById("error").innerHTML=error);
}