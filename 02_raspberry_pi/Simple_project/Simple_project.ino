#include <SoftwareSerial.h>
#include <Servo.h>
#include "dht11.h"
SoftwareSerial BT_Serial(2, 3); // TX, RX

Servo my_servo;
dht11 DHT11;
#define DHT11PIN 13

void setup() {
  Serial.begin(9600);
  BT_Serial.begin(9600);
  my_servo.attach(12);
  pinMode(9, OUTPUT);
//  my_servo.write(0);
}

void loop() {
//  my_servo.write(0);
  if(BT_Serial.available()){
    byte data;
    data = BT_Serial.read();
    Serial.write(data);
    if(data == '2'){
      int chk = DHT11.read(DHT11PIN);
      switch (chk)
      {
        case DHTLIB_OK: 
        Serial.println("OK"); 
        break;
        case DHTLIB_ERROR_CHECKSUM: 
        Serial.println("Checksum error"); 
        break;
        case DHTLIB_ERROR_TIMEOUT: 
        Serial.println("Time out error"); 
        break;
        default: 
        Serial.println("Unknown error"); 
        break;
      }
      Serial.println((float)DHT11.temperature);
      if((float)DHT11.temperature > 10){
        Serial.println("Air conditioner on");
        int pos = 1;
        for(; pos < 720; pos += 1){
          my_servo.write(pos);
          delay(10);
        }
      }else{
        Serial.println("Air conditioner off");
      }  
    }
  }
  if(Serial.available()){
    BT_Serial.write(Serial.read());
  }
}
