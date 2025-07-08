from abc import ABC, abstractmethod

class AbstractSerialHandler(ABC):
    @abstractmethod
    def verify_connection(self, serial_port, event_callback=None) -> bool | None:
        pass

    @abstractmethod
    def sensors(self, routine, event_callback=None):
        pass