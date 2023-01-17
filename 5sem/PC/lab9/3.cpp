#include <stdio.h>
#include "mpi.h"
int main(int argc, char *argv[])
{
	int rank;
	int size;
	int n, i, s = 0, j;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	if (rank == 0) 
		scanf("%d", &n);
	MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);
	int *b = new int[n];
	for (i = 0; i < n; i++)
		b[i] = rank;
	int **a = new int *[size];
	a[0] = new int[n * size];
	for (i = 1; i < size; i++)
		a[i] = a[i - 1] + n;
	MPI_Gather(b, n, MPI_INT, *a, n, MPI_INT, 0, MPI_COMM_WORLD);
	if (rank == 0)
	{
		printf("rank= %d a: \n", rank);
		for (i = 0; i < size; i++)
		{
			for (j = 0; j < n; j++)
				printf(" %d ", a[i][j]);
			printf("\n ");
		}
	}
	MPI_Finalize();
	return 0;
}