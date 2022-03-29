#include <MsTimer2.h>
#include <SoftwareSerial.h>

#define MESSAGE_GAP_TIMEOUT_IN_MS 80
#define LED_TOGGLE_MSGS 50


uint8_t RecvBuffer[256];     


unsigned int recvIndex = 0;
unsigned long msgIndex = 0;
unsigned long receiveTime = 0;

char receiveTimeString[32];
char msgIndexString[32];

const byte LED_PIN = 13;

SoftwareSerial RS485(3, 4); // RX, TX

void setup()
{
  
  pinMode(LED_PIN, OUTPUT);

  // set an end-of-message detection timeout of 5ms
  MsTimer2::set(MESSAGE_GAP_TIMEOUT_IN_MS, onTimer);

  Serial.begin(115200);
  while (!Serial) {
    ; // Espera a que se establezca conexión.
  }
  Serial.println("¡Arduino Debuger READY!");
  // Inicializa el puerto SoftwareSerial
  RS485.begin(115200);
}

bool dumpData = false;
bool timerStarted = false;

// If this timer expires, this means no additional character was received for a while: notify main loop
void onTimer() {
  dumpData = true;        
}

void loop()
{
   uint8_t received;

   if (RS485.available() > 0) {
      received =  RS485.read();
      RecvBuffer[recvIndex++] = received;
      Serial.print(received,HEX);
      Serial.print(" ");
   }

    // first time we get an empty buffer after receiving stuff:
    // this could be the end of the message, (re)start the end-of-message detection timer. 
    if (recvIndex>0) {

      if (!timerStarted){
        MsTimer2::start();
        timerStarted = true;
      }
    } 

   // If the timer expired and positioned this var, we should now dump the received message
   // into a UDP packet to the remote host/logger.
   if (dumpData) {
      receiveTime = micros() - MESSAGE_GAP_TIMEOUT_IN_MS*1000; 
      
      // reinitialize vars for next detection/dump
      dumpData = false;
      MsTimer2::stop();
      timerStarted = false;   

      msgIndex++ ;
      if (msgIndex > 999) msgIndex = 0;
      Serial.println("--- fin trama---");
      
      for(int i = 0; i > sizeof(RecvBuffer);i++){
       Serial.print(RecvBuffer[i],HEX);
      }
      Serial.println();
      //Serial.println(RecvBuffer);

      // reset index for next message
      recvIndex = 0;
   } 
} 