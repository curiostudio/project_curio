# import RPi.GPIO as GPIO
import time


motor_control_pins = [
    ([11,  7, 15, 13], "Alice"),
    ([16, 18, 22, 32], "Bob"),
    ([33, 31, 29, 35], "Charlie"),
    ([36, 37, 38, 40], "Derek"),
    ([23, 21, 19, 10], "Eddie")]

halfstep_seq = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]]


def reverse_motor(motor):
    return ([motor[0][2], motor[0][1], motor[0][0], motor[0][3]], motor[1])
# end def


def set_5_indents(levels):
    steps_per_level = 1
    motor_steps = [0] * 5

    for i in range(5):
        motor_steps[i] = levels[i] * steps_per_level

    for current_full_step in range(max(levels) * steps_per_level):
        i = 0  # Keeps track of the motor indices
        for motor in motor_control_pins:
            if (current_full_step < abs(motor_steps[i])):
                if (levels[i] > 0):
                    print("Forward: {0}", motor[1])
                elif (levels[i] < 0):
                    print("Reverse: {0}", motor[1])
                else:
                    pass  # The else-clause should never be visited
            i = i + 1
# end def


def load_indents_from_file(filename):
    " load all indent information from the file and returns a list of indentations "
    filehandle = open(filename, 'r')
    ind = []

    while True:
        line = filehandle.readline()
        if (not line):
            break
        else:
            # asuming 4 spaces per indent level
            ind.append((len(line) - len(line.lstrip())) >> 2)

    filehandle.close()
    return ind
# end def


def get_5_indent_values(in_buffer, start_line):
    " returns five lines from the input buffer "
    return in_buffer[start_line:start_line+5]
# end def


indents = load_indents_from_file("mock_stepper_control.py")

# Display all indents from the file
for e in indents:
    print(e)

# Select five indent values from a certain linenumber
five_indents = get_5_indent_values(indents, 37)
# TODO: calculate relative indentations
set_5_indents(five_indents)
