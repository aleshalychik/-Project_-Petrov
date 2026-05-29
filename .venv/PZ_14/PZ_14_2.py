import tkinter as tk
from tkinter import messagebox

def check_numbers():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        num3 = int(entry3.get())
        if num1 == num2 or num2 == num3 or num1 == num3:
            result_label.config(text="Результат: ИСТИНА (есть совпадения) ✔", fg="green")
        else:
            result_label.config(text="Результат: ЛОЖЬ (все числа разные) ✖", fg="red")

    except ValueError:
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите только целые числа!")

root = tk.Tk()
root.title("Проверка условия")
root.geometry("600x450")
root.configure(bg="#eef2f5")

title_label = tk.Label(root, text="Логическая задача", font=("Arial", 16), fg="#2fa4e7", bg="#eef2f5")
title_label.pack(anchor="w", padx=40, pady=(20, 5))

main_frame = tk.Frame(root, bg="white", highlightbackground="#d3d3d3", highlightthickness=1)
main_frame.pack(fill="both", expand=False, padx=40, pady=5)

header_frame = tk.Frame(main_frame, bg="#2fa4e7")
header_frame.pack(fill="x")

header_label = tk.Label(header_frame, text="Проверка трех целых чисел", font=("Arial", 12, "bold"), bg="#2fa4e7", fg="white")
header_label.pack(pady=10)

input_frame = tk.Frame(main_frame, bg="white")
input_frame.pack(pady=20)

lbl_font = ("Arial", 10, "bold")
ent_font = ("Arial", 10)

tk.Label(input_frame, text="Первое число", font=lbl_font, bg="white", fg="#4aa9e9").grid(row=0, column=0, sticky="e", padx=10, pady=10)
entry1 = tk.Entry(input_frame, font=ent_font, width=30, relief="solid", bd=1)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(input_frame, text="Второе число", font=lbl_font, bg="white", fg="#4aa9e9").grid(row=1, column=0, sticky="e", padx=10, pady=10)
entry2 = tk.Entry(input_frame, font=ent_font, width=30, relief="solid", bd=1)
entry2.grid(row=1, column=1, padx=10, pady=10)

tk.Label(input_frame, text="Третье число", font=lbl_font, bg="white", fg="#4aa9e9").grid(row=2, column=0, sticky="e", padx=10, pady=10)
entry3 = tk.Entry(input_frame, font=ent_font, width=30, relief="solid", bd=1)
entry3.grid(row=2, column=1, padx=10, pady=10)

result_label = tk.Label(main_frame, text="Введите числа и нажмите кнопку", font=("Arial", 11, "bold"), bg="white", fg="gray")
result_label.pack(pady=10)

btn = tk.Button(main_frame, text="Проверить", font=("Arial", 10, "bold"), bg="#2fa4e7", fg="white", activebackground="#1b88c4", activeforeground="white", relief="flat", padx=20, pady=5, command=check_numbers)
btn.pack(pady=(10, 20))

root.mainloop()
