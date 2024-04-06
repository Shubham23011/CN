"use client";
import React, { useEffect, useRef, useState } from "react";

import { Input, theme, Button, Tag } from "antd";
// import { toast } from "@/components/ui/use-toast";

export default function TagVal({
 setTags,tags
}) {
  const { token } = theme.useToken();

  const[tagval,settagval]=useState('')
  const [inputVisible, setInputVisible] = useState(false);
  const [inputValue, setInputValue] = useState("");
  const inputRef = useRef(null);

  useEffect(() => {
    if (inputVisible) {
      inputRef.current?.focus();
    }
  }, [inputVisible]);

  const handleClose = (removedTag) => {
    const newTags = tags.filter((tag) => tag !== removedTag);

    setTags(newTags);
  };

  const forMap = (tag) => (
    <span
      key={1}
      style={{ display: "inline-block", width: "auto", color: "black" }}
    >
      <Tag
        closable
        onClose={(e) => {
          e.preventDefault();
          handleClose(tag);
        }}
      >
        <span className="">{tag}</span>
      </Tag>
    </span>
  );

  const tagChild = tags.map(forMap);

  const tagPlusStyle = {
    background: token.colorBgContainer,
    borderStyle: "dashed",
  };
console.log(tags)
  return (
    <>
      <div style={{ marginBottom: 16 }}>{tagChild}</div>

      <div className="flex space-x-2 mt-2">
        <div className="">
          <label
            htmlFor="Project_name"
            className="block mb-2  text-black text-sm font-medium font-['DM Sans'] "
          >
            Devices
          </label>
          <Input
            type="text"
            id="Project_name"
            value={tagval}
            onChange={(e) => settagval(e.target.value)}
            className="bg-gray-50 border  border-gray-300 text-black text-sm  font-medium font-['DM Sans']    dark:bg-white-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-black "
            required={true}
            placeholder="Tag Value"
          />
        </div>
      </div>

      <Button
        className="text-black dark:bg-[#EAEAEA] mr-10 mt-3 font-medium "
        style={{
          transition: "transform 0.3s",
          backgroundColor: "#EAEAEF",
        }}
        onMouseEnter={(e) => {
          e.target.style.color = "black";
          e.target.style.border = "none";
          e.target.style.scale = 1.01;
        }}
        onMouseLeave={(e) => {
          e.target.style.scale = 1;
        }}
        onClick={() => {
          if (tagval) {
            // setreqbody((prev) => ([
            //   ...prev,
            //    tagval,
            // ]));
            // const tagpai = {
            //   key: tagkey,
            //   value: tagval,
            // };
            console.log(tagval)
            setTags((prev) => [
              ...prev,
              tagval,
            ]);

            settagval("");
          } else {
           
          }
        }}
      >
        Add Devices
      </Button>
     
    </>
  );
}