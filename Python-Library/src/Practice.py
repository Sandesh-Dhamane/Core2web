import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel,QPushButton,QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class Practice(QWidget):
    # HEllo Core2web
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")

        self.setGeometry(500,300,500,300)

        self.mainLayout = QVBoxLayout(self)

        self.setLayout(self.mainLayout)

        self.LabelUI()

    def LabelUI(self):
        self.label = QLabel ("Hello Core2web")

        self.mainLayout.addWidget(self.label,0,Qt.AlignmentFlag.AlignCenter)

    #Text Change
    #def __init__(self):
    #    super().__init__()
    def textchange(self):
        self.setWindowTitle("Main Window")
        self.setGeometry(500,300,500,300)
        self.mainLayout=QVBoxLayout(self)
        self.mainLayout.setSpacing(0)
        self.setLayout(self.mainLayout)

        self.label1=QLabel ("Hello Core2web")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label1.setFixedSize(500,30)
        self.mainLayout.addWidget(self.label1,alignment = Qt.AlignmentFlag.AlignCenter)
        self.addButton()

    def addButton(self):
        self.Button1 = QPushButton("Text Change")
        self.Button1.setFixedSize(100,30)
        self.Button1.clicked.connect(lambda:self.label1.setText("Hello Core2web"if self.label1.text()=="I am Here" else "I am Here"))
        self.mainLayout.addWidget(self.Button1,alignment=Qt.AlignmentFlag.AlignCenter)

    #Color changer
    # def __init__(self):
        #super().__init__()
        #self.init_ui()

    def init_ui(self):
    # Create a QVBoxLayout
        layout = QVBoxLayout()
        # Create a QComboBox and add colors to it
        color_combo = QComboBox(self)
        colors = ["Red", "Green", "Blue", "Yellow", "Cyan", "Magenta"]
        color_combo.addItems(colors)
        # Connect the color change signal to the slot
        color_combo.currentIndexChanged.connect(self.change_color)
        # Add the QComboBox to the layout
        layout.addWidget(color_combo)
        # Set the layout for the main window
        self.setLayout(layout)
        # Set the initial background color explicitly
        self.change_color(0)
        # Set the window properties
        self.setGeometry(500, 300, 500, 400)
        self.setWindowTitle('Color Changer App')

    def change_color(self, index):
        # Get the selected color from the QComboBox
        color_name = self.sender().currentText() if self.sender() else "Red"
        # Get the QColor object based on the color name

        color = QColor(color_name)
        # Set the background color of the window
        self.setStyleSheet(f"background-color: {color.name()};")


if __name__=="__main__":
    app = QApplication(sys.argv)
    Practice = Practice()
    Practice.show()
    sys.exit(app.exec_())