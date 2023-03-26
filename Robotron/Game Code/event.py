
class Event:
    """
    A class which is a super for all other events the system might handle
    """
    def __init__(self):
        self.name = 'Some event'

    def __str__(self):
        return self.name

class EndGame(Event):
    """
    This event is sent at the end of the game
    """
    def __init__(self):
        self.name = 'End Game'


class Start(Event):
    """
    This event is sent at the start of the game
    """
    def __init__(self):
        self.name = 'Start Game'


class Tick(Event):
    """
    A tick
    """
    def __init__(self):
        self.name = 'Tick'

class Keyboard(Event):
    """
    Event for keyboard clicks
    """
    def __init__(self, keys, letter):
        self.name = 'Keyboard'
        self.key = keys
        self.uni = letter
    def __str__(self):
        return f"Keypress - {self.uni}"

class KeyboardUp(Event):
    """
    Event for keyboard clicks
    """
    def __init__(self, keys):
        self.name = 'Keyboard'
        self.key = keys
    def __str__(self):
        return f"Key release - {self.key}"

class Mouse(Event):
    """
    Event for mouse clicks
    """
    def __init__(self, pos):
        self.name = 'Mouse'
        self.pos = pos
    def __str__(self):
        return f"Mouse - {self.pos}"

class ChangeState(Event):
    def __init__(self, newState):
        self.name = 'Change State'
        self.state = newState
    def __str__(self):
        return str(self.state)