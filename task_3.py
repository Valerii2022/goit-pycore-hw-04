import sys
from pathlib import Path
from colorama import init, Fore, Style
import os

init(autoreset=True)  # Ініціалізувати colorama, автоматично скидаючи кольори

def print_directory_structure(path, indent=0):
    if not path.is_dir():
        print(f"{Fore.RED}Помилка: {path} не є директорією.")
        return

    for item in path.iterdir():
        if item.is_dir():
            # Відображаємо директорії з певним відступом і кольором
            print("  " * indent + f"{Fore.BLUE}📂 {item.name}")
            # Рекурсивно проходимо піддиректорії
            print_directory_structure(item, indent + 1)
        else:
            # Відображаємо файли з певним відступом і кольором
            print("  " * indent + f"{Fore.GREEN}📜 {item.name}")

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Будь ласка, вкажіть шлях до директорії як аргумент командного рядка.")
        return
    
    path_str = sys.argv[1]
    path = Path(path_str)

    if not path.exists():
        print(f"{Fore.RED}Помилка: Шлях {path_str} не існує.")
        return
    
    print_directory_structure(path)

if __name__ == "__main__":
    main()