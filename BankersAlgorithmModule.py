class BankersAlgorithm:
    def __init__(self, processes, resources, available, max_need, allocation):
        self.processes = processes
        self.resources = resources
        self.available = available
        self.max_need = max_need
        self.allocation = allocation
        self.n = len(processes)
        self.m = len(resources)

    def is_safe(self):
        need = [[self.max_need[i][j] - self.allocation[i][j] for j in range(self.m)] for i in range(self.n)]
        work = self.available[:]
        finish = [False] * self.n
        safe_sequence = []

        while len(safe_sequence) < self.n:
            found = False
            for i in range(self.n):
                if not finish[i] and all(need[i][j] <= work[j] for j in range(self.m)):
                    for j in range(self.m):
                        work[j] += self.allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(self.processes[i])
                    found = True
            if not found:  # No process found that can be satisfied
                return False, []
        return True, safe_sequence


def detect_deadlock(allocation, request, available):
    n = len(allocation)
    m = len(available)
    work = available[:]
    finish = [all(allocation[i][j] == 0 for j in range(m)) for i in range(n)]

    while True:
        found = False
        for i in range(n):
            if not finish[i] and all(request[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += allocation[i][j]
                finish[i] = True
                found = True
        if not found:
            break

    return not all(finish)  # Returns True if deadlock exists
