import json

#Преобразует список словарей в JSON-строку и сохраняет в файл.
def dict_list_to_json(dict_list, filename):
    try:
        json_str = json.dumps(dict_list, ensure_ascii=False)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_str)
        return json_str
    except (TypeError, ValueError, IOError) as e:
        print(f"При преобразовании списка словарей в Json-строку произошла ошибка: {e}")
        return None

#Преобразует JSON-строку из файла в список словарей.
def json_to_dict_list(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            json_str = file.read()
            dict_list = json.loads(json_str)
        return dict_list
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при чтении файла или преобразовании строки в список словарей: {e}")
        return None