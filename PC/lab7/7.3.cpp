#include <stdio.h>
#include "iostream"
#include "mpi.h"
#include "windows.h"

using namespace std;

int main(int argc, char *argv[])
{
	int rank;
	int size;
	MPI_Status stat;
	MPI_Request req;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	double t1, t2;
	int n = 10000000;
	if (rank == 0)
	{
		int *a = new int[n];
		for (int i = 0; i < n; i++)
		{
			a[i] = 0;
		}
		t1 = MPI_Wtime();
		MPI_Sendrecv(&a[0], n, MPI_INT, 1, 777, &a[0], n, MPI_INT, 1, 777, MPI_COMM_WORLD, &stat);
		t2 = MPI_Wtime();
		printf("rank=%d t2-t1=%g\n", rank, t2 - t1);
	}
	if (rank == 1)
	{
		int *b = new int[n];
		for (int i = 0; i < n; i++)
		{
			b[i] = 1;
		}
		t1 = MPI_Wtime();
		MPI_Sendrecv(&b[0], n, MPI_INT, 0, 777, &b[0], n, MPI_INT, 0, 777, MPI_COMM_WORLD, &stat);
		t2 = MPI_Wtime();
		printf("rank=%d t2-t1=%g\n", rank, t2 - t1);
	}
	MPI_Finalize();
	return 0;
}
