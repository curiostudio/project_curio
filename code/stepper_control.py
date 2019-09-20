import time
import os
import linecache
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


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


class indent_decoder:
    def load_file(self, filename):
        """
        Load all indent information from the file and returns a list of
        indentations
        """

        print(f"[indent_decoder] Opening file: {filename}.")

        with open(filename, 'r') as f:
            content = f.readlines()

        self.indentations = [(len(line) - len(line.lstrip())) >> 2 for line in content]

        print(f"[indent_decoder] Loaded {len(self.indentations)} lines.")

    # end def


    def get_values(self, start_line, num=5):
        " Returns five lines from the input buffer "
        return self.indentations[start_line:start_line+num]
    # end def

    def get_total_lines(self):
        return len(self.indentations)
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

        for motor in self.motor_control_pins:
            for pin in motor[0]:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, 0)
            # end for
        # end for
    # end def


    def set_indents(self, levels):
        set_5_indents_real(self, levels)
        return
    # end if
# end class


class curio:
    def __init__(self):
        self.active_line = 0
        self.speech_line = 0
        self.display_lines = 5
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

    def get_line_from_file(self, linenumber):
        return []
    # end def

    def run(self):
        pass
    # end def
# end class


curio_app = curio()
indents = indent_decoder()
indents.load_file("mock_stepper_control.py")
steppers = stepper_control()

active_line = 0
display_lines = 5
userinput = ""


@static_vars(page=[0] * 5)
@static_vars(previous_page=[0] * 5)
def update_interface(start_line, visible_lines):
    " Calculates the new state of the interface "
    print(f"Showing lines: {start_line + 1} - {start_line + visible_lines}")
    update_interface.page = indents.get_values(active_line)

    print("prev\tnext\t|\tdifference")
    levels = []
    for p1, p2 in zip(update_interface.previous_page, update_interface.page):
        print(p1, p2, "|", p2 - p1, sep="\t")
        levels.append(p2 - p1)

    steppers.set_indents(levels)

    update_interface.previous_page = update_interface.page
# end def


if indents.get_total_lines() <= 5:
    update_interface(0, indents.get_total_lines())
    print(f"Showing lines: 1 - {indents.get_total_lines()}")
else:
    while True:

        curio_app.run()

        # User selected Next page
        if (userinput == "n") and ((active_line + 5) <= indents.get_total_lines()):
            active_line = active_line + 5
            speech_line = 1
            display_lines = 5

        # User selected Previous page
        elif (userinput == "p") and ((active_line - 5) >= 0):
            active_line = active_line - 5
            speech_line = 1
            display_lines = 5

        # User selected Quit program
        elif userinput == "q":
            break

        elif userinput.isdigit():
            if (int(userinput) > 0) and (int(userinput) <= 5):
                speech_line = active_line + int(userinput)
                print(f"Active line: {int(userinput)}\n")
            else:
                print("Number not in range [1-5]\n")

        elif userinput.isalpha():
            if (userinput >= "A") and (userinput <= "Z"):
                word_number = ord(userinput[0]) - ord("A")
                print(f"word# {word_number}")
                #  `print(fetch_word(filename, speech_line, word_number))
            else:
                print("Letter not in range [A-Z]\n")

        # User entered invalid character
        else:
            pass

        if active_line + display_lines > indents.get_total_lines():
            display_lines = indents.get_total_lines() - active_line

        update_interface(active_line, display_lines)
        userinput = input("(N)ext | (P)revious | Relative line#[1-5] | Word# in line[A-Z] | (Q)uit > ")
    # end while
