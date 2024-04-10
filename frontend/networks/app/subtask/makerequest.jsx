"use client";
import React, { useState } from "react";
import { Select, Space } from "antd";
import { Button, Checkbox } from "antd";
import { getackdata } from "../api";
const MakeRequest = ({ url }) => {
  const [sen, setSen] = useState([]);
  const [rec, setRec] = useState([]);
  const [msg, setFl] = useState("");
  const [res, setres] = useState( []);
  const devices = url?.devices_details;
  const handleChange = (value) => {
    console.log(`selected ${value}`);
    if (devices) {
      const device = devices.filter((device) => device.device_name === value);
      if (device.length > 0) {
        setSen([device[0].device_name, device[0].port_number]);
      }
    }
  };
  const handleChange1 = (value) => {
    console.log(`selected ${value}`);
    if (devices) {
      const device = devices.filter((device) => device.device_name === value);
      if (device.length > 0) {
        setRec([device[0].device_name, device[0].port_number]);
      }
    }
  };
  const handeldata = async () => {
    const req = {
      sender: sen,
      reciver: rec,
    };
    console.log(req, msg);

    const response = await getackdata({ req, msg, setRec });
    setres(response);
    console.log(response);
  };

  const { Option } = Select;
  return (
    <div className="text-black h-screen relative">
      <div>
        {" "}
        <label htmlFor="req" className="font-bold text-xl px-1">Sender:</label>
        <Select
          className="rounded-md mr-2 border-2 border-sky-500"
          defaultValue="N/A"
          style={{ width: 120 }}
          onChange={handleChange}
        >
          {url?.devices_details?.map((device, index) => (
            <Option key={index} value={device.device_name}>
              {device.device_name}
            </Option>
          ))}
        </Select>
        <input
          type="text"
          placeholder="Type message"
          onChange={(e) => setFl(e.target.value)}
          className="text-black font-bold rounded-md  h-8 px-4 border-2 border-sky-500"
        />
        <label htmlFor="req1 " className="font-bold pl-12 pr-2 text-xl">Receiver:</label>
        <Select
          defaultValue="N/A"
          style={{ width: 120 }}
          onChange={handleChange1}
          className="rounded-md mr-2 border-2 border-sky-500"
        >
          {url?.devices_details?.map((device, index) => (
            <Option key={index} value={device.device_name}>
              {device.device_name}
            </Option>
          ))}
        </Select>
        <Button
          
          style={{
            transition: "transform 0.3s",
            backgroundColor: "#EAEAEF",
          }}
          onMouseEnter={(e) => {
            e.target.style.color = "black";
            e.target.style.backgroundColor = "pink"
            e.target.style.border = "none";
            e.target.style.scale = 1.01;
          }}
          onMouseLeave={(e) => {
            e.target.style.scale = 1;
          }}
          onClick={handeldata}
        >
          Send Request
        </Button>
      </div>
      <div className="bg-red-900 text-white text-lg">
        {res.map((item, index) => (
          <div key={index}>{item}</div>
        ))}
      </div>
    </div>
  );
};

export default MakeRequest;
