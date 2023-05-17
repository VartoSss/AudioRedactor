from Fragment import Fragment
from TimeLine import TimeLine

timeLine = TimeLine()
koktail = Fragment("LSP_-_Koktejjl_47965009.mp3")
golden_fishes = Fragment("LSP_-_Zolotye_rybki_48616367.mp3")
without_you = Fragment("Dora_LSP_-_Net_tebya_74372746.mp3")
meteor_rain = Fragment("LSP_-_Meteoritnyjj_dozhd_48616375.mp3")

timeLine.add(koktail)
timeLine.add(golden_fishes)
timeLine.add(without_you)
timeLine.add(meteor_rain)

timeLine.crop(1, 28000, 58000)
timeLine.crop(2, 32500, 45000)
timeLine.crop(3, 58000, 110000)
timeLine.crop(4, 53000, 78000)

timeLine.fade_out(1, 3000)
timeLine.fade_in(2, 3000)
timeLine.fade_out(2, 3000)
timeLine.fade_in(3, 3000)
timeLine.fade_out(3, 3000)
timeLine.fade_in(4, 3000)

timeLine.render("LSP1Love.mp3", "mp3")