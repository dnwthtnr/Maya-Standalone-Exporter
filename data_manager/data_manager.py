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



class InterfaceJSON( json ):

    def __init__( self, json, overwrite = False ):

        self.schema = json
        
        if overwrite == False:
            self.file = 'data_write.json'

        else:
            self.file = json


        pass

    # TODO: get commands from json
    def json_reader( self ):

        with open( self.data ) as json_file:

            dict = self.load( json_file )

        return dict

    def json_write( self, dict_location, key, value ):

        # write self.json to disk
        with open( file, 'w' ) as json_file:
            json_file.write( self.json )

        

        

    def dict_add( self, dict_location, key, value ):

        if value is list():

            print('list')

        dict_location[ str( key ) ] = value
        pass

    def dict_pack( self, key, value ):

        dictionary = dict

        if key == int:

            iterations = value

        # if keys and values are same len then iterate together
        #if value>key then put multiple values under key
        #if key>value put same value under keys
        """ else:

            if len( key ) == len( value ):
                iterator = 
                iterations = key

            elif len( value ) > len( key ):
                value_per_key = value // key
                
                pass

            else:
                pass """

        for iter, item in enumerate(iterations):

            dictionary[ str( iter ) ] = item

        return dictionary



    # TODO: parse through given dict and return values and eval type ( var(), exec() )
    def json_unpack( self, dict ):
        pass
    
    

jsonInterface = InterfaceJSON( json=DATA_JSON )

json = jsonInterface.json_reader( file = DATA_JSON )

#print(json)

data_manager = DataManager( data=json )

data_manager.start_instance( path = None )

#print( json )