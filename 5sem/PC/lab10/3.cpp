#include <stdio.h>
#include "mpi.h"
int main(int argc, char *argv[])
{
	int rank;
	int size;
	int n;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	if (rank == 0){
		scanf("%d", &n);
	}
	MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);
	int **a = new int *[size];
	a[0] = new int[n * size];
	for (int i = 1; i < size; i++)
	{
		a[i] = a[i - 1] + n;
	}

	if (rank == 0)
	{
		for (int i = 0; i < size; i++)
		{
			for (int j = 0; j < n; j++)
			{
				a[i][j] = 10*(i+1) + j + 1;
			}
		}
	}

	int *b = new int[n];
	MPI_Scatter(*a, n, MPI_INT, b, n, MPI_INT, 0, MPI_COMM_WORLD);

	printf("rank= %d b: [", rank);
	for (int i = 0; i < n; i++)
	{
		printf(" %d ", b[i]);
	}
	printf("]\n");
	MPI_Finalize();
	return 0;
}