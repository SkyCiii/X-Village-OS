import multiprocessing
import random
import time
import numpy as np

def thread_func(i, j, matA, matB, result, result_queue, result_sort_queue):
    for k in range(j):
        result[j*i+k] = np.matmul(matA[j*i+k], matB)
        result_sort = np.hstack((([j*i+k], result[j*i+k])))
        result_queue.put(result[j*i+k])
        result_sort_queue.put(result_sort)
        
def main():
    starttime = time.time()

    result_queue = multiprocessing.Manager().Queue()
    result_sort_queue = multiprocessing.Manager().Queue()

    j = 100

    matA = np.random.randint(10, size = (10*j, 10*j))
    matB = np.random.randint(10, size = (10*j, 10*j))
    result = np.zeros((matA.shape[0], matB.shape[1]))
    
    processes = 10
    jobs = []

    for i in range(processes):
        process = multiprocessing.Process(target = thread_func, args = (i, j, matA, matB, result, result_queue, result_sort_queue))
        jobs.append(process)

    for process in jobs:
        process.start()
        
    for process in jobs:
        process.join()

    result = result_queue.get()
    result_sort = result_sort_queue.get()

    while not result_queue.empty():
        result = np.vstack((result, result_queue.get()))
        result_sort = np.vstack((result_sort, result_sort_queue.get()))
        
    result_sort = result_sort[result_sort[:,0].argsort()]
    result = np.delete(result_sort, 0, 1)

    print(type(result))
    print(type(np.matmul(matA, matB)))
    endtime = time.time()

    print('Answer is correct:', np.all(np.matmul(matA, matB) == result))
    print(endtime-starttime)

if __name__ == "__main__":
    main()