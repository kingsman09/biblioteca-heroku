document.getElementById('id_imagen').setAttribute('accept', 'image/*')

var atributo = document.querySelectorAll('a')
// atributo.setAttribute('id', 'nombre')
console.log(atributo)
atributo.forEach((elemento, index) => {
    if (index == 7 ){
        elemento.setAttribute('id', 'nombre')
    }
})

var href = document.getElementById('nombre')
var nuevo = href.getAttribute('href')
console.log(nuevo)
document.getElementById('perfil_imagen').setAttribute('src', nuevo)


var contador = document.querySelectorAll('p')
console.log(contador)


contador.forEach((element, index)=>{
    if (index == 7){
        element.setAttribute('id', 'insert_municipio')
    }
    if (index == 3){
        element.setAttribute('id', 'celphone_user')
    }
})


$('#id_birth_date').datepicker()


$.datepicker.regional['es'] = {
                closeText: 'Cerrar',
                prevText: '&#x3c;Ant',
                nextText: 'Sig&#x3e;',
                currentText: 'Hoy',
                monthNames: ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
                monthNamesShort: ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'],
                dayNames: ['Domingo','Lunes','Martes','Mi&eacute;rcoles','Jueves','Viernes','S&aacute;bado'],
                dayNamesShort: ['Dom','Lun','Mar','Mi&eacute;','Juv','Vie','S&aacute;b'],
                dayNamesMin: ['Do','Lu','Ma','Mi','Ju','Vi','S&aacute;'],
                weekHeader: 'Sm',
                dateFormat: 'yy-mm-dd',
                yearRange: "-90:+0",
                changeMonth: true,
                changeYear: true,
                firstDay: 1,
                isRTL: false,
                showMonthAfterYear: false,
                yearSuffix: ''};
$.datepicker.setDefaults($.datepicker.regional['es']);


// se guarda en el local storage el nombre del municipio del usuario
localStorage.setItem('muni_id', $('#user_municipio').val())

// se guarda en el local storage el id del municipio del usuario
localStorage.setItem('id', $('#municipio_id').val())


var municipio_actual = localStorage.getItem('muni_id')
var id_municipio = localStorage.getItem('id')

// insertar select en blanco de municipios
var municipio = `<label for='id_municipio'> Municipio </label>
                 <select id='id_municipio' name='municipio' class='form-control' required>
                 <option value=${id_municipio}> ${municipio_actual}</option>`

$('#insert_municipio').html(municipio)



$('#id_departamento').on('change', function(){
    var departamento = $(this).val()
    $.ajax({
        url: `/departamento/?id=${departamento}`,
        type: 'get',
        dataType: 'json',
        data: {
            id_departamento: departamento
        },
        success: function(response){
            var municipios = $.parseJSON(response.dato)
            var insertar = '';

            // se crean los municipios segun el departamento seleccionado
            municipios.forEach(municipio => {
                insertar += `<option value=${municipio.id}> ${municipio.name} </option> `;
            })
            // se insertan los municipios creados en el template
            $('#id_municipio').html(insertar);
        },
        error: function(error){
            console.log(error)
        }
    })
})