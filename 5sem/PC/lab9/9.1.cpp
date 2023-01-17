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
	int *s = new int[3 * size];
	for (int i = 0; i < 3; i++)
	{
		b[i] = rank;
	}
	MPI_Gather(&b[0], 3, MPI_INT, &s[0], 3, MPI_INT, 0, MPI_COMM_WORLD);
	if (rank == 0){
		printf("rank=%d [", rank);
		for (int i = 0; i < 3 * size; i++)
		{
			printf("%d ", s[i]);
		}
		printf("]\n");
	}
	
	MPI_Finalize();

	return 0;
}
