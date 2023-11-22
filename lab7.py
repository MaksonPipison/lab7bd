import sqlite3
from datetime import datetime

# Підключення до бази даних (створить файл бази даних, якщо його не існує)
conn = sqlite3.connect('planner.db')
cursor = conn.cursor()

# Створення таблиці, якщо її не існує
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Events (
        event_id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_name TEXT NOT NULL,
        event_date DATE NOT NULL,
        event_time TIME,
        event_description TEXT
    );
''')
conn.commit()

def create_event(name, date, time, description):
    """Додавання події"""
    cursor.execute('''
        INSERT INTO Events (event_name, event_date, event_time, event_description)
        VALUES (?, ?, ?, ?);
    ''', (name, date, time, description))
    conn.commit()
    print("Подія додана успішно.")

def read_events():
    """Виведення всіх подій"""
    cursor.execute('SELECT * FROM Events;')
    events = cursor.fetchall()
    if events:
        for event in events:
            print(event)
    else:
        print("Немає жодної події.")

def update_event(event_id, new_name, new_date, new_time, new_description):
    """Оновлення події"""
    cursor.execute('''
        UPDATE Events
        SET event_name=?, event_date=?, event_time=?, event_description=?
        WHERE event_id=?;
    ''', (new_name, new_date, new_time, new_description, event_id))
    conn.commit()
    print("Подія оновлена успішно.")

def delete_event(event_id):
    """Видалення події"""
    cursor.execute('DELETE FROM Events WHERE event_id=?;', (event_id,))
    conn.commit()
    print("Подія видалена успішно.")

# Приклад використання
create_event('Зустріч з друзями', '2023-11-25', '18:00', 'Обговорення планів на вихідні')
create_event('Зустріч на роботі', '2023-11-26', '09:30', 'Презентація проекту')
read_events()

update_event(1, 'Зустріч з друзями', '2023-11-25', '19:00', 'Обговорення планів на вихідні')
read_events()

delete_event(2)
read_events()

# Закриття підключення до бази даних
conn.close()
