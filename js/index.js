//TODO-JQUERY
async function validaCorreo(email, div) {
    console.log(email);
    var email = $(email).val();
    var caracteres = new RegExp(/^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/);

    if (caracteres.test(email) == false) {
        $(div).hide().removeClass('hide').slideDown('fast');
        return false;

    } else {
        $(div).hide().addClass('hide').slideDown('slow');
        return true;
    }
}

$('form').find('input[type=email]').blur(function(){
    validaCorreo($(this).val(), '#xemail')
  });


function ingresoUsuario() {

}

//PRUEBA JQUERY
/*$(document).ready(function () {
    $('#btnIngresar').on('click', function (e) {
        console.log("TEST");
    })
});*/

