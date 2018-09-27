
import threading
import queue as q
import os
import time

buffer_size = 5

lock = threading.Lock()
queue = q.Queue(buffer_size)
file_count = 0

def producer(top_dir, queue_buffer):
    text = os.listdir(top_dir)
    # print(top_dir)
    if os.path.isdir(top_dir) == True:
        queue_buffer.put(top_dir, block=True)
    for i in text:
        
        
            # print(text_path)
            # while not queue_buffer.full():
            #     queue_buffer.put(text_path, block=False)
            
            # lock.acquire()
            
        text_path = os.path.join(top_dir, i)
        if os.path.isdir(text_path) == True:
            producer(text_path, queue)
            # lock.release()
                # print(queue_buffer.qsize())
            # except q.Full:
            #     time.sleep(1)
            #     while queue_buffer.empty():
            # # lock.acquire()
            #         queue_buffer.put(text_path, block=False)
            # # lock.release()
              
                

    # for i in text:
    #     text_path = os.path.join(top_dir, i)
    #     if os.path.isdir(text_path) == True:
    #         producer(text_path, queue)
    
   
        
def consumer(queue_buffer):
    global file_count
    # if not queue_buffer.empty():
    #     text_path = queue_buffer.get(block = False)
    #     if os.path.isfile(text_path) == True:
    #         global file_count
    #         file_count = file_count + 1
    # for i in (0, 10000):
    try:
            # lock.acquire()
        text = queue_buffer.get(block = True, timeout = 0.1)
        text_path = os.listdir(text)
        for i in text_path:
            text_abspath = os.path.join(text, i)
            if os.path.isfile(text_abspath) == True:
                print(text_abspath)
                lock.acquire()
                file_count = file_count + 1
                lock.release()
            # else:
            #     lock.acquire()
            #     file_count = file_count + 1
            #     lock.release()
            # lock.release()
    except q.Empty:
        pass
        # while queue_buffer.full():
        #     # lock.acquire()
        #     text_path = queue_buffer.get(block = False)
        #     if os.path.isfile(text_path) == True:
        #     # global file_count
        #             file_count = file_count + 1
        #     # lock.release()
    # else:
    #     if os.path.isfile(text_path) == True:
                
    #         file_count = file_count + 1
        
            


def main():
    producer_thread = threading.Thread(target = producer, args = ('./testdata', queue))

    consumer_count = 20
    consumers = []
    for i in range(consumer_count):
        consumers.append(threading.Thread(target = consumer, args = (queue,)))

    producer_thread.start()
    for c in consumers:
        c.start()

    producer_thread.join()
    for c in consumers:
        c.join()

    print(file_count, 'files found.')

if __name__ == "__main__":
    main()