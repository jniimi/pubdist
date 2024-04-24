import sys
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
import sip

class MainWindow(qtw.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setGeometry(300, 50, 400, 350)
        self.setWindowTitle('Instant Share')

        base_x = 50
        box_width  = 300
        box_height = 200

        self.title = qtw.QLabel('Instant Sharer', self)
        self.title.setAlignment(qtc.Qt.AlignCenter)
        self.title.resize(box_width, 20)
        self.title.move(base_x, 10)

        drag_y = 40
        self.label = qtw.QLabel('Drag & Drop Here', self)
        self.label.setAlignment(qtc.Qt.AlignCenter)
        self.label.setStyleSheet("color: black; background-color: lightgrey;")
        self.label.resize(box_width, box_height)
        self.label.move(base_x, drag_y)

        filepath_x = base_x
        filepath_y = drag_y + box_height + 30
        self.filepath_text = qtw.QTextEdit('File Path:',self)
        self.filepath_text.setStyleSheet("background-color: transparent;")
        self.filepath_text.move(filepath_x,filepath_y-20)

        self.filepath = qtw.QLineEdit(self)
        self.filepath.move(filepath_x+4,filepath_y)
        self.filepath.resize(box_width,20)

        button_x = base_x
        button_y = filepath_y+30
        button_width = 160
        self.button = qtw.QPushButton('Upload', self)
        self.button.resize(button_width,40)
        self.button.move(button_x, button_y)

        checkbox_x = button_x + button_width + 5
        checkbox_y = button_y
        self.needShorten = qtw.QCheckBox('Shorten the URL', self)
        self.needShorten.move(checkbox_x, checkbox_y)

        self.needPublic = qtw.QCheckBox('Make it Full Public', self)
        self.needPublic.move(checkbox_x, checkbox_y+20)

        #self.button.clicked.connect(self.output)
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())