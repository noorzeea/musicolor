import RPi.GPIO as GPIO
from constants import STATES, CHANNELS


import requests

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)


def get_track_id():
    track_id = 'pippo'
    return track_id


def get_song_analisys(track_id):
    return requests.get(f"https://api.spotify.com/v1/audio-analysis/{track_id}")


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



