import tkinter as tk
from tkinter import ttk


def create_ui():
    root = tk.Tk()
    root.title("Регистрация")
    root.geometry("650x450")
    root.configure(bg="#e8eef2")

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TEntry", padding=3)

    main_blue = "#38a3d5"
    text_blue = "#4a8fb3"
    check_green = "#4caf50"

    header_label = tk.Label(root, text="Регистрация", font=("Arial", 16, "bold"), fg=main_blue, bg="#e8eef2")
    header_label.pack(anchor="nw", padx=30, pady=(20, 10))

    main_frame = tk.Frame(root, bg="white", bd=1, relief="ridge")
    main_frame.pack(fill="both", expand=True, padx=30, pady=(0, 30))

    banner_frame = tk.Frame(main_frame, bg=main_blue, height=40)
    banner_frame.pack(fill="x")
    banner_label = tk.Label(banner_frame, text="Создание нового сайта", bg=main_blue, fg="white", font=("Arial", 12))
    banner_label.pack(pady=10)

    form_frame = tk.Frame(main_frame, bg="white")
    form_frame.pack(pady=20, padx=20)

    def add_row(row_idx, label_text, widget, show_check=True):
        lbl = tk.Label(form_frame, text=label_text, bg="white", fg=text_blue, font=("Arial", 9, "bold"), anchor="e")
        lbl.grid(row=row_idx, column=0, sticky="e", padx=(10, 10), pady=6)
        widget.grid(row=row_idx, column=1, sticky="w", pady=6)

        if show_check:
            check = tk.Label(form_frame, text="✔", fg=check_green, bg="white", font=("Arial", 10, "bold"))
            check.grid(row=row_idx, column=2, sticky="w", padx=5)

    email_entry = ttk.Entry(form_frame, width=35)
    email_entry.insert(0, "test@gmail.com")
    add_row(0, "Email", email_entry)

    pwd_entry = ttk.Entry(form_frame, width=35)
    pwd_entry.insert(0, "password123")
    add_row(1, "Пароль", pwd_entry)

    name_entry = ttk.Entry(form_frame, width=35)
    name_entry.insert(0, "Руслан")
    add_row(2, "Имя", name_entry)

    surname_entry = ttk.Entry(form_frame, width=35)
    surname_entry.insert(0, "Тертышный")
    add_row(3, "Фамилия", surname_entry)

    nick_entry = ttk.Entry(form_frame, width=35)
    nick_entry.insert(0, "TRos")
    add_row(4, "Никнейм", nick_entry)

    dob_entry = ttk.Entry(form_frame, width=35)
    dob_entry.insert(0, "4 Ноября 1988")
    add_row(5, "Дата рождения", dob_entry)

    gender_frame = tk.Frame(form_frame, bg="white")
    gender_var = tk.StringVar(value="Мужчина")
    rb_m = tk.Radiobutton(gender_frame, text="Мужчина", variable=gender_var, value="Мужчина", bg="white", fg="#333", font=("Arial", 9))
    rb_f = tk.Radiobutton(gender_frame, text="Женщина", variable=gender_var, value="Женщина", bg="white", fg="#333", font=("Arial", 9))
    rb_m.pack(side="left", padx=(0, 10))
    rb_f.pack(side="left")
    add_row(6, "Пол", gender_frame)

    loc_entry = ttk.Entry(form_frame, width=35)
    loc_entry.insert(0, "Другой город")
    add_row(7, "Место проживания", loc_entry)

    buttons_frame = tk.Frame(form_frame, bg="white")
    buttons_frame.grid(row=8, column=1, sticky="w", pady=(20, 0))

    reg_btn = tk.Button(buttons_frame, text="Регистрация", bg=main_blue, fg="white", font=("Arial", 10, "bold"), relief="flat", width=15, pady=5)
    reg_btn.pack(side="left", padx=(0, 10))

    root.mainloop()

if __name__ == "__main__":
    create_ui()
