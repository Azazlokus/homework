#include <stdio.h>
#include "mpi.h"

int main(int argc, char *argv[])
{
	int rank;
	int size;
	double res = 0, sumPart = 1, i = 0, start, end, eps;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	if (rank == 0)
		eps = 1e-6;
	if (rank == 1)
		eps = 1e-7;
	if (rank == 2)
		eps = 1e-8;
	if (rank == 3)
		eps = 1e-9;

	start = MPI_Wtime();
	while (sumPart > eps)
	{
		sumPart = 1. / (1 + i);
		res += sumPart;
		i++;
	}
	end = MPI_Wtime();
	printf("rank: %d, res: %f, sec: %f\n", rank, res, end - start);

	MPI_Finalize();
	return 0;
}
