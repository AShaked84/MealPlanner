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
    sys.exit(app.exec())
"""
import sys
from PyQt6.QtWidgets import (
    QApplication, QListWidget, QListWidgetItem, QWidget, 
    QHBoxLayout, QLabel, QPushButton, QMainWindow
)
from PyQt6.QtCore import Qt

class HoverAdjusterWidget(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.value = 0
        self.text_label = text
        
        # Main layout
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(5, 2, 5, 2)
        
        # Item text display
        self.label = QLabel(f"{self.text_label} ({self.value})", self)
        self.layout.addWidget(self.label)
        self.layout.addStretch()
        
        # Minus button
        self.minus_btn = QPushButton("-", self)
        self.minus_btn.setFixedSize(20, 20)
        self.minus_btn.clicked.connect(self.decrement)
        self.layout.addWidget(self.minus_btn)
        
        # Plus button
        self.plus_btn = QPushButton("+", self)
        self.plus_btn.setFixedSize(20, 20)
        self.plus_btn.clicked.connect(self.increment)
        self.layout.addWidget(self.plus_btn)
        
        # Hide buttons initially
        self.set_buttons_visible(False)
        
    def increment(self):
        self.value += 1
        self.update_text()
        
    def decrement(self):
        self.value -= 1
        self.update_text()
        
    def update_text(self):
        self.label.setText(f"{self.text_label} ({self.value})")

    def set_buttons_visible(self, visible):
        self.minus_btn.setVisible(visible)
        self.plus_btn.setVisible(visible)

    # Detect hover entry
    def enterEvent(self, event):
        self.set_buttons_visible(True)
        super().enterEvent(event)

    # Detect hover exit
    def leaveEvent(self, event):
        self.set_buttons_visible(False)
        super().leaveEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Hover Adjuster Example")
        self.resize(300, 400)
        
        # Initialize List Widget
        self.list_widget = QListWidget(self)
        self.setCentralWidget(self.list_widget)
        
        # Enable mouse tracking to capture hover properly
        self.list_widget.setMouseTracking(True)
        
        # Populate list
        items = ["Apples", "Bananas", "Oranges", "Pineapples"]
        for item_text in items:
            # 1. Create the base list item
            item = QListWidgetItem(self.list_widget)
            
            # 2. Create the custom widget with adjusters
            custom_widget = HoverAdjusterWidget(item_text)
            
            # 3. Set the size hint so the row accommodates the widget
            item.setSizeHint(custom_widget.sizeHint())
            
            # 4. Link them together
            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, custom_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())"""
