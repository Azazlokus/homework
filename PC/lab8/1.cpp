#include <cmath>
#include "mpi.h"
#include "windows.h"

int MyBcast(void *buffer, int count, MPI_Datatype datatype, int root, MPI_Comm comm)
{
	int rank, size, c_rank;
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Status stat;

	if (root >= size)
	{
		return -1;
	}

	if (rank >= root)
	{
		c_rank = rank - root;
	}
	else
	{
		c_rank = rank - root + size;
	}

	if (rank != root)
	{
		MPI_Recv(buffer, count, datatype, MPI_ANY_SOURCE, 777, comm, &stat);
	}

	for (int i = 0; i < ceil(log2(size)); i++)
	{
		if (c_rank < pow(2, i))
		{
			MPI_Send(buffer, count, datatype, int(ceil(pow(2, i) + rank)) % size, 777, comm);
		}
	}

	MPI_Barrier(comm);
	return 0;
}

int main(int argc, char *argv[])
{
	int rank, size;
	double t1, t2;
	int n;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	if (rank == 3)
	{
		n = 10;
	}
	t1 = MPI_Wtime();
	MyBcast(&n, 1, MPI_INT, 3, MPI_COMM_WORLD);
	t2 = MPI_Wtime();
	Sleep(1000);
	if (rank == 0)
	{
		printf("time: %g\n", t2 - t1);
	}
	printf("rank: %d n=%d\n", rank, n);
	MPI_Finalize();
	return 0;
}