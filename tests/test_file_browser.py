from genericpath import exists
import os

import sys

from PyQt6.QtTest import QSignalSpy
from PyQt6.QtWidgets import QApplication
ROOT_DIR = os.path.realpath( os.path.join( os.path.dirname( __file__ ), '..' ) )

sys.path.append( ROOT_DIR )

from ui import file_browser

import unittest



class TestFileBrowser( unittest.TestCase ):

    def test_events( self ):

        app = QApplication( sys.argv )
        window = file_browser.FileBrowser( )
        window.show()

        events = [ window.showEvent, window.inputMethodEvent, window.moveEvent, window.keyPressEvent ]
        

        while window.exec( ):

            for event in events:
            
                QSignalSpy( obj=window, signal=event )

        sys.exit( app.exec( ) )



        pass

if __name__ == '__main__':

    unittest.main( )