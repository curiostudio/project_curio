import time
import os
import linecache
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


def set_5_indents_real(object, levels):
    def reverse_motor(motor):
        return [motor[2], motor[1], motor[0], motor[3]]
    # end def

    steps_per_level = 512
    motor_steps = [0] * 5

    for i in range(len(levels)):
        motor_steps[i] = levels[i] * steps_per_level

    for current_full_step in range(max(levels) * steps_per_level):
        for halfstep in range(len(object.halfstep_seq)):
            i = 0
            for motor in object.motor_control_pins:
                if (i + 1) > len(levels):
                    break
                # end if

                for pin in range(len(object.halfstep_seq[0])):
                    if (current_full_step < motor_steps[i]):
                        if (levels[i] < 0):
                            GPIO.output(reverse_motor(motor[0])[pin], 
                                        object.halfstep_seq[halfstep][pin])
                            pass
                        elif (levels[i] > 0):
                            GPIO.output(motor[0][pin],
                                        object.halfstep_seq[halfstep][pin])
                            pass
                        # end if
                    # end if
                # end for
                
                i = i + 1
            # end for
            
            time.sleep(1)
            userinput = input(".")
            
        # end for
    # end for
# end def


class stepper_control:
    def __init__(self):
        self.motor_control_pins = [
            ([13, 15, 11,  7], "Alice"),
            ([32, 22, 16, 18], "Bob"),
            ([33, 31, 29, 35], "Charlie"),
            ([37, 40, 38, 36], "Derek"),
            ([10, 23, 21, 19], "Eddie")] 
        
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
# end class stepper_control
    
stepper = stepper_control()
stepper.set_indents([1, 1, 1, 1, 1])

GPIO.cleanup()