from Fragment import Fragment
from TimeLine import TimeLine

timeline = TimeLine()

shit = Fragment("sample-15s.wav")
morgen = Fragment("MORGENSHTERN_-_DULO_72947606.mp3")
timeline.add(shit)
timeline.add(morgen)

timeline.remove(2)
timeline.remove(1)

timeline.undo()
timeline.undo()

timeline.render("bebra.mp3", "mp3")
