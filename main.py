from Fragment import Fragment
from TimeLine import TimeLine

timeline = TimeLine()

morgen_fragment = Fragment("MORGENSHTERN_-_DULO_72947606.mp3")

timeline.add(morgen_fragment)

shit = Fragment("sample-15s.wav")
timeline.add(shit)

timeline.undo()

timeline.render("zaebalo.mp3", "mp3")
