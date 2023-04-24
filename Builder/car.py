from specs.body import Body
from specs.engine import Engine
from specs.wheel import Wheel

class Car:
    def __init__(self) -> None:
        self.__wheels: Wheel = list()
        self.__engine: Engine = None
        self.__body:Body = None

    def set_body(self, body):
        self.__body = body

    def attach_wheel(self, wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine):
        self.__engine = engine

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d\'" % self.__wheels[0].size)