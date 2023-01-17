#include <stdio.h>
#include "mpi.h"
#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
	int rank, size;
	MPI_Status stat;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	int n = 100000000;
	char *a = new char[n];
	int size_buf;
	char *buf;
	double t1, t2;
	int pos = 0;
	if (rank == 0)
	{
		t1 = MPI_Wtime();
		size_buf = sizeof(char) * n;
		buf = new char[size_buf];
		for (int i = 0; i < n; i++)
		{
			a[i] = i;
		}

		MPI_Pack(a, n, MPI_CHAR, buf, size_buf, &pos, MPI_COMM_WORLD);
		MPI_Send(buf, size_buf, MPI_PACKED, 1, 777, MPI_COMM_WORLD);
		pos = 0;
		MPI_Recv(buf, size_buf, MPI_PACKED, 1, 777, MPI_COMM_WORLD, &stat);
		MPI_Unpack(buf, size_buf, &pos, a, n, MPI_CHAR, MPI_COMM_WORLD);
		delete[] buf;
		delete[] a;
		t2 = MPI_Wtime();
		printf("time: %f ", (t2 - t1)/2);
	}
	if (rank == 1)
	{
		size_buf = sizeof(char) * n;
		buf = new char[size_buf];
		MPI_Recv(buf, size_buf, MPI_PACKED, 0, 777, MPI_COMM_WORLD, &stat);
		MPI_Unpack(buf, size_buf, &pos, a, n, MPI_CHAR, MPI_COMM_WORLD);
		pos = 0;
		MPI_Pack(a, n, MPI_CHAR, buf, size_buf, &pos, MPI_COMM_WORLD);
		MPI_Send(buf, size_buf, MPI_PACKED, 0, 777, MPI_COMM_WORLD);
		delete[] buf;
		delete[] a;
	}
	MPI_Finalize();
	return 0;
}