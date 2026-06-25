#Приложение ГРУЗОВЫЕ ПЕРЕВОЗКИ для некоторой организации. БД должна содержать таблицу
#Перевозки со следующей структурой записи: маршрут, фамилия водителя, даты отправки и прибытия, масса груза.

import sqlite3

connection = sqlite3.connect('car_rental.db')
cursor = connection.cursor()

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

cursor.execute("DELETE FROM Client")
connection.commit()

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

def display_clients(title):
    print(f"\n=== {title} ===")
    cursor.execute("SELECT * FROM Client")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]} | ФИО: {row[1]} | Авто: {row[2]} | Срок: {row[3]} дн. | Сумма: {row[4]} руб. | Предоплата: {row[5]}")

display_clients("Данные в базе после добавления")

print("\n[Выполнение UPDATE]: Изменяем статус предоплаты для Петрова...")
cursor.execute('''
UPDATE Client
SET prepayment = 'да'
WHERE fio = 'Петров Петр Петрович'
''')

print("[Выполнение UPDATE]: Обновляем срок и сумму проката для Иванова...")
cursor.execute('''
UPDATE Client
SET rental_period = 6, amount = 30000.0
WHERE fio = 'Иванов Иван Иванович'
''')

connection.commit()

display_clients("Данные в базе ПОСЛЕ выполнения UPDATE")

connection.close()
