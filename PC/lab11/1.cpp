#include <stdio.h>
#include "mpi.h" 
int main(int argc, char *argv[])
{
	int rank;
	int size;
	int s = 0;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Reduce(&rank, &s, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
	printf("rank=%d s=%d \n", rank, s);
	MPI_Finalize();
	return 0;
}