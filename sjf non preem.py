import matplotlib.pyplot as plt

class Process:
    def __init__(self, pid, bt, at, prio=None):
        self.pid = pid  # Process ID
        self.bt = bt  # Burst time
        self.at = at  # Arrival time
        self.prio = prio  # Priority (only for priority-based scheduling)
        self.wt = 0  # Waiting time
        self.tat = 0  # Turnaround time
        self.ft = 0  # Finish time
        self.rt = bt  # Remaining time (for preemptive scheduling)

# Shortest Job First (Non-Preemptive)
def SJF_Non_Preemptive(processes):
    processes.sort(key=lambda x: x.at)
    current_time = 0
    gantt_chart = []
    ready_queue = []
    completed_processes = []
    while len(completed_processes) < len(processes):
        for p in processes:
            if p.at <= current_time and p not in ready_queue and p not in completed_processes:
                ready_queue.append(p)
        if ready_queue:
            ready_queue.sort(key=lambda x: x.bt)
            p = ready_queue.pop(0)
            gantt_chart.append((p.pid, current_time, current_time + p.bt))
            current_time += p.bt
            p.ft = current_time
            p.tat = p.ft - p.at
            p.wt = p.tat - p.bt
            completed_processes.append(p)
        else:
            current_time += 1
    return gantt_chart

# Function to print the Gantt Chart (text-based)
def print_gantt_chart(gantt_chart):
    print("Gantt Chart:")
    for entry in gantt_chart:
        print(f"| P{entry[0]} ", end="")
    print("|")
    for entry in gantt_chart:
        print(f"{entry[1]:<5}", end="")
    print(gantt_chart[-1][2])

# Function to plot the Gantt Chart using Matplotlib
def plot_gantt_chart(gantt_chart):
    fig, gnt = plt.subplots()
    gnt.set_ylim(0, 50)
    gnt.set_xlim(0, max([end for _, _, end in gantt_chart]))
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')
    yticks = [15 * i + 10 for i in range(len(gantt_chart))]
    gnt.set_yticks(yticks)
    gnt.set_yticklabels([f'P{entry[0]}' for entry in gantt_chart])
    for i, (pid, start_time, end_time) in enumerate(gantt_chart):
        gnt.broken_barh([(start_time, end_time - start_time)], (yticks[i] - 5, 10), facecolors=('tab:blue'))
    plt.show()

# Function to print the results with proper column alignment
def display_sjf_np_results(jobs, gantt_chart):
    print("\nShortest Job First (Non-Preemptive):")
    # Adjusted column widths to ensure proper alignment
    print(f"{'Pid':<6}{'BT':<6}{'AT':<6}{'FT':<6}{'TAT':<6}{'WT':<6}")
    for job in jobs:
        print(f"P{job.pid:<4}{job.bt:<6}{job.at:<6}{job.ft:<6}{job.tat:<6}{job.wt:<6}")
    print_gantt_chart(gantt_chart)
    plot_gantt_chart(gantt_chart)

# Example tasks for SJF Non-Preemptive
tasks_sjf_np = [
    Process(pid=1, bt=10, at=0, prio=3),
    Process(pid=2, bt=5, at=1, prio=1),
    Process(pid=3, bt=8, at=2, prio=4),
    Process(pid=4, bt=6, at=3, prio=2),
    Process(pid=5, bt=2, at=4, prio=5)
]

gantt_chart_sjf_np = SJF_Non_Preemptive(tasks_sjf_np)
display_sjf_np_results(tasks_sjf_np, gantt_chart_sjf_np)
