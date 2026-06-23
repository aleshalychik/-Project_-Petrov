#Приложение ГРУЗОВЫЕ ПЕРЕВОЗКИ для некоторой организации. БД должна содержать таблицу
#Перевозки со следующей структурой записи: маршрут, фамилия водителя, даты отправки и прибытия, масса груза.

import sqlite3

conn = sqlite3.connect('freight.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Перевозки (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    маршрут TEXT NOT NULL,
    фамилия_водителя TEXT NOT NULL,
    дата_отправки TEXT NOT NULL,
    дата_прибытия TEXT NOT NULL,
    масса_груза REAL NOT NULL
)
''')
conn.commit()


def add_transport(route, driver, dep_date, arr_date, weight):
    cursor.execute('''
    INSERT INTO Перевозки (маршрут, фамилия_водителя, дата_отправки, дата_прибытия, масса_груза)
    VALUES (?, ?, ?, ?, ?)
    ''', (route, driver, dep_date, arr_date, weight))
    conn.commit()
    print(f" Успешно добавлено: Маршрут '{route}', Водитель: {driver}")


def show_all_transports():
    cursor.execute('SELECT * FROM Перевозки')
    rows = cursor.fetchall()

    print("\n БАЗА: ГРУЗОВЫЕ ПЕРЕВОЗКИ ---")
    if not rows:
        print("База данных пуста.")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Маршрут: {row[1]} | Водитель: {row[2]} | "
                  f"Отправка: {row[3]} | Прибытие: {row[4]} | Масса: {row[5]} т.")
    print("-----------------------------------\n")


cursor.execute('DELETE FROM Перевозки')
conn.commit()

add_transport('Москва - Санкт-Петербург', 'Иванов', '2026-06-01', '2026-06-03', 15.5)
add_transport('Казань - Екатеринбург', 'Петров', '2026-06-05', '2026-06-08', 20.0)
add_transport('Новосибирск - Владивосток', 'Сидоров', '2026-06-10', '2026-06-25', 12.3)

show_all_transports()

conn.close()
