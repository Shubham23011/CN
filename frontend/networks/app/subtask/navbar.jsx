"use client";
import React,{useState} from "react";
import { Tabs } from "antd";
import { useRouter } from "next/navigation";
const Navbar = () => {
  const { push } = useRouter();
  const [tabId,setTabId]=useState(1)
  const handleTabChange = (tabId) => {
    setTabId(tabId);
    // if (tabId == 1) push("/star");
    // else if (tabId == 2) push("/bus");
    // else if (tabId == 3) push("/ring");
    // else if (tabId == 4) push("/mesh");
  };
  return (
    <Tabs
      
      tabBarStyle={{
        paddingLeft: "30px ",
        border: "2px",
        margin: "0px",
        backgroundColor: "white",
        color: "white",
        position: "fixed",
        top: "6vh",
        width: "100%",
        zIndex: "2",
      }}
      onChange={handleTabChange}
      items={[
        {
          label: "Star",
          key: "1",
        },
        {
          label: "Bus",
          key: "2",
        },
        {
          label: "Ring",
          key: "3",
        },
        {
          label: "Mesh",
          key: "4",
        },
      ]}
    />
  );
};

export default Navbar;
