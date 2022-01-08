import board
import neopixel
pixels = neopixel.NeoPixel(board.D21, 30)

for pixel in pixels:
        pixel = (255, 0, 0)