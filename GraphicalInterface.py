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
        change_speed_button = Button(
            self.functions_frame,
            text="Изменить скорость",
            font=self.hat_font,
        )
        change_speed_button.grid(row=0, column=0, sticky=NSEW, padx=5, pady=5)
        change_volume_button = Button(
            self.functions_frame,
            text="Изменить громкость",
            font=self.hat_font,
        )
        change_volume_button.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)

        reverse_button = Button(
            self.functions_frame,
            text="Развернуть",
            font=self.hat_font,
        )
        reverse_button.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)

        crop_button = Button(
            self.functions_frame,
            text="Обрезать",
            font=self.hat_font,
        )
        crop_button.grid(row=0, column=1, sticky=NSEW, padx=5, pady=5)

        slice_button = Button(
            self.functions_frame,
            text="Разрезать",
            font=self.hat_font,
        )
        slice_button.grid(row=1, column=1, sticky=NSEW, padx=5, pady=5)

        cuncat_button = Button(
            self.functions_frame,
            text="Обьеденить с следующим",
            font=self.hat_font,
        )
        cuncat_button.grid(row=2, column=1, sticky=NSEW, padx=5, pady=5)

        fade_in_button = Button(
            self.functions_frame,
            text="Fade in",
            font=self.hat_font,
        )
        fade_in_button.grid(row=0, column=2, sticky=NSEW, padx=5, pady=5)

        fade_out_button = Button(
            self.functions_frame,
            text="Fade out",
            font=self.hat_font,
        )
        fade_out_button.grid(row=1, column=2, sticky=NSEW, padx=5, pady=5)

        remove_button = Button(
            self.functions_frame,
            text="Удалить фрагмент",
            font=self.hat_font,
        )
        remove_button.grid(row=2, column=2, sticky=NSEW, padx=5, pady=5)

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
        self.timeLineGraphics.update()

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
        self.timeLineGraphics.update()

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
