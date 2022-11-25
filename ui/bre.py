import os
import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QTabBar, QTabWidget, QToolBar, QMenuBar, QTextEdit
from PyQt5.QtWidgets import QVBoxLayout, QBoxLayout, QHBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer

class JuicyAss(QWidget):

	def __init__(self):
		super(JuicyAss, self).__init__()
		self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
		self.ass()
		self.show()

	def ass( self ):
		VIDEO = 'Q:\\media\\booty.mp4'
		assHolder = QVBoxLayout(self)

		font = QFont('comic sans')
		font.setBold(True)
		font.setItalic(True)

		

		vid = QVideoWidget()

		t = QLabel('Hey there Breanna')
		a = QLabel('I heard you got that fat ass booty')
		s = QLabel('Im 1000 miles away but girl tonight that thing looks juicy')
		d = QLabel('YES IT DO!')
		h = QLabel("no one\'s got a badonkadonk like you")
		o = QLabel('I swears its true')

		

		hand = [t,a,s,d,h,o]

		for ass in hand:
			ass.setFont(font)
			ass.setStyleSheet("background-color: lightblue")
			assHolder.addWidget(ass)

		#aaa.addLayout(assHolder)
		assHolder.addWidget(vid)

		self.mediaPlayer.setVideoOutput(vid)

		self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(VIDEO)))

		self.mediaPlayer.play()
		
		
		self.setLayout(assHolder)

		

def main( ):

    app = QApplication( sys.argv )

    window = JuicyAss( )

    window.show

    sys.exit( app.exec( ) )

if __name__ == "__main__":

    main( )






