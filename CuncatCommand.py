from CommandInterface import CommandInterface
from Fragment import Fragment
from copy import deepcopy


class CuncatWithNextCommand(CommandInterface):
    def __init__(self, timeLine, id):
        self.id = id
        self.timeLine = timeLine

    def execute(self):
        self.fragment = self.timeLine.get_node_by_id(self.id)
        self.next = self.fragment.next
        self.copied_next_fragment = deepcopy(self.fragment.next)
        self.copied_current_AudioSegment = deepcopy(self.fragment.value)

        self.fragment.cuncat_with(self.next)
        self.timeLine.remove_node(self.next)

    def undo(self):
        if self.fragment.next is None:
            self.timeLine.tail = self.copied_next_fragment
            self.timeLine.tail.previous = self.fragment
            self.fragment.next = self.timeLine.tail
        else:
            fragment_after_current = self.fragment.next
            fragment_after_current.previous = self.copied_next_fragment
            self.copied_next_fragment.previous = fragment_after_current
            self.fragment.next = self.copied_next_fragment
            self.copied_next_fragment.previous = self.fragment

        self.timeLine.set_value_by_id(self.id, self.fragment)
        self.timeLine.count += 1
