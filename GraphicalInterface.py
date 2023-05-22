from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from TimeLine import TimeLine
from TimeLineGraphicalFrame import TimeLineGraphicalFrame
from Fragment import Fragment


class GraphicalInterface:
    def __init__(self):
        self.timeLine = TimeLine()
        self.window = Tk()
        self.window.title("VartAudio")
        self.window.geometry("600x450")
        self.window.resizable(False, False)
        self.hat_frame = Frame(
            self.window,
            bg="#000834",
        )
        self.hat_frame.pack_propagate(False)
        self.hat_frame.configure(width=600, height=50)
        self.hat_frame.pack(side=TOP)
        self.hat_font = ("Roboto", 12, "bold")
        self.undo_button = Button(
            self.hat_frame,
            height=62,
            text="Назад",
            fg="white",
            font=self.hat_font,
            padx=10,
            bg="#938CDD"
        )
        self.save_button = Button(
            self.hat_frame,
            height=50,
            text="Сохранить как",
            fg="white",
            font=self.hat_font,
            padx=10,
            bg="#938CDD"
        )
        self.export_button = Button(
            self.hat_frame,
            height=62,
            text="Экспортировать аудио",
            fg="white",
            font=self.hat_font,
            padx=10,
            bg="#938CDD"
        )
        self.add_button = Button(
            self.hat_frame,
            height=62,
            text="Добавить трек",
            fg="white",
            font=self.hat_font,
            padx=10,
            bg="#938CDD"
        )
        self.save_button.pack(side=LEFT)
        self.export_button.pack(side=LEFT)
        self.undo_button.pack(side=LEFT)
        self.add_button.pack(side=LEFT)

        self.functions_frame = LabelFrame(
            self.window,
            text="Функции",
            font=self.hat_font,
            bg="#DDD9D9"
        )

        # Настройка функций
        self.functions_frame.pack_propagate(False)
        self.functions_frame.configure(width=600, height=150)
        self.functions_frame.pack(side=TOP)

        # Настройка Таймлайна
        self.timeLineGraphics = TimeLineGraphicalFrame(
            self.window, self.timeLine)

        pass

    def undo_command(self):
        if self.timeLine.count == 0:
            self.create_warning_window(
                "Пока не происходило никаких действий, отменять нечего")
            return
        self.timeLine.undo()

    def save_command(self):
        print("This button doesn't work yet")

    def add_command(self):
        path_to_audio = filedialog.askopenfilename()
        if path_to_audio == '':
            return
        if not (path_to_audio.endswith(".mp3") or path_to_audio.endswith('.wav')):
            self.create_warning_window(
                "Можно добавлять только файлы с расширением .mp3 или .wav")
        new_fragment = Fragment(path_to_audio)
        self.timeLine.add(new_fragment)
        self.timeLineGraphics.update(new_fragment)

    def export_command(self):
        if self.timeLine.count == 0:
            self.create_warning_window(
                "На таймлайне пусто, нельзя экспортировать")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".mp3")
        self.timeLine.export(file_path, ".mp3")

    def create_warning_window(self, warning_text):
        messagebox.showerror("Кое-что пошло не так", warning_text)

    def run(self):
        self.undo_button['command'] = self.undo_command
        self.save_button['command'] = self.save_command
        self.add_button['command'] = self.add_command
        self.export_button['command'] = self.export_command
        self.window.mainloop()
