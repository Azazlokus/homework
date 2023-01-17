#include <stdio.h>
#include "mpi.h"
#include "string.h"
int main(int argc, char *argv[])
{
	int rank, size;
	int a;
	double b;
	char c[12];
	MPI_Status stat;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	int n = sizeof(int) + sizeof(double) + 12 * sizeof(char);
	char *buf = new char[n];
	int pos = 0;
	if (rank == 0)
	{
		a = 7;
		b = 0.8;
		strcpy(c, "hello world!");
		MPI_Pack(&a, 1, MPI_INT, buf, n, &pos, MPI_COMM_WORLD);
		MPI_Pack(&b, 1, MPI_DOUBLE, buf, n, &pos, MPI_COMM_WORLD);
		MPI_Pack(&c, 12, MPI_CHAR, buf, n, &pos, MPI_COMM_WORLD);
		MPI_Send(buf, n, MPI_PACKED, 1, 777, MPI_COMM_WORLD);
	}
	if (rank == 1)
	{
		MPI_Recv(buf, n, MPI_PACKED, 0, 777, MPI_COMM_WORLD, &stat);
		MPI_Unpack(buf, n, &pos, &a, 1, MPI_INT, MPI_COMM_WORLD);
		MPI_Unpack(buf, n, &pos, &b, 1, MPI_DOUBLE, MPI_COMM_WORLD);
		MPI_Unpack(buf, n, &pos, &c, 12, MPI_CHAR, MPI_COMM_WORLD);
		printf("a= %d \n", a);
		printf("b= %f \n", b);
		printf("c= %s \n", c);
	}
	MPI_Finalize();
	return 0;
}