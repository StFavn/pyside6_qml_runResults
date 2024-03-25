import sys
import os

from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from app.view import MainView, ResultModel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    resultModel = ResultModel()
    main = MainView(resultModel)
    main.init_db()

    engine.rootContext().setContextProperty("backend", main)
    engine.rootContext().setContextProperty("resultModel", resultModel)
    
    engine.load(os.path.join(os.path.dirname(__file__), "qml/main.qml"))
    
    app.aboutToQuit.connect(main.close_db)

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())

