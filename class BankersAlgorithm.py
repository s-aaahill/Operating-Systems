class BankersAlgorithm:
    def __init__(self, processes, resources, available, max_need, allocation):
        self.processes = processes
        self.resources = resources
        self.available = available
        self.max_need = max_need
        self.allocation = allocation
        self.need = [[self.max_need[i][j] - self.allocation[i][j] for j in range(len(resources))] for i in range(len(processes))]


