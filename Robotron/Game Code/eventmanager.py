from event import *


class EventManager:
    """
    Controls the flow of events between the M, V and C
    """

    def __init__(self):
        """
        """
        self.listeners = []

    def add_listener(self, listener):
        """
        This adds an object as a listener
        """
        self.listeners.append(listener)

    def remove_listener(self, listener):
        """
        This is to stop objects listening.
        """

        if listener in self.listeners:
            del self.listeners[listener]

    def post(self, event):
        """
        This will emit a message to all the objects in the listen dict
        if it isn't a tick then we also print that event - mostly to debug
        """
        if not isinstance(event, Tick):
            print(str(event))
        for listener in self.listeners:
            listener.notify(event)
