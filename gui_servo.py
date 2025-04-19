from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from tkinter import *

factory = PiGPIOFactory()
servo = Servo(17, pin_factory=factory)  # change pin if needed

def move_left():
    servo.min()

def move_center():
    servo.mid()

def move_right():
    servo.max()

# GUI setup
root = Tk()
root.title("Servo Control Panel")

Button(root, text="Left", width=20, command=move_left).pack(pady=5)
Button(root, text="Center", width=20, command=move_center).pack(pady=5)
Button(root, text="Right", width=20, command=move_right).pack(pady=5)

root.mainloop()
