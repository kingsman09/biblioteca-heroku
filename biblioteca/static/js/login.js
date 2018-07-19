$('form').on('submit', function(evt){
    // evt.preventDefault()
    email = $('#id_email').val()
    password = $('#id_password').val()
    biblioteca = $('#slc_biblioteca').val()

    $.ajax({
        url: '/login/',
        type: 'post',
        dataType: 'json',
        data: {
            email: email,
            password: password,
            biblioteca: biblioteca,
            csrfmiddlewaretoken: $('input:hidden[name=csrfmiddlewaretoken]').val(), 
        },
        success: function(response){
            console.log(biblioteca)
            localStorage.setItem('biblioteca_id', biblioteca)
            
        }, 
        error: function(error){
            console.log(error)
        }
    })

})