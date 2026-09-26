from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QLineEdit, QListWidget, QInputDialog, QFormLayout, QDialog, QPushButton, QHBoxLayout, QTextEdit
from PyQt6.QtGui import QIntValidator

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
        submit_button.clicked.connect(lambda: (print(self.recipe_name_input.text(), self.serving_size_input.text(), self.ingredients_input.toPlainText()), recipe_form.close()))
        
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
