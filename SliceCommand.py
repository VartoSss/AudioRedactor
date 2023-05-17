from CommandInterface import CommandInterface
from Fragment import Fragment

class SliceCommand(CommandInterface):
    def __init__(self, timeLine, id, where_to_cut_milisecconds):
        self.timeLine = timeLine
        self.id = id
        self.where_to_cut_milisecconds = where_to_cut_milisecconds

    def execute(self):
        self.fragment = self.timeLine.get_node_by_id(self.id)
        name = self.fragment.name
        value = self.fragment.value
        path_to_audio = self.fragment.path_to_audio
        self.previous = self.fragment.previous
        self.next = self.fragment.next

        value_before_cut = value[:self.where_to_cut_milisecconds]
        value_after_cut = value[self.where_to_cut_milisecconds:]
        
        if self.previous is None and self.next is None:
            fragment_before_cut = Fragment(
            path_to_audio, name, value_before_cut, None, None
            )
            self.timeLine.head = fragment_before_cut
            fragment_after_cut = Fragment(
                path_to_audio, name, value_after_cut,  fragment_before_cut, None
            )

            self.timeLine.tail = fragment_after_cut
            fragment_before_cut.next = fragment_after_cut
            fragment_after_cut.previous = fragment_before_cut

        elif self.next is None:
            fragment_before_cut = Fragment(
                path_to_audio, name, value_before_cut, self.previous, None
            )
            fragment_after_cut = Fragment(
            path_to_audio, name, value_after_cut, fragment_before_cut, None
            )
            self.timeLine.tail = fragment_after_cut
            fragment_before_cut.next = fragment_after_cut
            self.previous.next = fragment_before_cut

        elif self.previous is None:
            fragment_before_cut = Fragment(
                path_to_audio, name, value_before_cut, None, None
            )
            fragment_after_cut = Fragment(
            fragment_before_cut, name, value_after_cut, path_to_audio, self.next
            )
            self.timeLine.head = fragment_before_cut
            fragment_before_cut.next = fragment_after_cut
            self.next.previous = fragment_after_cut
               
        else:
            fragment_before_cut = Fragment(
                path_to_audio, name, value_before_cut, self.previous, None
            )
            fragment_after_cut = Fragment(
            path_to_audio, name, value_after_cut, fragment_before_cut, self.next
            )
            self.previous.next = fragment_before_cut
            fragment_before_cut.next = fragment_after_cut
            self.next.previous = fragment_after_cut
            
        self.id_fragment_before_cut = fragment_before_cut.id
        self.timeLine.count += 1


    def undo(self):
        if self.previous is None and self.next is None:
            self.timeLine.head = self.timeLine.tail = self.fragment

        elif self.previous is None:
            self.next.previous = self.fragment
            self.fragment.next = self.next
            self.timeLine.head = self.fragment
        
        elif self.next is None:
            self.previous.next = self.fragment
            self.timeLine.tail = self.fragment
            self.fragment.previous = self.previous

        else:
            self.fragment.next = self.next
            self.fragment.previous = self.previous
            self.next.previous = self.fragment
            self.previous.nexe = self.fragment

        self.timeLine.count -= 1
