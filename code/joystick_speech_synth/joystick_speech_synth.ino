#include "Joystick.h"

Joystick joystick(A2, A3);

void setup()
{
  Serial.begin(9600);
  joystick.calibrate();
}

void print_joystick_command(const Joystick& input)
{
  static constexpr uint16_t JOYSTICK_RESPONSE_RADIUS = 255;

  int16_t x_deflection = input.getX();
  int16_t y_deflection = input.getY();

  if (input.isPressed()) {
    Serial.println("READ THIS");
  }
  else {
    if (abs(y_deflection) > JOYSTICK_RESPONSE_RADIUS) {
      if (y_deflection > 0) {
        Serial.println("PREVIOUS LINE");
      }
      else {
        Serial.println("NEXT LINE");
      }
    }
    else if (abs(x_deflection) > JOYSTICK_RESPONSE_RADIUS) {
      if (x_deflection > 0) {
        Serial.println("NEXT PAGE");
      }
      else {
        Serial.println("PREVIOUS PAGE");
      }
    }
    else {
      // Ignore joystick movement
    }
  }
}

void loop()
{
  Serial.println("X,Y");
  Serial.print(joystick.getX(), DEC);
  Serial.print(",");
  Serial.println(joystick.getY(), DEC);
  print_joystick_command(joystick);
  delay(200);

  joystick.process();
}
