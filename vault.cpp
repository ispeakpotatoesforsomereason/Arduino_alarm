#include <Servo.h>
#include <IRremote.hpp>

Servo myservo;
const int IR_RECEIVE_PIN = 11;
const int buttonPin = A1;

int currentPos = 180;
int targetPos = 180;
bool isAt180 = true;
bool lastButtonState = HIGH;

unsigned long lastMoveTime = 0;
const int stepDelay = 15;

void setup() {
  Serial.begin(9600);
  IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);
  myservo.attach(9);
  myservo.write(currentPos);
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  unsigned long currentTime = millis();

  if (currentPos != targetPos) {
    if (currentTime - lastMoveTime >= stepDelay) {
      if (currentPos < targetPos) currentPos++;
      else currentPos--;
      myservo.write(currentPos);
      lastMoveTime = currentTime;
    }
  }

  bool currentButtonState = digitalRead(buttonPin);
  if (currentButtonState != lastButtonState) {
    if (currentButtonState == LOW) {
      Serial.println("La cassaforte è chiusa.");
    } else {
      Serial.println("La cassaforte è aperta.");
    }
    lastButtonState = currentButtonState;
    delay(20);
  }

  if (IrReceiver.decode()) {
    uint16_t cmd = IrReceiver.decodedIRData.command;
    if (cmd == 0x45 && !isAt180) {
      targetPos = 180;
      isAt180 = true;
    }
    IrReceiver.resume();
  }

  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    input.trim();
    if (input == "21ss4WSOSOskc2Spp+s#") {
      if (isAt180) {
        targetPos = 40;
        isAt180 = false;
      } else {
        targetPos = 180;
        isAt180 = true;
      }
    }
  }
}
