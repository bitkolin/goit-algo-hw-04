def get_cats_info(path):
    """Читає файл з даними котів і повертає список словників
    з ключами "id", "name", "age". Якщо файл недоступний, повертає []."""
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")
                cat = {"id": cat_id, "name": name, "age": age}
                cats.append(cat)
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return []
    except ValueError:
        print(f"Файл '{path}' пошкоджений або має неправильний формат.")
        return []

    return cats


cats_info = get_cats_info("cats_file.txt")
print(cats_info)