from app.utils import Validator

class TestCase_Validator_JsonFile:
    def test_no_valid_no_json(self):
        excepted = False
        excepted_message = 'Ошибка: файл участников должен иметь расширение ".json". "app/tests/test_data/json/no_valid/no_json.txt"'
        
        file_path = 'app/tests/test_data/json/no_valid/no_json.txt'
        actual, actual_message = Validator.json_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_bad_json(self):
        excepted = False
        excepted_message = 'Ошибка чтения JSON файла: "Expecting property name enclosed in double quotes: line 1 column 2 (char 1)"'
        
        file_path = 'app/tests/test_data/json/no_valid/bad_json.json'
        actual, actual_message = Validator.json_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_without_top_lvl_key(self):
        excepted = False
        excepted_message = 'Ошибка: JSON-файл должен содержать объект верхнего уровня. "app/tests/test_data/json/no_valid/no_top_lvl_key.json"'
        
        file_path = 'app/tests/test_data/json/no_valid/no_top_lvl_key.json'
        actual, actual_message = Validator.json_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_empty(self):
        excepted = False
        excepted_message = 'Ошибка: JSON-файл не должен быть пустым. "app/tests/test_data/json/no_valid/empty.json"'
        
        file_path = 'app/tests/test_data/json/no_valid/empty.json'
        actual, actual_message = Validator.json_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_no_exists(self):
        excepted = False
        excepted_message = 'Ошибка: Файл не найден. "app/tests/test_data/json/no_valid/no_exist.json"'
        
        file_path = 'app/tests/test_data/json/no_valid/no_exist.json'
        actual, actual_message = Validator.json_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_no_format(self):
        excepted = False
        excepted_message = 'Ошибка: Неверный формат данных для ключа "1". Ожидается словарь с соответствующими полями.'
        
        file_path = 'app/tests/test_data/json/no_valid/no_format.json'
        actual, actual_message = Validator.json_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_no_name(self):
        excepted = False
        excepted_message = 'Ошибка: В файле отсутствует обязательное поле "Name" или "Surname" для ключа "1".'
        
        file_path = 'app/tests/test_data/json/no_valid/no_name.json'
        actual, actual_message = Validator.json_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_no_surname(self):
        excepted = False
        excepted_message = 'Ошибка: В файле отсутствует обязательное поле "Name" или "Surname" для ключа "1".'
        
        file_path = 'app/tests/test_data/json/no_valid/no_surname.json'
        actual, actual_message = Validator.json_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_empty_name(self):
        excepted = False
        excepted_message = 'Ошибка: Поля "Name" или "Surname" не могут быть пустым для ключа "1".'
        
        file_path = 'app/tests/test_data/json/no_valid/empty_name.json'
        actual, actual_message = Validator.json_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_bad_key(self):
        excepted = False
        excepted_message = 'Ошибка: Ключ "name" должен содержать только цифры.'
        
        file_path = 'app/tests/test_data/json/no_valid/bad_key.json'
        actual, actual_message = Validator.json_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_valid_normal(self):
        excepted = True
        excepted_message = 'Успешная валидация JSON-файла. "app/tests/test_data/json/valid/valid.json"'
        
        file_path = 'app/tests/test_data/json/valid/valid.json'
        actual, actual_message = Validator.json_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_valid_over_filds(self):
        excepted = True
        excepted_message = 'Успешная валидация JSON-файла. "app/tests/test_data/json/valid/over_fields.json"'
        
        file_path = 'app/tests/test_data/json/valid/over_fields.json'
        actual, actual_message = Validator.json_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message
    
    def test_valid_bad_simbol(self):
        excepted = True
        excepted_message = 'Успешная валидация JSON-файла. "app/tests/test_data/json/valid/bad_simbol.json"'
        
        file_path = 'app/tests/test_data/json/valid/bad_simbol.json'
        actual, actual_message = Validator.json_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message


class TestCase_Validator_TxtFile:
    def test_no_valid_no_format(self):
        excepted = False
        excepted_message = 'Ошибка: файл результатов должен иметь расширение ".txt". "app/tests/test_data/txt/no_valid/no_format.json"'
        
        file_path = 'app/tests/test_data/txt/no_valid/no_format.json'
        actual, actual_message = Validator.txt_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_bad_number(self):
        excepted = False
        excepted_message = 'Ошибка: Файл содержит не корректные данные: "a start 16:22:30,000000"'
        
        file_path = 'app/tests/test_data/txt/no_valid/bad_number.txt'
        actual, actual_message = Validator.txt_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_bad_action(self):
        excepted = False
        excepted_message = 'Ошибка: Файл содержит не корректные данные: "1 a 16:22:30,000000"'
        
        file_path = 'app/tests/test_data/txt/no_valid/bad_action.txt'
        actual, actual_message = Validator.txt_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_bad_time_161(self):
        excepted = False
        excepted_message = 'Ошибка: Файл содержит не корректные данные: "1 start 161:22:30,000000"'
        
        file_path = 'app/tests/test_data/txt/no_valid/bad_time_161.txt'
        actual, actual_message = Validator.txt_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_bad_time_hours(self):
        excepted = False
        excepted_message = 'Ошибка: Время указано не корректно: "1 start 25:22:30,000000"'
        
        file_path = 'app/tests/test_data/txt/no_valid/bad_time_hours.txt'
        actual, actual_message = Validator.txt_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_bad_time_minutes(self):
        excepted = False
        excepted_message = 'Ошибка: Время указано не корректно: "1 start 16:62:30,000000"'
        
        file_path = 'app/tests/test_data/txt/no_valid/bad_time_minutes.txt'
        actual, actual_message = Validator.txt_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_bad_time_second(self):
        excepted = False
        excepted_message = 'Ошибка: Время указано не корректно: "1 start 16:22:90,000000"'
        
        file_path = 'app/tests/test_data/txt/no_valid/bad_time_seconds.txt'
        actual, actual_message = Validator.txt_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_no_exist_file(self):
        excepted = False
        excepted_message = 'Ошибка: Файл не найден. "app/tests/test_data/txt/no_valid/no_exist.txt"'
        
        file_path = 'app/tests/test_data/txt/no_valid/no_exist.txt'
        actual, actual_message = Validator.txt_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_empty(self):
        excepted = False
        excepted_message = 'Ошибка: TXT-файл не должен быть пустым. "app/tests/test_data/txt/no_valid/empty.txt"'
        
        file_path = 'app/tests/test_data/txt/no_valid/empty.txt'
        actual, actual_message = Validator.txt_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_valid_normal(self):
        excepted = True
        excepted_message = 'Успешная валидация TXT-файла. "app/tests/test_data/txt/valid/valid.txt"'
        
        file_path = 'app/tests/test_data/txt/valid/valid.txt'
        actual, actual_message = Validator.txt_file(file_path)
        
        assert actual == excepted
        assert actual_message == excepted_message


class TestCase_Validator_timesData:
    def test_no_valid_no_start(self):
        excepted = False
        excepted_message = 'Ошибка: В файле отсутствует обязательное поле "start" или "finish" для номера "1".'
        
        data = {
            "1" : {
                "start" : "16:22:30,000000"
            }
        }

        actual, actual_message = Validator.times_data(data)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_no_valid_no_finish(self):
        excepted = False
        excepted_message = 'Ошибка: В файле отсутствует обязательное поле "start" или "finish" для номера "1".'
        
        data = {
            "1" : {
                "finish" : "16:22:30,000000"
            }
        }

        actual, actual_message = Validator.times_data(data)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_valid_normal(self):
        excepted = True
        excepted_message = 'Успешная валидация данных.'
        
        data = {
            "1" : {
                "start" : "16:22:30,000000",
                "finish" : "16:22:30,000000"
            }
        }

        actual, actual_message = Validator.times_data(data)
        
        assert actual == excepted
        assert actual_message == excepted_message

    def test_valid_over_data(self):
        excepted = True
        excepted_message = 'Успешная валидация данных.'
        
        data = {
            "1" : {
                "start" : "16:22:30,000000",
                "finish" : "16:23:30,000000",
                "result" : "1"
            }
        }

        actual, actual_message = Validator.times_data(data)
        
        assert actual == excepted
        assert actual_message == excepted_message



    

    