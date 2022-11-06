'''

Author: Tanner Dunworth

This tool is meant to allow user to access maya file(s) and export into unreal engine without having to seperately open up each file

Tool is intended to be independent from maya and unreal

'''


# ----------| IMPORTS |---------- #

# pymel needed for mayapy

#from pymel.core.system import openFile

# import config to interface with .env file


# import SubprocessMayapy to interface with mayapy

from mayapy_delegate import SubprocessMayapy


#from dotenv import load_dotenv

import os

import sys

ROOT_DIR = os.path.realpath( os.path.join( os.path.dirname( __file__ ), '..' ) )

sys.path.append( ROOT_DIR )


# json for data storage and communication with UI

from config.definitions import DATA_JSON

import json


class DataManager( ):

    def __init__( self, data ):

        self.data = data["data"]
        self.commands = data["mayapy"]["commands"]

        maya_bin = 'C:\\Program_Files\\Autodesk\\Maya2022\\bin'

        self.mayapy = maya_bin + '\\mayapy.exe'

    # start mayapy 
    def start_instance( self, path ):

        self.mayapy = SubprocessMayapy( )

        self.dict_iterate(  dictionary = self.commands["startup_code"], 
                            range_bounds = [ 1,5 ],
                            call_function = self.mayapy.send_command )

    # mayapy startup
    def dict_iterate( self, dictionary, range_bounds, call_function ):

        range0 = int(range_bounds[ 0 ])
        range1 = int(range_bounds[ 1 ])

        print( range0, range1 )

        for i in range( range0, range1 ):
            
            dict_object = dictionary[ str( i ) ]

            call_function( dict_object )

    # TODO: take in file paths

    # TODO: query for different animations in scene(s)

    # TODO: use json cache as 'model' to organize data

    # TODO: take in users desired animations to export & desired save location || preferences in file type and fbx settings

    # TODO: take in unreal project to import into

    # TODO: take settings for desired import



class InterfaceJSON( ):

    def __init__( self ):

        pass

    # TODO: get commands from json
    def json_reader( self, file ):

        with open( file ) as json_file:

            dict = json.load( json_file )

        return dict
    
    

jsonInterface = InterfaceJSON( )

json = jsonInterface.json_reader( file = DATA_JSON )

#print(json)

data_manager = DataManager( data=json )

data_manager.start_instance( path = None )

#print( json )