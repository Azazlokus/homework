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
	int *b = new int[size - rank];
	int *a = new int[size * (size + 1) / 2];
	int *rc = new int[size];
	int *ds = new int[size];
	for (int i = 0; i < size-rank; i++)
	{
		b[i] = rank;
	}
	for (int i = 0; i < size; i++)
	{
		rc[i] = size - i;
	}
	ds[0] = 0;
	for (int i = 1; i < size; i++)
	{
		ds[i] = ds[i-1] + size - i + 1;
	}
	
	MPI_Gatherv(&b[0], size-rank, MPI_INT, &a[0], rc, ds, MPI_INT, 0, MPI_COMM_WORLD);
	if (rank == 0)
	{
		printf("rank=%d [", rank);
		for (int i = 0; i < size * (size + 1) / 2; i++)
		{
			printf("%d ", a[i]);
		}
		printf("]\n");
	}
	MPI_Finalize();

	return 0;
}
