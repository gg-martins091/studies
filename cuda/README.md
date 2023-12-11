## Followed tutorials 01 and 02 from here:   
https://cuda-tutorial.readthedocs.io/en/latest/tutorials/tutorial01/


### Overview

1 - Fist add two arrays single threaded   (same as c program)
2 - Then, with 1 block of 256 threads (256 threads with strides of 256)   
3 - Then, with a grid of x blocks with 256 threads where x is at least N/256 (1 operation per thread)   

N = 10000000   

1 - slowwwww   
2 - fast, 14ms   
3 - wow, 740us   



### Running
```nvcc first.cu   
nvprof ./a.out   ```

