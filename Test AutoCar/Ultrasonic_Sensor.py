# from RPi.GPIO import setmode, setup, OUT, \
#     HIGH, LOW, PWM, setwarnings, output, BOARD, IN, cleanup
# from time import sleep,time


# # stop = 0
# class Ultrasonics_Sensor(object):
#     def __init__(self,Trigger,Echo):
#         setmode(BOARD)
#         setwarnings(False)
#         self.GPIO_TRIGGER = Trigger
#         self.GPIO_ECHO = Echo
#         setup(self.GPIO_TRIGGER,OUT)
#         setup(self.GPIO_ECHO,IN)
#         output(self.GPIO_TRIGGER, False) # initialize trigger pin to low

#     def Measurement(self):
#         output(self.GPIO_TRIGGER, True)
#         sleep(0.00001)
#         output(self.GPIO_TRIGGER, False)
#         start = time()
#         stop = 0
#         while input(self.GPIO_ECHO)==0:
#             start = time()

#         while input(self.GPIO_ECHO)==1:
#             stop = time()

#         Elapsed = stop-start
#         Distance = (Elapsed * 34300)/2

#         return Distance

# if __name__ == '__main__':
#     try:
#         Sensor = Ultrasonics_Sensor(20,30)
#         while True:
#             distance = Sensor.Measurement()
#             # if distance <= 40: # cm
#             #     # Car.stop()
#             print("Distance : %.1f cm" % distance)
#     finally:
#         cleanup()


# def nb_dig(n,d):
#     List = [u*u for u in range(n+1)]
#     List = list(map(str,List))
#     print(List)
#     L = []
#     for u in List:
#         L.append(u.count(str(d)))
#     print(sum(L))

# # nb_dig(25,1)

# print('121'.count(str(1)))


# def mult_two(a, b):
#     return multiply_of_a_and_b   if False else a*b

# print(mult_two(2,3))

# def Name(B):
#     print(B.split(' ')[0])

# Name("Shahab Ali")





import os

print(os.listdir(os.getcwd()))







