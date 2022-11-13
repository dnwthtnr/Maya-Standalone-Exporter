'''
Author: Tanner Dunworth

This is meant to function as a dynamic UI that interfaces with the data_manager.py utilizing a json cache

'''

# ----------| LIB IMPORTS |---------- #

import os
import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QTabBar, QTabWidget, QToolBar, QMenuBar, QTextEdit
from PyQt6.QtWidgets import QVBoxLayout, QBoxLayout, QHBoxLayout
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# ----------| LOCAL IMPORTS |---------- #
from data_manager import data_manager

from ui.file_browser import main as file_dialog

from ui.output_window import OutputWindow

from config.definitions import DATA_JSON, ROOT_DIR

#DATA_MANAGER = data_manager.DataManager()
JSON_MANAGER = data_manager.DataManager(    json=DATA_JSON, overwrite=False, 
                                            object_instance=True, rootdir=ROOT_DIR )


class MainWindow( QWidget ):

    def __init__( self, **slots ):

        super(MainWindow, self).__init__()

        self.__build__( )
        self.__edit__( )
        self.__layout__( )
        self.__connect__( )
        self.__update__( )

    def __build__( self ):

        self.layout_main = QVBoxLayout( )

        self.tab_widget = QTabWidget( )     # tabs

        # debug tab
        self.tab_debug = QWidget( )              # tab has to be widget
        self.layout_tab_debug = QVBoxLayout( )   # layout for debug tab
        self.debug_output_box = OutputWindow( )

        # main tab
        self.tab_main = QWidget( )
        self.layout_tab_main = QHBoxLayout( )

        self.menu_bar = QMenuBar( )

        self.print_files = QAction( )
        
        
        self.button = QPushButton( )
        
        self.label_main = QLabel( )
        self.label_debug = QLabel( )

    def __edit__( self ):

        self.setWindowTitle( 'Maya Standalone Anim Exporter' )
        self.setGeometry(   100,100,
                            280,80  )

        self.main_tab = self.tab_widget.addTab(     self.tab_main, 
                                                    "Main"      )
        self.debug_tab = self.tab_widget.addTab(    self.tab_debug, 
                                                    "Debug"     )

        self.menu_file = self.menu_bar.addMenu( "&File" )
        self.menu_debug = self.menu_bar.addMenu( "&Debug" )
        
        
        self.print_files.setText( "&print_files" )
        self.menu_debug.addAction( self.print_files )
        
        self.button.setText( 'Browse' )

        self.label_main.setText( 'main' )
        self.label_debug.setText( 'debug' )

    def __layout__( self ):

        # add main tab widgets
        self.layout_tab_main.addWidget( self.button )
        self.layout_tab_main.addWidget( self.label_main )

        # add debug tab widgets
        self.layout_tab_debug.addWidget( self.label_debug )
        self.layout_tab_debug.addWidget( self.debug_output_box )
        
        # add widgets to main window layout
        self.layout_main.addWidget( self.menu_bar )

        self.layout_main.addWidget( self.tab_widget )

        # set layout for each tab
        self.tab_main.setLayout( self.layout_tab_main )
        self.tab_debug.setLayout( self.layout_tab_debug )

        # set layout for main window
        self.setLayout( self.layout_main )

    def __connect__( self ):

        slots = InterfaceSlots()

        self.print_files.triggered.connect( 
                    lambda: self.debug_output_box.write( 
                            slots.debug_output(
                                    print = "paths") ) )

        self.button.clicked.connect( slots.file_browser )

    # TODO: dynamic ui generation from json['ui']
    def __generate__( self ):
        # take in json
        #interface_data = JSON_MANAGER.json_reader( file = DATA_JSON )
        # algorithm to parse and identify variables using 'id'
        pass
    
    def __update__( self ):
        
        self.show( )

    def closeEvent( self, event ):

        print('closed')


class InterfaceSlots( ):

    def __init__( self ):

        pass

    def file_browser( self, verbosity, *args): # opens file dialogue returns list of selected files

        file_dialogue = file_dialog( )

        if verbosity > 0:
            print( 'file_dialogue:{}'.format(file_dialogue) )
            print( 'file_dialogue type:{}'.format(type(file_dialogue)) )
        

        if not isinstance( file_dialogue, type( None ) ):
            JSON_MANAGER.dict_add(  
                dict_location = JSON_MANAGER.cache['data']['paths'], 
                key = int,
                value = file_dialogue,
                iterate = True  )

        else:
            print( "No files selected" )

    def debug_output( self, print ):
        return JSON_MANAGER.cache['data'][print]

    #@pyqtSlot( )
    def method( ):

        pass

def main( ):

    app = QApplication( sys.argv )

    interface_slots = InterfaceSlots( )

    window = MainWindow( slots = interface_slots )

    window.show

    sys.exit( app.exec( ) )

if __name__ == "__main__":

    main( )