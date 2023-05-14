from Fragment import Fragment


class TimeLine:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value: Fragment):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_node_by_id(self, id):
        node = self.get_node_by_id(id)
        self.remove_node(node)

    def remove_node(self, node):
        next_node = node.next
        previous_node = node.previous
        previous_node.next = next_node
        next_node.previous = previous_node

    def get_value_by_id(self, id):
        return self.get_node_by_id(id).value

    def get_node_by_id(self, id):
        current_node = self.head
        while (current_node.id != id):
            current_node = current_node.next
        return current_node

    def cuncat_audio_with_next_by_id(self, id):
        node = self.get_node_by_id(id)
        if node.next is None:
            raise TypeError
        next = node.next
        node_value = node.value
        node_value.cuncat_with(next.value)
        self.remove_node(next)


class LinkedListNode:
    def __init__(self, value: Fragment):
        self.value = value
        self.next = None
        self.previous = None
        self.id = Fragment.id
        Fragment.id += 1
