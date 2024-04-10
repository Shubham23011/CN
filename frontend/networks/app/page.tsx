'use client'
import React,{useState} from "react";
import Image from "next/image";
import { getData } from "./api";
import { useEffect } from "react";
import TagVal from './subtask/tag'
import { Button, Checkbox } from 'antd';
import MakeRequest from  './subtask/makerequest'
export default function Home() {
  const [url,setUrl]=useState<any>([])
  // const[tags,settag]=useState([])
  const[devices,setdevices]=useState("")
  const [selectedOption, setSelectedOption] = useState([]);
  const[tags,setTags] =useState([]);
  const [topo,settopo]=useState("")
 
  const onChange = (checkedValue:any) => {
    // If no option is selected, set selectedOption to null
    if (!checkedValue || checkedValue.length === 0) {
      setSelectedOption([]);
    } else {
      // If an option is selected, set selectedOption to that option
      setSelectedOption(checkedValue[0]);
      settopo(checkedValue[0])
      
    }
  };
  const handeldata=async()=>{
    // setUrl([])
    const response:any=await getData({topo,tags})
        // console.log(response.image)

        setUrl(response)
  }
  const plainOptions = ['star', 'bus', 'ring','mesh'];
  return (
    <main className="flex  flex-col items-center justify-between p-24 bg-wheat-100 space-y-20">
      <h1 className="text-black font-bold text-[40px]">Computer Networks</h1>
      <div>
        
        {/* <input type="text" onChange={(e)=>setdevices(e.target.value)}/> */}
        <TagVal tags={tags} setTags={setTags}/>
      </div>
      <Checkbox.Group options={plainOptions} onChange={onChange} value={selectedOption}>
      {plainOptions.map((option) => (
        <Checkbox key={option} value={option}>
          {option}
        </Checkbox>
      ))}
    </Checkbox.Group>
    <br />
    <Button
        className="text-black dark:bg-[#EAEAEA] mt-3 font-medium "
        style={{
          transition: "transform 0.3s",
          backgroundColor: "#EAEAEF",
        }}
        onMouseEnter={(e:any) => {
          e.target.style.color = "black";
          e.target.style.border = "none";
          e.target.style.scale = 1.01;
        }}
        onMouseLeave={(e:any) => {
          e.target.style.scale = 1;
        }}
       
         onClick={handeldata}
      >
        create topology
      </Button>
      {url?.image && <img src={`data:image/png;base64, ${url?.image}`} alt="" className="w-[400px] h-[400px]" />}
    <div>
    
    </div>
    <MakeRequest url={url}/>
    </main>
  );
}
