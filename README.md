Una fábrica de Piezas para motores de autos eléctricos desea conseguir un algoritmo que le
permita llevar el control diario (al final del día) de la cantidad de Piezas, de la cantidad de
Componentes de cada Pieza, y del Precio de los Componentes que se vendieron. Tal control le
permite a la fábrica proyectar la fabricación futura para reposición de sus productos.
El Código de Pieza (CP) es un valor de dos dígitos entre 01 y 99.
El Código de Componente (CC) es un valor de 4 dígitos, donde los dos primeros representan el
Código del Componente propiamente dicho, y está entre 01 y 99; y los dos últimos representan el
Código de Pieza al que corresponde y está entre 01 y 99.
Cada Componente tiene un Precio (PrC) que va desde $10,00 hasta $999,99, y el precio de cada
Pieza es igual a la suma de los precios de todos los Componentes de esa Pieza.
Se pide que construya un diagrama de flujo o un pseudocódigo que permita:
a) Ingresar valores numéricos que representan Códigos de Pieza para procesar, hasta que el
Código ingresado sea igual a 0 (cero), en cuyo caso terminará el procesamiento y el algoritmo.
b) Controlar que el valor del Código de Pieza sea un valor válido, y en caso contrario, volver a
pedirlo. En caso correcto imprimir el Código de Pieza.
c) Para cada código de Pieza válido, solicitar el ingreso de por lo menos un código de
Componente (valor de al menos 3 dígitos), al que habrá que controlar que sus últimos dígitos 
correspondan a la Pieza que se está procesando. En caso de que sea distinto, se solicitará el
reingreso del Código de Componente hasta que ingresen uno correcto.
d) Para cada código de Componente correcto se deberá imprimir dicho código, y se solicitará el
Precio, que deberá controlarse que sea un valor válido.
e) Para cada Pieza se calculará el Precio Total (PrT) como la suma de los Precios de las
Componentes.
f) El fin del procesamiento de Componentes para cada Pieza está determinado por el ingreso de
un Código de Componente igual a 0 (cero), y en tal caso deberá imprimir el Precio Total de los
componentes sumados hasta ese momento, y deberá enviar el control para pedir un nuevo
código de Pieza.
g) Al finalizar el algoritmo deberá imprimir la cantidad de Piezas procesadas.