def total_salary(path):
    """Рахує загальну та середню зарплату з файлу path. Повертає кортеж (сума, середнє)."""
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return 0, 0
    except ValueError:
        print(f"Файл '{path}' пошкоджений або має неправильний формат.")
        return 0, 0

    if count == 0:
        return 0, 0

    average = total / count
    return total, average


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")