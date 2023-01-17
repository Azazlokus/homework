#include <stdio.h>
#include "iostream"
#include "mpi.h"
#include "windows.h"

using namespace std;

int main(int argc, char *argv[])
{
	int rank;
	int size;
	int a = 0, b = 0, count = 0, flag = 0;
	MPI_Status stat;
	MPI_Request req;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	double t1, t2, t3;

	if (rank == 0)
	{
		a = 5;
		b = 0;
		t1 = MPI_Wtime();
		Sleep(1000);
		MPI_Sendrecv(&a, 1, MPI_INT, 1, 777, &b, 1, MPI_INT, 1, 777, MPI_COMM_WORLD, &stat);
		t2 = MPI_Wtime();
		printf("rank = %d t2-t1=%g a=%d b=%d\n", rank, t2 - t1, a, b);
	}

	if (rank == 1)
	{
		a = 0;
		b = 7;
		t1 = MPI_Wtime();
		MPI_Sendrecv(&b, 1, MPI_INT, 0, 777, &a, 1, MPI_INT, 0, 777, MPI_COMM_WORLD, &stat);
		t2 = MPI_Wtime();
		printf("rank = %d t2-t1=%g a=%d b=%d\n", rank, t2 - t1, a, b);
	}

	MPI_Finalize();

	return 0;
}
