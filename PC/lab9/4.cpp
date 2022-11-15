#include <stdio.h>
#include "mpi.h"
int main(int argc, char *argv[])
{
	int rank;
	int size;
	int i, s = 0, j;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	int *b = new int[rank + 1];
	for (i = 0; i < rank + 1; i++)
		b[i] = rank;
	int **a = new int *[size];
	a[0] = new int[size * size];
	for (i = 1; i < size; i++) 
		a[i] = a[i - 1] + size;
	int *rc = new int[size];
	for (int i = 0; i < size; i++) 
		rc[i] = i + 1;
	int *ds = new int[size];
	for (int i = 0; i < size; i++)
		ds[i] = i * size;
	MPI_Gatherv(b, rank + 1, MPI_INT, *a, rc, ds, MPI_INT, 0, MPI_COMM_WORLD);
	if (rank == 0)
	{
		printf("rank= %d a: \n", rank);
		for (i = 0; i < size; i++)
		{
			for (j = 0; j < size; j++) 
				printf(" %d ", a[i][j]);
			printf("\n ");
		}
	}
	MPI_Finalize();
	return 0;
}