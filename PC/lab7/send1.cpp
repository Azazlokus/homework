#include <stdio.h>
#include "iostream"
#include "mpi.h"
#include "windows.h"

using namespace std;

int main(int argc, char *argv[])
{
int rank;
int size;
int a=0;
MPI_Status stat;
MPI_Request req;
MPI_Init(&argc, &argv);
MPI_Comm_rank(MPI_COMM_WORLD, &rank);
MPI_Comm_size(MPI_COMM_WORLD, &size);
double t1,t2,t3;

if(rank==0)
{
a=5;
t1=MPI_Wtime();
Sleep(1000);
    MPI_Send(&a, 1, MPI_INT, 1, 777, MPI_COMM_WORLD);
t2=MPI_Wtime();

printf( "rank = %d t2-t1=%g a=%d \n", rank,t2-t1,a); 
}

if(rank==1)
{
t1=MPI_Wtime();
    MPI_Irecv(&a, 1, MPI_INT, 0, 777, MPI_COMM_WORLD,&req);
t2=MPI_Wtime();

printf( "rank = %d t2-t1=%g a=%d \n", rank,t2-t1,a); 

}

MPI_Finalize();

return 0;
}

