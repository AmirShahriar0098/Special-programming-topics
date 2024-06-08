// برنامه ای بنویسید که یک LED را از 3 دکمه بتوان مدیریت کرد(اگر با اولی روشن شد با دوتای دیگر خاموش شود)
#include <Bounce2.h>

#define buttonPin1 2
#define buttonPin2 3
#define buttonPin3 4

#define ledPin 13

Bounce debouncer1 = Bounce(buttonPin1, 5);
Bounce debouncer2 = Bounce(buttonPin2, 5);
Bounce debouncer3 = Bounce(buttonPin3, 5);

void setup() {
  pinMode(ledPin, OUTPUT);
  
  pinMode(buttonPin1, INPUT_PULLUP);
  pinMode(buttonPin2, INPUT_PULLUP);
  pinMode(buttonPin3, INPUT_PULLUP);
}

void loop() {
  debouncer1.update();
  debouncer2.update();
  debouncer3.update();
  
  if (debouncer1.fell() || debouncer2.fell() || debouncer3.fell()) {
    if (digitalRead(ledPin) == HIGH){
      digitalWrite(ledPin, LOW);
    }
    else{
      digitalWrite(ledPin, HIGH);
    }
  }
}
