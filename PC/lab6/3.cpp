#include <stdio.h>
#include "iostream"
#include "mpi.h"

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
		int **a = new int *[size];
		a[0] = new int[size * size];
		for (int i = 1; i < size; i++)
			a[i] = a[i - 1] + size;

		for (int i = 1; i < size; i++)
		{
			MPI_Probe(MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &stat);
			int count = 0;
			MPI_Get_count(&stat, MPI_INT, &count);
			MPI_Recv(a[stat.MPI_SOURCE], count, MPI_INT, stat.MPI_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &stat);
			printf("source = %d \n", stat.MPI_SOURCE);
		}
		for (int i = 0; i < size; i++)
		{
			for (int j = 0; j < size; j++)
				printf("%d ", a[i][j]);
			cout << endl;
		}
	}
	else
	{
		int *a = new int[rank + 1];
		for (int i = 0; i < rank + 1; i++)
		{
			a[i] = rank;
		}
		MPI_Send(&a[0], rank + 1, MPI_INT, 0, 100 * rank, MPI_COMM_WORLD);
	}

	MPI_Finalize();

	return 0;
}
