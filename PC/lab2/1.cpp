#include <stdio.h>
#include "mpi.h"

int main(int argc, char *argv[])
{
	int rank;
	int size, n;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Status stat;

	if (rank == 0)
	{
		scanf("%d", &n);
		MPI_Send(&n, 1, MPI_INT, rank + 1, 777, MPI_COMM_WORLD);
		MPI_Recv(&n, 1, MPI_INT, size - 1, 777, MPI_COMM_WORLD, &stat);
		printf("after: n=%d", n);
	}
	else if (rank == size - 1)
	{
		MPI_Recv(&n, 1, MPI_INT, rank - 1, 777, MPI_COMM_WORLD, &stat);
		n += 1;
		MPI_Send(&n, 1, MPI_INT, 0, 777, MPI_COMM_WORLD);
	}
	else
	{
		MPI_Recv(&n, 1, MPI_INT, rank - 1, 777, MPI_COMM_WORLD, &stat);
		n += 1;
		MPI_Send(&n, 1, MPI_INT, rank + 1, 777, MPI_COMM_WORLD);
	}

	MPI_Finalize();
	return 0;
}
