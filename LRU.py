# Function to simulate LRU page replacement
def lru(pages, frame_size):
    frame = []
    page_faults = 0
    page_hits = 0

    for page in pages:
        if page in frame:
            page_hits += 1
            frame.remove(page)
            frame.append(page)
        else:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
            page_faults += 1

    total_accesses = len(pages)
    print(
        f"LRU  - Page Hits: {page_hits}, Page Faults: {page_faults}, Hit Ratio: {page_hits / total_accesses:.2f}, Miss Ratio: {page_faults / total_accesses:.2f}")

# Driver code for LRU
if __name__ == "__main__":
    pages = [6,  7, 8, 9, 6, 7, 1, 6, 7, 8, 9, 1, 7, 9, 6]
    frame_size = 3

    print("LRU Algorithm Simulation:")
    lru(pages, frame_size)
