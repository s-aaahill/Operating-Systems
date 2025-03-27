class BankersAlgorithm:
    def __init__(self, processes, resources, available, max_need, allocation):
        self.processes = processes
        self.resources = resources
        self.available = available
        self.max_need = max_need
        self.allocation = allocation
        self.need = self._calculate_need()

    def _calculate_need(self):
        # Fix loop order (i first, then j)
        return [
            [self.max_need[i][j] - self.allocation[i][j] 
            for j in range(len(self.resources))]
            for i in range(len(self.processes))
        ]

    def is_safe(self):
        work = self.available.copy()
        finish = [False] * len(self.processes)
        safe_sequence = []

        while True:
            found = False
            for i in range(len(self.processes)):
                if not finish[i] and all(self.need[i][j] <= work[j] for j in range(len(self.resources))):
                    # Allocate resources
                    work = [work[j] + self.allocation[i][j] for j in range(len(self.resources))]
                    finish[i] = True
                    safe_sequence.append(self.processes[i])
                    found = True

            if not found:
                break

        # Return True if all processes could finish, otherwise False
        return (all(finish), safe_sequence if all(finish) else [])

def detect_deadlock(allocation, request, available):
    num_processes = len(allocation)
    num_resources = len(available)
    work = available.copy()
    finish = [False] * num_processes

    while True:
        found = False
        for i in range(num_processes):
            # Fix: Check if request <= work AND request <= need
            if not finish[i] and all(request[i][j] <= work[j] for j in range(num_resources)):
                work = [work[j] + allocation[i][j] for j in range(num_resources)]
                finish[i] = True
                found = True

        if not found:
            break

    # If all processes finished, no deadlock
    return not all(finish)
