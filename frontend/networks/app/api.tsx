import axios from "axios";
const getData=async({topo,tags}:any)=>{
  const newArray = !topo.includes("ring") && !topo.includes("mesh") ? ['hub', ...tags] : tags;


console.log(topo)
  
  // Fetch POST request
  try {
    const response = await axios.post(`http://localhost:8000/index?type=${topo}`, newArray, {
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

const getackdata=async({req,msg,setRec}:any)=>{

  console.log(msg)
  // setRec([])
    // Fetch POST request
    try {
      const response = await axios.post(`http://127.0.0.1:8000/transfer_data?requestmsg=${msg}`, req, {
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
  


export  {getData,getackdata}