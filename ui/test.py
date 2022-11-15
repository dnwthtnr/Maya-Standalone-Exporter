import sys
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
print( 'output:{}'.format(proc.returncode) )