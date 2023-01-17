#include <stdio.h>
#include "mpi.h"
#include "string.h"
int main(int argc, char *argv[])
{
	int rank, size, n = 10;
	MPI_Status stat;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Datatype st[n], mt;
	int **a = new int *[n];
	int *bl = new int [n];
	MPI_Aint *ds = new MPI_Aint [n];
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

	for (int i = 0; i < n; i++)
	{
		MPI_Type_vector(n-i, 1, n, MPI_INT, &st[i]);
		MPI_Type_commit(&st[i]);
		bl[i] = 1;
		ds[i] = 4*i;
	}

	MPI_Type_struct(n, bl, ds, st, &mt);
	MPI_Type_commit(&mt);

	if (rank == 0)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				a[i][j] = (i + 1) + j;
			}
		}
		MPI_Send(*a, 1, mt, 1, 777, MPI_COMM_WORLD);
	}
	if (rank == 1)
	{
		MPI_Recv(*a, 1, mt, 0, 777, MPI_COMM_WORLD, &stat);
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