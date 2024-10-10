/*
 * A simple example to interface with rdm6300 rfid reader.
 *
 * Connect the rdm6300 to VCC=5V, GND=GND, TX=any GPIO (this case GPIO-04)
 * Note that the rdm6300's TX line is 3.3V level,
 * so it's safe to use with both AVR* and ESP* microcontrollers.
 * Note that on SAMD the RX_PIN is ignored, the default is Serial1 (pin0),
 * but if specify rdm6300.begin(RDM6300_RX_PIN, 2); then Serial2 (pin30) is used.
 *
 * This example uses SoftwareSerial, please read its limitations here:
 * https://www.arduino.cc/en/Reference/softwareSerial
 *
 * Arad Eizen (https://github.com/arduino12).
 */

#include <Arduino.h>
#include <rdm6300.h>

#define RDM6300_ORGANIC_RX_PIN 10 // read the SoftwareSerial doc above! may need to change this pin to 10...
#define RDM6300_RECYCLABE_RX_PIN 12
#define ORGANIC_SERVO_PIN 13
#define RECYCLABLE_SERVO_PIN 11

Rdm6300 organicRdm6300; 
Rdm6300 recyclableRdm6300
uint8_t organicServoSituation;
uint8_t recyclableServoSituation

void setup()
{
	Serial.begin(9600);

  pinMode(ORGANIC_SERVO_PIN, OUTPUT);
  pinMode(RECYCLABLE_SERVO_PIN, OUTPUT)
	organicRdm6300.begin(RDM6300_ORGANIC_RX_PIN);
  recyclableRdm6300.begin(RDM6300_RECYCLABE_RX_PIN);
  while(!Serial){;}
  Serial.println("\nGame started");
}

void loop()
{
  if(organicRdm6300.get_new_tag_id() != 0)
    Serial.write('1', organicRdm6300.get_new_tag_id());
  if(organicRdm6300.get_tag_id() != 0)
	  Serial.write('1', organicRdm6300.get_tag_id());
  delay(100);
  if(recyclableRdm6300.get_new_tag_id() != 0)
    Serial.write('2', recyclabeRdm6300.get_new_tag_id());
  if(recyclabeRdm6300.get_tag_id() != 0)
	  Serial.write('2', recyclableRdm6300.get_tag_id());
  delay(100)

  servoSituation = Serial.read();

  if(servo)

	delay(10);
}
