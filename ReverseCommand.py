from CommandInterface import CommandInterface

class ReverseCommand(CommandInterface):
    def __init__(self, timeLine, id: int):
        self.timeLine = timeLine
        self.id = id

    def execute(self):
        value_before = self.timeLine.get_value_by_id(self.id)
        value_after = value_before.reverse()
        self.timeLine.set_value_by_id(self.id, value_after)

    def undo(self):
        self.execute()
