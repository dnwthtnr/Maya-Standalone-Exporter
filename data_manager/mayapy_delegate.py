# import thread to be able to delegate output management 

from threading import Thread


# import from subproccess to interface with mayapy

from wexpect import spawn

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




class SubprocessMayapy( ):

    def __init__( self, id = 0, path = '"C:\\Program Files\\Autodesk\Maya2022\\bin\mayapy.exe"' ):

        self.id = id
        
        # create instance of mayapy in new process when class instantiated
        self.instance = spawn( 'cmd.exe' )
        self.instance.expect( '>' )
        self.instance.sendline( path )
        self.instance.expect
    
    # TODO: create function to execute command on self.mayapy
    def send_command( self, command = [] ):

        print(  'instance-{}:{}'.format(self.id, command) )
        
        self.instance.sendline( command )

        self.instance.expect( '>' )

        output = self.instance.before

        return output
    
    # TODO: create command to terminate program
    def kill( self ):

        # exit mayapy
        self.instance.sendline( 'exit( )' )

        # exit cmd
        self.instance.sendline( 'exit' )

        self.instance.wait( )

    def print_id( self, *args):
        #print( 'instance_id:{}'.format( self.id ) )

        return self.id



if __name__ == "__main__":

    mayapy_path = '"C:\\Program Files\\Autodesk\Maya2022\\bin\mayapy.exe"'
    instance = spawn( 'cmd.exe' )
    instance.expect( '>' )
    first = instance.before
    instance.sendline( mayapy_path )
    instance.expect( '>' )
    second = instance.before
    print( first, second )