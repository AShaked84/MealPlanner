from PyQt6.QtWidgets import QFormLayout, QListWidget, QSizePolicy, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QPushButton
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

class RecipeCard(QWidget):
    def __init__(self, db_id, parent = None):
        super().__init__(parent)

        self.db_id = db_id

        self.item_layout = QVBoxLayout(self)
        self.item_layout.setContentsMargins(15, 15, 15, 15)
        self.item_layout.setSpacing(8)

        self.title = QLabel(DM.idRecipe(db_id))
        self.title.setMinimumHeight(self.title.sizeHint().height())
        self.item_layout.addWidget(self.title)

        self.details = QWidget()
        self.detailsLayout = QFormLayout(self.details)

        servings = str(DM.recipeServings(db_id)[0])
        self.default_servings = QLabel(servings)
        ingredients = DM.getIngredients(db_id)
        print(ingredients)

        self.detailsLayout.addRow("Default servings: ", self.default_servings)
        for ingredient in ingredients:
            self.detailsLayout.addRow(str(ingredient[3]) + " " + ingredient[2], QLabel(ingredient[0]))

        self.item_layout.addWidget(self.details)

        """self.details = QLabel("Placeholder text")
        self.item_layout.addWidget(self.details)"""
        self.details.hide()

    """def update_size(self):
        self.item_layout.activate()
        return self.item_layout.sizeHint()"""

    def update_size(self):
        # Activate inner layouts first, then the outer one
        self.details.layout().activate()
        self.item_layout.invalidate()
        self.item_layout.activate()

        # Use the widget's sizeHint, which includes margins
        hint = self.sizeHint()

        # Optionally enforce the width of the list so wrapping labels compute correctly
        return hint

