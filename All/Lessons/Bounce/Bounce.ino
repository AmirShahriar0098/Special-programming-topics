#include <Bounce2.h> // Add Library
#define buttonPin 2 // Define a constanct
#define ledPin 13
Bounce debouncer = Bounce(buttonPin, 5); // Create a variable from Bounce class(Library)

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin,OUTPUT);
  pinMode(buttonPin,INPUT_PULLUP);

  debouncer.attach(buttonPin); // Connect BPin to Debouncer
  debouncer.interval(5); // Interval is in Melli Second(ms)
}

void loop() {
  // put your main code here, to run repeatedly:
  debouncer.update();
  
  int value = debouncer.read();
  if (value == HIGH){
    digitalWrite(ledPin,LOW);
  }
  else{
    digitalWrite(ledPin,HIGH);
  }
}
