#include <stdio.h>
#include "mpi.h"
#include "windows.h"
int main(int argc, char *argv[]){
	int rank;
	int size;
	int i, s = 0;
	MPI_Status stat;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	int *a = new int[(size * (size + 1)) / 2];
	if (rank == 0){
		for (i = 0; i < (size * (size + 1)) / 2; i++){
			a[i] = i;
		}
	}
	 
	int *b = new int[rank + 1];
	int *rc = new int[size];
	int *ds = new int[size];
	for (int i = 0; i < size; i++){
		rc[i] = i + 1;
		ds[i] = (i * (i + 1)) / 2;
	}
	MPI_Scatterv(a, rc, ds, MPI_INT, b, rank + 1, MPI_INT, 0, MPI_COMM_WORLD);
	Sleep(1000 * rank);
	printf("rank= %d [", rank);
	for (i = 0; i < rank + 1; i++){
		printf(" %d ", b[i]);
	}	
	printf("]\n ");
	MPI_Finalize();
	return 0;
}