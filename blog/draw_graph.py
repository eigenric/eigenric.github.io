import matplotlib.pyplot as plt
import networkx as nx
import os

# Create a MultiGraph
G = nx.MultiGraph()

# Add nodes
G.add_nodes_from([1, 2, 3, 4])

# Add edges for the triangle (1, 2, 4)
G.add_edge(1, 2)
G.add_edge(2, 4)
G.add_edge(1, 4)

# Add two edges between 2 and 3
G.add_edge(2, 3, weight=1)
G.add_edge(2, 3, weight=2)

# Define positions
pos = {
    1: (0, 1),
    4: (-1, 0),
    2: (1, 0),
    3: (3, 0)
}

plt.figure(figsize=(6, 4))

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=800, node_color='#4CA1AF', edgecolors='black', linewidths=2)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=16, font_color='white', font_weight='bold')

# Draw the standard edges (the triangle)
triangle_edges = [(1, 2), (2, 4), (1, 4)]
nx.draw_networkx_edges(G, pos, edgelist=triangle_edges, width=2.5, edge_color='#2C3E50')

# Draw parallel edges manually using connection styles
# Edge 1 between 2 and 3 (curve up)
nx.draw_networkx_edges(
    G, pos,
    edgelist=[(2, 3)],
    width=2.5,
    edge_color='#2C3E50',
    connectionstyle='arc3,rad=0.3'
)
# Edge 2 between 2 and 3 (curve down)
nx.draw_networkx_edges(
    G, pos,
    edgelist=[(2, 3)],
    width=2.5,
    edge_color='#2C3E50',
    connectionstyle='arc3,rad=-0.3'
)

plt.axis('off')
plt.tight_layout()

# Save the figure
output_dir = os.path.join(os.path.dirname(__file__), 'images')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'graph.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight', transparent=True)
print(f"Graph saved successfully to {output_path}")
