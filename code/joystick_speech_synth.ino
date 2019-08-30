# This code will only work in certain arduino versions (Leonardo, Esplora, Zero, Due and MKR Family)

#include <Keyboard.h>
int VRx = A0;
int VRy = A1;
int SW = 2;
char altKey = KEY_LEFT_ALT;

int xPosition = 0;
int yPosition = 0;
int SW_state = 0;
int mapX = 0;
int mapY = 0;

void setup() {
  Serial.begin(9600); 
  Keyboard.begin();
  pinMode(VRx, INPUT);
  pinMode(VRy, INPUT);
  pinMode(SW, INPUT_PULLUP); 
  pinMode(2, INPUT_PULLUP);
  // initialize control over the keyboard:
  Keyboard.begin();
}

void loop() {
  xPosition = analogRead(VRx);
  yPosition = analogRead(VRy);
  SW_state = digitalRead(SW);
  mapX = map(xPosition, 0, 1023, -512, 512);
  mapY = map(yPosition, 0, 1023, -512, 512);

 if (mapX < -200) {
    Keyboard.press(130);
    Keyboard.press(102);
  }
  else if (mapX > 200)
    {
    Keyboard.press(130);
    Keyboard.press(98);
  }
  else if (mapY > 200){
    Keyboard.write(215);
    delay(100);
  }
  else if (mapY < -200){
    Keyboard.write(216);
    delay(100);
  }
  delay(100);
  Keyboard.releaseAll();
  delay(1000);
  Serial.print("X: ");
  Serial.print(mapX);
  Serial.print(" | Y: ");
  Serial.print(mapY);
  Serial.print(" | Button: ");
  Serial.println(SW_state);

  delay(100);
  
}
