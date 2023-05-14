from Fragment import Fragment

fragment_morgen = Fragment("MORGENSHTERN_-_DULO_72947606.mp3")

fragment_morgen.change_speed(1.5)
fragment_morgen.fade_in(5000)
fragment_morgen.slice(0, 10000)
fragment_morgen.fade_out(5000)

fragment_morgen.export_fragment("morgen_test.mp3", "mp3")
