from CommandInterface import CommandInterface

class ReplayCommand(CommandInterface):
    def __init__(self, timeLine, id: int, times_to_replay: int):
        self.timeLine = timeLine
        self.id = id
        self.times_to_replay = times_to_replay

    def execute(self):
        self.value_before = self.timeLine.get_value_by_id(self.id)
        value_after = self.value_before * self.times_to_replay
        self.timeLine.set_value_by_id(self.id, value_after)

    def undo(self):
        self.timeLine.set_value_by_id(self.id, self.value_before)
