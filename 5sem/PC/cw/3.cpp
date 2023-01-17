#include <stdio.h>
#include "mpi.h"

int main(int argc, char *argv[])
{
	int rank;
	int size;
	MPI_Status stat;
	MPI_Request req;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	int n = 10;
	int *a = new int[n];
	for (int i = 0; i < n; i++)
	{
		a[i] = rank;
	}

	int **s = new int *[size];
	s[0] = new int[n * size];
	for (int i = 1; i < size; i++)
	{
		s[i] = s[i - 1] + n;
	}

	MPI_Gather(&a[0], n, MPI_INT, &s[0][0], n, MPI_INT, 0, MPI_COMM_WORLD);
	if (rank == 0)
	{
		printf("rank=%d \n", rank);
		for (int i = 0; i < size; i++)
		{
			printf("[");
			for (int j = 0; j < n; j++)
			{
				printf(" %d ", s[i][j]);
			}
			printf("]\n");
		}
	}
	delete[] a;
	delete[] s[0];
	delete[] s;
	MPI_Finalize();
	return 0;
}
