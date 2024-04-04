import axios from "axios";
const getData=async()=>{

const postData = {
    "num_devices": 5,
    "topology_choice": 1,
    "topology_name": "Star Topology",
    "names": ["Device1", "Device2", "Device3","Device4", "Device5"],
    "types": ["EndDevice", "EndDevice", "Hub","Hub","EndDevice"]
  };
  
  // Fetch POST request
  try {
    const response = await axios.post('http://localhost:8000/index', postData, {
      headers: {
        'Content-Type': 'application/json'
      }
    });

    console.log('Response:', response.data);
    return response.data
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  }
}


export  {getData}