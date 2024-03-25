from PySide6.QtWidgets import QFileDialog

class FileDialog:
    @staticmethod
    def choose_json_file():
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(None, "Выберите JSON файл", "", "JSON Files (*.json)", options=options)
        if file_path:
            return file_path, "JSON-файл выбран"
        else:
            return None, "Файл не выбран"
        
    @staticmethod
    def choose_txt_file():
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(None, "Выберите TXT файл", "", "TXT Files (*.txt)", options=options)
        if file_path:
            return file_path, "TXT-файл выбран"
        else:
            return None, "Файл не выбран"
    
    @staticmethod
    def choose_json_file_for_save():
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(None, "Сохранить JSON файл", "", "JSON Files (*.json)", options=options)
        if file_path:
            return file_path, "JSON-файл для сохранения выбран"
        else:
            return None, "Операция сохранения отменена"

