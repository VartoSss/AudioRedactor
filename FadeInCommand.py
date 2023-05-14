from CommandInterface import CommandInterface

class FadeInCommand(CommandInterface):
    def __init__(self, timeLine, id: int, duration_miliseconds: int):
        self.timeLine = timeLine
        self.id = id
        self.duration_miliseconds = duration_miliseconds

    def Execute(self):
        value_before = self.timeLine.get_value_by_id(self.id)
        value_after = value_before.fade_in(self.duration_miliseconds)
        self.timeLine.set_value_by_id(self.id, value_after)

    def Undo(self):
        value_before = self.timeLine.get_value_by_id(self.id)
        value_after = value_before.fade_out(self.duration_miliseconds)
        self.timeLine.set_value_by_id(self.id, value_after)
