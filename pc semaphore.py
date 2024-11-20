import threading
import time
import random

# Initialize buffer, semaphores, and locks
BUFFER_SIZE = 5
buffer = []

empty = threading.Semaphore(BUFFER_SIZE)  # Initially, buffer has all empty slots
full = threading.Semaphore(0)  # Initially, buffer is empty
buffer_lock = threading.Lock()

# Number of iterations for producing and consuming
NUM_ITERATIONS = 10


def producer(producer_id):
    for i in range(NUM_ITERATIONS):
        # Produce an item (simulated by a random number)
        item = random.randint(1, 100)

        # Wait if buffer is full (empty semaphores)
        empty.acquire()

        # Lock the buffer and add the produced item
        buffer_lock.acquire()
        buffer.append(item)
        print(f"Producer {producer_id} produced item {item}. Buffer: {buffer}")
        buffer_lock.release()

        # Signal that buffer has a new item (full semaphores)
        full.release()

        time.sleep(random.uniform(0.5, 2))  # Simulate variable time between productions


    print(f"Producer {producer_id} has finished producing.")


def consumer(consumer_id):
    for i in range(NUM_ITERATIONS):
        # Wait if buffer is empty (full semaphores)
        full.acquire()

        # Lock the buffer and remove the consumed item
        buffer_lock.acquire()
        item = buffer.pop(0)
        print(f"Consumer {consumer_id} consumed item {item}. Buffer: {buffer}")
        buffer_lock.release()

        # Signal that buffer has an empty slot (empty semaphores)
        empty.release()

        time.sleep(random.uniform(0.5, 2))  # Simulate variable time between consumptions

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
