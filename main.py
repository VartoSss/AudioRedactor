import pydub
from Fragment import Fragment
from TimeLine import TimeLine
from pydub import AudioSegment

timeLine = TimeLine()
morgen1 = Fragment("MORGENSHTERN_-_DULO_72947606.mp3")

timeLine.add(morgen1)

timeLine.crop(1, 10000, 20000)
timeLine.undo()

timeLine.render("crop.mp3", "mp3")