#include <Bounce2.h> // Add Library
#define buttonPin 2 // Define a constanct
#define ledPin 13

Bounce debouncer = Bounce(); // Create a variable from Bounce class(Library)

int ledState = 0;

void setup() {
  pinMode(ledPin,OUTPUT);
  pinMode(buttonPin,INPUT_PULLUP);
  
  debouncer.attach(buttonPin); // Connect BPin to Debouncer
  debouncer.interval(5); // Interval is in Melli Second(ms)

  digitalWrite(ledPin, ledState);
}

void loop() {
  debouncer.update();
  if (debouncer.rose()){
    ledState = ! ledState;
    digitalWrite(ledPin, ledState);
  }

}
