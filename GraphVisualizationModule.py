import networkx as nx
import matplotlib.pyplot as plt

def draw_resource_allocation_graph(allocation, request, processes, resources):
    G = nx.DiGraph()

    # Add process and resource nodes
    for process in processes:
        G.add_node(process, bipartite=0, type='process')
    for resource in resources:
        G.add_node(resource, bipartite=1, type='resource')

    # Add edges for allocation and request with proper labels
    edge_labels = {}
    for i, process in enumerate(processes):
        for j, resource in enumerate(resources):
            if allocation[i][j] > 0:
                G.add_edge(resource, process)
                edge_labels[(resource, process)] = f"A:{allocation[i][j]}"
            if request[i][j] > 0:
                G.add_edge(process, resource)
                edge_labels[(process, resource)] = f"R:{request[i][j]}"

    # Positioning with bipartite layout
    pos = nx.bipartite_layout(G, nodes=[n for n in G.nodes if G.nodes[n]['bipartite'] == 0])

    # Draw the graph
    plt.figure(figsize=(10, 8))
    nx.draw_networkx_nodes(G, pos, nodelist=processes, node_color='lightblue', node_size=2000)
    nx.draw_networkx_nodes(G, pos, nodelist=resources, node_color='lightgreen', node_size=2000)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    # Draw directed edges with arrows
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black',
                           arrows=True, arrowstyle='->', arrowsize=20, connectionstyle='arc3,rad=0.1')

    # Draw edge labels
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title("Resource Allocation Graph (Directed)", fontsize=16)
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
