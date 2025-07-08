import time
import serial
import serial.serialutil
import threading
from base_serial import AbstractSerialHandler


class Serial_Arduino(AbstractSerialHandler):
    def __init__(self):
        self.serial_port = None
        self.secure_disconnection = False
        self.is_connected = False
        self.is_decode_error = False
        self.is_running = False
    
    def read_data(self):
        if self.serial_port and self.serial_port.is_open:
            try:
                self.data = self.serial_port.read(1024).decode().strip()
                if self.data:
                        #Aquí va trigger_event ??
                        #aquí se pueden enviar los datos al controlador que le sean útiles
                        #a través de trigger_event ??
                    return self.data
            except serial.SerialException:
                self.secure_disconnection = False
                self.is_connected = False
                self.is_decode_error = False
            except UnicodeDecodeError:
                self.secure_disconnection = False
                self.is_connected = False
                self.is_decode_error = True
        return None
    
    def verify_connection(self, serial_port, event_callback = None):
        self.serial_port = serial_port
        time.sleep(0.08)
        self.serial_port.write(b"Primer contacto")
        response = self.serial_port.read(20).decode().strip()
        if response:    
            if 'READY' in response:
                return True
            if 'BUSY' in response:
                self.serial_port.write(b"\x30\x0d")
                response = self.serial_port.read(20).decode().strip()
                if '%' in response:
                    return True
                else:
                    if event_callback:
                        event_callback("restart_controller") #mandar un mensaje al usuario de que el control está ocupado y 
                        return None                          #necesita ser reiniciado.
            if event_callback:
                event_callback("wrong_port")
        return False
    
    def sensors(self, routine, event_callback = None):
        #The serial port is the same used in the verification method, it cannot be different because before doing the sensors 
        #routine you always have to be connected and therefore the connection always has to be verified
        time_between_steps = 1
        """NEVER EVER USE THIS VALUE SMALLER THAN THE TIMEOUT"""
        
        self.is_running = True
        
        def internal_routine():
            try: 
                self.serial_port.write(b"Hola")
            except (IndexError, AttributeError):
                try:
                    for i in range(3):
                        self.serial_port.write(b"\x30\x0d")
                        time.sleep(time_between_steps)
                except (serial.SerialException, serial.serialutil.SerialException):
                    self.secure_disconnection = False
                    self.is_connected = False
                    self.is_decode_error = False
                    if event_callback:
                        event_callback("unexpected_disconnection")
                        event_callback("unable_to_finish_routine")  
            except (serial.SerialException, serial.serialutil.SerialException):
                self.secure_disconnection = False
                self.is_connected = False
                self.is_decode_error = False 
                if event_callback:
                    event_callback("unexpected_disconnection")
                    event_callback("unable_to_finish_routine")
            except UnicodeDecodeError:
                self.secure_disconnection = False
                self.is_connected = False
                self.is_decode_error = True
                if event_callback:
                    event_callback("unexpected_disconnection")
                    event_callback("unable_to_finish_routine")
            finally:
                self.is_running = False
        threading.Thread(target=internal_routine, daemon=True).start() 
        
    