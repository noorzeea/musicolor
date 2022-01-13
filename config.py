import configparser


class Config:
    class __Config:
        def __init__(self):
            self.config = configparser.ConfigParser()
            self.config.read('env.ini')

        def get(self, key):
            return self.config['DEFAULT'][key]

        def set(self, key, value):
            self.config['DEFAULT'][key] = value

    CONFIG = __Config()

    @staticmethod
    def get(key):
        return Config.CONFIG.get(key)

    @staticmethod
    def getInt(key):
        return int(Config.CONFIG.get(key))

    @staticmethod
    def getFloat(key):
        return float(Config.CONFIG.get(key))

    @staticmethod
    def getBool(key):
        return (Config.CONFIG.get(key)) == "True"
