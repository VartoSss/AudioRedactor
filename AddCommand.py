from CommandInterface import CommandInterface
from Fragment import Fragment


class AddCommand(CommandInterface):
    def __init__(self, timeline, fragment: Fragment):
        self.timeline = timeline
        self.fragment = fragment

    def execute(self):
        self.timeline.id_to_names[self.fragment.id] = self.fragment.name
        self.timeline.count += 1
        if self.timeline.head is None:
            self.timeline.head = self.fragment
            self.timeline.tail = self.fragment

        else:
            self.fragment.previous = self.timeline.tail
            self.timeline.tail.next = self.fragment
            self.timeline.tail = self.fragment

    def undo(self):
        self.timeline.count -= 1
        if self.timeline.tail.previous is None:
            self.timeline.head = self.timeline.tail = None
            return
        self.timeline.tail = self.timeline.tail.previous
        self.timeline.tail.next = None
