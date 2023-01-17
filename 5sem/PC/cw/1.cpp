#include <stdio.h>
#include "mpi.h"

int main(int argc, char *argv[])
{
	int rank;
	int size, n;
	int buffer_len = MPI_MAX_PROCESSOR_NAME;
	char name[buffer_len];
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Status stat;

	if (rank == 0)
	{
		n = 7;
		printf("before: n=%d\n", n);
		MPI_Send(&n, 1, MPI_INT, 2, 777, MPI_COMM_WORLD);
		MPI_Recv(&n, 1, MPI_INT, 2, 777, MPI_COMM_WORLD, &stat);
		printf("after: n=%d\n", n);
		MPI_Get_processor_name(name, &buffer_len);
		printf("rank:%d name:%s\n", rank, name);
	}
	else if (rank == 2)
	{
		MPI_Recv(&n, 1, MPI_INT, 0, 777, MPI_COMM_WORLD, &stat);
		n += 1;
		MPI_Send(&n, 1, MPI_INT, 0, 777, MPI_COMM_WORLD);
		MPI_Get_processor_name(name, &buffer_len);
		printf("rank:%d name:%s\n", rank, name);
	}
	MPI_Finalize();
	return 0;
}
