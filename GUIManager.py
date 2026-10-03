from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QSpinBox, QLineEdit, QListWidget, QInputDialog, QFormLayout, QDialog, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit, QListWidgetItem, QLabel
from PyQt6.QtGui import QIntValidator, QTextCharFormat
from PyQt6.QtCore import QDate, Qt, QPoint
import json
from qt_material import apply_stylesheet, list_themes

import DatabaseManager as DM
import IngredientManager as IM
import MealManager as MM


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)

        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(29, 40, 600, 80))
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
        self.calendarWidget.setGeometry(QtCore.QRect(50, 160, 300, 220))
        self.calendarWidget.setObjectName("calendarWidget")

        self.menuWidget = QtWidgets.QWidget(parent = self.centralwidget)
        self.menuWidget.setGeometry(QtCore.QRect(370, 100, 400, 450))
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

        self.changeMealPlanButton = QtWidgets.QPushButton(parent=self.menuWidget)
        self.changeMealPlanButton.setObjectName("changeMealPlanButton")
        self.changeMealPlanButton.setText("Change Meal Plan")

        self.removeDishButton = QtWidgets.QPushButton(parent=self.menuWidget)
        self.removeDishButton.setObjectName("removeDishButton")
        self.removeDishButton.setText("Remove Dish")

        self.menuLayout.addLayout(self.breakfastLayout)
        self.menuLayout.addLayout(self.lunchLayout)
        self.menuLayout.addLayout(self.dinnerLayout)
        self.menuLayout.addLayout(self.snacksLayout)
        self.menuLayout.addWidget(self.changeMealPlanButton)
        self.menuLayout.addWidget(self.removeDishButton)
        self.changeMealPlanButton.hide()
        self.removeDishButton.hide()
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        
        self.menuSettings = QtWidgets.QMenu(parent=self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        
        self.menuColorScheme = QtWidgets.QMenu(parent=self.menuSettings)
        self.menuColorScheme.setObjectName("menuColorScheme")

        self.menuDinerSettings = QtGui.QAction("Diner Settings", self.menuSettings)

        self.themeGroup = QtGui.QActionGroup(self.menuColorScheme)
        self.themeGroup.setExclusive(True)
        themes = [
                    "Amber", "Blue", "Cyan", "Light Green", "Pink", "Purple",
                    "Red", "Teal", "Yellow"]

        self.menuSettings.addAction(self.menuDinerSettings)
        self.menuSettings.addAction(self.menuColorScheme.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.menuDinerSettings.triggered.connect(self.diner_settings_dialog)

        self.darkModeAction = QtGui.QAction("Dark Mode", self.menuSettings)
        self.darkModeAction.setCheckable(True)

        self.dark_mode = False
        self.current_theme = "amber"

        self.menuSettings.addAction(self.darkModeAction)
        self.darkModeAction.toggled.connect(self.toggle_dark_mode)

        self.connect_signals(themes)

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.centralwidget.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.centralwidget.setFocus()

        self.default_servings = 2
        self.AddURLRecipeButton.clicked.connect(self.add_recipe_URL_lineEdit)
        self.AddMyRecipeButton.clicked.connect(self.add_my_recipe_form)
        self.SeeRecipesButton.clicked.connect(self.show_recipe_list)
        self.ShoppingListButton.clicked.connect(self.show_shopping_list)
        self.changeMealPlanButton.clicked.connect(self.fill_meal)
        self.removeDishButton.clicked.connect(self.remove_meal)

        self.calendarWidget.clicked.connect(self.date_clicked)

        self.breakfastList.itemClicked.connect(self.recipe_selected)
        self.lunchList.itemClicked.connect(self.recipe_selected)
        self.dinnerList.itemClicked.connect(self.recipe_selected)
        self.snacksList.itemClicked.connect(self.recipe_selected)

    def connect_signals(self, themes):
        for theme in themes:
            action = QtGui.QAction(theme, parent=self.menuColorScheme)
            action.setCheckable(True)
            self.themeGroup.addAction(action)
            self.menuColorScheme.addAction(action)
            action.triggered.connect(lambda checked, t=theme: self.change_theme(t))

   #launches a dialog that defines default diner settings, to be changed as needed day to day
    def diner_settings_dialog(self):
        dialog = QDialog(parent=self.centralwidget)
        dialog.setWindowTitle("Diner Settings")

        settings_layout = QFormLayout(parent=dialog)

        diner_number = QSpinBox()
        diner_number.setRange(0, 99)
        diner_number.setValue(2)

        settings_layout.addRow("Default number of diners:", diner_number)
        save_button = QPushButton("Save Settings")
        save_button.clicked.connect(dialog.accept)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(dialog.reject)
        #settings_layout.addRow(save_button)
        settings_layout.addRow(save_button, cancel_button)

        dialog.setLayout(settings_layout)

        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            self.default_servings = diner_number.value()
            print(self.default_servings)

   #opens a dialog that has user choose a start and end date
    def toggle_dark_mode(self, checked):
        self.dark_mode = checked
        self.apply_theme()

    #changes the window theme based on user choice
    def change_theme(self, theme):
        self.current_theme = theme.lower().replace(" ", "")
        self.apply_theme()

    def apply_theme(self):
        mode = "dark" if self.dark_mode else "light"
        theme = f"{mode}_{self.current_theme}.xml"

        apply_stylesheet(QtWidgets.QApplication.instance(), theme=theme)
   #shopping list is then generated for the recipes to be prepared for chosen dates
    def show_shopping_list(self):
        shopping_list_dialog = QDialog(parent = self.centralwidget)
        shopping_list_dialog.setWindowTitle('Shopping List')

        start_date = None
        end_date = None
        dates = [start_date, end_date, True]

        window_layout = QVBoxLayout(shopping_list_dialog)
        shopping_list = QListWidget()
        label_layout = QHBoxLayout()
        date_chooser_calendar = QtWidgets.QCalendarWidget(parent=shopping_list_dialog)
        start_label = QLabel("Start: ")
        end_label = QLabel("End: ")
        date_chooser_calendar.clicked.connect(lambda date: self.date_chooser(date, dates, start_label, end_label))

        label_layout.addWidget(start_label)
        label_layout.addWidget(end_label)

        window_layout.addWidget(date_chooser_calendar)
        window_layout.addLayout(label_layout)

        generate_button = QPushButton("Generate Grocery List")
        window_layout.addWidget(generate_button)
        window_layout.addWidget(shopping_list)

        def generate_list():
            if dates[0] is None or dates[1] is None:
                start_label.setText("Please select both dates first")
                return
            shopping_list.clear()

            dates_list = [date.toString("yyyy-MM-dd") for date in dates[:-1]]
            meal_counts = MM.mealCounter(dates_list)
            grocery_list = IM.grocery_lister(meal_counts)

            for ingredient, amount in grocery_list.items():
                shopping_list.addItem(f"{amount.magnitude} {amount.units} {ingredient}")

        generate_button.clicked.connect(generate_list)

        shopping_list_dialog.exec()

    #function that allows user to choose two dates from a calendar widget
    #First date chosen is the start date, second is the end date
    #if the end date chosen is before the start date, they switch
    #labels display chosen dates
    def date_chooser(self, date:QDate, dates, start_label, end_label):
        if dates[2]:
            dates[0] = date
            dates[2] = False

        else:
            dates[1] = date
            dates[2] = True

        if dates[0] is not None and dates[1] is not None:
            if dates[1] < dates[0]:
                dates[0], dates[1] = dates[1], dates[0]
            
        if dates[0] is not None:
            start_label.setText(f"Start: {dates[0].toString('yyyy-MM-dd')}")
        if dates[1] is not None:
            end_label.setText(f"End: {dates[1].toString('yyyy-MM-dd')}")

    #function opens a dialog with a list populated with all the user's saved recipes      
    def show_recipe_list(self):
        recipe_list_dialog = QDialog(parent = self.centralwidget)
        recipe_list_dialog.setWindowTitle('Recipe Book')

        window_layout = QVBoxLayout(recipe_list_dialog)
        recipe_list = QListWidget()
        remove_recipe_button = QPushButton("Remove Recipe")
        window_layout.addWidget(recipe_list)
        window_layout.addWidget(remove_recipe_button)
        remove_recipe_button.clicked.connect(lambda: self.remove_recipe(recipe_list))
        remove_recipe_button.hide()

        self.populate_recipe_list(recipe_list)

        #recipe_list.itemClicked.connect(lambda item: (setattr(self, "selected_recipe", item),
         #                                             remove_recipe_button.show()))
        recipe_list.itemClicked.connect(lambda item: (setattr(self, "selected_recipe", item),
                                                      self.handle_recipe_list_click(item, remove_recipe_button)))

        recipe_list_dialog.exec()

    #handles clicking a recipe in the show recipes button
    def handle_recipe_list_click(self, item, remove_recipe_button):#, recipe_list):
        remove_recipe_button.show()
        #rect = recipe_list.visualItemRect(item)
        #global_pos = recipe_list.mapToGlobal(QPoint(rect.right(), rect.top))

    #when recipe is clicked, a remove dish button is shown
    #called for the menus
    def recipe_selected(self, item):
        for meal_list in [
            self.breakfastList,
            self.lunchList,
            self.dinnerList,
            self.snacksList
        ]:
            if meal_list is not item.listWidget():
                meal_list.clearSelection()

        self.removeDishButton.show()

        self.selected_dish = item
        meal_list = MainWindow.sender()
        item_widget = meal_list.itemWidget(item)

        details = item_widget.layout().itemAt(1).widget()
        details.setVisible(not details.isVisible())
        item.setSizeHint(item_widget.sizeHint())

    #when recipe is clicked, a remove recipe button is shown that allows users to delete chosen recipe from Recipes database
    #def recipe_book_selected(self, item):
     #   self.selected_recipe = item

    #removes clicked meal from the menu and refreshes menus
    #used on the daily menus
    def remove_meal(self):
        db_id = self.selected_dish.data(Qt.ItemDataRole.UserRole)
        DM.removeMeal(db_id)
        self.date_clicked(self.selected_date)

    #removes clicked recie from the recipe list and refreshes list
    #used on the recipe list 
    def remove_recipe(self, recipe_list):
        db_id = self.selected_recipe.data(Qt.ItemDataRole.UserRole)
        DM.removeRecipe(db_id)
        recipe_list.clear()
        self.populate_recipe_list(recipe_list)

    #fills in the menus with the recipes saved for each meal
    #refreshes the menus after update
    def refresh_menus(self, date_string):
        self.breakfastList.clear()
        self.lunchList.clear()
        self.dinnerList.clear()
        self.snacksList.clear()

        rows = DM.todaysMeals(date_string)
        #row[0] - id row[1] - date row[2] - meal type row[3] recipe_id row[4] - servings
        
        """for row in rows:
            meal_list = getattr(self, row[2].lower() + "List") 
            item = QListWidgetItem(DM.idRecipe(row[3]))
            item.setData(Qt.ItemDataRole.UserRole, row[0])
            meal_list.addItem(item)"""

        for row in rows:
            meal_list = getattr(self, row[2].lower() + "List") #which menu to add item to?
            item_widget = QtWidgets.QWidget()
            layout = QVBoxLayout(item_widget)

            title = QLabel(DM.idRecipe(row[3]))
            details = QLabel("add info here")

            plus_button = QPushButton("+")
            plus_button.setFixedSize(25,25)
            plus_button.setStyleSheet("padding: 0px; margin: 0px;")
            
            minus_button = QPushButton("-")
            minus_button.setFixedSize(25,25)
            minus_button.setStyleSheet("padding: 0px; margin: 0px;")

            serving_label = QLabel(str(row[4]))
            serving_label.setFixedSize(15,25)

            title_layout = QHBoxLayout()
            title_layout.addWidget(title)
            title_layout.addWidget(minus_button)
            title_layout.addWidget(serving_label)
            title_layout.addWidget(plus_button)

            layout.addLayout(title_layout)
            layout.addWidget(details)

            details.hide()

            item = QListWidgetItem()

            item.setData(Qt.ItemDataRole.UserRole, row[3]) #db_id
            item.setData(Qt.ItemDataRole.UserRole + 1, self.default_servings) #servings
            item.setData(Qt.ItemDataRole.UserRole + 2, row[0]) #meal_id

            meal_list.addItem(item)
            meal_list.setItemWidget(item, item_widget)

            hint = item_widget.sizeHint()
            safe_height = max(hint.height(), 45)
            hint.setHeight(safe_height)

            item.setSizeHint(hint)

            plus_button.clicked.connect(lambda _, current_item = item, current_label = serving_label: self.change_serving(current_item, current_label, 1))
            minus_button.clicked.connect(lambda _, current_item = item, current_label = serving_label: self.change_serving(current_item, current_label, -1))

            #meal_list.itemClicked.connect(lambda item: self.expand_item(meal_list, item))
    """
    def expand_item(self, item):
        item_widget = self.sender()
        details = item_widget.layout().itemAt(1).widget()
        details.setVisible(not details.isVisible())
        item.sizeHint(item_widget.setSizeHint())"""

    #add a serving to a menu item
    def change_serving(self, item, label, delta):

        meal_id = int(item.data(Qt.ItemDataRole.UserRole + 2))
        servings = DM.get_servings(meal_id)[0][0]

        DM.change_servings(meal_id, delta)

        servings += delta
        item.setData(Qt.ItemDataRole.UserRole + 1, servings)
        label.setText(str(servings))


    #when date is clicked on recipe widget, change meal plan button appears
    #if meal plan is changed, the menus are refreshed
    def date_clicked(self, date:QDate):
        self.selected_date = date
        self.changeMealPlanButton.show()
        date_string = date.toString("yyyy-MM-dd")

        self.refresh_menus(date_string)
        
    #dialog window that allows user to choose a meal to fill in and with what dish        
    def fill_meal(self):#, date: QDate):
        date_string = self.selected_date.toString("yyyy-MM-dd")
        date_dialog = QDialog(parent = self.centralwidget)
        date_dialog.setWindowTitle(f'{date_string} Meal Plan')

        meal_type_list = ["Breakfast", "Lunch", "Dinner", "Snacks"]

        window_layout = QVBoxLayout()
        lists_layout = QHBoxLayout()
        meal_type_layout = QVBoxLayout()
        recipe_list_layout = QVBoxLayout()

        meal_list = QListWidget()
        #meal_list.setStyleSheet("""QListWidget::item:hover { background-color: lightblue;}""")
        meal_type_layout.addWidget(meal_list)
        meal_list.addItems(meal_type_list)

        recipe_list = QListWidget()

        self.populate_recipe_list(recipe_list)

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

                self.date_clicked(self.selected_date)

   #gets all the recipes titles from the Recipes database table, tags them with their ID number
   #fills the recipe_list list widget with the recipe titles
    def populate_recipe_list(self, recipe_list):
        recipe_list_dictionary = DM.listRecipes()
        
        for db_id, title in recipe_list_dictionary.items():
            item = QListWidgetItem(str(title))
            item.setData(Qt.ItemDataRole.UserRole, db_id)
            recipe_list.addItem(item)

    #returns the invisible tag for a tagged item 
    # used when the item's tag should be saved rather than what's visible to the user
    # called by the fill meal function
    def handle_selection(self, item):
        selected_key = item.data(Qt.ItemDataRole.UserRole)
        return selected_key

    def initialize_app(self):
        self.meal_plan = DM.getMealPlan()

#opens dialog box with a space to add a URL
#URL is then sent to the scraper that fills in the recipe
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

#opens a dialog box that allows users to manually enter their own recipes
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuColorScheme.setTitle(_translate("MainWindow", "Color Scheme"))

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AddMyRecipeButton.setText(_translate("MainWindow", "Add Recipe Manually"))
        self.AddURLRecipeButton.setText(_translate("MainWindow", "Add Recipe with URL"))
        self.SeeRecipesButton.setText(_translate("MainWindow", "See Recipes"))
        self.ShoppingListButton.setText(_translate("MainWindow", "Shopping List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme = 'light_amber.xml')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
