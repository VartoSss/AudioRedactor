import pydub

from pydub.playback import play


def slice_audio(audio, from_miliseconds, to_miliseconds):
    slised_song = audio[from_miliseconds:to_miliseconds]
    return slised_song


def speed_change(audio, speed=1.0):
    sound_with_altered_frame_rate = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * speed)
    })
    return sound_with_altered_frame_rate.set_frame_rate(audio.frame_rate)


def change_volume(audio, volume_delta_decibels):
    return audio + volume_delta_decibels


def cuncat_audio(first_audio, second_audio):
    return first_audio + second_audio


def fade_in_audio(audio, duration_miliseconds):
    final_duration = duration_miliseconds
    if audio.duration_seconds * 1000 < duration_miliseconds:
        final_duration = audio.duration_seconds * 1000
    return audio.fade_in(final_duration)


def fade_out_audio(audio, duration_miliseconds):
    final_duration = duration_miliseconds
    if audio.duration_seconds * 1000 < duration_miliseconds:
        final_duration = audio.duration_seconds * 1000
    return audio.fade_out(final_duration)


def get_audio(file_path: str):
    if (file_path.endswith(".wav")):
        return pydub.AudioSegment.from_wav(file_path)
    elif (file_path.endswith(".mp3")):
        return pydub.AudioSegment.from_mp3(file_path)
    else:
        raise TypeError


audio = get_audio("MORGENSHTERN_-_DULO_72947606.mp3")

sliced_audio = slice_audio(audio, 5000, 14100)

sliced_second = slice_audio(audio, 14100, 150000)

second_double_speed = speed_change(sliced_second, 2)

cuncated = cuncat_audio(sliced_audio, second_double_speed)

cuncated.export("cool_morgen.mp3", format="mp3")
play(cuncated)
