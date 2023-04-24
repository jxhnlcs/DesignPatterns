from specs.body import Body
from specs.engine import Engine
from specs.wheel import Wheel
from director import Director
from car_model.land_rover_builder import LandRoberBuilder
from car_model.porsche_builder import PorscheBuilder

director = Director()

print("\n------------------------------------\n")

land_rover_builder = LandRoberBuilder()
director.set_builder(land_rover_builder)
jeep = director.get_car()
jeep.specification()

print("\n------------------------------------\n")

porsche_builder = PorscheBuilder()
director.set_builder(porsche_builder)
porsche = director.get_car()
porsche.specification()

print("\n------------------------------------\n")