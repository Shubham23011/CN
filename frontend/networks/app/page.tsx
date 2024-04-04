'use client'
import React,{useState} from "react";
import Image from "next/image";
import { getData } from "./api";
import { useEffect } from "react";

export default function Home() {
  const [url,setUrl]=useState("")
  useEffect(()=>{
    const fetchImg=async()=>{
      const response:any=await getData()
        console.log(response.image)
        setUrl(response?.image)
    }
    fetchImg()
  },[])
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
    <img src={`data:image/png;base64, ${url}`} alt="" className="w-[800px] h-[800px]" />
    </main>
  );
}
