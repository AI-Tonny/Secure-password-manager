Secure Password Manager
Опис проєкту
Цей "Менеджер паролів" є простим та безпечним інструментом для зберігання паролів. Паролі шифруються за допомогою бібліотеки cryptography (модуль Fernet), а дані зберігаються у форматі JSON. Програма підтримує автоматичний вихід після 1 хвилини бездіяльності для забезпечення додаткової безпеки.

Функціональні можливості
Додавання нового облікового запису та пароля
Перегляд існуючих облікових записів та паролів
Оновлення пароля для існуючого облікового запису
Видалення облікового запису
Автоматичний вихід після 1 хвилини бездіяльності
Вимоги
Python 3.7 або новіша версія
Бібліотека cryptography
Встановити бібліотеку cryptography можна за допомогою команди:

bash
Копіювати код
pip install cryptography
Основні файли
manager.json - файл для збереження зашифрованих даних паролів у JSON форматі.
key.key - файл для зберігання ключа шифрування, який генерується лише один раз.
Основні функції
Генерація ключа шифрування
Функція Write_key генерує ключ шифрування, якщо його ще не існує, та зберігає його у файлі key.key.

python
Копіювати код
def Write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
Завантаження ключа
Функція Load_key читає збережений ключ з файлу key.key і повертає його.

python
Копіювати код
def Load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
        return key
Таймер автоматичного виходу
Функція start_logout_timer запускає таймер, який автоматично завершує програму через 60 секунд неактивності.

python
Копіювати код
def start_logout_timer():
    global logout_timer
    if logout_timer is not None:
        logout_timer.cancel()
    logout_timer = threading.Timer(TIMEOUT, automatic_logout)
    logout_timer.start()
Завантаження та запис даних
Функція Load_data завантажує JSON дані з файлу manager.json. Якщо файл порожній або не існує, функція повертає порожній словник.

python
Копіювати код
def Load_data():
    with open("manager.json", "r") as json_file:
        try:
            data = json.load(json_file)
            return data
        except json.decoder.JSONDecodeError:
            return {}
Функція Write_data записує JSON дані у файл manager.json.

python
Копіювати код
def Write_data(filename, database):
    with open(filename, "w") as json_file:
        json.dump(database, json_file)
Основні операції над обліковими записами
Перегляд бази даних (View_database): відображає всі облікові записи та паролі у розшифрованому вигляді.

Додавання облікового запису (Add_account): зчитує назву облікового запису та пароль, шифрує пароль і зберігає його у базі даних.

Видалення облікового запису (Delete_account): видаляє обліковий запис, якщо він існує в базі даних.

Оновлення пароля (Update_password): оновлює зашифрований пароль для існуючого облікового запису.

Приклад використання
Після запуску програма запитує користувача, яку операцію він хоче виконати:

view - перегляд бази даних
add - додавання нового облікового запису
delete - видалення облікового запису
update - оновлення пароля
q - вихід з програми
Основний код
python
Копіювати код
if __name__ == "__main__":
    main()
Цей фрагмент запускає основну функцію програми, main, яка керує головним циклом та скидає таймер активності після кожної взаємодії з користувачем.

Запуск проєкту
Скопіюйте файли до своєї робочої директорії.
Запустіть програму з командного рядка:
bash
Копіювати код
python Secure_password_manager.py
Дотримуйтесь інструкцій на екрані для роботи з базою даних паролів.
