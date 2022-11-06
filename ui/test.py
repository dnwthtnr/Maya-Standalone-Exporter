import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class Window(QFileDialog):
    def __init__(self):
        #QFileDialog.__init__(self, *args, **kwargs)

        super( Window, self ).__init__()

        """ self.button1 = QPushButton("Test 1", self)
        self.button2 = QPushButton("Test 2", self)
        self.button3 = QPushButton("Test 3", self) """

        """ self.layout = QHBoxLayout()
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3) """

        #self.setLayout(self.layout)
        self.show()

        """ self.button1.clicked.connect(self.on_button1)
        self.button2.clicked.connect(self.on_button2)
        self.button3.clicked.connect(self.on_button3)
 """


    def closeEvent(self, event):

        print('closed')

""" if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    sys.exit( app.exec( ) ) """

from io import StringIO
import os
s = StringIO()
s.write("abc")
s.seek(0, os.SEEK_END)
print(s.tell())