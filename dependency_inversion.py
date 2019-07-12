from abc import ABCMeta, abstractmethod


class IOpenAndClose(metaclass=ABCMeta):
    @abstractmethod
    def open(self):
        pass


class ITV(metaclass=ABCMeta):
    @abstractmethod
    def play(self):
        pass


class OpenAndClose(IOpenAndClose):
    def __init__(self, tv):
        self.tv = tv

    def open(self):
        self.tv.play()


class TV(ITV):
    def play(self):
        print('tv is playing!')


if __name__ == '__main__':
    OpenAndClose(TV()).open()
