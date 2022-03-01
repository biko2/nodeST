## Proyecto educativo NodeST

### Introducción

Estas en la unidad de disco del proyecto NodeST. Para poder comunicarnos con el Nodo (el disco verde)
Usamos un micro controlador de la fundación raspberry pi que se llama Pico.

Pico es un chip (micro controlador) programable que nos permite adentrarnos en la electrónica educativa
de forma amigable y sencilla.

En NodeST usamos "la pico" para poder comunicarnos con el nodo y para poder aprender los conceptos básicos de la programación.
En la Pico se pueden usar distintos lenguajes de programación. En nuestro caso hemos elegido una versión especial de python creada por [AdaFruit](https://learn.adafruit.com)

Adafruit fue fundada en 2005 por la ingeniera del MIT, Limor "Ladyada" Fried. Su objetivo era crear el mejor lugar en línea para aprender electrónica y fabricar los mejores productos diseñados para creadores de todas las edades y niveles de habilidad

Las personas de Adafruit se dieron cuenta que programar micro controladores con los métodos anteriores se podía simplificar. Por eso crearon una versión especial de python que se llama [Circuitpython](https://circuitpython.readthedocs.io/en/latest/index.html)

NodeST se podría decir que es una librería de Circuitpython que conecta con el nodo con la Pico.

### Estructura de carpetas

En esta unidad de disco del proyecto NodeST se encuentra el siguiente contenido:

- Readme.md con la información del proyecto
- lib: librería de Circuitpython
- Ejercicios: carpeta con los ejercicios
- code.py con el código del proyecto

Cuando conectas la pico mediante el usb. Con el usb se alimenta la placa y su bootloader carga el fichero code.py y su código se ejecuta nuestra pico.

Si es la primera vez que arrancas la pico conectada el nodo, veras que se te enciende el led rojo. Este es nuestro "hola mundo"

Cada uno de los ejercicios introduce pequeños concepto de programación. Como asientes en los talleres de NodeST o como persona que se esta introduciendo en la electrónica educativa te listamos los ejercicios y que se busca enseñar en ellos

### Ejercicios

En cada carpeta de ejercicios el el fichero code.py, no solo estará el código con el que trabajaremos también habrá una documentación interna del código. Sobre todo en los primero ejercicios el código será más extenso. Si eres un formador y ves que la información es excesiva o necesitas modificar hazlo sin problemas, nosotros hemos intentado abarcar más de lo necesario lo más genérico posibles

- **01_Hola_mundo**: Este es nuestro _hola mundo_ en NodeST el hola mundo es un led Rojo encendido. Es el código mínimo para poder trabajar con la pico y el nodo.
- **02_2_LEDS**: En este código se explican la mayor parte de los elementos de Circuitpython y los primeros pasos para acceder a las funcionalidades de nodo. Similar al ejercicio uno pero adentrándose en los elementos fundamentales de Circuitpython. Se ven conceptos básicos como las variables, la biblioteca de Sumalib. Pero la documentación es extensa para no obligatoria.
  Comprender las variables es lo fundamental de este ejercicio, en este caso guardaremos un color, pero sobre todo nos metemos en la idea de lo abstracto.
- **03_LED_Blink**: En este ejercicio, lo que buscamos es continuar con los conceptos anteriores, pero añadiremos el tiempo. En la pico el tiempo lo mide la placa y nuestra programación puede necesitar un control del tiempo `time.sleep(1)` le dice a la pico que espere 1 segundo. En este ejercicio es bueno recordar el bucle while para que el led se encienda y se apague.
- **04_Colores**: Nuestro NodeSt usa los 16 leds para comprender los fundamento básicos de la programación, guardar variables con colores y hacer que la Pico ejecute el `code.py` para mostrar los colores es una forma de pasar de lo abstracto a lo concreto.
- **05_Colores_predefinidos**: En programación una de las reglas básicas en no repetir es que no debemos repetir lo que ya hemos visto. En este ejercicio vamos a usar los colores predefinidos de nuestra biblioteca Sumalin. Aquí lo importante es entender que podemos usar utilidades externas como los colores para poder programar.
- **06_Comentarios**: De la misma manera que en el segundo ejercicio el `code.py` esta repleto de comentarios en este ejercicio lo que buscamos es como añadir connotarías en linea con `#` y comentarios en bloques con `"""`
- **07_16_LEDS**: NodeSt tiene 16 leds y tiene una relación, con este ejercicio indicaremos que una variable puede ser de un tipo, en nuestro caso de tipo `led` y que a esa relación le llamamos array o conjunto. tenemos un array de leds, más concretamente un array de 16 leds. Jugar a encender los distintos leds y apagar los distintos leds. Nos permitirá otra vez visualizar esa relación y enter el concepto de array.
- **08_16_LEDS_BUCLE**: Un array o un conjunto como elemento abstracto es una de los elementos mas poderosos dentro de los lenguajes de programación recorre ese conjunto y hacer con el algo es un reto, entender la importancia de los bucles es la idea de este ejercicio
- **09_LED_CAMINANTE**: En este caso el ejercicio busca explicar las condiciones, pero sobre las bases de los ejercicios anteriores. Para ello haremos que un led avance, pero en realidad lo que es estamos e trabajando con los bucles y añadiremos la sentencia `if` para introducir condiciones.
- **10_LED_CAMINANTE_DEPURAR**: ¿Y como podemos saber lo que pasa mientras se van ejecutando cada una de las líneas del código? Saber que ocurre y ver que es lo que contienen nuestros array o nuestras variables le llamamos depurar el código y es la finalidad de este ejercicio.
