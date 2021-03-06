from MotorController import MotorController
from threading import Thread
from math import sin, radians

def backgroundLoop():
    controller = MotorController()

    while True:
        for i in range(0, 360):
            xVal = (sin(radians(i)) + 1) * 50
            yVal = (sin(radians(i + 90)) + 1) * 50
            controller.moveXY(xVal, yVal)

if __name__ == "__main__":
    backgroundThread = Thread(target=backgroundLoop, daemon=True)
    backgroundThread.start()

    input("Press enter to exit.")
