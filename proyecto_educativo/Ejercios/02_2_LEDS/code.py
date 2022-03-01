

''' 
Sumalib es la biblioteca para el control del nodeST y que lo hacemos mediante de la Raspberry Pico
Mediante esta biblioteca podemos programar el NodeST usando los LEDs, el botín y altavoz
    
En python la forma de usar la biblioteca es: from (desde) import (utilidades)
'''
from sumalib import Sumalib

'''
Los leds son el elemento principal que se pueden controlar desde el nodeST
Usuremos los leds para entender los rudimentos básicos de la programación
Accedemos a los leds y sus utilidades de esta forma:
'''
leds = Sumalib()


'''
Nuestros leds son RGB (Rojo, Verde, Azul). Podemos conbinarlos para crear colores. 
Si quires profundizar más en los concepto básicos de colores te recomiendo este link:
https://imborrable.com/blog/rgb-y-cmyk/#:~:text=El%20modo%20de%20color%20RGB,de%20luz%20y%20no%20tinta. 

Cuando realizamos esta sentencia: 
palabra = "Texto prueba" 

Lo que estamos haciendo es asignar una variable 
Estamos indicando que la variable palabra va a ser una cadena de texto (En este caso "texto prueba")
En la linea donde pone COLOR_ROJO = (255,0,0), se esta asignando a la variable COLOR_ROJO = tres valores numéricos que simplificando
Son la cantidad de rojo, verde y azul que queremos que tenga nuestro led.

Te sorprenderá que el valor de rojo que es 255, el verde es 0 y el azul es 0. 
Tendremos de 0 a 255 para cada uno de los colores (20, 0, 0) sera un rojo, 
pero al ser un valor muy bajo sera un rojo apagado ya que ese valor se traduce en cantidad de voltaje que es la forma
de controlar el brillo del led.
Y en el caso de los leds esto se notará es su brillo
Como los leds son aditivos, la suma de los colores será el color final. Si ponemos (255, 255, 255) tendremos el color blanco más brillante

A su vez (0, 0, 0) sera un negro y que en los leds de nuestro NodeST equivale a tener el led apagado 
'''
COLOR_ROJO = (255, 0, 0)
COLOR_NEGRO = (0, 0, 0)

'''
Uno de los elementos más importantes que usaremos es un bucle infinito, en la pico este sentencia while le dice que la repita infinitamente
'''
while(True):
    leds[0] = COLOR_ROJO
    leds[1] = COLOR_ROJO
    leds.show()
