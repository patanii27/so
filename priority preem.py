import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_gantt_chart(processes, timeline):
    fig, gnt = plt.subplots()

    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')

    # Get all unique processes from the timeline
    unique_processes = sorted(set(p for p, _ in timeline))

    gnt.set_yticks([10 * (i + 1) for i in range(len(unique_processes))])
    gnt.set_yticklabels([f'P{pid}' for pid in unique_processes])

    gnt.set_xlim(0, max(t for _, t in timeline) + 1)
    gnt.set_ylim(0, 10 * (len(unique_processes) + 1))

    colors = ['red', 'green', 'blue', 'orange', 'purple']
    for pid, start in timeline:
        gnt.broken_barh([(start, 1)], (10 * (pid) - 5, 9), facecolors=(colors[(pid - 1) % len(colors)]))

    handles = [mpatches.Patch(color=colors[i % len(colors)], label=f'P{i + 1}') for i in range(len(unique_processes))]
    plt.legend(handles=handles)

    plt.title("Gantt Chart")
    plt.show()

def preemptive_priority(processes):
    n = len(processes)
    # Sort processes by arrival time and then by priority
    processes.sort(key=lambda x: (x[1], x[3]))

    current_time = 0
    finish_times = [0] * n
    remaining_burst = [burst for _, _, burst, _ in processes]
    timeline = []  # For Gantt chart

    while True:
        # Find the process with the highest priority that has arrived
        idx = -1
        highest_priority = float('inf')
        for i, (pid, arrival, burst, priority) in enumerate(processes):
            if arrival <= current_time and remaining_burst[i] > 0 and priority < highest_priority:
                highest_priority = priority
                idx = i

        if idx == -1:
            # If no process is ready, increment time
            current_time += 1
            continue

        # Run the selected process for 1 time unit
        remaining_burst[idx] -= 1
        timeline.append((processes[idx][0], current_time))

        if remaining_burst[idx] == 0:
            finish_times[idx] = current_time + 1

        current_time += 1

        # If the process has finished, we might need to check for others
        if remaining_burst[idx] == 0:
            for i in range(n):
                if remaining_burst[i] == 0 and finish_times[i] == 0:
                    finish_times[i] = current_time

        # Check if all processes are finished
        if all(burst == 0 for burst in remaining_burst):
            break

    # Calculate turnaround and waiting times
    turnaround_times = [finish_times[i] - processes[i][1] for i in range(n)]
    waiting_times = [turnaround_times[i] - processes[i][2] for i in range(n)]

    # Print table with proper alignment
    print("\n{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}{:<10}".format(
        "Process", "Arrival", "Burst", "Priority", "Finish", "Turnaround", "Waiting"
    ))

    for i, (pid, arrival, burst, priority) in enumerate(processes):
        print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}{:<10}".format(
            f"P{pid}", arrival, burst, priority, finish_times[i], turnaround_times[i], waiting_times[i]
        ))

    plot_gantt_chart(processes, timeline)

# Example Input
processes = [(1, 0, 4, 2), (2, 1, 3, 1), (3, 2, 1, 4), (4, 3, 2, 3)]
preemptive_priority(processes)