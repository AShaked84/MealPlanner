import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from GUIManager import Ui_MainWindow
"""
app = QApplication(sys.argv)

MainWindow = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.initialize_app()

MainWindow.show()

sys.exit(app.exec())"""

"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class DropDownImageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drop-Down Image List")
        self.setGeometry(100, 100, 400, 500)

        # Main layout
        layout = QVBoxLayout()
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Create Tree Widget to act as our list
        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)  # Hide the header so it looks like a list
        self.tree.setIndentation(10)     # Optional: control how much the image shifts right
        layout.addWidget(self.tree)

        # Add items to the list
        self.add_image_item("Click to see Python Logo", "python_logo.png")
        self.add_image_item("Click to see Another Image", "another_image.png")

        # Connect the click signal to toggle expansion
        self.tree.itemClicked.connect(self.toggle_item)

    def add_image_item(self, text, image_path):
        # 1. Create the parent item (The list text)
        parent = QTreeWidgetItem(self.tree)
        parent.setText(0, text)

        # 2. Create the child item that will hold the image
        child = QTreeWidgetItem(parent)
        
        # 3. Create a QLabel to display the image
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        
        # Optional: Scale the image to fit nicely
        scaled_pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 4. Inject the QLabel into the child tree item
        self.tree.setItemWidget(child, 0, image_label)

        # Start with the item collapsed
        parent.setExpanded(False)

    def toggle_item(self, item, column):
        # Toggle expansion when the parent item is clicked
        if item.childCount() > 0:
            item.setExpanded(not item.isExpanded())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DropDownImageWindow()
    window.show()
    sys.exit(app.exec())"""

import IngredientManager as IM
data = IM.recipe_scraper("https://www.budgetbytes.com/classic-three-bean-salad/").image()
print(data)