document.getElementById('id_imagen').setAttribute('accept', 'image/*')
var error = $('.errorlist').css({'color': 'red', 'font-size': '25px'})

var contador = document.querySelectorAll('p')
document.getElementById('id_birth_date').setAttribute('hidden', '')

contador.forEach((element, index)=>{
    if (index == 13){
        element.setAttribute('id', 'fecha')
    }
    if (index == 11){
        element.setAttribute('id', 'insert_municipio')
    }
})

// creo un nuevo label y un input para sobreescribir el que viene por defecto
var datepicker = `<label for='id_birth_date'> Birth Date </label>
                  <input type='text' name='birth_date' id='id_birthdate' required class='form-control'>`

// inserto el input y el label en el html 
$('#fecha').html(datepicker)
// le agrego el datepicker al campo que acabo de crear con el id "id_birth_date"
$('#id_birthdate').datepicker()

document.getElementById('id_birthdate').setAttribute('placeholder', 'Press here')

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
        

// insertar select en blanco de municipios
var municipio = `<label for='id_municipio'> Municipio </label>
                 <select id='id_municipio' name='municipio' class='form-control' required>
                 <option value=0> --------- </option>`

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


