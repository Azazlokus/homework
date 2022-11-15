#include <stdio.h>
#include "mpi.h"
#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
	int rank;
	int size, n = 20;
	int a[n];
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Status stat;

	if (rank == 0)
	{
		for (int i = 0; i < n; i++)
		{
			a[i] = i;
		}

		for (int i = 1; i < size; i++)
		{
			MPI_Send(&a, n, MPI_INT, i, 777, MPI_COMM_WORLD);
		}
	}
	else
	{
		for (int i = 0; i < n; i++)
		{
			a[i] = 0;
		}
		MPI_Recv(&a, n, MPI_INT, 0, 777, MPI_COMM_WORLD, &stat);
	}

	cout << "rank: " << rank << endl;
	for (int i = 0; i < n; i++)
	{
		cout << a[i] << " ";
	}
	cout << endl;

	MPI_Finalize();
	return 0;
}