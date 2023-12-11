
import numpy as np
import time

N = 1024;

if __name__ == '__main__':
    A = np.random.randn(N,N).astype(np.float16)
    B = np.random.randn(N,N).astype(np.float16)


    flop = N*N*2*N;

    # for i in range(100):
    st = time.monotonic()
    C = A@B;
    et = time.monotonic()

    s = et-st

    print(f"{flop/s * 1e-9:.2f} GFLOPS")
