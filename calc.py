import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        label_result.config(text=f"Результат: {result}")
    except Exception:
        label_result.config(text="Ошибка")

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=30)
entry.pack()

button = tk.Button(root, text="Вычислить", command=calculate)
button.pack()

label_result = tk.Label(root, text="Результат: ")
label_result.pack()

root.mainloop()
