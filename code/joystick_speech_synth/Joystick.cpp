#include "Joystick.h"

Joystick::Joystick(int pin_x, int pin_y) :
  pin_x_(pin_x), pin_y_(pin_y)
{
  pinMode(pin_x, INPUT);
  pinMode(pin_y, INPUT);
}

int16_t Joystick::getX() const
{
  static int16_t prev_x = 0;
  if (!isPressed()) {
    prev_x = x_;
    return x_;
  }
  return prev_x;
}

int16_t Joystick::getY() const
{
  static int16_t prev_y = 0;
  if (!isPressed()) {
    prev_y = y_;
    return y_;
  }
  return prev_y;
}

bool Joystick::isPressed() const
{
  return pressed_;
}

void Joystick::calibrate()
{
  analogRead(pin_x_); // Discard first reading to avoid crosstalk
  x_limits_.mid = analogRead(pin_x_);
  analogRead(pin_y_); // Discard first reading to avoid crosstalk
  y_limits_.mid = analogRead(pin_y_);

  while (1) {
    analogRead(pin_x_); // Discard first reading to avoid crosstalk
    raw_x_ = analogRead(pin_x_);
    analogRead(pin_y_); // Discard first reading to avoid crosstalk
    raw_y_ = analogRead(pin_y_);

    if (X_PRESSED_VALUE == raw_x_) {
      break;
    }

    x_limits_.low  = min(raw_x_, x_limits_.low);
    x_limits_.high = max(raw_x_, x_limits_.high);
    y_limits_.low  = min(raw_y_, y_limits_.low);
    y_limits_.high = max(raw_y_, y_limits_.high);

    // DEBUG CODE
    if (0 == (millis() % 1000)) {
      Serial.print(x_limits_.low);
      Serial.print(',');
      Serial.print(x_limits_.high);
      Serial.print(',');
      Serial.print(y_limits_.low);
      Serial.print(',');
      Serial.println(y_limits_.high);
    }
  }
}

void Joystick::process()
{
  raw_x_ = analogRead(pin_x_);
  raw_y_ = analogRead(pin_y_);

  x_ = map(raw_x_, {x_limits_.low, x_limits_.mid, x_limits_.high}, 
                   {LOW_COORD_VALUE, 0, HIGH_COORD_VALUE});
  y_ = map(raw_y_, {y_limits_.low, y_limits_.mid, y_limits_.high}, 
                   {LOW_COORD_VALUE, 0, HIGH_COORD_VALUE});

  pressed_ = (X_PRESSED_VALUE == raw_x_);
}
