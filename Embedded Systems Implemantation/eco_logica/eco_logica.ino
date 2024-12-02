#include <Arduino.h>
#include <SPI.h>
#include <MFRC522.h>
#include<Servo.h>
#define ORGANIC_SERVO_PIN 11
#define RECYCLABLE_SERVO_PIN 12
#define SS_PIN_1 10 
#define SS_PIN_2 8   
#define RST_PIN 9    

MFRC522 rfid1(SS_PIN_1, RST_PIN); 
MFRC522 rfid2(SS_PIN_2, RST_PIN);  
Servo organicServo;
Servo recyclableServo;

void setup() {
  Serial.begin(9600);  
  SPI.begin(); 
  rfid1.PCD_Init();  
  rfid2.PCD_Init();  

  organicServo.attach(ORGANIC_SERVO_PIN);
  recyclableServo.attach(RECYCLABLE_SERVO_PIN);

  while (!Serial) { ; }
  while (Serial.available()) {
    Serial.read();
  }
  Serial.write('s');
}

void loop() {
  RFID(rfid1, 1); //ORGANIC
  RFID(rfid2, 2); //RECYCLABLE
}

void RFID(MFRC522 &rfid, int sensorNumber) {
  if (!rfid.PICC_IsNewCardPresent()) {
    return; // No new card
  }

  if (!rfid.PICC_ReadCardSerial()) {
    return; // Could not read card
  }

  String uidString = "";
  for (byte i = 0; i < rfid.uid.size; i++) {
    if (rfid.uid.uidByte[i] < 10) {
      uidString += "00";
    } else if (rfid.uid.uidByte[i] < 100) {
      uidString += "0";
    }
    uidString += String(rfid.uid.uidByte[i]);
  }

  Serial.print(String(sensorNumber) + uidString);

  while (!Serial.available()) { ; }
  char servoSituation = Serial.read();

  if (servoSituation == '1') {
    if (sensorNumber == 1)
      organicServo.write(180);
    else recyclableServo.write(180);
  } else {
    if (sensorNumber == 1)
      organicServo.write(0);
    else recyclableServo.write(0);
  }
  rfid.PICC_HaltA();
}
