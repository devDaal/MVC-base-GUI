import serial
import serial.tools.list_ports
import threading
import time
from .base import ObservableModel
from serial_handler.serial_arduino import Serial_Arduino

class SerialManager(ObservableModel):
    
    def __init__(self):
        super().__init__()
        self.serial_port = None
        self.port_name = None
        self.ports = None
        
        self.protocols = {
                        'ard': Serial_Arduino()}
        
        self.current_protocol = None
        
        self.list_ports()

    @property
    def is_connected(self):
        if self.current_protocol is not None:
            return self.current_protocol.is_connected
        return False
    
    @is_connected.setter
    def is_connected(self, state = bool):
        self.current_protocol.is_connected = state
    
    @property
    def is_running(self):
        if self.current_protocol is not None:
            return self.current_protocol.is_running
        return False
    
    @is_running.setter
    def is_running(self, state):
        self.current_protocol.is_running = state
    
    @property
    def secure_disconnection(self):
        return self.current_protocol.secure_disconnection
    
    @secure_disconnection.setter
    def secure_disconnection(self, state):
        self.current_protocol.secure_disconnection = state
    
    @property
    def is_decode_error(self):
        return self.current_protocol.is_decode_error
    
    @is_decode_error.setter
    def is_decode_error(self, state):
        self.current_protocol.is_decode_error = state


    def list_ports(self):
        """The filters here are for the devDaal's computer, adapt for the needs of the release version.
            If the release is on raspberry pi, it probably won't need the intel filter."""
        
        self.port_list = []
        self.ports = serial.tools.list_ports.comports()
        for port in self.ports:
            desc = port.description.lower()
            if "intel" in desc or "bluetooth" in desc:
                continue
            else:
                self.port_list.append(port.device)
        self.trigger_event("update_ports")
        
    def update_current_protocol(self, protocol):
        self.current_protocol = self.protocols[protocol]
        
        
    def read_data(self):
        if self.serial_port and self.serial_port.is_open:
            #Variable de sincronía = False
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
            except AttributeError:
                self.secure_disconnection = True
                self.is_connected = False
                self.is_decode_error = False
        return None
    
    def connect(self, port_to_open, baudrate, timeout, protocol):
        timeout = timeout
        if port_to_open == "No ports available":
            self.trigger_event("no_available_ports")
        else:
            try:
                self.serial_port = serial.Serial(port_to_open, baudrate, timeout = 0.5)
                verification = self.verify_connection(protocol)
                if verification:
                    self.is_connected = True
                    self.port_name = port_to_open
                    return True
                elif verification is False:
                    self.trigger_event("wrong_port")
                self.serial_port.close()                    
                return False
            except serial.SerialException as e:
                print(f"Error al conectar: {e}")
                self.is_connected = False
                return False
    
    def disconnect(self):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            self.is_connected = False
            self.port_name = None
            self.secure_disconnection = True
    
    def toggle_connection(self, port_to_open, port_config, protocol):
        baudrate = port_config['baudrate']
        timeout = port_config['timeout']
        if self.is_connected:
            self.disconnect()
            self.trigger_event("update_connection_status")
        else:
            selected_port = port_to_open
            if selected_port:
                success = self.connect(selected_port,baudrate,timeout, protocol)
                if success:
                    self.trigger_event("update_connection_status")
                    self.start_monitoring()
    
    def verify_connection(self,protocol):
        self.update_current_protocol(protocol)
        def event_callback(event, *args):
            self.trigger_event(event, *args)
        #Este if no va a ser necesario cuando pueda usar los demás protocolos. Simplemente hay que hacer:
        #return self.current_protocol.verify_connnection(self.serial_port, event_callback)
        if protocol == 'ltz':
            if self.current_protocol.verify_connection(self.serial_port, event_callback):
                return True
        elif protocol == 'sh':
            print("sheffield")
        else:
            print("pantec")
            return False                
        #Para cada protocolo hay una mensajito que se puede enviar sabiendo qué va a responder el control
        #Si responde lo esperado, devolver True, caso contrario devuelve False
    
    def start_monitoring(self):
        """This method is useful because serial connection doesn't have a way to let you know
        when it fails. I used the if self.is_running structure to stop monitoring while 
        something is running, because it leads to race conditions either with the buffer or 
        trying to read and write at the same time.
        """
        def monitor():
            while self.is_connected:
                try:
                    if self.is_running:
                        time.sleep(0.5)
                        continue
                    else:          
                        data = self.read_data()
                        if data is None and not self.is_connected:
                            if not self.secure_disconnection:
                                self.trigger_event("unexpected_disconnection")
                            break        
                    time.sleep(0.5)
                except serial.SerialException:
                    self.secure_disconnection = False
                    self.is_connected = False
                    self.is_decode_error = False
                except UnicodeDecodeError:
                    self.secure_disconnection = False
                    self.is_connected = False
                    self.is_decode_error = True
        threading.Thread(target=monitor, daemon=True).start()
    
    def leitz_sensor_routine(self,routine):
        """Probably this name will be just sensors_routine when there are more protocols, because the important
        logic is on each protocol module for serial communication. This only will be the base."""
        def event_callback(event, *args):
            self.trigger_event(event, *args)
        self.current_protocol.sensors(routine, event_callback)
        
    def serial_status_routine(self, status_routine):
        def event_callback(event, *args):
            self.trigger_event(event, *args)
        self.current_protocol.status(status_routine, event_callback)
       
    def reset_connection(self):
        if self.serial_port and self.serial_port.is_open:    
            print("Enviando: ctrl + ECB")
            
    def test_soft(self):
        if self.serial_port and self.serial_port.is_open:
            print("Enviando: testsoft")
            #self.serial_port.write(b"\x74\x65\x73\x74\x73\x6f\x66\x74\x0d")