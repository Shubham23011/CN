import os
import uvicorn
from fastapi.security import HTTPBasic
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import matplotlib.pyplot as plt
import networkx as nx
import io
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import Contact, Info
from typing import List
from fastapi import FastAPI, Request, Form, File, UploadFile, Response,Body
import base64

from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from simulator import  EndDevice, Hub, create_star_topology, create_bus_topology,create_point_to_point_topology,create_ring_topology,create_mesh_topology

# Create a FastAPI application instance
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


app = FastAPI(
    title="Inspeq AI APIS",
    description="Inspeq AI APIS",
    version="0.1",
    contact={"name": "Inspeq AI", "email": "support@inspeq.ai"},
    openapi_url="/openapi.json",
    docs_url=None,
    redoc_url="/redoc",
    info=Info(
        title="inspeq ai",
        description="Insepeq AI APIS",
        version="1.0.0",
        contact=Contact(
            name="Inspeq AI",
            email="support@inspeq.ai",
        ),
    ),
)


security = HTTPBasic()


# Check if the DATABASE_URI variable exists in the environment

# Add DBSessionMiddleware
# app.add_middleware(DBSessionMiddleware, db_url=database_url)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def generate_network_diagram(devices, hub, topology_name):
    G = nx.Graph()

    # Add devices to the graph
    for device in devices:
        G.add_node(device.name)

    # Add connections between devices and hub
    for device in devices:
        G.add_edge(hub.name, device.name)

    # Generate the network diagram
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    plt.title(f"Network Topology: {topology_name}")
    plt.tight_layout()

    # Save the diagram to a BytesIO object
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    plt.close()
    print(img_bytes)
    return img_bytes

def create_star_topology(devices, hub_name):
    hub = Hub(hub_name)
    for device in devices:
        hub.connect_device(device)
    return hub
    

# Root route
@app.get("/docs")
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.post("/index")
async def index(request: Request, response: Response, request_body: dict = Body(...)):
    num_devices = request_body.get("num_devices")
    topology_choice = request_body.get("topology_choice")
    topology_name = request_body.get("topology_name")
    names = request_body.get("names", [])
    types = request_body.get("types", [])

    devices = []
    for i in range(num_devices):
        name = names[i]
        device_type = types[i]
        if device_type == 'EndDevice':
            devices.append(EndDevice(name))
        elif device_type == 'Hub':
            devices.append(Hub(name))

    hub = None  # Initialize hub variable

    if topology_choice == 1:
        hub = create_star_topology(devices, topology_name)
    elif topology_choice == 2:
        create_point_to_point_topology(devices)
    elif topology_choice == 3:
        hub = create_bus_topology(devices)
    elif topology_choice == 4:
        create_ring_topology(devices)
    elif topology_choice == 5:
        create_mesh_topology(devices)

    if hub:
        # Generate and save the network diagram
        diagram_bytes = generate_network_diagram(devices, hub, topology_name)
        # Send the diagram file as a response
        print(
             {
  "message": "Topology diagram generated successfully",
  "image": base64.b64encode(diagram_bytes.getvalue()).decode('utf-8')

}
        )
        return {
  "message": "Topology diagram generated successfully",
  "image": base64.b64encode(diagram_bytes.getvalue()).decode('utf-8')

}


# # Include auth routes
#  app.include_router(auth_router, prefix="/api/v1/auth", tags=["Authentication"])

# Run the application
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)