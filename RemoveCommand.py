from CommandInterface import CommandInterface
from Fragment import Fragment


class RemoveCommand(CommandInterface):
    def __init__(self, timeline, id: int):
        self.timeline = timeline
        self.id = id
        self.previous_id = None

    def execute(self):
        fragment = self.timeline.get_node_by_id(self.id)
        self.fragment = fragment
        if fragment.previous is not None:
            self.previous_id = fragment.previous.id
        self.timeline.remove_node_by_id(self.id)

    def undo(self):
        self.timeline.count += 1
        if self.timeline.head is None:
            self.timeline.head = self.timeline.tail = self.fragment
            self.timeline.count += 1
            return
        
        elif self.previous_id is None:
            self.timeline.head.previous = self.fragment
            self.timeline.head = self.timeline.head.previous
            return
        
        previous_fragment = self.timeline.get_node_by_id(self.previous_id)
        if previous_fragment.next is None:
            previous_fragment.next = self.fragment
            self.fragment.previous = self.timeline.tail
            self.timeline.tail = self.timeline.tail.next
        
        else:
            next_fragment = previous_fragment.next
            next_fragment.previous = self.fragment
            self.fragment.next = next_fragment
            previous_fragment.next = self.fragment
            self.fragment.previous = previous_fragment