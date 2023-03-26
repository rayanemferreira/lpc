from event import *
from statemachine import StateMachine

from states import *


class Game:
    def __init__(self, eventManager):
        self.statem = StateMachine()
        self.eventManager = eventManager
        eventManager.add_listener(self)
        self.on = False

    def notify(self, event):
        if isinstance(event, EndGame):
            self.stop()
        elif isinstance(event, ChangeState):
            # pop request
            if not event.state:
                # false if no more states are left
                if not self.statem.pop():
                    self.eventManager.Post(EndGame())
            else:
                # push a new state on the stack
                self.statem.push(event.state)

    def stop(self):
        self.on = False


    def run(self, mode='norm'):
        self.on = True
        self.eventManager.post(Start())
        if mode == 'test':
            self.statem.push(STATE_TEST)
        elif mode == 'light':
            pass
        else:
            self.statem.push(STATE_INTRO1)
        while self.on:
            newTick = Tick()
            self.eventManager.post(newTick)