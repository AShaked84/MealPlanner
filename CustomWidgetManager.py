from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QHBoxLayout, QPushButton
from PyQt6.QtCore import pyqtSignal

import DatabaseManager as DM


class MealListItem(QWidget):
    servings_change_requested = pyqtSignal(int, int)

    def __init__(self, db_id, meal_id, servings, parent=None):
        super().__init__(parent)

        self.db_id = db_id
        self.meal_id = meal_id

        self.item_layout = QVBoxLayout(self)
        self.title_layout = QHBoxLayout()

        self.title = QLabel(DM.idRecipe(db_id))
        self.serving_label = QLabel(str(servings))

        self.minus_button = QPushButton("-")
        self.plus_button = QPushButton("+")

        self.details = QLabel("Placeholder text")
        self.details.hide()

        self.minus_button.setFixedSize(25, 25)
        self.plus_button.setFixedSize(25, 25)
        self.serving_label.setFixedSize(25, 25)

        self.title_layout.addWidget(self.title)
        self.title_layout.addWidget(self.minus_button)
        self.title_layout.addWidget(self.serving_label)
        self.title_layout.addWidget(self.plus_button)

        self.item_layout.addLayout(self.title_layout)
        self.item_layout.addWidget(self.details)

        self.minus_button.clicked.connect(
            lambda: self.request_serving_change(-1)
        )
        self.plus_button.clicked.connect(
            lambda: self.request_serving_change(1)
        )

    def request_serving_change(self, delta):
        self.servings_change_requested.emit(self.meal_id, delta)

    def set_servings(self, servings):
        self.serving_label.setText(str(servings))

"""from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QListWidgetItem
)
from PyQt6.QtCore import Qt

import DatabaseManager as DM

class MealListItem(QWidget):
    def __init__(self, db_id, selected_date, parent = None):
        super().__init__(parent)

        self.db_id = db_id
        self.selected_date = selected_date

        self.item_layout = QHBoxLayout()

        self.title_layout = QHBoxLayout()
        self.title = QLabel(DM.idRecipe(db_id))
        self.title_layout.addWidget(self.title)

        self.item_layout.addLayout(self.title_layout)

        self.details = QLabel(str(db_id))
        self.details.hide()

        self.item_layout.addWidget(self.details)
        self.setLayout(self.item_layout)"""