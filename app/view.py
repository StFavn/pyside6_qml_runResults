from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt, QObject, Slot, Signal

from app.utils import Validator, ResultUtils, FileUtils
from app.dialogs import FileDialog
from app.database.db_utils import DatabaseUtils


class MainView(QObject):
    def __init__(self, resultModel):
        QObject.__init__(self)
        self.resultModel = resultModel

    message = Signal(str)
    jsonValid = Signal(str)
    txtValid = Signal(str)
    isCalculated = Signal(str)
    isSaved = Signal(str)
    isReset = Signal(str)

    jsonFileName = None
    txtFileName = None
    calculated = False

    @Slot()
    def openJsonFile(self):
        if not self.jsonFileName:
            file_path, message = FileDialog.choose_json_file()
            self.message.emit(message)
            if not file_path: 
                self.jsonValid.emit("default"); return

            is_valid, message = Validator.json_file(file_path)
            self.message.emit(message)
            if not is_valid: 
                self.jsonValid.emit("error"); return
            
            json_data, message = FileUtils.parse_json_file(file_path)
            self.message.emit(message)
            if not json_data: 
                self.jsonValid.emit("error"); return

            is_valid, message = DatabaseUtils.save_to_competitorsModel(json_data)
            self.message.emit(message)
            if not is_valid: 
                self.jsonValid.emit("error"); return

            self.jsonFileName = FileUtils.get_filename(file_path)
            self.jsonValid.emit("valid")
        else:
            self.message.emit(f'Файл {self.jsonFileName} уже загружен')
        
    @Slot()
    def openTxtFile(self):
        if not self.txtFileName:
            file_path, message = FileDialog.choose_txt_file()
            self.message.emit(message)
            if not file_path:
                self.txtValid.emit("default"); return

            is_valid, message = Validator.txt_file(file_path)
            self.message.emit(message)
            if not is_valid:
                self.txtValid.emit("error"); return
            
            txt_data, message = FileUtils.parse_txt_file(file_path)
            self.message.emit(message)
            if not txt_data:
                self.txtValid.emit("error"); return
            
            is_valid, message = Validator.times_data(txt_data)
            self.message.emit(message)
            if not is_valid:
                self.txtValid.emit("error"); return

            is_valid, message = DatabaseUtils.save_to_timesModel(txt_data)
            self.message.emit(message)
            if not is_valid:
                self.txtValid.emit("error"); return

            self.txtFileName = FileUtils.get_filename(file_path)
            self.txtValid.emit("valid")
        else:
            self.message.emit(f'Файл {self.txtFileName} уже загружен')

    @Slot()
    def calculateResult(self):
        if not self.jsonFileName or not self.txtFileName:
            self.message.emit("Необходимо выбрать JSON-файл и TXT-файл")
        elif self.calculated:
            self.message.emit("Результат уже получен")
        else:
            times = DatabaseUtils.get_times()
            competitors = DatabaseUtils.get_competitors()
            data = ResultUtils.get_result(times, competitors)
            self.resultModel.updateData(data)
            self.calculated = True
            self.isCalculated.emit("valid")

    @Slot()
    def saveJsonFile(self):
        if self.calculated:
            file_path, message = FileDialog.choose_json_file_for_save()
            self.message.emit(message)
            if not file_path: 
                self.isSaved.emit("default"); return

            data = self.resultModel.get_data()
            data_valid_view = ResultUtils.result_to_valid_view(data)
            is_valid, message = FileUtils.save_to_json_file(file_path, data_valid_view)
            self.message.emit(message)
            if not is_valid:
                self.isSaved.emit("error"); return

            self.isSaved.emit("valid")
        else:
            self.message.emit("Результат ещё не получен")

    @Slot()
    def reset(self):
        is_valid, message = DatabaseUtils.clear_database()
        self.message.emit(message)
        if not is_valid: 
            self.isReset.emit("error"); return

        self.jsonValid.emit("default")
        self.txtValid.emit("default")
        self.isCalculated.emit("default")
        self.isSaved.emit("default")
        self.isReset.emit("default")

        self.jsonFileName = None
        self.txtFileName = None
        self.calculated = False
        self.resultModel.updateData([])

        self.message.emit("Успешный сброс информации")

    def init_db(self):
        is_valid, message = DatabaseUtils.create_database()
        self.message.emit(message)
        return is_valid
    
    def close_db(self):
        is_valid, message = DatabaseUtils.delete_database()
        self.message.emit(message)
        return is_valid



class ResultModel(QAbstractListModel):
    PlaceRole  = Qt.UserRole + 1
    NumberRole = Qt.UserRole + 2
    NameRole = Qt.UserRole + 3
    SurnameRole = Qt.UserRole + 4
    ResultRole = Qt.UserRole + 5

    def __init__(self, data=[], parent=None):
        super().__init__(parent)
        self._data = data

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self._data)):
            return None

        row = index.row()
        item = self._data[row]

        if role == self.PlaceRole:
            return item['place']
        elif role == self.NumberRole:
            return item['number']
        elif role == self.NameRole:
            return item['name']
        elif role == self.SurnameRole:
            return item['surname']
        elif role == self.ResultRole:
            return item['result']

    def roleNames(self):
        roles = {
            self.PlaceRole: b'place',
            self.NumberRole: b'number',
            self.NameRole: b'name',
            self.SurnameRole: b'surname',
            self.ResultRole: b'result'
        }
        return roles
        
    def updateData(self, new_data):
        self.beginResetModel()
        self._data = new_data
        self.endResetModel()

    def get_data(self):
        return self._data