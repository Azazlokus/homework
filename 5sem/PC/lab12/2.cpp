#include <stdio.h>
#include "mpi.h"
int main(int argc, char *argv[])
{
	int rank;
	int size;
	int n = 20, i;
	MPI_Status stat;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	int *a = new int[n];
	for (i = 0; i < n; i++)
	{
		a[i] = -1;
	}
	MPI_Datatype mt;
	MPI_Type_vector(4, 2, 3, MPI_INT, &mt);
	MPI_Type_commit(&mt);
	if (rank == 0)
	{
		for (i = 0; i < n; i++)
		{
			a[i] = i;
		}
		MPI_Send(a, 1, mt, 1, 777, MPI_COMM_WORLD);
	}
	if (rank == 1)
	{
		MPI_Recv(a, 1, mt, 0, 777, MPI_COMM_WORLD, &stat);
		printf("rank= %d a: ", rank);
		for (i = 0; i < n; i++)
		{
			printf("%d ", a[i]);
		}
		printf("\n");
	}
	MPI_Finalize();
	return 0;
}