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

"""
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Database/RecipeBook.db")  # Replace with your actual db filename


conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("CREATE TABLE Ingredients ( ID INT PRIMARY KEY, Recipe_ID INT, Amount FLOAT, Unit VARCHAR(50), Ingredient VARCHAR(100), FOREIGN KEY (Recipe_ID) REFERENCES Recipes(ID))")
conn.commit()
conn.close()"""

"""from PyQt6.QtCore import QMimeData, Qt, pyqtSignal
from PyQt6.QtGui import QDrag, QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


class DragTargetIndicator(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContentsMargins(25, 5, 25, 5)
        self.setStyleSheet(
            "QLabel { background-color: #ccc; border: 1px solid black; }"
        )


class DragItem(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setContentsMargins(25, 5, 25, 5)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("border: 1px solid black;")
        # Store data separately from display label, but use label for default.
        self.data = self.text()

    def set_data(self, data):
        self.data = data

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            pixmap = QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)

            drag.exec(Qt.DropAction.MoveAction)
            self.show() # Show this widget again, if it's dropped outside.


class DragWidget(QWidget):
    #Generic list sorting handler.

    orderChanged = pyqtSignal(list)

    def __init__(self, *args, orientation=Qt.Orientation.Vertical, **kwargs):
        super().__init__()
        self.setAcceptDrops(True)

        # Store the orientation for drag checks later.
        self.orientation = orientation

        if self.orientation == Qt.Orientation.Vertical:
            self.blayout = QVBoxLayout()
        else:
            self.blayout = QHBoxLayout()

        # Add the drag target indicator. This is invisible by default,
        # we show it and move it around while the drag is active.
        self._drag_target_indicator = DragTargetIndicator()
        self.blayout.addWidget(self._drag_target_indicator)
        self._drag_target_indicator.hide()

        self.setLayout(self.blayout)

    def dragEnterEvent(self, e):
        e.accept()

    def dragLeaveEvent(self, e):
        self._drag_target_indicator.hide()
        e.accept()

    def dragMoveEvent(self, e):
        # Find the correct location of the drop target, so we can move it there.
        index = self._find_drop_location(e)
        if index is not None:
            # Inserting moves the item if its alreaady in the layout.
            self.blayout.insertWidget(index, self._drag_target_indicator)
            # Hide the item being dragged.
            e.source().hide()
            # Show the target.
            self._drag_target_indicator.show()
        e.accept()

    def dropEvent(self, e):
        widget = e.source()
        # Use drop target location for destination, then remove it.
        self._drag_target_indicator.hide()
        index = self.blayout.indexOf(self._drag_target_indicator)
        if index is not None:
            self.blayout.insertWidget(index, widget)
            self.orderChanged.emit(self.get_item_data())
            widget.show()
            self.blayout.activate()
        e.accept()

    def _find_drop_location(self, e):
        pos = e.position()
        spacing = self.blayout.spacing() / 2

        for n in range(self.blayout.count()):
            # Get the widget at each index in turn.
            w = self.blayout.itemAt(n).widget()

            if self.orientation == Qt.Orientation.Vertical:
                # Drag drop vertically.
                drop_here = (
                    pos.y() >= w.y() - spacing
                    and pos.y() <= w.y() + w.size().height() + spacing
                )
            else:
                # Drag drop horizontally.
                drop_here = (
                    pos.x() >= w.x() - spacing
                    and pos.x() <= w.x() + w.size().width() + spacing
                )

            if drop_here:
                # Drop over this target.
                break

        return n

    def add_item(self, item):
        self.blayout.addWidget(item)

    def get_item_data(self):
        data = []
        for n in range(self.blayout.count()):
            # Get the widget at each index in turn.
            w = self.blayout.itemAt(n).widget()
            if w != self._drag_target_indicator:
                # The target indicator has no data.
                data.append(w.data)
        return data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.drag = DragWidget(orientation=Qt.Orientation.Vertical)
        for n, l in enumerate(["A", "B", "C", "D"]):
            item = DragItem(l)
            item.set_data(n)  # Store the data.
            self.drag.add_item(item)

        # Print out the changed order.
        self.drag.orderChanged.connect(print)

        container = QWidget()
        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.drag)
        layout.addStretch(1)
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication([])
w = MainWindow()
w.show()

app.exec()

class DragWidget(QWidget):
    
    #Generic list sorting handler.
    

    orderChanged = pyqtSignal(list)

    def __init__(self, *args, orientation=Qt.Orientation.Vertical, **kwargs):
        super().__init__()
        self.setAcceptDrops(True)

        # Store the orientation for drag checks later.
        self.orientation = orientation

        if self.orientation == Qt.Orientation.Vertical:
            self.blayout = QVBoxLayout()
        else:
            self.blayout = QHBoxLayout()

        # Add the drag target indicator. This is invisible by default,
        # we show it and move it around while the drag is active.
        self._drag_target_indicator = DragTargetIndicator()
        self.blayout.addWidget(self._drag_target_indicator)
        self._drag_target_indicator.hide()

        self.setLayout(self.blayout)

    def dragEnterEvent(self, e):
        e.accept()

    def dragLeaveEvent(self, e):
        self._drag_target_indicator.hide()
        e.accept()

    def dragMoveEvent(self, e):
        # Find the correct location of the drop target, so we can move it there.
        index = self._find_drop_location(e)
        if index is not None:
            # Inserting moves the item if its alreaady in the layout.
            self.blayout.insertWidget(index, self._drag_target_indicator)
            # Hide the item being dragged.
            e.source().hide()
            # Show the target.
            self._drag_target_indicator.show()
        e.accept()

    def dropEvent(self, e):
        widget = e.source()
        # Use drop target location for destination, then remove it.
        self._drag_target_indicator.hide()
        index = self.blayout.indexOf(self._drag_target_indicator)
        if index is not None:
            self.blayout.insertWidget(index, widget)
            self.orderChanged.emit(self.get_item_data())
            widget.show()
            self.blayout.activate()
        e.accept()

    def _find_drop_location(self, e):
        pos = e.position()
        spacing = self.blayout.spacing() / 2

        for n in range(self.blayout.count()):
            # Get the widget at each index in turn.
            w = self.blayout.itemAt(n).widget()

            if self.orientation == Qt.Orientation.Vertical:
                # Drag drop vertically.
                drop_here = (
                    pos.y() >= w.y() - spacing
                    and pos.y() <= w.y() + w.size().height() + spacing
                )
            else:
                # Drag drop horizontally.
                drop_here = (
                    pos.x() >= w.x() - spacing
                    and pos.x() <= w.x() + w.size().width() + spacing
                )

            if drop_here:
                # Drop over this target.
                break

        return n

    def add_item(self, item):
        self.blayout.addWidget(item)

    def get_item_data(self):
        data = []
        for n in range(self.blayout.count()):
            # Get the widget at each index in turn.
            w = self.blayout.itemAt(n).widget()
            if w != self._drag_target_indicator:
                # The target indicator has no data.
                data.append(w.data)
        return data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.drag = DragWidget(orientation=Qt.Orientation.Vertical)
        for n, l in enumerate(["A", "B", "C", "D"]):
            item = DragItem(l)
            item.set_data(n)  # Store the data.
            self.drag.add_item(item)

        # Print out the changed order.
        self.drag.orderChanged.connect(print)

        container = QWidget()
        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.drag)
        layout.addStretch(1)
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication([])
w = MainWindow()
w.show()

app.exec()"""



"""class DragButton(QPushButton):
    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            pixmap = QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)

            drag.exec(Qt.DropAction.MoveAction)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

        self.blayout = QHBoxLayout()
        for l in ["A", "B", "C", "D"]:
            btn = DragButton(l)
            self.blayout.addWidget(btn)

        self.setLayout(self.blayout)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.position()
        widget = e.source()
        self.blayout.removeWidget(widget)

        for n in range(self.blayout.count()):
            #get widget at each index in turn
            w  = self.blayout.itemAt(n).widget()
            if pos.x() < w.x() + w.size().width() // 2: #give some room for error
                #then we didnt drag past this widget.
                #insert to its left
                break

        else:
            #we're not to the left of any of the buttons
            #so we drop the button at the very end. add 1 to insert
            n += 1
        self.blayout.insertWidget(n, widget)
        e.accept()



app = QApplication([])
w = Window()
w.show()

app.exec()"""

"""import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QLabel, QWidget
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag

class CopyDragButton(QPushButton):
    #The source widget that remains unaffected.
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

    def mouseMoveEvent(self, event):
        # Only trigger drag on left-click move
        if event.buttons() != Qt.MouseButton.LeftButton:
            return

        # Package the data
        mime_data = QMimeData()
        mime_data.setText(self.text())

        # Create the drag object
        drag = QDrag(self)
        drag.setMimeData(mime_data)

        # CRITICAL: Tell Qt this is a COPY action, not a MOVE action
        # This prevents the source from modifying or hiding itself.
        drag.exec(Qt.DropAction.CopyAction)

class CopyDropLabel(QLabel):
    #The target widget that accepts and clones the data.
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("border: 2px dashed #aaa; background-color: #f0f0f0;")
        
        # Enable dropping on this widget
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        # Accept the event if it contains plain text
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        # Extract the cloned text data
        dropped_text = event.mimeData().text()
        self.setText(f"Copied: {dropped_text}")
        
        # Explicitly set the drop action feedback to Copy
        event.setDropAction(Qt.DropAction.CopyAction)
        event.accept()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Copy Drag and Drop")
        self.setMinimumSize(400, 200)

        # Main Layout
        layout = QHBoxLayout()

        # Add Source and Target
        self.source_button = CopyDragButton("Drag Me (Copy)")
        self.target_label = CopyDropLabel("Drop Content Here")

        layout.addWidget(self.source_button)
        layout.addWidget(self.target_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
"""

"""import sys
from PyQt6.QtWidgets import QLabel,QListWidgetItem, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QAbstractItemView
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets

class DragDropWindow(QWidget):
    def __init__(self):
        print("1")
        super().__init__()
        print("2")
        self.setWindowTitle("PyQt6 List to List Drag & Drop")
        self.resize(500, 300)
        print("3")

        # 1. Create a horizontal layout
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        print("4")

        # 2. Create Left List Widget
        self.left_list = QListWidget()
        left_items = ["Apple", "Banana", "Cherry", "Date"]
        for n, item_name in enumerate(left_items):
            item_widget = QtWidgets.QWidget()
            item_layout = QVBoxLayout(item_widget)

            title_layout = QHBoxLayout()
            title_layout.addWidget(QLabel(item_name))

            main_layout.addLayout(title_layout)
            details = QLabel(str(n))
            main_layout.addWidget(details)

            item = QListWidgetItem()

            self.left_list.addItem(item)
            self.left_list.setItemWidget(item, item_widget)
        
        # 3. Create Right List Widget
        self.right_list = QListWidget()
        self.right_list.addItems(["Elephant", "Fox", "Giraffe"])

        # 4. Enable Drag and Drop on both lists
        for list_widget in self.left_list:#, self.right_list):
            # Allows selecting multiple items if needed
            list_widget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
            
            # Enables both dragging items out and dropping items in
            list_widget.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
            
            # Sets the default action to MOVE (removes from source, adds to target)
            list_widget.setDefaultDropAction(Qt.DropAction.CopyAction)
            
            # Ensures the widget explicitly accepts the drop
            list_widget.setAcceptDrops(True)

        # 5. Add widgets to layout
        main_layout.addWidget(self.left_list)
        main_layout.addWidget(self.right_list)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    print("app")
    window = DragDropWindow()
    print("window")
    window.show()
    print("show")
    sys.exit(app.exec())
    print("exec")
"""
"""
import sys
import pickle
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QListWidget, QListWidgetItem
from PyQt6.QtCore import Qt, QMimeData, QByteArray
from PyQt6.QtGui import QDrag

# Define a custom MIME type identifier for your data
MIME_TYPE = "application/x-custom-item-data"

class MetadataListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)

    def startDrag(self, supportedActions):
        #Triggered when the user starts dragging an item.
        item = self.currentItem()
        if not item:
            return

        # 1. Extract the custom tagged data from the item
        custom_data = item.data(Qt.ItemDataRole.UserRole)
        
        # 2. Package both the text and the metadata into a dictionary
        payload = {
            "text": item.text(),
            "metadata": custom_data
        }

        # 3. Serialize the payload into bytes using pickle
        bytes_data = pickle.dumps(payload)
        byte_array = QByteArray(bytes_data)

        # 4. Create MIME data container
        mime_data = QMimeData()
        mime_data.setData(MIME_TYPE, byte_array)

        # 5. Execute the drag operation
        drag = QDrag(self)
        drag.setMimeData(mime_data)
        
        # If a move action completes successfully, delete the item from the source list
        drag.exec(Qt.DropAction.CopyAction)# == Qt.DropAction.CopyAction:
         #   self.takeItem(self.row(item))

    def dragEnterEvent(self, event):
        #Validates if the incoming dragged item matches our custom format.
        if event.mimeData().hasFormat(MIME_TYPE):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        #Keeps accepting the action while moving inside the widget boundaries.
        if event.mimeData().hasFormat(MIME_TYPE):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        Triggered when the item is released over this list.
        if event.mimeData().hasFormat(MIME_TYPE):
            # 1. Retrieve the byte stream from MIME container
            byte_array = event.mimeData().data(MIME_TYPE)
            bytes_data = byte_array.data()
            
            # 2. Deserialize back into a Python dictionary
            payload = pickle.loads(bytes_data)

            # 3. Create a brand new item in this list
            new_item = QListWidgetItem(payload["text"])
            # Re-apply the metadata to the new item
            new_item.setData(Qt.ItemDataRole.UserRole, payload["metadata"])
            
            self.addItem(new_item)
            event.acceptProposedAction()
        else:
            event.ignore()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Metadata Drag and Drop")
        self.resize(600, 300)

        layout = QHBoxLayout(self)

        # Create our custom lists
        self.left_list = MetadataListWidget()
        self.right_list = MetadataListWidget()
        self.center_list = QListWidget

        # Add items with hidden UserRole metadata (e.g., database IDs, complex dicts)
        items_to_add = [
            ("Apple", {"id": 101, "type": "fruit", "color": "red"}),
            ("Banana", {"id": 102, "type": "fruit", "color": "yellow"}),
            ("Carrot", {"id": 205, "type": "vegetable", "color": "orange"}),
        ]

        for text, metadata in items_to_add:
            item = QListWidgetItem(text)
            item.setData(Qt.ItemDataRole.UserRole, metadata)
            self.left_list.addItem(item)

        layout.addWidget(self.left_list)
        layout.addWidget(self.center_list)
        layout.addWidget(self.right_list)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
"""

import sys
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QListWidgetItem, QWidget, QHBoxLayout, QListWidget, QAbstractItemView
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets
import json
    
class DropList(QListWidget):
    """def dropEvent(self, event):
        super().dropEvent(event)

        item = self.itemAt(event.position().toPoint())

        if item:
            print(item.data(Qt.ItemDataRole.UserRole))"""
    def dropEvent(self, event):
        left_items = ["Apple", "Banana", "Cherry", "Date"]
        source = event.source()
        item = source.currentItem()

        if item:
            new_item = item.clone()
            item_widget = QtWidgets.QWidget()
            item_layout = QVBoxLayout(item_widget)

            db_id = new_item.data(Qt.ItemDataRole.UserRole)
            title = QLabel(left_items[db_id])
            details = QLabel(str(db_id))

            title_layout = QHBoxLayout()
            title_layout.addWidget(title)

            item_layout.addLayout(title_layout)
            item_layout.addWidget(details)

            final_item = QListWidgetItem()
            self.addItem(final_item)
            self.setItemWidget(final_item, item_widget)

            hint = item_widget.sizeHint()
            safe_height = max(hint.height(), 45)
            hint.setHeight(safe_height)

            final_item.setSizeHint(hint)
            #self.addItem(new_item)
            #print(new_item)#.data(Qt.ItemDataRole.UserRole))

        event.acceptProposedAction()

class DragDropWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 List to List Drag & Drop")
        self.resize(500, 300)

        # 1. Create a horizontal layout
        layout = QHBoxLayout()
        self.setLayout(layout)

        # 2. Create Left List Widget
        self.left_list = QListWidget()
        left_items = ["Apple", "Banana", "Cherry", "Date"]

        for n, item_name in enumerate(left_items):
            item = QListWidgetItem(str(item_name))
            item.setData(Qt.ItemDataRole.UserRole, n)
            self.left_list.addItem(item)
        
        # 3. Create Right List Widget
        self.right_list = DropList()
        #self.right_list.addItems(["Elephant", "Fox", "Giraffe"])

        # 4. Enable Drag and Drop on both lists
        #for list_widget in (self.left_list, self.right_list):
            # Allows selecting multiple items if needed
        #self.left_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
            
            # Enables both dragging items out and dropping items in
        #self.left_list.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
            
            # Sets the default action to MOVE (removes from source, adds to target)
        #self.left_list.setDefaultDropAction(Qt.DropAction.CopyAction)
            
            # Ensures the widget explicitly accepts the drop
        #self.left_list.setAcceptDrops(True)

        self.left_list.setDragEnabled(True)
        self.left_list.setAcceptDrops(False)
        self.left_list.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)

        self.right_list.setDragEnabled(False)
        self.right_list.setAcceptDrops(True)
        self.right_list.setDragDropMode(QAbstractItemView.DragDropMode.DropOnly)

        # 5. Add widgets to layout
        layout.addWidget(self.left_list)
        layout.addWidget(self.right_list)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DragDropWindow()
    window.show()
    sys.exit(app.exec())


"""import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QListWidget, QAbstractItemView
from PyQt6.QtCore import Qt

class DragDropWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 List to List Drag & Drop")
        self.resize(500, 300)

        # 1. Create a horizontal layout
        layout = QHBoxLayout()
        self.setLayout(layout)

        # 2. Create Left List Widget
        self.left_list = QListWidget()
        self.left_list.addItems(["Apple", "Banana", "Cherry", "Date"])
        
        # 3. Create Right List Widget
        self.right_list = QListWidget()
        self.right_list.addItems(["Elephant", "Fox", "Giraffe"])

        # 4. Enable Drag and Drop on both lists
        for list_widget in (self.left_list, self.right_list):
            # Allows selecting multiple items if needed
            list_widget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
            
            # Enables both dragging items out and dropping items in
            list_widget.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
            
            # Sets the default action to MOVE (removes from source, adds to target)
            list_widget.setDefaultDropAction(Qt.DropAction.MoveAction)
            
            # Ensures the widget explicitly accepts the drop
            list_widget.setAcceptDrops(True)

        # 5. Add widgets to layout
        layout.addWidget(self.left_list)
        layout.addWidget(self.right_list)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DragDropWindow()
    window.show()
    sys.exit(app.exec())
"""