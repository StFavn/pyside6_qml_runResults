#### Установка и запуск проекта
Для запуска проекта выполните следующие шаги:
1. Склонируйте репозиторий на локальное устройство 
```
git clone
```
2. Рекомендуется создать виртуальную среду python и установить зависимости
```
python3.10 -m venv myenv
sourсe myvenv/bin/activate
pip install -r requirements.txt
```
3. Запустите проект
```
python3 main.py
```

#### Пример работы приложения
1. Вам необходимо выбрать 2 файла: 
	- Данные участников в формате .json
	- Данные забегов в формате .txt
	Файлы должны иметь строгий формат данных:
	- Файл участников должен иметь словарь, с ключем - номером участника и значение в виде словаря с именем и фамилией
	- Каждая строка файла забегов должна быть представлена в виде данных типа \[номер, действие(start|finish\], и время в формате ЧЧ:ММ:СС:милисекунды
```
Пример json файла
{
	"123" : {
		"Name" : "name",
		"Surname" : "surname"
	},
	...
}

Пример txt файла
123 start 12:22:23:000000
```

2. После внесения данных необходимо нажать кнопку "Расчитать". Вы увидите таблицу с результатами отсортированных по времени от меньшего к большему
3. Вы можете сохранить результаты в json файл
4. Предусматривается возможность произвести сброс данных

#### Реализация проекта
- Программа написана с использованием библиотеки pyside6 и языка разметки qml
- Система логирования представленна в виде отображения сообщений в консоль.
- Выбор файла производится через диалоговое окно, предоставляемое pyside6.QtWidgets в виде объекта QFileDialog
- После выбора файла, файл валидируется. В случае любой ошибки, информация об ошибке отправляется в console.log через signal message
- После успешной валидации файла, данные парсятся из файла к удобному для чтения типу данных и сохраняются в базу данных sqlite. Для работы с базой данных используется orm sqlalchemy
- Во время расчета, данные выгружаются из базы данных и формируются в общую структуру "Номер" "имя" "фамилия" "результат". Результат представляется в виде float значения, которое является результатом вычитания строковых значений времени finish и start, приведенных к float секундам. 
- После форматирования к общей структуре, данные сортируются, а затем возвращаются с добавлением к каждому значению поля "Место"
- Результат расчетов отправляется в модель отображения pyside6, которая является объектом QAbstractListModel
- После расчета данных, информацию можно сохранить через диалоговое окно  QFileDialog

#### Архитектура проекта
- Особенностью архитектуры является решение взаимодействия элементов программы через главный интерфейс mainView. 5 основных функций (принять json файл, принять txt файл, расчитать, сохранить, сбросить) принимают сигнал от пользовательского интерфейса и запускают цепочку подфункций, которые импортируются из 3х основных модулей, которые инкапсулированы друг от друга.
- Модуль dialogs имеет 3 функции запуска фиалоговых окон, которые возвращают путь к выбранному файлу
- Модуль utils имеет 3 класса функций, которые также изолированы друг от друга
	- Валидация - имеет 3 основные функции
		- валидация json файла участников
		- валидация txt файла результатов
		- валидация результатов забегов после парсинга данных - здесь я убеждаюсь, что каждый элемент имеет оба действия start и finish
	- Файловые утилиты -  здесь представленые 2 функции парсинга значений и одна функция записи результатов в файл, а также дополнительная утилита вывода названия файла для использования в некоторых сообщения логирования
	- Система расчетов - цепочка функций для произведения необходимых вычислений
		- парсинг строкового значения времени и вычисление результата, возвращаемого в виде float значения
		- перевод float значения в строковый, требуемый тип результата
		- сортировка словаря
		- функция, производящая расчет и возвращающая данные в виде структуры для модели отображения
		- функция, приводящая данные модели к требуемому виду для сохранения в json формат
- Модуль для работы с базой данных 
	- создание базы
	- отчистка базы
	- удаление базы
	- запись участников
	- запись результато забегов
	- получение данных из базы участников
	- получение данных из базы результатов

#### Тестирование 
- Тестирование реализуется через библиотеку pyside
- Запуск тестов осуществляется через команду 
```
pyside -v
```
- На данный момент имеется полное покрытие unit для функций валидаций файлов и парсинга

#### Примечания
- TODO: Необходимо иметь полное unit покрытие для всех утилит программы (Ведь если что-то не покрыто тестами, значит это что-то не написано)
- TODO: Необходимо реализовать интеграционное тестирование через библиотеку pytest-qt
- TODO: Необходимо провести тестирование на высокой нагрузке для оптимизации приложения, так как из-за глубокой валидации, парсинга и записи, программа на больших объемах данных может работать медленно. 
- Можно было бы не добавлять базу данных в проект, а держать результат парсинга в памяти, но это может негативно сказываться при работе с большим объемом данных.
- Благодаря подобной архитектуре для расширения программы(например добавления еще одного файла для парсинга или изменения шаблона) не потребуется больших затрат по времени. 