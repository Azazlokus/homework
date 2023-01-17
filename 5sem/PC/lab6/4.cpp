#include <stdio.h>
#include "mpi.h"
#include "time.h"
#include "stdlib.h"
using namespace std;
int main(int argc, char *argv[])
{
	int rank;
	int size;
	int n = 0;
	double eps = 1e-9;
	MPI_Status stat;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	if (rank == 0)
	{
		double start, end;
		double suma = 0;
		double sum;
		start = MPI_Wtime();
		for (int i = 1; i < size; i++)
		{
			MPI_Recv(&sum, 1, MPI_DOUBLE, MPI_ANY_SOURCE, 777, MPI_COMM_WORLD, &stat);
			suma = suma + sum;
		}
		end = MPI_Wtime();
		printf("res: %f, sec: %f\n", suma, end - start);
	}
	else
	{
		double sum = 0;
		for (int i = rank; 1.0 / (1 + i) > eps; i = i + (size - 1))
		{
			sum += 1.0 / (1 + i);
		}
		MPI_Send(&sum, 1, MPI_DOUBLE, 0, 777, MPI_COMM_WORLD);
	}
	MPI_Finalize();
	return 0;
}