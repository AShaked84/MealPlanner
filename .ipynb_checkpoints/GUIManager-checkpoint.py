from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QLineEdit, QListWidget

import DatabaseManager as DM


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
        self.ChangeMealPlanButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.ChangeMealPlanButton.setObjectName("ChangeMealPlanButton")
        self.horizontalLayout.addWidget(self.ChangeMealPlanButton)
        self.AddRecipeButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.AddRecipeButton.setObjectName("AddRecipeButton")
        self.horizontalLayout.addWidget(self.AddRecipeButton)
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

        self.AddRecipeButton.clicked.connect(self.add_recipe_lineEdit)
        #self.SeeRecipesButton.clicked.connect(DM.listRecipes)
        self.SeeRecipesButton.clicked.connect(self.add_recipe_list)

    def add_recipe_lineEdit(self):
        self.recipe_input_field = QLineEdit(parent = self.centralwidget)
        add_new_recipe = QtWidgets.QPushButton(parent = self.centralwidget)
        self.recipe_input_field.setGeometry(40, 100, 200, 40)
        add_new_recipe.setGeometry(250, 100, 40, 40)
        self.recipe_input_field.show()
        add_new_recipe.show()
        add_new_recipe.clicked.connect(lambda checked: DM.addRecipe(self.recipe_input_field.text()))

    def add_recipe_list(self):
        recipe_list = QListWidget(parent = self.centralwidget)
        recipe_list.addItems(DM.listRecipes())
        recipe_list.setGeometry(460, 40, 150, 200)
        recipe_list.show()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ChangeMealPlanButton.setText(_translate("MainWindow", "Change Meal Plan"))
        self.AddRecipeButton.setText(_translate("MainWindow", "Add Recipe"))
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
