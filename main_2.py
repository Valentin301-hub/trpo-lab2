# Бета-версия обновления

from datetime import datetime

def ask_first_name():
    """Запрашивает имя пользователя."""
    return input("Напишите, пожалуйста, ваше имя: ")

def ask_last_name():
    """Запрашивает фамилию пользователя."""
    return input("Напишите вашу фамилию: ")

def get_greeting():
    """Возвращает приветствие в зависимости от времени суток."""
    hour = datetime.now().hour
    if hour < 12:
        return "Доброе утро"
    elif hour < 18:
        return "Добрый день"
    else:
        return "Добрый вечер"

def main():
    first = ask_first_name()
    last = ask_last_name()
    greeting = get_greeting()
    print(f"{greeting}, {first} {last}!")

if __name__ == "__main__":
    main()