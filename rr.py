import matplotlib.pyplot as plt

# Function to find the waiting time for all processes
def findWaitingTime(processes, n, bt, wt, quantum, at):
    rem_bt = [0] * n
    t = 0  # Current time

    # Copy the burst time into rem_bt[]
    for i in range(n):
        rem_bt[i] = bt[i]

    gantt_chart = []  # Gantt chart to store (process, start_time, end_time)

    # Keep traversing processes in round robin manner until all of them are not done
    while True:
        done = True

        # Traverse all processes one by one repeatedly
        for i in range(n):
            if rem_bt[i] > 0 and at[i] <= t:
                done = False  # There is a pending process

                start_time = t
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - bt[i] - at[i]
                    rem_bt[i] = 0
                end_time = t
                gantt_chart.append((processes[i], start_time, end_time))

        if done:
            break

    return gantt_chart

# Function to calculate turn around time
def findTurnAroundTime(processes, n, bt, wt, tat):
    # Calculating turnaround time
    for i in range(n):
        tat[i] = bt[i] + wt[i]

# Function to calculate average waiting and turn-around times
def findavgTime(processes, n, bt, quantum, at):
    wt = [0] * n
    tat = [0] * n
    ct = [0] * n

    # Function to find waiting time of all processes
    gantt_chart = findWaitingTime(processes, n, bt, wt, quantum, at)

    # Function to find turn around time for all processes
    findTurnAroundTime(processes, n, bt, wt, tat)

    # Calculate completion time
    for i in range(n):
        ct[i] = tat[i] + at[i]

    # Display processes along with all details
    print("{:<12}{:<15}{:<15}{:<15}{:<20}{:<15}".format(
        "Processes", "Arrival Time", "Burst Time", "Waiting Time", "Turn-Around Time", "Completion Time"))
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print("{:<12}{:<15}{:<15}{:<15}{:<20}{:<15}".format(
            processes[i], at[i], bt[i], wt[i], tat[i], ct[i]))

    print("\nAverage waiting time = {:.5f}".format(total_wt / n))
    print("Average turn around time = {:.5f}".format(total_tat / n))

    # Return the Gantt chart for visualization
    return gantt_chart

# Function to print the Gantt Chart in text format
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

# Driver code
if __name__ == "__main__":
    # Process id's
    proc = [1, 2, 3]
    n = len(proc)

    # Arrival time of all processes
    arrival_time = [0, 1, 2]

    # Burst time of all processes
    burst_time = [10, 5, 8]

    # Time quantum
    quantum = 2
    gantt_chart = findavgTime(proc, n, burst_time, quantum, arrival_time)

    # Print Gantt Chart in text format
    print_gantt_chart(gantt_chart)

    # Plot Gantt Chart using matplotlib
    plot_gantt_chart(gantt_chart)
