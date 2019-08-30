import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

motor_control_pins = [
    [11,  7, 15, 13], # Alice
    [16, 18, 22, 32], # Bob
    [33, 31, 29, 35], # Charlie
    [36, 37, 38, 40], # Derek
    [23, 21, 19, 10]] # Eddie

for motor in motor_control_pins:
    for pin in motor:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
  
halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

def reverse_motor(motor):
    return [motor[2], motor[1], motor[0], motor[3]]

def set_5_indents(levels, backwards=False):
    steps_per_level = 512;
    motor_steps = [0] * 5

    for i in range(5):
        motor_steps[i] = levels[i] * steps_per_level
        
    for current_full_step in range(max(levels) * steps_per_level):
        if (not backwards):
            halfstep_range = range(8)
        else:
            halfstep_range = reversed(range(8))
            
        for halfstep in halfstep_range:
            i = 0
            for motor in motor_control_pins:
                for pin in range(4):
                    if (current_full_step < motor_steps[i]):
                        GPIO.output(motor[pin], halfstep_seq[halfstep][pin])
                i = i + 1
            
            time.sleep(0.001)

filehandle = open("indent_decode.py", 'r')
ind = []
empty = 0
j = 0
while True:
    line = filehandle.readline()
    if not line:
        break;
    elif (len(line.strip())==0):
        ind.append(empty)
        j=j+1
    else:
        leading_spaces = len(line) - len(line.lstrip())
        ind.append(leading_spaces)
        j=j+1

filehandle.close()
# ind[] ready for use

set_5_indents([2,4,2,1,0])
set_5_indents([2,4,2,1,0], True)


GPIO.cleanup()