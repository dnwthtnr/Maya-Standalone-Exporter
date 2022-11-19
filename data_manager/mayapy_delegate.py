# import thread to be able to delegate output management 

from threading import Thread


# import from subproccess to interface with mayapy

#from wexpect import spawn
import wexpect

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

import subprocess
import multiprocessing


import os




# wexpect
class SubprocessMayapy( ):

    def __init__( self, verbosity = 0, id = 0, path = "C:\\Program' 'Files\\Autodesk\\Maya2022\\bin\\mayapy.exe" ):

        self.verbosity = verbosity
        
        self.id = id
        
        self.shell_startup( path )

        #print( 'maya start: {}'.format( mayapy_start ) )
        #self.instance.sendline( path )
        #self.instance.expect
    
    def send_command_batch( self, commands = [] ):
        pass

    def command_configure( self ):
        pass
    
    # TODO: create function to execute command on self.mayapy
    def send_command( self, command = [], return_output = False, expect = '>>>' ):

        #print(  'instance-{}:{}'.format(self.id, command) )

        output = None
        
        self.instance.write( command )

        self.instance.write( expect )

        output = self.instance.getConsoleOut()

        if self.verbosity > 0:

            print( '>instance-{}\n  command:{}\n    output:{}\n\n'.format( self.id, command, output ) )
        
        if return_output == True:
            return output
        else:
            return type(None)
    
    # TODO: create command to terminate program
    def kill( self ):

        # exit mayapy
        self.instance.sendline( 'exit( )' )

        # exit cmd
        self.instance.sendline( 'exit' )

        self.instance.wait( )

    def shell_startup( self, path = None ):
        
        # start shell
        self.instance = wexpect.console_reader.ConsoleReaderSocket( path, host_pid = os.getppid() )
        print('appended')
        #self.instance.expect( '>>>' )
        
        # start python env
        #output = self.send_command( command = 'python', return_output=True, expect = '>' )

        # open application instance
        #if path != None:
            
        #    path_output = self.send_command( command = path, return_output=True )

        #if self.verbosity > 0:
         #   print( 'python_output: {}\npath_output: {}'.format( output,path_output ) ) 

    def print_id( self, *args):
        #print( 'instance_id:{}'.format( self.id ) )

        return self.id


def main():
    instance = SubprocessMayapy( verbosity=1, id=0 )

    a = instance.send_command( command = "'import maya.standalone'", return_output=True)
    b = instance.send_command( command = "'maya.standalone.initialize( name = python )'", return_output=True)
    c = instance.send_command( command = "'import maya.cmds as cmds'", return_output=True)
    d = instance.send_command( command = "'import maya.mel as mel'", return_output=True )
    
    #print( 'a:{}\nb:{}\nc:{}\nd:{}\n'.format( a,b,c,d ) )
    
    first = instance.send_command( 
        command = "'cmds.file( {}, open = True )'".format( "Q:/__packages/_GitHub/Maya-Standalone-Exporter/test/test_anims_v01.mb"),
        return_output=True )
    second = instance.send_command( 
        command = f"'obj = cmds.ls( objectsOnly = True, assemblies = True, dag = True, exactType = [ {'camera'}, {'transform'}, {'joint'} ])'",
        return_output=True )
    third = instance.send_command( 
        command = "'print(obj)'",
        return_output=True )
    print(2)


if __name__ == "__main__":

    


    process = multiprocessing.Process( target=main() )
    process.start()

    print(1)
    
