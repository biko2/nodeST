# Sumalim
> en ninguno de las pruebas hemos recibido datos del nodo.
> Ni respuestas ACK a comandos ni tampoco el POLLING_STATUS
> Tampoco recibimos respuesta de las pulsaciones de los botones.

No tenemos claro el procedimiento a seguir para capturar los eventos de los botones. Por lo que vemos está el POLLING_STATUS pero tambien parece que envian directamente evento de pulsación en el momento correspondiente  [a confirmar]






(Tanto el RPI como Arduino usamos un modulo rs485 para la comunicacion)
- Con un arduino en modo lectura.
- Poniendo el cable FTDI en paralelo entre el nodo y un Arduino en modo lectura
- Con un Pico en modo lectura.
- Con el cable FTDI directamente y el programa cleverterm, enviando los comando del documento.


- Conseguimos enviar datos bien formados para practicamente todos los efectos de LED y el buzzer.

Podemos configurar los botones para que los efectos se lancen al pulsar el central.


- Tras varios intentos creimos que el nodo de Demo no mandaba nada por lo que implementamos lo necesario para calcular el CRC y enviar datos a un nodo normal.
- Todas las pruebas las hemos hecho con el nodo demo y uno "normal" ambos con el ID 5
