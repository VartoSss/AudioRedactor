from Fragment import Fragment
from typing import TypeVar
from pydub import AudioSegment
from ChangeSpeedCommand import ChangeSpeedComand
from ChangeVolumeCommand import ChangeVolumeComand
from FadeOutCommand import FadeOutCommand
from FadeInCommand import FadeInCommand
from AddCommand import AddCommand


class TimeLine:
    def __init__(self):
        self.head = None
        self.tail = None
        self.names_to_id = dict()
        self.count = 0
        self.command_stack = []

    def add(self, fragment: Fragment):
        add_command = AddCommand(self, fragment)
        self.command_stack.append(add_command)
        add_command.execute()

    def remove_node_by_id(self, id):
        node = self.get_node_by_id(id)
        self.remove_node(node)

    def remove_node(self, node: Fragment):
        if self.count == 0:
            raise TypeError
        elif self.count == 1:
            self.head = self.tail = None

        elif node.previous is None:
            self.head = node.next
            self.head.previous = None

        elif node.next is None:
            self.tail = node.previous
            self.tail.next = None

        else:
            next_node = node.next
            previous_node = node.previous
            previous_node.next = next_node
            next_node.previous = previous_node

        self.count -= 1

    def get_value_by_id(self, id):
        return self.get_node_by_id(id).value

    def set_value_by_id(self, id, new_value):
        self.get_node_by_id(id).value = new_value

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
        node.cuncat_with(next)
        self.remove_node(next)

    def render(self, path_with_name: str, format_file: str) -> AudioSegment:
        final_segment = self.head
        current_segment = self.head
        while (current_segment.next is not None):
            current_segment = current_segment.next
            final_segment.cuncat_with(current_segment)
        final_segment.export_fragment(path_with_name, format_file)

    def change_speed(self, id: int, speed_multiplier: float):
        change_speed_command = ChangeSpeedComand(self, id, speed_multiplier)
        self.command_stack.append(change_speed_command)
        change_speed_command.execute()

    def change_volume(self, id: int, volume_delta_decibels: int):
        change_volume_command = ChangeVolumeComand(
            self, id, volume_delta_decibels)
        self.command_stack.append(change_volume_command)
        change_volume_command.execute()

    def fade_out(self, id: int, duration_miliseconds):
        fade_out_command = FadeOutCommand(self, id, duration_miliseconds)
        self.command_stack.append(fade_out_command)
        fade_out_command.execute()

    def fade_in(self, id: int, duration_miliseconds):
        fade_in_command = FadeInCommand(self, id, duration_miliseconds)
        self.command_stack.append(fade_in_command)
        fade_in_command.execute()

    def undo(self):
        command = self.command_stack.pop()
        command.undo()
