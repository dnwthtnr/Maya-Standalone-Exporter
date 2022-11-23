#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

int main(int argc, char* argv[])
{
    int p1[2]; //c to p
    int p2[2];// p to c
    if ( pipe(p1) == -1 ){return 1;}    //error check
    if ( pipe(p2) == -1 ){return 1;}    //error check
    int pid = fork();
    if( pid == -1 ){return 2;}      // error check
    if (pid == 0){
        close(p1[0]);
        close(p2(1));
        // child process pid == 0
        int x;
        if (read(p2[0], &x, sizeof(x)) == -1) { return 3; };    // read input from process 0 the value at the address of x
        printf( 'Recieved %d\n', x );
        x *= 4;
        if (write( p1[1], &x, sizeof(x) ) == -1) {return 4;}  // write from the address of x to proccess 0
        printf( 'Wrote %d\n', x );
        close(p1[1]);
        close(p2[0]);
    } else{
        close(p1[1]);
        close(p2[0]);
        // parent process
        srand( time( NULL ) );
        int y = rand() % 10;    // generate number
        if (write( p1[1], &y, sizeof(y) ) == -1) { return 5; }  // send it
        printf( "Wrote %d\n", y );
        if (read( p2[0], &y, sizeof(y) ) == -1 ) { return 6; }  // read result
        printf( "result: %d\n", y );
        close(p1[1]);
        close(p2[0]);
    }
    
    return 0;
}
