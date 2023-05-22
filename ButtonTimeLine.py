from tkinter import *


class ButtonTimeLine:
    def __init__(self, timeLineFrame, fragment):
        self.tmeLineFrame = timeLineFrame
        self.fragment = fragment
        self.default_font = ("Roboto", 12, "bold")
        pixelVirtual = PhotoImage(width=1, height=1)
        button = Button(
            self.tmeLineFrame.frame,
            text=f"{fragment.name}",
            bg="#72FEFE",
            font=self.default_font,
            image=pixelVirtual,
            compound="c",
            anchor="center",
            wraplength=120,
            height=140,
            width=140
        )
        button.pack(side='left')

    def on_click(self):
        pass
