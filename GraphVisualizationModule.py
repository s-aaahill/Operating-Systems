import networkx as nx
import matplotlib.pyplot as plt

def draw_resource_allocation_graph(allocation, request, processes, resources):
    G = nx.DiGraph()

    # Add nodes
    for process in processes:
        G.add_node(process, bipartite=0)
    for resource in resources:
        G.add_node(resource, bipartite=1)

    # Add edges for allocation (resource → process) and request (process → resource)
    edge_labels = {}
    for i, process in enumerate(processes):
        for j, resource in enumerate(resources):
            if allocation[i][j] > 0:
                G.add_edge(resource, process)
                edge_labels[(resource, process)] = f"A:{allocation[i][j]}"
            if request[i][j] > 0:
                G.add_edge(process, resource)
                edge_labels[(process, resource)] = f"R:{request[i][j]}"

    # Position nodes in bipartite layout
    pos = nx.bipartite_layout(G, nodes=[n for n in G.nodes if n in processes])

    # Create figure
    plt.figure(figsize=(10, 8))

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, nodelist=processes, node_color='skyblue', node_size=2000)
    nx.draw_networkx_nodes(G, pos, nodelist=resources, node_color='lightgreen', node_size=2000)

    # Draw labels
    nx.draw_networkx_labels(G, pos, font_weight='bold', font_size=12)

    # Draw directed edges with visible arrows
    nx.draw_networkx_edges(
        G, pos,
        edgelist=G.edges(),
        arrowstyle='->',
        arrowsize=25,
        edge_color='black',
        connectionstyle='arc3,rad=0.1'
    )

    # Draw edge labels
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title("Directed Resource Allocation Graph", fontsize=14)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

    return G, pos

def export_graph_to_file(G, pos, file_path):
    plt.figure(figsize=(10, 8))
    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=2000)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(G, pos, width=1.5, arrowstyle='->', arrowsize=20)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.axis('off')
    plt.savefig(file_path)
    plt.close()
