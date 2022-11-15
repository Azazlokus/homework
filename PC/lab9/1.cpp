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
	int *b = new int[2];
	int *s = new int[2*size];
	for (int i=0; i < 2; i++){
		b[i] = rank;
	}
	MPI_Gather(&b[0], 2, MPI_INT, &s[0], 2, MPI_INT, 0, MPI_COMM_WORLD);
	printf("rank=%d [", rank);
	for (int i = 0; i < 2*size; i++){
		printf("%d ", s[i]);
	}
	printf("]\n");
	MPI_Finalize();

	return 0;
}
