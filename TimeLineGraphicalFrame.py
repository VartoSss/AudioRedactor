from tkinter import *
from ButtonTimeLine import ButtonTimeLine


class TimeLineGraphicalFrame:
    def __init__(self, window, timeLine):
        self.timeLine = timeLine
        canvas = Canvas(window)
        canvas.pack(side='left', fill='both', expand=True)

        # создаем фрейм на канвасе
        self.frame = Frame(canvas, bd=2)
        self.frame.configure(bg="#B4FFF6")
        self.frame.pack(side='left', fill='both', expand=True)
        canvas.create_window((0, 0), window=self.frame, anchor='nw')

        # настраиваем скроллбар
        scrollbar = Scrollbar(window, orient='horizontal',
                              command=canvas.xview)
        scrollbar.place(relx=0, rely=1, relwidth=1, anchor='sw')
        canvas.configure(xscrollcommand=scrollbar.set)

        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox('all'))

        self.frame.bind('<Configure>', on_frame_configure)

    def update(self):
        for child in self.frame.winfo_children():
            child.destroy()

        current = self.timeLine.head
        if current == self.timeLine.tail:
            ButtonTimeLine(self, current)
            return

        while (current.next is not None):
            ButtonTimeLine(self, current)
            current = current.next
        ButtonTimeLine(self, current)
