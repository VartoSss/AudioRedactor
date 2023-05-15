from CommandInterface import CommandInterface


class ChangeSpeedComand(CommandInterface):
    def __init__(self, timeLine, id: int, speed_multiplier: float):
        self.timeLine = timeLine
        self.id = id
        self.speed_multiplier = speed_multiplier

    def execute(self):
        fragment = self.timeLine.get_value_by_id(self.id)
        sound_with_altered_frame_rate = fragment._spawn(
            fragment.raw_data, overrides={
                "frame_rate": int(fragment.frame_rate * self.speed_multiplier)
            })
        fragment = sound_with_altered_frame_rate.set_frame_rate(
            fragment.frame_rate)

        self.timeLine.set_value_by_id(self.id, fragment)

    def undo(self):
        fragment = self.timeLine.get_value_by_id(self.id)
        speed_multiplier = 1.0 / self.speed_multiplier
        sound_with_altered_frame_rate = fragment._spawn(
            fragment.raw_data, overrides={
                "frame_rate": int(fragment.frame_rate * speed_multiplier)
            })
        fragment = sound_with_altered_frame_rate.set_frame_rate(
            fragment.frame_rate)

        self.timeLine.set_value_by_id(self.id, fragment)
