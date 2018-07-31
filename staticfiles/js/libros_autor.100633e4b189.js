var id = localStorage.getItem('biblioteca_id')
var autor = document.getElementById('id_autor').value
console.log(id + "  " + autor )

$.ajax({
    url:`/autores/prueba${autor}/`,
    type: 'post',
    dataType: 'json',
    data: {
        id_biblioteca: id,
        id_autor: autor,
        csrfmiddlewaretoken: $('input:hidden[name=csrfmiddlewaretoken]').val(), 
    },
    success: function(response){
        console.log('sirve')
        var libros = $.parseJSON(response['Libro'])
        console.log(libros)
        
        var tabla = '';

        libros.forEach((libro, index)=>{
            tabla += `<tr>
                      <th scope='col'>${index + 1}</th>
                      <th> ${libro.titulo} </th>
                      <th> ${libro.autor__nombre} </th>
                      <th> ${libro.tema__tema} </th>
                      <th> ${libro.ubicacion} </th>
                      <th> ${libro.disponibles} </th>`

                      if(libro.disponibles > 0){
                          tabla += `<th>
                                    <a href="/prestamos/pre-prestamo/${libro.id}" class='btn btn-info'>  Prestar </a>
                                    </th>
                                    </tr>`
                      }else{
                            tabla += `<th> No disponibles </th>
                                      </tr>`
                      }
                    
        })
        if(libros.length > 0){
        $('#tbl_libros_autor').html(tabla)
        $('#table-controller').before('<h4> Libros del autor disponibles en esta biblioteca </h4><br>')
        }

    },
    error: function(error){
        console.log('error')
        console.log(error)
    }
})