import tkinter as tk
from tkinter import ttk

def create_ui():
    root = tk.Tk()
    root.title("Регистрация")
    root.geometry("650x450")  # Уменьшил высоту, так как элементов стало меньше
    root.configure(bg="#e8eef2") # Светло-серый фон страницы

    # --- Стили ---
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TEntry", padding=3)
    
    # Цвета
    main_blue = "#38a3d5"
    text_blue = "#4a8fb3"
    check_green = "#4caf50"
    
    # --- Заголовок страницы ---
    header_label = tk.Label(root, text="Регистрация", font=("Arial", 16, "bold"), fg=main_blue, bg="#e8eef2")
    header_label.pack(anchor="nw", padx=30, pady=(20, 10))

    # --- Основной контейнер формы (белый фон) ---
    main_frame = tk.Frame(root, bg="white", bd=1, relief="ridge")
    main_frame.pack(fill="both", expand=True, padx=30, pady=(0, 30))

    # Синяя плашка "Создание нового сайта"
    banner_frame = tk.Frame(main_frame, bg=main_blue, height=40)
    banner_frame.pack(fill="x")
    banner_label = tk.Label(banner_frame, text="Создание нового сайта", bg=main_blue, fg="white", font=("Arial", 12))
    banner_label.pack(pady=10)

    # --- Фрейм для полей ввода (Grid Layout) ---
    form_frame = tk.Frame(main_frame, bg="white")
    form_frame.pack(pady=20, padx=20)

    # Вспомогательная функция для добавления строк формы
    def add_row(row_idx, label_text, widget, show_check=True):
        lbl = tk.Label(form_frame, text=label_text, bg="white", fg=text_blue, font=("Arial", 9, "bold"), anchor="e")
        lbl.grid(row=row_idx, column=0, sticky="e", padx=(10, 10), pady=6)
        widget.grid(row=row_idx, column=1, sticky="w", pady=6)
        
        if show_check:
            check = tk.Label(form_frame, text="✔", fg=check_green, bg="white", font=("Arial", 10, "bold"))
            check.grid(row=row_idx, column=2, sticky="w", padx=5)

    # 1. Email
    email_entry = ttk.Entry(form_frame, width=35)
    email_entry.insert(0, "test@gmail.com")
    add_row(0, "Email", email_entry)

    # 2. Пароль (теперь без show="*", текст пишется открыто)
    pwd_entry = ttk.Entry(form_frame, width=35)
    pwd_entry.insert(0, "password123")
    add_row(1, "Пароль", pwd_entry)

    # 3. Имя
    name_entry = ttk.Entry(form_frame, width=35)
    name_entry.insert(0, "Руслан")
    add_row(2, "Имя", name_entry)

    # 4. Фамилия
    surname_entry = ttk.Entry(form_frame, width=35)
    surname_entry.insert(0, "Тертышный")
    add_row(3, "Фамилия", surname_entry)

    # 5. Никнейм
    nick_entry = ttk.Entry(form_frame, width=35)
    nick_entry.insert(0, "TRos")
    add_row(4, "Никнейм", nick_entry)

    # 6. Дата рождения (теперь обычное поле для ввода текста вместо выпадающих списков)
    dob_entry = ttk.Entry(form_frame, width=35)
    dob_entry.insert(0, "4 Ноября 1988")
    add_row(5, "Дата рождения", dob_entry)

    # 7. Пол (теперь простое неизменяемое текстовое поле)
    gender_entry = ttk.Entry(form_frame, width=35)
    gender_entry.insert(0, "Мужчина")
    gender_entry.configure(state="readonly") # Запрет на изменение текста
    add_row(6, "Пол", gender_entry)

    # 8. Место проживания (теперь простое неизменяемое текстовое поле)
    loc_entry = ttk.Entry(form_frame, width=35)
    loc_entry.insert(0, "Другой город")
    loc_entry.configure(state="readonly") # Запрет на изменение текста
    add_row(7, "Место проживания", loc_entry)

    # --- Кнопка Регистрация ---
    reg_btn = tk.Button(form_frame, text="Регистрация", bg=main_blue, fg="white", 
                        font=("Arial", 10, "bold"), relief="flat", width=15, pady=5)
    reg_btn.grid(row=8, column=1, sticky="w", pady=(20, 0))

    root.mainloop()

if __name__ == "__main__":
    create_ui()
