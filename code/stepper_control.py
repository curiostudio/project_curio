import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

motor_control_pins = [
    ([11,  7, 15, 13], "Alice"),
    ([16, 18, 22, 32], "Bob"),
    ([33, 31, 29, 35], "Charlie"),
    ([36, 37, 38, 40], "Derek"),
    ([23, 21, 19, 10], "Eddie")]

for motor in motor_control_pins:
    for pin in motor[0]:
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
    [1,0,0,1]]


def reverse_motor(motor):
    return [motor[2], motor[1], motor[0], motor[3]]


def set_5_indents(levels):
    steps_per_level = 512
    motor_steps = [0] * 5

    for i in range(5):
        motor_steps[i] = levels[i] * steps_per_level
        
    for current_full_step in range(max(levels) * steps_per_level):
        for halfstep in range(8):
            i = 0
            for motor in motor_control_pins:
                print(i)
                for pin in range(4):
                    if (current_full_step < motor_steps[i]):
                        if (levels[i] < 0):
                            GPIO.output(reverse_motor(motor[0])[pin], halfstep_seq[halfstep][pin])
                        elif (levels[i] > 0): 
                            GPIO.output(motor[0][pin], halfstep_seq[halfstep][pin])
                i = i + 1
            
            time.sleep(0.001)
#end def


def load_indents_from_file(filename):
    " load all indent information from the file and returns a list of indentations "
    filehandle = open(filename, 'r')
    ind = []

    while True:
        line = filehandle.readline()
        if (not line):
            break
        else:
            ind.append((len(line) - len(line.lstrip())) >> 2)  # asuming 4 spaces per indent level

    filehandle.close()
    return ind
#end def


def get_5_indent_values(in_buffer, start_line):
    " returns five lines from the input buffer "
    return in_buffer[start_line:start_line+5]
#end def


#############################################################
# Start of implementation                                   #
#############################################################


indents = load_indents_from_file("mock_stepper_control.py")

# Display all indents from the file
for e in indents:
    print(e)

# Select five indent values from a certain linenumber
five_indents = get_5_indent_values(indents, 37)
# TODO: calculate relative indentations 
set_5_indents(five_indents)

GPIO.cleanup()