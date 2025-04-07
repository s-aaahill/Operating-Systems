import networkx as nx
import matplotlib.pyplot as plt

def draw_resource_allocation_graph(allocation, request, processes, resources):
    G = nx.DiGraph()

    for process in processes:
        G.add_node(process, bipartite=0, type='process')
    for resource in resources:
        G.add_node(resource, bipartite=1, type='resource')

    for i, process in enumerate(processes):
        for j, resource in enumerate(resources):
            if allocation[i][j] > 0:
                G.add_edge(resource, process, weight=allocation[i][j])
            if request[i][j] > 0:
                G.add_edge(process, resource, weight=request[i][j])

    pos = nx.bipartite_layout(G, nodes=[n for n in G.nodes if G.nodes[n]['bipartite'] == 0])

    plt.figure(figsize=(10, 8))
    nx.draw_networkx_nodes(G, pos, nodelist=processes, node_color='lightblue', node_size=2000)
    nx.draw_networkx_nodes(G, pos, nodelist=resources, node_color='lightgreen', node_size=2000)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(G, pos, width=1.5, arrowstyle='->', arrowsize=20)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.axis('off')
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
