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
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]]


def static_vars(**kwargs):
    """
    Custom decorator to allow declaration of static variables like this:\n
    @static_var(variable = 0)\n
    def foo(parameters):\n
        foo.variable += 1
    """
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate
# end def


def reverse_motor(motor):
    return [motor[2], motor[1], motor[0], motor[3]]
# end def


def set_5_indents(levels):
    steps_per_level = 512
    motor_steps = [0] * 5

    for i in range(len(levels)):
        motor_steps[i] = levels[i] * steps_per_level

    for current_full_step in range(max(levels) * steps_per_level):
        for halfstep in range(8):
            i = 0
            for motor in motor_control_pins:
                if (i + 1) > len(levels):
                    break

                print(i)
                for pin in range(4):
                    if (current_full_step < motor_steps[i]):
                        if (levels[i] < 0):
                            GPIO.output(reverse_motor(motor[0])[
                                        pin], halfstep_seq[halfstep][pin])
                        elif (levels[i] > 0):
                            GPIO.output(motor[0][pin],
                                        halfstep_seq[halfstep][pin])
                i = i + 1

            time.sleep(0.001)
# end def


def load_indents_from_file(filename):
    """
    Load all indent information from the file and returns a list of
    indentations
    """
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
    " Returns five lines from the input buffer "
    return in_buffer[start_line:start_line+5]
# end def


def get_5_indent_deltas(old, new):
    return [(new[i] - old[i]) for i in range(5) if (i < len(new)) and (i < len(old))]
# end def


@static_vars(page=[0] * 5)
@static_vars(previous_page=[0] * 5)
def update_interface(start_line, visible_lines):
    " Calculates the new state of the interface "
    print("Showing lines: %d - %d" %
          (start_line + 1, start_line + visible_lines))
    update_interface.page = get_5_indent_values(indents, active_line)

    print("prev\tnext\t|\tdifference")
    for p1, p2 in zip(update_interface.previous_page, update_interface.page):
        print(p1, p2, "|", p2 - p1, sep="\t")

    update_interface.previous_page = update_interface.page
# end def


indents = load_indents_from_file("mock_stepper_control.py")

active_line = 0
display_lines = 5
total_lines = len(indents) + 1
userinput = ""

if total_lines <= 5:
    update_interface(0, total_lines)
    print("Showing lines: 1 - %d" % (total_lines))
else:
    while True:

        # User selected Next page
        if (userinput.upper() == "N") and ((active_line + 5) <= total_lines):
            active_line = active_line + 5
            display_lines = 5

        # User selected Previous page
        elif (userinput.upper() == "P") and ((active_line - 5) >= 0):
            active_line = active_line - 5
            display_lines = 5

        # User selected Quit program
        elif userinput.upper() == "Q":
            break

        # User entered invalid character
        else:
            pass

        if active_line + display_lines > total_lines:
            display_lines = total_lines - active_line

        update_interface(active_line, display_lines)
        userinput = input("(N)ext | (P)revious | (Q)uit > ")
    # end while


GPIO.cleanup()
