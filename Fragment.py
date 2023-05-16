import pydub
import os
from typing import TypeVar

Fragment = TypeVar('Fragment', bound='Fragment')


class Fragment:
    __last_id = 1

    def __init__(self, path_to_audio: str) -> None:
        self.path_to_audio = path_to_audio
        self.set_value_by_path(path_to_audio)
        self.set_name_by_path(path_to_audio)
        self.id = self.__last_id
        self.next = None
        self.previous = None
        Fragment.__last_id += 1

    def set_value_by_path(self, path_to_audio: str):
        if (path_to_audio.endswith(".wav")):
            self.value = pydub.AudioSegment.from_wav(path_to_audio)
        elif (path_to_audio.endswith(".mp3")):
            self.value = pydub.AudioSegment.from_mp3(path_to_audio)
        else:
            raise TypeError

    def set_name_by_path(self, path_to_audio: str):
        self.name = os.path.splitext(os.path.basename(path_to_audio))[0]

    def slice(self, from_miliseconds: int, to_miliseconds: int) -> None:
        self.value = self.value[from_miliseconds:to_miliseconds]

    def change_speed(self, speed_multiplier: float) -> None:
        sound_with_altered_frame_rate = self.value._spawn(
            self.value.raw_data, overrides={
                "frame_rate": int(self.value.frame_rate * speed_multiplier)
            })
        self.value = sound_with_altered_frame_rate.set_frame_rate(
            self.value.frame_rate)

    def change_volume(self, volume_delta_decibels: int) -> None:
        self.value += volume_delta_decibels
        self.value = self.value.apply_gain(volume_delta_decibels)

    def cuncat_with(self, other_fragment: Fragment) -> None:
        self.value += other_fragment.value

    def fade_out(self, duration_miliseconds):
        self.value = self.value.fade_out(duration_miliseconds)

    def fade_in(self, duration_miliseconds):
        self.value = self.value.fade_in(duration_miliseconds)

    def copy(self):
        new_fragment = Fragment(self.path_to_audio)
        return new_fragment

    def export_fragment(self, path_with_name: str, format_file: str) -> None:
        self.value.export(path_with_name, format=format_file)
