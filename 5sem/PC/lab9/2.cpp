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
	int *b = new int[rank + 1];
	int *a = new int[size * (size + 1) / 2];
	int *bl = new int[size];
	int *ds = new int[size];
	for (int i = 0; i < rank + 1; i++)
	{
		b[i] = rank;
	}
	for (int i = 0; i < size; i++)
	{
		ds[i] = i * (i + 1) / 2;
		bl[i] = i + 1;
	}

	MPI_Gatherv(&b[0], rank + 1, MPI_INT, &a[0], bl, ds, MPI_INT, 0, MPI_COMM_WORLD);
	if (rank == 0)
	{
		printf("rank=%d [", rank);
		for (int i = 0; i < size * (size + 1) / 2; i++)
		{
			printf("%d ", a[i]);
		}
		printf("]\n");
	}
	MPI_Finalize();

	return 0;
}
