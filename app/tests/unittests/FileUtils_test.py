from app.utils import FileUtils
import os, json

class TestCase_parseJsonFile:
    def test_no_valid_no_exist(self):
        excepted = None
        excepted_message = 'Ошибка: Файл не найден: "app/tests/test_data/json/no_valid/no_exist.json"'

        file_path = 'app/tests/test_data/json/no_valid/no_exist.json'
        actual, actual_message = FileUtils.parse_json_file(file_path)

        assert actual is excepted
        assert actual_message == excepted_message

    def test_valid_normal(self):
        excepted = {
            "1" : {
                "Name": "Name",
                "Surname": "Surname"
            },
            "2" : {
                "Name": "Name2",
                "Surname": "Surname2"
            }
        }
        except_message = 'Успешный парсинг JSON-файла'

        file_path = 'app/tests/test_data/json/valid/valid.json'
        actual, actual_message = FileUtils.parse_json_file(file_path)

        assert actual == excepted
        assert actual_message == except_message

class TestCase_parseTxtFile:
    def test_no_valid_no_exist(self):
        excepted = None
        excepted_message = 'Ошибка: Файл не найден: "app/tests/test_data/txt/no_exist.txt"'

        file_path = 'app/tests/test_data/txt/no_exist.txt'
        actual, actual_message = FileUtils.parse_txt_file(file_path)

        assert actual is excepted
        assert actual_message == excepted_message

    def test_valid_normal(self):
        excepted = {
            "1" : {
                "start" : "16:22:30,000000",
                "finish" : "16:23:40,100000"
            },
            "2" : {
                "start" : "16:24:30,000000",
                "finish" : "16:25:50,300000"
            }
        }
        excepted_message = 'Успешный парсинг TXT-файла'

        file_path = 'app/tests/test_data/txt/valid/valid.txt'
        actual, actual_message = FileUtils.parse_txt_file(file_path)

        assert actual == excepted
        assert actual_message == excepted_message

class TestCase_saveToJsonFile:
    def test_valid_no_exist(self):
        excepted = True
        excepted_message = 'Результат сохранен в JSON-файл "app/tests/test_data/json/valid/no_exist.json"'

        file_path = 'app/tests/test_data/json/valid/no_exist.json'
        data = {
            "1" : {
                "Name": "Name",
                "Surname": "Surname"
            },
            "2" : {
                "Name": "Name2",
                "Surname": "Surname2"
            }
        }
        actual, actual_message = FileUtils.save_to_json_file(file_path, data)

        assert actual == excepted
        assert actual_message == excepted_message

        with open(file_path, 'r', encoding='utf-8') as file:
            actual_data = json.load(file)
        
        assert actual_data == data
        os.remove(file_path)
