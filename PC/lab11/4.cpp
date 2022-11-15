#include <stdio.h>
#include "mpi.h"
int main(int argc, char *argv[])
{
	int rank;
	int size;
	int i;
	MPI_Status stat;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	int *a = new int[size * (size+1) / 2];
	for (i = 0; i < size * (size + 1) / 2; i++)
	{
		a[i] = rank + i;
	}
	int *b = new int[rank + 1];
	int *rc = new int[size];
	for (i = 0; i < size; i++)
	{
		rc[i] = i + 1;
	}
	MPI_Reduce_scatter(a, b, rc, MPI_INT, MPI_SUM, MPI_COMM_WORLD);

	printf("rank= %d b: ", rank);
	for (i = 0; i < rank+1; i++)
	{
		printf(" %d ", b[i]);
	}
	printf("\n ");
	MPI_Finalize();
	return 0;
}