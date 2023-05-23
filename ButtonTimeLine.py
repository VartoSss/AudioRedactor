from tkinter import *


class ButtonTimeLine:
    def on_click(self):
        print("SUKA BLYAT")
        self.timeLineFrame.graphicalInterface.fade_in_button['state'] = 'normal'
        self.timeLineFrame.graphicalInterface.fade_out_button['state'] = 'normal'
        self.timeLineFrame.graphicalInterface.change_speed_button['state'] = 'normal'
        self.timeLineFrame.graphicalInterface.change_volume_button['state'] = 'normal'
        self.timeLineFrame.graphicalInterface.crop_button['state'] = 'normal'
        self.timeLineFrame.graphicalInterface.slice_button['state'] = 'normal'
        self.timeLineFrame.graphicalInterface.cuncat_button['state'] = 'normal'
        self.timeLineFrame.graphicalInterface.remove_button['state'] = 'normal'
        self.timeLineFrame.graphicalInterface.reverse_button['state'] = 'normal'
        print("Меня нажали")

    def __init__(self, timeLineFrame, fragment):
        self.timeLineFrame = timeLineFrame
        self.fragment = fragment
        self.default_font = ("Roboto", 12, "bold")
        self.pixelVirtual = PhotoImage(width=1, height=1)
        button = Button(
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
        button.pack(side='left')
