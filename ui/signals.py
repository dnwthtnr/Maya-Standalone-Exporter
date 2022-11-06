import os

import sys

from PyQt6.QtCore import pyqtSlot


from file_browser import main as open_file_browser



class InterfaceSignals( ):

    def __init__( self ):

        pass

    
    @pyqtSlot( )
    def file_browse( self ):

        open_file_browser( )

