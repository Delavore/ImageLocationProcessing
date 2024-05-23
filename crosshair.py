import tkinter as tk

root = tk.Tk()

# Получаем размер экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.attributes('-topmost', True)
root.update()
root.attributes('-topmost', False)
# Определяем координаты центра экрана
center_x = screen_width // 2
center_y = screen_height // 2

canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()

# Создаем точку в центре экрана
canvas.create_oval(center_x - 3, center_y - 3, center_x + 3, center_y + 3, fill="red")

root.attributes('-alpha', 1)  # Прозрачность окна
# root.overrideredirect(True) # Убираем рамку окна

root.mainloop()


'''
app = SampleApp()

app.attributes('-topmost', True)
app.update()
app.attributes('-topmost', False)

app.mainloop()
'''