from pydantic import BaseModel
from pydantic import BaseModel
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
from fastapi import FastAPI, Request, Form, File, UploadFile, Response, Body
import base64

from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from simulator import generate_ring_topology, generate_bus_topology, generate_mesh_topology, generate_star_topology
from physical_layer import classdata, port_and_mac_assigen_to_devices
# Create a FastAPI application instance
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


app = FastAPI(
    title="Cn project",
    description="Cn project Apis",
    version="0.1",
    # contact={"name": "Inspeq AI", "email": "support@inspeq.ai"},
    openapi_url="/openapi.json",
    docs_url=None,
    redoc_url="/redoc",
    info=Info(
        title="Nit srinagar ",
        description="Cn project",
        version="1.0.0",
        contact=Contact(
            name="Inspeq AI",

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


class Item(BaseModel):
    devices_name: List[str] = []

# Root route


device = []


@app.get("/docs")
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


@app.post("/index")
async def index(type: str, devices: List[str]):
    device = devices
    devices_details = port_and_mac_assigen_to_devices(devices)
    img = base64
    if type == "star":
        img = generate_star_topology(devices)
    elif type == "bus":
        img = generate_bus_topology(devices)
    elif type == "mesh":
        img = generate_mesh_topology(devices)
    elif type == "ring":
        img = generate_ring_topology(devices)

    return {
        "message": "Topology diagram generated successfully",
        "image": img,
        "devices_details": devices_details,
    }


@app.post("/transfer_data")
async def transfer_data(sender: List[str], reciver: List[str], requestmsg: str):
   
    return classdata(reciver,sender,requestmsg)

# # Include auth routes
#  app.include_router(auth_router, prefix="/api/v1/auth", tags=["Authentication"])

# Run the application
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
