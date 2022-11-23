import subprocess
import sys
import os
import wexpect
import pexpect

#proc = wexpect.host.SpawnPipe( '"C:\\Program Files\\Autodesk\\Maya2022\\bin\\mayapy.exe"' )
""" proc = wexpect.host.SpawnPipe( 'C:\Windows\system32\cmd.exe', ['python'], env="Q:\__packages\__python\python_3.7.7\python" )
print('ah')
proc.expect( '>>>' )
print( proc.before )

print('ho')
proc.sendline( 'python' )
proc.expect( '>>>' )
print( proc.before ) """

""" proc.expect('>>>')
print(proc.before)

proc.sendline( "import maya.standalone" )
proc.expect('>>>')
print(proc.before) """

""" from pexpect.popen_spawn import PopenSpawn

p = PopenSpawn( 'cmd.exe', encoding='utf8' )
p.expect_exact( '\r\n\r\n' )
print(p.before)

p.send( 'python' )
p.expect_exact( '\n\r\n\r>>>' )
print( p.before)

p.sendline( "C:\\Program Files\\Autodesk\\Maya2022\\bin\\mayapy.exe" )
p.expect( '>>> ' )
print( p.before ) """






""" result = subprocess.Popen( 
    ["C:\\Program Files\\Autodesk\\Maya2022\\bin\\mayapy.exe"], 
    stdin = subprocess.PIPE, 
    stdout = subprocess.PIPE, 
    stderr = subprocess.PIPE, 
    encoding='UTF8', 
    universal_newlines=True )

out, err = result.communicate( "import maya.standalone" )

print('Out: {}\nErr: {}'.format(out, err) )

#time.sleep(.5)

out, err = result.communicate( "maya.standalone.initialize( name = 'python' )" )

print('Out: {}\nErr: {}'.format(out, err) )

out, err = result.communicate( "import maya.cmds as cmds" )

print('Out: {}\nErr: {}'.format(out, err) )

out, err = result.communicate( "cmds.file('Q:\__packages\_GitHub\Maya-Standalone-Exporter\test\test_anims_v01.ma'open=True)" )

print('Out: {}\nErr: {}'.format(out, err) ) """


""" from subprocess import PIPE, Popen

p = Popen(["python", "-u", "1st.py"], stdin=PIPE, stdout=PIPE, bufsize=1)

print(p.stdout.readline()), # read the first line

for i in range(10): # repeat several times to show that it works
    print (p.stdin, i) # write input
    p.stdin.flush() # not necessary in this case
    print(p.stdout.readline()) # read output

print(p.communicate(b"n\n")[0]) """


""" import os

read, write = os.pipe()

if not os.fork():
    # child

    os.close( read )        # close read pipe

    wdup = 1
    os.dup2( write, wdup )      # wdup == &write """


""" import subprocess

wr_out = open( "temp_out", "wb" )
re_out = open( "temp_out", "r" )

wr_err = open( "temp_err", "w" )
re_err = open( "temp_err", "rb" )

proc = subprocess.Popen( 
    'cmd',
    stdin = subprocess.PIPE,
    stdout=wr_out,
    stderr=wr_err,
    encoding='UTF8',
    bufsize=-1
 )

proc.stdin.write( 'pythonn\n' )
out = re_out.tell()
err = re_err.tell()

print( re_out.read(), err )
 """


import sys
import os
import subprocess
from subprocess import Popen, PIPE
import threading


""" class LocalShell(object):
    def __init__(self):
        pass

    def run(self):
        env = os.environ.copy()
        self.p = Popen(
                    'cmd.exe', 
                    stdin=PIPE, 
                    stdout=PIPE, 
                    stderr=subprocess.STDOUT, 
                    shell=True, 
                    env=env,
                    text=True)
        
        sys.stdout.write("Started Local Terminal...\r\n\r\n")

    def read(self):

        def writeall(p):
            while True:
                #print("read data: ")
                data = p.stdout.read(1)     # output

                if not data:        # if no data : break
                    break

                sys.stdout.write(data)      # console print
                sys.stdout.flush()

        writer = threading.Thread(target=writeall, args=[self.p,] )
        writer.start()

        try:
            while True:
                d = sys.stdin.read(1)
                if not d:
                    break
                self._write(self.p, d.encode())

        except EOFError:
            pass


    
    def _write(self,message):
        self.p.stdin.write(message)
        self.p.stdin.flush()


shell = LocalShell()
shell.run()
shell.read()
shell._write( 'python\n' )
shell.read() """

import time

class LocalShell(object):
    
    def __init__(self):

        self.start()

    
    def start( self ):
        print( 'LocalShell.start()\n' )
        env = os.environ.copy()

        command = ['cmd.exe']
        
        self.p = Popen(
                    command, 
                    stdin=PIPE, 
                    stdout=PIPE, 
                    stderr=subprocess.STDOUT,
                    env=env,
                    text=True)

        print( '\tsuccess' )        # console print

    
    def read(self):
        print( 'LocalShell.read()\n' )

        def threaded_read(p):
            print( '\tLocalShell.read().threaded_read()\n' )
            while True:
                #print("read data: ")
                data = p.stdout.readline()     # output

                if data == '\n':        # if no data : break
                    
                    print( 'hit new line' )
                    break

                print('data:{}'.format(data))

        self.writer = threading.Thread(target=threaded_read, args=[self.p,] )     # thread to take data from stdout
        self.writer.start()

        """ try:
            while True:
                
                d = sys.stdin.read(1)

                if not d:
                    break
                self.write(self.p, d.encode())

        except EOFError:
            pass """


    
    def write(self,message):
        print( f'\nLocalShell.write({message})\n' )
        self.writer.join()

        self.p.stdin.write(message)
        self.p.stdin.flush()

shell = LocalShell(  )      # starts instance of the shell
shell.read()
time.sleep(.01)
shell.write( 'python' )
shell.read()




""" shell = LocalShell()
shell.read()
shell._write( 'python\n' )
shell.read() """


""" w = open('not', 'wb')
r = open('not', 'r')

w.write(b'nononono')
r.read()

print( r.read() ) """


#shell.write( shell, 'python' )








""" def start(executable_file):
    return subprocess.Popen(
        executable_file,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)


def read(process):
    return process.stdout.readline().decode("utf-8").strip()


def write(process, message):
    process.stdin.write(f"{message.strip()}\n".encode("utf-8"))
    process.stdin.flush()


def terminate(process):
    process.stdin.close()
    process.terminate()
    process.wait(timeout=0.2)


process = start("C:\\Program Files\\Autodesk\\Maya2022\\bin\\mayapy.exe")
write(process, "import maya.standalone")
print(read(process))
print(read(process))

terminate(process)
 """