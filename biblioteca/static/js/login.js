$(function(){

    console.log('entra')
    var id_biblioteca = localStorage.getItem('biblioteca_id')
    console.log(id_biblioteca)

    
    $.ajax({
        url: '/libros/index-user/',
        type: 'post',
        dataType: 'json',
        data: {
            biblioteca_id: id_biblioteca,   
            csrfmiddlewaretoken: $('input:hidden[name=csrfmiddlewaretoken]').val(), 
        },
        success: function(response){
            console.log('jajsjs')
            var libros = $.parseJSON(response.Libro)
            console.log(libros)
            var tabla = ''
            libros.forEach((libro, index) => {
                tabla += '<tr>';
                tabla += '<td>' + (index + 1)  + '</td>' +
                         '<td>' + libros[index]['titulo'] + '</td>' +
                         '<td>' + libros[index]['autor__nombre'] +  '</td>' + 
                         '<td>' + libros[index]['tema__tema'] + '</td>' + 
                         '<td>' + libros[index]['ubicacion'] + '</td>' + 
                         '<td>' + libros[index]['disponibles'] + '</td>'

                         if(libros[index]['disponibles'] > 0 ){
                            tabla += '<td> <a href="/prestamos/pre-prestamo/'+ libros[index]['id']+'"  class="btn btn-info"> Prestar </a> </td>' + 
                            '</tr>';

                         } 
                         else {
                            tabla += `<td>  No disponible </td> </tr>`;

                         }


            });
            $('#tbl_libros').html(tabla)
            
            
        }, 
        error: function(error){
            console.log('error')
            console.log(error)
        }
    })

})

