


function ValidarLetra(evt, tipo) {
    var tecla = evt.keyCode;

    switch (tipo) {
        case 1:
            if (tecla == 8 || tecla == 32 || tecla == 11) {
                return true;
            }

            var patron = /[a-zA-Z]/
    }

    var tecla_final = String.fromCharCode(tecla);
    return patron.test(tecla_final);
}