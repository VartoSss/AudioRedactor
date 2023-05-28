from tkinter import *


class ButtonTimeLine:
    def on_click(self):
        self.timeLineFrame.graphicalInterface.track_button_clicked(self)

    def __init__(self, timeLineFrame, fragment):
        self.timeLineFrame = timeLineFrame
        self.fragment = fragment
        self.default_font = ("Roboto", 12, "bold")
        self.pixelVirtual = PhotoImage(width=1, height=1)
        self.button = Button(
            self.timeLineFrame.frame,
            text=f"{fragment.name}",
            bg="#72FEFE",
            font=self.default_font,
            image=self.pixelVirtual,
            compound="c",
            anchor="center",
            wraplength=120,
            height=140,
            width=140,
            command=self.on_click
        )
        self.button.pack(side='left')
