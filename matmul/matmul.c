#include <stdint.h>
#include <stdio.h>
#include <assert.h>
#include <time.h>
#define N 1024

float A[N][N];
float B[N][N];
float C[N][N];

uint64_t nanos() {
	struct timespec start;
	clock_gettime(CLOCK_MONOTONIC_RAW, &start);
	return (uint64_t)start.tv_sec * 1000000000 + (uint64_t)start.tv_nsec;
}

#define BLOCK 32

int main() {
	assert(N%BLOCK == 0);

	uint64_t start = nanos();
	/* for (int by = 0; by < N; by += BLOCK) { */
	/* 	for (int bx = 0; bx < N; bx += BLOCK) { */
			for (int y = 0; y < N; y++) {
				for (int x = 0; x < N; x++) {
					float acc = 0;
					for(int k = 0; k < N; k++) {
						acc += A[y][k] * B[x][k];
					} 

					C[y][x] = acc;
				}
			}
		/* } */

	/* } */
	uint64_t end = nanos();
	double gflop = ((float)N*N*2*N)*1e-9;
	double s = (end-start)/1e9;

	printf("%f GFLOP/S\n", gflop/s);

	return 0;
}
