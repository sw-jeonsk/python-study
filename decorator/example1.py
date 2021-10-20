class Decorator:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print('전처리')
        print(self.function(*args, **kwargs))
        print('후처리')

@Decorator
def example():
    return '클래스'



class MainProcess:
    def __init__(self, function):
        print("__init__")
        self.function = function

    def __call__(self, *args, **kwargs):
        print('전처리')
        print(self.function())
        self.__del__()

    def __del__(self):
        print("__del__")

@MainProcess
def add():
    return 1 + 1

@MainProcess
def delete():
    return 1 - 1


