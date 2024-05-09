def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                _, salary= line.strip().split(',')
                salary = int(salary)
                salaries.append(salary)
            total = sum(salaries)
            average = total / len(salaries)
            return (total, average)
    except FileNotFoundError:
        print("Файл не знайдено.")
        return (0, 0)
    except Exception:
        print(f"Сталася помилка.")
        return (0, 0)

total, average = total_salary("task_1.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
