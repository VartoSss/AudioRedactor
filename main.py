from Fragment import Fragment
from TimeLine import TimeLine

timeLine = TimeLine()

morgen_fragment = Fragment("MORGENSHTERN_-_DULO_72947606.mp3")

timeLine.add(morgen_fragment)

shit = Fragment("sample-15s.wav")
timeLine.add(shit)

timeLine.render("final.mp3", "mp3")

