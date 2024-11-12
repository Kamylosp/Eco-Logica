#include <Arduino.h>
#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10  // Pino de seleção (SDA) conectado ao pino digital 10 do Arduino Mega 2560
#define RST_PIN 9  // Pino de reset conectado ao pino digital 9 do Arduino Mega 2560

MFRC522 rfid(SS_PIN, RST_PIN);  // Cria a instância do objeto MFRC522

#define ORGANIC_SERVO_PIN 13
//#define RECYCLABLE_SERVO_PIN 11

uint8_t cardIndex = 0;  // Renomeado de 'index' para 'cardIndex'
char servoSituation;

void setup() {
  Serial.begin(9600);
  SPI.begin();  // Inicializa o barramento SPI
  rfid.PCD_Init();  // Inicializa o MFRC522

  pinMode(ORGANIC_SERVO_PIN, OUTPUT);

  while (!Serial) { ; }
  while (Serial.available()) {
    Serial.read();
  }
  Serial.write('s');
}

void loop() {
  // Procura por novos cartões
  if (!rfid.PICC_IsNewCardPresent()) {
    return;
  }

  // Seleciona um dos cartões presentes
  if (!rfid.PICC_ReadCardSerial()) {
    return;
  }

  String uidString = "";
  
  // Constrói o UID do cartão como um único número inteiro em uma string
  for (byte i = 0; i < rfid.uid.size; i++) {
    // Adiciona zeros à esquerda, se necessário
    if (rfid.uid.uidByte[i] < 10) {
      uidString += "00";
    } else if (rfid.uid.uidByte[i] < 100) {
      uidString += "0";
    }
    uidString += String(rfid.uid.uidByte[i]);
  }

  String addressStr;
  if (cardIndex % 2 == 0) {
    addressStr = String('1') + uidString;
  } else {
    addressStr = String('2') + uidString;
  }
  
  Serial.write(addressStr.c_str(), addressStr.length());
  // Serial.write('\n'); // Adicione um caractere de nova linha para melhor legibilidade do lado do receptor
  
  cardIndex++;  // Incrementando 'cardIndex'
  if (cardIndex >= 2) cardIndex = 0;

  while (Serial.available() <= 0) { ; }

  servoSituation = Serial.read();

  if (servoSituation == '1') {
    digitalWrite(ORGANIC_SERVO_PIN, HIGH);
  } else {
    digitalWrite(ORGANIC_SERVO_PIN, LOW);
  }

  // Para a leitura do cartão
  rfid.PICC_HaltA();
}
