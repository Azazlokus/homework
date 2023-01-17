#include <stdio.h>
#include "mpi.h"
int main(int argc, char *argv[])
{
	int rank;
	int size;
	int n = 20;
	MPI_Status stat;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	int *a = new int[n];
	for (int i = 0; i < n; i++) {
		a[i] = 0;
	}
	MPI_Datatype mt;
	int bl[] = {2, 3, 1, 1};
	int ds[] = {7, 3, 13, 1};
	MPI_Type_indexed(4, bl, ds, MPI_INT, &mt);
	MPI_Type_commit(&mt);
	if (rank == 0)
	{
		for (int i = 0; i < n; i++) {
			a[i] = i;
		}
		MPI_Send(a, 1, mt, 1, 777, MPI_COMM_WORLD);
	}
	if (rank == 1)
	{
		MPI_Recv(a, 1, mt, 0, 777, MPI_COMM_WORLD, &stat);
		printf("rank= %d a: ", rank);
		for (int i = 0; i < n; i++){
			printf("%d ", a[i]);
		}
		printf("\n");
	}
	MPI_Finalize();
	return 0;
}