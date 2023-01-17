#include <stdio.h>
#include "mpi.h"
int main(int argc, char *argv[])
{
	int rank;
	int size;
	int n = 5;
	MPI_Status stat;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	int **a = new int *[n];
	a[0] = new int[n * n];
	for (int i = 1; i < n; i++)
	{
		a[i] = a[i - 1] + n;
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			a[i][j] = 0;
		}
	}

	MPI_Datatype mt;
	int *bl = new int[n];
	int *ds = new int[n];
	for (int i = 0; i < n; i++)
	{
		bl[i] = i + 1;
		ds[i] = i * n;
	}
	MPI_Type_indexed(n, bl, ds, MPI_INT, &mt);
	MPI_Type_commit(&mt);

	if (rank == 0)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				a[i][j] = (i+1) + j;
			}
		}
		MPI_Send(*a, 1, mt, 1, 777, MPI_COMM_WORLD);
	}
	if (rank == 1)
	{
		MPI_Recv(*a, 1, mt, 0, 777, MPI_COMM_WORLD, &stat);
		printf("rank= %d a: \n", rank);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				printf(" %d ", a[i][j]);
			}
			printf("\n");
		}
	}
	MPI_Finalize();
	return 0;
}