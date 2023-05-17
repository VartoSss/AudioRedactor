from Fragment import Fragment
from TimeLine import TimeLine
from pydub import AudioSegment

timeLine = TimeLine()
morgen = Fragment("MORGENSHTERN_-_DULO_72947606.mp3")

timeLine.add(morgen)

timeLine.slice(1, 10000)

timeLine.remove(3)

timeLine.undo()
timeLine.undo()

timeLine.render("ahahah.mp3", "mp3")

