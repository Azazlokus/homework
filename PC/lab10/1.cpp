#include <stdio.h>
#include "iostream"
#include "mpi.h"
#include "windows.h"

using namespace std;

int main(int argc, char *argv[])
{
	int rank;
	int size;
	MPI_Status stat;
	MPI_Request req;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	int *b = new int[3];
	int *a = new int[3 * size];
	if (rank == 0){
		for (int i = 0; i < 3*size; i++)
		{
			a[i] = i;
		}
	}
	MPI_Scatter(&a[0], 3, MPI_INT, &b[0], 3, MPI_INT, 0, MPI_COMM_WORLD);
	Sleep(1000 * rank);
	printf("rank: %d [", rank);
	for (int i = 0; i < 3; i++)
	{
		printf(" %d ", b[i]);
	}
	printf("]\n");
	
	MPI_Finalize();

	return 0;
}
