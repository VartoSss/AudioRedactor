from CommandInterface import CommandInterface

class CropCommand(CommandInterface):
    def __init__(self, timeLine, id, from_miliseconds, to_miliseconds):
        self.timeLine = timeLine
        self.id = id
        self.from_miliseconds = from_miliseconds
        self.to_miliseconds = to_miliseconds
        
    def execute(self):
        self.fragment = self.timeLine.get_node_by_id(self.id)
        self.old_value = self.fragment.copy_value()
        self.fragment.value = self.fragment.value[self.from_miliseconds:self.to_miliseconds]

    def undo(self):
        self.fragment.value = self.old_value
