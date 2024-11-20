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

# Driver code for OPT
if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
    frame_size = 4

    print("OPT Algorithm Simulation:")
    optimal(pages, frame_size)
