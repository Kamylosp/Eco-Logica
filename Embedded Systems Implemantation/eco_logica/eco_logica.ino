#include <Arduino.h>
#include <rdm6300.h>

//#define RDM6300_ORGANIC_RX_PIN 10 // read the SoftwareSerial doc above! may need to change this pin to 10...
//#define RDM6300_RECYCLABE_RX_PIN 12
#define ORGANIC_SERVO_PIN 13
//#define RECYCLABLE_SERVO_PIN 11

Rdm6300 organicRdm6300;
Rdm6300 recyclableRdm6300;
uint32_t organicServoSituation;
uint32_t recyclableServoSituation;
uint32_t addresses[] = {151615615, 211131312, 115651666, 328329233};
uint8_t index = 0;
char servoSituation;

void setup() {
  Serial.begin(9600);

  pinMode(ORGANIC_SERVO_PIN, OUTPUT);
 // pinMode(12, OUTPUT);
  // pinMode(RECYCLABLE_SERVO_PIN, OUTPUT);
  // organicRdm6300.begin(RDM6300_ORGANIC_RX_PIN, 1);
  // recyclableRdm6300.begin(RDM6300_RECYCLABE_RX_PIN, 2);
  while (!Serial) { ; }
  while (Serial.available()) {
    Serial.read();
  }
  Serial.write('s');
  //analogWrite(ORGANIC_SERVO_PIN, 191);
  //Serial.println("\nGame started");
}

void loop() {
  String addressStr;
  if (index % 2 == 0) {
    addressStr = String('1') + String(addresses[index]);
  } else {
    addressStr = String('2') + String(addresses[index]);
  }
  
  Serial.write(addressStr.c_str(), addressStr.length());
  //Serial.write('\n'); // Add a newline character for better readability on the receiver side
  
  index++;
  if (index >= 4) index = 0;

  while(Serial.available() <= 0){;}

  servoSituation = Serial.read();

  if (servoSituation == '1') {
    analogWrite(ORGANIC_SERVO_PIN, 254);
    //digitalWrite(12, HIGH);
  } else {
    analogWrite(ORGANIC_SERVO_PIN, 1);
   // digitalWrite(12, LOW);
  }

}
