# import RPi.GPIO as GPIO
import time
import os
import linecache
#import RPi.GPIO as GPIO
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)


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


def set_5_indents_real(object, levels):
    def reverse_motor(motor):
        return [motor[2], motor[1], motor[0], motor[3]]
    # end def

    steps_per_level = 512
    motor_steps = [0] * 5

    for i in range(len(levels)):
        motor_steps[i] = levels[i] * steps_per_level

    for current_full_step in range(max(levels) * steps_per_level):
        for halfstep in range(8):
            i = 0
            for motor in object.motor_control_pins:
                if (i + 1) > len(levels):
                    break

                print(i)
                for pin in range(4):
                    if (current_full_step < motor_steps[i]):
                        if (levels[i] < 0):
                            GPIO.output(reverse_motor(motor[0])[pin], 
                                        object.halfstep_seq[halfstep][pin])
                        elif (levels[i] > 0):
                            GPIO.output(motor[0][pin],
                                        object.halfstep_seq[halfstep][pin])
                i = i + 1

            time.sleep(0.001)
# end def


def set_5_indents_mock(object, levels):
    steps_per_level = 512
    motor_steps = [0] * 5

    for i in range(len(levels)):
        motor_steps[i] = levels[i] * steps_per_level

    for current_full_step in range(max(levels) * steps_per_level):
        i = 0  # Keeps track of the motor indices
        for motor in object.motor_control_pins:
            if (i + 1) > len(levels):
                break
            # end if

            if current_full_step < abs(motor_steps[i]):
                if levels[i] > 0:
                    print("Forward: {0}", motor[1])
                elif levels[i] < 0:
                    print("Reverse: {0}", motor[1])
                else:
                    pass  # The else-clause should never be visited
                # end if
            # end if
            i = i + 1
        # end for
# end def


class indent_decoder:
    def __init__(self, filename):
        self.indentations = []
        self.filehandle = open(filename, 'r')
        return
    # end def


    def load_indents_from_file(self):
        """
        Load all indent information from the file and returns a list of
        indentations
        """
        while True:
            line = self.filehandle.readline()
            if (not line):
                break
            else:
                # asuming 4 spaces per indent level
                self.indentations.append((len(line) - len(line.lstrip())) >> 2)
            # end if
        # end while 

        self.filehandle.close()
        return self.indentations
    # end def
# end class


class stepper_control:
    def __init__(self):
        self.motor_control_pins = [
            ([11,  7, 15, 13], "Alice"),
            ([16, 18, 22, 32], "Bob"),
            ([33, 31, 29, 35], "Charlie"),
            ([36, 37, 38, 40], "Derek"),
            ([23, 21, 19, 10], "Eddie")]
        
        self.halfstep_seq = [
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 1]]
        return
    # end if


    def set_indents(self, levels):
        set_5_indents_mock(self, levels)
        return
    # end if
# end class


class curio:
    def __init__(self, filename):
        self.indents = indent_decoder(filename)
        self.steppers = stepper_control
        self.active_line = 0
        self.speech_line = 0
        self.display_lines = 5
        self.total_lines = len(self.indents) + 1
        return
    # end def


    def next_page(self):
        self.active_line = self.active_line + 5
        self.speech_line = 1
        self.display_lines = 5
        return
    # end def


    def previous_page(self):
        self.active_line = self.active_line - 5
        self.speech_line = 1
        self.display_lines = 5
        return
    # end def
# end class

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


curio_app = curio("stepper_controll.py")

userinput = ""

if total_lines <= 5:
    update_interface(0, total_lines)
    print("Showing lines: 1 - %d" % (total_lines))
else:
    while True:

        # User selected Next page
        if (userinput == "n") and ((active_line + 5) <= total_lines):
            next_page()

        # User selected Previous page
        elif (userinput == "p") and ((active_line - 5) >= 0):
            previous_page()

        # User selected Quit program
        elif userinput == "q":
            break

        elif userinput.isdigit():
            if (int(userinput) > 0) and (int(userinput) <= 5):
                speech_line = active_line + int(userinput)
                print("Active line: %d\n" % int(userinput))
            else:
                print("Number not in range [1-5]\n")

        elif userinput.isalpha():
            if (userinput >= "A") and (userinput <= "Z"):
                word_number = ord(userinput[0]) - ord("A")
                print("word# %d" % word_number)
                print(fetch_word(filename, speech_line, word_number))
            else:
                print("Letter not in range [A-Z]\n")

        # User entered invalid character
        else:
            pass

        if active_line + display_lines > total_lines:
            display_lines = total_lines - active_line

        update_interface(active_line, display_lines)
        userinput = input("(N)ext | (P)revious | Relative line#[1-5] | Word# in line[A-Z] | (Q)uit > ")
    # end while
