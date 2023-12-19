import sys
from TextFile import textFile
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QListWidget,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QAction,
    QMenu
)

# Subclass QMainWindow to customize your application's main window


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()
        self.label.setText("Press this button to create a new file:")
        self.fileList = QListWidget()

        self.createFileButton = QPushButton()
        self.createFileButton.clicked.connect(self.addNewFile)
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.createFileButton)
        container = QWidget()
        container.setLayout(self.layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())

    def addNewFile(self):
        print("adding a new file")
        self.fileNameGetter = QLineEdit()
        self.fileNameGetter.returnPressed.connect(self.deleteNewFileLineEdit)
        self.newFileName = ""
        self.layout.addWidget(self.fileNameGetter)

    def deleteNewFileLineEdit(self):
        print(self.fileNameGetter.text())
        self.fileNameGetter.setParent(None)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
