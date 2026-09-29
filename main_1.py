# Программа приветствия пользователя

def ask_name():
    """Запрашивает имя пользователя и возвращает его."""
    name = input("Напишите ваше имя: ")
    return name

def main():
    name = ask_name()
    print(f"Привет, {name}!")

if __name__ == "__main__":
    main()
