import threading
import time

# Initialize lock for mutual exclusion and semaphore for readers
mutex = threading.Lock()
write_semaphore = threading.Semaphore(1)

# Shared data and reader counter
shared_data = ""
read_count = 0
read_count_lock = threading.Lock()

def writer(writer_id):
    global shared_data
    for i in range(2):
        # Writer acquires write semaphore for exclusive access
        write_semaphore.acquire()
        print(f"Writer {writer_id} is writing...")
        shared_data = f"Data written by Writer {writer_id} at iteration {i + 1}"
        time.sleep(1)
        print(f"Writer {writer_id} has finished writing.")
        write_semaphore.release()
        time.sleep(2)

def reader(reader_id):
    global read_count
    for i in range(2):
        # Reader incrementing read_count safely
        read_count_lock.acquire()
        read_count += 1
        if read_count == 1:
            # First reader locks the writer semaphore
            write_semaphore.acquire()
        read_count_lock.release()

        # Reader accesses the shared data
        print(f"Reader {reader_id} is reading: {shared_data}")
        time.sleep(1)
        print(f"Reader {reader_id} has finished reading.")

        # Reader decrementing read_count safely
        read_count_lock.acquire()
        read_count -= 1
        if read_count == 0:
            # Last reader releases the writer semaphore
            write_semaphore.release()
        read_count_lock.release()
        time.sleep(2)

# Create and start threads for one writer and two readers
writer_thread = threading.Thread(target=writer, args=(1,))
reader_thread1 = threading.Thread(target=reader, args=(1,))
reader_thread2 = threading.Thread(target=reader, args=(2,))

writer_thread.start()
reader_thread1.start()
reader_thread2.start()

# Wait for all threads to complete
writer_thread.join()
reader_thread1.join()
reader_thread2.join()

print("All writers and readers have finished their tasks.")

