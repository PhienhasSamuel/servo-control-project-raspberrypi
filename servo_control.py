from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# Use pigpio for smoother PWM
factory = PiGPIOFactory()
servo = Servo(18, pin_factory=factory)  # GPIO18 (Pin 12)

print("Moving servo between 0°, 90°, 180°...")

while True:
    servo.min()   # 0 degrees
    print("Position: 0°")
    sleep(1)
    servo.mid()   # 90 degrees
    print("Position: 90°")
    sleep(1)
    servo.max()   # 180 degrees
    print("Position: 180°")
    sleep(1)
