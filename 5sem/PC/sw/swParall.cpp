#include <time.h>
#include <iostream>
#include "mpi.h"
using namespace std;

int main(int argc, char *argv[])
{
	const int lenDesk = 8;
	const int quantityCell = 64;
	int chessDesk[lenDesk][lenDesk];
	int lineDesk[quantityCell];
	int quantityZeros = 0, quantitySolutions = 0, n = 0;
	double t1, t2;

	int rank;
	int size;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	if (rank == 0)
	{
		t1 = MPI_Wtime();
	}
	for (int i1 = rank; i1 < quantityCell - 4; i1 += size)
	{
		for (int i2 = i1 + 1; i2 < quantityCell - 3; i2++)
		{
			for (int i3 = i2 + 1; i3 < quantityCell - 2; i3++)
			{
				for (int i4 = i3 + 1; i4 < quantityCell - 1; i4++)
				{
					for (int i5 = i4 + 1; i5 < quantityCell; i5++)
					{
						for (int l = 0; l < quantityCell; l++)
						{
							lineDesk[l] = 0;
						}
						lineDesk[i1] = 2;
						lineDesk[i2] = 2;
						lineDesk[i3] = 2;
						lineDesk[i4] = 2;
						lineDesk[i5] = 2;
						int k = 0;
						for (int i = 0; i < lenDesk; i++)
						{
							for (int j = 0; j < lenDesk; j++)
							{
								chessDesk[i][j] = lineDesk[k];
								k++;
							}
						}
						for (int i = 0; i < lenDesk; i++)
						{
							for (int j = 0; j < lenDesk; j++)
							{
								if (chessDesk[i][j] == 2)
								{
									for (int m = 0; m < lenDesk; m++)
									{
										if (chessDesk[i][m] != 2)
										{
											chessDesk[i][m] = 1;
										}
									}
									for (int m = 0; m < lenDesk; m++)
									{
										if (chessDesk[m][j] != 2)
										{
											chessDesk[m][j] = 1;
										}
									}
									for (int m = 0; m < lenDesk; m++)
									{
										if (chessDesk[i + m][j + m] != 2)
										{
											if ((i + m < lenDesk) && (j + m < lenDesk))
											{
												chessDesk[i + m][j + m] = 1;
											}
										}
									}
									for (int m = 0; m < lenDesk; m++)
									{
										if (chessDesk[i - m][j - m] != 2)
										{
											if ((i - m >= 0) && (j - m >= 0))
											{
												chessDesk[i - m][j - m] = 1;
											}
										}
									}
									for (int m = 0; m < lenDesk; m++)
									{
										if (chessDesk[i - m][j + m] != 2)
										{
											if ((i - m >= 0) && (j + m < lenDesk))
											{
												chessDesk[i - m][j + m] = 1;
											}
										}
									}
									for (int m = 0; m < lenDesk; m++)
									{
										if (chessDesk[i + m][j - m] != 2)
										{
											if ((i + m < lenDesk) && (j - m >= 0))
											{
												chessDesk[i + m][j - m] = 1;
											}
										}
									}
								}
							}
						}
						quantityZeros = 0;
						for (int i = 0; i < lenDesk; i++)
						{
							for (int j = 0; j < lenDesk; j++)
							{
								if (chessDesk[i][j] == 0)
								{
									quantityZeros++;
								}
							}
						}
						if (quantityZeros == 0)
						{
							quantitySolutions++;
						}
					}
				}
			}
		}
	}
	MPI_Reduce(&quantitySolutions, &n, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
	if (rank == 0)
	{
		t2 = MPI_Wtime();
		cout << "Quantity of solutions = " << n << endl;
		cout << "Time: " << t2 - t1;
	}
	MPI_Finalize();
	return 0;
}