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
	int **a = new int *[(size * (size + 1)) / 2];
	a[0] = new int[(size * (size + 1)) / 2 * n];
	for (int i = 1; i < (size * (size + 1)) / 2; i++)
	{
		a[i] = a[i - 1] + n;
	}
	if (rank == 0)
	{
		for (int i = 0; i < (size * (size + 1)) / 2; i++)
		{
			for (int j = 0; j < n; j++)
			{
				a[i][j] = 10 * (i+1) + j + 1;
			}
		}
	}
	int **b = new int *[rank + 1];
	b[0] = new int[(rank + 1) * n];
	for (int i = 1; i < rank + 1; i++)
	{
		b[i] = b[i - 1] + n;
	}
	int *rc = new int[size];
	int *ds = new int[size];
	for (int i = 0; i < size; i++)
	{
		rc[i] = (i + 1) * n;
		ds[i] = i * (i + 1) / 2 * n;
	}
	MPI_Scatterv(*a, rc, ds, MPI_INT, *b, (rank + 1) * n, MPI_INT, 0, MPI_COMM_WORLD);
	printf("rank= %d \n", rank);
	for (int i = 0; i < rank + 1; i++)
	{
		printf("[");
		for (int j = 0; j < n; j++)
		{
			printf(" %d ", b[i][j]);
		}
		printf("]\n");
	}
	MPI_Finalize();
	delete[] rc;
	delete[] ds;
	delete[] b[0];
	delete[] b;
	delete[] a[0];
	delete[] a;
	return 0;
}