<em> # QA - PROJECT URBAN ROUTES ES </em>#

#### JORGE GARCIA CARDONA
#### QA25

###### Descripción
Este proyecto es una aplicación diseñada para realizar pruebas de calidad (QA)\
y asegurar el correcto funcionamiento de un sistema relacionado con Urban Routes\
usando selenium incluyendo métodos y localizadores; escribiendo pruebas de forma\
que nos permitan realizar el pedido de un taxi.\
Iniciamos digitando la dirección desde hasta en cada campo correspondiente,\
seleccionamos el icono del taxi y luego damos click en el botón pedir taxi, allí\
elegimos la tarifa comfort, digitamos el campo número, seleccionamos método de pago\
digitamos un mensaje para el conductor, en requisitos del pedido seleccionamos\
mantas y pañuelos y solicitamos helado, por último buscamos el taxi.\
Es muy relevante que tengamos presente que tanto como los métodos como los test\
los nombremos de forma que el mismo nombre nos indique para que se están creando.


###### Tecnologías

El proyecto lo creamos en PyCharm usamos Python como Lenguaje de programación\
principal; pytest como Framework de pruebas utilizado para automatizar y\
gestionar las pruebas, biblioteca de Python para realizar solicitudes HTTP.

###### Ejecución pruebas

Para las pruebas debemos tener muy presente que deben ser claras\
y enfocadas para lo que se quiere probar, directamente relacionadas en la lista de comprobación.\
Las pruebas deben estar alineasdas con respecto a los métodos y los requerimientos.\

*Abre el proyecto en PyCharm\
*Abre el archivo "main.py"\
*Verifica que tengas instalado pytest\
*Haz click derecho sobre el archivo de pruebas "main.py"\
*Seleciona la opción (Run python test for...) o de click en el en el icono de play en la parte superior\


*Si vas a correr la prube desde una terminal valida si tienes pytest instalado\
(abre la terminal y ejecuta "pip install pytest")\
*Desde el directorio raiz del proyecto ejecuta el comando "pytest -v"\

Es fundamental que antes de correr las pruebas actualice la url



##### Comando de ejecución de las pruebas:/

pytest \projects\qa-project-Urban-Routes-es-main\main.py
