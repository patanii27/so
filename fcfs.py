import matplotlib.pyplot as plt


# Process class
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0


# FCFS Scheduling
def fcfs_scheduling(processes):
    time = 0
    processes.sort(key=lambda x: x.arrival_time)  # Sort processes based on arrival time
    gantt_chart = []

    for p in processes:
        if time < p.arrival_time:
            time = p.arrival_time
        gantt_chart.append((p.pid, time, time + p.burst_time))  # Store process execution details in gantt chart
        time += p.burst_time
        p.completion_time = time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

    return gantt_chart


# Display Results with properly aligned columns
def display_results(processes):
    print("{:<12}{:<15}{:<15}{:<15}{:<20}{:<15}".format(
        "PID", "Arrival Time", "Burst Time", "Completion Time", "Turnaround Time", "Waiting Time"))

    total_wt = 0
    total_tat = 0
    for p in processes:
        total_wt += p.waiting_time
        total_tat += p.turnaround_time
        print("{:<12}{:<15}{:<15}{:<15}{:<20}{:<15}".format(
            p.pid, p.arrival_time, p.burst_time, p.completion_time, p.turnaround_time, p.waiting_time))

    print("\nAverage waiting time = {:.5f}".format(total_wt / len(processes)))
    print("Average turnaround time = {:.5f}".format(total_tat / len(processes)))


# Display Gantt Chart
def display_gantt_chart(gantt_chart, title):
    fig, ax = plt.subplots(figsize=(10, 2))
    for pid, start, end in gantt_chart:
        ax.barh(0, end - start, left=start, edgecolor='black', align='center')
        ax.text((start + end) / 2, 0, f'P{pid}', va='center', ha='center', color='white')
    ax.set_title(title)
    ax.set_xlabel("Time")
    ax.set_yticks([])  # Remove y-axis ticks
    plt.show()


# Driver code
if __name__ == "__main__":
    # Example processes (PID, Arrival Time, Burst Time)
    process_list = [Process(1, 0, 2),
                    Process(2, 1, 2),
                    Process(3, 5, 3),
                    Process(4, 6, 4)]

    # Apply FCFS Scheduling
    gantt_chart_fcfs = fcfs_scheduling(process_list)

    # Display Results in formatted table
    display_results(process_list)

    # Display Gantt Chart
    display_gantt_chart(gantt_chart_fcfs, "First Come First Serve")
