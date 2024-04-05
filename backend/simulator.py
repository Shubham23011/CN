import networkx as nx
import matplotlib.pyplot as plt
import io
import base64

def generate_ring_topology(devices:list):
    # Create a ring topology graph using NetworkX
    num_devices = len(devices)
    print(num_devices)
    G = nx.cycle_graph(num_devices)

    # Draw the graph
    pos = nx.circular_layout(G)
    nx.draw(G, pos,  with_labels=True, labels={i: device for i, device in enumerate(devices)}, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')

    # Convert the image to a base64 string
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_str = base64.b64encode(img_buffer.read()).decode('utf-8')

    return img_str

def generate_star_topology(devices):
    # Create a star topology graph using NetworkX
    num_devices = len(devices)
    print(num_devices)
    G = nx.star_graph(num_devices - 1)

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, labels={i: device for i, device in enumerate(devices)},
            node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')


    # Convert the image to a base64 string
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_str = base64.b64encode(img_buffer.read()).decode('utf-8')

    return img_str

def generate_bus_topology(devices):
    # Create a bus topology graph using NetworkX
    num_devices = len(devices)
    G = nx.path_graph(num_devices)

    # Set custom positions for nodes
    pos = {node: (node, 0) for node in G.nodes()}

    # Draw the graph with custom positions
    nx.draw(G, pos,  with_labels=True, labels={i: device for i, device in enumerate(devices)}, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')

    # Convert the image to a base64 string
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_str = base64.b64encode(img_buffer.read()).decode('utf-8')

    return img_str

def generate_mesh_topology(devices):
    # Create a mesh topology graph using NetworkX
    num_devices = len(devices)
    G = nx.complete_graph(num_devices)

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos,  with_labels=True, labels={i: device for i, device in enumerate(devices)}, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
    # Convert the image to a base64 string
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_str = base64.b64encode(img_buffer.read()).decode('utf-8')

    return img_str

# Example usage:
# devices = ["Device1", "Device2", "Device3", "Device4"]

# # Generate topologies
# ring_topology_img = generate_ring_topology(devices)
# star_topology_img = generate_star_topology(devices)
# bus_topology_img = generate_bus_topology(devices)
# mesh_topology_img = generate_mesh_topology(devices)

# Now you can use the generated image strings as needed
# For example, you can return them in a FastAPI endpoint response
