import pydub
import os
from typing import TypeVar

Fragment = TypeVar('Fragment', bound='Fragment')


class Fragment:
    id = 0
    
    def __init__(self, path_to_audio: str) -> None:
        self.set_fragment_by_path(path_to_audio)
        self.set_name_by_path(path_to_audio)

    def set_fragment_by_path(self, path_to_audio: str):
        if (path_to_audio.endswith(".wav")):
            self.fragment = pydub.AudioSegment.from_wav(path_to_audio)
        elif (path_to_audio.endswith(".mp3")):
            self.fragment = pydub.AudioSegment.from_mp3(path_to_audio)
        else:
            raise TypeError

    def set_name_by_path(self, path_to_audio: str):
        self.name = os.path.splitext(os.path.basename(path_to_audio))[0]

    def slice(self, from_miliseconds: int, to_miliseconds: int) -> None:
        self.fragment = self.fragment[from_miliseconds:to_miliseconds]

    def change_speed(self, speed_multiplier: float) -> None:
        sound_with_altered_frame_rate = self.fragment._spawn(
            self.fragment.raw_data, overrides={
                "frame_rate": int(self.fragment.frame_rate * speed_multiplier)
            })
        self.fragment = sound_with_altered_frame_rate.set_frame_rate(
            self.fragment.frame_rate)

    def change_volume(self, volume_delta_decibels: int) -> None:
        self.fragment += volume_delta_decibels
        self.fragment = self.fragment.apply_gain(volume_delta_decibels)

    def cuncat_with(self, other_fragment: Fragment) -> None:
        self.fragment += other_fragment

    def fade_out(self, duration_miliseconds):
        self.fragment = self.fragment.fade_out(duration_miliseconds)

    def fade_in(self, duration_miliseconds):
        self.fragment = self.fragment.fade_in(duration_miliseconds)

    def export_fragment(self, path_with_name: str, format_file: str) -> None:
        self.fragment.export(path_with_name, format=format_file)
