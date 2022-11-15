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
	int **b = new int *[2];
	b[0] = new int[2 * size];
	for (int i = 1; i < 2; i++)
		b[i] = b[i - 1] + size;
	for (int i = 0; i < 2; i++){
		for (int j = 0; j < rank + 1; j++)
			b[i][j] = rank;
		for (int j = rank + 1; j < size; j++)
			b[i][j] = 0;
	}
		
	int **a = new int *[2 * size];
	a[0] = new int[2 * size * size];
	for (i = 1; i < 2 * size; i++) 
		a[i] = a[i - 1] + size;
	for (int i = 0; i < 2 * size; i++)
		for (int j = 0; j < size; j++)
			a[i][j] = 0;

	int *RC = new int[size];
	int *ds = new int[size];
	for (int i = 0; i < size; i++){
		ds[i] = 2 * i * size;
		RC[i] = 2 * size;
	}
		
		
	MPI_Gatherv(*b, 2*size, MPI_INT, *a, RC, ds, MPI_INT, 0, MPI_COMM_WORLD);
	if (rank == 0)
	{
		printf("rank= %d a: \n", rank);
		for (i = 0; i < 2 * size; i++)
		{
			for (j = 0; j < size; j++) 
				printf(" %d ", a[i][j]);
			printf("\n ");
		}
	}
	MPI_Finalize();
	return 0;
}