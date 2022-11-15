#include <stdio.h>
#include "mpi.h" 
int main(int argc, char *argv[])
{
	int rank;
	int size;
	int n;
	MPI_Status stat;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	if (rank == 0) {
		scanf("%d", &n);
	} 
	MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);
	int *a = new int[n];
	for (int i = 0; i < n; i++) {
		a[i] = i + rank;
	}
	int *b = new int[n];
	MPI_Reduce(a, b, n, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
	
	if (rank == 0){
		printf("rank= %d b: ", rank);
		for (int i = 0; i < n; i++)
		{
			printf(" %d ", b[i]);
		}
		printf("\n ");
	}
	MPI_Finalize();
	return 0;
}