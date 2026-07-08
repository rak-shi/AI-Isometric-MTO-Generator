"use client";


import {useState} from "react";

import UploadBox from "@/components/UploadBox";

import MTOTable from "@/components/MTOTable";


export default function Home(){

const [data,setData]=useState<any>();

return (

<main>

<h1>
Isometric Drawing MTO Generator
</h1>


<UploadBox setData={setData}/>


{
data &&
<>

<h2>
Material Take Off
</h2>

<MTOTable items={data.items}/>


<a href="http://127.0.0.1:8000/api/mto/csv">

<button>
Download CSV
</button>

</a>

</>

}


</main>


)

}