int Timer = 500;           // The higher the number, the slower the timing.

void setup() {
  // use a for loop to initialize each pin as an output:
  for (int currntPin = 2; currntPin <= 7; currntPin++) {
    pinMode(currntPin, OUTPUT);
  }
}

void loop() {
  // loop from the lowest pin to the highest:
  for (int currntPin = 2; currntPin <= 7; currntPin++) {
    // turn the pin on:
    digitalWrite(currntPin, HIGH);
    delay(Timer);
    // turn the pin off:
    digitalWrite(currntPin, LOW);
  }

  // loop from the highest pin to the lowest:
  for (int currntPin = 7; currntPin >= 2; currntPin--) {
    // turn the pin on:
    digitalWrite(currntPin, HIGH);
    delay(Timer);
    // turn the pin off:
    digitalWrite(currntPin, LOW);
  }
}
