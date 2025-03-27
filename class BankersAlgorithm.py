class BankersAlgorithm:
    def __init__(self, processes, resources, available, max_need, allocation):
        self.processes = processes
        self.resources = resources
        self.available = available
        self.max_need = max_need
        self.allocation = allocation
        self.need = [[self.max_need[i][j] - self.allocation[i][j] for j in range(len(resources))] for i in range(len(processes))]
    def is_safe(self):
        work = self.available.copy()
        finish = [False] * len(self.processes)
        safe_sequence = []

        while True:
            found = False
            for i in range(len(self.processes)):
                if not finish[i] and all(self.need[i][j] <= work[j] for j in range(len(self.resources))):
                    work = [work[j] + self.allocation[i][j] for j in range(len(self.resources))]
                    finish[i] = True
                    safe_sequence.append(self.processes[i])
                    found = True
             if not found:
                break

        if all(finish):
            return True, safe_sequence
        else:
            return False, []
# Deadlock Detection
def detect_deadlock(allocation, request, available):
    num_processes = len(allocation)
    num_resources = len(available)
    work = available.copy()
    finish = [False] * num_processes

    while True:
        found = False
        for i in range(num_processes):
            if not finish[i] and all(request[i][j] <= work[j] for j in range(num_resources)):
                work = [work[j] + allocation[i][j] for j in range(num_resources)]
                finish[i] = True
                found = True
        if not found:
            break

    if all(finish):
        return False  # No deadlock
    else:
        return True  # Deadlock detected
# Resource Allocation Graph Visualization
def draw_resource_allocation_graph(allocation, request, processes, resources):
    G = nx.DiGraph()

    # Add nodes for processes and resources
    for process in processes:
        G.add_node(process, type='process')
    for resource in resources:
        G.add_node(resource, type='resource')

    # Add edges for allocation and request
    for i in range(len(processes)):
        for j in range(len(resources)):
            if allocation[i][j] > 0:
                G.add_edge(resources[j], processes[i])  # Resource -> Process
            if request[i][j] > 0:
                G.add_edge(processes[i], resources[j])  # Process -> Resource

    # Draw the graph
    pos = nx.spring_layout(G)
    node_colors = ['lightblue' if G.nodes[node]['type'] == 'process' else 'lightgreen' for node in G.nodes]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=3000, font_size=10, font_weight='bold')
    return G, pos


                    



