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

int Vl, set = 0;

void setup() {
  lcd.begin(16, 2);

  lcd.print("Hello, World!");
  lcd.setCursor(0, 1);

}

  int GetNumber(){
  int Num = 0;
  lcd.clear();
  char key = keypad.getKey();
  while (key != '='){
    switch (key){
      case NO_KEY:
      break;
      case '0': case '1': case '2': case '3': case '4':
      case '5': case '6': case '7': case '8': case '9':

      lcd.print(key);
      Num = Num * 10+ (key  - '0');
      break;

      case 'c':
      Num = 0;
      lcd.clear();
      break;
    }
    key = keypad.getKey();
  }
  return Num;
  }


void loop() {
  Vl = GetNumber();
  
  if (Vl == 456){
    lcd.clear();
    lcd.print("OK");
    digitalWrite(A0, HIGH);
    delay(2000);
    digitalWrite(A0, LOW);
  }
  else{
    lcd.clear();
    lcd.print("Error!");
  }
  delay(1000);
  
  char key = keypad.getKey();
  if (key){
    lcd.print(key);
  }
}
