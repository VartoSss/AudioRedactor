from CommandInterface import CommandInterface
from Fragment import Fragment


class CuncatWithNextCommand(CommandInterface):
    def __init__(self, timeLine, id):
        self.id = id
        self.timeLine = timeLine

    def execute(self):
        self.fragment = self.timeLine.get_node_by_id(self.id)
        self.fragment_length = len(self.fragment.value)
        if self.fragment.next is None:
            raise TypeError("This track doesn't have a track after him")
        self.next = self.fragment.next
        self.next_name = self.next.name
        self.next_id = self.next.id
        self.fragment.cuncat_with(self.next)
        self.timeLine.remove_node(self.next)

    def undo(self):
        pass
