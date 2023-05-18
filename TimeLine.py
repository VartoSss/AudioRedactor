from Fragment import Fragment
from typing import TypeVar
from pydub import AudioSegment
from ChangeSpeedCommand import ChangeSpeedComand
from ChangeVolumeCommand import ChangeVolumeComand
from FadeOutCommand import FadeOutCommand
from FadeInCommand import FadeInCommand
from AddCommand import AddCommand
from RemoveCommand import RemoveCommand
from CropCommand import CropCommand
from SliceCommand import SliceCommand
from ReverseCommand import ReverseCommand


class TimeLine:
    def __init__(self):
        self.head = None
        self.tail = None
        self.id_to_names = dict()
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
        node = self.get_node_by_id(id)
        node.value = new_value

    def get_node_by_id(self, id):
        current_node = self.head
        while (current_node.id != id):
            current_node = current_node.next
        return current_node

    def cuncat_audio_with_next_by_id(self, id):
        node = self.get_node_by_id(id)
        if node.next is None:
            raise TypeError("This track doesn't have a track after him")
        next = node.next
        node.cuncat_with(next)
        self.remove_node(next)

    def render(self, path_with_name: str, format_file: str):
        if (self.count == 0):
            raise TypeError("There is nothing on timeLine now")
        final_segment_value = self.head.copy_value()
        current_segment = self.head
        while (current_segment.next is not None):
            current_segment = current_segment.next
            final_segment_value += current_segment.value
        final_segment_value.export(path_with_name, format_file)

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

    def remove(self, id: int):
        remove_command = RemoveCommand(self, id)
        self.command_stack.append(remove_command)
        remove_command.execute()

    def crop(self, id, from_miliseconds, to_miliseconds):
        crop_command = CropCommand(self, id, from_miliseconds, to_miliseconds)
        self.command_stack.append(crop_command)
        crop_command.execute()

    def slice(self, id, where_to_cut_miliseconds):
        slice_command = SliceCommand(self, id, where_to_cut_miliseconds)
        self.command_stack.append(slice_command)
        slice_command.execute()

    def reverse(self, id):
        reverse_command = ReverseCommand(self, id)
        self.command_stack.append(reverse_command)
        reverse_command.execute()

    def undo(self):
        command = self.command_stack.pop()
        command.undo()
