import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
''')

countries = [('Кыргызстан',), ('Германия',), ('Китай',), ('Россия',), ('США',)]
cursor.executemany("INSERT INTO countries (title) VALUES (?)", countries)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0.0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id)
    )
''')

cities = [
    ('Бишкек', 160.0, 1),
    ('Ош', 182.5, 1),
    ('Берлин', 891.85, 2),
    ('Мюнхен', 310.7, 2),
    ('Пекин', 16410.54, 3),
    ('Шанхай', 6340.5, 3),
    ('Москва', 2561.5, 4)
]
cursor.executemany("INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)", cities)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(id)
    )
''')

students = [
    ('Айбек', 'Петров', 1),
    ('Самат', 'Иванов', 1),
    ('Гульмира', 'Сидорова', 2),
    ('Эрмек', 'Кузнецов', 2),
    ('Анна', 'Шмидт', 3),
    ('Лукас', 'Мюллер', 3),
    ('София', 'Вагнер', 4),
    ('Йонас', 'Браун', 4),
    ('Ли', 'Ван', 5),
    ('Мэй', 'Чен', 5),
    ('Чжао', 'Вэй', 6),
    ('Хуан', 'Ли', 6),
    ('Дмитрий', 'Смирнов', 7),
    ('Елена', 'Попова', 7),
    ('Игорь', 'Морозов', 1)
]
cursor.executemany("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", students)

conn.commit()
conn.close()

print("База данных 'university.db' успешно создана и заполнена.")