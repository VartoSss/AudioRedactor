from CommandInterface import CommandInterface
from Fragment import Fragment


class AddCommand(CommandInterface):
    def __init__(self, timeline, fragment: Fragment):
        self.timeline = timeline
        self.fragment = fragment

    def execute(self):
        self.timeline.names_to_id[self.fragment.name] = self.fragment.id
        self.timeline.count += 1
        if self.timeline.head is None:
            self.timeline.head = self.fragment
            self.timeline.tail = self.fragment

        else:
            self.fragment.previous = self.timeline.tail
            self.timeline.tail.next = self.fragment
            self.timeline.tail = self.fragment

    def undo(self):
        self.timeline.tail = self.timeline.tail.previous
        self.timeline.tail.next = None
