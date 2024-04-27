//var opciones = ["piedra","papel","tijera"]

var opciones = [0,1,2];
var eleccionMaquina;

function aleatorio(minimo, maximo){
    var numero = Math.floor(Math.random() * (maximo - minimo +1)+ minimo);
    return numero;

}

function usuario (eleccionUsuario){
    eleccionUsuario = parseInt(eleccionUsuario);
    eleccionMaquina = aleatorio(0,2);

    if(eleccionUsuario == 0){//Eleccion usuario "piedra"
        if (opciones[eleccionMaquina]== 1){
            document.getElementById('efecto').innerHTML='<h1> ¡Perdiste!</h1> <h3> la maquina eligio papel</h3>';
            console.log ("perdi");
        }else{
            if (opciones[eleccionMaquina] == 2){
                document.getElementById('efecto').innerHTML='<h1> Ganaste!</h1> <h3> la maquina eligio tijera</h3>';
                console.log ("gane");
            }else
            if (opciones[eleccionMaquina] == 0){
                document.getElementById('efecto').innerHTML='<h1> Empate!</h1> <h3> la maquina eligio piedra</h3>';
                console.log ("empate");
            }
        }
    }

    if(eleccionUsuario == 1){//Eleccion usuario "papel"
        if (opciones[eleccionMaquina]== 1){ 
            document.getElementById('efecto').innerHTML='<h1> Empate!</h1> <h3> la maquina eligio papel</h3>';
            console.log ("empate");
        }else{
            if (opciones[eleccionMaquina] == 2){
                document.getElementById('efecto').innerHTML='<h1> Gano la maquina!</h1> <h3> la maquina eligio tijera</h3>';
                console.log ("gano la maquina");
            }else
            if (opciones[eleccionMaquina] == 0){
                document.getElementById('efecto').innerHTML='<h1> gane!</h1> <h3> la maquina eligio piedra</h3>';
                console.log ("gane");
            }
        }

    }
    document.getElementById('efecto').style.display="";
}

function quitarEfecto(){
    document.getElementById('efecto').style.display ="none";
    
}