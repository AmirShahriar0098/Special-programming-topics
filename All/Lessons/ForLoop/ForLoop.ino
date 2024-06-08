int Timer = 500;

void setup() {
  for (int pinCounter = 12; pinCounter <= 13; pinCounter++){
    pinMode(pinCounter, OUTPUT);
  }
}

void loop() {
  digitalWrite(12, HIGH);
  
  for (int i = 0; i < 4; i++){
    digitalWrite(13, HIGH);
    delay(Timer);
    digitalWrite(13, LOW);
    delay(Timer);
  }
  while(1);
}
