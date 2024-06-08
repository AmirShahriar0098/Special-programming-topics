#include <LiquidCrystal.h>

// Define the LCD pins
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;

// Create an instance of the LCD library
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  // Initialize the LCD
  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.print("Digital Clock");
  delay(1000);
  lcd.clear();
}

// Function to get the current hour
int Hour() {
  return (millis() / 3600000) % 24;
}

// Function to get the current minute
int Minute() {
  return (millis() / 60000) % 60;
}

// Function to get the current second
int Second() {
  return (millis() / 1000) % 60;
}

void loop() {
  // Get the current time
  int Hours = Hour();
  int Minutes = Minute();
  int Seconds = Second();

  // Display the time on the LCD
  lcd.setCursor(0, 0);
  lcd.print(Hours);
  lcd.print(":");
  if (Minutes < 10) {
    lcd.print("0");
  }
  lcd.print(Minutes);
  lcd.print(":");
  if (Seconds < 10) {
    lcd.print("0");
  }
  lcd.print(Seconds);

  // Update the display every second
  delay(1000);
}
