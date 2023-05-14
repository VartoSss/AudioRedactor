from Fragment import Fragment
from TimeLine import TimeLine

timeLine = TimeLine()

morgen_fragment = Fragment("MORGENSHTERN_-_DULO_72947606.mp3")

timeLine.add(morgen_fragment)

shit = Fragment("sample-15s.wav")
timeLine.add(shit)

timeLine.change_speed(1, 1.5)
timeLine.change_volume(1, 15)
timeLine.fade_in(1, 5000)
timeLine.fade_in(2, 2000)


timeLine.render("speeded_up.mp3", "mp3")

timeLine.undo()
timeLine.undo()
timeLine.undo()
timeLine.undo()

timeLine.render("undo.mp3", "mp3")
