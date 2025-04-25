import sqlite3

conn = sqlite3.connect("test_products.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS categories")
cursor.execute("DROP TABLE IF EXISTS stores")

cursor.execute("""
CREATE TABLE categories (
    code TEXT PRIMARY KEY,
    title TEXT
)
""")

cursor.execute("""
CREATE TABLE stores (
    store_id INTEGER PRIMARY KEY,
    title TEXT
)
""")

cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    title TEXT,
    category_code TEXT,
    unit_price REAL,
    stock_quantity INTEGER,
    store_id INTEGER,
    FOREIGN KEY (category_code) REFERENCES categories(code),
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
)
""")

stores_data = [
    (1, 'Asia'),
    (2, 'Globus'),
    (3, 'Spar')
]
cursor.executemany("INSERT INTO stores (store_id, title) VALUES (?, ?)", stores_data)

categories_data = [
    ('FD', 'Food products'),
    ('EL', 'Electronics'),
    ('CL', 'Clothing'),
    ('BT', 'Beauty'),
    ('HG', 'Home & Garden'),
    ('SP', 'Sports'),
    ('BK', 'Books'),
    ('TO', 'Toys'),
    ('PH', 'Pharmacy'),
    ('OF', 'Office Supplies'),
]
cursor.executemany("INSERT INTO categories (code, title) VALUES (?, ?)", categories_data)

products_data = [
    (1, 'Chocolate', 'FD', 10.5, 129, 1),
    (2, 'Laptop', 'EL', 850.0, 12, 2),
    (3, 'T-shirt', 'CL', 15.0, 50, 3),
    (4, 'Face Cream', 'BT', 25.0, 30, 1),
    (5, 'Garden Chair', 'HG', 45.5, 20, 2),
    (6, 'Soccer Ball', 'SP', 18.99, 100, 3),
    (7, 'Novel "Python Master"', 'BK', 12.5, 75, 1),
    (8, 'LEGO Set', 'TO', 60.0, 15, 2),
    (9, 'Painkiller', 'PH', 5.2, 200, 3),
    (10, 'Notebook Pack', 'OF', 8.9, 90, 1),
]
cursor.executemany("""
INSERT INTO products (id, title, category_code, unit_price, stock_quantity, store_id)
VALUES (?, ?, ?, ?, ?, ?)
""", products_data)

conn.commit()

def show_menu():
    print("\nВы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
    cursor.execute("SELECT store_id, title FROM stores")
    for store in cursor.fetchall():
        print(f"{store[0]}. {store[1]}")

def show_products_by_store(store_id):
    cursor.execute("""
    SELECT p.title, c.title, p.unit_price, p.stock_quantity
    FROM products p
    JOIN categories c ON p.category_code = c.code
    WHERE p.store_id = ?
    """, (store_id,))
    results = cursor.fetchall()
    if results:
        for product in results:
            print(f"\nНазвание продукта: {product[0]}\nКатегория: {product[1]}\nЦена: {product[2]}\nКоличество на складе: {product[3]}")
    else:
        print("Нет продуктов в этом магазине.")

while True:
    show_menu()
    choice = input("Введите id магазина: ")
    if choice == '0':
        print("Выход из программы.")
        break
    elif choice.isdigit() and int(choice) in [1, 2, 3]:
        show_products_by_store(int(choice))
    else:
        print("Пожалуйста, введите корректный id магазина (1, 2 или 3).")

conn.close()