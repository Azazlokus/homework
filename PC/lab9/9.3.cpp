#include <stdio.h>
#include "mpi.h"
#include <iostream>
using namespace std;
int main(int argc, char *argv[])
{
	int rank;
	int size;
	int n, i, s = 0, j;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	if (rank == 0){
		cin >> n;
	}
	MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);

	int **b = new int *[2];
	b[0] = new int[2 * n];
	for (int i = 1; i < 2; i++)
		b[i] = b[i - 1] + n;
	for (int i = 0; i < 2; i++)
		for (int j = 0; j < n; j++)
			b[i][j] = rank;

	int **a = new int *[2 * size];
	a[0] = new int[2 * size * n];
	for (int i = 1; i < 2 * size; i++)
		a[i] = a[i - 1] + n;

	MPI_Gather(*b, 2*n, MPI_INT, *a, 2*n, MPI_INT, 0, MPI_COMM_WORLD);
	if (rank == 0)
	{
		printf("rank= %d a: \n", rank);
		for (i = 0; i < 2 * size; i++)
		{
			for (j = 0; j < n; j++)
				printf(" %d ", a[i][j]);
			printf("\n ");
		}
	}
	MPI_Finalize();
	return 0;
}