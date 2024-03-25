import json
import re
import os
import unicodedata

class Validator:
    @staticmethod
    def json_file(file_path):
        file_format = os.path.splitext(file_path)[-1]
        if file_format != '.json':
            return False, f'Ошибка: файл участников должен иметь расширение ".json". "{file_path}"'

        try:
            with open(file_path, 'r', encoding='utf-8-sig') as file:
                data = json.load(file)
                if not data:
                    return False, f'Ошибка: JSON-файл не должен быть пустым. "{file_path}"'
                
                if not isinstance(data, dict):
                    return False, f'Ошибка: JSON-файл должен содержать объект верхнего уровня. "{file_path}"'
                
                for key, value in data.items():
                    key = unicodedata.normalize('NFKD', key).encode('ascii', 'ignore').decode('utf-8')
                    if not re.match(r'^[0-9]+$', key):
                        return False, f'Ошибка: Ключ "{key}" должен содержать только цифры.'
                    if not isinstance(value, dict):
                        return False, f'Ошибка: Неверный формат данных для ключа "{key}". Ожидается словарь с соответствующими полями.'
                    if "Name" not in value or "Surname" not in value:
                        return False, f'Ошибка: В файле отсутствует обязательное поле "Name" или "Surname" для ключа "{key}".'
                    if not isinstance(value["Name"], str) or not isinstance(value["Surname"], str):
                        return False, f'Ошибка: Поля "Name" или "Surname" должны иметь строковый тип значений для ключа "{key}".'
                    if value["Name"] == "" or value["Surname"] == "":
                        return False, f'Ошибка: Поля "Name" или "Surname" не могут быть пустым для ключа "{key}".'
        except FileNotFoundError:
            return False, f'Ошибка: Файл не найден. "{file_path}"'
        except json.JSONDecodeError as e:
            return False, f'Ошибка чтения JSON файла: "{e}"'
        return True, f'Успешная валидация JSON-файла. "{file_path}"'
        
    @staticmethod
    def txt_file(file_path):
        file_format = os.path.splitext(file_path)[-1]
        if file_format != '.txt':
            return False, f'Ошибка: файл результатов должен иметь расширение ".txt". "{file_path}"'
    
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as file:
                lines = file.readlines()
                if not lines:
                    return False, f'Ошибка: TXT-файл не должен быть пустым. "{file_path}"'
                for line in lines:
                    line = line.strip()
                    match = re.match(r'^\d+ (start|finish) (\d{2}):(\d{2}):(\d{2}),(\d+)$', line)
                    if not match:
                        return False, f'Ошибка: Файл содержит не корректные данные: "{line}"'
                    hour = int(match.group(2))
                    minute = int(match.group(3))
                    second = int(match.group(4))
                    if hour >= 24 or minute >= 60 or second >= 60:
                        return False, f'Ошибка: Время указано не корректно: "{line}"'
                    
                return True, f'Успешная валидация TXT-файла. "{file_path}"'
        except FileNotFoundError:
            return False, f'Ошибка: Файл не найден. "{file_path}"'
        
    @staticmethod
    def times_data(data):
        for key, value in data.items():
            if "start" not in value or "finish" not in value:
                return False, f'Ошибка: В файле отсутствует обязательное поле "start" или "finish" для номера "{key}".'
        return True, "Успешная валидация данных."

        
class ResultUtils:
    @staticmethod
    def time_to_seconds(time_str: str) -> float:
        parts = time_str.split(':')
        seconds, milliseconds = parts[2].split(',')
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(seconds)
        milliseconds = float('0.' + milliseconds)
        total_seconds = hours * 3600 + minutes * 60 + seconds + milliseconds
        return total_seconds
    
    @classmethod
    def calculate(cls, time_start: str, time_finish: str) -> float:
        start_seconds = cls.time_to_seconds(time_start)
        finish_seconds = cls.time_to_seconds(time_finish)
        if finish_seconds < start_seconds:
            finish_seconds += 24 * 3600
        return finish_seconds - start_seconds
    
    @staticmethod
    def second_to_result(second_float: float) -> str:
        miliseconds = int(round(second_float % 1 * 100))

        second = int(second_float)
        hours = int(second // 3600)
        if not hours:
            minutes = int((second % 3600) // 60)
            seconds = int(second % 60)
        else: 
            minutes = 59
            seconds = 59
            miliseconds = 99
        
        return f"{minutes:02d}:{seconds:02d},{miliseconds}"

    @classmethod
    def sort_by_time(cls, results: list) -> list:
        results = sorted(results, key=lambda x: x['result_second'])

        data = []
        place = 1
        for result in results:
            data.append(
                {
                    'place': place,
                    'number': result['number'],
                    'name': result['name'],
                    'surname': result['surname'],
                    'result': cls.second_to_result(result['result_second'])
                }
            )
            place += 1
        return data
        
    @classmethod
    def get_result(cls, times: list, competitors: list) -> list:
        data = []
        for time in times:
            data.append(
                {
                    'number': time['number'],
                    'name': competitors[time['number']]['name'],
                    'surname': competitors[time['number']]['surname'],
                    'result_second': cls.calculate(time['start_time'], time['finish_time'])
                }
            )
        
        data = cls.sort_by_time(data)
        return data
    
    @staticmethod
    def result_to_valid_view(results: list):
        data = {}
        for result in results:
            data[result['place']] = {
                'Нагрудный номер': result['number'],
                'Имя': result['name'],
                'Фамилия': result['surname'],
                'Результат': result['result']
            }
        return data


class FileUtils:
    @staticmethod
    def parse_json_file(file_path):
        """
        - Файл для парсинга поступает после валидации
        - Контроль входных данных не осуществляется
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            return None, f'Ошибка: Файл не найден: "{file_path}"'
        return data, "Успешный парсинг JSON-файла"

    @staticmethod
    def parse_txt_file(file_path):
        """
        - Файл для парсинга поступает после валидации
        - Контроль входных данных не осуществляется
        """
        data = {}
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip().split()
                    number = line[0]
                    action = line[1]
                    time = line[2]
                    if number not in data:
                        data[number] = {}
                    data[number][action] = time
        except FileNotFoundError:
            return None, f'Ошибка: Файл не найден: "{file_path}"'
        return data, "Успешный парсинг TXT-файла"
        
    @staticmethod
    def save_to_json_file(file_path, data):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            return False, f'Ошибка: Не удалось сохранить результат: {e}'
        return True, f'Результат сохранен в JSON-файл "{file_path}"'
        
    @staticmethod
    def get_filename(file_path):
        return os.path.basename(file_path)

            


