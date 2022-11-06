'''
Author: Tanner Dunworth

This is meant to function as a dynamic UI that interfaces with the data_manager.py utilizing a json cache

'''

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from PyQt6.QtWidgets import QFileDialog, QWidget, QApplication, QMainWindow, QVBoxLayout, QMdiSubWindow


import sys

class FileBrowser( QFileDialog ):

    def __init__( self, dialogue_type = int() ):

        super( FileBrowser, self ).__init__()

        #self.window = MainWindow( )

        #self.openFiles = QFileDialog( self, 'open files', 'Quick access' )

        self.setWindowTitle( 'file opens' )
        
        self.setFileMode( self.FileMode.ExistingFiles )

        #self.file_dialogue = QFileDialog.getOpenFileNames( self, 'Open Export Files', 'Quick access' )
    
    def closeEvent(self, a0: QCloseEvent) -> None:
        print('FileBrowser_closeEvent')


    


def main( ):

    
    window = FileBrowser()
    window.show()

    files = None

    if window.exec( ):

        files = window.selectedFiles( )

        window.closeEvent( QCloseEvent )

        #print( files )

    if files != None:
        return files
    else:
        return None
    

    

    

if __name__ == "__main__":

    app = QApplication( sys.argv )
    instance = main( )
    sys.exit( app.exec( ) )
    