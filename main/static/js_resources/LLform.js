const form_llamadas = document.getElementById('form-llamadas'); //o
const in_nombre = document.getElementById('in_nombre'); //o
const in_documento = document.getElementById('in_documento');//o
const in_tipo_documento = document.getElementById('in_tipo_documento');//o
const in_sexo = document.getElementById('in_sexo'); //o
const in_edad = document.getElementById('in_edad');
const in_eps = document.getElementById('in_eps'); //o-n
const in_direccion = document.getElementById('in_direccion');
const in_pais = document.getElementById('in_pais');
const in_departamento = document.getElementById('in_departamento');
const in_municipio = document.getElementById('in_municipio');
const in_telefono = document.getElementById('in_telefono');

const numTiposDocumento = 8;
const numSexos = 3;
const numEps = 36;

form_llamadas.addEventListener('submit', function(e){
    e.preventDefault();
    let ban = true;
    let msg = "";
    let preventiveBan = true;
    let preventiveMsg = "";

    if(in_nombre.value.trim() === ""){
        ban = false
        msg += "El nombre no puede estar vacío";
    }

    if(in_documento.value.trim() === ""){
        ban = false;
        msg += "El documento no puede estar vacío";
    }

    if(in_tipo_documento.value < 1 && in_tipo_documento.value > numTiposDocumento){
        ban = false;
        msg += "Compruebe tipo de documento";
    }

    if(in_sexo.value < 1 && in_sexo.value > numSexos){
        ban = false;
        msg += "Compruebe el sexo";
    }

    if(in_edad.value.trim() == ""){
        preventiveBan = false;
        preventiveMsg += "Edad no especificada ¿Esto está bien?";
    }

});
