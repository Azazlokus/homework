#include <windows.h>
#include <iostream>
#include "mpi.h"
using namespace std;
int main(int argc, char *argv[])
{
	int rank;
	int size;
	int n = 1000000000;
	MPI_Status stat;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	int *a = new int[n];
	int *b = new int[n / 2];
	if (rank == 0)
	{
		double start, end;
		for (int i = 0; i < n; i++)
		{
			a[i] = i;
		}
		start = MPI_Wtime();
		for (int i = 0; i < n; i++)
		{
			if (i % 2 == 0)
			{
				MPI_Send(&a[i], 1, MPI_INT, 1, 777, MPI_COMM_WORLD);
			}
		}
		MPI_Recv(b, n / 2, MPI_INT, 1, 777, MPI_COMM_WORLD, &stat);
		end = MPI_Wtime();
		cout << "t = " << end - start << endl;
		delete[] b;
		delete[] a;
	}
	else
	{
		for (int i = 0; i < n / 2; i++)
		{
			MPI_Recv(&b[i], 1, MPI_INT, 0, 777, MPI_COMM_WORLD, &stat);
		}
		MPI_Send(b, n / 2, MPI_INT, 0, 777, MPI_COMM_WORLD);
		delete[] a;
		delete[] b;
	}
	MPI_Finalize();
	return 0;
}
