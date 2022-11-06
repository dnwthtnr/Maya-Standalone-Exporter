import sys
import time
from threading import Thread

from subprocess import PIPE

from subprocess import Popen

from subprocess import STDOUT

import pexpect

from queue import Queue



class AsynchronousOutputHandler( Thread ):

    def __init__( self, out_pipe, queue ):

        assert isinstance(queue, Queue )
        assert callable(out_pipe.readline)
        Thread.__init__( self )

        self.output = out_pipe
        self.queue = queue

    def run(self):

        for line in iter( self.output.readline, '' ):

            self.queue.put( line )

    def eof( self ):

        return not self.is_alive( ) and self._queue.empty( )



cmd = r"C:\Program Files\Autodesk\Maya2022\bin\mayapy.exe"

process = Popen( cmd, stdout=PIPE, stdin=PIPE, stderr=PIPE )

output_queue = Queue( )
output_reader = AsynchronousOutputHandler( process.stdout, output_queue )
output_reader.start()

error_queue = Queue( )
error_reader = AsynchronousOutputHandler( process.stderr, error_queue )
error_reader.start()


while not output_reader.eof( ) or not error_reader.eof( ):

    while not output_queue.empty( ):
        line = output_queue.get( )
        print( 'Recieved output line: %s' % ( line ) )

    while not error_queue.empty( ):
        line = error_queue.get( )
        print( 'Recieved error line: %s' % ( line ) )


    time.sleep( .1 )

output_reader.join( )
error_reader.join( )