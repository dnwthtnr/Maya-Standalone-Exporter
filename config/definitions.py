from imp import reload
import os
import sys


ROOT_DIR = os.path.realpath( os.path.join( os.path.dirname( __file__ ), '..' ) )

sys.path.insert( 1, ROOT_DIR )

MAYAPY_COMMANDS_JSON = ROOT_DIR + '\cache\mayapy_commands.json'

DATA_JSON = ROOT_DIR + '\cache\data.json'