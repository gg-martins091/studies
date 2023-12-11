#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>

#define N 10000000
#define MAX_ERR 1e-6

__global__ void vector_add(float *out, float *a, float *b, int n) {
    // 1 thread per item add
    int tid = blockIdx.x * blockDim.x + threadIdx.x;
    if (tid < n){
        out[tid] = a[tid] + b[tid];
    }
}

__global__ void old_vector_add(float *out, float *a, float *b, int n) {
    int i = threadIdx.x;
    int stride = blockDim.x;
    while(i < n) {
        out[i] = a[i] + b[i];
        i += stride;
    }
}

int main(){
    float *a, *b, *out; 
    float *ad, *bd, *outd;

    // Allocate memory
    a   = (float*)malloc(sizeof(float) * N);
    b   = (float*)malloc(sizeof(float) * N);
    out = (float*)malloc(sizeof(float) * N);

    // Initialize array
    for(int i = 0; i < N; i++){
        a[i] = 1.0f;
        b[i] = 2.0f;
    }


    cudaMalloc((void**)&ad, sizeof(float) * N);
    cudaMalloc((void**)&bd, sizeof(float) * N);
    cudaMalloc((void**)&outd, sizeof(float) * N);

    cudaMemcpy(ad, a, sizeof(float) * N, cudaMemcpyHostToDevice);
    cudaMemcpy(bd, b, sizeof(float) * N, cudaMemcpyHostToDevice);
    /* for (int i = 0; i < N; i++) { */
    /*     printf("%f ", a[i]); */
    /* } */

    int block_size = 256; // 256 threads per block
    int grid_size = ((N+block_size)/block_size); // to have 1 thread per item
    // 1 thread per operation very fast 740us
    vector_add<<<grid_size,block_size>>>(outd, ad, bd, N);
    cudaMemcpy(out, outd, sizeof(float) * N, cudaMemcpyDeviceToHost);

    // 256 threads with 256 stride: N/256 operations per thread 14ms
    vector_add<<<grid_size,block_size>>>(outd, ad, bd, N);

    old_vector_add<<<1,256>>>(outd, ad, bd, N);
    cudaMemcpy(out, outd, sizeof(float) * N, cudaMemcpyDeviceToHost);

    // Verification
    for(int i = 0; i < N; i++){
        assert(fabs(out[i] - a[i] - b[i]) < MAX_ERR);
    }

    printf("out[0] = %f\n", out[0]);
    printf("PASSED\n");

    free(a);
    cudaFree(ad);
    free(b);
    cudaFree(bd);
    free(out);
    cudaFree(outd);
}
