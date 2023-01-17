#include <stdio.h>
#include "mpi.h"
#include <iostream>
#include "windows.h"
using namespace std;

int main(int argc, char *argv[])
{
	int rank;
	int size;
	int *a = new int[3*size];
	int *b = new int[3];
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Status stat;

	if (rank == 0)
	{
		for (int i = 0; i < 3*size; i++)
		{
			a[i] = i;
		}

		for (int i = 1; i < size; i++)
		{
			MPI_Send(&a[3*i], 3, MPI_INT, i, 777, MPI_COMM_WORLD);
		}
	}
	else
	{
		for (int i = 0; i < 3; i++)
		{
			b[i] = 0;
		}
		MPI_Recv(&b[0], 3, MPI_INT, 0, 777, MPI_COMM_WORLD, &stat);
	}

	
	if (rank == 0){
		cout << "rank: " << rank << " a: ";
		for (int i = 0; i < 3 * size; i++)
		{
			cout << a[i] << " ";
		}
		cout << endl;
	} else {
		Sleep(1000);
		cout << "rank: " << rank << " b: ";
		for (int i = 0; i < 3; i++)
		{
			cout << b[i] << " ";
		}
		cout << endl;
	}
	delete[] a;
	delete[] b;
	MPI_Finalize();
	return 0;
}