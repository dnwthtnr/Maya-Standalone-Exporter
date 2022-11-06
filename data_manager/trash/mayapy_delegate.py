'''

Author: Tanner Dunworth

This tool is meant to allow user to access maya file(s) and export into unreal engine without having to seperately open up each file

Tool is intended to be independent from maya and unreal

'''


# ----------| IMPORTS |---------- #

# pymel needed for mayapy

#from pymel.core.system import openFile

# import config to interface with .env file

#from decouple import config

from asyncio import subprocess
from dotenv import load_dotenv


import os


# json for data storage and communication with UI

import json


# import thread to be able to delegate output management 

from threading import Thread


# import from subproccess to interface with mayapy

import pexpect



class SubprocessMayapy( ):

    def __init__( self, path = r"C:\Program Files\Autodesk\Maya2022\bin" ):

        mayapy_path = r"C:\Program Files\Autodesk\Maya2022\bin\mayapy.exe"

        # create instance of mayapy in new process when class instantiated
        self.instance = Popen( mayapy_path,
                                stdin=PIPE, stdout=PIPE, 
                                stderr=STDOUT, encoding="UTF8", bufsize=1 )

        

        self.input = self.instance.stdin
        self.output = self.instance.stdout
        print( 'instance has started' )
        print( 'instance: %s\ninstance_type: %s' % ( self.instance, type( self.instance ) ) )

    #
    
    # TODO: create function to execute command on self.mayapy
    def send_command( self, command ):

        print('command send start')
        
        # give input to instance
        #self.input.write( "import maya.standalone" )

        print('command send 2 start')

        #print( 'commandLine: %s' % (commandLine) )
        
        self.input.flush( )

        print('command send 2.5 start')

        # create thread to buffer output
        output_thread = Thread( target = self.read_output, args = (self.instance, ) )

        print( 'ok' )

        output_thread.start( )

        output_thread.join( )


        """ # any returns
        output = self.output.readline( )

        print('command send 3 start')

        print( 'send_command input: %s\nsend_command output : %s' % ( command, output ) )

       # return output """

    # threaded process to manage output data
    def read_output( self, instance ):
        
        print( "Output: %s" % ( self.output.readline( ) ) )
        
    
    # TODO: create command to terminate program
    def kill( self ):

        #self.instance.stdin.close( )

        self.instance.terminate( )

        try:
            output = self.instance.wait( timeout = 0.2 )

            print( 'instance terminated with returncode: %s' % ( self.instance.returncode ) )

        except TimeoutExpired:

            print( 'instance did not termiante in time' )
            
            return output


func = SubprocessMayapy( )

print( "command 1 sent" )

func.send_command(command = "import maya.standalone")

print( "command sent" )

func.send_command(command = 'maya.standalone.initialize( name = "python" )') 

func.send_command(command = "import maya.cmds as cmds")

func.send_command( command = "cmds.file( %s, open = True )" % ( 'Q:\__packages\__tools\maya_to_engine\test\test_anims_v01.ma' ) )

func.send_command( command = "cmds.ls( objectsOnly = True, assemblies = True, dag = True, exactType = [ 'camera', 'transform', 'joint' ])" )

func.kill( )