from typing import Callable, TypeVar, Any
import threading
import queue

Self = TypeVar("Self", bound="ObservableModel")

class ObservableModel:
    _instance = None
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._instance_lock:
            if cls._instance is None:
                cls._instance = super(ObservableModel, cls).__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialized = True
            self._event_listeners: dict[str, list[Callable[[Any], None]]] = {}
            self._event_queue: queue.Queue[tuple[str, Any]] = queue.Queue()
            self._stop_event = threading.Event()
            self._event_thread = threading.Thread(target=self._process_events, daemon=True)
            self._event_thread.start()

    def add_event_listener(self, event: str, fn: Callable[[Self], None]) -> Callable:
        try:
            self._event_listeners[event].append(fn)
        except KeyError:
            self._event_listeners[event] = [fn]
        return lambda: self._event_listeners[event].remove(fn)

    def trigger_event(self, event: str, *args, **kwargs) -> None:
        if event not in self._event_listeners:
            return
        self._event_queue.put((event, self, args, kwargs))

    def _process_events(self):
        while not self._stop_event.is_set():
            try:
                event, instance, args, kwargs = self._event_queue.get(timeout=1)
                for fn in self._event_listeners.get(event, []):
                    fn(instance, *args, **kwargs)
                self._event_queue.task_done()
            except queue.Empty:
                continue
            except Exception as e:
                print("Error processing event:", e)

    def stop(self):
        self._stop_event.set()
        self._event_thread.join()
