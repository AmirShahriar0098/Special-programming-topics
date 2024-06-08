#include <LiquidCrystal.h>
#include <Keypad.h>

const byte ROWS = 4;
const byte COLS = 4;

char keys[ROWS][COLS] = {
  {'7', '8', '9', '/'},
  {'4', '5', '6', '*'},
  {'1', '2', '3', '-'},
  {'c', '0', '=', '+'}
};

byte rowPins[ROWS] = {7, 6, 5, 4};
byte colPins[COLS] = {3, 2, 1, 0};

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

LiquidCrystal lcd(13, 12, 11, 10, 9, 8);

float Num1, Num2, Result;
char Operation;

void setup() {
  lcd.begin(16, 2);
  lcd.print("Calculator");
  delay(1500);
  lcd.clear();
}

void loop() {
  char key = keypad.getKey();
  if (key) {
    if (key == '=') {
      // Perform the operation
      switch (Operation) {
        case '+':
          Result = Num1 + Num2;
          break;
        case '-':
          Result = Num1 - Num2;
          break;
        case '*':
          Result = Num1 * Num2;
          break;
        case '/':
          Result = Num1 / Num2;
          break;
      }
      // Display the result
      lcd.setCursor(0, 0);
      lcd.print("Result: ");
      lcd.print(Result);
    } else if (key == '+' || key == '-' || key == '*' || key == '/') {
      // Store the operation
      Operation = key;
      // Clear the LCD
      lcd.clear();
    } else {
      // Store the number
      if (Num1 == 0) {
        Num1 = key - '0';
      } else {
        Num2 = key - '0';
      }
      // Display the number
      lcd.setCursor(0, 0);
      lcd.print(Num1);
      lcd.print(" ");
      lcd.print(Operation);
      lcd.print(" ");
      lcd.print(Num2);
    }
  }
}
