#include <Bounce2.h> // Add Library
#define buttonPin 2 // Define a constanct
#define ledPin 13

Bounce debouncer = Bounce(); // Create a variable from Bounce class(Library)

unsigned long BtnPressTime;
void setup() {
  Serial.begin(250000);
  pinMode(ledPin,OUTPUT);
  pinMode(buttonPin,INPUT_PULLUP);
  
  debouncer.attach(buttonPin); // Connect BPin to Debouncer
  debouncer.interval(5); // Interval is in Melli Second(ms)}
}
void loop() {
  debouncer.update();
  
  if (debouncer.fell()){
    Serial.print("<");
     Serial.print(millis() - BtnPressTime);
      Serial.println(">");
    BtnPressTime = millis();
  }

}
