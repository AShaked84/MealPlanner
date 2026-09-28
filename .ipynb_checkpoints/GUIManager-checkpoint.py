from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QLineEdit, QListWidget, QInputDialog, QFormLayout, QDialog, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit, QListWidgetItem
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import QDate, Qt
import json

import DatabaseManager as DM
import IngredientLister as IL


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(29, 40, 421, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddMyRecipeButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.AddMyRecipeButton.setObjectName("AddMyRecipeButton")
        self.horizontalLayout.addWidget(self.AddMyRecipeButton)
        self.AddURLRecipeButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.AddURLRecipeButton.setObjectName("AddURLRecipeButton")
        self.horizontalLayout.addWidget(self.AddURLRecipeButton)
        self.SeeRecipesButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.SeeRecipesButton.setObjectName("SeeRecipesButton")
        self.horizontalLayout.addWidget(self.SeeRecipesButton)
        self.ShoppingListButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.ShoppingListButton.setObjectName("ShoppingListButton")
        self.horizontalLayout.addWidget(self.ShoppingListButton)
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(130, 160, 200, 144))
        self.calendarWidget.setObjectName("calendarWidget")

        self.menuWidget = QtWidgets.QWidget(parent = self.centralwidget)
        self.menuWidget.setGeometry(QtCore.QRect(370, 160, 300, 271))
        self.menuWidget.setObjectName("MenuWidget")

        self.menuLayout = QtWidgets.QVBoxLayout(self.menuWidget)
        self.menuLayout.setObjectName("MenuLayOut")

        self.breakfastLayout = QtWidgets.QVBoxLayout()
        self.breakfastLayout.setObjectName("BreakfastLayout")
        self.breakfastLabel = QtWidgets.QLabel(parent = self.menuWidget)
        self.breakfastLabel.setObjectName("Breakfast")
        self.breakfastLabel.setText("Breakfast")
        self.breakfastList = QtWidgets.QListWidget(parent = self.menuWidget)
        self.breakfastList.setObjectName("BreakfastList")
        self.breakfastLayout.addWidget(self.breakfastLabel)
        self.breakfastLayout.addWidget(self.breakfastList)

        self.lunchLayout = QtWidgets.QVBoxLayout()
        self.lunchLayout.setObjectName("LunchLayout")
        self.lunchLabel = QtWidgets.QLabel(parent = self.menuWidget)
        self.lunchLabel.setObjectName("Lunch")
        self.lunchLabel.setText("Lunch")
        self.lunchList = QtWidgets.QListWidget(parent = self.menuWidget)
        self.lunchList.setObjectName("LunchList")
        self.lunchLayout.addWidget(self.lunchLabel)
        self.lunchLayout.addWidget(self.lunchList)

        self.dinnerLayout = QtWidgets.QVBoxLayout()
        self.dinnerLayout.setObjectName("DinnerLayout")
        self.dinnerLabel = QtWidgets.QLabel(parent = self.menuWidget)
        self.dinnerLabel.setObjectName("Dinner")
        self.dinnerLabel.setText("Dinner")
        self.dinnerList = QtWidgets.QListWidget(parent = self.menuWidget)
        self.dinnerList.setObjectName("DinnerList")
        self.dinnerLayout.addWidget(self.dinnerLabel)
        self.dinnerLayout.addWidget(self.dinnerList)

        self.snacksLayout = QtWidgets.QVBoxLayout()
        self.snacksLayout.setObjectName("SnackLayout")
        self.snacksLabel = QtWidgets.QLabel(parent = self.menuWidget)
        self.snacksLabel.setObjectName("Snacks")
        self.snacksLabel.setText("Snacks")
        self.snacksList = QtWidgets.QListWidget(parent = self.menuWidget)
        self.snacksList.setObjectName("SnacksList")
        self.snacksLayout.addWidget(self.snacksLabel)
        self.snacksLayout.addWidget(self.snacksList)

        self.menuLayout.addLayout(self.breakfastLayout)
        self.menuLayout.addLayout(self.lunchLayout)
        self.menuLayout.addLayout(self.dinnerLayout)
        self.menuLayout.addLayout(self.snacksLayout)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.AddURLRecipeButton.clicked.connect(self.add_recipe_URL_lineEdit)
        self.AddMyRecipeButton.clicked.connect(self.add_my_recipe_form)
        self.SeeRecipesButton.clicked.connect(self.add_recipe_list)

        self.calendarWidget.clicked.connect(self.date_clicked)

    def date_clicked(self, date:QDate):
        date_string = date.toString("dd-MM-yyyy")
        
        self.breakfastList.clear()
        self.lunchList.clear()
        self.dinnerList.clear()
        self.snacksList.clear()
            
        rows = DM.todaysMeals(date_string)

        for row in rows:
            meal_list = getattr(self, row[2].lower() + "List") 
            meal_list.addItem(DM.idRecipe(row[3])[0][0])

    def fill_meal(self, date: QDate):
        date_string = date.toString("dd-MM-yyyy")
        date_dialog = QDialog(parent = self.centralwidget)
        date_dialog.setWindowTitle(f'{date_string} Meal Plan')

        meal_type_list = ["Breakfast", "Lunch", "Dinner", "Snacks"]

        window_layout = QVBoxLayout()
        lists_layout = QHBoxLayout()
        meal_type_layout = QVBoxLayout()
        recipe_list_layout = QVBoxLayout()

        meal_list = QListWidget()
        meal_type_layout.addWidget(meal_list)
        meal_list.addItems(meal_type_list)

        recipe_list = QListWidget()
        recipe_list_dictionary = DM.listRecipes()

        for db_id, title in recipe_list_dictionary.items():
            item = QListWidgetItem(str(title))
            item.setData(Qt.ItemDataRole.UserRole, db_id)
            recipe_list.addItem(item)
        #recipe_list.addItems(DM.listRecipes())
        #self.populate_list(recipe_list)
        recipe_list.hide()
        recipe_list_layout.addWidget(recipe_list)

        lists_layout.addLayout(meal_type_layout)
        lists_layout.addLayout(recipe_list_layout)

        button_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        cancel_button = QPushButton("Cancel")
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)

        window_layout.addLayout(lists_layout)
        window_layout.addLayout(button_layout)
        date_dialog.setLayout(window_layout)

        meal_list.itemClicked.connect(lambda item: recipe_list.show())
        recipe_list.itemClicked.connect(self.handle_selection)

        save_button.clicked.connect(date_dialog.accept)
        cancel_button.clicked.connect(date_dialog.reject)
        
        result = date_dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            selected_meal = meal_list.selectedItems()
            selected_recipe = recipe_list.selectedItems()
            if selected_meal and selected_recipe:
                meal_type = selected_meal[0].text()
                # Get the hidden recipe ID from the selected item
                chosen_recipe_id = selected_recipe[0].data(Qt.ItemDataRole.UserRole)

            DM.addMeal(date_string, meal_type, chosen_recipe_id)        
        #return meal_type, chosen_recipe_id, date_string
                
        return None, None, None

    def handle_selection(self, item):
        selected_key = item.data(Qt.ItemDataRole.UserRole)
        return selected_key

    """def populate_list(self, list_name):
        self.dm_instance = DM()
        rows = self.dm_instance.loadRecipes()
        for ID, RecipeName in rows:
            item = QListWidgetItem(RecipeName)
            item.setData(Qt.ItemDataRole, ID)
            list_name.addItem(item)"""

    def initialize_app(self):
        self.meal_plan = DM.getMealPlan()

    def add_recipe_URL_lineEdit(self):
        """self.recipe_input_field = QLineEdit(parent = self.centralwidget)
        add_new_recipe = QtWidgets.QPushButton(parent = self.centralwidget)
        self.recipe_input_field.setGeometry(40, 100, 200, 40)
        add_new_recipe.setGeometry(250, 100, 40, 40)
        self.recipe_input_field.show()
        add_new_recipe.show()
        add_new_recipe.clicked.connect(lambda checked: DM.addRecipe(self.recipe_input_field.text()))"""
        text, ok = QInputDialog.getText(self.centralwidget, "Add Recipe URL", "Enter Recipe URL: ")
        if ok and text:
            DM.addRecipe(text)

    def add_recipe_list(self):
        recipe_list = QListWidget(parent = self.centralwidget)
        recipe_list.addItems(DM.listRecipes())
        recipe_list.setGeometry(350, 160, 150, 200)
        recipe_list.show()

    def add_my_recipe_form(self):
        recipe_form = QDialog(parent = self.centralwidget)
        recipe_form.setWindowTitle("Add Recipe Manually")

        form_layout = QFormLayout(parent = recipe_form)
        
        self.recipe_name_input = QLineEdit(parent = recipe_form)
        self.recipe_name_input.setPlaceholderText("Enter recipe title")
        
        self.serving_size_input = QLineEdit(parent = recipe_form)
        self.serving_size_input.setValidator(QIntValidator(1, 100))
        self.serving_size_input.setPlaceholderText("Enter number of servings")

        self.ingredients_input = QtWidgets.QTextEdit(parent = recipe_form)
        self.ingredients_input.setPlaceholderText("1 block of tofu, 2 limes, 3 tablespoons olive oil")

        form_layout.addRow("Title: ", self.recipe_name_input)
        form_layout.addRow("Servings: ", self.serving_size_input)
        form_layout.addRow("ingredients: ", self.ingredients_input)

        submit_button = QPushButton("Save Recipe")
        cancel_button = QPushButton("Cancel")

        button_layout = QHBoxLayout()
        button_layout.addWidget(submit_button)
        button_layout.addWidget(cancel_button)
        
        form_layout.addRow(button_layout)

        cancel_button.clicked.connect(recipe_form.close)
        #submit_button.clicked.connect(lambda: (DM.addRecipe([self.recipe_name_input.text(), self.serving_size_input.text(), json.dumps(self.ingredients_input.toPlainText().split(','))])), recipe_form.close)
        submit_button.clicked.connect(
    lambda: (
        DM.addRecipe([
            self.recipe_name_input.text(), 
            self.serving_size_input.text(), 
            json.dumps(self.ingredients_input.toPlainText().split(','))
        ]), 
        recipe_form.close()
    )
)
        
        recipe_form.exec()
        
    """def add_shopping_list(self)
        shopping_list = QListWidget(parent = self.centralwidget)
        shopping_dictionary = IL.
        recipe_list.addItems(DM.listRecipes())
        recipe_list.setGeometry(350, 160, 150, 200)
        recipe_list.show()
    """
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AddMyRecipeButton.setText(_translate("MainWindow", "Add Recipe Manually"))
        self.AddURLRecipeButton.setText(_translate("MainWindow", "Add Recipe with URL"))
        self.SeeRecipesButton.setText(_translate("MainWindow", "See Recipes"))
        self.ShoppingListButton.setText(_translate("MainWindow", "Shopping List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
