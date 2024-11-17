import networkx as nx
import matplotlib.pyplot as plt
# Initialize Graph with Nodes and Edges
def initialize_graph():
    graph = nx.Graph()
    edges = [
        ('A', 'B', 10), ('A', 'C', 15), ('B', 'C', 7),
        ('B', 'D', 10), ('C', 'D', 10), ('C', 'E', 20),
        ('D', 'E', 10), ('D', 'F', 5), ('E', 'F', 5)
    ]
    graph.add_weighted_edges_from(edges)
    return graph
# Compute Shortest Path Using Dijkstra's Algorithm
def dijkstra_route(graph, start, end):
    if start not in graph or end not in graph:
        return None, float('inf')
    try:
        path = nx.dijkstra_path(graph, start, end)
        path_length = nx.dijkstra_path_length(graph, start, end)
        return path, path_length
    except nx.NetworkXNoPath:
        return None, float('inf')
# Visualization Function
def visualize_route(graph, path, start, end):
    pos = nx.spring_layout(graph, seed=42)  # Consistent layout for clarity
    nx.draw(
        graph, pos, with_labels=True, node_color='lightblue',
        node_size=500, font_size=10
    )
    # Draw edge weights
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    # Highlight the shortest path in red
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)
        nx.draw_networkx_nodes(graph, pos, nodelist=[start, end], node_color='yellow', node_size=700)

    plt.title(f"Optimal Route from {start} to {end}")
    plt.show()
# Main Execution
def main():
    map_graph = initialize_graph()
    # Initial Route Calculation
    start_location, end_location = 'A', 'F'
    initial_path, initial_cost = dijkstra_route(map_graph, start_location, end_location)
    if initial_path:
        print("Initial optimal route:", initial_path)
        print("Route cost:", initial_cost)
        visualize_route(map_graph, initial_path, start_location, end_location)
    else:
        print("No path found between the specified nodes.")
    # Simulate Real-Time Update (e.g., increased traffic)
    print("\nUpdating weights (e.g., traffic conditions)...")
    map_graph['B']['D']['weight'] = 20
    # Updated Route Calculation
    updated_path, updated_cost = dijkstra_route(map_graph, start_location, end_location)
    if updated_path:
        print("Updated optimal route:", updated_path)
        print("Updated route cost:", updated_cost)
        visualize_route(map_graph, updated_path, start_location, end_location)
    else:
        print("No path found between the specified nodes.")
if __name__ == "__main__":
    main()
