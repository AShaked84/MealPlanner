import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from GUIManager import Ui_MainWindow

app = QApplication(sys.argv)

MainWindow = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.initialize_app()

MainWindow.show()

sys.exit(app.exec())