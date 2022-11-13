from io import StringIO
import sys
import os

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from PyQt6.QtWidgets import QFileDialog, QWidget, QApplication, QMainWindow, QVBoxLayout, QMdiSubWindow




class OutputWindow( QTextEdit ):

    def __init__( self ):
        
        super( OutputWindow, self ).__init__( )

        self.setReadOnly( True )

        #self.autoFormatting(AutoFormattingFlag)

        self.buffer = StringIO()


    def write( self, output ):
        cursor = self.textCursor( )
        anchor = self.anchorAt

        self.buffer.seek( 0, os.SEEK_END )
        buffer_size = self.buffer.tell()
        print(buffer_size)
        
        if buffer_size == 0:
            message = ( '> {}'.format( output ) )

        else:
            message = ( '\n> {}'.format( output ) )

        
        self.insertPlainText( message )

        

        self.buffer.write( str(output) )
        
        pass





def main( ):

    instance = OutputWindow()
    instance.show()

    return instance

if __name__ == "__main__":

    app = QApplication( sys.argv )
    instance = main( )
    sys.exit( app.exec( ) )
    