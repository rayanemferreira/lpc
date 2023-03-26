class StateMachine:
    def __init__(self):
        self.stack = []

    def peek(self):
        try:
            return self.stack[-1]
        except IndexError:
            return None

    def pop(self):
        try:
            self.stack =  self.stack[1:]
            return len(self.stack) > 0
        except IndexError:
            return None

    def push(self, state):
        self.stack.append(state)
        return state