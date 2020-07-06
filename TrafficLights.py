# Importing
import RPi.GPIO as GPIO
import time

# Vars
OpenPins = []

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Classes
class Light:
    def __init__(self, Colour, Pin, Active):
        OpenPins.append(Pin)
        self.Colour = Colour
        self.Active = Active
        self.Pin = Pin
        GPIO.setup(Pin, GPIO.OUT, initial = self.Active)

    def Toggle(self, NewState):
        self.Active = NewState
        GPIO.output(self.Pin, NewState)

class LightSet:
    def __init__(self, RP, AP, GP):
        self.Red = Light("Red", RP, True)
        self.Amber = Light("Amber", AP, False)
        self.Green = Light("Green", GP, False)

    def ToRed(self):
        if not (self.Red.Active):
            self.Green.Toggle(False)
            self.Amber.Toggle(True)
            time.sleep(2)
            self.Amber.Toggle(False)
            self.Red.Toggle(True)

    def ToGreen(self):
        self.Red.Toggle(True)
        self.Amber.Toggle(True)
        time.sleep(2)
        self.Red.Toggle(False)
        self.Amber.Toggle(False)
        self.Green.Toggle(True)

    def GetState(self):
        return self.Red.Active, self.Amber.Active, self.Green.Active
        
Set1 = LightSet(17,27,22)
Set2 = LightSet(25,8,7)

try:
    while True:

        Set2.ToRed()
        S1S = Set1.GetState()
        S2S = Set2.GetState()

        time.sleep(2)
        Set1.ToGreen()

        time.sleep(8)

        S2S = Set2.GetState()
        S1S = Set1.GetState()

        Set1.ToRed()
        time.sleep(2)
        Set2.ToGreen()


        time.sleep(8)

except KeyboardInterrupt:
    print("\nEND\n")
    GPIO.cleanup(OpenPins)

