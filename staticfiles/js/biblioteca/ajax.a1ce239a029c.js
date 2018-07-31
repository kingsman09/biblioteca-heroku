$('form').on('submit', function(evt){
    // evt.preventDefault()

    console.log('entra')

    var nombre = $('#id_nombre').val()
    var descripcion = $('#id_descripcion').val()
    var ubicacion = $('#id_ubicacion').val()
    var latitud = $('#id_latitud').val()
    var longitud = $('#id_longitud').val()

    console.log(nombre + '\n' + descripcion + '\n' + ubicacion + '\n' + latitud  + '\n' + longitud )

    $.ajax({
        url: '/libros/crear-biblioteca/',
        type: 'post',
        dataType: 'json',
        contenType: 'application/json',
        data: {
            nombre: nombre,
            descripcion: descripcion,
            ubicacion:ubicacion,
            latitud: latitud,
            longitud: longitud,
            csrfmiddlewaretoken: $('input:hidden[name=csrfmiddlewaretoken]').val(),
        }, 
        success: function(response){
            window.location.href = '/libros/bibliotecas/'
        },
        error: function(error){
            console.log(error)
        }
    })

})