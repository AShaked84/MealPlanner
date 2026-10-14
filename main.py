"""import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QMenu, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Right Click Item Example")
        self.resize(400, 300)

        # 1. Initialize the item view widget
        self.list_widget = QListWidget(self)
        self.list_widget.addItems(["Apple", "Banana", "Cherry", "Date"])
        self.setCentralWidget(self.list_widget)

        # 2. Enable custom context menus on the widget
        self.list_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        
        # 3. Connect the context menu signal to your handler function
        self.list_widget.customContextMenuRequested.connect(self.show_item_context_menu)

    def show_item_context_menu(self, position):
        # 4. Find the specific item at the right-click position
        clicked_item = self.list_widget.itemAt(position)
        
        # Guard clause: ensure the user actually clicked on an item, not empty space
        if clicked_item is None:
            return

        # 5. Build and populate the context menu
        menu = QMenu(self)
        edit_action = menu.addAction(f"Edit '{clicked_item.text()}'")
        delete_action = menu.addAction(f"Delete '{clicked_item.text()}'")

        # 6. Map the local widget position to screen/global coordinates
        global_position = self.list_widget.viewport().mapToGlobal(position)
        
        # 7. Execute the menu and capture which action was selected
        selected_action = menu.exec(global_position)

        # 8. Handle the action logic
        if selected_action == edit_action:
            QMessageBox.information(self, "Edit", f"Editing: {clicked_item.text()}")
        elif selected_action == delete_action:
            # Safely remove the item from the list
            row = self.list_widget.row(clicked_item)
            self.list_widget.takeItem(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())"""

from PyQt6.QtWidgets import QApplication

from pyqt_search_bar import SearchBar



if __name__ == "__main__":

    import sys



    app = QApplication(sys.argv)

    searchBar = SearchBar()

    searchBar.setPlaceHolder('Input the text...')

    searchBar.show()

    app.exec_()