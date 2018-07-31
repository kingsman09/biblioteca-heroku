document.getElementById('id_imagen').setAttribute('accept', 'image/*')
var error = $('.errorlist').css({'color': 'red', 'font-size': '25px'})

var contador = document.querySelectorAll('p')

document.getElementById('id_birth_date').setAttribute('hidden', '')



contador.forEach((element, index)=>{
    if (index == 13){
        element.setAttribute('id', 'fecha')
    }
})


var datepicker = `<label for='id_birth_date'> Birth Date </label>
                  <input type='text' name='birth_date' id='id_birthdate' required class='form-control'>`


$('#fecha').html(datepicker)
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
        