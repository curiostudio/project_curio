#ifndef JOYSTICK_H_
#define JOYSTICK_H_

#include <Arduino.h>

template <typename T> 
struct lmh_t {
  T low;
  T mid;
  T high;  
};

// This three-point map function overloads the existing two-point map function
template <typename T> 
T map(T in, lmh_t<T> from, lmh_t<T> to)
{
  T mapped_val;
  
  if (in < from.mid) {
    mapped_val = map(in, from.low, from.mid, to.low, to.mid);
  }
  else {
    mapped_val = map(in, from.mid, from.high, to.mid, to.high);
  }
  
  return mapped_val;  
}

class Joystick
{
  public:

    Joystick(int pin_x, int pin_y);
    int16_t getX() const;
    int16_t getY() const;
    bool isPressed() const;

    void calibrate();
    void process();

  private:

    static constexpr int16_t X_PRESSED_VALUE = 1023;
    static constexpr int16_t LOW_COORD_VALUE = -512;
    static constexpr int16_t HIGH_COORD_VALUE = 512;

    int pin_x_ = 0;
    int pin_y_ = 0;

    lmh_t<int16_t> x_limits_{HIGH_COORD_VALUE, LOW_COORD_VALUE, 0};
    lmh_t<int16_t> y_limits_{HIGH_COORD_VALUE, LOW_COORD_VALUE, 0};
    int16_t x_ = 0;
    int16_t y_ = 0;
    int16_t raw_x_ = 0;
    int16_t raw_y_ = 0;
    bool    pressed_ = false;
};

#endif // JOYSTICK_H_
