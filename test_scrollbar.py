import tkinter as tk

# создаем окно
window = tk.Tk()

# создаем канвас
canvas = tk.Canvas(window)
canvas.pack(side='left', fill='both', expand=True)

# создаем фрейм на канвасе
frame = tk.Frame(canvas, bg="red")

canvas.create_window((0, 0), window=frame, anchor='nw')

# создаем кнопки на фрейме

# настраиваем скроллбар
scrollbar = tk.Scrollbar(window, orient='horizontal', command=canvas.xview)
scrollbar.place(relx=0, rely=1, relwidth=1, anchor='sw')
canvas.configure(xscrollcommand=scrollbar.set)

# настраиваем обработчик событий для изменения размера фрейма на канвасе


def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))


frame.bind('<Configure>', on_frame_configure)

# запускаем главный цикл
window.mainloop()
