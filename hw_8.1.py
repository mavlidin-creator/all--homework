import sqlite3

def display_students_by_city():
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()

    print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()

    for city_id, city_title in cities:
        print(f"{city_title} (ID: {city_id})")

    while True:
        try:
            city_id_input = int(input("Введите ID города для просмотра учеников (или 0 для выхода): "))
            if city_id_input == 0:
                break
            elif city_id_input > 0:
                cursor.execute("SELECT title FROM cities WHERE id = ?", (city_id_input,))
                city_result = cursor.fetchone()
                if city_result:
                    city_name = city_result[0]
                    cursor.execute('''
                        SELECT s.first_name, s.last_name, cy.title AS city_name, co.title AS country_name, cy.area
                        FROM students s
                        JOIN cities cy ON s.city_id = cy.id
                        JOIN countries co ON cy.country_id = co.id
                        WHERE cy.id = ?
                    ''', (city_id_input,))
                    students = cursor.fetchall()

                    if students:
                        print(f"\nСписок учеников, проживающих в городе {city_name}:")
                        for first_name, last_name, city, country, area in students:
                            print(f"  Имя: {first_name}, Фамилия: {last_name}, Город: {city}, Страна: {country}, Площадь города: {area}")
                    else:
                        print(f"Нет учеников, проживающих в городе с ID {city_id_input}.")
                else:
                    print(f"Города с ID {city_id_input} не существует.")
            else:
                print("Пожалуйста, введите корректный ID города или 0 для выхода.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

    conn.close()
    print("Программа завершена.")

if __name__ == "__main__":
    display_students_by_city()