
$(function(){
    renderizar_tabla()
})

$('#enviar').on('click', function(evt){
    evt.preventDefault()
    renderizar_tabla()
})


function renderizar_tabla(){
    var guardar_biblioteca = document.getElementById('slc_biblioteca').value
    localStorage.setItem('biblioteca_id', guardar_biblioteca)


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
            var tabla = '';
            tabla += `<table class='table table-hover table-sm text-center' id='table-controller'>
                            <thead class='thead-dark'>
                                <tr>
                                    <th scope="col" > #  </th>
                                    <th scope="col" > Libro </th>
                                    <th scope="col" > Autor </th>
                                    <th scope="col" > Tema </th>
                                    <th scope="col" > Ubicacion </th>
                                    <th scope="col" > Disponibles </th>
                                    <th scope="col" > Operaciones </th>
                                </tr>
                            </thead>
                            <tbody>`

            libros.forEach((libro, index) => {
                tabla += `<tr role='row' class='odd'>
                            <td class='sorting_1'> ${index + 1}  </td>
                            <td> ${libro.titulo} </td>
                            <td> ${libro.autor__nombre}  </td> 
                            <td> ${libro.tema__tema} </td> 
                            <td> ${libro.ubicacion} </td> 
                            <td> ${libro.disponibles} </td>`

                        if(libro.disponibles > 0 ){
                            tabla += `<td> <a href="/prestamos/pre-prestamo/${libro.id}"  class="btn btn-info"> Prestar </a> </td>                             
                                      </tr>`
                        }else {
                            tabla += `<td>  No disponible </td> </tr>`;

                        }


            });

            tabla += `</tbody>
                      </table>`

            $('#insertar_tabla').html(tabla)
            $('#table-controller').DataTable();
            $("#table-controller_paginate").hide();
            $("#table-controller_length").hide();
            $("#table-controller_info").hide();
       
            
            
        }, 
        error: function(error){
            console.log('error')
            console.log(error)
        }
    })
}






