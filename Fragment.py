import pydub
import os
from typing import TypeVar
from copy import deepcopy

Fragment = TypeVar('Fragment', bound='Fragment')


class Fragment:
    __last_id = 1

    def __init__(self, path_to_audio, name=None, value=None, id=None, previous=None, next=None):
        if name is None:
            self.path_to_audio = path_to_audio
            self.set_value_by_path(path_to_audio)
            self.set_name_by_path(path_to_audio)
            self.id = self.__last_id
            self.next = None
            self.previous = None
        else:
            self.name = name
            self.value = value
            self.path_to_audio = path_to_audio
            self.previous = previous
            self.next = next
            if id is None:
                self.id = self.__last_id
            else: self.id = id
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

    def copy_value(self):
        new_value = deepcopy(self.value)
        return new_value
