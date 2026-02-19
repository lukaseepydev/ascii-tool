from ascii_tool.logging_config import setup_logging
import logging
from ascii_tool.converter import convert
import sys
import argparse

setup_logging()

logger = logging.getLogger(__name__)

logger.info("Programm started!")


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, 
    QIntValidator)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget, QFileDialog, QLabel)

#UI class genrated from layout.ui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.filePickButton = QPushButton(self.centralwidget)
        self.filePickButton.setObjectName(u"filePickButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filePickButton.sizePolicy().hasHeightForWidth())
        self.filePickButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.filePickButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.width = QLineEdit(self.centralwidget)
        self.width.setObjectName(u"width")
        sizePolicy.setHeightForWidth(self.width.sizePolicy().hasHeightForWidth())
        self.width.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.width)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.textBox = QPlainTextEdit(self.centralwidget)
        self.textBox.setObjectName(u"textBox")
        self.textBox.setReadOnly(True)

        self.verticalLayout.addWidget(self.textBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AsciiTool", None))
        self.filePickButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Width:", None))
        self.width.setText(QCoreApplication.translate("MainWindow", u"120", None))
  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        font = QFont("Courier New")   # or "Consolas"
        font.setStyleHint(QFont.Monospace)

        self.ui.textBox.setFont(font)

        self.ui.width.setValidator(QIntValidator(1, 99999))

        self.ui.filePickButton.clicked.connect(self.select_file)
        self.ui.pushButton.clicked.connect(self.clicked_convert)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Pick File",
            "",
            "Images (*.png *.jpg *.jpeg)"
        )

        self.ui.lineEdit.setText(file_path)

    def clicked_convert(self):
        ascii_art = convert(self.ui.lineEdit.text(), int(self.ui.width.text()))
        self.ui.textBox.setPlainText(ascii_art)

def main():
    parser = argparse.ArgumentParser(description="AsciiImg tool")
    parser.add_argument("image", nargs="?", help="Path to image to convert")
    parser.add_argument(
        "-width", 
        type=int, 
        default=120, 
        help="Width of the ASCII output (default: 80)"
    )
    args = parser.parse_args()

    if not args.image:
        # Launch GUI
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    else:
        # Run CLI mode
        ascii_art = convert(args.image, args.width)
        print(ascii_art)

if __name__ == "__main__":
    main()