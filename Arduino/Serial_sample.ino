#Sample program for Arduino
void setup() {
  Serial.begin(9600);
}

void loop() {
  for (int n = 0; n <1024; n++) {
    //Serial.write(n); //up to 8bit
    //int x = analogRead(A0);
    Serial.println(n, DEC);
    delay(10);
  }
}

