# Banker's Safety Algorithm in Python

# Function to check if the system is in a safe state
def is_safe(processes, available, max_demand, allocated, need):
    num_processes = len(processes)
    num_resources = len(available)

    # Mark all processes as not finished
    finish = [False] * num_processes
    safe_sequence = []

    # Work is a copy of available resources
    work = available[:]

    while len(safe_sequence) < num_processes:
        safe_found = False
        for p in range(num_processes):
            if not finish[p]:
                # Check if process can be satisfied with available resources
                if all(need[p][r] <= work[r] for r in range(num_resources)):
                    # If yes, pretend to allocate resources to this process
                    for r in range(num_resources):
                        work[r] += allocated[p][r]
                    safe_sequence.append(p)
                    finish[p] = True
                    safe_found = True
                    break

        if not safe_found:
            # No safe sequence found
            return False, []

    return True, safe_sequence


# Driver code
if __name__ == "__main__":
    # Number of processes and resources
    processes = [0, 1, 2, 3, 4]  # Example processes
    num_processes = len(processes)

    # Available resources (example: 3 resource types)
    available = [3, 3, 2]

    # Maximum demand of each process
    max_demand = [
        [7, 5, 3],  # P0
        [3, 2, 2],  # P1
        [9, 0, 2],  # P2
        [2, 2, 2],  # P3
        [4, 3, 3]  # P4
    ]

    # Resources currently allocated to each process
    allocated = [
        [0, 1, 0],  # P0
        [2, 0, 0],  # P1
        [3, 0, 2],  # P2
        [2, 1, 1],  # P3
        [0, 0, 2]  # P4
    ]

    # Calculate the need matrix: max_demand - allocated
    need = []
    for i in range(num_processes):
        need.append([max_demand[i][j] - allocated[i][j] for j in range(len(available))])

    # Print input details
    print("Processes:", processes)
    print("Available Resources:", available)
    print("Max Demand Matrix:", max_demand)
    print("Allocated Resources Matrix:", allocated)
    print("Need Matrix:", need)
    print()

    # Check system safety
    safe, safe_sequence = is_safe(processes, available, max_demand, allocated, need)

    if safe:
        print("System is in a safe state.")
        print("Safe sequence is:", safe_sequence)
    else:
        print("System is NOT in a safe state!")
