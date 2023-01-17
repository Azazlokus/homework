#include <stdio.h>
#include "mpi.h"

int main(int argc, char *argv[])
{
	int rank;
	int size;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Status stat;
	int n = 7;
	int *s = new int[size - 1];

	if (rank == 0)
	{	
		for (int i = 1; i < size; i++)
		{
			MPI_Recv(&n, 1, MPI_INT, i, 777, MPI_COMM_WORLD, &stat);
			s[i - 1] = n;
		}
		for (int i = 0; i < size - 1; i++)
		{
			printf(" %d ", s[i]);
		}
	}
	else
	{
		MPI_Send(&n, 1, MPI_INT, 0, 777, MPI_COMM_WORLD);	
	}
	delete[] s;
	MPI_Finalize();
	return 0;
}