# Function to simulate FIFO page replacement
def fifo(pages, frame_size):
    frame = []
    page_faults = 0
    page_hits = 0

    for page in pages:
        if page in frame:
            page_hits += 1
        else:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
            page_faults += 1

    total_accesses = len(pages)
    print(
        f"FIFO - Page Hits: {page_hits}, Page Faults: {page_faults}, Hit Ratio: {page_hits / total_accesses:.2f}, Miss Ratio: {page_faults / total_accesses:.2f}")


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


# Function to simulate OPT (Optimal) page replacement
def optimal(pages, frame_size):
    frame = []
    page_faults = 0
    page_hits = 0

    for i in range(len(pages)):
        if pages[i] in frame:
            page_hits += 1
        else:
            if len(frame) < frame_size:
                frame.append(pages[i])
            else:
                # Predict the farthest page to be used and replace it
                future_uses = []
                for page in frame:
                    if page in pages[i + 1:]:
                        future_uses.append(pages[i + 1:].index(page))
                    else:
                        future_uses.append(float('inf'))

                frame.pop(future_uses.index(max(future_uses)))
                frame.append(pages[i])
            page_faults += 1

    total_accesses = len(pages)
    print(
        f"OPT   - Page Hits: {page_hits}, Page Faults: {page_faults}, Hit Ratio: {page_hits / total_accesses:.2f}, Miss Ratio: {page_faults / total_accesses:.2f}")


# Driver code
if __name__ == "__main__":
    # Example page reference string and frame size
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frame_size = 3

    print("Page Reference String:", pages)
    print("Frame Size:", frame_size)
    print()

    # Simulate each algorithm
    fifo(pages, frame_size)
    lru(pages, frame_size)
    optimal(pages, frame_size)
