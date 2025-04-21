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

        print("Need Matrix:")
        for row in need:
            print(row)
        print("Initial Available:", work)

        while len(safe_sequence) < self.n:
            found = False
            for i in range(self.n):
                if not finish[i] and all(need[i][j] <= work[j] for j in range(self.m)):
                    print(f"Process {self.processes[i]} can be executed.")
                    for j in range(self.m):
                        work[j] += self.allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(self.processes[i])
                    found = True
                    break
            if not found:
                print("No eligible process found in this iteration.")
                return False, []
        return True, safe_sequence


# Deadlock-prone input test
processes = ["P0", "P1", "P2"]
resources = ["R0", "R1"]
available = [0, 0]

allocation = [
    [1, 0],  # P0 holds R0
    [0, 1],  # P1 holds R1
    [0, 0],  # P2 holds nothing
]

max_need = [
    [1, 1],  # P0 needs 1 more R1
    [1, 1],  # P1 needs 1 more R0
    [1, 1],  # P2 needs both
]

banker = BankersAlgorithm(processes, resources, available, max_need, allocation)
is_safe, sequence = banker.is_safe()

print("\nSafe state?:", is_safe)
print("Safe sequence:" if is_safe else "Unsafe system. Deadlock likely.")
print(sequence)
