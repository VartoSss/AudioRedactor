from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from TimeLine import TimeLine
from TimeLineGraphicalFrame import TimeLineGraphicalFrame
from Fragment import Fragment
from re import match, compile


class GraphicalInterface:
    def __init__(self):
        self.timeLine = TimeLine()
        self.current_fragment_button = None
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
        self.change_speed_button = Button(
            self.functions_frame,
            text="Изменить скорость",
            font=self.hat_font,
            state='disabled',
            command=lambda: self.handle_change_speed_button()
        )
        self.change_speed_button.grid(
            row=0, column=0, sticky=NSEW, padx=5, pady=5)
        self.change_volume_button = Button(
            self.functions_frame,
            text="Изменить громкость",
            font=self.hat_font,
            state='disabled',
            command=lambda: self.handle_change_volume_button()
        )
        self.change_volume_button.grid(
            row=1, column=0, sticky=NSEW, padx=5, pady=5)

        self.reverse_button = Button(
            self.functions_frame,
            text="Развернуть",
            font=self.hat_font,
            state='disabled',
            command=lambda: self.handle_reverse_button()
        )
        self.reverse_button.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)

        self.crop_button = Button(
            self.functions_frame,
            text="Обрезать",
            font=self.hat_font,
            state='disabled',
            command=lambda: self.handle_crop_button()
        )
        self.crop_button.grid(row=0, column=1, sticky=NSEW, padx=5, pady=5)

        self.slice_button = Button(
            self.functions_frame,
            text="Разрезать",
            font=self.hat_font,
            state='disabled',
            command=lambda: self.handle_slice_button()
        )
        self.slice_button.grid(row=1, column=1, sticky=NSEW, padx=5, pady=5)

        self.cuncat_button = Button(
            self.functions_frame,
            text="Обьединить с следующим",
            font=self.hat_font,
            state='disabled',
            command=lambda: self.handle_cuncat_button()
        )
        self.cuncat_button.grid(row=2, column=1, sticky=NSEW, padx=5, pady=5)

        self.fade_in_button = Button(
            self.functions_frame,
            text="Fade in",
            font=self.hat_font,
            state='disabled',
            command=lambda: self.handle_fade_in_dialog()
        )
        self.fade_in_button.grid(row=0, column=2, sticky=NSEW, padx=5, pady=5)

        self.fade_out_button = Button(
            self.functions_frame,
            text="Fade out",
            font=self.hat_font,
            state='disabled',
            command=lambda: self.handle_fade_out_dialog()
        )
        self.fade_out_button.grid(row=1, column=2, sticky=NSEW, padx=5, pady=5)

        self.remove_button = Button(
            self.functions_frame,
            text="Удалить фрагмент",
            font=self.hat_font,
            state='disabled',
            command=lambda: self.handle_remove_button()
        )
        self.remove_button.grid(row=2, column=2, sticky=NSEW, padx=5, pady=5)

        # Настройка Таймлайна
        self.timeLineGraphics = TimeLineGraphicalFrame(
            self, self.timeLine)

        pass

    def undo_command(self):
        if len(self.timeLine.command_stack) == 0:
            self.create_warning_window(
                "Пока не происходило никаких действий, отменять нечего")
            return
        self.timeLine.undo()
        self.timeLineGraphics.update()
        self.end_work_fragment_actions()

    def save_command(self):
        print("This button doesn't work yet")

    def add_command(self):
        path_to_audio = filedialog.askopenfilename()
        if path_to_audio == '':
            return
        if not (path_to_audio.endswith(".mp3") or path_to_audio.endswith('.wav')):
            self.create_warning_window(
                "Можно добавлять только файлы с расширением .mp3 или .wav")
            return

        new_fragment = Fragment(path_to_audio)
        self.timeLine.add(new_fragment)
        self.timeLineGraphics.update()
        self.end_work_fragment_actions()

    def export_command(self):
        if self.timeLine.count == 0:
            self.create_warning_window(
                "На таймлайне пусто, нельзя экспортировать")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".mp3")
        self.timeLine.export(file_path, "mp3")
        self.end_work_fragment_actions()
    # --------------------------------------------------------------------------
    # fade in button

    def apply_fade_in_button(self, dialog_window, time_seconds):
        if not time_seconds.isdigit():
            self.create_warning_window(
                "Время должно быть неотрицательным числом")
            return

        self.timeLine.fade_in(self.current_fragment_id,
                              int(time_seconds) * 1000)
        dialog_window.destroy()
        self.end_work_fragment_actions()

    def handle_fade_in_dialog(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("400x100")

        # Создание метки с сообщением
        message_label = Label(
            dialog, text="Введить время fade in в секундах: ")
        message_label.grid(row=0, column=0, padx=10, pady=10)

        # Создание поля ввода
        input_entry = Entry(dialog)
        input_entry.grid(row=0, column=1, padx=10, pady=10)

        # Создание кнопки "Применить"
        apply_button = Button(dialog, text="Применить", command=lambda: self.apply_fade_in_button(
            dialog, input_entry.get()))
        apply_button.grid(row=1, column=0, padx=10, pady=10)

        # Создание кнопки "Отмена"
        cancel_button = Button(dialog, text="Отмена", command=dialog.destroy)
        cancel_button.grid(row=1, column=1, padx=10, pady=10)
        self.end_work_fragment_actions()

    # ----------------------------------------------------
    # fade out
    def apply_fady_out_change(self, dialog_window, time_seconds):
        if not time_seconds.isdigit():
            self.create_warning_window(
                "Время должно быть неотрицательным числом")
            return

        self.timeLine.fade_out(self.current_fragment_id,
                               int(time_seconds) * 1000)
        dialog_window.destroy()
        self.end_work_fragment_actions()

    def handle_fade_out_dialog(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("400x100")

        # Создание метки с сообщением
        message_label = Label(
            dialog, text="Введить время fade out в секундах: ")
        message_label.grid(row=0, column=0, padx=10, pady=10)

        # Создание поля ввода
        input_entry = Entry(dialog)
        input_entry.grid(row=0, column=1, padx=10, pady=10)

        # Создание кнопки "Применить"
        apply_button = Button(dialog, text="Применить", command=lambda: self.apply_fade_in_button(
            dialog, input_entry.get()))
        apply_button.grid(row=1, column=0, padx=10, pady=10)

        # Создание кнопки "Отмена"
        cancel_button = Button(dialog, text="Отмена", command=dialog.destroy)
        cancel_button.grid(row=1, column=1, padx=10, pady=10)
        self.end_work_fragment_actions()

    # -----------------------------------------------------
    # reverse

    def handle_reverse_button(self):
        self.timeLine.reverse(self.current_fragment_id)
        messagebox.showinfo("Успешно", "Фрагмент успешно развёрнут")
        self.end_work_fragment_actions()

    # -------------------------------------------------------
    # remove

    def handle_remove_button(self):
        self.timeLine.remove(self.current_fragment_id)
        self.timeLineGraphics.update()
        messagebox.showinfo("Успешно", "Фрагмент успешно удален")
        self.end_work_fragment_actions()

    # ------------------------------------------------------
    # change speed
    def apply_change_speed_change(self, dialog_window, speed_multiplier):
        if match(r"^[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$", speed_multiplier) is None:
            self.create_warning_window(
                "Мультипликатор должен быть вещественным неотрицательным числом")
            return

        self.timeLine.change_speed(
            self.current_fragment_id, float(speed_multiplier))
        dialog_window.destroy()
        self.end_work_fragment_actions()

    def handle_change_speed_button(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("600x150")

        # Создание метки с сообщением
        message_label = Label(
            dialog, text="Введите мультипликатор увеличения скорости \n \
            Для замедления введите вещественной число < 1 \n \
            Для ускорения введите число с плавающей точкой > 1 \n \
            Число вводить через точку")
        message_label.grid(row=0, column=0, padx=3, pady=3)

        # Создание поля ввода
        input_entry = Entry(dialog)
        input_entry.grid(row=0, column=1, padx=3, pady=3)

        # Создание кнопки "Применить"
        apply_button = Button(dialog, text="Применить", command=lambda: self.apply_change_speed_change(
            dialog, input_entry.get()))
        apply_button.grid(row=1, column=0, padx=3, pady=3)

        # Создание кнопки "Отмена"
        cancel_button = Button(dialog, text="Отмена", command=dialog.destroy)
        cancel_button.grid(row=1, column=1, padx=3, pady=3)
        self.end_work_fragment_actions()

    # -------------------------------------------------------------------------
    # change volume
    def apply_change_volume_change(self, dialog_window, volume_delta_decibels):
        if not volume_delta_decibels.isdigit():
            self.create_warning_window(
                "Значение должно быть целым числом")
            return

        self.timeLine.change_volume(
            self.current_fragment_id, int(volume_delta_decibels))
        dialog_window.destroy()
        self.end_work_fragment_actions()

    def handle_change_volume_button(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("600x150")

        # Создание метки с сообщением
        message_label = Label(
            dialog, text="Введите на сколько децибелл вы хотите изменить громкость\n \
            Для увеличения громкости введите целое число > 0 \n \
            Для уменьшения громкости введите целое число < 0")
        message_label.grid(row=0, column=0, padx=3, pady=3)

        # Создание поля ввода
        input_entry = Entry(dialog)
        input_entry.grid(row=0, column=1, padx=3, pady=3)

        # Создание кнопки "Применить"
        apply_button = Button(dialog, text="Применить", command=lambda: self.apply_change_volume_change(
            dialog, input_entry.get()))
        apply_button.grid(row=1, column=0, padx=3, pady=3)

        # Создание кнопки "Отмена"
        cancel_button = Button(dialog, text="Отмена", command=dialog.destroy)
        cancel_button.grid(row=1, column=1, padx=3, pady=3)
        self.end_work_fragment_actions()

    # -------------------------------------------------------------------------------
    # crop button

    def apply_crop(self, dialog_window, from_value_seconds, to_value_seconds):
        if match(r"^[0-9]*\.?[0-9]$", from_value_seconds) is None \
                or match(r"^[0-9]*\.?[0-9]$", to_value_seconds) is None:
            self.create_warning_window(
                "Правая и левая граница должны быть неотрицательнымы вещественными числами")
            return

        fragment = self.timeLine.get_value_by_id(self.current_fragment_id)
        fragment_duration_seconds = float(fragment.duration_seconds)

        if float(from_value_seconds) > float(to_value_seconds) \
                or float(from_value_seconds) > fragment_duration_seconds \
                or float(to_value_seconds) > fragment_duration_seconds:
            self.create_warning_window(
                "Правая и левая граница не должны быть больше времени фрагмента")
            return

        self.timeLine.crop(self.current_fragment_id, float(
            from_value_seconds) * 1000, float(to_value_seconds) * 1000)
        dialog_window.destroy()
        self.end_work_fragment_actions()

    def handle_crop_button(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("600x150")

        fragment = self.timeLine.get_value_by_id(self.current_fragment_id)
        fragment_duration_seconds = f"{float(fragment.duration_seconds):.2f}"

        message_label = Label(
            dialog, text=f"Введите начало и конец отрезка в секундах:\n \
            Текущая длина трека: {fragment_duration_seconds} секунд")
        message_label.grid(row=0, column=1, padx=3, pady=3)

        duration_from_label = Label(dialog, text="Левая граница:")
        duration_from_label.grid(row=1, column=0, padx=5, pady=10)

        duration_from_entry = Entry(dialog)
        duration_from_entry.grid(row=1, column=1, padx=10, pady=10)

        duration_to_label = Label(dialog, text="Правая граница:")
        duration_to_label.grid(row=1, column=2, padx=5, pady=10)

        duration_to_entry = Entry(dialog)
        duration_to_entry.grid(row=1, column=3, padx=10, pady=10)

        apply_button = Button(dialog, text="Применить", command=lambda: self.apply_crop(
            dialog, duration_from_entry.get(), duration_to_entry.get()))
        apply_button.grid(row=2, column=0, columnspan=2, padx=3, pady=3)

        # Создание кнопки "Отмена"
        cancel_button = Button(dialog, text="Отмена", command=dialog.destroy)
        cancel_button.grid(row=2, column=1, columnspan=2, padx=3, pady=3)
        self.end_work_fragment_actions()

    # -----------------------------------------------------------------------
    # slice
    def apply_slice_button(self, dialog, time_seconds):
        if match(r"^[0-9]*\.?[0-9]$", time_seconds) is None:
            self.create_warning_window(
                "Время разреза должно быть неотрицательным вещественным числом")
            return
        current_fragment = self.timeLine.get_value_by_id(
            self.current_fragment_id)
        current_fragment_len = current_fragment.duration_seconds

        if float(time_seconds) > current_fragment_len:
            self.create_warning_window(
                "Время разреза не должно превышать протяженность фрагмента")
            return

        self.timeLine.slice(self.current_fragment_id,
                            float(time_seconds) * 1000)
        dialog.destroy()
        self.timeLineGraphics.update()
        self.end_work_fragment_actions()

    def handle_slice_button(self):
        dialog = Toplevel()
        dialog.grab_set()
        dialog.geometry("500x150")

        current_fragment = self.timeLine.get_value_by_id(
            self.current_fragment_id)
        current_fragment_len = f"{float(current_fragment.duration_seconds):.2f}"

        # Создание метки с сообщением
        message_label = Label(
            dialog, text=f"Введите время в секундах, \n \
                на котором нужно разрезать фрагмент \n \
                протяженность фрагмента: {current_fragment_len} секунд")
        message_label.grid(row=0, column=0, padx=10, pady=10)

        # Создание поля ввода
        input_entry = Entry(dialog)
        input_entry.grid(row=0, column=1, padx=10, pady=10)

        # Создание кнопки "Применить"
        apply_button = Button(dialog, text="Применить", command=lambda: self.apply_slice_button(
            dialog, input_entry.get()))
        apply_button.grid(row=1, column=0, padx=10, pady=10)

        # Создание кнопки "Отмена"
        cancel_button = Button(dialog, text="Отмена", command=dialog.destroy)
        cancel_button.grid(row=1, column=1, padx=10, pady=10)
        self.end_work_fragment_actions()

    # -------------------------------------------------------------------------
    # cuncat

    def handle_cuncat_button(self):
        try:
            self.timeLine.cuncat_audio_with_next(
                self.current_fragment_id)
            messagebox.showinfo(
                "Успешно", "фрагмент успешно обьединен со следующим")
        except TypeError:
            self.create_warning_window("За этим фрагментом ничего нет")
        self.timeLineGraphics.update()
        self.end_work_fragment_actions()

    def track_button_clicked(self, button_time_line):
        self.current_fragment_id = button_time_line.fragment.id
        self.current_fragment_button = button_time_line.button
        self.current_fragment_button.configure(bg="#00D1FF")
        self.turn_on_functions_button()

    def set_fragment_button_color_to_default(self):
        self.current_fragment_button.configure(bg="#72FEFE")

    def end_work_fragment_actions(self):
        self.turn_off_functions_button()
        if self.current_fragment_button is not None:
            self.set_fragment_button_color_to_default()
        self.current_fragment_button = None

    def end_work_fragment_actions1(self):
        self.timeLineGraphics.update()
        self.current_fragment_button = None

    def turn_on_functions_button(self):
        self.fade_in_button['state'] = 'normal'
        self.fade_out_button['state'] = 'normal'
        self.change_speed_button['state'] = 'normal'
        self.change_volume_button['state'] = 'normal'
        self.crop_button['state'] = 'normal'
        self.slice_button['state'] = 'normal'
        self.cuncat_button['state'] = 'normal'
        self.remove_button['state'] = 'normal'
        self.reverse_button['state'] = 'normal'

    def turn_off_functions_button(self):
        self.fade_in_button['state'] = 'disabled'
        self.fade_out_button['state'] = 'disabled'
        self.change_speed_button['state'] = 'disabled'
        self.change_volume_button['state'] = 'disabled'
        self.crop_button['state'] = 'disabled'
        self.slice_button['state'] = 'disabled'
        self.cuncat_button['state'] = 'disabled'
        self.remove_button['state'] = 'disabled'
        self.reverse_button['state'] = 'disabled'

    def create_warning_window(self, warning_text):
        messagebox.showerror("Кое-что пошло не так", warning_text)

    def run(self):
        self.undo_button['command'] = self.undo_command
        self.save_button['command'] = self.save_command
        self.add_button['command'] = self.add_command
        self.export_button['command'] = self.export_command
        self.window.mainloop()
