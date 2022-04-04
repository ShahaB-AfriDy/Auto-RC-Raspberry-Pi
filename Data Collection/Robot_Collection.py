
from RPi.GPIO import setmode,setup,OUT,HIGH,LOW,PWM,setwarnings,output,BOARD
from time import sleep

class Car:
    def __init__(self,EnA,N1,N2,N3,N4,EnB,Speed=25):
        self.N1 = N1
        self.N2 = N2
        self.N3 = N3
        self.N4 = N4
        self.EnA = EnA
        self.EnB = EnB
        setmode(BOARD) # type setmode
        setwarnings(False)
        setup(self.N1,OUT)
        setup(self.N2,OUT)
        setup(self.N3,OUT)
        setup(self.N4,OUT)
        setup(self.EnA,OUT)
        setup(self.EnB,OUT)
    # created object of PWM = pules Width modulation
        self.Enable_A = PWM(self.EnA,100)
        self.Enable_B = PWM(self.EnB,100)
        # Initial valule is 0
        self.Enable_A.start(0)
        self.Enable_B.start(0)
        self.speed = Speed

    def Forward(self):
        output(self.N1,HIGH)
        output(self.N2,LOW)
        self.Enable_A.start(self.speed)

        output(self.N3,HIGH)
        output(self.N4,LOW)
        self.Enable_B.start(self.speed)

    def Backward(self):
        output(self.N1,LOW)
        output(self.N2,HIGH)
        self.Enable_A.start(self.speed)

        output(self.N3,LOW)
        output(self.N4,HIGH)
        self.Enable_B.start(self.speed)

    def Left_Side(self):
        output(self.N1,HIGH)
        output(self.N2,LOW)
        self.Enable_A.start(self.speed+10)

        output(self.N3,LOW)
        output(self.N4,HIGH)
        self.Enable_B.start(self.speed-10)

    def Right_Side(self):
        output(self.N1,LOW)
        output(self.N2,HIGH)
        self.Enable_A.start(self.speed-10)

        output(self.N3,HIGH)
        output(self.N4,LOW)
        self.Enable_B.start(self.speed+10)

    def Forward_Left(self):
        output(self.N1, HIGH)
        output(self.N2, LOW)
        self.Enable_A.start(self.speed + 7)

        output(self.N3, LOW)
        output(self.N4, HIGH)
        self.Enable_B.start(self.speed - 7)

    def Forward_Right(self):
        output(self.N1, LOW)
        output(self.N2, HIGH)
        self.Enable_A.start(self.speed - 7)

        output(self.N3, HIGH)
        output(self.N4, LOW)
        self.Enable_B.start(self.speed + 7)


    def Stop_Car(self):
        output(self.N1,LOW)
        output(self.N2,LOW)
        self.Enable_A.stop()

        output(self.N3,LOW)
        output(self.N4,LOW)
        self.Enable_B.stop()

# # Directions pins
# N1, N2, N3, N4 = 11, 13, 16, 18
# # Enable pins
# EnA, EnB = 32, 33
# Start_Car = Car(N1, N2, N3, N4, EnA, EnB)
