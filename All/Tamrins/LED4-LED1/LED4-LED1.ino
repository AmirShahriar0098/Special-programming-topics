#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 9, 8, 7, 6);

const int YledPin = 2;
const int GledPin = 3;
const int bPin = 5;

int Counter = 0;
int btnState = HIGH; // initialize button state to HIGH

void setup() {
  lcd.begin(16, 2);
  
  pinMode(YledPin, OUTPUT);
  pinMode(GledPin, OUTPUT);
  
  pinMode(bPin, INPUT_PULLUP);
}

void loop() {
  int currentState = digitalRead(bPin);
  
  if (currentState == LOW && btnState == HIGH) {
    Counter++;
    btnState = LOW; // update button state
  } else if (currentState == HIGH) {
    btnState = HIGH; // update button state
  }
  
  if (Counter == 3) {
    Counter = 0;
    if (digitalRead(YledPin)  == HIGH){
      digitalWrite(YledPin, LOW);
    }
    else{
      digitalWrite(YledPin, HIGH);
    }
  }


    if (currentState == LOW){
    digitalWrite(GledPin,HIGH);
  }
  else{
    digitalWrite(GledPin,LOW);
  }
  
  lcd.setCursor(0, 1);
  lcd.print("Counter: ");
  lcd.print(Counter);
  lcd.print("   "); // clear the rest of the line
}
