#Приложение ГРУЗОВЫЕ ПЕРЕВОЗКИ для некоторой организации. БД должна содержать таблицу
#Перевозки со следующей структурой записи: маршрут, фамилия водителя, даты отправки и прибытия, масса груза.

import sqlite3

# 1. Подключение к базе данных (файл car_rental.db создастся автоматически)
connection = sqlite3.connect('car_rental.db')
cursor = connection.cursor()

# 2. Создание таблицы "Клиент" в соответствии с Вариантом 23
cursor.execute('''
CREATE TABLE IF NOT EXISTS Client (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fio TEXT NOT NULL,
    car_brand TEXT NOT NULL,
    rental_period INTEGER,
    amount REAL,
    prepayment TEXT
)
''')
connection.commit()

# Очистим таблицу перед демонстрацией (чтобы данные не дублировались при повторном запуске)
cursor.execute("DELETE FROM Client")
connection.commit()

# 3. Добавление (INSERT) начальных данных в таблицу
clients_data = [
    ('Иванов Иван Иванович', 'Toyota Camry', 5, 25000.0, 'да'),
    ('Петров Петр Петрович', 'Hyundai Solaris', 3, 12000.0, 'нет'),
    ('Сидоров Сидор Сидорович', 'BMW X5', 7, 70000.0, 'да')
]

cursor.executemany('''
INSERT INTO Client (fio, car_brand, rental_period, amount, prepayment)
VALUES (?, ?, ?, ?, ?)
''', clients_data)
connection.commit()

# Функция для красивого вывода таблицы в консоль
def display_clients(title):
    print(f"\n=== {title} ===")
    cursor.execute("SELECT * FROM Client")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]} | ФИО: {row[1]} | Авто: {row[2]} | Срок: {row[3]} дн. | Сумма: {row[4]} руб. | Предоплата: {row[5]}")

# Выводим первоначальные данные
display_clients("Данные в базе после добавления")


# =====================================================================
# 4. ОБНОВЛЕНИЕ ДАННЫХ (UPDATE)
# =====================================================================
# Пример 1: Петров Петр Петрович внес предоплату, меняем 'нет' на 'да'
print("\n[Выполнение UPDATE]: Изменяем статус предоплаты для Петрова...")
cursor.execute('''
UPDATE Client
SET prepayment = 'да'
WHERE fio = 'Петров Петр Петрович'
''')

# Пример 2: Иванову увеличили срок проката до 6 дней и, соответственно, сумму до 30000
print("[Выполнение UPDATE]: Обновляем срок и сумму проката для Иванова...")
cursor.execute('''
UPDATE Client
SET rental_period = 6, amount = 30000.0
WHERE fio = 'Иванов Иван Иванович'
''')

# Сохраняем изменения в базе данных
connection.commit()
# =====================================================================


# 5. Выводим данные еще раз, чтобы увидеть результат обновлений
display_clients("Данные в базе ПОСЛЕ выполнения UPDATE")

# Закрытие соединения с базой данных
connection.close()
