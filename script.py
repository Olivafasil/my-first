print("Привет, GitHub! 🚀")
import random
import string

def generate_password(length=12):
    """Генерирует случайный пароль заданной длины."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔒 Генератор паролей 🔒")
    
    try:
        length = int(input("Введите длину пароля (по умолчанию 12): ") or 12)
        if length < 6:
            print("⚠ Пароль должен быть не менее 6 символов.")
            return
        
        password = generate_password(length)
        print(f"✅ Ваш случайный пароль: {password}")
    
    except ValueError:
        print("❌ Ошибка: Введите число!")

if __name__ == "__main__":
    main()
