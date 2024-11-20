import threading
import time
import random

# Initialize buffer, mutex, and semaphores
BUFFER_SIZE = 5
buffer = []

# Semaphores to keep track of the number of empty and full slots
empty = threading.Semaphore(BUFFER_SIZE)  # Starts with the number of empty slots
full = threading.Semaphore(0)  # Starts with zero full slots

# Mutex for mutual exclusion when accessing the buffer
buffer_mutex = threading.Lock()

# Number of iterations for producing and consuming
NUM_ITERATIONS = 10


def producer(producer_id):
    for i in range(NUM_ITERATIONS):
        # Produce an item (simulated by a random number)
        item = random.randint(1, 100)

        # Wait if buffer is full (empty semaphore)
        empty.acquire()

        # Acquire mutex before modifying the shared buffer
        buffer_mutex.acquire()
        buffer.append(item)
        print(f"Producer {producer_id} produced item {item}. Buffer: {buffer}")
        buffer_mutex.release()

        # Signal that buffer has a new item (release full semaphore)
        full.release()

        time.sleep(random.uniform(0.5, 2))  # Simulate time taken to produce

    print(f"Producer {producer_id} has finished producing.")


def consumer(consumer_id):
    for i in range(NUM_ITERATIONS):
        # Wait if buffer is empty (full semaphore)
        full.acquire()

        # Acquire mutex before modifying the shared buffer
        buffer_mutex.acquire()
        item = buffer.pop(0)
        print(f"Consumer {consumer_id} consumed item {item}. Buffer: {buffer}")
        buffer_mutex.release()

        # Signal that there is an empty slot in the buffer (release empty semaphore)
        empty.release()

        time.sleep(random.uniform(0.5, 2))  # Simulate time taken to consume

    print(f"Consumer {consumer_id} has finished consuming.")


# Create producer and consumer threads
producer_thread1 = threading.Thread(target=producer, args=(1,))
producer_thread2 = threading.Thread(target=producer, args=(2,))
consumer_thread1 = threading.Thread(target=consumer, args=(1,))
consumer_thread2 = threading.Thread(target=consumer, args=(2,))

# Start the threads
producer_thread1.start()
producer_thread2.start()
consumer_thread1.start()
consumer_thread2.start()

# Wait for all threads to complete
producer_thread1.join()
producer_thread2.join()
consumer_thread1.join()
consumer_thread2.join()

print("All producers and consumers have finished their tasks.")
