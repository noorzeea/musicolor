class STATES:
    OFF = 0
    ON = 1


class CHANNELS(object):
    RED = 16
    GREEN = 20
    BLUE = 21

    def find_gpio(self, color):

        if color == 'red': return self.RED
        if color == 'blue': return self.BLUE
        if color == 'green': return self.GREEN

        return Exception("Color not found")
