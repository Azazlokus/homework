#include <cmath>
#include "windows.h"
#include "mpi.h"

int main(int argc, char *argv[])
{
	int rank, size, n = 10000;
	double t1, t2;
	int *a = new int[n];
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	if (rank == 5)
	{
		for (int i = 0; i < n; i++){
			a[i] = rank;
		}
	}
	t1 = MPI_Wtime();
	MPI_Bcast(&a[0], n, MPI_INT, 5, MPI_COMM_WORLD);
	t2 = MPI_Wtime();
	Sleep(1000);
	if (rank == 0)
	{
		printf("time: %g\n", t2 - t1);
	}

	MPI_Finalize();
	return 0;
}