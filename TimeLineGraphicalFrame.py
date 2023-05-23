from tkinter import *
from ButtonTimeLine import ButtonTimeLine


class TimeLineGraphicalFrame:
    def __init__(self, graphicalInterface, timeLine):
        self.timeLine = timeLine
        self.graphicalInterface = graphicalInterface
        canvas = Canvas(self.graphicalInterface.window)
        canvas.pack(side='left', fill='both', expand=True)

        # создаем фрейм на канвасе
        self.frame = Frame(canvas, bd=2)
        self.frame.pack(side='left', fill='both', expand=True)
        canvas.create_window((0, 0), window=self.frame, anchor='nw')

        # настраиваем скроллбар
        scrollbar = Scrollbar(self.graphicalInterface.window, orient='horizontal',
                              command=canvas.xview)
        scrollbar.place(relx=0, rely=1, relwidth=1, anchor='sw')
        canvas.configure(xscrollcommand=scrollbar.set)

        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox('all'))

        self.frame.bind('<Configure>', on_frame_configure)

    def update(self):
        for child in self.frame.winfo_children():
            child.destroy()

        if self.timeLine.count == 0:
            return

        current = self.timeLine.head
        if current == self.timeLine.tail:
            ButtonTimeLine(self, current)
            return

        while (current.next is not None):
            ButtonTimeLine(self, current)
            current = current.next
        ButtonTimeLine(self, current)
