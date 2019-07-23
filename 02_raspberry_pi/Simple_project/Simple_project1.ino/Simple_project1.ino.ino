#include <SoftwareSerial.h>
SoftwareSerial BT_Serial(2, 3); // TX, RX

void distAlarm(int freq){
    digitalWrite(4, HIGH);
    tone(7, 963, freq);
    delay(freq);
    digitalWrite(4, LOW);
    noTone(7);
    delay(freq);
}

void infraredSensor(){

  long distance;
  
  while(1){
    digitalWrite(TRIG, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG, LOW);

    distance = pulseIn(ECHO, HIGH)/58.2;
    
    if(distance < 10){
      distAlarm(50);
    }else if(distance < 20){
      distAlarm(100);
    }else if(distance < 30){
      distAlarm(300);
    }
    
    if(Serial.available()>0){
        breakSign = Serial.read();
        if(breakSign){
          return;
        }
    }
  }  
}

void setup() {
  Serial.begin(9600);
  BT_Serial.begin(9600);
  pinMode(12, OUTPUT);
}

void loop() {
  if(BT_Serial.available()){
    byte data = BT_Serial.read();
    Serial.write(data);
       
    switch
    
    if(data == '1'){
      digitalWrite(12,HIGH);
    }else if(data == '2'){
      digitalWrite(12,LOW);
    }
  }

  if(Serial.available()){
    BT_Serial.write(Serial.read());
  }
}
