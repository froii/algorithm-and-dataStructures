import sys
import shutil
from pathlib import Path


def copy_files_recursively(src_dir: Path, dest_dir: Path):
    try:
        for item in src_dir.iterdir():
            if item.is_dir():
                copy_files_recursively(item, dest_dir)
            elif item.is_file():
                extension = item.suffix[1:] or 'no_extension'
                target_dir = dest_dir / extension
                target_dir.mkdir(parents=True, exist_ok=True)

                shutil.copy2(item, target_dir / item.name)
                print(f"Copied: {item} -> {target_dir / item.name}")

    except PermissionError:
        print(f"Permission denied: {item}")
    except Exception as e:
        print(f"Error processing {item}: {e}")


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    dest = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('dist')

    if not src.exists():
        print(f"Source directory doesn't exist: {src}")
        return

    copy_files_recursively(src, dest)


if __name__ == "__main__":
    main()


# 1. Парсинг аргументів. Скрипт приймає два аргументи командного рядка: шлях до вихідної директорії та шлях до директорії призначення(за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).

# 2. Рекурсивне читання директорій:
# Написана функція, яка приймає шлях до директорії як аргумент.
# Функція перебирає всі елементи у директорії.
# Якщо елемент є директорією, функція викликає саму себе рекурсивно для цієї директорії.
# Якщо елемент є файлом, він є обробленим для копіювання.

# 3. Копіювання файлів:
# Для кожного типу файлів створюється новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
# Файл з відповідним типом копіюється у відповідну піддиректорію.

# 4. Обробка винятків: код обробляє винятки, наприклад, помилки доступу до файлів або директорій.

# 5. Після виконання програми всі файли у вихідній директорії рекурсивно скопійовано в нову директорію та розсортовано в піддиректорії за їх розширенням.
