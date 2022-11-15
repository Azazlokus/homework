#include <stdio.h>
#include "mpi.h"
#include <iostream>
using namespace std;
int main(int argc, char *argv[])
{
	int rank;
	int size;
	int i, s = 0, j;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	int *b = new int[size-rank];
	for (i = 0; i < size-rank; i++)
	 	b[i] = rank;

	int **a = new int *[size];
	a[0] = new int[size * size];
	for (i = 1; i < size; i++)
	 	a[i] = a[i - 1] + size;
	
	for (int i = 0; i < size; i++)
		for (int j = 0; j < size; j++)
			a[i][j] = 0;
	
	
	int *RC = new int[size];		
	int *ds = new int[size];
	for (int i = 0; i < size; i++){
		RC[size-1-i] = i + 1;
		ds[i] = i * size;
	}
		
	MPI_Gatherv(b, size-rank, MPI_INT, *a, RC, ds, MPI_INT, 0, MPI_COMM_WORLD);
	if (rank == 0)
	{
		printf("rank= %d a: \n", rank);
		for (i = 0; i < size; i++)
		{
			for (j = 0; j < size; j++)
				printf(" %d ", a[i][j]);
			printf("\n ");
		}
	}
	MPI_Finalize();
	return 0;
}