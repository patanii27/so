import threading
import time

# Initialize semaphores and locks
write_semaphore = threading.Semaphore(1)
read_count_lock = threading.Lock()

# Shared data and counters
shared_data = ""
read_count = 0

# Number of iterations for reading and writing
NUM_ITERATIONS = 3


def writer(writer_id):
    global shared_data
    for i in range(NUM_ITERATIONS):
        # Acquire semaphore to ensure exclusive writing
        write_semaphore.acquire()
        print(f"Writer {writer_id} is writing...")

        # Write to the shared data
        shared_data = f"Data written by Writer {writer_id} at iteration {i + 1}"
        time.sleep(1)

        # Writer finished
        print(f"Writer {writer_id} has finished writing: {shared_data}")

        # Release semaphore after writing
        write_semaphore.release()
        time.sleep(3)  # Simulate time between writes

    print(f"Writer {writer_id} has finished all writing tasks.")


def reader(reader_id):
    global read_count
    for i in range(NUM_ITERATIONS):
        # Acquire lock to update read_count safely
        read_count_lock.acquire()
        read_count += 1
        if read_count == 1:
            # First reader locks the writer semaphore
            write_semaphore.acquire()
        read_count_lock.release()

        # Reading the shared data
        print(f"Reader {reader_id} is reading: {shared_data}")
        time.sleep(1)

        # Decrease read_count and potentially allow writers if no readers left
        read_count_lock.acquire()
        read_count -= 1
        if read_count == 0:
            write_semaphore.release()
        read_count_lock.release()

        time.sleep(2)  # Simulate time between reads

    print(f"Reader {reader_id} has finished all reading tasks.")


# Create writer and reader threads
writer_thread1 = threading.Thread(target=writer, args=(1,))
writer_thread2 = threading.Thread(target=writer, args=(2,))
reader_thread1 = threading.Thread(target=reader, args=(1,))
reader_thread2 = threading.Thread(target=reader, args=(2,))

# Start the threads
writer_thread1.start()
writer_thread2.start()
reader_thread1.start()
reader_thread2.start()

# Wait for all threads to complete
writer_thread1.join()
writer_thread2.join()
reader_thread1.join()
reader_thread2.join()

print("All writers and readers have finished their tasks.")
