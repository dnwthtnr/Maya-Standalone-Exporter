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

from config.definitions import DATA_JSON

#DATA_MANAGER = data_manager.DataManager()
JSON_MANAGER = data_manager.InterfaceJSON( file = DATA_JSON )


class MainWindow( QWidget ):

    def __init__( self, **slots ):

        super(MainWindow, self).__init__()
        
        self.slots = InterfaceSlots()

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

        self.someaction = QAction( )
        
        
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
        self.someaction.setText( "&someaction" )
        self.menu_debug.addAction( self.someaction )
        
        self.button.setText( 'Browse' )

        self.label_main.setText( 'main' )
        self.label_debug.setText( 'debug' )

    def __layout__( self ):

        

        self.layout_tab_main.addWidget( self.button )
        self.layout_tab_main.addWidget( self.label_main )

        self.layout_tab_debug.addWidget( self.label_debug )
        self.layout_tab_debug.addWidget( self.debug_output_box )
        
        self.layout_main.addWidget( self.menu_bar )

        self.layout_main.addWidget( self.tab_widget )

        self.tab_main.setLayout( self.layout_tab_main )
        self.tab_debug.setLayout( self.layout_tab_debug )


        self.setLayout( self.layout_main )

    def __connect__( self ):

        self.someaction.triggered.connect( lambda: self.debug_output_box.write( 'someaction' ) )

        self.button.clicked.connect( self.slots.file_browser )

    # TODO: dynamic ui generation from json['ui']
    def __generate__( self ):
        # take in json
        interface_data = JSON_MANAGER.json_reader( file = DATA_JSON )
        # algorithm to parse and identify variables using 'id'
        pass
    
    def __update__( self ):
        
        self.show( )

    def closeEvent( self, event ):

        print('closed')


class InterfaceSlots( ):

    def __init__( self ):

        pass

    def file_browser( self, *args): # opens file dialogue returns list of selected files

        file_dialogue = file_dialog( )

        JSON_MANAGER.dict_add(  dict_location = JSON_MANAGER.json['data']['paths'], 
                                key = int,
                                value = file_dialogue )

        print( file_dialogue )

    def debug_output( self ):

        pass

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