from abc import ABC, abstractmethod

from specs.body import Body
from specs.engine import Engine
from specs.wheel import Wheel


class Builder(ABC):
    @abstractmethod
    def get_wheel(self) -> Wheel: pass

    @abstractmethod
    def get_engine(self) -> Engine: pass

    @abstractmethod
    def get_body(self) -> Body: pass