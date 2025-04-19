import sqlite3

def create_database():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title VARCHAR(200) NOT NULL,
            price REAL(10, 2) NOT NULL DEFAULT 0.0,
            quantity INTEGER NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()
    print("База данных и таблица 'products' успешно созданы.")

def add_products():
    products_to_add = [
        ('Яблоко Голден', 55.50, 100),
        ('Банан Эквадор', 70.00, 150),
        ('Молоко Parmalat', 95.75, 50),
        ('Хлеб Бородинский', 45.20, 80),
        ('Сыр Российский', 320.00, 30),
        ('Масло сливочное', 180.50, 40),
        ('Чай черный Lipton', 110.00, 120),
        ('Кофе Jacobs Monarch', 250.30, 60),
        ('Сахар песок', 65.80, 200),
        ('Соль поваренная', 25.15, 250),
        ('Макароны Barilla', 85.40, 90),
        ('Рис Басмати', 150.60, 70),
        ('Куриное филе', 280.90, 35),
        ('Яйца куриные (10шт)', 90.25, 110),
        ('Вода питьевая Аква', 35.00, 300)
    ]
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", products_to_add)
    conn.commit()
    conn.close()
#    print(f"{len(products_to_add)} товаров успешно добавлены.")

def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    conn.commit()
    conn.close()
    print(f"Количество товара с id {product_id} успешно изменено на {new_quantity}.")

def update_price(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()
    conn.close()
    print(f"Цена товара с id {product_id} успешно изменена на {new_price}.")

def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()
    print(f"Товар с id {product_id} успешно удален.")

def select_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    all_products = cursor.fetchall()
    conn.close()
    if all_products:
        print("\nВсе товары в базе данных:")
        for product in all_products:
            print(f"ID: {product[0]}, Название: {product[1]}, Цена: {product[2]}, Количество: {product[3]}")
    else:
        print("В базе данных нет товаров.")

def select_cheap_and_plentiful(price_limit, quantity_limit):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE price < ? AND quantity > ?", (price_limit, quantity_limit))
    selected_products = cursor.fetchall()
    conn.close()
    if selected_products:
        print(f"\nТовары дешевле {price_limit} сом и с количеством больше {quantity_limit} шт:")
        for product in selected_products:
            print(f"ID: {product[0]}, Название: {product[1]}, Цена: {product[2]}, Количество: {product[3]}")
    else:
        print(f"Нет товаров дешевле {price_limit} сом и с количеством больше {quantity_limit} шт.")

def search_product_by_title(search_term):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE product_title LIKE ?", ('%' + search_term + '%',))
    found_products = cursor.fetchall()
    conn.close()
    if found_products:
        print(f"\nТовары, содержащие '{search_term}' в названии:")
        for product in found_products:
            print(f"ID: {product[0]}, Название: {product[1]}, Цена: {product[2]}, Количество: {product[3]}")
    else:
        print(f"Товары, содержащие '{search_term}' в названии, не найдены.")

# Тестирование функций
if __name__ == "__main__":
    create_database()
    add_products()

    select_all_products()

    update_quantity(1, 120)
    update_price(2, 75.50)

    select_all_products()

    delete_product(16)

    select_all_products()

    select_cheap_and_plentiful(100, 50)

    search_product_by_title("Яблоко")
    search_product_by_title("мыло")
