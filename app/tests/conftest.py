import os
import sys
import pytest
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from app.view import MainView, ResultModel
from app.database.db import Base, engine, session, competitorsModel, timeModel




