from CommandInterface import CommandInterface


class ChangeVolumeComand(CommandInterface):
    def __init__(self, timeLine, id: int, volume_delta_decibels: float):
        self.timeLine = timeLine
        self.id = id
        self.volume_delta_decibels = volume_delta_decibels
        self.previous_value = None

    def execute(self):
        value_before = self.timeLine.get_value_by_id(self.id)
        value_after = value_before.apply_gain(self.volume_delta_decibels)
        self.timeLine.set_value_by_id(self.id, value_after)
        self.previous_value = value_before

    def undo(self):
        self.timeLine.set_value_by_id(self.id, self.previous_value)
