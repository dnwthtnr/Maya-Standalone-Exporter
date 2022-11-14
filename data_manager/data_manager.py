'''

Author: Tanner Dunworth

This tool is meant to allow user to access maya file(s) and export into unreal engine without having to seperately open up each file

Tool is intended to be independent from maya and unreal

'''

# ----------| LIB IMPORTS |---------- #

import os

import sys

import json

import ctypes

# ----------| LOCAL IMPORTS |---------- #

from data_manager.interface_json import InterfaceJSON

from data_manager.mayapy_delegate import SubprocessMayapy

from config.definitions import DATA_JSON
from config.definitions import ROOT_DIR


class DataManager( InterfaceJSON ):

    def __init__(self, verbosity = 1, json = DATA_JSON, overwrite=False, object_instance=True, rootdir='Desktop'):

        super( DataManager, self ).__init__(    json, overwrite, 
                                                object_instance, rootdir )

        self.verbosity = verbosity
        
        self.cache = self.json_reader( )     # start cache from 'json' - self.cache
        self.instance_array = []
        
        # mayapy 
        self.data = self.cache["data"]
        self.commands = self.cache["mayapy"]["commands"]
        
        maya_bin = 'C:\\Program_Files\\Autodesk\\Maya2022\\bin'
        self.mayapy_path = maya_bin + '\\mayapy.exe'

    # start mayapy - store instance
    def start_instance( self, instance_id = 0, path = None, open_file = None ):

        mayapy = SubprocessMayapy(  id = instance_id, 
                                    path = path )

        #key = 'mayapy_instance_{}'.format( instance_id )

        
        #instance_address = ctypes.addressof(id( mayapy )) # convert instance to ctypes data to be able to retrieve later on

        #instance_address = ctypes.pointer
        #value = ctypes.byref( ctypes.addressof(id(mayapy)) )

        # add instance to list

        #print( 'key:{}\nvalue:{}'.format( key,value ) )
        # add instance to cache
        self.instance_array.append(mayapy)

        """  # add instances and address to dict
        self.dict_add(  dict_location = self.data['instances']['mayapy'], 
                        key = instance_id, 
                        value = mayapy,
                        array = True ) """

        
        instance_info = {"address":mayapy, "return_data":{}}  # default dictionary to add

        # add instance 
        self.dict_add(
            dict_location=self.data["from_maya"]["instance"],
            key=instance_id,
            value=instance_info,
            array=False
        )
        # run startup codes
        self.dict_iterate(  dictionary = self.commands["startup_code"], 
                            range_bounds = [ 1,5 ],
                            call_function = mayapy.send_command )
                            
    # iterate over instances, sends given command -- add results to cache -- only given string of code name
    def instance_send_commands( self, command = str() ):
        
        command_dict = self.commands ["main_code"]

        
        for i, instance in enumerate ( self.instance_array ):    # for each instance
            
            command_info = command_dict [command]    # corresponding command from cache
            result = command_info ["command"]   # command that gets sent -- if formatting is needed it will override
            
            if command == "open_file":
                file = self.data ["paths"] [str(i)]    # given file path under key i
            
            if "format" in command_info:     # if given key = dict then needs formatting
                
                dict_command = command_dict [command] ["command"]
                dict_format = command_dict [command] ["format"]
                
                # need to format
                result = dict_command.format ( locals()[dict_format] )       # resulting command after format -- dict_format is = a locals() key

            
            if self.verbosity > 1:
                print ( 'instance_send_commands--locals:{}'.format( locals() ) )
            
            store_return = command_info["return"]    # dict value of if return value is stored
            
            returned = instance.send_command( command = result, return_output = store_return )

            if store_return == True:
                store_location = self.data["from_maya"]["instance"][str(i)]["return_data"]
                
                self.dict_add(
                    dict_location = store_location,
                    key = command,
                    value = returned,
                    iterate = False,
                    array = False
                    )

            if self.verbosity > 0:
                print ( 'instance-{}: recieved <{}>'.format( i, result ) )
        
        pass

    # take commands and format strings
    def get_command( self, command = [], formatted = False ):
        
        pass

    # call function with dict strings as input -- used to run set of mayapy commands in order
    def dict_iterate( self, dictionary, range_bounds, call_function ):

        range0 = int(range_bounds[ 0 ])
        range1 = int(range_bounds[ 1 ])

        print( range0, range1 )

        for i in range( range0, range1 ):
            
            dict_object = dictionary[ str( i ) ]

            call_function( dict_object )


    def identify_instances( self ):

        array = self.data['instances']['mayapy']
        id_list = []

        for index, _ in enumerate(array):

            class_object = self.instance_array[ index ]

            #class_object = ctypes.cast( class_address.strip('<>'), ctypes.py_object ).value
            #class_object = eval( class_address.strip('<>') )

            #print( 'class obj:{}\ntype:{}'.format( class_object, type( class_object ) ) )

            id = class_object.print_id()

            id_list.append( '{}:{}'.format(class_object, id) )

        return id_list


    def start_file_instances( self ):

        files = self.cache['data']['paths']
        
        for i, file in enumerate(files):

            self.start_instance(    instance_id = i,
                                    path = file )
        pass


    def class_evaluation( self, string_object ):

        return getattr( sys.modules[__name__], string_object )


    # TODO: take in file paths

    # TODO: query for different animations in scene(s)

    # TODO: use json cache as 'model' to organize data

    # TODO: take in users desired animations to export & desired save location || preferences in file type and fbx settings

    # TODO: take in unreal project to import into

    # TODO: take settings for desired import




    
    

if __name__ == "__main__":

    data_manager = DataManager(    
                        json=DATA_JSON, 
                        overwrite=False, 
                        object_instance=True, 
                        rootdir=ROOT_DIR )

    data_manager.start_instance( path = None )

    #print( json )