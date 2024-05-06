def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            for line in file:
                id, name, age = line.strip().split(',')
                cats_info.append({"id": id, "name": name, "age": age})
            return cats_info
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception:
        print("Сталася помилка.")
        return []

cats_info = get_cats_info("task_2.txt")
print(cats_info)
