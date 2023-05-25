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

        name_next = deepcopy(self.next.name)
        value_next = deepcopy(self.next.value)
        path_to_audio_next = deepcopy(self.next.path_to_audio)
        id_next = deepcopy(self.next.id)
        previous_next = self.next.previous
        next_next = self.next.next

        self.copied_next_fragment = Fragment(
            path_to_audio_next, name_next, value_next, id_next, previous_next, next_next)
        self.copied_current_AudioSegment = self.fragment.value + 0

        self.fragment.value += self.next.value
        self.timeLine.remove_node(self.next)

    def undo(self):
        if self.fragment.next is None:
            self.timeLine.tail = self.copied_next_fragment
            self.timeLine.tail.previous = self.fragment
            self.fragment.next = self.timeLine.tail
            self.fragment = None
        else:
            fragment_after_current = self.fragment.next
            fragment_after_current.previous = self.copied_next_fragment
            self.copied_next_fragment.previous = fragment_after_current
            self.fragment.next = self.copied_next_fragment
            self.copied_next_fragment.previous = self.fragment

        self.timeLine.set_value_by_id(self.id, self.fragment)
        self.timeLine.count += 1
