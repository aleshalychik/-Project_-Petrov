import tkinter as tk
from tkinter import ttk

def create_ui():
    root = tk.Tk()
    root.title("Регистрация")
    root.geometry("650x550")
    root.configure(bg="#e8eef2") # Светло-серый фон страницы

    # --- Стили ---
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TEntry", padding=3)
    style.configure("TCombobox", padding=3)
    
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

    # Вспомогательная функция для добавления стандартной строки формы
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

    # 2. Пароль
    pwd_entry = ttk.Entry(form_frame, width=35, show="*")
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

    # 6. Дата рождения (Составной виджет)
    dob_frame = tk.Frame(form_frame, bg="white")
    day_cb = ttk.Combobox(dob_frame, width=3, values=[str(i) for i in range(1, 32)])
    day_cb.set("4")
    day_cb.pack(side="left", padx=(0, 5))
    
    month_cb = ttk.Combobox(dob_frame, width=12, values=["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"])
    month_cb.set("Ноябрь")
    month_cb.pack(side="left", padx=5)
    
    year_cb = ttk.Combobox(dob_frame, width=5, values=[str(i) for i in range(1970, 2010)])
    year_cb.set("1988")
    year_cb.pack(side="left", padx=5)
    add_row(5, "Дата рождения", dob_frame)

    # 7. Пол (Radiobuttons)
    gender_frame = tk.Frame(form_frame, bg="white")
    gender_var = tk.StringVar(value="m")
    rb_m = tk.Radiobutton(gender_frame, text="Мужчина", variable=gender_var, value="m", bg="white", fg="#333", font=("Arial", 9))
    rb_f = tk.Radiobutton(gender_frame, text="Женщина", variable=gender_var, value="f", bg="white", fg="#333", font=("Arial", 9))
    rb_m.pack(side="left")
    rb_f.pack(side="left")
    add_row(6, "Пол", gender_frame)

    # 8. Место проживания
    loc_cb = ttk.Combobox(form_frame, width=33, values=["Другой город", "Москва", "Санкт-Петербург"])
    loc_cb.set("Другой город")
    add_row(7, "Место проживания", loc_cb)

    # 9. Код безопасности (Капча)
    captcha_frame = tk.Frame(form_frame, bg="white")
    capt_entry = ttk.Entry(captcha_frame, width=8)
    capt_entry.insert(0, "VPyJL")
    capt_entry.pack(side="left", padx=(0, 5))
    
    arrow_lbl = tk.Label(captcha_frame, text="←", bg="white", fg="#777")
    arrow_lbl.pack(side="left", padx=2)
    
    # Имитация картинки с капчей
    img_lbl = tk.Label(captcha_frame, text=" VPyJL ", font=("Georgia", 16, "italic"), bg="#e8f5e9", fg="black")
    img_lbl.pack(side="left", padx=5)
    
    refresh_lbl = tk.Label(captcha_frame, text="↻", bg="white", fg="#777", font=("Arial", 12))
    refresh_lbl.pack(side="left")
    add_row(8, "Код безопасности", captcha_frame)

    # --- Блок с условиями и кнопкой ---
    
    # Чекбокс условий
    terms_var = tk.BooleanVar(value=True)
    terms_cb = tk.Checkbutton(form_frame, text="Подтверждаю условия использования uID сообщества", 
                              variable=terms_var, bg="white", fg="#333", font=("Arial", 9))
    terms_cb.grid(row=9, column=1, columnspan=2, sticky="w", pady=(15, 0))

    # Мелкий текст под чекбоксом
    sub_lbl = tk.Label(form_frame, text="Мы гарантируем: Ваша конфиденциальная информация никогда не попадет в чужие руки.", 
                       font=("Arial", 7), fg="#999", bg="white")
    sub_lbl.grid(row=10, column=1, columnspan=2, sticky="w", padx=25)

    # Кнопка Регистрация
    reg_btn = tk.Button(form_frame, text="Регистрация", bg=main_blue, fg="white", 
                        font=("Arial", 10, "bold"), relief="flat", width=15, pady=5)
    reg_btn.grid(row=11, column=1, sticky="w", pady=(15, 0))

    root.mainloop()

if __name__ == "__main__":
    create_ui()

