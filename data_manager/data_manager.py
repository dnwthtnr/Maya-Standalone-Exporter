'''

Author: Tanner Dunworth

This tool is meant to allow user to access maya file(s) and export into unreal engine without having to seperately open up each file

Tool is intended to be independent from maya and unreal

'''

# ----------| LIB IMPORTS |---------- #

import os

import sys

import json

# ----------| LOCAL IMPORTS |---------- #

from data_manager.mayapy_delegate import SubprocessMayapy

from config.definitions import DATA_JSON
from config.definitions import ROOT_DIR


class DataManager(  ):

    def __init__( self, data ):

        self.data = data["data"]
        self.commands = data["mayapy"]["commands"]

        maya_bin = 'C:\\Program_Files\\Autodesk\\Maya2022\\bin'

        self.mayapy = maya_bin + '\\mayapy.exe'

    # start mayapy - store instance
    def start_instance( self, path ):

        self.mayapy = SubprocessMayapy( )

        self.dict_iterate(  dictionary = self.commands["startup_code"], 
                            range_bounds = [ 1,5 ],
                            call_function = self.mayapy.send_command )

    # call function with dict strings as input -- used to run set of mayapy commands in order
    def dict_iterate( self, dictionary, range_bounds, call_function ):

        range0 = int(range_bounds[ 0 ])
        range1 = int(range_bounds[ 1 ])

        print( range0, range1 )

        for i in range( range0, range1 ):
            
            dict_object = dictionary[ str( i ) ]

            call_function( dict_object )

    def 

    # TODO: take in file paths

    # TODO: query for different animations in scene(s)

    # TODO: use json cache as 'model' to organize data

    # TODO: take in users desired animations to export & desired save location || preferences in file type and fbx settings

    # TODO: take in unreal project to import into

    # TODO: take settings for desired import




    
    

jsonInterface = DataManager( json=DATA_JSON, overwrite=False )

json = jsonInterface.json_reader( file = DATA_JSON )

#print(json)

data_manager = DataManager( data=json )

data_manager.start_instance( path = None )

#print( json )