""" import sys
import os
import subprocess

MAYA_LOCATION = "C:/Program Files/Autodesk/Maya2022"
PYTHON_LOCATION = MAYA_LOCATION + "/Python/Lib/site-packages"

os.environ["MAYA_LOCATION"] = MAYA_LOCATION
os.environ["PYTHONPATH"] = PYTHON_LOCATION

sys.path.append(MAYA_LOCATION)
sys.path.append(PYTHON_LOCATION)
sys.path.append(MAYA_LOCATION+"/bin")
sys.path.append(MAYA_LOCATION+"/lib")
sys.path.append(MAYA_LOCATION+"/Python")
sys.path.append(MAYA_LOCATION+"/Python/DLLs")
sys.path.append(MAYA_LOCATION+"/Python/Lib")
sys.path.append(MAYA_LOCATION+"/Python/Lib/plat-win")
sys.path.append(MAYA_LOCATION+"/Python/Lib/lib-tk")
print('\n'.join(sys.path))


def test():
    import maya.cmds as cmds
    # full path to your Maya file to OPEN
    maya_file_to_open = r"Q:\__packages\_GitHub\Maya-Standalone-Exporter\test\test_anims_v01.ma"
    # Open your file
    cmds.file(maya_file_to_open, o=True)
    # full path to your Maya file to IMPORT
    maya_file_to_import = r"Q:\__packages\_GitHub\Maya-Standalone-Exporter\test\test_anims_v01.ma"
    # Import the file. the variable "nodes" will hold the names of all nodes imported, just in case.
    cmds.file(maya_file_to_import, i=True, type="mayaAscii")
    render = r"Q:\__packages\_GitHub\Maya-Standalone-Exporter\test\test_anims_v012.ma"
    cmds.file(rename=render)
    cmds.file(force=True, save=True, options='v=1;p=17', type='mayaBinary')
    print('a')






command = 'mayapy {}'.format( test )
proc = subprocess.Popen( command, shell=True, stdout=subprocess.PIPE )
proc.wait()
print( 'output:{}'.format(proc.returncode) ) """

""" string1 = '"white spaces"'
string = string1.replace( ' ', "' '" )

print( string1, string ) """

import subprocess
import os
import io
import time, os, sys
o, p = 10, 15

buffer = io.StringIO()
buffer.seek( 0, os.SEEK_END )
buffer_size = buffer.tell()
print( f"Buffer Size {buffer_size}" )
#import ctypes
#buffer = ctypes.create_string_buffer(1024)

#print( ctypes.addressof( buffer ) )

@subprocess.PIPE
class DataClass( ):
    def __init__(self) -> None:
        print(  )
        

classs = DataClass( 'cmd.exe' )


cmd = [ 'cmd.exe' ]

calc = subprocess.Popen(    cmd, 
                            stdin=subprocess.PIPE,
                            stdout=sys.stdout,
                            stderr=sys.stdout,
                            encoding='UTF-8',
                            universal_newlines=True)



#print( sys.stdout )

""" for line in iter( calc.stdout.readline, '' ):
    buffer.write( str(line) )
    if line in ['\n', '\r\n']:
        print( f'hit new line:{line}' )
        break """
    #print( ">>>{}".format( line.rstrip() ) )
    #print('hang')


#print( "Spawn Output {}: {}".format( 1, sys.stdout ) )
#calc.stdin.flush()

#print(buffer.getvalue())
print('hang')

calc.stdin.flush()
sys.stdout.flush
sys.stdin.write( 'python\n' )

#print( calc.stdout.read )
print(sys.stdout)
#calc.stdin.write( '{} + {}\n'.format( 10,15 ) )


#print(buffer.getvalue())



#print( "Spawn Output {}: {}".format( 2, sys.stdout ) )