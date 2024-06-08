// برنامه ای بنویسید که وضعیت led با دابل کلیلک پایین رونده تغییر  پیدا کند.
#include <Bounce2.h>

#define buttonPin 2
#define ledPin 13

int Clicks = 0;
unsigned long lastClickTime = 0;

Bounce debouncer = Bounce(buttonPin, 5);

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  debouncer.update();
  if (debouncer.fell()) {
    if (millis() - lastClickTime < 500) {
      Clicks++;
    } else {
      Clicks = 1;
    }
    lastClickTime = millis();
  }
  if (Clicks == 2) {
    digitalWrite(ledPin, HIGH);
    delay(1000);
    Clicks = 0;
  } else {
    digitalWrite(ledPin, LOW);
  }
}
