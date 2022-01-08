import RPi.GPIO as GPIO
from constants import STATES, CHANNELS

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

def main(color):

    channels = CHANNELS()
    channel = channels.find_gpio(color=color)

    print(f"CHANNEL IS: {channel}")

    if GPIO.input(channel) is STATES.OFF:
        GPIO.output(channel, GPIO.HIGH)
    else:
        GPIO.output(channel, GPIO.LOW)



if __name__ == '__main__':
    color = input("color: ")

    main(color)



