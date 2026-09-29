# Программа приветствия пользователя

def ask_first_name():
    """Запрашивает имя пользователя."""
    return input("Напишите, пожалуйста, ваше имя: ")

def ask_last_name():
    """Запрашивает фамилию пользователя."""
    return input("Напишите вашу фамилию: ")

def main():
    first = ask_first_name()
    last = ask_last_name()
    print(f"Привет, {first} {last}!")

if __name__ == "__main__":
    main()