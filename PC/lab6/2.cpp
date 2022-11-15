#include <stdio.h>
#include <iostream>
#include "mpi.h"
#include "time.h"
using namespace std;
int main(int argc, char *argv[])
{
	int rank;
	int size;
	int n = 0;
	MPI_Status stat;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	if (rank == 0)
	{
		int a[size];
		a[0] = 0;
		for (int i = 1; i < size; i++)
		{
			MPI_Recv(&n, 1, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &stat);
			a[stat.MPI_SOURCE] = n;
			printf("source = %d n=%d \n", stat.MPI_SOURCE, n);
		}
		for (int i = 0; i<size; i++) cout<< i << ": " << a[i] << endl;
	}
	else
	{
		srand(rank * time(0));
		n = rand();
		MPI_Send(&n, 1, MPI_INT, 0, 100 * rank, MPI_COMM_WORLD);
	}

	MPI_Finalize();
	return 0;
}
