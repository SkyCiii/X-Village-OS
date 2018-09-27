import numpy as np
import time

def main():
    i = 1000
    start_time = time.time()
    
    matA = np.random.randint(10, size = (i, i))
    matB = np.random.randint(10, size = (i, i))
    result = np.zeros((matA.shape[0], matB.shape[1]))
    
    for row in range(0, matA.shape[0]):
        result[row] = np.matmul(matA[row], matB)

    end_time = time.time()
    
    print('Answer is correct:', np.all(np.matmul(matA, matB) == result))
    print (end_time - start_time)

if __name__ == "__main__":
    main()