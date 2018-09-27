
import threading
import numpy as np
import time

def thread_func(i, j, matA, matB, result):
    for k in range(j):
        result[j*i+k] = np.matmul(matA[j*i+k], matB)

def main():
    start_time = time.time()

    j = 100

    matA = np.random.randint(10, size = (10*j, 10*j))
    matB = np.random.randint(10, size = (10*j, 10*j))

    result = np.zeros((matA.shape[0], matB.shape[1]))
    
    thread_num = 10
    threads = []

    for i in range(thread_num):
        
        thread = threading.Thread(target = thread_func, args = (i, j, matA, matB, result))
        threads.append(thread)
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

    print(result)
    print(np.matmul(matA, matB))
    end_time = time.time()

    print('Answer is correct:', np.all(np.matmul(matA, matB) == result))
    print (end_time - start_time)
    

if __name__ == "__main__":
    main()