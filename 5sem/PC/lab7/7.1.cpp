#include <stdio.h>
#include "mpi.h"
#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
	int rank;
	int size, a = 0, b = 1;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Status stat;

	if (rank == 0 || rank == 1)
	{
		if (rank == 0)
		{
			cout << "rank: " << rank << " before: " << a << endl;
			MPI_Sendrecv(&a, 1, MPI_INT, rank + 2, 777, &a, 1, MPI_INT, MPI_ANY_SOURCE, 777, MPI_COMM_WORLD, &stat);
			cout << "rank: " << rank << " after: " << a << endl;
		}
		else
		{
			cout << "rank: " << rank << " before: " << b << endl;
			MPI_Sendrecv(&b, 1, MPI_INT, rank + 2, 777, &b, 1, MPI_INT, MPI_ANY_SOURCE, 777, MPI_COMM_WORLD, &stat);
			cout << "rank: " << rank << " after: " << b << endl;
		}
	}
	else if (rank == size - 1 || rank == size - 2)
	{
		if (rank % 2 == 0)
		{
			MPI_Recv(&a, 1, MPI_INT, rank - 2, 777, MPI_COMM_WORLD, &stat);
			a += 1;
			MPI_Send(&a, 1, MPI_INT, 0, 777, MPI_COMM_WORLD);
		}
		else
		{
			MPI_Recv(&b, 1, MPI_INT, rank - 2, 777, MPI_COMM_WORLD, &stat);
			b += 1;
			MPI_Send(&b, 1, MPI_INT, 1, 777, MPI_COMM_WORLD);
		}
	}
	else
	{
		if (rank % 2 == 0)
		{
			MPI_Recv(&a, 1, MPI_INT, rank - 2, 777, MPI_COMM_WORLD, &stat);
			a += 1;
			MPI_Send(&a, 1, MPI_INT, rank + 2, 777, MPI_COMM_WORLD);
		}
		else
		{
			MPI_Recv(&b, 1, MPI_INT, rank - 2, 777, MPI_COMM_WORLD, &stat);
			b += 1;
			MPI_Send(&b, 1, MPI_INT, rank + 2, 777, MPI_COMM_WORLD);
		}
	}

	MPI_Finalize();
	return 0;
}
