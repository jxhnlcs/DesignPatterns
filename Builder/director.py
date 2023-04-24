from specs.body import Body
from builder import Builder
from car import Car


class Director:
    def set_builder(self, builder: Builder):
        self.__builder = builder

    def get_car(self) -> Car:
        car = Car()
        car.set_body(self.__builder.get_body())
        car.attach_wheel(self.__builder.get_wheel())
        car.set_engine(self.__builder.get_engine())
        return car
        
        