"use client";

import {useState} from "react";
import {api} from "@/lib/api";

export default function UploadBox({setData}:any){

const [loading,setLoading]=useState(false);

async function upload(e:any){

const file=e.target.files[0];

const formData=new FormData();

formData.append("file",file);

setLoading(true);

const res=await api.post(
"/extract",
formData
);

setData(res.data);

setLoading(false);

}


return(
<div>

<input
type="file"
accept=".pdf,image/*"
onChange={upload}
/>

{
loading &&
<p>
Generating MTO...
</p>
}

</div>
)

}