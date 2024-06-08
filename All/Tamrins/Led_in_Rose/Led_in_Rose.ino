// تغییر وضعیت led در لبه بالا رونده
#include <Bounce2.h> // Add Library
#define buttonPin 2 // Define a constant
#define ledPin 13

Bounce debouncer = Bounce(buttonPin, 5); // Create a variable from Bounce class(Library)

void setup() {
  pinMode(ledPin,OUTPUT);
  pinMode(buttonPin,INPUT_PULLUP);
}

void loop() {
  debouncer.update();
  
  if (debouncer.rose()){
    digitalWrite(ledPin,HIGH);
  } else if (debouncer.fell()){
    digitalWrite(ledPin,LOW);
  }
}
